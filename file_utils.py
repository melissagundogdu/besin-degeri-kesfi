from typing import Optional, Union
import pandas as pd
import streamlit as st
from io import BytesIO, StringIO

class FileUtils:
    
    @staticmethod
    def read_csv(file_or_path: Union[BytesIO, StringIO], sep=",", encoding="utf-8") -> Optional[pd.DataFrame]:
        try:
            df = pd.read_csv(file_or_path, sep=sep, encoding=encoding)
            
            # sütun isimlerindeki boşlukları temizle
            df.columns = [str(c).strip() for c in df.columns]

            # sütunları sayısala çevir (belirli kelimeler yoksa)
            text_keywords = ['id', 'name', 'food', 'from']
            
            for col in df.columns:
                is_text = any(keyword in col.lower() for keyword in text_keywords)
                if not is_text:
                    df[col] = pd.to_numeric(df[col], errors='coerce')
                    
            return df

        except Exception as e:
            st.error(f"❌ Dosya okuma hatası: {e}")
            return None

    @staticmethod
    def download_df_as_csv(df: pd.DataFrame, filename="filtered_data.csv"):
        if df.empty:
            return
            
        csv_data = df.to_csv(index=False).encode('utf-8')
        
        st.download_button(
            label="📥 CSV İndir",
            data=csv_data,
            file_name=filename,
            mime='text/csv'
        )