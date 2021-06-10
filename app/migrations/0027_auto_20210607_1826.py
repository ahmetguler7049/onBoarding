# Generated by Django 3.1.7 on 2021-06-07 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_auto_20210607_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='bootcamp_name',
            field=models.CharField(choices=[('Adana Alparslan Türkeş Bilim ve Teknoloji Üniversitesi', 'Adana Alparslan Türkeş Bilim ve Teknoloji Üniversitesi'), ('Çukurova Üniversitesi', 'Çukurova Üniversitesi'), ('Adıyaman Üniversitesi', 'Adıyaman Üniversitesi'), ('Afyon Kocatepe Üniversitesi', 'Afyon Kocatepe Üniversitesi'), ('Afyonkarahisar Sağlık Bilimleri Üniversitesi', 'Afyonkarahisar Sağlık Bilimleri Üniversitesi'), ('Ağrı İbrahim Çeçen Üniversitesi', 'Ağrı İbrahim Çeçen Üniversitesi'), ('Aksaray Üniversitesi', 'Aksaray Üniversitesi'), ('Amasya Üniversitesi', 'Amasya Üniversitesi'), ('Ankara Üniversitesi', 'Ankara Üniversitesi'), ('Ankara Müzik ve Güzel Sanatlar Üniversitesi', 'Ankara Müzik ve Güzel Sanatlar Üniversitesi'), ('Ankara Hacı Bayram Veli Üniversitesi', 'Ankara Hacı Bayram Veli Üniversitesi'), ('Ankara Sosyal Bilimler Üniversitesi', 'Ankara Sosyal Bilimler Üniversitesi'), ('Gazi Üniversitesi', 'Gazi Üniversitesi'), ('Hacettepe Üniversitesi', 'Hacettepe Üniversitesi'), ('Orta Doğu Teknik Üniversitesi', 'Orta Doğu Teknik Üniversitesi'), ('Ankara Yıldırım Beyazıt Üniversitesi', 'Ankara Yıldırım Beyazıt Üniversitesi'), ('Polis Akademisi', 'Polis Akademisi'), ('Anka Teknoloji Üniversitesi', 'Anka Teknoloji Üniversitesi'), ('Ankara Bilim Üniversitesi', 'Ankara Bilim Üniversitesi'), ('Ankara Medipol Üniversitesi', 'Ankara Medipol Üniversitesi'), ('Atılım Üniversitesi', 'Atılım Üniversitesi'), ('Başkent Üniversitesi', 'Başkent Üniversitesi'), ('Çankaya Üniversitesi', 'Çankaya Üniversitesi'), ('İhsan Doğramacı Bilkent Üniversitesi', 'İhsan Doğramacı Bilkent Üniversitesi'), ('Lokman Hekim Üniversitesi', 'Lokman Hekim Üniversitesi'), ('Ostim Teknik Üniversitesi', 'Ostim Teknik Üniversitesi'), ('TED Üniversitesi', 'TED Üniversitesi'), ('TOBB Ekonomi ve Teknoloji Üniversitesi', 'TOBB Ekonomi ve Teknoloji Üniversitesi'), ('Ufuk Üniversitesi', 'Ufuk Üniversitesi'), ('Türk Hava Kurumu Üniversitesi', 'Türk Hava Kurumu Üniversitesi'), ('Yüksek İhtisas Üniversitesi', 'Yüksek İhtisas Üniversitesi'), ('Akdeniz Üniversitesi', 'Akdeniz Üniversitesi'), ('Alanya Alaaddin Keykubat Üniversitesi', 'Alanya Alaaddin Keykubat Üniversitesi'), ('Alanya Hamdullah Emin Paşa Üniversitesi', 'Alanya Hamdullah Emin Paşa Üniversitesi'), ('Antalya Akev Üniversitesi', 'Antalya Akev Üniversitesi'), ('Antalya Bilim Üniversitesi', 'Antalya Bilim Üniversitesi'), ('Ardahan Üniversitesi', 'Ardahan Üniversitesi'), ('Artvin Çoruh Üniversitesi', 'Artvin Çoruh Üniversitesi'), ('Aydın Adnan Menderes Üniversitesi', 'Aydın Adnan Menderes Üniversitesi'), ('Balıkesir Üniversitesi', 'Balıkesir Üniversitesi'), ('Bandırma Onyedi Eylül Üniversitesi', 'Bandırma Onyedi Eylül Üniversitesi'), ('Bartın Üniversitesi', 'Bartın Üniversitesi'), ('Batman Üniversitesi', 'Batman Üniversitesi'), ('Bayburt Üniversitesi', 'Bayburt Üniversitesi'), ('Bilecik Şeyh Edebali Üniversitesi', 'Bilecik Şeyh Edebali Üniversitesi'), ('Bingöl Üniversitesi', 'Bingöl Üniversitesi'), ('Bitlis Eren Üniversitesi', 'Bitlis Eren Üniversitesi'), ('Bolu Abant İzzet Baysal Üniversitesi', 'Bolu Abant İzzet Baysal Üniversitesi'), ('Burdur Mehmet Akif Ersoy Üniversitesi', 'Burdur Mehmet Akif Ersoy Üniversitesi'), ('Bursa Teknik Üniversitesi', 'Bursa Teknik Üniversitesi'), ('Bursa Uludağ Üniversitesi', 'Bursa Uludağ Üniversitesi'), ('Çanakkale Onsekiz Mart Üniversitesi', 'Çanakkale Onsekiz Mart Üniversitesi'), ('Çankırı Karatekin Üniversitesi', 'Çankırı Karatekin Üniversitesi'), ('Hitit Üniversitesi', 'Hitit Üniversitesi'), ('Pamukkale Üniversitesi', 'Pamukkale Üniversitesi'), ('Dicle Üniversitesi', 'Dicle Üniversitesi'), ('Düzce Üniversitesi', 'Düzce Üniversitesi'), ('Trakya Üniversitesi', 'Trakya Üniversitesi'), ('Fırat Üniversitesi', 'Fırat Üniversitesi'), ('Erzincan Binali Yıldırım Üniversitesi', 'Erzincan Binali Yıldırım Üniversitesi'), ('Atatürk Üniversitesi', 'Atatürk Üniversitesi'), ('Erzurum Teknik Üniversitesi', 'Erzurum Teknik Üniversitesi'), ('Anadolu Üniversitesi', 'Anadolu Üniversitesi'), ('Eskişehir Osmangazi Üniversitesi', 'Eskişehir Osmangazi Üniversitesi'), ('Eskişehir Teknik Üniversitesi', 'Eskişehir Teknik Üniversitesi'), ('Gaziantep Üniversitesi', 'Gaziantep Üniversitesi'), ('Gaziantep İslam Bilim ve Teknoloji Üniversitesi', 'Gaziantep İslam Bilim ve Teknoloji Üniversitesi'), ('Hasan Kalyoncu Üniversitesi', 'Hasan Kalyoncu Üniversitesi'), ('Sanko Üniversitesi', 'Sanko Üniversitesi'), ('Giresun Üniversitesi', 'Giresun Üniversitesi'), ('Gümüşhane Üniversitesi', 'Gümüşhane Üniversitesi'), ('Hakkari Üniversitesi', 'Hakkari Üniversitesi'), ('İskenderun Teknik Üniversitesi', 'İskenderun Teknik Üniversitesi'), ('Hatay Mustafa Kemal Üniversitesi', 'Hatay Mustafa Kemal Üniversitesi'), ('Iğdır Üniversitesi', 'Iğdır Üniversitesi'), ('Süleyman Demirel Üniversitesi', 'Süleyman Demirel Üniversitesi'), ('Isparta Uygulamalı Bilimler Üniversitesi', 'Isparta Uygulamalı Bilimler Üniversitesi'), ('Boğaziçi Üniversitesi', 'Boğaziçi Üniversitesi'), ('Galatasaray Üniversitesi', 'Galatasaray Üniversitesi'), ('İstanbul Medeniyet Üniversitesi', 'İstanbul Medeniyet Üniversitesi'), ('İstanbul Teknik Üniversitesi', 'İstanbul Teknik Üniversitesi'), ('İstanbul Üniversitesi', 'İstanbul Üniversitesi'), ('İstanbul Üniversitesi-Cerrahpaşa', 'İstanbul Üniversitesi-Cerrahpaşa'), ('Marmara Üniversitesi', 'Marmara Üniversitesi'), ('Milli Savunma Üniversitesi\xa0(Askerî)', 'Milli Savunma Üniversitesi\xa0(Askerî)'), ('Mimar Sinan Güzel Sanatlar Üniversitesi', 'Mimar Sinan Güzel Sanatlar Üniversitesi'), ('Türkiye Uluslararası İslam, Bilim ve Teknoloji Üniversitesi', 'Türkiye Uluslararası İslam, Bilim ve Teknoloji Üniversitesi'), ('Türk-Alman Üniversitesi', 'Türk-Alman Üniversitesi'), ('Türk-Japon Bilim ve Teknoloji Üniversitesi', 'Türk-Japon Bilim ve Teknoloji Üniversitesi'), ('Sağlık Bilimleri Üniversitesi', 'Sağlık Bilimleri Üniversitesi'), ('Yıldız Teknik Üniversitesi', 'Yıldız Teknik Üniversitesi'), ('Acıbadem Üniversitesi', 'Acıbadem Üniversitesi'), ('Bahçeşehir Üniversitesi', 'Bahçeşehir Üniversitesi'), ('Beykent Üniversitesi', 'Beykent Üniversitesi'), ('Bezmialem Vakıf Üniversitesi', 'Bezmialem Vakıf Üniversitesi'), ('Biruni Üniversitesi', 'Biruni Üniversitesi'), ('Doğuş Üniversitesi', 'Doğuş Üniversitesi'), ('Fatih Sultan Mehmet Üniversitesi', 'Fatih Sultan Mehmet Üniversitesi'), ('Fenerbahçe Üniversitesi', 'Fenerbahçe Üniversitesi'), ('Gedik Üniversitesi', 'Gedik Üniversitesi'), ('Haliç Üniversitesi', 'Haliç Üniversitesi'), ('Işık Üniversitesi', 'Işık Üniversitesi'), ('İbn Haldun Üniversitesi', 'İbn Haldun Üniversitesi'), ('İstanbul 29 Mayıs Üniversitesi', 'İstanbul 29 Mayıs Üniversitesi'), ('Altınbaş Üniversitesi', 'Altınbaş Üniversitesi'), ('İstanbul Arel Üniversitesi', 'İstanbul Arel Üniversitesi'), ('İstanbul Atlas Üniversitesi', 'İstanbul Atlas Üniversitesi'), ('İstanbul Aydın Üniversitesi', 'İstanbul Aydın Üniversitesi'), ('İstanbul Ayvansaray Üniversitesi', 'İstanbul Ayvansaray Üniversitesi'), ('Beykoz Üniversitesi', 'Beykoz Üniversitesi'), ('İstanbul Bilgi Üniversitesi', 'İstanbul Bilgi Üniversitesi'), ('İstanbul Galata Üniversitesi', 'İstanbul Galata Üniversitesi'), ('Demiroğlu Bilim Üniversitesi', 'Demiroğlu Bilim Üniversitesi'), ('İstanbul Ticaret Üniversitesi', 'İstanbul Ticaret Üniversitesi'), ('İstanbul Esenyurt Üniversitesi', 'İstanbul Esenyurt Üniversitesi'), ('İstanbul Gedik Üniversitesi', 'İstanbul Gedik Üniversitesi'), ('İstanbul Gelişim Üniversitesi', 'İstanbul Gelişim Üniversitesi'), ('İstanbul Kent Üniversitesi', 'İstanbul Kent Üniversitesi'), ('İstanbul Kültür Üniversitesi', 'İstanbul Kültür Üniversitesi'), ('İstanbul Medipol Üniversitesi', 'İstanbul Medipol Üniversitesi'), ('İstanbul Okan Üniversitesi', 'İstanbul Okan Üniversitesi'), ('İstanbul Rumeli Üniversitesi', 'İstanbul Rumeli Üniversitesi'), ('İstanbul Sabahattin Zaim Üniversitesi', 'İstanbul Sabahattin Zaim Üniversitesi'), ('İstinye Üniversitesi', 'İstinye Üniversitesi'), ('Kadir Has Üniversitesi', 'Kadir Has Üniversitesi'), ('Koç Üniversitesi', 'Koç Üniversitesi'), ('Maltepe Üniversitesi', 'Maltepe Üniversitesi'), ('MEF Üniversitesi', 'MEF Üniversitesi'), ('Nişantaşı Üniversitesi', 'Nişantaşı Üniversitesi'), ('Özyeğin Üniversitesi', 'Özyeğin Üniversitesi'), ('Piri Reis Üniversitesi', 'Piri Reis Üniversitesi'), ('Sabancı Üniversitesi', 'Sabancı Üniversitesi'), ('İstanbul Sağlık ve Teknoloji Üniversitesi', 'İstanbul Sağlık ve Teknoloji Üniversitesi'), ('Üsküdar Üniversitesi', 'Üsküdar Üniversitesi'), ('Yeditepe Üniversitesi', 'Yeditepe Üniversitesi'), ('Yeni Yüzyıl Üniversitesi', 'Yeni Yüzyıl Üniversitesi'), ('Dokuz Eylül Üniversitesi', 'Dokuz Eylül Üniversitesi'), ('Ege Üniversitesi', 'Ege Üniversitesi'), ('İzmir Yüksek Teknoloji Enstitüsü', 'İzmir Yüksek Teknoloji Enstitüsü'), ('İzmir Kâtip Çelebi Üniversitesi', 'İzmir Kâtip Çelebi Üniversitesi'), ('İzmir Bakırçay Üniversitesi', 'İzmir Bakırçay Üniversitesi'), ('İzmir Demokrasi Üniversitesi', 'İzmir Demokrasi Üniversitesi'), ('İzmir Ekonomi Üniversitesi', 'İzmir Ekonomi Üniversitesi'), ('İzmir Tınaztepe Üniversitesi', 'İzmir Tınaztepe Üniversitesi'), ('Yaşar Üniversitesi', 'Yaşar Üniversitesi'), ('Kahramanmaraş Sütçü İmam Üniversitesi', 'Kahramanmaraş Sütçü İmam Üniversitesi'), ('Kahramanmaraş İstiklal Üniversitesi', 'Kahramanmaraş İstiklal Üniversitesi'), ('Karabük Üniversitesi', 'Karabük Üniversitesi'), ('Karamanoğlu Mehmetbey Üniversitesi', 'Karamanoğlu Mehmetbey Üniversitesi'), ('Kafkas Üniversitesi', 'Kafkas Üniversitesi'), ('Kastamonu Üniversitesi', 'Kastamonu Üniversitesi'), ('Abdullah Gül Üniversitesi', 'Abdullah Gül Üniversitesi'), ('Erciyes Üniversitesi', 'Erciyes Üniversitesi'), ('Kayseri Üniversitesi', 'Kayseri Üniversitesi'), ('Nuh Naci Yazgan Üniversitesi', 'Nuh Naci Yazgan Üniversitesi'), ('Kırıkkale Üniversitesi', 'Kırıkkale Üniversitesi'), ('Kırklareli Üniversitesi', 'Kırklareli Üniversitesi'), ('Kırşehir Ahi Evran Üniversitesi', 'Kırşehir Ahi Evran Üniversitesi'), ('Kilis 7 Aralık Üniversitesi', 'Kilis 7 Aralık Üniversitesi'), ('Gebze Teknik Üniversitesi', 'Gebze Teknik Üniversitesi'), ('Kocaeli Üniversitesi', 'Kocaeli Üniversitesi'), ('Kocaeli Sağlık ve Teknoloji Üniversitesi', 'Kocaeli Sağlık ve Teknoloji Üniversitesi'), ('Konya Teknik Üniversitesi', 'Konya Teknik Üniversitesi'), ('Necmettin Erbakan Üniversitesi', 'Necmettin Erbakan Üniversitesi'), ('Selçuk Üniversitesi', 'Selçuk Üniversitesi'), ('Konya Gıda ve Tarım Üniversitesi', 'Konya Gıda ve Tarım Üniversitesi'), ('KTO Karatay Üniversitesi', 'KTO Karatay Üniversitesi'), ('Kütahya Dumlupınar Üniversitesi', 'Kütahya Dumlupınar Üniversitesi'), ('Kütahya Sağlık Bilimleri Üniversitesi', 'Kütahya Sağlık Bilimleri Üniversitesi'), ('İnönü Üniversitesi', 'İnönü Üniversitesi'), ('Malatya Turgut Özal Üniversitesi', 'Malatya Turgut Özal Üniversitesi'), ('Manisa Celal Bayar Üniversitesi', 'Manisa Celal Bayar Üniversitesi'), ('Mardin Artuklu Üniversitesi', 'Mardin Artuklu Üniversitesi'), ('Mersin Üniversitesi', 'Mersin Üniversitesi'), ('Tarsus Üniversitesi', 'Tarsus Üniversitesi'), ('Çağ Üniversitesi', 'Çağ Üniversitesi'), ('Toros Üniversitesi', 'Toros Üniversitesi'), ('Muğla Sıtkı Koçman Üniversitesi', 'Muğla Sıtkı Koçman Üniversitesi'), ('Muş Alparslan Üniversitesi', 'Muş Alparslan Üniversitesi'), ('Nevşehir Hacı Bektaş Veli Üniversitesi', 'Nevşehir Hacı Bektaş Veli Üniversitesi'), ('Kapadokya Üniversitesi', 'Kapadokya Üniversitesi'), ('Niğde Ömer Halisdemir Üniversitesi', 'Niğde Ömer Halisdemir Üniversitesi'), ('Ordu Üniversitesi', 'Ordu Üniversitesi'), ('Osmaniye Korkut Ata Üniversitesi', 'Osmaniye Korkut Ata Üniversitesi'), ('Recep Tayyip Erdoğan Üniversitesi', 'Recep Tayyip Erdoğan Üniversitesi'), ('Sakarya Üniversitesi', 'Sakarya Üniversitesi'), ('Sakarya Uygulamalı Bilimler Üniversitesi', 'Sakarya Uygulamalı Bilimler Üniversitesi'), ('Ondokuz Mayıs Üniversitesi', 'Ondokuz Mayıs Üniversitesi'), ('Samsun Üniversitesi', 'Samsun Üniversitesi'), ('Siirt Üniversitesi', 'Siirt Üniversitesi'), ('Sinop Üniversitesi', 'Sinop Üniversitesi'), ('Sivas Cumhuriyet Üniversitesi', 'Sivas Cumhuriyet Üniversitesi'), ('Sivas Bilim ve Teknoloji Üniversitesi', 'Sivas Bilim ve Teknoloji Üniversitesi'), ('Harran Üniversitesi', 'Harran Üniversitesi'), ('Şırnak Üniversitesi', 'Şırnak Üniversitesi'), ('Tekirdağ Namık Kemal Üniversitesi', 'Tekirdağ Namık Kemal Üniversitesi'), ('Tokat Gaziosmanpaşa Üniversitesi', 'Tokat Gaziosmanpaşa Üniversitesi'), ('Karadeniz Teknik Üniversitesi', 'Karadeniz Teknik Üniversitesi'), ('Trabzon Üniversitesi', 'Trabzon Üniversitesi'), ('Avrasya Üniversitesi', 'Avrasya Üniversitesi'), ('Munzur Üniversitesi', 'Munzur Üniversitesi'), ('Uşak Üniversitesi', 'Uşak Üniversitesi'), ('Van Yüzüncü Yıl Üniversitesi', 'Van Yüzüncü Yıl Üniversitesi'), ('Yalova Üniversitesi', 'Yalova Üniversitesi'), ('Yozgat Bozok Üniversitesi', 'Yozgat Bozok Üniversitesi'), ('Zonguldak Bülent Ecevit Üniversitesi', 'Zonguldak Bülent Ecevit Üniversitesi')], max_length=250, null=True, verbose_name='Bootcamp Adı'),
        ),
        migrations.AlterField(
            model_name='company',
            name='girisim_kategorisi',
            field=models.CharField(choices=[('Agriculture', 'Agriculture'), ('Biotechnology', 'Biotechnology'), ('Business Services', 'Business Services'), ('Clean Technology', 'Clean Technology'), ('Construction', 'Construction'), ('Consulting', 'Consulting'), ('Consumer Products', 'Consumer Products'), ('Consumer Services', 'Consumer Services'), ('Digital Marketing', 'Digital Marketing'), ('Education', 'Education'), ('Electronics / Instrumentation', 'Electronics / Instrumentation'), ('Energy', 'Energy'), ('Fashion', 'Fashion'), ('Financial Services', 'Financial Services'), ('Fintech', 'Fintech'), ('Food and Beverage', 'Food and Beverage'), ('Gaming', 'Gaming'), ('Healthcare Services', 'Healthcare Services'), ('Internet / Web Services', 'Internet / Web Services'), ('IT Services', 'IT Services'), ('Legal', 'Legal'), ('Lifestyle', 'Lifestyle'), ('Marine', 'Marine'), ('Maritime/Shipping', 'Maritime/Shipping'), ('Marketing / Advertising', 'Marketing / Advertising'), ('Media and Entertainment', 'Media and Entertainment'), ('Medical Devices and Equipment', 'Medical Devices and Equipment'), ('Mobility', 'Mobility'), ('Nanotechnology', 'Nanotechnology'), ('Real Estate', 'Real Estate'), ('Retailing / Distribution', 'Retailing / Distribution'), ('Robotics', 'Robotics'), ('Security', 'Security'), ('Software', 'Software'), ('Sports', 'Sports'), ('Telecommunications', 'Telecommunications'), ('Transportation', 'Transportation'), ('Travel', 'Travel'), ('Other', 'Other')], max_length=250, null=True, verbose_name='Girişim Kategorisi'),
        ),
    ]
