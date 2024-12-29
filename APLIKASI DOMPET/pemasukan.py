import streamlit as st

st.title("Pemasukan")

# Pemasukan Per-Hari
with st.form("Pemasukan"):
    nama = st.text_input("Nama")
    jumlah = st.number_input("Jumlah (Rp.)", min_value=0)
    tanggal = st.date_input("Tanggal")
    waktu = st.time_input("Waktu")
    keterangan = st.text_input("Keterangan")
    submit_button = st.form_submit_button(label="Oke")
    if submit_button:
        st.session_state["jumlah"].append({
            "Tipe" : "Pemasukan",
            "Nama" : nama,
            "Jumlah" : jumlah,
            "Keterangan": keterangan,
            "Tanggal": tanggal,
            "Waktu": waktu
        })

        st.success("Pemasukan berhasil ditambahkan")
    else:
        st.error("Pemasukan gagal ditambahkan")

# Fungsi Untuk Menghitung

def total():
    total_pemasukan = sum(t["Jumlah"] 
                          for t in st.session_state ["jumlah"] 
                          if t["Tipe"] == "Pemasukan")
    return f"Total Pemasukan Anda {total_pemasukan}"

st.write(total())