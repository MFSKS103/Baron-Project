import streamlit as st

username = st.text_input("Masukkan Username Anda:")
email = st.text_input("Masukkan Email Anda:")
password = st.text_input("Masukkan Password Anda:", type="password")
nomor_telepon = st.text_input("Masukkan Nomor Telepon Anda:")
provinsi = st.text_input("Masukkan Provinsi Anda:")
kab_kota = st.text_input("Masukkan Kabupaten/Kota Anda:")
kec = st.text_input("Masukkan Kecamatan Anda:")
alamat = st.text_input("Masukkan Alamat Anda:")
kode_pos = st.text_input("Masukkan Kode Pos Anda:")


if st.button("Daftar"):
    if username and email and password and nomor_telepon and provinsi and kab_kota and kec and alamat and kode_pos:
        st.success(f"Berhasil Daftar sebagai {email}")
    else:
        st.error("Harap masukkan input dengan benar.")
