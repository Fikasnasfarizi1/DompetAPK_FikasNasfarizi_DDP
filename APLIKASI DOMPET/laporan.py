import streamlit as st
import pandas as pd

st.title("Halaman Laporan Saldo Bulanan")

#Fungsi menghitung
def total():
    total_pengeluaran = sum(t["Jumlah"] 
                            for t in st.session_state ["jumlah"] 
                            if t["Tipe"] == "Pengeluaran")
    total_pemasukan = sum(t["Jumlah"] 
                            for t in st.session_state ["jumlah"] 
                            if t["Tipe"] == "Pemasukan")
 
    return total_pemasukan, total_pengeluaran


total_semua = st.session_state['jumlah']
total_pemasukan, total_pengeluaran = total()

st.metric("Total Pemasukan", f"Rp {total_pemasukan:,}")
st.metric("Total Pengeluaran", f"RP {total_pengeluaran:,}")

st.title("Riwayat Transaksi")
transaksi = st.session_state['transaksi']

if transaksi:
    df = pd.DataFrame(transaksi)
    df['jumlah'] = df['jumlah'].apply(lambda x: f"Rp {x:,}")
    df['tanggal'] = pd.to_datetime(df['tanggal'])
    st.dataframe(df[['tanggal', 'type', 'petugas', 'keterangan', 'jumlah']].sort_values(by='tanggal', ascending=False))

    with st.form("delete_form"):
        if len(transaksi) > 0:
            index_to_delete = st.number_input(
                "Masukkan indeks transaksi yang ingin dihapus", 
                min_value=0, 
                max_value=len(transaksi) - 1, 
                step=1
            )
            delete_submitted = st.form_submit_button("Hapus Transaksi")
            if delete_submitted:
                del st.session_state['transaksi'][index_to_delete]
                st.success("Transaksi berhasil dihapus!")
                # # Hanya memanggil st.experimental_rerun jika ada data yang dihapus
                # st.experimental_rerun()
            else:
                st.warning("Indeks transaksi tidak valid atau data transaksi kosong.")
else:
    st.info("Belum ada transaksi.")