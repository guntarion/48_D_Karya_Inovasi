
def get_prompt_ideasi(
    inputan_kategori_request, inputan_data_ide_judul, inputan_data_latar_belakang, inputan_data_solusi):

    if inputan_kategori_request == 'saransolusi':
        konten = f"Berikut adalah rencana atau ide [judul ide inovasi] = '{inputan_data_ide_judul}', dengan [latar belakang] = {inputan_data_latar_belakang}, dan [rencana solusi] = {inputan_data_solusi}.\n"
        instruksi = """
        Berdasarkan [latar belakang] yang disebutkan, dalam konteks perusahaan yang bergerak di bidang pembangkitan listrik, dalam fungsi operation & maintenance pembangkit listrik termasuk segala aspek manajerial terkait; 
        1. Beri komentar/remark berkualitas atas [rencana solusi], beri pandangan untuk lebih memperjelas dari apa yang sudah disampaikan, 
        2. Terhadap [rencana solusi], beri masukan terkait fitur atau fungsionalitas apa yang perlu ditambahkan/diterapkan. 
        3. Jika perlu dan relevan, beri masukan terkait fitur atau fungsionalitas apa yang perlu dihilangkan/ditidak diterapkan.
        """

    if inputan_kategori_request == 'pengembangan':
        konten = f"Berikut adalah rencana atau ide [judul ide inovasi] = '{inputan_data_ide_judul}', dengan [latar belakang] = {inputan_data_latar_belakang}, dan [rencana solusi] = {inputan_data_solusi}.\n"
        instruksi = """
        Berdasarkan [latar belakang] yang disebutkan dan [rencana solusi] sebagai solusi dan apa yang renana akan diimplementasi, bertindaklah sebagai implementator bagi ide inovasi tersebut: 
        1. Sampaikan seperti apa langkah kerja atau tahapan pengembangan hingga implementasi dan evaluasinya; tambahkan lain hal yang Anda rasa penting untuk dipertimbangkan. 
        2. Beri remarks tambahan yang menunjukkan bahwa Anda adalah orang yang sangat piawai di pengembangan perangkat lunak. Tidak perlu ragu menggunakan istilah yang sulit atau teknis dan sophisticated. 
        """

    if inputan_kategori_request == 'rancanganaplikasi':
        konten = f"Berikut adalah rencana atau ide [judul ide inovasi] = '{inputan_data_ide_judul}', dengan [latar belakang] = {inputan_data_latar_belakang}, dan [rencana solusi] = {inputan_data_solusi}.\n"
        instruksi = """
        Berdasarkan [latar belakang] yang disebutkan, buatkan rancangan perangkat lunak yang paling sesuai untuk ditindaklanjuti menjadi karya inovasi/solusi. Berikan penjelasan tentang fitur apa saja yang perlu/sebaiknya disediakan berikut sedikit penjelasan tentangnya; sampaikan metodologi pengembangannya, ukuran efektivitas apa yang perlu digunakan, dan lain hal yang Anda rasa penting untuk dipertimbangkan. Tidak perlu ragu menggunakan istilah yang sulit atau teknis dan sophisticated. 
        """

    if inputan_kategori_request == 'skoringlatarbelakang':
        konten = f"Berikut adalah rencana atau ide [judul ide inovasi] = '{inputan_data_ide_judul}', dengan [latar belakang] = {inputan_data_latar_belakang}, dan [rencana solusi] = {inputan_data_solusi}.\n"
        instruksi = """

        Dari informasi yang ada, lakukan penilaian terkait 'Relevansi Latar Belakang Masalah/Akar Permasalahan Terhadap Penyelesaian Masalah', atas aspek berikut:
        1. Seberapa baik ide inovasi mengidentifikasi masalah nyata yang dihadapi; pemahaman yang mendalam tentang masalah tersebut, termasuk aspek-aspek seperti sebab, dampak, dan konteks di mana masalah itu terjadi.
        2. Menilai seberapa relevan ide inovasi dengan kebutuhan atau tantangan aktual yang dihadapi oleh perusahaan atau industri. Ide inovasi harus berakar pada kebutuhan nyata, bukan hanya pada teori atau spekulasi.
        3. Apakah inovasi didasarkfan pada analisis yang mendalam tentang akar permasalahan. Termasuk memahami berbagai faktor yang berkontribusi pada masalah dan bagaimana inovasi dapat mengatasinya.

        Berikan skor dengan menggunakan ini sebagai acuan penilaian:

        - Skor 41-50: Predikat Rendah. Indikator: Bilamana ide inovasi menunjukkan pemahaman yang sangat terbatas tentang masalah. Analisis masalah dangkal dan kurang terkait dengan solusi yang diusulkan.
        - Skor 51-60. Predikat Cukup. Indikator: Identifikasi masalah yang cukup, tetapi analisisnya tidak terlalu mendalam atau tidak sepenuhnya relevan dengan solusi yang diusulkan. Pemahaman tentang akar masalah dan relevansinya dengan solusi cukup.
        - Skor 61-70. Predikat Memadai. Indikator: Identifikasi dan analisis masalah yang memadai. Ide inovasi berhubungan dengan masalah yang relevan, meskipun masih ada ruang untuk peningkatan dalam pemahaman atau analisis yang lebih mendalam.
        - Skor 71-80. Predikat Baik. Indikator: Pemahaman yang baik tentang masalah dan analisis yang relevan. Ide inovasi terhubung dengan baik dengan masalah yang diidentifikasi dan menunjukkan potensi solusi yang efektif.
        - Skor 81-90. Predikat Sangat Baik. Indikator: Analisis masalah yang sangat baik dan relevan. Ide inovasi menunjukkan pemahaman yang mendalam tentang masalah dan akar permasalahannya, dengan solusi yang sangat terkait dan berpotensi efektif.
        - Skor 91-100. Predikat Luar Biasa. Indikator: Pemahaman yang luar biasa tentang masalah dan akar permasalahannya. Analisis yang sangat mendalam dan terperinci, dengan ide inovasi yang sangat relevan dan menawarkan solusi yang sangat potensial dan inovatif.

        Respon Anda berupa satu angka skoring dalam rentang 41 sampai dengan 100, dengan menyertakan alasan dan pertimbangan berdasarkan isi makalah. Anda mungkin juga ingin memberikan saran untuk perbaikan atau peningkatan yang dapat membantu meningkatkan kualitas dan efektivitas karya inovasi tersebut. Anda memberi respon dengan mengawalinya dengan 'Skor yang saya berikan untuk aspek Relevansi Latar Belakang Permasalahan terhadap Penyelesaian Masalah adalah ... karena ...'

        """

    else:
        konten = f"Saya hendak membahas topik berikut: {inputan_data_ide_judul}.\n"
        instruksi = "Berikan komentar kritis tentangnya"

    return f"{konten} {instruksi}"

def get_prompt_analisis_makalah(kategori_request, inputan_judul_makalah, inputan_abstrak, inputan_klaim, inputan_latar_belakang, inputan_maksud_tujuan, inputan_identifikasi_masalah, inputan_analisis_masalah, inputan_metodologi, inputan_desain_inovasi, inputan_implementasi, inputan_evaluasi_implementasi, inputan_manfaat_finansial, inputan_manfaat_non_finansial, inputan_daftar_pustaka):

    if kategori_request == 'pertanyaan':
        konten = f"Dari makalah pembuatan karya inovasi berjudul '{inputan_judul_makalah}', berikut adalah [abstrak] = {inputan_abstrak}, berikut adalah [latar belakang] = {inputan_latar_belakang}, berikut adalah [maksud dan tujuan] = {inputan_maksud_tujuan}.\n"
        instruksi = """
        Berdasarkan seluruh informasi tersebut, buatkan 2 pertanyaan untuk perihal yang sifatnya menguji, perihal yang tampaknya salah atau aneh, ada logika yang aneh atau tidak tepat, adanya ketidaksingkronan atau inkonsistensi informasi. Berikan pertanyaan yang sulit dan tidak mudah dijawab.
        """

    elif kategori_request == 'kritikan':
        konten = f"Dari makalah pembuatan karya inovasi berjudul '{inputan_judul_makalah}', berikut adalah [abstrak] = {inputan_abstrak}, berikut adalah [latar belakang] = {inputan_latar_belakang}, berikut adalah [maksud dan tujuan] = {inputan_maksud_tujuan}, berikut adalah [desain inovasi] = {inputan_desain_inovasi}, berikut adalah [implementasi] nya = {inputan_implementasi}, berikut adalah [manfaat inovasi] = {inputan_manfaat_finansial} dan {inputan_manfaat_non_finansial}.\n"
        instruksi = f"Jadilah orang yang bersikap sangat skeptis, negatif dan pesimis terhadap karya inovasinya. Cari dan sampaikan dua atau tiga poin tentang segala bentuk kelemahan, alasan, dan pertimbangan --dinyatakan dengan argumen valid dan kuat-- yang menunjukkan bahwa karya bersangkutan tidak pantas disebut inovasi, dan/atau dibangun dengan dasar atau justifikasi yang tidak kuat, dan/atau tidak memiliki keunggulan dan manfaat yang patut dibanggakan, dan/atau susah untuk diimplementasikan, dan/atau tidak menarik bagi pihak manapun untuk mengadopsinya.\n"

    elif kategori_request == 'saran_pengembangan':
        konten = f"Dari makalah pembuatan karya inovasi berjudul '{inputan_judul_makalah}', berikut adalah [abstrak] = {inputan_abstrak}, berikut adalah [latar belakang] = {inputan_latar_belakang}, berikut adalah [maksud dan tujuan] = {inputan_maksud_tujuan}, berikut adalah [desain inovasi] = {inputan_desain_inovasi}, berikut adalah [implementasi] nya = {inputan_implementasi}, berikut adalah [manfaat inovasi] = {inputan_manfaat_finansial} dan {inputan_manfaat_non_finansial}.\n"
        instruksi = f"Sebatas dari informasi yang tersampaikan di makalah, buatkan dua atau tiga rekomendasi atau usulan berikut konsideran atau alasannya, tentang bagaimana bentuk perbaikan atau penyempurnaan atau pengembangan lebih lanjut dari karya inovasi bersangkutan. Anda bisa mendasarkan pada potensi kelemahan dari karyanya, atau peningkatan dari apa yang sudah baik.\n"

    elif kategori_request == 'catatan_kritis_umum':
        konten = f"Dari makalah pembuatan karya inovasi berjudul '{inputan_judul_makalah}', berikut adalah [abstrak] = {inputan_abstrak}, berikut adalah [latar belakang] = {inputan_latar_belakang}, berikut adalah [maksud dan tujuan] = {inputan_maksud_tujuan}, berikut adalah [desain inovasi] = {inputan_desain_inovasi}, berikut adalah [implementasi] nya = {inputan_implementasi}, berikut adalah [manfaat inovasi] = {inputan_manfaat_finansial} dan {inputan_manfaat_non_finansial}.\n"
        instruksi = f"Berdasarkan informasi tersebut, berikan dua atau tiga remarks atau komentar atau catatan yang berbobot. Tunjukkan bahwa Anda adalah orang yang sangat berpengalaman di bidang pembangkitan listrik dan manajerial. Tidak perlu ragu menggunakan istilah yang sulit atau teknis dan sophisticated.\n"


    elif kategori_request == 'catatan_kritis_aplikasi':
        konten = f"Dari makalah pembuatan karya inovasi berjudul '{inputan_judul_makalah}', berikut adalah [abstrak] = {inputan_abstrak}, berikut adalah [latar belakang] = {inputan_latar_belakang}, berikut adalah [maksud dan tujuan] = {inputan_maksud_tujuan}, berikut adalah [desain inovasi] = {inputan_desain_inovasi}, berikut adalah [implementasi] nya = {inputan_implementasi}, berikut adalah [manfaat inovasi] = {inputan_manfaat_finansial} dan {inputan_manfaat_non_finansial}.\n"
        instruksi = f"Berdasarkan informasi tersebut, berikan dua atau tiga remarks atau komentar atau catatan atau pertanyaan terkait apapun dari sisi teknologi yang diulas. Ini bisa melingkupi apa saja, bisa dari tampilan, algoritma yang dipilih, arsitektur, framework, cara perangkat lunaknya dibangun, pilihan bahasa pemrograman, user acceptance test, apapun. Tunjukkan bahwa Anda adalah orang yang sangat berpengalaman di bidang teknologi. Tidak perlu ragu menggunakan istilah yang sulit atau teknis dan sophisticated. Untuk ini, Anda juga bisa membandingkan atau menyebut padanan atau perihal atau studi kasus di tempat lain yang bisa dikaitkan dengan konteks karya inovasi bersangkutan dari sisi teknologi; untuk menunjukkan bahwa Anda adalah orang yang sangat berwawasan.\n"

    elif kategori_request == 'ide_manfaat_inovasi':
        konten = f"Dari makalah pembuatan karya inovasi berjudul '{inputan_judul_makalah}', berikut adalah [abstrak] = {inputan_abstrak}, berikut adalah [latar belakang] = {inputan_latar_belakang}, berikut adalah [maksud dan tujuan] = {inputan_maksud_tujuan}, berikut adalah [desain inovasi] = {inputan_desain_inovasi}, berikut adalah [implementasi] nya = {inputan_implementasi}, berikut adalah [manfaat inovasi] = {inputan_manfaat_finansial} dan {inputan_manfaat_non_finansial}.\n"
        instruksi = """
        Berdasarkan informasi tersebut, silakan identifikasi dan analisis manfaat yang ditimbulkan dari karya inovasi bersangkutan. Fokuskan pada dua aspek utama, yaitu Manfaat Finansial dan Manfaat Non-Finansial, dengan mempertimbangkan manfaat langsung maupun tidak langsung:

        1. Manfaat Finansial:
        - Evaluasi potensi penghematan biaya yang dapat dihasilkan oleh inovasi, seperti pengurangan penggunaan sumber daya, efisiensi operasional, atau pengurangan pemborosan.
        - Analisis kemungkinan inovasi dalam menghindari potential losses, seperti melalui peningkatan keandalan sistem atau pencegahan kesalahan.
        - Pertimbangkan dan usulkan dampak positif lainnya pada aspek finansial, seperti peningkatan pendapatan atau ROI (Return on Investment).

        2. Manfaat Non-Finansial:
        - Tinjau peningkatan citra perusahaan sebagai hasil dari implementasi inovasi, termasuk persepsi publik dan reputasi di industri.
        - Evaluasi tingkat kepuasan pengguna dan pengaruhnya terhadap loyalitas pelanggan atau keterlibatan pengguna.
        - Analisis peningkatan kompetensi dan awareness di kalangan karyawan atau pengguna, serta dampaknya pada inovasi dan pengetahuan.
        - Pertimbangkan peningkatan keselamatan dan kenyamanan kerja sebagai akibat dari penerapan inovasi.
        - Identifikasi manfaat lainnya seperti peningkatan efisiensi kerja, kolaborasi tim, dan adaptabilitas.

        Berikan ringkasan tentang setiap manfaat yang diidentifikasi, sertakan contoh atau kasus yang relevan, dan jelaskan bagaimana manfaat ini dapat mempengaruhi kinerja dan keberhasilan keseluruhan dari inovasi tersebut dalam jangka panjang
        """

    elif kategori_request == 'ide_risiko_inovasi':
        konten = f"\n"
        instruksi = f"\n"

    elif kategori_request == 'ide_risiko_inovasi_softwarefull':
        konten = f"Dari makalah pembuatan karya inovasi berjudul '{inputan_judul_makalah}', berikut adalah [abstrak] = {inputan_abstrak}, berikut adalah [latar belakang] = {inputan_latar_belakang}, berikut adalah [maksud dan tujuan] = {inputan_maksud_tujuan}, berikut adalah [desain inovasi] = {inputan_desain_inovasi}, berikut adalah [implementasi] nya = {inputan_implementasi}.\n"
        instruksi = """
        Berdasarkan informasi tersebut, silakan lakukan identifikasi dan analisis risiko, dengan menyertakan antisipasi dan masukan upaya untuk mengecilkan tingkat risikonya,  dengan fokus pada aspek-aspek berikut:

        1. Risiko Teknis:
        - Identifikasi potensi masalah teknis yang mungkin timbul, seperti bug, masalah kompatibilitas, atau kegagalan integrasi dengan sistem yang ada. Buat perkiraan sistem apa yang sekiranya bisa/berpotensi terintegrasi/diintegrasikan.
        - Evaluasi risiko keamanan, termasuk potensi kerentanan terhadap serangan siber, akibat kesalahan manusia, atau kebocoran data. 

        2. Risiko Operasional:
        - Buat perkiraan tentang seberapa perangkat lunak akan mengubah proses kerja, permasalahan teknis yang bisa muncul akibat implementasi dan operasionalnya. Identifikasi masalah apa yang berpotensi muncul berdasarkan nature karya bersangkutan. 

        3. Risiko Finansial:
        - Tinjau potensi risiko finansial, termasuk biaya pengembangan yang berlebihan, biaya pemeliharaan, atau dampak pada penghasilan jika perangkat lunak tidak berfungsi seperti yang diharapkan.

        4. Risiko Penerimaan Pengguna:
        - Analisis risiko terkait dengan penerimaan perangkat lunak oleh pengguna akhir, termasuk kemungkinan penolakan atau kurangnya adopsi.

        Berikan ringkasan tentang setiap risiko yang diidentifikasi, potensi dampaknya, dan saran untuk mitigasi risiko tersebut. Tujuan dari analisis ini adalah untuk membantu dalam mempersiapkan strategi pengelolaan risiko yang efektif untuk karya inovasi/perbaikan perangkat lunak tersebut.
        """

    elif kategori_request == 'ide_risiko_inovasi_softwarealat':
        konten = f"Dari makalah pembuatan karya inovasi berjudul '{inputan_judul_makalah}', berikut adalah [abstrak] = {inputan_abstrak}, berikut adalah [latar belakang] = {inputan_latar_belakang}, berikut adalah [maksud dan tujuan] = {inputan_maksud_tujuan}, berikut adalah [desain inovasi] = {inputan_desain_inovasi}, berikut adalah [implementasi] nya = {inputan_implementasi}.\n"
        instruksi = """
        Silakan lakukan identifikasi dan analisis risiko dari karya improvement atau karya inovasi berbentuk perangkat lunak yang melibatkan penggunaan alat, peralatan, atau perangkat keras tersebut. Dalam analisis Anda, pertimbangkan aspek-aspek berikut dan sertakan saran serta strategi mitigasi:

        1. Risiko Kompatibilitas Teknis:
        - Identifikasi potensi masalah teknis yang mungkin timbul, seperti bug, masalah kompatibilitas, atau kegagalan integrasi dengan sistem yang ada. Buat perkiraan sistem apa yang sekiranya bisa/berpotensi terintegrasi/diintegrasikan.
        - Evaluasi potensi risiko terkait dengan kompatibilitas antara perangkat lunak dan perangkat keras yang digunakan. Apakah ada isu interoperabilitas atau masalah integrasi yang mungkin timbul?
        - Berikan saran untuk menguji dan memvalidasi kompatibilitas sebelum penerapan penuh.

        2. Risiko Operasional dan Penggunaan:
        - Buat perkiraan tentang seberapa perangkat lunak akan mengubah proses kerja, permasalahan teknis yang bisa muncul akibat implementasi dan operasionalnya. Identifikasi masalah apa yang berpotensi muncul berdasarkan nature karya bersangkutan. 
        - Pertimbangkan risiko operasional yang mungkin terjadi karena penggunaan gabungan perangkat lunak dan perangkat keras, seperti masalah ergonomi, kesulitan dalam penggunaan, atau kesalahan pengguna.
        - Sarankan pelatihan pengguna dan desain antarmuka yang ramah pengguna untuk meminimalkan risiko ini.

        3. Risiko Kegagalan Perangkat Keras:
        - Identifikasi risiko yang terkait dengan kegagalan perangkat keras yang digunakan bersama dengan perangkat lunak. Bagaimana kegagalan ini dapat mempengaruhi keseluruhan sistem?
        - Sarankan rencana redundansi atau penggantian perangkat keras untuk memitigasi dampak dari kegagalan.

        4. Risiko Keamanan dan Kerentanan:
        - Evaluasi risiko keamanan, termasuk potensi kerentanan terhadap serangan siber, akibat kesalahan manusia, atau kebocoran data. 
        - Analisis risiko keamanan yang timbul dari interaksi antara perangkat lunak dan perangkat keras, termasuk kerentanan potensial yang mungkin dieksploitasi.
        - Berikan rekomendasi untuk pengujian keamanan yang komprehensif dan implementasi protokol keamanan yang kuat.

        5. Risiko Biaya dan Anggaran:
        - Tinjau potensi risiko finansial, termasuk biaya pengembangan yang berlebihan, biaya pemeliharaan, atau dampak pada penghasilan jika perangkat lunak tidak berfungsi seperti yang diharapkan.
        - Tinjau risiko finansial yang berkaitan dengan biaya perangkat keras, pemeliharaan, dan upgrade. Apakah biaya ini sesuai dengan anggaran?

        6. Risiko Dampak Lingkungan:
        - Evaluasi dampak lingkungan dari penggunaan perangkat keras, seperti konsumsi energi atau pembuangan limbah, jika relevan dengan karya bersangkutan.
        - Sarankan langkah-langkah untuk mengurangi dampak lingkungan, seperti penggunaan teknologi hijau atau daur ulang perangkat keras, jika relevan dengan karya bersangkutan..

        Berikan analisis mendalam untuk setiap risiko yang diidentifikasi, potensi dampaknya, serta saran dan strategi mitigasi yang relevan. Tujuan dari analisis ini adalah untuk mengembangkan strategi pengelolaan risiko yang efektif dan berkelanjutan untuk implementasi karya inovasi/perbaikan perangkat lunak dan perangkat keras.
        """

    elif kategori_request == 'analisis_latar_belakang':
        konten = f"Dari makalah pembuatan karya inovasi berjudul '{inputan_judul_makalah}', berikut adalah [abstrak] = {inputan_abstrak}, berikut adalah [latar belakang] = {inputan_latar_belakang}, berikut adalah [maksud dan tujuan] = {inputan_maksud_tujuan}.\n"
        instruksi = """
        Silakan lakukan analisis terhadap bagian [latar belakang] dari makalah karya inovasi tersebut, dengan memahami konteks berdasarkan informasi lain yang disampaikan. Dalam analisis Anda, fokuskan pada aspek-aspek berikut untuk dinilai:

        1. Keterkaitan Masalah dengan Topik:
        - Evaluasi seberapa jelas dan tepat masalah yang diidentifikasi dalam karya inovasi tersebut dikaitkan dengan topik utama.
        - Analisis apakah latar belakang memberikan pemahaman yang cukup tentang masalah dan relevansinya dengan topik yang dibahas.

        2. Konteks dan Justifikasi:
        - Tinjau seberapa baik latar belakang menjelaskan konteks di mana inovasi tersebut dikembangkan, termasuk relevansi historis atau kontemporer.
        - Pertimbangkan apakah latar belakang memberikan justifikasi yang kuat untuk kebutuhan inovasi tersebut.
        - Apakah sudah memuat indeks kinerja atau Key Performance Indicator atau ukuran/indikator lain yang relevan dengan permasalahan dan tujuan pembuatan karya.

        3. Kejelasan dan Struktur Narasi:
        - Pertimbangkan seberapa jelas dan logis struktur narasi dalam latar belakang. Apakah informasi disajikan dengan cara yang mudah diikuti?
        - Tinjau kejelasan tujuan dan sasaran dari karya inovasi seperti yang dijelaskan dalam latar belakang.
        -  Apakah latar belakang dan maksud tujuan sudah menunjukkan hubungan yang logis. Apakah terbentuk hubungan sebab dan akibat atau analisa dampak yang masuk akal, dari karya/inovasi terhadap permasalahan yang hendak dipecahkan atau peluang yang dikejar.
        - Apakah obyek atau karya inovasinya sudah diperkenalkan dengan cukup baik.

        4. Identifikasi Gap Penelitian atau Inovasi:
        - Analisis apakah latar belakang berhasil mengidentifikasi gap dalam penelitian atau praktik yang ada yang inovasi berusaha untuk alamat.
        - Evaluasi apakah ada penjelasan tentang bagaimana karya inovasi ini berbeda atau lebih baik daripada solusi yang sudah ada, jika ada.

        Berikan ringkasan dari evaluasi Anda tentang setiap aspek latar belakang makalah, termasuk area yang kuat serta saran untuk perbaikan atau penjelasan lebih lanjut yang mungkin diperlukan.
        """

    elif kategori_request == 'analisis_metodologi':
        konten = f"Dari makalah pembuatan karya inovasi berjudul '{inputan_judul_makalah}', berikut adalah [abstrak] = {inputan_abstrak}, berikut adalah [latar belakang] = {inputan_latar_belakang}, berikut adalah [metodologi] = {inputan_metodologi}.\n"
        instruksi = """
        Silakan lakukan analisis dan pengkritisan terhadap pemaparan [metodologi] dalam makalah karya inovasi tersebut. Dalam analisis Anda, pertimbangkan aspek-aspek berikut dan sertakan saran perbaikan atau improvement:

        1. Kesesuaian [metodologi]:
        - Evaluasi apakah metodologi yang dipilih sesuai dengan tujuan dan sifat karya inovasi perangkat lunak tersebut.
        - Kritik dan saran tentang cara-cara untuk meningkatkan atau memperbaiki pemilihan dan penerapan metodologi tersebut.

        2. Kejelasan dan Detail:
        - Analisis seberapa jelas dan rinci pemaparan [metodologi] dalam makalah. Apakah langkah-langkah, alat, dan teknik yang digunakan dijelaskan dengan cukup?
        - Berikan saran untuk meningkatkan kejelasan dan detail dalam pemaparan [metodologi].

        3. Validitas dan Keandalan:
        - Tinjau validitas dan keandalan dari [metodologi] yang dijelaskan, termasuk teknik pengujian dan evaluasi yang digunakan.

        4. Inovasi dalam [metodologi]:
        - Pertimbangkan apakah ada aspek inovatif atau unik dalam metodologi yang diusulkan yang membedakannya dari pendekatan lain.
        - Sarankan cara-cara untuk lebih menonjolkan atau mengembangkan inovasi metodologis tersebut.

        5. Implikasi dan Risiko:
        - Evaluasi implikasi dan risiko yang mungkin timbul dari penerapan metodologi ini, termasuk potensi hambatan atau kesulitan.
        - Berikan saran mitigasi risiko dan cara mengatasi potensi hambatan tersebut.

        Berikan ringkasan dari evaluasi Anda tentang pemaparan metodologi dalam makalah, termasuk poin-poin kritik dan saran untuk perbaikan atau peningkatan yang dapat membantu meningkatkan kualitas dan efektivitas karya inovasi tersebut.

        """

    elif kategori_request == 'skoring_latar_belakang':
        konten = f"\n"
        instruksi = """

        Dari informasi yang ada, lakukan penilaian terkait 'Relevansi Latar Belakang Masalah/Akar Permasalahan Terhadap Penyelesaian Masalah', atas aspek berikut:
        1. Seberapa baik ide inovasi mengidentifikasi masalah nyata yang dihadapi; pemahaman yang mendalam tentang masalah tersebut, termasuk aspek-aspek seperti sebab, dampak, dan konteks di mana masalah itu terjadi.
        2. Menilai seberapa relevan ide inovasi dengan kebutuhan atau tantangan aktual yang dihadapi oleh perusahaan atau industri. Ide inovasi harus berakar pada kebutuhan nyata, bukan hanya pada teori atau spekulasi.
        3. Apakah inovasi didasarkfan pada analisis yang mendalam tentang akar permasalahan. Termasuk memahami berbagai faktor yang berkontribusi pada masalah dan bagaimana inovasi dapat mengatasinya.

        Berikan skor dengan menggunakan ini sebagai acuan penilaian:

        - Skor 41-50: Predikat Rendah. Indikator: Bilamana ide inovasi menunjukkan pemahaman yang sangat terbatas tentang masalah. Analisis masalah dangkal dan kurang terkait dengan solusi yang diusulkan.
        - Skor 51-60. Predikat Cukup. Indikator: Identifikasi masalah yang cukup, tetapi analisisnya tidak terlalu mendalam atau tidak sepenuhnya relevan dengan solusi yang diusulkan. Pemahaman tentang akar masalah dan relevansinya dengan solusi cukup.
        - Skor 61-70. Predikat Memadai. Indikator: Identifikasi dan analisis masalah yang memadai. Ide inovasi berhubungan dengan masalah yang relevan, meskipun masih ada ruang untuk peningkatan dalam pemahaman atau analisis yang lebih mendalam.
        - Skor 71-80. Predikat Baik. Indikator: Pemahaman yang baik tentang masalah dan analisis yang relevan. Ide inovasi terhubung dengan baik dengan masalah yang diidentifikasi dan menunjukkan potensi solusi yang efektif.
        - Skor 81-90. Predikat Sangat Baik. Indikator: Analisis masalah yang sangat baik dan relevan. Ide inovasi menunjukkan pemahaman yang mendalam tentang masalah dan akar permasalahannya, dengan solusi yang sangat terkait dan berpotensi efektif.
        - Skor 91-100. Predikat Luar Biasa. Indikator: Pemahaman yang luar biasa tentang masalah dan akar permasalahannya. Analisis yang sangat mendalam dan terperinci, dengan ide inovasi yang sangat relevan dan menawarkan solusi yang sangat potensial dan inovatif.

        Respon Anda berupa angka skoring dalam rentang 41 sampai dengan 100, dengan menyertakan alasan dan pertimbangan berdasarkan isi makalah.
        """
    
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
