import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, DataReturnMode
from sidebar_menu import show_sidebar
from file_utils import FileUtils

# sayfa config
st.set_page_config(layout="wide", page_title="Veri Keşfi & Analiz")
show_sidebar()

st.title("📊 Veri Keşfi & Analiz")

# sessiondan df'i al
df = st.session_state.get("df", None)

# df yoksa uyar ve dur
if df is None:
    st.warning("Lütfen önce 'Veri Yükleme' sayfasından bir CSV dosyası yükleyin.", icon="⚠️")
    st.stop()

st.subheader("Grafik ve Filtreleme Ayarları")

# sütunları ayır numeric ve categorical
numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
categorical_cols = df.select_dtypes(include='object').columns.tolist()

# yeterli sütun yoksa hata ver
if not numeric_cols or not categorical_cols:
    st.error("Veri setinizde analiz için yeterli sayıda sayısal ve kategorik sütun bulunmuyor.")
    st.stop()

# eksen seçimleri
col1, col2 = st.columns(2)
with col1:
    # food sütunu varsa onu seç, yoksa ilkini
    food_idx = 0
    if 'Food' in categorical_cols:
        food_idx = categorical_cols.index('Food')
    
    x_axis = st.selectbox("Kategori Ekseni (X)", categorical_cols, index=food_idx)

with col2:
    # antioxidant score varsa onu seç
    antioxidant_idx = 0
    if 'Antioxidant Score' in numeric_cols:
        antioxidant_idx = numeric_cols.index('Antioxidant Score')
        
    y_axis = st.selectbox("Değer Ekseni (Y)", numeric_cols, index=antioxidant_idx)

st.divider()

# özet istatistikler
st.subheader(f"Genel Bakış: '{y_axis}' Değerleri")
col1, col2, col3 = st.columns(3)

total_records = len(df)
mean_val = df[y_axis].mean()
max_val = df[y_axis].max()

col1.metric(f"Toplam Kayıt", f"{total_records}")
col2.metric(f"Ortalama {y_axis}", f"{mean_val:.2f}")
col3.metric(f"En Yüksek {y_axis}", f"{max_val:.2f}")

st.divider()

# aggrid tablosu
st.subheader("🔬 İnteraktif Veri Tablosu")
st.info("Bu tabloda sıralama, filtreleme yapabilir ve analiz için satırlar seçebilirsiniz.")

# grid builder ayarları
gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_selection('multiple', use_checkbox=True)
gb.configure_side_bar()
gb.configure_grid_options(domLayout='autoHeight')  # yüksekliği otomatik ayarla

gridOptions = gb.build()

# gridi oluştur
grid_response = AgGrid(
    df,
    gridOptions=gridOptions,
    width='100%',
    data_return_mode=DataReturnMode.AS_INPUT,
    update_mode=GridUpdateMode.MODEL_CHANGED,
    fit_columns_on_grid_load=True,  # sütunları sığdır
    allow_unsafe_jscode=True,
    enable_enterprise_modules=False
)

# seçili satırları al
selected_rows = grid_response['selected_rows']
selected_df = pd.DataFrame(selected_rows)

st.divider()

# seçili verilerin analizi
st.subheader("📈 Seçilen Verilerin Analizi")

if selected_df.empty:
    st.info("Grafikleri görmek için yukarıdaki tablodan en az bir satır seçin.")
else:
    st.write(f"**{len(selected_df)}** adet satır seçtiniz.")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write(f"#### '{x_axis}' ve '{y_axis}' Karşılaştırması")
        
        # bar chart oluştur
        fig_bar = px.bar(
            selected_df,
            x=x_axis,
            y=y_axis,
            color=x_axis,
            title=f"Seçilen Kayıtların {y_axis} Değerleri"
        )
        st.plotly_chart(fig_bar, use_container_width=True)
    
    with col2:
        st.write("#### Seçilen Veriler")
        
        # gereksiz sütunu temizle
        display_df = selected_df.copy()
        if '_selectedRowNodeInfo' in display_df.columns:
            display_df = display_df.drop(columns=['_selectedRowNodeInfo'])
            
        st.dataframe(display_df)
        
        # csv indirme
        FileUtils.download_df_as_csv(display_df)