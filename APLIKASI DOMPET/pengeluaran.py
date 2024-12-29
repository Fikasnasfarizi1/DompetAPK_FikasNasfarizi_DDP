import streamlit as st

st.title("Pengeluaran")

# Halaman Pengeluaran
with st.form("Pengeluaran"):
    nama = st.text_input("Nama")
    jumlah = st.number_input("jumlah (Rp.)", min_value=0)
    tanggal = st.date_input("Tanggal")
    waktu = st.time_input("Waktu")
    keterangan = st.text_input("Keterangan")
    submit_button = st.form_submit_button(label="Oke")
    if submit_button:
        st.session_state["jumlah"].append({
            "Tipe" : "Pengeluaran",
            "Nama" : nama,
            "Jumlah" : jumlah,
            "Tanggal" : tanggal,
            "Waktu" : waktu,
            "keterangan" : keterangan
        })
        st.success("Pengeluaran Berhasil")
    else:
        st.error("Pengeluaran Gagal")

# fungsi menhitung total pengeluaran
def total():
    total_pengeluaran = sum(t["Jumlah"] 
                            for t in st.session_state ["jumlah"] 
                            if t["Tipe"] == "Pengeluaran")

    return f"Total Pengeluaran anda {total_pengeluaran}"

st.write(total())