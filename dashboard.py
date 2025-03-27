import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.set_page_config(page_title='Bike Sharing Dashboard', layout='wide')
st.title('🚲 Bike Sharing Dashboard')
st.write('Dashboard ini menyajikan hasil analisis data penyewaan sepeda harian.')

# Load Data
@st.cache_data
def load_data():
    path = r'C:\Users\Ferdy Luqman\Downloads\bike_sharing_project\dashboard\day_clean.csv'
    df = pd.read_csv(path)
    return df

df = load_data()

# Sidebar
st.sidebar.title('Menu')
selected = st.sidebar.radio('Pilih Visualisasi:', [
    'Tren Penyewaan Harian',
    'Rata-rata Penyewaan per Musim'
])

# Visualisasi 1: Tren Penyewaan Harian
if selected == 'Tren Penyewaan Harian':
    st.subheader('📈 Tren Penyewaan Sepeda Harian')

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(pd.to_datetime(df['dteday']), df['cnt'], color='tab:blue')
    ax.set_xlabel('Tanggal')
    ax.set_ylabel('Jumlah Penyewaan')
    ax.set_title('Tren Penyewaan Sepeda Harian')
    plt.xticks(rotation=45)

    st.pyplot(fig)

    st.markdown("""
    **Insight:**  
    Dari grafik ini terlihat adanya tren musiman. Jumlah penyewaan cenderung meningkat pada musim panas dan gugur, lalu menurun saat musim dingin.
    """)

# Visualisasi 2: Rata-rata Penyewaan per Musim
elif selected == 'Rata-rata Penyewaan per Musim':
    st.subheader('🌤️ Rata-rata Penyewaan Berdasarkan Musim')

    season_labels = {
        1: 'Spring',
        2: 'Summer',
        3: 'Fall',
        4: 'Winter'
    }
    df['season_name'] = df['season'].map(season_labels)

    season_avg = df.groupby('season_name')['cnt'].mean().reset_index()

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(season_avg['season_name'], season_avg['cnt'], color='tab:green')
    ax.set_xlabel('Musim')
    ax.set_ylabel('Rata-rata Penyewaan')
    ax.set_title('Rata-rata Penyewaan Sepeda per Musim')

    st.pyplot(fig)

    st.markdown("""
    **Insight:**  
    Musim gugur dan musim panas memiliki rata-rata jumlah penyewaan sepeda paling tinggi. Hal ini bisa menjadi pertimbangan untuk strategi bisnis atau promosi saat musim tersebut.
    """)

# Footer
st.sidebar.markdown('---')
st.sidebar.caption('© 2025 Ferdy Luqman')
