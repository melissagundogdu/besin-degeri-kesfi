import streamlit as st
from sidebar_menu import show_sidebar
from file_utils import FileUtils

# sayfa ayarları
st.set_page_config(layout="wide", page_title="Veri Yükleme")
show_sidebar()

st.title("Veri Yükleme")

# açıklama metni
st.write(
    "CSV dosyanızı yükleyin. Dosyada `Food`, `Antioxidant Score`, `Calories`, `Protein (g)` "
    "gibi sütunlar olması bekleniyor."
)

# dosya yükleyici
uploaded_file = st.file_uploader(
    "CSV dosyası seçin:",
    type=["csv"],
    help="Sadece .csv uzantılı dosyalar"
)

# dosya yüklendiyse işle
if uploaded_file is not None:
    st.info(f"Dosya: **{uploaded_file.name}**")
    
    # dosyayı oku
    df = FileUtils.read_csv(uploaded_file)
    
    if df is not None:
        st.success("✅ Dosya başarıyla yüklendi!")
        
        # session'a kaydet
        st.session_state["df"] = df
        
        # önizleme göster
        st.subheader("Veri Önizlemesi")
        st.dataframe(df.head())
        
        # bilgi mesajı
        st.info("Veri hazır. Analiz sayfasına geçebilirsiniz.")