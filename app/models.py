# from django.db import models
# from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from onBoarding import settings

"""Declare models for YOUR_APP app."""

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django_vimeo import fields
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


Cities = [
    ('Adana', 'Adana'),
    ('Adıyaman', 'Adıyaman'),
    ('Afyonkarahisar', 'Afyonkarahisar'),
    ('Ağrı', 'Ağrı'),
    ('Aksaray', 'Aksaray'),
    ('Amasya', 'Amasya'),
    ('Ankara', 'Ankara'),
    ('Antalya', 'Antalya'),
    ('Ardahan', 'Ardahan'),
    ('Artvin', 'Artvin'),
    ('Aydın', 'Aydın'),
    ('Balıkesir', 'Balıkesir'),
    ('Bartın', 'Bartın'),
    ('Batman', 'Batman'),
    ('Bayburt', 'Bayburt'),
    ('Bilecik', 'Bilecik'),
    ('Bingöl', 'Bingöl'),
    ('Bitlis', 'Bitlis'),
    ('Bolu', 'Bolu'),
    ('Burdur', 'Burdur'),
    ('Bursa', 'Bursa'),
    ('Çanakkale', 'Çanakkale'),
    ('Çankırı', 'Çankırı'),
    ('Çorum', 'Çorum'),
    ('Denizli', 'Denizli'),
    ('Diyarbakır', 'Diyarbakır'),
    ('Düzce', 'Düzce'),
    ('Edirne', 'Edirne'),
    ('Elazığ', 'Elazığ'),
    ('Erzincan', 'Erzincan'),
    ('Erzurum', 'Erzurum'),
    ('Eskişehir', 'Eskişehir'),
    ('Gaziantep', 'Gaziantep'),
    ('Giresun', 'Giresun'),
    ('Gümüşhane', 'Gümüşhane'),
    ('Hakkâri', 'Hakkâri'),
    ('Hatay', 'Hatay'),
    ('Iğdır', 'Iğdır'),
    ('Isparta', 'Isparta'),
    ('İstanbul', 'İstanbul'),
    ('İzmir', 'İzmir'),
    ('Kahramanmaraş', 'Kahramanmaraş'),
    ('Karabük', 'Karabük'),
    ('Karaman', 'Karaman'),
    ('Kars', 'Kars'),
    ('Kastamonu', 'Kastamonu'),
    ('Kayseri', 'Kayseri'),
    ('Kilis', 'Kilis'),
    ('Kırıkkale', 'Kırıkkale'),
    ('Kırklareli', 'Kırklareli'),
    ('Kırşehir', 'Kırşehir'),
    ('Kocaeli', 'Kocaeli'),
    ('Konya', 'Konya'),
    ('Kütahya', 'Kütahya'),
    ('Malatya', 'Malatya'),
    ('Manisa', 'Manisa'),
    ('Mardin', 'Mardin'),
    ('Mersin', 'Mersin'),
    ('Muğla', 'Muğla'),
    ('Muş', 'Muş'),
    ('Nevşehir', 'Nevşehir'),
    ('Niğde', 'Niğde'),
    ('Ordu', 'Ordu'),
    ('Osmaniye', 'Osmaniye'),
    ('Rize', 'Rize'),
    ('Sakarya', 'Sakarya'),
    ('Samsun', 'Samsun'),
    ('Şanlıurfa', 'Şanlıurfa'),
    ('Siirt', 'Siirt'),
    ('Sinop', 'Sinop'),
    ('Sivas', 'Sivas'),
    ('Şırnak', 'Şırnak'),
    ('Tekirdağ', 'Tekirdağ'),
    ('Tokat', 'Tokat'),
    ('Trabzon', 'Trabzon'),
    ('Tunceli', 'Tunceli'),
    ('Uşak', 'Uşak'),
    ('Van', 'Van'),
    ('Yalova', 'Yalova'),
    ('Yozgat', 'Yozgat'),
    ('Zonguldak', 'Zonguldak'),
]

Cinsiyetler = [('Erkek', 'Erkek'), ('Kadın', 'Kadın')]

ContentTypes = [('Text', 'Text'), ('Video', 'Video'), ('Anket', 'Anket')]

Is_Tech_Exist = [('Var', 'Var'), ('Yok', 'Yok')]

Siniflar = [
    ('Mezun', 'Mezun'),
    ('Hazırlık', 'Hazırlık'),
    ('1. Sınıf', '1. Sınıf'),
    ('2. Sınıf', '2. Sınıf'),
    ('3. Sınıf', '3. Sınıf'),
    ('4. Sınıf', '4. Sınıf'),
    ('5. Sınıf', '5. Sınıf'),
    ('6. Sınıf', '6. Sınıf'),
    ('Yüksek Lisans', 'Yüksek Lisans'),
    ('Doktora', 'Doktora'),
    ('Diğer', 'Diğer'),
]

universiteler = [
    (
        'Adana Alparslan Türkeş Bilim ve Teknoloji Üniversitesi',
        'Adana Alparslan Türkeş Bilim ve Teknoloji Üniversitesi'),
    ('Çukurova Üniversitesi', 'Çukurova Üniversitesi'),
    ('Adıyaman Üniversitesi', 'Adıyaman Üniversitesi'),
    ('Afyon Kocatepe Üniversitesi', 'Afyon Kocatepe Üniversitesi'),
    ('Afyonkarahisar Sağlık Bilimleri Üniversitesi', 'Afyonkarahisar Sağlık Bilimleri Üniversitesi'),
    ('Ağrı İbrahim Çeçen Üniversitesi', 'Ağrı İbrahim Çeçen Üniversitesi'),
    ('Aksaray Üniversitesi', 'Aksaray Üniversitesi'),
    ('Amasya Üniversitesi', 'Amasya Üniversitesi'),
    ('Ankara Üniversitesi', 'Ankara Üniversitesi'),
    ('Ankara Müzik ve Güzel Sanatlar Üniversitesi', 'Ankara Müzik ve Güzel Sanatlar Üniversitesi'),
    ('Ankara Hacı Bayram Veli Üniversitesi', 'Ankara Hacı Bayram Veli Üniversitesi'),
    ('Ankara Sosyal Bilimler Üniversitesi', 'Ankara Sosyal Bilimler Üniversitesi'),
    ('Gazi Üniversitesi', 'Gazi Üniversitesi'),
    ('Hacettepe Üniversitesi', 'Hacettepe Üniversitesi'),
    ('Orta Doğu Teknik Üniversitesi', 'Orta Doğu Teknik Üniversitesi'),
    ('Ankara Yıldırım Beyazıt Üniversitesi', 'Ankara Yıldırım Beyazıt Üniversitesi'),
    ('Polis Akademisi', 'Polis Akademisi'),
    ('Anka Teknoloji Üniversitesi', 'Anka Teknoloji Üniversitesi'),
    ('Ankara Bilim Üniversitesi', 'Ankara Bilim Üniversitesi'),
    ('Ankara Medipol Üniversitesi', 'Ankara Medipol Üniversitesi'),
    ('Atılım Üniversitesi', 'Atılım Üniversitesi'),
    ('Başkent Üniversitesi', 'Başkent Üniversitesi'),
    ('Çankaya Üniversitesi', 'Çankaya Üniversitesi'),
    ('İhsan Doğramacı Bilkent Üniversitesi', 'İhsan Doğramacı Bilkent Üniversitesi'),
    ('Lokman Hekim Üniversitesi', 'Lokman Hekim Üniversitesi'),
    ('Ostim Teknik Üniversitesi', 'Ostim Teknik Üniversitesi'),
    ('TED Üniversitesi', 'TED Üniversitesi'),
    ('TOBB Ekonomi ve Teknoloji Üniversitesi', 'TOBB Ekonomi ve Teknoloji Üniversitesi'),
    ('Ufuk Üniversitesi', 'Ufuk Üniversitesi'),
    ('Türk Hava Kurumu Üniversitesi', 'Türk Hava Kurumu Üniversitesi'),
    ('Yüksek İhtisas Üniversitesi', 'Yüksek İhtisas Üniversitesi'),
    ('Akdeniz Üniversitesi', 'Akdeniz Üniversitesi'),
    ('Alanya Alaaddin Keykubat Üniversitesi', 'Alanya Alaaddin Keykubat Üniversitesi'),
    ('Alanya Hamdullah Emin Paşa Üniversitesi', 'Alanya Hamdullah Emin Paşa Üniversitesi'),
    ('Antalya Akev Üniversitesi', 'Antalya Akev Üniversitesi'),
    ('Antalya Bilim Üniversitesi', 'Antalya Bilim Üniversitesi'),
    ('Ardahan Üniversitesi', 'Ardahan Üniversitesi'),
    ('Artvin Çoruh Üniversitesi', 'Artvin Çoruh Üniversitesi'),
    ('Aydın Adnan Menderes Üniversitesi', 'Aydın Adnan Menderes Üniversitesi'),
    ('Balıkesir Üniversitesi', 'Balıkesir Üniversitesi'),
    ('Bandırma Onyedi Eylül Üniversitesi', 'Bandırma Onyedi Eylül Üniversitesi'),
    ('Bartın Üniversitesi', 'Bartın Üniversitesi'),
    ('Batman Üniversitesi', 'Batman Üniversitesi'),
    ('Bayburt Üniversitesi', 'Bayburt Üniversitesi'),
    ('Bilecik Şeyh Edebali Üniversitesi', 'Bilecik Şeyh Edebali Üniversitesi'),
    ('Bingöl Üniversitesi', 'Bingöl Üniversitesi'),
    ('Bitlis Eren Üniversitesi', 'Bitlis Eren Üniversitesi'),
    ('Bolu Abant İzzet Baysal Üniversitesi', 'Bolu Abant İzzet Baysal Üniversitesi'),
    ('Burdur Mehmet Akif Ersoy Üniversitesi', 'Burdur Mehmet Akif Ersoy Üniversitesi'),
    ('Bursa Teknik Üniversitesi', 'Bursa Teknik Üniversitesi'),
    ('Bursa Uludağ Üniversitesi', 'Bursa Uludağ Üniversitesi'),
    ('Çanakkale Onsekiz Mart Üniversitesi', 'Çanakkale Onsekiz Mart Üniversitesi'),
    ('Çankırı Karatekin Üniversitesi', 'Çankırı Karatekin Üniversitesi'),
    ('Hitit Üniversitesi', 'Hitit Üniversitesi'),
    ('Pamukkale Üniversitesi', 'Pamukkale Üniversitesi'),
    ('Dicle Üniversitesi', 'Dicle Üniversitesi'),
    ('Düzce Üniversitesi', 'Düzce Üniversitesi'),
    ('Trakya Üniversitesi', 'Trakya Üniversitesi'),
    ('Fırat Üniversitesi', 'Fırat Üniversitesi'),
    ('Erzincan Binali Yıldırım Üniversitesi', 'Erzincan Binali Yıldırım Üniversitesi'),
    ('Atatürk Üniversitesi', 'Atatürk Üniversitesi'),
    ('Erzurum Teknik Üniversitesi', 'Erzurum Teknik Üniversitesi'),
    ('Anadolu Üniversitesi', 'Anadolu Üniversitesi'),
    ('Eskişehir Osmangazi Üniversitesi', 'Eskişehir Osmangazi Üniversitesi'),
    ('Eskişehir Teknik Üniversitesi', 'Eskişehir Teknik Üniversitesi'),
    ('Gaziantep Üniversitesi', 'Gaziantep Üniversitesi'),
    ('Gaziantep İslam Bilim ve Teknoloji Üniversitesi', 'Gaziantep İslam Bilim ve Teknoloji Üniversitesi'),
    ('Hasan Kalyoncu Üniversitesi', 'Hasan Kalyoncu Üniversitesi'),
    ('Sanko Üniversitesi', 'Sanko Üniversitesi'),
    ('Giresun Üniversitesi', 'Giresun Üniversitesi'),
    ('Gümüşhane Üniversitesi', 'Gümüşhane Üniversitesi'),
    ('Hakkari Üniversitesi', 'Hakkari Üniversitesi'),
    ('İskenderun Teknik Üniversitesi', 'İskenderun Teknik Üniversitesi'),
    ('Hatay Mustafa Kemal Üniversitesi', 'Hatay Mustafa Kemal Üniversitesi'),
    ('Iğdır Üniversitesi', 'Iğdır Üniversitesi'),
    ('Süleyman Demirel Üniversitesi', 'Süleyman Demirel Üniversitesi'),
    ('Isparta Uygulamalı Bilimler Üniversitesi', 'Isparta Uygulamalı Bilimler Üniversitesi'),
    ('Boğaziçi Üniversitesi', 'Boğaziçi Üniversitesi'),
    ('Galatasaray Üniversitesi', 'Galatasaray Üniversitesi'),
    ('İstanbul Medeniyet Üniversitesi', 'İstanbul Medeniyet Üniversitesi'),
    ('İstanbul Teknik Üniversitesi', 'İstanbul Teknik Üniversitesi'),
    ('İstanbul Üniversitesi', 'İstanbul Üniversitesi'),
    ('İstanbul Üniversitesi-Cerrahpaşa', 'İstanbul Üniversitesi-Cerrahpaşa'),
    ('Marmara Üniversitesi', 'Marmara Üniversitesi'),
    ('Milli Savunma Üniversitesi (Askerî)', 'Milli Savunma Üniversitesi (Askerî)'),
    ('Mimar Sinan Güzel Sanatlar Üniversitesi', 'Mimar Sinan Güzel Sanatlar Üniversitesi'),
    ('Türkiye Uluslararası İslam, Bilim ve Teknoloji Üniversitesi',
     'Türkiye Uluslararası İslam, Bilim ve Teknoloji Üniversitesi'),
    ('Türk-Alman Üniversitesi', 'Türk-Alman Üniversitesi'),
    ('Türk-Japon Bilim ve Teknoloji Üniversitesi', 'Türk-Japon Bilim ve Teknoloji Üniversitesi'),
    ('Sağlık Bilimleri Üniversitesi', 'Sağlık Bilimleri Üniversitesi'),
    ('Yıldız Teknik Üniversitesi', 'Yıldız Teknik Üniversitesi'),
    ('Acıbadem Üniversitesi', 'Acıbadem Üniversitesi'),
    ('Bahçeşehir Üniversitesi', 'Bahçeşehir Üniversitesi'),
    ('Beykent Üniversitesi', 'Beykent Üniversitesi'),
    ('Bezmialem Vakıf Üniversitesi', 'Bezmialem Vakıf Üniversitesi'),
    ('Biruni Üniversitesi', 'Biruni Üniversitesi'),
    ('Doğuş Üniversitesi', 'Doğuş Üniversitesi'),
    ('Fatih Sultan Mehmet Üniversitesi', 'Fatih Sultan Mehmet Üniversitesi'),
    ('Fenerbahçe Üniversitesi', 'Fenerbahçe Üniversitesi'),
    ('Gedik Üniversitesi', 'Gedik Üniversitesi'),
    ('Haliç Üniversitesi', 'Haliç Üniversitesi'),
    ('Işık Üniversitesi', 'Işık Üniversitesi'),
    ('İbn Haldun Üniversitesi', 'İbn Haldun Üniversitesi'),
    ('İstanbul 29 Mayıs Üniversitesi', 'İstanbul 29 Mayıs Üniversitesi'),
    ('Altınbaş Üniversitesi', 'Altınbaş Üniversitesi'),
    ('İstanbul Arel Üniversitesi', 'İstanbul Arel Üniversitesi'),
    ('İstanbul Atlas Üniversitesi', 'İstanbul Atlas Üniversitesi'),
    ('İstanbul Aydın Üniversitesi', 'İstanbul Aydın Üniversitesi'),
    ('İstanbul Ayvansaray Üniversitesi', 'İstanbul Ayvansaray Üniversitesi'),
    ('Beykoz Üniversitesi', 'Beykoz Üniversitesi'),
    ('İstanbul Bilgi Üniversitesi', 'İstanbul Bilgi Üniversitesi'),
    ('İstanbul Galata Üniversitesi', 'İstanbul Galata Üniversitesi'),
    ('Demiroğlu Bilim Üniversitesi', 'Demiroğlu Bilim Üniversitesi'),
    ('İstanbul Ticaret Üniversitesi', 'İstanbul Ticaret Üniversitesi'),
    ('İstanbul Esenyurt Üniversitesi', 'İstanbul Esenyurt Üniversitesi'),
    ('İstanbul Gedik Üniversitesi', 'İstanbul Gedik Üniversitesi'),
    ('İstanbul Gelişim Üniversitesi', 'İstanbul Gelişim Üniversitesi'),
    ('İstanbul Kent Üniversitesi', 'İstanbul Kent Üniversitesi'),
    ('İstanbul Kültür Üniversitesi', 'İstanbul Kültür Üniversitesi'),
    ('İstanbul Medipol Üniversitesi', 'İstanbul Medipol Üniversitesi'),
    ('İstanbul Okan Üniversitesi', 'İstanbul Okan Üniversitesi'),
    ('İstanbul Rumeli Üniversitesi', 'İstanbul Rumeli Üniversitesi'),
    ('İstanbul Sabahattin Zaim Üniversitesi', 'İstanbul Sabahattin Zaim Üniversitesi'),
    ('İstinye Üniversitesi', 'İstinye Üniversitesi'),
    ('Kadir Has Üniversitesi', 'Kadir Has Üniversitesi'),
    ('Koç Üniversitesi', 'Koç Üniversitesi'),
    ('Maltepe Üniversitesi', 'Maltepe Üniversitesi'),
    ('MEF Üniversitesi', 'MEF Üniversitesi'),
    ('Nişantaşı Üniversitesi', 'Nişantaşı Üniversitesi'),
    ('Özyeğin Üniversitesi', 'Özyeğin Üniversitesi'),
    ('Piri Reis Üniversitesi', 'Piri Reis Üniversitesi'),
    ('Sabancı Üniversitesi', 'Sabancı Üniversitesi'),
    ('İstanbul Sağlık ve Teknoloji Üniversitesi', 'İstanbul Sağlık ve Teknoloji Üniversitesi'),
    ('Üsküdar Üniversitesi', 'Üsküdar Üniversitesi'),
    ('Yeditepe Üniversitesi', 'Yeditepe Üniversitesi'),
    ('Yeni Yüzyıl Üniversitesi', 'Yeni Yüzyıl Üniversitesi'),
    ('Dokuz Eylül Üniversitesi', 'Dokuz Eylül Üniversitesi'),
    ('Ege Üniversitesi', 'Ege Üniversitesi'),
    ('İzmir Yüksek Teknoloji Enstitüsü', 'İzmir Yüksek Teknoloji Enstitüsü'),
    ('İzmir Kâtip Çelebi Üniversitesi', 'İzmir Kâtip Çelebi Üniversitesi'),
    ('İzmir Bakırçay Üniversitesi', 'İzmir Bakırçay Üniversitesi'),
    ('İzmir Demokrasi Üniversitesi', 'İzmir Demokrasi Üniversitesi'),
    ('İzmir Ekonomi Üniversitesi', 'İzmir Ekonomi Üniversitesi'),
    ('İzmir Tınaztepe Üniversitesi', 'İzmir Tınaztepe Üniversitesi'),
    ('Yaşar Üniversitesi', 'Yaşar Üniversitesi'),
    ('Kahramanmaraş Sütçü İmam Üniversitesi', 'Kahramanmaraş Sütçü İmam Üniversitesi'),
    ('Kahramanmaraş İstiklal Üniversitesi', 'Kahramanmaraş İstiklal Üniversitesi'),
    ('Karabük Üniversitesi', 'Karabük Üniversitesi'),
    ('Karamanoğlu Mehmetbey Üniversitesi', 'Karamanoğlu Mehmetbey Üniversitesi'),
    ('Kafkas Üniversitesi', 'Kafkas Üniversitesi'),
    ('Kastamonu Üniversitesi', 'Kastamonu Üniversitesi'),
    ('Abdullah Gül Üniversitesi', 'Abdullah Gül Üniversitesi'),
    ('Erciyes Üniversitesi', 'Erciyes Üniversitesi'),
    ('Kayseri Üniversitesi', 'Kayseri Üniversitesi'),
    ('Nuh Naci Yazgan Üniversitesi', 'Nuh Naci Yazgan Üniversitesi'),
    ('Kırıkkale Üniversitesi', 'Kırıkkale Üniversitesi'),
    ('Kırklareli Üniversitesi', 'Kırklareli Üniversitesi'),
    ('Kırşehir Ahi Evran Üniversitesi', 'Kırşehir Ahi Evran Üniversitesi'),
    ('Kilis 7 Aralık Üniversitesi', 'Kilis 7 Aralık Üniversitesi'),
    ('Gebze Teknik Üniversitesi', 'Gebze Teknik Üniversitesi'),
    ('Kocaeli Üniversitesi', 'Kocaeli Üniversitesi'),
    ('Kocaeli Sağlık ve Teknoloji Üniversitesi', 'Kocaeli Sağlık ve Teknoloji Üniversitesi'),
    ('Konya Teknik Üniversitesi', 'Konya Teknik Üniversitesi'),
    ('Necmettin Erbakan Üniversitesi', 'Necmettin Erbakan Üniversitesi'),
    ('Selçuk Üniversitesi', 'Selçuk Üniversitesi'),
    ('Konya Gıda ve Tarım Üniversitesi', 'Konya Gıda ve Tarım Üniversitesi'),
    ('KTO Karatay Üniversitesi', 'KTO Karatay Üniversitesi'),
    ('Kütahya Dumlupınar Üniversitesi', 'Kütahya Dumlupınar Üniversitesi'),
    ('Kütahya Sağlık Bilimleri Üniversitesi', 'Kütahya Sağlık Bilimleri Üniversitesi'),
    ('İnönü Üniversitesi', 'İnönü Üniversitesi'),
    ('Malatya Turgut Özal Üniversitesi', 'Malatya Turgut Özal Üniversitesi'),
    ('Manisa Celal Bayar Üniversitesi', 'Manisa Celal Bayar Üniversitesi'),
    ('Mardin Artuklu Üniversitesi', 'Mardin Artuklu Üniversitesi'),
    ('Mersin Üniversitesi', 'Mersin Üniversitesi'),
    ('Tarsus Üniversitesi', 'Tarsus Üniversitesi'),
    ('Çağ Üniversitesi', 'Çağ Üniversitesi'),
    ('Toros Üniversitesi', 'Toros Üniversitesi'),
    ('Muğla Sıtkı Koçman Üniversitesi', 'Muğla Sıtkı Koçman Üniversitesi'),
    ('Muş Alparslan Üniversitesi', 'Muş Alparslan Üniversitesi'),
    ('Nevşehir Hacı Bektaş Veli Üniversitesi', 'Nevşehir Hacı Bektaş Veli Üniversitesi'),
    ('Kapadokya Üniversitesi', 'Kapadokya Üniversitesi'),
    ('Niğde Ömer Halisdemir Üniversitesi', 'Niğde Ömer Halisdemir Üniversitesi'),
    ('Ordu Üniversitesi', 'Ordu Üniversitesi'),
    ('Osmaniye Korkut Ata Üniversitesi', 'Osmaniye Korkut Ata Üniversitesi'),
    ('Recep Tayyip Erdoğan Üniversitesi', 'Recep Tayyip Erdoğan Üniversitesi'),
    ('Sakarya Üniversitesi', 'Sakarya Üniversitesi'),
    ('Sakarya Uygulamalı Bilimler Üniversitesi', 'Sakarya Uygulamalı Bilimler Üniversitesi'),
    ('Ondokuz Mayıs Üniversitesi', 'Ondokuz Mayıs Üniversitesi'),
    ('Samsun Üniversitesi', 'Samsun Üniversitesi'),
    ('Siirt Üniversitesi', 'Siirt Üniversitesi'),
    ('Sinop Üniversitesi', 'Sinop Üniversitesi'),
    ('Sivas Cumhuriyet Üniversitesi', 'Sivas Cumhuriyet Üniversitesi'),
    ('Sivas Bilim ve Teknoloji Üniversitesi', 'Sivas Bilim ve Teknoloji Üniversitesi'),
    ('Harran Üniversitesi', 'Harran Üniversitesi'),
    ('Şırnak Üniversitesi', 'Şırnak Üniversitesi'),
    ('Tekirdağ Namık Kemal Üniversitesi', 'Tekirdağ Namık Kemal Üniversitesi'),
    ('Tokat Gaziosmanpaşa Üniversitesi', 'Tokat Gaziosmanpaşa Üniversitesi'),
    ('Karadeniz Teknik Üniversitesi', 'Karadeniz Teknik Üniversitesi'),
    ('Trabzon Üniversitesi', 'Trabzon Üniversitesi'),
    ('Avrasya Üniversitesi', 'Avrasya Üniversitesi'),
    ('Munzur Üniversitesi', 'Munzur Üniversitesi'),
    ('Uşak Üniversitesi', 'Uşak Üniversitesi'),
    ('Van Yüzüncü Yıl Üniversitesi', 'Van Yüzüncü Yıl Üniversitesi'),
    ('Yalova Üniversitesi', 'Yalova Üniversitesi'),
    ('Yozgat Bozok Üniversitesi', 'Yozgat Bozok Üniversitesi'),
    ('Zonguldak Bülent Ecevit Üniversitesi', 'Zonguldak Bülent Ecevit Üniversitesi'),
]

bolumler = [
    ('Acil Durum ve Afet Yönetimi', 'Acil Durum ve Afet Yönetimi'),
    ('Acil Yardım ve Afet Yönetimi', 'Acil Yardım ve Afet Yönetimi'),
    ('Adalet', 'Adalet'),
    ('Adli Bilimler', 'Adli Bilimler'),
    ('Adli Bilişim Mühendisliği', 'Adli Bilişim Mühendisliği'),
    ('Ağaç İşleri Endüstri Mühendisliği', 'Ağaç İşleri Endüstri Mühendisliği'),
    ('Ağız ve Diş Sağlığı', 'Ağız ve Diş Sağlığı'),
    ('Aile ve Tüketici Bilimleri', 'Aile ve Tüketici Bilimleri'),
    ('Aktüerya Bilimleri', 'Aktüerya Bilimleri'),
    ('Alman Dili ve Edebiyatı  ', 'Alman Dili ve Edebiyatı  '),
    ('Almanca Mütercim ve Tercümanlık  ', 'Almanca Mütercim ve Tercümanlık  '),
    ('Almanca Öğretmenliği  ', 'Almanca Öğretmenliği  '),
    ('Alternatif Enerji Kaynakları Teknolojisi ', 'Alternatif Enerji Kaynakları Teknolojisi '),
    ('Ambalaj Tasarımı ', 'Ambalaj Tasarımı '),
    ('Ameliyathane Hizmetleri ', 'Ameliyathane Hizmetleri '),
    ('Amerikan Kültürü ve Edebiyatı  ', 'Amerikan Kültürü ve Edebiyatı  '),
    ('Anestezi ', 'Anestezi '),
    ('Antrenörlük Eğitimi  ', 'Antrenörlük Eğitimi  '),
    ('Antropoloji  ', 'Antropoloji  '),
    ('Arap Dili ve Edebiyatı  ', 'Arap Dili ve Edebiyatı  '),
    ('Arapça Mütercim ve Tercümanlık  ', 'Arapça Mütercim ve Tercümanlık  '),
    ('Arapça Öğretmenliği  ', 'Arapça Öğretmenliği  '),
    ('Arıcılık ', 'Arıcılık '),
    ('Arkeoloji  ', 'Arkeoloji  '),
    ('Arkeoloji ve Sanat Tarihi  ', 'Arkeoloji ve Sanat Tarihi  '),
    ('Arnavut Dili ve Edebiyatı  ', 'Arnavut Dili ve Edebiyatı  '),
    ('Aşçılık ', 'Aşçılık '),
    ('Astronomi ve Uzay Bilimleri  ', 'Astronomi ve Uzay Bilimleri  '),
    ('Atçılık ve Antrenörlüğü ', 'Atçılık ve Antrenörlüğü '),
    ('Atık Yönetimi ', 'Atık Yönetimi '),
    ('Avcılık ve Yaban Hayatı ', 'Avcılık ve Yaban Hayatı '),
    ('Ayakkabı Tasarım ve Üretimi (2 Yıllık)', 'Ayakkabı Tasarım ve Üretimi (2 Yıllık)'),
    ('Ayakkabı Tasarımı ve Üretimi (4 Yıllık', 'Ayakkabı Tasarımı ve Üretimi (4 Yıllık'),
    ('Azerbaycan Türkçesi ve Edebiyatı  ', 'Azerbaycan Türkçesi ve Edebiyatı  '),
    ('Bağcılık ', 'Bağcılık '),
    ('Bahçe Bitkileri  ', 'Bahçe Bitkileri  '),
    ('Bahçe Tarımı ', 'Bahçe Tarımı '),
    ('Balıkçılık Teknolojisi Mühendisliği  ', 'Balıkçılık Teknolojisi Mühendisliği  '),
    ('Bankacılık  ', 'Bankacılık  '),
    ('Bankacılık ve Finans  ', 'Bankacılık ve Finans  '),
    ('Bankacılık ve Sigortacılık (2 Yıllık)', 'Bankacılık ve Sigortacılık (2 Yıllık)'),
    ('Bankacılık ve Sigortacılık (4 Yıllık)', 'Bankacılık ve Sigortacılık (4 Yıllık)'),
    ('Basım Teknolojileri  ', 'Basım Teknolojileri  '),
    ('Basım ve Yayım Teknolojileri ', 'Basım ve Yayım Teknolojileri '),
    ('Basın ve Yayın  ', 'Basın ve Yayın  '),
    ('Batı Dilleri  ', 'Batı Dilleri  '),
    ('Beden Eğitimi ve Spor Öğretmenliği  ', 'Beden Eğitimi ve Spor Öğretmenliği  '),
    ('Beslenme ve Diyetetik  ', 'Beslenme ve Diyetetik  '),
    ('Bilgi Güvenliği Teknolojisi  ', 'Bilgi Güvenliği Teknolojisi  '),
    ('Bilgi ve Belge Yönetimi  ', 'Bilgi ve Belge Yönetimi  '),
    ('Bilgi Yönetimi ', 'Bilgi Yönetimi '),
    ('Bilgisayar Bilimleri  ', 'Bilgisayar Bilimleri  '),
    ('Bilgisayar Destekli Tasarım ve Animasyon ', 'Bilgisayar Destekli Tasarım ve Animasyon '),
    ('Bilgisayar Mühendisliği  ', 'Bilgisayar Mühendisliği  '),
    ('Bilgisayar Operatörlüğü ', 'Bilgisayar Operatörlüğü '),
    ('Bilgisayar Programcılığı ', 'Bilgisayar Programcılığı '),
    ('Bilgisayar Teknolojisi ', 'Bilgisayar Teknolojisi '),
    ('Bilgisayar Teknolojisi ve Bilişim Sistemleri  ', 'Bilgisayar Teknolojisi ve Bilişim Sistemleri  '),
    ('Bilgisayar ve Öğretim Teknolojileri Öğretmenliği  ', 'Bilgisayar ve Öğretim Teknolojileri Öğretmenliği  '),
    ('Bilim Tarihi  ', 'Bilim Tarihi  '),
    ('Bilişim Güvenliği Teknolojisi ', 'Bilişim Güvenliği Teknolojisi '),
    ('Bilişim Sistemleri Mühendisliği  ', 'Bilişim Sistemleri Mühendisliği  '),
    ('Bilişim Sistemleri ve Teknolojileri  ', 'Bilişim Sistemleri ve Teknolojileri  '),
    ('Bitki Koruma (2 Yıllık)', 'Bitki Koruma (2 Yıllık)'),
    ('Bitki Koruma (4 Yıllık)', 'Bitki Koruma (4 Yıllık)'),
    ('Bitkisel Üretim ve Teknolojileri  ', 'Bitkisel Üretim ve Teknolojileri  '),
    ('Biyoenformatik ve Genetik  ', 'Biyoenformatik ve Genetik  '),
    ('Biyokimya (2 Yıllık)', 'Biyokimya (2 Yıllık)'),
    ('Biyokimya (4 Yıllık)', 'Biyokimya (4 Yıllık)'),
    ('Biyoloji  ', 'Biyoloji  '),
    ('Biyoloji Öğretmenliği  ', 'Biyoloji Öğretmenliği  '),
    ('Biyomedikal Cihaz Teknolojisi ', 'Biyomedikal Cihaz Teknolojisi '),
    ('Biyomedikal Mühendisliği  ', 'Biyomedikal Mühendisliği  '),
    ('Biyomühendislik  ', 'Biyomühendislik  '),
    ('Biyosistem Mühendisliği  ', 'Biyosistem Mühendisliği  '),
    ('Biyoteknoloji  ', 'Biyoteknoloji  '),
    ('Boşnak Dili ve Edebiyatı  ', 'Boşnak Dili ve Edebiyatı  '),
    ('Boya Teknolojisi ', 'Boya Teknolojisi '),
    ('Bulgar Dili ve Edebiyatı  ', 'Bulgar Dili ve Edebiyatı  '),
    ('Bulgarca Mütercim ve Tercümanlık  ', 'Bulgarca Mütercim ve Tercümanlık  '),
    ('Büro Yönetimi ve Yönetici Asistanlığı ', 'Büro Yönetimi ve Yönetici Asistanlığı '),
    ('Çağdaş Türk Lehçeleri ve Edebiyatları  ', 'Çağdaş Türk Lehçeleri ve Edebiyatları  '),
    ('Çağdaş Yunan Dili ve Edebiyatı  ', 'Çağdaş Yunan Dili ve Edebiyatı  '),
    ('Çağrı Merkezi Hizmetleri ', 'Çağrı Merkezi Hizmetleri '),
    ('Çalışma Ekonomisi ve Endüstri İlişkileri  ', 'Çalışma Ekonomisi ve Endüstri İlişkileri  '),
    ('Çay Tarımı ve İşleme Teknolojisi ', 'Çay Tarımı ve İşleme Teknolojisi '),
    ('Çerkez Dili ve Edebiyatı  ', 'Çerkez Dili ve Edebiyatı  '),
    ('Cevher Hazırlama Mühendisliği  ', 'Cevher Hazırlama Mühendisliği  '),
    ('Çeviribilim  ', 'Çeviribilim  '),
    ('Çevre Koruma ve Kontrol ', 'Çevre Koruma ve Kontrol '),
    ('Çevre Mühendisliği  ', 'Çevre Mühendisliği  '),
    ('Çevre Sağlığı ', 'Çevre Sağlığı '),
    ('Çevre Temizliği ve Denetimi ', 'Çevre Temizliği ve Denetimi '),
    ('Ceza İnfaz ve Güvenlik Hizmetleri ', 'Ceza İnfaz ve Güvenlik Hizmetleri '),
    ('Çim Alan Tesisi ve Yönetimi ', 'Çim Alan Tesisi ve Yönetimi '),
    ('Çin Dili ve Edebiyatı  ', 'Çin Dili ve Edebiyatı  '),
    ('Çince Mütercim ve Tercümanlık  ', 'Çince Mütercim ve Tercümanlık  '),
    ('Çini Sanatı ve Tasarımı ', 'Çini Sanatı ve Tasarımı '),
    ('Çizgi Film ve Animasyon  ', 'Çizgi Film ve Animasyon  '),
    ('Çocuk Gelişimi (2 Yıllık)', 'Çocuk Gelişimi (2 Yıllık)'),
    ('Çocuk Gelişimi (4 Yıllık)', 'Çocuk Gelişimi (4 Yıllık)'),
    ('Çocuk Koruma ve Bakım Hizmetleri ', 'Çocuk Koruma ve Bakım Hizmetleri '),
    ('Coğrafi Bilgi Sistemleri ', 'Coğrafi Bilgi Sistemleri '),
    ('Coğrafya  ', 'Coğrafya  '),
    ('Coğrafya Öğretmenliği  ', 'Coğrafya Öğretmenliği  '),
    ('Çok Boyutlu Modelleme ve Animasyon ', 'Çok Boyutlu Modelleme ve Animasyon '),
    ('Deniz Bilimleri ve Teknolojisi Mühendisliği  ', 'Deniz Bilimleri ve Teknolojisi Mühendisliği  '),
    ('Deniz Brokerliği ', 'Deniz Brokerliği '),
    ('Deniz Ulaştırma İşletme Mühendisliği  ', 'Deniz Ulaştırma İşletme Mühendisliği  '),
    ('Deniz Ulaştırma ve İşletme ', 'Deniz Ulaştırma ve İşletme '),
    ('Deniz ve Liman İşletmeciliği ', 'Deniz ve Liman İşletmeciliği '),
    ('Denizcilik İşletmeleri Yönetimi  ', 'Denizcilik İşletmeleri Yönetimi  '),
    ('Deri Konfeksiyon ', 'Deri Konfeksiyon '),
    ('Deri Mühendisliği  ', 'Deri Mühendisliği  '),
    ('Deri Teknolojisi ', 'Deri Teknolojisi '),
    ('Dezenfeksiyon, Sterilizasyon ve Antisepsi Teknikerliği ',
     'Dezenfeksiyon, Sterilizasyon ve Antisepsi Teknikerliği '),
    ('Dijital Fabrika Teknolojileri ', 'Dijital Fabrika Teknolojileri '),
    ('Dijital Oyun Tasarımı  ', 'Dijital Oyun Tasarımı  '),
    ('Dil ve Konuşma Terapisi  ', 'Dil ve Konuşma Terapisi  '),
    ('Dilbilimi  ', 'Dilbilimi  '),
    ('Diş Hekimliği  ', 'Diş Hekimliği  '),
    ('Diş Protez Teknolojisi ', 'Diş Protez Teknolojisi '),
    ('Dış Ticaret ', 'Dış Ticaret '),
    ('Diyaliz ', 'Diyaliz '),
    ('Doğal Yapı Taşları Teknolojisi ', 'Doğal Yapı Taşları Teknolojisi '),
    ('Doğalgaz ve Tesisatı Teknolojisi ', 'Doğalgaz ve Tesisatı Teknolojisi '),
    ('Döküm ', 'Döküm '),
    ('Ebelik  ', 'Ebelik  '),
    ('Eczacılık  ', 'Eczacılık  '),
    ('Eczane Hizmetleri ', 'Eczane Hizmetleri '),
    ('Egzersiz ve Spor Bilimleri  ', 'Egzersiz ve Spor Bilimleri  '),
    ('Ekonometri  ', 'Ekonometri  '),
    ('Ekonomi  ', 'Ekonomi  '),
    ('Ekonomi ve Finans  ', 'Ekonomi ve Finans  '),
    ('El Sanatları  ', 'El Sanatları  '),
    ('Elektrik ', 'Elektrik '),
    ('Elektrik Enerjisi Üretim, İletim ve Dağıtımı ', 'Elektrik Enerjisi Üretim, İletim ve Dağıtımı '),
    ('Elektrik Mühendisliği  ', 'Elektrik Mühendisliği  '),
    ('Elektrik-Elektronik Mühendisliği  ', 'Elektrik-Elektronik Mühendisliği  '),
    ('Elektrikli Cihaz Teknolojisi ', 'Elektrikli Cihaz Teknolojisi '),
    ('Elektronik Haberleşme Teknolojisi ', 'Elektronik Haberleşme Teknolojisi '),
    ('Elektronik Mühendisliği  ', 'Elektronik Mühendisliği  '),
    ('Elektronik Teknolojisi ', 'Elektronik Teknolojisi '),
    ('Elektronik ve Haberleşme Mühendisliği  ', 'Elektronik ve Haberleşme Mühendisliği  '),
    ('Elektronörofizyoloji ', 'Elektronörofizyoloji '),
    ('Emlak Yönetimi ', 'Emlak Yönetimi '),
    ('Endüstri Mühendisliği  ', 'Endüstri Mühendisliği  '),
    ('Endüstri Ürünleri Tasarımı ', 'Endüstri Ürünleri Tasarımı '),
    ('Endüstriyel Cam ve Seramik ', 'Endüstriyel Cam ve Seramik '),
    ('Endüstriyel Hammaddeler İşleme Teknolojisi ', 'Endüstriyel Hammaddeler İşleme Teknolojisi '),
    ('Endüstriyel Kalıpçılık ', 'Endüstriyel Kalıpçılık '),
    ('Endüstriyel Tasarım  ', 'Endüstriyel Tasarım  '),
    ('Endüstriyel Tasarım Mühendisliği  ', 'Endüstriyel Tasarım Mühendisliği  '),
    ('Enerji Mühendisliği  ', 'Enerji Mühendisliği  '),
    ('Enerji Sistemleri Mühendisliği  ', 'Enerji Sistemleri Mühendisliği  '),
    ('Enerji Tesisleri İşletmeciliği ', 'Enerji Tesisleri İşletmeciliği '),
    ('Enerji Yönetimi  ', 'Enerji Yönetimi  '),
    ('Engelli Bakımı ve Rehabilitasyon ', 'Engelli Bakımı ve Rehabilitasyon '),
    ('Engelliler İçin Destek Programı ', 'Engelliler İçin Destek Programı '),
    ('Ergoterapi  ', 'Ergoterapi  '),
    ('Ermeni Dili ve Kültürü  ', 'Ermeni Dili ve Kültürü  '),
    ('Eser Koruma ', 'Eser Koruma '),
    ('Eski Yunan Dili ve Edebiyatı  ', 'Eski Yunan Dili ve Edebiyatı  '),
    ('Et ve Ürünleri Teknolojisi ', 'Et ve Ürünleri Teknolojisi '),
    ('E-Ticaret ve Pazarlama ', 'E-Ticaret ve Pazarlama '),
    ('Ev İdaresi ', 'Ev İdaresi '),
    ('Evde Hasta Bakımı ', 'Evde Hasta Bakımı '),
    ('Fars Dili ve Edebiyatı  ', 'Fars Dili ve Edebiyatı  '),
    ('Farsça Mütercim ve Tercümanlık  ', 'Farsça Mütercim ve Tercümanlık  '),
    ('Felsefe  ', 'Felsefe  '),
    ('Felsefe Grubu Öğretmenliği  ', 'Felsefe Grubu Öğretmenliği  '),
    ('Fen Bilgisi Öğretmenliği  ', 'Fen Bilgisi Öğretmenliği  '),
    ('Fidan Yetiştiriciliği ', 'Fidan Yetiştiriciliği '),
    ('Film Tasarım ve Yönetmenliği  ', 'Film Tasarım ve Yönetmenliği  '),
    ('Film Tasarımı ve Yazarlığı  ', 'Film Tasarımı ve Yazarlığı  '),
    ('Film Tasarımı ve Yönetimi  ', 'Film Tasarımı ve Yönetimi  '),
    ('Fındık Eksperliği ', 'Fındık Eksperliği '),
    ('Fizik  ', 'Fizik  '),
    ('Fizik Mühendisliği  ', 'Fizik Mühendisliği  '),
    ('Fizik Öğretmenliği  ', 'Fizik Öğretmenliği  '),
    ('Fizyoterapi ', 'Fizyoterapi '),
    ('Fizyoterapi ve Rehabilitasyon  ', 'Fizyoterapi ve Rehabilitasyon  '),
    ('Fotoğraf  ', 'Fotoğraf  '),
    ('Fotoğraf ve Video  ', 'Fotoğraf ve Video  '),
    ('Fotoğrafçılık ve Kameramanlık ', 'Fotoğrafçılık ve Kameramanlık '),
    ('Fotonik  ', 'Fotonik  '),
    ('Fransız Dili ve Edebiyatı  ', 'Fransız Dili ve Edebiyatı  '),
    ('Fransızca Mütercim ve Tercümanlık  ', 'Fransızca Mütercim ve Tercümanlık  '),
    ('Fransızca Öğretmenliği  ', 'Fransızca Öğretmenliği  '),
    ('Gastronomi ve Mutfak Sanatları  ', 'Gastronomi ve Mutfak Sanatları  '),
    ('Gayrimenkul Geliştirme ve Yönetimi  ', 'Gayrimenkul Geliştirme ve Yönetimi  '),
    ('Gazetecilik  ', 'Gazetecilik  '),
    ('Geleneksel El Sanatları ', 'Geleneksel El Sanatları '),
    ('Geleneksel Türk Sanatları  ', 'Geleneksel Türk Sanatları  '),
    ('Gemi İnşaatı ', 'Gemi İnşaatı '),
    ('Gemi İnşaatı ve Gemi Makineleri Mühendisliği  ', 'Gemi İnşaatı ve Gemi Makineleri Mühendisliği  '),
    ('Gemi Makineleri İşletme Mühendisliği  ', 'Gemi Makineleri İşletme Mühendisliği  '),
    ('Gemi Makineleri İşletmeciliği ', 'Gemi Makineleri İşletmeciliği '),
    ('Gemi ve Deniz Teknolojisi Mühendisliği  ', 'Gemi ve Deniz Teknolojisi Mühendisliği  '),
    ('Gemi ve Yat Tasarımı  ', 'Gemi ve Yat Tasarımı  '),
    ('Genetik ve Biyomühendislik  ', 'Genetik ve Biyomühendislik  '),
    ('Genetik ve Yaşam Bilimleri Programları  ', 'Genetik ve Yaşam Bilimleri Programları  '),
    ('Geomatik Mühendisliği  ', 'Geomatik Mühendisliği  '),
    ('Geoteknik ', 'Geoteknik '),
    ('Gerontoloji  ', 'Gerontoloji  '),
    ('Gıda Kalite Kontrolü ve Analizi ', 'Gıda Kalite Kontrolü ve Analizi '),
    ('Gıda Mühendisliği  ', 'Gıda Mühendisliği  '),
    ('Gıda Teknolojisi (2 Yıllık)', 'Gıda Teknolojisi (2 Yıllık)'),
    ('Gıda Teknolojisi (4 Yıllık)', 'Gıda Teknolojisi (4 Yıllık)'),
    ('Girişimcilik  ', 'Girişimcilik  '),
    ('Giyim Üretim Teknolojisi ', 'Giyim Üretim Teknolojisi '),
    ('Görsel İletişim Tasarımı  ', 'Görsel İletişim Tasarımı  '),
    ('Görsel Sanatlar  ', 'Görsel Sanatlar  '),
    ('Grafik  ', 'Grafik  '),
    ('Grafik Tasarımı (2 Yıllık)', 'Grafik Tasarımı (2 Yıllık)'),
    ('Grafik Tasarımı (4 Yıllık) ', 'Grafik Tasarımı (4 Yıllık) '),
    ('Gümrük İşletme  ', 'Gümrük İşletme  '),
    ('Gürcü Dili ve Edebiyatı  ', 'Gürcü Dili ve Edebiyatı  '),
    ('Halıcılık ve Kilimcilik ', 'Halıcılık ve Kilimcilik '),
    ('Halkbilim  ', 'Halkbilim  '),
    ('Halkla İlişkiler  ', 'Halkla İlişkiler  '),
    ('Halkla İlişkiler ve Reklamcılık  ', 'Halkla İlişkiler ve Reklamcılık  '),
    ('Halkla İlişkiler ve Tanıtım (2 Yıllık)', 'Halkla İlişkiler ve Tanıtım (2 Yıllık)'),
    ('Halkla İlişkiler ve Tanıtım (4 Yıllık)', 'Halkla İlişkiler ve Tanıtım (4 Yıllık)'),
    ('Harita Mühendisliği  ', 'Harita Mühendisliği  '),
    ('Harita ve Kadastro ', 'Harita ve Kadastro '),
    ('Hava Lojistiği ', 'Hava Lojistiği '),
    ('Havacılık Elektrik ve Elektroniği  ', 'Havacılık Elektrik ve Elektroniği  '),
    ('Havacılık ve Uzay Mühendisliği  ', 'Havacılık ve Uzay Mühendisliği  '),
    ('Havacılık Yönetimi  ', 'Havacılık Yönetimi  '),
    ('Hayvansal Üretim ve Teknolojileri  ', 'Hayvansal Üretim ve Teknolojileri  '),
    ('Hemşirelik  ', 'Hemşirelik  '),
    ('Hibrid ve Elektrikli Taşıtlar Teknolojisi ', 'Hibrid ve Elektrikli Taşıtlar Teknolojisi '),
    ('Hidrojeoloji Mühendisliği  ', 'Hidrojeoloji Mühendisliği  '),
    ('Hindoloji  ', 'Hindoloji  '),
    ('Hititoloji  ', 'Hititoloji  '),
    ('Hukuk  ', 'Hukuk  '),
    ('Hukuk Büro Yönetimi ve Sekreterliği ', 'Hukuk Büro Yönetimi ve Sekreterliği '),
    ('Hungaroloji  ', 'Hungaroloji  '),
    ('İbrani Dili ve Kültürü  ', 'İbrani Dili ve Kültürü  '),
    ('İç Mekan Tasarımı ', 'İç Mekan Tasarımı '),
    ('İç Mimarlık  ', 'İç Mimarlık  '),
    ('İç Mimarlık ve Çevre Tasarımı  ', 'İç Mimarlık ve Çevre Tasarımı  '),
    ('İklimlendirme ve Soğutma Teknolojisi ', 'İklimlendirme ve Soğutma Teknolojisi '),
    ('İkram Hizmetleri ', 'İkram Hizmetleri '),
    ('İktisadi ve İdari Bilimler Programları  ', 'İktisadi ve İdari Bilimler Programları  '),
    ('İktisadi ve İdari Programlar  ', 'İktisadi ve İdari Programlar  '),
    ('İktisat  ', 'İktisat  '),
    ('İlahiyat (2 Yıllık)', 'İlahiyat (2 Yıllık)'),
    ('İlahiyat (4 Yıllık)', 'İlahiyat (4 Yıllık)'),
    ('İletişim Bilimleri  ', 'İletişim Bilimleri  '),
    ('İletişim Fakültesi  ', 'İletişim Fakültesi  '),
    ('İletişim Sanatları  ', 'İletişim Sanatları  '),
    ('İletişim Tasarımı ve Yönetimi  ', 'İletişim Tasarımı ve Yönetimi  '),
    ('İletişim ve Tasarım  ', 'İletişim ve Tasarım  '),
    ('İlk ve Acil Yardım ', 'İlk ve Acil Yardım '),
    ('İlköğretim Matematik Öğretmenliği  ', 'İlköğretim Matematik Öğretmenliği  '),
    ('İmalat Mühendisliği  ', 'İmalat Mühendisliği  '),
    ('İngiliz Dil Bilimi  ', 'İngiliz Dil Bilimi  '),
    ('İngiliz Dili ve Edebiyatı  ', 'İngiliz Dili ve Edebiyatı  '),
    ('İngiliz ve Rus Dilleri ve Edebiyatları  ', 'İngiliz ve Rus Dilleri ve Edebiyatları  '),
    ('İngilizce Mütercim ve Tercümanlık  ', 'İngilizce Mütercim ve Tercümanlık  '),
    ('İngilizce Öğretmenliği  ', 'İngilizce Öğretmenliği  '),
    ('İngilizce, Fransızca Mütercim ve Tercümanlık  ', 'İngilizce, Fransızca Mütercim ve Tercümanlık  '),
    ('İnşaat Mühendisliği  ', 'İnşaat Mühendisliği  '),
    ('İnşaat Teknolojisi ', 'İnşaat Teknolojisi '),
    ('İnsan Kaynakları Yönetimi (2 Yıllık)', 'İnsan Kaynakları Yönetimi (2 Yıllık)'),
    ('İnsan Kaynakları Yönetimi (4 Yıllık)', 'İnsan Kaynakları Yönetimi (4 Yıllık)'),
    ('İnsansız Hava Aracı Teknolojisi ve Operatörlüğü ', 'İnsansız Hava Aracı Teknolojisi ve Operatörlüğü '),
    ('İnternet ve Ağ Teknolojileri ', 'İnternet ve Ağ Teknolojileri '),
    ('İş Makineleri Operatörlüğü ', 'İş Makineleri Operatörlüğü '),
    ('İş Sağlığı ve Güvenliği (2 Yıllık)', 'İş Sağlığı ve Güvenliği (2 Yıllık)'),
    ('İş Sağlığı ve Güvenliği (4 Yıllık)', 'İş Sağlığı ve Güvenliği (4 Yıllık)'),
    ('İş ve Uğraşı Terapisi ', 'İş ve Uğraşı Terapisi '),
    ('İslam Bilimleri  ', 'İslam Bilimleri  '),
    ('İslam İktisadı ve Finans  ', 'İslam İktisadı ve Finans  '),
    ('İslami İlimler (2 Yıllık)', 'İslami İlimler (2 Yıllık)'),
    ('İslami İlimler (4 Yıllık)', 'İslami İlimler (4 Yıllık)'),
    ('İşletme  ', 'İşletme  '),
    ('İşletme Mühendisliği  ', 'İşletme Mühendisliği  '),
    ('İşletme Yönetimi ', 'İşletme Yönetimi '),
    ('İspanyol Dili ve Edebiyatı  ', 'İspanyol Dili ve Edebiyatı  '),
    ('İstatistik  ', 'İstatistik  '),
    ('İstatistik ve Bilgisayar Bilimleri  ', 'İstatistik ve Bilgisayar Bilimleri  '),
    ('İtalyan Dili ve Edebiyatı  ', 'İtalyan Dili ve Edebiyatı  '),
    ('Japon Dili ve Edebiyatı  ', 'Japon Dili ve Edebiyatı  '),
    ('Japonca Öğretmenliği  ', 'Japonca Öğretmenliği  '),
    ('Jeofizik Mühendisliği  ', 'Jeofizik Mühendisliği  '),
    ('Jeoloji Mühendisliği  ', 'Jeoloji Mühendisliği  '),
    ('Kamu Yönetimi  ', 'Kamu Yönetimi  '),
    ('Kanatlı Hayvan Yetiştiriciliği  ', 'Kanatlı Hayvan Yetiştiriciliği  '),
    ('Karşılaştırmalı Edebiyat  ', 'Karşılaştırmalı Edebiyat  '),
    ('Kaynak Teknolojisi ', 'Kaynak Teknolojisi '),
    ('Kazak Dili ve Edebiyatı  ', 'Kazak Dili ve Edebiyatı  '),
    ('Kentsel Tasarım ve Peyzaj Mimarlığı  ', 'Kentsel Tasarım ve Peyzaj Mimarlığı  '),
    ('Kimya  ', 'Kimya  '),
    ('Kimya Mühendisliği  ', 'Kimya Mühendisliği  '),
    ('Kimya Öğretmenliği  ', 'Kimya Öğretmenliği  '),
    ('Kimya Teknolojisi ', 'Kimya Teknolojisi '),
    ('Kimya-Biyoloji Mühendisliği  ', 'Kimya-Biyoloji Mühendisliği  '),
    ('Klasik Arkeoloji  ', 'Klasik Arkeoloji  '),
    ('Kontrol ve Otomasyon Mühendisliği  ', 'Kontrol ve Otomasyon Mühendisliği  '),
    ('Kontrol ve Otomasyon Teknolojisi ', 'Kontrol ve Otomasyon Teknolojisi '),
    ('Kooperatifçilik ', 'Kooperatifçilik '),
    ('Kore Dili ve Edebiyatı  ', 'Kore Dili ve Edebiyatı  '),
    ('Kozmetik Teknolojisi ', 'Kozmetik Teknolojisi '),
    ('Kültür Varlıklarını Koruma ve Onarım  ', 'Kültür Varlıklarını Koruma ve Onarım  '),
    ('Kültür ve İletişim Bilimleri  ', 'Kültür ve İletişim Bilimleri  '),
    ('Kültürel Miras ve Turizm ', 'Kültürel Miras ve Turizm '),
    ('Kümes Hayvanları Yetiştiriciliği ', 'Kümes Hayvanları Yetiştiriciliği '),
    ('Küresel Siyaset ve Uluslararası İlişkiler  ', 'Küresel Siyaset ve Uluslararası İlişkiler  '),
    ('Kürt Dili ve Edebiyatı  ', 'Kürt Dili ve Edebiyatı  '),
    ('Kuyumculuk ve Mücevher Tasarımı  ', 'Kuyumculuk ve Mücevher Tasarımı  '),
    ('Kuyumculuk ve Takı Tasarımı ', 'Kuyumculuk ve Takı Tasarımı '),
    ('Laborant ve Veteriner Sağlık ', 'Laborant ve Veteriner Sağlık '),
    ('Laboratuvar Teknolojisi ', 'Laboratuvar Teknolojisi '),
    ('Latin Dili ve Edebiyatı  ', 'Latin Dili ve Edebiyatı  '),
    ('Leh Dili ve Edebiyatı  ', 'Leh Dili ve Edebiyatı  '),
    ('Lojistik ', 'Lojistik '),
    ('Lojistik Yönetimi  ', 'Lojistik Yönetimi  '),
    ('Maden Mühendisliği  ', 'Maden Mühendisliği  '),
    ('Madencilik Teknolojisi ', 'Madencilik Teknolojisi '),
    ('Makine ', 'Makine '),
    ('Makine Mühendisliği  ', 'Makine Mühendisliği  '),
    ('Makine Resim ve Konstrüksiyonu ', 'Makine Resim ve Konstrüksiyonu '),
    ('Maliye (2 Yıllık)', 'Maliye (2 Yıllık)'),
    ('Maliye (4 Yıllık)', 'Maliye (4 Yıllık)'),
    ('Malzeme Bilimi ve Mühendisliği  ', 'Malzeme Bilimi ve Mühendisliği  '),
    ('Malzeme Bilimi ve Nanoteknoloji Mühendisliği  ', 'Malzeme Bilimi ve Nanoteknoloji Mühendisliği  '),
    ('Malzeme Bilimi ve Teknolojileri  ', 'Malzeme Bilimi ve Teknolojileri  '),
    ('Mantarcılık ', 'Mantarcılık '),
    ('Marina ve Yat İşletmeciliği ', 'Marina ve Yat İşletmeciliği '),
    ('Marka İletişimi ', 'Marka İletişimi '),
    ('Matematik  ', 'Matematik  '),
    ('Matematik Mühendisliği  ', 'Matematik Mühendisliği  '),
    ('Matematik Öğretmenliği  ', 'Matematik Öğretmenliği  '),
    ('Matematik ve Bilgisayar Bilimleri  ', 'Matematik ve Bilgisayar Bilimleri  '),
    ('Medya ve Görsel Sanatlar  ', 'Medya ve Görsel Sanatlar  '),
    ('Medya ve İletişim (2 Yıllık)', 'Medya ve İletişim (2 Yıllık)'),
    ('Medya ve İletişim (4 Yıllık)', 'Medya ve İletişim (4 Yıllık)'),
    ('Mekatronik ', 'Mekatronik '),
    ('Mekatronik Mühendisliği  ', 'Mekatronik Mühendisliği  '),
    ('Menkul Kıymetler ve Sermaye Piyasası ', 'Menkul Kıymetler ve Sermaye Piyasası '),
    ('Mermer Teknolojisi ', 'Mermer Teknolojisi '),
    ('Metalurji ', 'Metalurji '),
    ('Metalurji ve Malzeme Mühendisliği  ', 'Metalurji ve Malzeme Mühendisliği  '),
    ('Meteoroloji Mühendisliği  ', 'Meteoroloji Mühendisliği  '),
    ('Meyve ve Sebze İşleme Teknolojisi ', 'Meyve ve Sebze İşleme Teknolojisi '),
    ('Mimari Dekoratif Sanatlar ', 'Mimari Dekoratif Sanatlar '),
    ('Mimari Restorasyon ', 'Mimari Restorasyon '),
    ('Mimarlık  ', 'Mimarlık  '),
    ('Mobil Teknolojileri ', 'Mobil Teknolojileri '),
    ('Mobilya ve Dekorasyon ', 'Mobilya ve Dekorasyon '),
    ('Moda Tasarımı (2 Yıllık)', 'Moda Tasarımı (2 Yıllık)'),
    ('Moda Tasarımı (4 Yıllık)', 'Moda Tasarımı (4 Yıllık)'),
    ('Moda Yönetimi ', 'Moda Yönetimi '),
    ('Moleküler Biyoloji ve Genetik  ', 'Moleküler Biyoloji ve Genetik  '),
    ('Moleküler Biyoteknoloji  ', 'Moleküler Biyoteknoloji  '),
    ('Muhasebe ve Denetim  ', 'Muhasebe ve Denetim  '),
    ('Muhasebe ve Finans Yönetimi  ', 'Muhasebe ve Finans Yönetimi  '),
    ('Muhasebe ve Vergi Uygulamaları ', 'Muhasebe ve Vergi Uygulamaları '),
    ('Mühendislik Programları  ', 'Mühendislik Programları  '),
    ('Mühendislik ve Doğa Bilimleri Programları  ', 'Mühendislik ve Doğa Bilimleri Programları  '),
    ('Mütercim-Tercümanlık  ', 'Mütercim-Tercümanlık  '),
    ('Müzecilik  ', 'Müzecilik  '),
    ('Nanobilim ve Nanoteknoloji  ', 'Nanobilim ve Nanoteknoloji  '),
    ('Nanoteknoloji Mühendisliği  ', 'Nanoteknoloji Mühendisliği  '),
    ('Nüfus ve Vatandaşlık ', 'Nüfus ve Vatandaşlık '),
    ('Nükleer Enerji Mühendisliği  ', 'Nükleer Enerji Mühendisliği  '),
    ('Nükleer Teknoloji ve Radyasyon Güvenliği ', 'Nükleer Teknoloji ve Radyasyon Güvenliği '),
    ('Nükleer Tıp Teknikleri ', 'Nükleer Tıp Teknikleri '),
    ('Odyoloji  ', 'Odyoloji  '),
    ('Odyometri ', 'Odyometri '),
    ('Okul Öncesi Öğretmenliği  ', 'Okul Öncesi Öğretmenliği  '),
    ('Optik ve Akustik Mühendisliği  ', 'Optik ve Akustik Mühendisliği  '),
    ('Optisyenlik ', 'Optisyenlik '),
    ('Organik Tarım ', 'Organik Tarım '),
    ('Organik Tarım İşletmeciliği  ', 'Organik Tarım İşletmeciliği  '),
    ('Orman Endüstrisi Mühendisliği  ', 'Orman Endüstrisi Mühendisliği  '),
    ('Orman Mühendisliği  ', 'Orman Mühendisliği  '),
    ('Ormancılık ve Orman Ürünleri ', 'Ormancılık ve Orman Ürünleri '),
    ('Ortopedik Protez ve Ortez ', 'Ortopedik Protez ve Ortez '),
    ('Otel Yöneticiliği  ', 'Otel Yöneticiliği  '),
    ('Otobüs Kaptanlığı ', 'Otobüs Kaptanlığı '),
    ('Otomotiv Gövde ve Yüzey İşlem Teknolojileri ', 'Otomotiv Gövde ve Yüzey İşlem Teknolojileri '),
    ('Otomotiv Mühendisliği  ', 'Otomotiv Mühendisliği  '),
    ('Otomotiv Teknolojisi ', 'Otomotiv Teknolojisi '),
    ('Otopsi Yardımcılığı ', 'Otopsi Yardımcılığı '),
    ('Özel Eğitim Öğretmenliği  ', 'Özel Eğitim Öğretmenliği  '),
    ('Özel Güvenlik ve Koruma ', 'Özel Güvenlik ve Koruma '),
    ('Pastacılık ve Ekmekçilik ', 'Pastacılık ve Ekmekçilik '),
    ('Patoloji Laboratuvar Teknikleri ', 'Patoloji Laboratuvar Teknikleri '),
    ('Pazarlama (2 Yıllık)', 'Pazarlama (2 Yıllık)'),
    ('Pazarlama (4 Yıllık)', 'Pazarlama (4 Yıllık)'),
    ('Perakende Satış ve Mağaza Yönetimi ', 'Perakende Satış ve Mağaza Yönetimi '),
    ('Perfüzyon  ', 'Perfüzyon  '),
    ('Petrol ve Doğalgaz Mühendisliği  ', 'Petrol ve Doğalgaz Mühendisliği  '),
    ('Peyzaj Mimarlığı  ', 'Peyzaj Mimarlığı  '),
    ('Peyzaj ve Süs Bitkileri Yetiştiriciliği ', 'Peyzaj ve Süs Bitkileri Yetiştiriciliği '),
    ('Pilotaj  ', 'Pilotaj  '),
    ('Podoloji ', 'Podoloji '),
    ('Polimer Malzeme Mühendisliği  ', 'Polimer Malzeme Mühendisliği  '),
    ('Polimer Teknolojisi ', 'Polimer Teknolojisi '),
    ('Politika ve Ekonomi  ', 'Politika ve Ekonomi  '),
    ('Posta Hizmetleri ', 'Posta Hizmetleri '),
    ('Protohistorya ve Ön Asya Arkeolojisi  ', 'Protohistorya ve Ön Asya Arkeolojisi  '),
    ('Psikoloji  ', 'Psikoloji  '),
    ('Psikolojik Danışmanlık ve Rehberlik  ', 'Psikolojik Danışmanlık ve Rehberlik  '),
    ('Psikolojik Danışmanlık ve Rehberlik Öğretmenliği  ', 'Psikolojik Danışmanlık ve Rehberlik Öğretmenliği  '),
    ('Radyo ve Televizyon Programcılığı ', 'Radyo ve Televizyon Programcılığı '),
    ('Radyo ve Televizyon Teknolojisi ', 'Radyo ve Televizyon Teknolojisi '),
    ('Radyo, Televizyon ve Sinema  ', 'Radyo, Televizyon ve Sinema  '),
    ('Radyoterapi ', 'Radyoterapi '),
    ('Rafineri ve Petro-Kimya Teknolojisi ', 'Rafineri ve Petro-Kimya Teknolojisi '),
    ('Raylı Sistemler Elektrik ve Elektronik ', 'Raylı Sistemler Elektrik ve Elektronik '),
    ('Raylı Sistemler İşletmeciliği ', 'Raylı Sistemler İşletmeciliği '),
    ('Raylı Sistemler Makine Teknolojisi ', 'Raylı Sistemler Makine Teknolojisi '),
    ('Raylı Sistemler Makinistliği ', 'Raylı Sistemler Makinistliği '),
    ('Raylı Sistemler Mühendisliği  ', 'Raylı Sistemler Mühendisliği  '),
    ('Raylı Sistemler Yol Teknolojisi ', 'Raylı Sistemler Yol Teknolojisi '),
    ('Rehberlik ve Psikolojik Danışmanlık  ', 'Rehberlik ve Psikolojik Danışmanlık  '),
    ('Reklam Tasarımı ve İletişimi  ', 'Reklam Tasarımı ve İletişimi  '),
    ('Reklamcılık (2 Yıllık)', 'Reklamcılık (2 Yıllık)'),
    ('Reklamcılık (4 Yıllık)', 'Reklamcılık (4 Yıllık)'),
    ('Rekreasyon  ', 'Rekreasyon  '),
    ('Rekreasyon Yönetimi  ', 'Rekreasyon Yönetimi  '),
    ('Rus Dili ve Edebiyatı  ', 'Rus Dili ve Edebiyatı  '),
    ('Rus Dili ve Edebiyatı Öğretmenliği  ', 'Rus Dili ve Edebiyatı Öğretmenliği  '),
    ('Rus ve İngiliz Dilleri ve Edebiyatları  ', 'Rus ve İngiliz Dilleri ve Edebiyatları  '),
    ('Rusça Mütercim ve Tercümanlık  ', 'Rusça Mütercim ve Tercümanlık  '),
    ('Saç Bakımı ve Güzellik Hizmetleri ', 'Saç Bakımı ve Güzellik Hizmetleri '),
    ('Sağlık Bilgi Sistemleri Teknikerliği ', 'Sağlık Bilgi Sistemleri Teknikerliği '),
    ('Sağlık Kurumları İşletmeciliği ', 'Sağlık Kurumları İşletmeciliği '),
    ('Sağlık Turizmi İşletmeciliği ', 'Sağlık Turizmi İşletmeciliği '),
    ('Sağlık Yönetimi  ', 'Sağlık Yönetimi  '),
    ('Sahne Işık ve Ses Teknolojileri ', 'Sahne Işık ve Ses Teknolojileri '),
    ('Sahne ve Dekor Tasarımı ', 'Sahne ve Dekor Tasarımı '),
    ('Sanat Tarihi  ', 'Sanat Tarihi  '),
    ('Sanat ve Kültür Yönetimi  ', 'Sanat ve Kültür Yönetimi  '),
    ('Sanat ve Sosyal Bilimler Programları  ', 'Sanat ve Sosyal Bilimler Programları  '),
    ('Şehir ve Bölge Planlama  ', 'Şehir ve Bölge Planlama  '),
    ('Seracılık ', 'Seracılık '),
    ('Seramik ve Cam Tasarımı ', 'Seramik ve Cam Tasarımı '),
    ('Sermaye Piyasası  ', 'Sermaye Piyasası  '),
    ('Seyahat İşletmeciliği  ', 'Seyahat İşletmeciliği  '),
    ('Seyahat İşletmeciliği ve Turizm Rehberliği  ', 'Seyahat İşletmeciliği ve Turizm Rehberliği  '),
    ('Sigortacılık  ', 'Sigortacılık  '),
    ('Sigortacılık ve Aktüerya Bilimleri  ', 'Sigortacılık ve Aktüerya Bilimleri  '),
    ('Sigortacılık ve Risk Yönetimi  ', 'Sigortacılık ve Risk Yönetimi  '),
    ('Sigortacılık ve Sosyal Güvenlik  ', 'Sigortacılık ve Sosyal Güvenlik  '),
    ('Silah Sanayi Teknikerliği ', 'Silah Sanayi Teknikerliği '),
    ('Sinema ve Dijital Medya  ', 'Sinema ve Dijital Medya  '),
    ('Sinema ve Televizyon  ', 'Sinema ve Televizyon  '),
    ('Sınıf Öğretmenliği  ', 'Sınıf Öğretmenliği  '),
    ('Sinoloji  ', 'Sinoloji  '),
    ('Sivil Hava Ulaştırma İşletmeciliği ', 'Sivil Hava Ulaştırma İşletmeciliği '),
    ('Sivil Havacılık Kabin Hizmetleri ', 'Sivil Havacılık Kabin Hizmetleri '),
    ('Sivil Savunma ve İtfaiyecilik ', 'Sivil Savunma ve İtfaiyecilik '),
    ('Siyasal Bilimler  ', 'Siyasal Bilimler  '),
    ('Siyaset Bilimi  ', 'Siyaset Bilimi  '),
    ('Siyaset Bilimi ve Kamu Yönetimi  ', 'Siyaset Bilimi ve Kamu Yönetimi  '),
    ('Siyaset Bilimi ve Uluslararası İlişkiler  ', 'Siyaset Bilimi ve Uluslararası İlişkiler  '),
    ('Sondaj Teknolojisi ', 'Sondaj Teknolojisi '),
    ('Sosyal Bilgiler Öğretmenliği  ', 'Sosyal Bilgiler Öğretmenliği  '),
    ('Sosyal Güvenlik ', 'Sosyal Güvenlik '),
    ('Sosyal Hizmet  ', 'Sosyal Hizmet  '),
    ('Sosyal Hizmetler ', 'Sosyal Hizmetler '),
    ('Sosyal Medya Yöneticiliği ', 'Sosyal Medya Yöneticiliği '),
    ('Sosyal ve Siyasal Bilimler  ', 'Sosyal ve Siyasal Bilimler  '),
    ('Sosyoloji  ', 'Sosyoloji  '),
    ('Spor Yöneticiliği  ', 'Spor Yöneticiliği  '),
    ('Spor Yönetimi ', 'Spor Yönetimi '),
    ('Su Altı Teknolojisi ', 'Su Altı Teknolojisi '),
    ('Su Bilimleri ve Mühendisliği  ', 'Su Bilimleri ve Mühendisliği  '),
    ('Su Ürünleri İşleme Teknolojisi ', 'Su Ürünleri İşleme Teknolojisi '),
    ('Su Ürünleri Mühendisliği  ', 'Su Ürünleri Mühendisliği  '),
    ('Sulama Teknolojisi ', 'Sulama Teknolojisi '),
    ('Sümeroloji  ', 'Sümeroloji  '),
    ('Süryani Dili ve Edebiyatı  ', 'Süryani Dili ve Edebiyatı  '),
    ('Süt Teknolojisi  ', 'Süt Teknolojisi  '),
    ('Süt ve Besi Hayvancılığı ', 'Süt ve Besi Hayvancılığı '),
    ('Süt ve Ürünleri Teknolojisi ', 'Süt ve Ürünleri Teknolojisi '),
    ('Tahribatsız Muayene ', 'Tahribatsız Muayene '),
    ('Takı Tasarımı  ', 'Takı Tasarımı  '),
    ('Tapu Kadastro  ', 'Tapu Kadastro  '),
    ('Tapu ve Kadastro ', 'Tapu ve Kadastro '),
    ('Tarih  ', 'Tarih  '),
    ('Tarih Öğretmenliği  ', 'Tarih Öğretmenliği  '),
    ('Tarih Öncesi Arkeolojisi  ', 'Tarih Öncesi Arkeolojisi  '),
    ('Tarım Ekonomisi  ', 'Tarım Ekonomisi  '),
    ('Tarım Makineleri ', 'Tarım Makineleri '),
    ('Tarım Makineleri ve Teknolojileri Mühendisliği  ', 'Tarım Makineleri ve Teknolojileri Mühendisliği  '),
    ('Tarım Teknolojisi ', 'Tarım Teknolojisi '),
    ('Tarım Ticareti ve İşletmeciliği  ', 'Tarım Ticareti ve İşletmeciliği  '),
    ('Tarımsal Biyoteknoloji  ', 'Tarımsal Biyoteknoloji  '),
    ('Tarımsal Genetik Mühendisliği  ', 'Tarımsal Genetik Mühendisliği  '),
    ('Tarımsal İşletmecilik ', 'Tarımsal İşletmecilik '),
    ('Tarımsal Yapılar ve Sulama  ', 'Tarımsal Yapılar ve Sulama  '),
    ('Tarla Bitkileri (2 Yıllık)', 'Tarla Bitkileri (2 Yıllık)'),
    ('Tarla Bitkileri (4 Yıllık)', 'Tarla Bitkileri (4 Yıllık)'),
    ('Teknoloji ve Bilgi Yönetimi  ', 'Teknoloji ve Bilgi Yönetimi  '),
    ('Tekstil Mühendisliği  ', 'Tekstil Mühendisliği  '),
    ('Tekstil Tasarımı  ', 'Tekstil Tasarımı  '),
    ('Tekstil Teknolojisi ', 'Tekstil Teknolojisi '),
    ('Tekstil ve Halı Makineleri ', 'Tekstil ve Halı Makineleri '),
    ('Tekstil ve Moda Tasarımı  ', 'Tekstil ve Moda Tasarımı  '),
    ('Televizyon Haberciliği ve Programcılığı  ', 'Televizyon Haberciliği ve Programcılığı  '),
    ('Tıbbi Dokümantasyon ve Sekreterlik ', 'Tıbbi Dokümantasyon ve Sekreterlik '),
    ('Tıbbi Görüntüleme Teknikleri ', 'Tıbbi Görüntüleme Teknikleri '),
    ('Tıbbi Laboratuvar Teknikleri ', 'Tıbbi Laboratuvar Teknikleri '),
    ('Tıbbi Tanıtım ve Pazarlama ', 'Tıbbi Tanıtım ve Pazarlama '),
    ('Tıbbi ve Aromatik Bitkiler ', 'Tıbbi ve Aromatik Bitkiler '),
    ('Tıp  ', 'Tıp  '),
    ('Tıp Mühendisliği  ', 'Tıp Mühendisliği  '),
    ('Tiyatro Eleştirmenliği ve Dramaturji  ', 'Tiyatro Eleştirmenliği ve Dramaturji  '),
    ('Tohum Bilimi ve Teknolojisi  ', 'Tohum Bilimi ve Teknolojisi  '),
    ('Tohumculuk Teknolojisi ', 'Tohumculuk Teknolojisi '),
    ('Toprak Bilimi ve Bitki Besleme  ', 'Toprak Bilimi ve Bitki Besleme  '),
    ('Turist Rehberliği ', 'Turist Rehberliği '),
    ('Turizm Animasyonu ', 'Turizm Animasyonu '),
    ('Turizm İşletmeciliği  ', 'Turizm İşletmeciliği  '),
    ('Turizm Rehberliği  ', 'Turizm Rehberliği  '),
    ('Turizm ve Otel İşletmeciliği ', 'Turizm ve Otel İşletmeciliği '),
    ('Turizm ve Otel İşletmeciliği  ', 'Turizm ve Otel İşletmeciliği  '),
    ('Turizm ve Seyahat Hizmetleri ', 'Turizm ve Seyahat Hizmetleri '),
    ('Türk Dili ve Edebiyatı  ', 'Türk Dili ve Edebiyatı  '),
    ('Türk Halkbilimi  ', 'Türk Halkbilimi  '),
    ('Türk İslam Arkeolojisi  ', 'Türk İslam Arkeolojisi  '),
    ('Türkçe Öğretmenliği  ', 'Türkçe Öğretmenliği  '),
    ('Türkoloji  ', 'Türkoloji  '),
    ('Tütün Eksperliği  ', 'Tütün Eksperliği  '),
    ('Uçak Bakım ve Onarım  ', 'Uçak Bakım ve Onarım  '),
    ('Uçak Elektrik ve Elektroniği  ', 'Uçak Elektrik ve Elektroniği  '),
    ('Uçak Gövde ve Motor Bakımı  ', 'Uçak Gövde ve Motor Bakımı  '),
    ('Uçak Mühendisliği  ', 'Uçak Mühendisliği  '),
    ('Uçak Teknolojisi ', 'Uçak Teknolojisi '),
    ('Uçuş Harekat Yöneticiliği ', 'Uçuş Harekat Yöneticiliği '),
    ('Ukrayna Dili ve Edebiyatı  ', 'Ukrayna Dili ve Edebiyatı  '),
    ('Ulaştırma ve Trafik Hizmetleri ', 'Ulaştırma ve Trafik Hizmetleri '),
    ('Uluslararası Ekonomik İlişkiler  ', 'Uluslararası Ekonomik İlişkiler  '),
    ('Uluslararası Finans  ', 'Uluslararası Finans  '),
    ('Uluslararası Finans ve Bankacılık  ', 'Uluslararası Finans ve Bankacılık  '),
    ('Uluslararası Girişimcilik  ', 'Uluslararası Girişimcilik  '),
    ('Uluslararası İlişkiler  ', 'Uluslararası İlişkiler  '),
    ('Uluslararası İşletme Yönetimi  ', 'Uluslararası İşletme Yönetimi  '),
    ('Uluslararası Ticaret  ', 'Uluslararası Ticaret  '),
    ('Uluslararası Ticaret ve Finans  ', 'Uluslararası Ticaret ve Finans  '),
    ('Uluslararası Ticaret ve Finansman  ', 'Uluslararası Ticaret ve Finansman  '),
    ('Uluslararası Ticaret ve İşletmecilik  ', 'Uluslararası Ticaret ve İşletmecilik  '),
    ('Uluslararası Ticaret ve Lojistik  ', 'Uluslararası Ticaret ve Lojistik  '),
    ('Uluslararası Ulaştırma Sistemleri  ', 'Uluslararası Ulaştırma Sistemleri  '),
    ('Un ve Unlu Mamuller Teknolojisi ', 'Un ve Unlu Mamuller Teknolojisi '),
    ('Urdu Dili ve Edebiyatı  ', 'Urdu Dili ve Edebiyatı  '),
    ('Üretimde Kalite Kontrol ', 'Üretimde Kalite Kontrol '),
    ('Uygulamalı İngilizce Çevirmenlik ', 'Uygulamalı İngilizce Çevirmenlik '),
    ('Uygulamalı İspanyolca Çevirmenlik (İspanyolca) ', 'Uygulamalı İspanyolca Çevirmenlik (İspanyolca) '),
    ('Uygulamalı Rusça Çevirmenlik (Rusça) ', 'Uygulamalı Rusça Çevirmenlik (Rusça) '),
    ('Uzay Bilimleri ve Teknolojileri  ', 'Uzay Bilimleri ve Teknolojileri  '),
    ('Uzay Mühendisliği  ', 'Uzay Mühendisliği  '),
    ('Uzay ve Uydu Mühendisliği  ', 'Uzay ve Uydu Mühendisliği  '),
    ('Veteriner  ', 'Veteriner  '),
    ('Web Tasarımı ve Kodlama ', 'Web Tasarımı ve Kodlama '),
    ('Yaban Hayatı Ekolojisi ve Yönetimi  ', 'Yaban Hayatı Ekolojisi ve Yönetimi  '),
    ('Yağ Endüstrisi ', 'Yağ Endüstrisi '),
    ('Yapay Zeka Mühendisliği  ', 'Yapay Zeka Mühendisliği  '),
    ('Yapay Zeka ve Veri Mühendisliği  ', 'Yapay Zeka ve Veri Mühendisliği  '),
    ('Yapı Denetimi ', 'Yapı Denetimi '),
    ('Yapı Ressamlığı ', 'Yapı Ressamlığı '),
    ('Yapı Tesisat Teknolojisi ', 'Yapı Tesisat Teknolojisi '),
    ('Yapı Yalıtım Teknolojisi ', 'Yapı Yalıtım Teknolojisi '),
    ('Yaşlı Bakımı ', 'Yaşlı Bakımı '),
    ('Yat Kaptanlığı ', 'Yat Kaptanlığı '),
    ('Yazılım Geliştirme  ', 'Yazılım Geliştirme  '),
    ('Yazılım Mühendisliği  ', 'Yazılım Mühendisliği  '),
    ('Yeni Medya  ', 'Yeni Medya  '),
    ('Yeni Medya ve Gazetecilik ', 'Yeni Medya ve Gazetecilik '),
    ('Yeni Medya ve İletişim  ', 'Yeni Medya ve İletişim  '),
    ('Yerel Yönetimler (2 Yıllık)', 'Yerel Yönetimler (2 Yıllık)'),
    ('Yerel Yönetimler (4 Yıllık)', 'Yerel Yönetimler (4 Yıllık)'),
    ('Yiyecek ve İçecek İşletmeciliği  ', 'Yiyecek ve İçecek İşletmeciliği  '),
    ('Yönetim Bilimleri Programları  ', 'Yönetim Bilimleri Programları  '),
    ('Yönetim Bilişim Sistemleri  ', 'Yönetim Bilişim Sistemleri  '),
    ('Yunan Dili ve Edebiyatı  ', 'Yunan Dili ve Edebiyatı  '),
    ('Zaza Dili ve Edebiyatı    ', 'Zaza Dili ve Edebiyatı    '),
    ('Zeytincilik ve Zeytin İşleme Teknolojisi ', 'Zeytincilik ve Zeytin İşleme Teknolojisi '),
    ('Ziraat Mühendisliği Programları    ', 'Ziraat Mühendisliği Programları    '),
    ('Zootekni', 'Zootekni'),

]

Girisimler = [
    ('Animally', 'Animally'),
    ('Aquapure', 'Aquapure'),
    ('Arte/Make', 'Arte/Make'),
    ('Balkız', 'Balkız'),
    ('Bamboo', 'Bamboo'),
    ('Biged', 'Biged'),
    ('Cardpool', 'Cardpool'),
    ('Cepte Sevgi', 'Cepte Sevgi'),
    ('CezerUni', 'CezerUni'),
    ('ÇİBA APP', 'ÇİBA APP'),
    ('Cli̇ck Enerji̇', 'Cli̇ck Enerji̇'),
    ('Cloudbox', 'Cloudbox'),
    ('Comet', 'Comet'),
    ('Create Yourself', 'Create Yourself'),
    ('Dice Eğitim Setleri', 'Dice Eğitim Setleri'),
    ('DonationToken', 'DonationToken'),
    ('Ecotap', 'Ecotap'),
    ('Elimi Tut', 'Elimi Tut'),
    ('ENGELSİZ İLETİŞİM', 'ENGELSİZ İLETİŞİM'),
    ('ERILUM', 'ERILUM'),
    ('E-Şifa', 'E-Şifa'),
    ('EvdenEle', 'EvdenEle'),
    ('FilthreeX', 'FilthreeX'),
    ('Fişyo', 'Fişyo'),
    ('FOODIES', 'FOODIES'),
    ('FoodPro', 'FoodPro'),
    ('Freedom', 'Freedom'),
    ('FullArt', 'FullArt'),
    ('Gel Gel', 'Gel Gel'),
    ('Girişimciler İçin Girişim', 'Girişimciler İçin Girişim'),
    ('Götürelim', 'Götürelim'),
    ('Gübregaz', 'Gübregaz'),
    ('GÜCÜNÜ BİZDEN AL', 'GÜCÜNÜ BİZDEN AL'),
    ('Günsu', 'Günsu'),
    ('GüvenEli', 'GüvenEli'),
    ('Hidromotor', 'Hidromotor'),
    ('International Student ID', 'International Student ID'),
    ('Kablosuz Holter', 'Kablosuz Holter'),
    ('Kardelen', 'Kardelen'),
    ('Kiddy Kit', 'Kiddy Kit'),
    ('Kitapevski', 'Kitapevski'),
    ('KitAPP', 'KitAPP'),
    ('Kozmodrop', 'Kozmodrop'),
    ('Kutu', 'Kutu'),
    ('LUKOMETR', 'LUKOMETR'),
    ('Medicurism', 'Medicurism'),
    ('Meliloto', 'Meliloto'),
    ('MultiMindsAI', 'MultiMindsAI'),
    ('Musicowboy', 'Musicowboy'),
    ('No-fogfacemask', 'No-fogfacemask'),
    ('Nonzheimer', 'Nonzheimer'),
    ('Now we see too', 'Now we see too'),
    ('Pati İzi', 'Pati İzi'),
    ('PatyVer', 'PatyVer'),
    ('PenFriends', 'PenFriends'),
    ('Petsgram', 'Petsgram'),
    ('Pi̇si̇kocep', 'Pi̇si̇kocep'),
    ('Plastiği Yeniden Amaçlandırma', 'Plastiği Yeniden Amaçlandırma'),
    ('PREDECIR', 'PREDECIR'),
    ('Quik Roam', 'Quik Roam'),
    ('Sanreal Kütüphane', 'Sanreal Kütüphane'),
    ('SATÜ', 'SATÜ'),
    ('SelfCycle', 'SelfCycle'),
    ('Si-Ro', 'Si-Ro'),
    ('Social Jam', 'Social Jam'),
    ('Step', 'Step'),
    ('STEP Tim', 'STEP Tim'),
    ('Stok Ürün', 'Stok Ürün'),
    ('Studygether', 'Studygether'),
    ('Stutools', 'Stutools'),
    ('TabulaRasa', 'TabulaRasa'),
    ('Tamir Plus', 'Tamir Plus'),
    ('Tarımda Otomasyon', 'Tarımda Otomasyon'),
    ('Tester', 'Tester'),
    ('TETA', 'TETA'),
    ('ÜNİDEN', 'ÜNİDEN'),
    ('Univasyon', 'Univasyon'),
    ('Vanswap', 'Vanswap'),
    ('Yükselen Patatesler Topraksız Tarım', 'Yükselen Patatesler Topraksız Tarım'),
    ('Zappmatch', 'Zappmatch'),
]

Girisim_Kategorileri = [
    ('Agriculture', 'Agriculture'),
    ('Biotechnology', 'Biotechnology'),
    ('Business Services', 'Business Services'),
    ('Clean Technology', 'Clean Technology'),
    ('Construction', 'Construction'),
    ('Consulting', 'Consulting'),
    ('Consumer Products', 'Consumer Products'),
    ('Consumer Services', 'Consumer Services'),
    ('Digital Marketing', 'Digital Marketing'),
    ('Education', 'Education'),
    ('Electronics / Instrumentation', 'Electronics / Instrumentation'),
    ('Energy', 'Energy'),
    ('Fashion', 'Fashion'),
    ('Financial Services', 'Financial Services'),
    ('Fintech', 'Fintech'),
    ('Food and Beverage', 'Food and Beverage'),
    ('Gaming', 'Gaming'),
    ('Healthcare Services', 'Healthcare Services'),
    ('Internet / Web Services', 'Internet / Web Services'),
    ('IT Services', 'IT Services'),
    ('Legal', 'Legal'),
    ('Lifestyle', 'Lifestyle'),
    ('Marine', 'Marine'),
    ('Maritime/Shipping', 'Maritime/Shipping'),
    ('Marketing / Advertising', 'Marketing / Advertising'),
    ('Media and Entertainment', 'Media and Entertainment'),
    ('Medical Devices and Equipment', 'Medical Devices and Equipment'),
    ('Mobility', 'Mobility'),
    ('Nanotechnology', 'Nanotechnology'),
    ('Real Estate', 'Real Estate'),
    ('Retailing / Distribution', 'Retailing / Distribution'),
    ('Robotics', 'Robotics'),
    ('Security', 'Security'),
    ('Software', 'Software'),
    ('Sports', 'Sports'),
    ('Telecommunications', 'Telecommunications'),
    ('Transportation', 'Transportation'),
    ('Travel', 'Travel'),
    ('Other', 'Other'),
]


class Firm(models.Model):
    firm_name = models.CharField(max_length=250, verbose_name="Firma Adı", blank=False, null=False)
    firm_domain = models.CharField(max_length=250, verbose_name="Domain", blank=False, null=False)
    bulk_file = models.FileField(upload_to='excel', verbose_name='Excel Dosyası', blank=True, null=True)
    firm_logo = models.FileField(upload_to='firm_logos', verbose_name='Firma Logosu', blank=True, null=True)

    def __str__(self):
        return self.firm_name

    class Meta:
        verbose_name = "Firma"
        verbose_name_plural = "Firmalar"


class Company(models.Model):
    company_name = models.CharField(max_length=250, choices=Girisimler, verbose_name="Girişim Adı", blank=False,
                                    null=False)
    team_size = models.IntegerField(verbose_name="Ekip Büyüklüğü", blank=True, null=True)
    is_tech_exist = models.CharField(max_length=250, choices=Is_Tech_Exist, verbose_name="Teknik Üye Var mı",
                                     blank=False, null=True)
    girisim_kategorisi = models.CharField(max_length=250, choices=Girisim_Kategorileri,
                                          verbose_name="Girişim Kategorisi", blank=False, null=True)
    bootcamp_name = models.CharField(verbose_name="Bootcamp Adı", null=True, blank=False, max_length=250,
                                     choices=universiteler)
    enterprise_summary = models.CharField(max_length=450, verbose_name="Girişim Özeti", null=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = "Girişim"
        verbose_name_plural = "Girişimler"


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    username = None

    sehir = models.CharField(default='İstanbul', max_length=250, choices=Cities, verbose_name="Şehir", blank=False,
                             null=False)
    dogum_gunu = models.DateTimeField(default=timezone.datetime.now, verbose_name="Doğum Günü", blank=False, null=False)
    cinsiyet = models.CharField(default=Cinsiyetler[0][0], max_length=250, choices=Cinsiyetler, verbose_name="Cinsiyet",
                                blank=False, null=False)
    universite = models.CharField(default=universiteler[0][0], max_length=250, choices=universiteler,
                                  verbose_name="Üniversite", blank=False, null=False)
    sinif = models.CharField(default=Siniflar[0][0], max_length=250, choices=Siniflar, verbose_name="Sınıf",
                             blank=False, null=False)
    bolum = models.CharField(default=bolumler[0][0], max_length=250, choices=bolumler, verbose_name="Bölüm",
                             blank=False, null=False)
    telefon = models.CharField(default='', max_length=11, verbose_name="Telefon", blank=False, null=False)
    linkedin_url = models.URLField(default='', max_length=250, verbose_name="Linkedin URL", blank=True, null=False)
    bio = models.CharField(default='', max_length=999, verbose_name="Hakkımda", blank=True, null=False)
    is_profile_completed = models.BooleanField(default=False)
    is_teamleader = models.BooleanField(default=False, verbose_name="Ekip Lideri", blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE, null=True)
    is_firm_manager = models.BooleanField(default=False, verbose_name="Firma Yöneticisi", blank=True, null=True)
    objects = UserManager()

    pass


class Article(models.Model):
    article_header = models.CharField(max_length=350, verbose_name="Article Başlığı", blank=True, null=True)
    article_description = models.TextField(verbose_name="Article Açıklaması", blank=False, null=False)
    date_created = models.DateField(auto_now_add=True, verbose_name="Oluşturma Tarihi", blank=False, null=False)
    image_900 = models.FileField(upload_to='article_images', verbose_name='Article Image', null=False,
                                 help_text="Fotoğrafınızın boyutunun oranının 9:4 olmasına dikkat edin")
    text = models.TextField(verbose_name="Yazı İçeriği", blank=False, null=False)

    def __str__(self):
        return self.article_header

    class Meta:
        verbose_name = "Yazı İçeriği"
        verbose_name_plural = "Yazı İçerikleri"


class MultipleQuestion(models.Model):
    actual_question = models.CharField(max_length=350, verbose_name="Test Sorusu", blank=False, null=False)
    q_order = models.IntegerField(verbose_name="Sorunun Sıra Numarası", blank=False, null=False)
    is_required = models.BooleanField(verbose_name="Zorunlu Alan", blank=False, null=False, default=False)

    class Meta:
        ordering = ('q_order',)
        verbose_name = "Çoktan Seçmeli Soru"
        verbose_name_plural = "Çoktan Seçmeli Sorular"

    def __str__(self):
        return self.actual_question


class MultipleChoice(models.Model):
    actual_question = models.ForeignKey(MultipleQuestion, on_delete=models.CASCADE, null=True, blank=True)
    choice = models.CharField(max_length=350, verbose_name="Şık", blank=False)
    q_order = models.IntegerField(verbose_name="Şık Sıra Numarası", blank=False)

    class Meta:
        ordering = ('q_order',)

    def __str__(self):
        return self.choice


class OptionQuestion(models.Model):
    actual_question = models.CharField(max_length=550, verbose_name="Seçimlik Soru", blank=False)
    q_order = models.IntegerField(verbose_name="Sorunun Sıra Numarası", blank=False)
    is_required = models.BooleanField(verbose_name="Zorunlu Alan", blank=False, null=False, default=False)

    class Meta:
        ordering = ('q_order',)
        verbose_name = "Açılır Menülü Soru"
        verbose_name_plural = "Açılır Menülü Sorular"

    def __str__(self):
        return self.actual_question


class OptionChoice(models.Model):
    actual_question = models.ForeignKey(OptionQuestion, on_delete=models.CASCADE, null=True, blank=True)
    choice = models.CharField(max_length=350, verbose_name="Seçenek", blank=False, null=False)
    q_order = models.IntegerField(verbose_name="Seçenek Sıra Numarası", blank=False, null=False)

    class Meta:
        ordering = ('q_order',)

    def __str__(self):
        return self.choice


class TextQuestion(models.Model):
    actual_question = models.CharField(max_length=350, verbose_name="Text Sorusu", blank=False, null=False)
    q_order = models.IntegerField(verbose_name="Sorunun Sıra Numarası", blank=False, null=False)
    is_required = models.BooleanField(verbose_name="Zorunlu Alan", blank=False, null=False, default=False)

    def __str__(self):
        return self.actual_question

    class Meta:
        ordering = ('q_order',)
        verbose_name = "Text Sorusu"
        verbose_name_plural = "Text Soruları"


class Survey(models.Model):
    survey_header = models.CharField(max_length=350, verbose_name="Anket Başlığı", blank=False, null=False)
    survey_description = models.TextField(verbose_name="Anket Açıklaması", blank=False, null=False)
    date_created = models.DateField(auto_now_add=True, verbose_name="Oluşturma Tarihi", blank=False, null=False)
    text_question = models.ManyToManyField(TextQuestion, blank=True)
    option_question = models.ManyToManyField(OptionQuestion, blank=True)
    choice_question = models.ManyToManyField(MultipleQuestion, blank=True)

    def __str__(self):
        return self.survey_header

    def save(self, *args, **kwargs):
        super(Survey, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Anket"
        verbose_name_plural = "Anketler"


class SurveyAnswer(models.Model):
    survey_participant = models.ForeignKey(User, verbose_name="Anket Katılımcısı", on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, verbose_name="İlgili Anket", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Anket Cevabı"
        verbose_name_plural = "Anket Cevapları"


class SurveyAnswerFromQuestionText(models.Model):
    survey_answer = models.ForeignKey(SurveyAnswer, verbose_name="İlgili Cevap", on_delete=models.CASCADE)
    question = models.ForeignKey(TextQuestion, verbose_name="İlgili Text Sorusu", on_delete=models.CASCADE)
    answer = models.CharField(max_length=450, verbose_name="Text Cevabı", blank=True, null=True)


class SurveyAnswerFromQuestionOption(models.Model):
    survey_answer = models.ForeignKey(SurveyAnswer, verbose_name="İlgili Cevap", on_delete=models.CASCADE)
    question = models.ForeignKey(OptionQuestion, verbose_name="İlgili Dropdown", on_delete=models.CASCADE)
    answer = models.ForeignKey(OptionChoice, verbose_name="Dropdown Cevabı", on_delete=models.CASCADE, blank=True,
                               null=True)


class SurveyAnswerFromQuestionChoice(models.Model):
    survey_answer = models.ForeignKey(SurveyAnswer, verbose_name="İlgili Cevap", on_delete=models.CASCADE)
    question = models.ForeignKey(MultipleQuestion, verbose_name="İlgili Seçimlik Soru", on_delete=models.CASCADE)
    answer = models.ForeignKey(MultipleChoice, verbose_name="Çoktan Seçmeli Cevabı", on_delete=models.CASCADE,
                               blank=True, null=True)


class Video(models.Model):
    video_header = models.CharField(max_length=350, verbose_name="Video Başlığı", blank=False, null=False)
    video_description = models.TextField(verbose_name="Video Açıklaması", blank=False, null=False)
    date_created = models.DateField(auto_now_add=True, verbose_name="Oluşturma Tarihi", blank=False, null=False)
    video = fields.VimeoField(null=True, blank=True)

    def __str__(self):
        return self.video_header

    class Meta:
        verbose_name = "Video İçeriği"
        verbose_name_plural = "Video İçerikleri"


class Batch(models.Model):
    batch_name = models.CharField(max_length=250, verbose_name="Batch Adı", blank=False, null=False)
    batch_description = models.TextField(verbose_name="Batch Açıklaması", blank=False, null=True)
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE, blank=False, null=True)

    def __str__(self):
        return self.batch_name

    class Meta:
        verbose_name = "Batch"
        verbose_name_plural = "Batch'ler"


class Module(models.Model):
    module_name = models.CharField(max_length=250, verbose_name="Modül Adı", blank=False, null=False)
    batch_related = models.ForeignKey(Batch, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        m_name = str(self.module_name)
        b_name = str(self.batch_related)
        return b_name + " " + m_name

    class Meta:
        verbose_name = "Modül"
        verbose_name_plural = "Modüller"


class Content(models.Model):
    content_type = models.CharField(max_length=250, choices=ContentTypes, verbose_name="İçerik Tipi", blank=False,
                                    null=False)
    content_description = models.TextField(verbose_name="Content Açıklaması", blank=False, null=True)
    content_image = models.FileField(upload_to='content_images', verbose_name='Content Fotoğrafı', blank=True,
                                     null=True,
                                     help_text="Fotoğrafınızın boyutunun 150x150 olmasına dikkat edin",
                                     default="settings.MEDIA_ROOT/content-image.jpg")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, null=True, blank=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True, blank=True)
    module_related = models.ForeignKey(Module, on_delete=models.CASCADE, null=True, blank=True, )

    def __str__(self):
        if self.article:
            return self.article.article_header
        if self.survey:
            return self.survey.survey_header
        if self.video:
            return self.video.video_header

    class Meta:
        verbose_name = "İçerik"
        verbose_name_plural = "İçerikler"


User._meta.get_field('email')._unique = True
Video._meta.get_field('video_header')._unique = True
Survey._meta.get_field('survey_header')._unique = True
Article._meta.get_field('article_header')._unique = True
