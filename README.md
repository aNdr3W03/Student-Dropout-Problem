# Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding

Jaya Jaya Institute adalah sebuah lembaga pendidikan tinggi yang telah berdiri sejak tahun 2000 dan berhasil menghasilkan banyak lulusan dengan reputasi yang sangat baik. Namun, terdapat sejumlah siswa yang tidak menyelesaikan pendidikan mereka atau mengalami dropout. Tingginya angka dropout ini menjadi tantangan besar bagi institusi pendidikan. Untuk mengatasi hal tersebut, Jaya Jaya Institut berupaya mendeteksi siswa yang berpotensi mengalami dropout lebih awal, sehingga dapat memberikan bimbingan khusus kepada mereka.

### Business Problem

**Jaya Jaya Institute menghadapi tantangan tingginya angka dropout siswa, yang berpotensi merusak reputasi atau akreditasi institusi dan mengurangi kepercayaan masyarakat terhadap kualitas pendidikan yang ditawarkan**. Ketidakmampuan untuk mendeteksi siswa yang berisiko dropout secara dini menghambat upaya pencegahan dan pemberian bimbingan khusus, sehingga mengancam keberlangsungan dan daya saing institusi di tengah kompetisi dunia pendidikan yang semakin ketat.

**Untuk mengatasi masalah tersebut, penting untuk dapat mengidentifikasi dan memprediksi siswa yang berpotensi dropout sedini mungkin** agar institusi dapat memberikan intervensi yang tepat untuk meningkatkan tingkat kelulusan.

### Project Scope

- Data preparation dan data cleaning awal
- Exploratory Data Analysis (EDA) untuk mencari tahu faktor penyebab tingkat dropout yang tinggi melalui visualisasi data
- Membuat business dashboard dari faktor penyebab tingginya tingkat dropout
- Mengembangkan model machine learning untuk memprediksi status siswa berdasarkan variabel-variabel faktor penyebab tingginya dropout
- Deployment model machine learning untuk dapat digunakan dalam memprediksi status siswa dropout atau lulus

### Preparation

**Data source:**
- [Students' Performance data](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance 'Dicoding GitHub - Students Performance data')
- [Predict Students' Dropout and Academic Success](https://doi.org/10.24432/C5MC89 'UCI Machine Learning - Predict Students Dropout and Academic Success')

**Setup environment:**

1. Clone this Repository
   ```bash
   git clone https://github.com/aNdr3W03/Student-Dropout-Problem.git
   ```

2. Create Python Virtual Environment
   ```bash
   virtualenv venv
   ```

2. Activate the Environment
   ```bash
   venv\Scripts\activate
   ```

4. Install All the Requirements Inside "requirements.txt"
   ```bash
   pip install -r requirements.txt
   ```

## Business Dashboard

[Jaya Jaya Institute Students Dashboard](https://public.tableau.com/shared/HX5QWTBF4 'Tableau Public - Jaya Jaya Institute Students Dashboard'), dirancang secara optimal untuk menyediakan insight bagi para pengajar dan pihak internal institusi mengenai tingkat siswa dropout yang mencapai lebih dari 30%. Dashboard ini juga dibuat dengan visualisasi dan pilihan warna yang ramah bagi individu dengan gangguan penglihatan warna (color blind) untuk meningkatkan aksesibilitas inklusif.

![Jaya Jaya Maju Employees Dashboard](https://github.com/user-attachments/assets/cc514db7-03a7-4905-916d-ef707c0738dc 'Jaya Jaya Institute Students Dashboard')

Pada dashboard ini, terdapat 3 bagian, sisi kiri adalah pie chart tentang summary data siswa, sisi tengah adalah scatter plot tentang persebaran data siswa, dan sisi kanan adalah data numerik, bar chart faktor dropout mahasiswa, serta filter/legends dari plot dashboard ini.

> Dari **pie chart jenis kelamin**, dapat dilihat bahwa populasi data lebih banyak berjenis kelamin perempuan, sebesar 2868 (64.83%), sedangkan laki-laki hanya 1556 (35.17%).  
> Dari **pie chart status siswa**, terdapat total 4424 siswa, di antaranya 794 (17.95%) yang saat ini sedang terdaftar, 2209 (49.93%) yang sudah lulus, dan 1421 (32.12%) yang dropout.  
> Dari **pie chart beasiswa**, hampir 1/4, yaitu sebesar  1099 (24.84%) siswa yang memperoleh beasiswa, sedangkan 3325 (75.16%) sisanya tidak.  
> Dari **pie chart debitur** sebanyak 503 (11.37%) adalah seorang debitur, dan 3921 (88.63%) sisanya tidak.  

> Dari **scatter plot status siswa berdasarkan umur dan nilai tes masuk**, dapat dilihat dengan jelas rata-rata siswa yang lulus sebagian besar berada pada usia di bawah 20 sampai 25 tahun, dengan rata-rata Nilai Penerimaan (Admission Grade) berkisar 120 sampai 160. Sementara itu, siswa yang berusia 30 sampai 40 tahun, bahkan 50 tahun memiliki rata-rata Nilai Penerimaan (Admission Grade) 100 sampai 140 dan berstatus dropout.  

> **Rata-rata umur** adalah 23.27 tahun, **rata-rata Nilai Penerimaan (Admission Grade)** adalah 127.0, dan sebanyak 110 siswa **internasional**, dan 4314 siswa lokal.  
> Dari **bar chart status siswa berdasarkan status debtor**, dapat dilihat siswa yang menjadi debitur jelas tergambar paling banyak adalah mereka yang berstatus dropout (312 siswa) dibandingkan dengan mereka yang lulus (101 siswa). Hal ini menggambarkan adanya faktor finansial yang sangat kuat terhadap tingkat kelulusan dan dropout siswa.  
> Dari **bar chart status siswa berdasarkan beasiswa**, terdapat 835 siswa lulus dengan beasiswa dan 1374 siswa yang lulus tanpa beasiswa, sebesar 37.79% berbanding 62.20%. Sedangkan siswa yang dropout dengan beasiswa sebanyak 134 dan siswa yang dropout tanpa beasiswa sebanyak 1287, sebesar 9.43% berbanding 90.57%.  
> Dari **bar chart distribusi jenis kursus dan jenis kelamin**, kursus dengan data terbanyak adalah Keperawatan dengan jenis kelamin dominan adalah Perempuan. Sementara kursus dengan data paling sedikit adalah Teknologi Produksi Buofuel dengan dominasi Laki-laki. Selain itu, mahasiswa Laki-laki terbanyak ada di Program Studi Teknik Informatika dan Manajemen.  

> [!NOTE]
> Video singkat penjelasan business dashboard dan kesimpulannya dapat dilihat pada tautan [YouTube ini](https://youtu.be/FcmiS-Oo1xc 'Jaya Jaya Institute Students Dashboard').

## Machine Learning Prediction System

Untuk dapat membantu institusi dalam memprediksi kemungkinan jika siswanya akan dropout dan mencegah hal tersebut lebih dini, dapat menggunakan sistem prediksi yang telah dibangun. Sistem dibangun menggunakan Streamlit dan untuk menjalankan sistem tersebut secara local, dapat menjalankan kode berikut pada Terminal,

```bash
streamlit run streamlit_app.py
```

Dan untuk menghentikan program aplikasi Streamlit dapat melalui `ctrl + c`.

Sistem prediksi tersebut juga dapat diakses secara langsung yang sudah di-deploy ke Streamlit Cloud melalui tautan [berikut ini](https://student-dropout-predict.streamlit.app 'Jaya Jaya Institute Students Dropout Prediction').

## Conclusion

Berikut adalah beberapa poin penting yang bisa ditarik menjadi kesimpulan:
- **Distribusi Demografi Siswa:** Mayoritas siswa berjenis kelamin perempuan (64.83%), dengan sebagian besar populasi total adalah siswa lokal (97.51%) dibandingkan siswa internasional (2.49%).
- **Status Siswa:** Dari total 4424 siswa, hampir sepertiga (32.12%) mengalami dropout. Sebagian besar siswa yang lulus berada pada usia muda (20–25 tahun) dengan nilai penerimaan yang relatif lebih tinggi (120–160), sementara siswa usia lebih tua dan dengan nilai lebih rendah cenderung mengalami dropout.
- **Pengaruh Beasiswa:** Siswa yang menerima beasiswa memiliki tingkat kelulusan yang lebih tinggi (37.79%) dibandingkan dengan tingkat dropout (9.43%), menunjukkan peran signifikan beasiswa dalam mendukung keberhasilan akademik.
- **Faktor Keuangan:** Sebagian besar siswa dropout (61.99%) adalah debitur, menandakan kemungkinan adanya tekanan finansial yang memengaruhi keberlanjutan studi mereka.
- **Distribusi Berdasarkan Kursus:** Kursus dengan jumlah siswa tertinggi adalah Keperawatan dengan dominasi perempuan, sementara Teknologi Produksi Biofuel memiliki jumlah siswa terendah dengan dominasi laki-laki.

### Recommended Action Items

Berikut beberapa rekomendai yang dapat diambil oleh institusi untuk mengatasi permasalahan tingkat dropout siswa:
- Perluasan program beasiswa, terutama untuk kategori siswa yang berisiko dropout berdasarkan status keuangannya.
- Penyediaan opsi pembayaran cicilan dengan bunga 0% atau program penghapusan sebagian utang/biaya kuliah yang menunggak bagi siswa berprestasi.
- Menyediakan opsi program gap year disertai orientasi khusus untuk siswa yang kembali dari gap year, guna membantu dalam penyesuaian diri dengan lingkungan, teknologi, atau kurikulum yang mungkin telah berubah.
- Mengadakan program bimbingan belajar khusus untuk siswa dengan nilai rendah, terutama yang berusia lebih tua dan yang sudah menikah.
- Mendirikan pusat dukungan psikologis dan konseling bagi siswa yang mengalami tekanan finansial atau akademik.
- Melakukan peninjauan dan pemantauan lebih lanjut terhadap siswa yang saat ini sedang terdaftar (enrolled), serta prediksi kemungkinan siswa untuk tidak lulus/dropout melalui sistem yang telah dibangun menggunakan teknologi machine learning melalui website prediksi [berikut ini](https://student-dropout-predict.streamlit.app 'Jaya Jaya Institute Students Dropout Prediction').
