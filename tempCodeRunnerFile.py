import streamlit as st
from sidebar_menu import show_sidebar

def main():
    st.set_page_config(page_title="Antioksidan Keşifçisi", page_icon="🥦", layout="wide")
    show_sidebar()

    st.title("🏠 Ana Sayfa")
    st.write("**Veri yükle** → **Grafik sayfasında görselleştir** → **seç ve indir**")

    # adımlar
    c1, c2, c3 = st.columns(3)
    c1.metric("Adım", "1", "Yükle")
    c2.metric("Adım", "2", "Keşfet") 
    c3.metric("Adım", "3", "İndir")

    st.divider()
    st.subheader("📋 Örnek CSV")
    st.code(
        "food,region,antioxidant\n"
        "Pomegranate,Middle East,420\n"
        "Olive,Middle East,210\n"
        "Blueberry,Americas,380\n",
        language="csv"
    )

if __name__ == "__main__":
    main()