import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df_encoded = pd.read_csv("dashboard/main_data.csv")

def plot_heatmap(correlation_columns, title):
    correlation_matrix = df_encoded[correlation_columns].corr()
    mask = np.zeros_like(correlation_matrix, dtype=bool)
    mask[1:, 1:] = True  
    vmin, vmax = -1, 1  
    
    fig, ax = plt.subplots(figsize=(8, 5))
    
    sns.heatmap(
        correlation_matrix, annot=True, cmap="RdYlGn", fmt=".2f", linewidths=0.5, 
        mask=mask, vmin=vmin, vmax=vmax, ax=ax
    )
    
    sns.heatmap(
        correlation_matrix, annot=True, cmap="Blues", fmt=".2f", linewidths=0.5, 
        mask=~mask, alpha=0.3, cbar=False, vmin=vmin, vmax=vmax, ax=ax
    )
    
    for text in ax.texts:
        row, col = divmod(ax.texts.index(text), len(correlation_matrix.columns))
        if row != 0 and col != 0:
            text.set_color("lightgrey")
    
    plt.xticks(rotation=45, ha="right")
    plt.yticks(rotation=0)
    plt.title(title, fontsize=14, fontweight="bold", pad=10)
    st.pyplot(fig)

st.title("Dashboard Proyek Analisis Data: Air-quality-dataset")

st.markdown("<hr>", unsafe_allow_html=True)
st.subheader("Informasi Pengembang")
st.markdown("**Nama:** Muhammad Zidan Rizki Zulfazli")
st.markdown("**Email:** zidanrizki@student.ub.ac.id")
st.markdown("**ID Dicoding:** MC006D5Y1485")

st.markdown("<hr>", unsafe_allow_html=True)
st.header("Korelasi antara Tingkat Risiko Kesehatan Polusi Udara dengan Gas Penyusun Atmosfer")
st.markdown("- **Variabel yang digunakan:** SO₂, NO₂, CO, O₃, dan Tingkat Risiko Kesehatan Polusi Udara")
st.markdown("- **Tujuan:** Menganalisis korelasi antara gas atmosfer dengan tingkat risiko kesehatan polusi udara")

gas_option = st.radio("Pilih tingkat polusi:", ["Tingkat Sehat", "Tingkat Tidak Sehat"], horizontal=True, key="gas_radio")
if gas_option == "Tingkat Sehat":
    plot_heatmap(["Tingkat Polusi Sehat", "SO2", "NO2", "CO", "O3"], "Korelasi Gas Atmosfer - Sehat")
else:
    plot_heatmap(["Tingkat Polusi Tidak Sehat", "SO2", "NO2", "CO", "O3"], "Korelasi Gas Atmosfer - Tidak Sehat")
st.markdown("""
### <u>**Kesimpulan**</u> 
Gas penyusun atmosfer (**SO₂, NO₂, CO**) memiliki **korelasi positif** dengan peningkatan risiko polusi udara terhadap kesehatan, sedangkan **O₃** menunjukkan tren sebaliknya.  
Ini mengindikasikan bahwa semakin tinggi konsentrasi **SO₂, NO₂, dan CO**, semakin buruk dampaknya bagi kesehatan, sementara meningkatnya konsentrasi **O₃** justru menunjukkan udara yang lebih sehat.
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.header("Korelasi antara Tingkat Risiko Kesehatan Polusi Udara dengan Faktor Cuaca (Suhu, Kelembaban, Tekanan Udara, dan Curah Hujan)")
st.markdown("- **Variabel yang digunakan:** Suhu Udara (TEMP), Titik Embun (DEWP), Tekanan Udara (PRES), dan Curah Hujan (RAIN), dan Tingkat Risiko Kesehatan polusi Udara")
st.markdown("- **Tujuan:** Menganalisis bagaimana faktor cuaca mempengaruhi risiko kesehatan akibat polusi udara")

weather_option = st.radio("Pilih tingkat polusi:", ["Tingkat Sehat", "Tingkat Tidak Sehat"], horizontal=True, key="weather_radio")
if weather_option == "Tingkat Sehat":
    plot_heatmap(["Tingkat Polusi Sehat", "TEMP", "DEWP", "PRES", "RAIN"], "Korelasi Faktor Cuaca - Sehat")
else:
    plot_heatmap(["Tingkat Polusi Tidak Sehat", "TEMP", "DEWP", "PRES", "RAIN"], "Korelasi Faktor Cuaca - Tidak Sehat")
st.markdown("""
### <u>**Kesimpulan**</u>
Berdasarkan hasil analisis korelasi menggunakan **Heatmap**, **suhu, kelembaban (titik embun), tekanan udara, dan curah hujan** tidak memiliki **korelasi yang signifikan** terhadap tingkat risiko kesehatan polusi udara.  
Hal ini menunjukkan bahwa faktor-faktor cuaca tersebut hanya memiliki **pengaruh minimal** terhadap kualitas udara yang berdampak pada kesehatan.
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
## **Terima Kasih 😊**
""")
