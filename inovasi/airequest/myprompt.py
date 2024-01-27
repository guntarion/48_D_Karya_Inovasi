

def get_prompt_analisis_makalah(kategori_request, inputan_judul_makalah, inputan_abstrak, inputan_klaim, inputan_latar_belakang, inputan_maksud_tujuan, inputan_identifikasi_masalah, inputan_analisis_masalah, inputan_metodologi, inputan_desain_inovasi, inputan_implementasi, inputan_evaluasi_implementasi, inputan_manfaat_finansial, inputan_manfaat_non_finansial, inputan_daftar_pustaka):

    if kategori_request == 'pertanyaan':
        konten = f"Dari makalah pembuatan karya inovasi berjudul '{inputan_judul_makalah}', berikut adalah [abstrak] = {inputan_abstrak}, berikut adalah [latar belakang] = {inputan_latar_belakang}, berikut adalah [maksud dan tujuan] = {inputan_maksud_tujuan}.\n"
        instruksi = f"Berdasarkan seluruh informasi tersebut, buatkan minimal 10 pertanyaan untuk perihal yang sifatnya menguji, perihal yang tampaknya salah atau aneh, ada logika yang aneh atau tidak tepat, adanya ketidaksingkronan atau inkonsistensi informasi. Berikan pertanyaan yang sulit dan tidak mudah dijawab."
    else:
        konten = f"Saya hendak membahas topik berikut: {inputan_abstrak}.\n"
        instruksi = "Berikan komentar kritis tentangnya"

    return f"{konten} {instruksi}"


def get_prompt_masak_ide(kategori_spesifik_request, inputan_user_1, inputan_user_2):

    pengantar_prompt = f"Pelajarilah yang berikut ini: {inputan_user_1}\n"
    default_audience = ' para karyawan dari Perusahaan Listrik Negara Indonesia yang bertanggung jawab atas pembangkitan listrik dan distribusinya'

    isi_prompt_mencariinspirasi = f", berikan tujuh usulan topik presentasi, berikut sedikit penjelasannya, yang relevan dengan mereka. Kaitkan topik atau kata kunci yang diberikan dengan aspek-aspek yang sesuai dengan kepentingan, tugas dan fungsi audiens tersebut, serta bagaimana hal tersebut berpengaruh atau dapat memberikan manfaat bagi pekerjaan mereka."
    isi_prompt_mengembangkantopik = "Mohon susun daftar pembahasan yang runtut berbentuk alur, minimal tiga poin dan maksimal tujuh poin, dengan sedikit penjelasan tentang setiap poin, menjelaskan konten dan relevansinya dalam konteks topik secara keseluruhan."
    isi_prompt_mempertanyakan = "Tolong ajukan tujuh pertanyaan yang bertujuan menggali lebih dalam atau menyelidiki aspek-aspek yang belum diinformasikan secara jelas, atau yang tersirat dalam paparan tersebut. Pertanyaan-pertanyaan ini harus membantu dalam memahami konteks yang lebih luas, detail yang hilang, atau implikasi dari apa yang telah disampaikan."
    isi_prompt_mengkritik = "Tolong analisis kekurangan dan aspek yang bisa ditingkatkan dari ide/konsep ini. Berikan masukan dan rekomendasi untuk perbaikan dan penyempurnaan, termasuk strategi atau pendekatan yang mungkin lebih efektif atau inovatif."
    isi_prompt_mengangkat = "Tolong sebutkan aspek-aspek positif, unik, atau menarik dari ide/konsep ini. Selain itu, berikan juga saran tentang bagaimana kami bisa mengembangkan atau menyempurnakannya lebih lanjut untuk membuatnya lebih efektif, inovatif, atau menarik."
    isi_prompt_menjatuhkan = "Jadilah pelawak yang pintar, yang memberikan tujuh poin kritik dalam bentuk hinaan atau celaan, yang mengungkap kelemahan ide bersangkutan, didasarkan pada asumsi yang terkandung secara implisit atau informasi yang tidak dijelaskan. Kritik ini harus disampaikan dengan cara yang jenaka dan menjengkelkan."
    isi_prompt_mengkinikan = "Tolong sambungkan informasi terkini dengan narasi eksisting sehingga menjadi narasi yang terkait dan utuh. Tujuannya adalah untuk memperbarui narasi agar lebih relevan dengan peristiwa, tren, atau informasi terkini, dan memastikan bahwa pesan utama menjadi lebih kuat dan terhubung dengan konteks saat ini."
    isi_prompt_definisi = "Buatkan definisi singkat tentangnya"

    if kategori_spesifik_request == 'mencariinspirasi':
        if inputan_user_2 == '':
            inputan_user_2 = default_audience
        isi_prompt = f"Untuk kalangan audiens berikut: {inputan_user_2}" + \
            isi_prompt_mencariinspirasi
    elif kategori_spesifik_request == 'mengembangkantopik':
        isi_prompt = isi_prompt_mengembangkantopik
    elif kategori_spesifik_request == 'mempertanyakan':
        isi_prompt = isi_prompt_mempertanyakan
    elif kategori_spesifik_request == 'mengkritik':
        isi_prompt = isi_prompt_mengkritik
    elif kategori_spesifik_request == 'mengangkat':
        isi_prompt = isi_prompt_mengangkat
    elif kategori_spesifik_request == 'menjatuhkan':
        isi_prompt = isi_prompt_menjatuhkan
    elif kategori_spesifik_request == 'mengkinikan':
        isi_prompt = f"Pada narasi tersebut, saya juga ingin menambahkan informasi terkini ini: {inputan_user_2}" + \
            isi_prompt_mengkinikan
    else:
        isi_prompt = isi_prompt_definisi

    return f"{pengantar_prompt} {isi_prompt}"
