import sqlite3

conn = sqlite3.connect("lab4.db")
cursor = conn.cursor()

# Xóa bảng nếu tồn tại
cursor.execute("DROP TABLE IF EXISTS ChiTietHD")

# Tạo bảng
cursor.execute("""
CREATE TABLE ChiTietHD (
    ma_ct INTEGER PRIMARY KEY,
    ten_san_pham TEXT,
    so_luong INTEGER,
    gia REAL
)
""")

# Thêm dữ liệu
cursor.execute("""
INSERT INTO ChiTietHD (ma_ct, ten_san_pham, so_luong, gia)
VALUES (1, 'Ao thun', 2, 150000)
""")

conn.commit()
conn.close()

print("OK!")