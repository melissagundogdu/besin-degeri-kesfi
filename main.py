import streamlit as st
from sidebar_menu import show_sidebar
import base64 

# sayfa config
st.set_page_config(
    page_title="Antioksidan Keşifçisi",
    page_icon="🥦",
    layout="wide"
)

def get_base64_image(img_path):
    with open(img_path, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def get_bg_image_url(img_path):
    img_b64 = get_base64_image(img_path)
    return f'url(data:image/jpg;base64,{img_b64})'

def main():
    show_sidebar()
    
    bg_img = "arkaplan.jpg" 
    
    # ana sayfa html/css
    page_html = f"""
    <style>
        .main-container {{
            background-image: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), {get_bg_image_url(bg_img)};
            background-size: cover;
            background-position: center;
            padding: 5rem 2rem;
            border-radius: 10px;
            color: white;
            text-align: center;
            margin-bottom: 2rem;
        }}

        .main-container h1 {{
            font-size: 3.5rem;
            font-weight: 700;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }}

        .main-container p {{
            font-size: 1.25rem;
            max-width: 600px;
            margin: 0 auto 2rem auto;
        }}

        .steps-container {{
            display: flex;
            justify-content: center;
            gap: 2rem;
            flex-wrap: wrap;
        }}

        .step-card {{
            background-color: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 2rem;
            border-radius: 10px;
            width: 250px;
            transition: all 0.3s ease;
            backdrop-filter: blur(5px);
        }}
        
        .step-card:hover {{
            transform: translateY(-10px);
            background-color: rgba(255, 255, 255, 0.2);
        }}

        .step-card .icon {{
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }}
        
        .step-card h3 {{
            font-size: 1.5rem;
            margin-bottom: 0.5rem;
        }}
        
        .step-card p {{
            font-size: 1rem;
            color: #f0f0f0;
        }}
        
    </style>

    <div class="main-container">
        <h1>🥦 Antioksidan Keşifçisi</h1>
        <p>Veri setlerinizi interaktif deneyime dönüştürün. Gıdaların besin değerlerini keşfedin, analiz edin ve sonuçlar çıkarın.</p>
    </div>

    <h2 style="text-align:center; margin-bottom: 2rem;">Nasıl Çalışır?</h2>

    <div class="steps-container">
        <div class="step-card">
            <div class="icon">📤</div>
            <h3>1. Yükle</h3>
            <p>Sol menüden 'Veri Yükleme' sayfasına gidip CSV dosyanızı yükleyin.</p>
        </div>
        <div class="step-card">
            <div class="icon">📊</div>
            <h3>2. Keşfet</h3>
            <p>'Grafik Analizi' sayfasında tablolar ve grafiklerle verilerinizi inceleyin.</p>
        </div>
        <div class="step-card">
            <div class="icon">📥</div>
            <h3>3. Analiz & İndir</h3>
            <p>İstediğiniz verileri seçip karşılaştırmalı analiz yapın ve CSV olarak indirin.</p>
        </div>
    </div>
    """

    st.markdown(page_html, unsafe_allow_html=True)

if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError:
        st.error("Arkaplan görseli bulunamadı. `arkaplan.jpg` dosyasını kontrol edin.")