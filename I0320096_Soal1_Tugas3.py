print("===Daftar Nama Teman===")
Nama_teman = ["Raysa","Sasa","Funny","Rara","Ryan","Ervizal","Alvin","Rafli","Yolanda","Sekar"]
print(Nama_teman)
#Menampilkan list index
print("Nama teman pada indeks ke 2,5,6 :", Nama_teman[4], Nama_teman[6], Nama_teman[7])
#Mengganti Nama Teman
Nama_teman[3] = "Hani"
Nama_teman[5] = "Hana"
Nama_teman[9] = "Diva"
#Menambah Nama Teman
Nama_teman.extend(["Maurich", "Ano"])
print(Nama_teman * 3)
print(len(Nama_teman))