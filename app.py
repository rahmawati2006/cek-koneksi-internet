import streamlit as st

rules = [
    (["jarak"], "sinyal"),
    (["pengguna"], "bandwidth"),
    (["sinyal", "bandwidth"], "lambat"),
    (["cuaca"], "gangguan"),
    (["lambat"], "buruk"),
    (["gangguan"], "buruk"),
]


def forward_chaining(facts):
    inferred = facts.copy()
    langkah = []
    changed = True

    while changed:
        changed = False
        for kondisi, hasil in rules:
            if all(k in inferred for k in kondisi) and hasil not in inferred:
                langkah.append(f"{' + '.join(kondisi)} → {hasil}")
                inferred.append(hasil)
                changed = True

    return inferred, langkah


st.title("Cek Koneksi Internet")
st.caption("Sistem pakar sederhana dengan metode forward chaining")

jarak = st.selectbox("Jarak ke router", ["dekat", "jauh"])
pengguna = st.selectbox("Jumlah pengguna", ["sedikit", "banyak"])
cuaca = st.selectbox("Cuaca", ["cerah", "buruk"])

if st.button("Cek Koneksi"):
    facts = []
    if jarak == "jauh":
        facts.append("jarak")
    if pengguna == "banyak":
        facts.append("pengguna")
    if cuaca == "buruk":
        facts.append("cuaca")

    hasil, langkah = forward_chaining(facts)

    st.subheader("Proses inferensi")
    if langkah:
        for i, l in enumerate(langkah, 1):
            st.write(f"{i}. {l}")
    else:
        st.write("Tidak ada aturan yang terpenuhi.")

    st.write("Fakta awal:", facts if facts else "-")
    st.write("Hasil inferensi:", hasil)

    if "buruk" in hasil:
        st.error("Kesimpulan: Koneksi BURUK")
    else:
        st.success("Kesimpulan: Koneksi NORMAL")
