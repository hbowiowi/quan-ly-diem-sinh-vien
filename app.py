
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. CAU HINH TRANG WEB
st.set_page_config(
    page_title="Quan ly diem sinh vien",
    page_icon="📚",
    layout="wide"
)

# 2. DU LIEU 10 SINH VIEN
data = {
    "Ho_ten": [
        "Nguyen Van An",
        "Tran Thi Binh",
        "Le Minh Chau",
        "Pham Quoc Dat",
        "Hoang Thu Ha",
        "Vu Duc Huy",
        "Do Ngoc Lan",
        "Bui Thanh Nam",
        "Dang My Phuong",
        "Ngo Tuan Kiet"
    ],
    "Chuyen_can": [9, 8, 10, 6, 8, 7, 9, 5, 10, 6],
    "Giua_ky": [8, 7, 9, 5, 7, 6, 8, 4, 9, 6],
    "Cuoi_ky": [9, 8, 9, 4, 8, 7, 9, 5, 10, 6]
}

df = pd.DataFrame(data)

# 3. TINH DIEM TONG KET
df["Tong_ket"] = (
    0.2 * df["Chuyen_can"]
    + 0.3 * df["Giua_ky"]
    + 0.5 * df["Cuoi_ky"]
).round(2)

# 4. XEP LOAI
def xep_loai(diem):
    if diem >= 8.5:
        return "Gioi"
    elif diem >= 7:
        return "Kha"
    elif diem >= 5:
        return "Trung binh"
    return "Yeu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# 5. GIAO DIEN WEBSITE
st.title("QUAN LY DIEM SINH VIEN")
st.write(
    "Bang diem, thong ke va ket qua hoc tap "
    "cua 10 sinh vien."
)

# Doi ten cot de hien thi tren web
bang_hien_thi = df.rename(columns={
    "Ho_ten": "Ho ten",
    "Chuyen_can": "Chuyen can",
    "Giua_ky": "Giua ky",
    "Cuoi_ky": "Cuoi ky",
    "Tong_ket": "Tong ket",
    "Xep_loai": "Xep loai"
})

st.subheader("1. Bang diem sinh vien")
st.dataframe(bang_hien_thi, hide_index=True)

# 6. THONG KE
diem_tb = df["Tong_ket"].mean()
diem_max = df["Tong_ket"].max()
diem_min = df["Tong_ket"].min()
so_dat = int((df["Tong_ket"] >= 5).sum())

sv_max = df[df["Tong_ket"] == diem_max]["Ho_ten"].tolist()
sv_min = df[df["Tong_ket"] == diem_min]["Ho_ten"].tolist()

st.subheader("2. Thong ke ket qua")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Diem trung binh", f"{diem_tb:.2f}")
c2.metric("Diem cao nhat", f"{diem_max:.2f}")
c3.metric("Diem thap nhat", f"{diem_min:.2f}")
c4.metric("So sinh vien dat", f"{so_dat}/10")

st.write("Sinh vien co diem cao nhat:", ", ".join(sv_max))
st.write("Sinh vien co diem thap nhat:", ", ".join(sv_min))

# 7. CHON SINH VIEN
st.subheader("3. Tra cuu theo sinh vien")

ten_sv = st.selectbox(
    "Hay chon mot sinh vien:",
    df["Ho_ten"].tolist()
)

sv = df[df["Ho_ten"] == ten_sv].iloc[0]

st.write("Ho ten:", sv["Ho_ten"])
st.write("Diem chuyen can:", sv["Chuyen_can"])
st.write("Diem giua ky:", sv["Giua_ky"])
st.write("Diem cuoi ky:", sv["Cuoi_ky"])
st.write("Diem tong ket:", f"{sv['Tong_ket']:.2f}")
st.write("Xep loai:", sv["Xep_loai"])

# 8. BIEU DO COT
st.subheader("4. Bieu do diem tong ket")

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(df["Ho_ten"], df["Tong_ket"])
ax.set_title("Diem tong ket cua 10 sinh vien")
ax.set_xlabel("Ho ten sinh vien")
ax.set_ylabel("Diem tong ket")
ax.set_ylim(0, 10)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

st.pyplot(fig)
plt.close(fig)

# 9. THONG TIN NGUOI TAO
st.divider()
st.caption("Nguoi tao: [HOÀNG NGỌC BÍCH] | "
           "MSSV: [002308007779]")
