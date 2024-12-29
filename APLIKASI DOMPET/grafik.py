import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Judul halaman
st.title("Grafik Pemasukan dan Pengeluaran")

# Data dummy untuk grafik
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
pemasukan = np.random.randint(1000, 5000, 12)
pengeluaran = np.random.randint(500, 3000, 12)

# Grafik pemasukan vs pengeluaran per bulan
fig, ax = plt.subplots()
ax.plot(months, pemasukan, label="Pemasukan", color="green")
ax.plot(months, pengeluaran, label="Pengeluaran", color="red")
ax.set_xlabel("Bulan")
ax.set_ylabel("jumlah")
ax.set_title("Pemasukan dan Pengeluaran per Bulan")
ax.legend()

# Menampilkan grafik
st.pyplot(fig)

# Grafik tahunan
tahun = [2020, 2021, 2022]
pemasukan_tahun = [30000, 35000, 40000]
pengeluaran_tahun = [20000, 22000, 24000]

fig, ax = plt.subplots()
ax.bar(tahun, pemasukan_tahun, width=0.4, label="Pemasukan", color="green", align='center')
ax.bar(tahun, pengeluaran_tahun, width=0.4, label="Pengeluaran", color="red", align='edge')
ax.set_xlabel("Tahun")
ax.set_ylabel("jumlah")
ax.set_title("Pemasukan dan Pengeluaran per Tahun")
ax.legend()

# Menampilkan grafik tahunan
st.pyplot(fig)
