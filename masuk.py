import streamlit as st

email = st.text_input("Masukkan Email Anda:")

# Input untuk Password
password = st.text_input("Masukkan Password Anda:", type="password")

# Tombol Login
if st.button("Login"):
    if email and password:
        st.success(f"Berhasil login sebagai {email}")
    else:
        st.error("Harap masukkan email dan password dengan benar.")


st.write("[Lupa Password atau Email](https://www.google.com/search?gs_ssp=eJzj4tTP1TcwMU02T1JgNGB0YPBiS8_PT89JBQBASQXT&q=google&oq=goo&gs_lcrp=EgZjaHJvbWUqGAgBEC4YQxiDARjHARixAxjRAxiABBiKBTIMCAAQIxgnGIAEGIoFMhgIARAuGEMYgwEYxwEYsQMY0QMYgAQYigUyBggCEEUYOTIKCAMQABixAxiABDIKCAQQABixAxiABDIGCAUQRRg8MgYIBhBFGDwyBggHEEUYPNIBCDMzMDNqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8)")
