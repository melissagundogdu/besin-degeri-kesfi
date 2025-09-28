import streamlit as st

def show_sidebar():
    with st.sidebar:
        st.markdown("### 🍎 Besin Değeri Analiz Aracı")
        st.write("Verilerinizi interaktif analiz edin.")
        st.divider()
        
        if st.button("🏠 Ana Sayfa", use_container_width=True):
            st.switch_page("main.py")
            
        if st.button("📤 Veri Yükleme", use_container_width=True):
            st.switch_page("pages/1_data_upload.py")
        
        # veri yüklendiyse butonu vurgula    
        btn_type = "primary" if "df" in st.session_state else "secondary"
        if st.button("📊 Veri Analizi", use_container_width=True, type=btn_type):
            st.switch_page("pages/2_explorer.py")

        st.divider()
        st.info("Streamlit ve AgGrid ile veri analizi demo projesi.")