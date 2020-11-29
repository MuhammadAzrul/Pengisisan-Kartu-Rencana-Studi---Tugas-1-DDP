print("Fitur Pengisian Rencana Studi")
jum_sks=0
nim = input("Masukkan NIM: ") #Program meminta input NIM
#Seleksi Tahun Keberapa NIM anda
if nim[5:7]=='20':
    max_sks = 20
    print("Anda mahasiswa tahun pertama. Anda bisa mengambil paling banyak 20 SKS.\n")
    print("Jumlah SKS yang diambil: ", jum_sks)
    while True:
        if jum_sks < max_sks: #Jika Jumlah SKS lebih Kecil dibandingkan Maksimal SKS maka program akan menanyakan mata kuliah yang ingin diambil
            sks = input("Masukkan nama mata kuliah yang diambil atau X untuk berhenti: ")
            if sks == 'X' or sks == 'x': #Jika input program adalah x maka program akan berhenti
                print("Pengisian rencana Studi selesai")
                break
            else: #jika input program selain dari x maka program akan meminta inputan mata kuliah tersebut
                bebmat = eval(input("Masukkan Beban SKS Mata Kuliah tersebut: ")) #program akan meminta beban mata kuliah
                jum_sks = jum_sks + bebmat #jumlah mata kuliah akan diakumulasikan dengan beban mata kuliah
                print("Berhasil Mengambil mata kuliah", sks, "dengan bobot", bebmat, "SKS") #program menampilan mata kuliah yang diambil dan bobot mata kuliah yang diambil
                print("Jumlah SKS yang diambil: ", jum_sks, "\n") #program akan menampilkan banyaknya bobot sks yang sudah diambil
        elif jum_sks == max_sks: #jika jumlah sks sudah mencapai batas maksimum maka program akan menampilkan jumlah sks dan memberhentikan program
            print("Jumlah SKS yang anda adalah", jum_sks)
            print("Program Berhenti")
            break
        else: #jika jumlah bobot sks melebihi bobotnya maka program akan menampilkan jumlah sks dan memberi tahu bahwa jumlah sks melebih batas
            print("Jumlah SKS yang diambil: ", jum_sks)
            print("Penambilan SKS Telah melibihi batas")
            print("Penghitungan Selesai")
            break
elif nim[5:7]=='19':
    max_sks = 22
    print("Anda mahasiswa tahun kedua. Anda bisa mengambil paling banyak 22 SKS.\n")
    print("Jumlah SKS yang diambil: ", jum_sks)
    while True:
        if jum_sks < max_sks: #Jika Jumlah SKS lebih Kecil dibandingkan Maksimal SKS maka program akan menanyakan mata kuliah yang ingin diambil
            sks = input("Masukkan nama mata kuliah yang diambil atau X untuk berhenti: ")
            if sks == 'X' or sks == 'x': #Jika input program adalah x maka program akan berhenti
                print("Pengisian rencana Studi selesai")
                break
            else: #jika input program selain dari x maka program akan meminta inputan mata kuliah tersebut
                bebmat = eval(input("Masukkan Beban SKS Mata Kuliah tersebut: ")) #program akan meminta beban mata kuliah
                jum_sks = jum_sks + bebmat #jumlah mata kuliah akan diakumulasikan dengan beban mata kuliah
                print("Berhasil Mengambil mata kuliah", sks, "dengan bobot", bebmat, "SKS") #program menampilan mata kuliah yang diambil dan bobot mata kuliah yang diambil
                print("Jumlah SKS yang diambil: ", jum_sks, "\n") #program akan menampilkan banyaknya bobot sks yang sudah diambil
        elif jum_sks == max_sks: #jika jumlah sks sudah mencapai batas maksimum maka program akan menampilkan jumlah sks dan memberhentikan program
            print("Jumlah SKS yang anda adalah", jum_sks)
            print("Program Berhenti")
            break
        else: #jika jumlah bobot sks melebihi bobotnya maka program akan menampilkan jumlah sks dan memberi tahu bahwa jumlah sks melebih batas
            print("Jumlah SKS yang anda adalah", jum_sks)
            print("Penambilan SKS Telah melibihi batas")
            print("Penghitungan Selesai")
            break
elif nim[5:7]=='18':
    max_sks = 24
    print("Anda mahasiswa tahun ketiga. Anda bisa mengambil paling banyak 24 SKS.\n")
    print("Jumlah SKS yang diambil: ", jum_sks)
    while True:
        if jum_sks < max_sks: #Jika Jumlah SKS lebih Kecil dibandingkan Maksimal SKS maka program akan menanyakan mata kuliah yang ingin diambil
            sks = input("Masukkan nama mata kuliah yang diambil atau X untuk berhenti: ")
            if sks == 'X' or sks == 'x': #Jika input program adalah x maka program akan berhenti
                print("Pengisian rencana Studi selesai")
                break
            else: #jika input program selain dari x maka program akan meminta inputan mata kuliah tersebut
                bebmat = eval(input("Masukkan Beban SKS Mata Kuliah tersebut: ")) #program akan meminta beban mata kuliah
                jum_sks = jum_sks + bebmat #jumlah mata kuliah akan diakumulasikan dengan beban mata kuliah
                print("Berhasil Mengambil mata kuliah", sks, "dengan bobot", bebmat, "SKS") #program menampilan mata kuliah yang diambil dan bobot mata kuliah yang diambil
                print("Jumlah SKS yang diambil: ", jum_sks, "\n") #program akan menampilkan banyaknya bobot sks yang sudah diambil
        elif jum_sks == max_sks: #jika jumlah sks sudah mencapai batas maksimum maka program akan menampilkan jumlah sks dan memberhentikan program
            print("Jumlah SKS yang anda adalah", jum_sks)
            print("Program Berhenti")
            break
        else: #jika jumlah bobot sks melebihi bobotnya maka program akan menampilkan jumlah sks dan memberi tahu bahwa jumlah sks melebih batas
            print("Jumlah SKS yang diambil: ", jum_sks)
            print("Penambilan SKS Telah melibihi batas")
            print("Penghitungan Selesai")
            break
elif nim[5:7]=='17':
    max_sks = 26
    print("Anda mahasiswa tahun keempat. Anda bisa mengambil paling banyak 26 SKS.\n")
    print("Jumlah SKS yang diambil: ", jum_sks)
    while True:
        if jum_sks < max_sks: #Jika Jumlah SKS lebih Kecil dibandingkan Maksimal SKS maka program akan menanyakan mata kuliah yang ingin diambil
            sks = input("Masukkan nama mata kuliah yang diambil atau X untuk berhenti: ")
            if sks == 'X' or sks == 'x': #Jika input program adalah x maka program akan berhenti
                print("Pengisian rencana Studi selesai")
                break
            else: #jika input program selain dari x maka program akan meminta inputan mata kuliah tersebut
                bebmat = eval(input("Masukkan Beban SKS Mata Kuliah tersebut: ")) #program akan meminta beban mata kuliah
                jum_sks = jum_sks + bebmat #jumlah mata kuliah akan diakumulasikan dengan beban mata kuliah
                print("Berhasil Mengambil mata kuliah", sks, "dengan bobot", bebmat, "SKS") #program menampilan mata kuliah yang diambil dan bobot mata kuliah yang diambil
                print("Jumlah SKS yang diambil: ", jum_sks, "\n") #program akan menampilkan banyaknya bobot sks yang sudah diambil
        elif jum_sks == max_sks: #jika jumlah sks sudah mencapai batas maksimum maka program akan menampilkan jumlah sks dan memberhentikan program
            print("Jumlah SKS yang anda adalah", jum_sks)
            print("Program Berhenti")
            break
        else: #jika jumlah bobot sks melebihi bobotnya maka program akan menampilkan jumlah sks dan memberi tahu bahwa jumlah sks melebih batas
            print("Jumlah SKS yang diambil: ", jum_sks)
            print("Penambilan SKS Telah melibihi batas")
            print("Penghitungan Selesai")
            break
else:
    print("NIM yang anda masukkan salah") #jika nim yang di masukan salah