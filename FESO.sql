Create database FESO;
use FESO;

Create table Pembeli (
ID_Pembeli int (12) not null auto_increment,
nama_Penuh varchar (50) not null,
nama_Pengguna varchar (50) not null,
Alamat varchar (60),
tarikh_Lahir date,
nombor_Telefon int (12),
Email varchar (30),
kata_Laluan varchar (50),
Constraint PK_Pembeli Primary Key (ID_Pembeli)
);

Create table Penjual (
ID_Kedai int (12) not null auto_increment,
nama_Penuh varchar (50) not null,
nama_Kedai varchar (40) not null,
Alamat varchar (60),
tarikh_Lahir date,
nombor_Telefon int (12),
Email varchar (30),
kata_Laluan varchar (50),
constraint PK_Penjual Primary Key (ID_Kedai)
);

Create table Produk(
ID_Produk int (12) not null auto_increment,
nama_Produk varchar (30) not null,
kategori_Produk varchar (20),
jenama_Produk varchar (20),
Harga float,
constraint PK_Produk primary key (ID_Produk)
);

Create table Pengurus (
ID_Pengurus int (12) not null auto_increment,
ID_Kedai int (12),
ID_Produk int (12),
nama_Penuh varchar (50) not null,
nombor_Telefon int (12),
Email varchar (30),
kata_Laluan varchar (50),
constraint PK_Pengurus primary key (ID_Pengurus),
FOREIGN KEY (ID_Kedai) REFERENCES Penjual(ID_Kedai),
FOREIGN KEY (ID_Produk) REFERENCES Produk(ID_Produk)
);

Create table Bank (
ID_Pengguna int (12) not null auto_increment,
ID_Pembeli int (12),
ID_Kedai int (12),
nama_Penuh varchar (50) not null,
nama_Pengguna varchar (50) not null,
nombor_Telefon int (12),
nombor_Akaun int (30),
syarikat_Bank varchar (20),
constraint PK_Bank primary key (ID_Pengguna),
FOREIGN KEY (ID_Pembeli) REFERENCES Pembeli(ID_Pembeli),
FOREIGN KEY (ID_Kedai) REFERENCES Penjual(ID_Kedai)
);

create table Troli (
ID_Troli int (12) not null auto_increment,
ID_Produk int (12),
ID_Pembeli int (12),
nama_Produk varchar (30) not null,
kategori_Produk varchar (20),
jenama_produk varchar (20),
Kuantiti int,
jumlah_Harga float,
constraint PK_Troli primary key (ID_Troli),
FOREIGN KEY (ID_Pembeli) REFERENCES Pembeli(ID_Pembeli),
FOREIGN KEY (ID_Produk) REFERENCES Produk(ID_Produk)
);

create table Pesanan (
ID_Pesanan int (12) not null auto_increment,
ID_Troli int (12),
ID_Produk int (12),
ID_Pembeli int (12),
nama_Pengguna varchar (50) not null,
Alamat varchar (60),
nama_Kedai varchar (40),
nama_Produk varchar (30) not null,
kategori_Produk varchar (20),
jenama_Produk varchar (20),
syarikat_Penghantaran varchar (20),
jumlah_Harga float,
constraint PK_Pesanan primary key (ID_Pesanan),
FOREIGN KEY (ID_Troli) REFERENCES Troli(ID_Troli),
FOREIGN KEY (ID_Pembeli) REFERENCES Pembeli(ID_Pembeli),
FOREIGN KEY (ID_Produk) REFERENCES Produk(ID_Produk)
);

Create table Sejarah_Pesanan (
ID_Pesanan int (12),
ID_Produk int (12),
ID_Pembeli int (12),
nama_Produk varchar (30) not null,
kategori_Produk varchar (20),
jenama_Produk varchar (20),
nama_Kedai varchar (40),
Kuantiti int,
FOREIGN KEY (ID_Pesanan) REFERENCES Pesanan(ID_Pesanan),
FOREIGN KEY (ID_Pembeli) REFERENCES Pembeli(ID_Pembeli),
FOREIGN KEY (ID_Produk) REFERENCES Produk(ID_Produk)
);
drop database FESO;
