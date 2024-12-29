import streamlit as st

# Menampilkan judul aplikasi
st.title("Aplikasi Manajemen Keuangan Pribadi")

st.markdown(
    """
    <style>
    /* Warna latar belakang aplikasi */
    .stApp {
        background-color: #ffff;
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #3498db;
        color: white;
        padding: 5px;
    }

    /* Teks pada sidebar */
    [data-testid="stSidebar"] * {
        color: white !important;
        font-size: 16px;
        margin-bottom: 5px;
        margin-top: 5px;
    }

    [data-testid="stSidebar"] *:hover {
        color: #ecf0f1 !important;
    }

    /* Header bar styling */
    header[data-testid="stHeader"] {
        background-color: #3498db;
        color: white;
        padding: 5px;
        
    }

    header[data-testid="stHeader"] h1 {
        color: white;
        font-size: 10px;
    }

    .stButton > button:hover {
        background-color: #2980b9;
        color: #ecf0f1;
    }

    /* Custom title style for Kas Masjid */
    .sidebar-title {
        font-size: 20px;
        font-weight: bold;
        color: #ffffff;
        margin-bottom: 20px;
        text-align: center;
    }
    
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar navigasi
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman", ["Dashboard", "Pemasukan", "Pengeluaran", "Grafik", "Laporan"])

# Arahkan ke halaman sesuai pilihan
if page == "Pemasukan":
    import pemasukan
elif page == "Pengeluaran":
    import pengeluaran
elif page == "Grafik":
    import grafik
elif page == "Laporan":
    import laporan
else:
    st.write("Selamat datang di aplikasi manajemen keuangan pribadi. Silakan pilih halaman di sidebar.")

if 'jumlah' not in st.session_state:
    st.session_state['jumlah']=[]
