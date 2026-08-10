import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import warnings
warnings.filterwarnings("ignore")

#PLOTLY KÜTÜPHANESİNİ İÇE AKTARIYORUZ
from plotly.offline import iplot , plot
import plotly as py
import plotly.graph_objs as go
import plotly.io as pio
import plotly.figure_factory as ff

veri = pd.read_csv("timesData.csv")

print(veri.tail(3))

#SÜTUN İSİMLERİNİ TÜRKÇE YAPALIM
veri.rename(columns = {'world_rank' : 'dünya_sıralama' ,
                       'university_name' : 'üni_isim' ,
                       'country' : 'ülke' ,
                       'teaching' : 'öğretim' ,
                       'international' : 'uluslararası' ,
                       'research' : 'araştırma' ,
                       'citations' : 'alıntı' ,
                       'income' : 'gelir' ,
                       'total_score' : 'toplam_puan' ,
                       'num_students' : 'öğrenci_sayısı' ,
                       'student_staff_ratio' : 'öğrenci_çalışan_oranı' ,
                       'international_students' : 'uluslararası_öğrenci' ,
                       'female_male_ratio' : 'kadın_erkek_oranı' ,
                       'year' : 'yıl'
                       } , inplace = True)
print(veri.head(3))

print("-" * 70)

#ÇİZGİ GRAFİĞİ
#cizgi1 = go.Scatter(x = df.dunya_siralama,   #X EKSENİNDE DÜNYA SIRALAMASI OLSUN
#                    y = df.alinti,           #Y EKSENİNDE ALINTI OLSUN
#                    mode = "lines+markers", #GRAFİK ÇİZGİ VE SAÇILIM OLSUN
#                   name = "Alıntı",        #ETİKETİ ALINTI OLSUN
#                    marker = dict(color = 'rgba(78, 78, 250, 0.85)'), # RENK
#                    text = df.uni_isim)     #GRAFİK ÜZERİNDE İMLEÇ İLGİLİ NOKTAYA GELİNCE, ÜNİVERSİTE İSMİ YAZSIN

#İKİNCİ GRAFİK
#cizgi2 = go.Scatter(x = df.dunya_siralama,   #X EKSENİNDE DÜNYA SIRALAMASI OLSUN
#                    y = df.ogretim,          #Y EKSENİNDE EĞİTİM-ÖĞRETİM FAALİYETLERİNDEN ALINAN PUAN OLSUN
#                    mode = "lines+markers", #GRAFİK ÇİZGİ VE SAÇILIM OLSUN
#                   name = "Öğretim",       #ETİKETİ ÖĞRETİM OLSUN
#                   marker = dict(color = 'rgba(202, 43, 15, 0.85)'), # RENK
#                   text = df.uni_isim)     #GRAFİK ÜZERİNDE İMLEÇ İLGİLİ NOKTAYA GELİNCE, ÜNİVERSİTE İSMİ YAZSIN

#veri_ = [cizgi1, cizgi2]  #2 GRAFİĞİ VERİ_ DEĞİŞKENİ İÇERİSİNE KOY

#BAŞLIK EKLE VE EKSEN AYARLARINI YAP
#yerlesim = dict(title = 'Dünya Sıralamasında İlk 100 Üniversitenin Alıntı ve Öğretim Puanları',
#                xaxis = dict(title = 'Dünya Sıralaması', ticklen = 5, zeroline = False))

#fig = dict(data = veri_, layout = yerlesim)  # FİGÜR OLUŞTUR
#plot(fig, filename = '1_cizgi-alıntı ve öğretim puanları.html')  # .HTML OLARAK KAYDET

#SAÇILIM GRAFİĞİ
#14'-15'-16' YILLARINI AYIRALIM VE İLK 100 ER ÖRNEĞİ ALALIM
veri2014 = veri[veri.yıl == 2014].iloc[:100 , :]
veri2015 = veri[veri.yıl == 2015].iloc[:100 , :]
veri2016 = veri[veri.yıl == 2016].iloc[:100 , :]

çizgi1 = go.Scatter(x = veri2014.dünya_sıralama,   
                    y = veri2014.alıntı,         
                    mode = "markers",
                    name = "2014",        
                    marker = dict(color = 'rgba(78, 78, 250, 0.85)'), 
                    text = veri2014.üni_isim)

çizgi2 = go.Scatter(x = veri2015.dünya_sıralama,  
                    y = veri2015.alıntı,     
                    mode = "markers", 
                    name = "2015",       
                    marker = dict(color = 'rgba(202, 180, 15, 0.85)'), 
                    text = veri2015.üni_isim)

çizgi3 = go.Scatter(x = veri2016.dünya_sıralama,  
                    y = veri2016.alıntı,     
                    mode = "markers", 
                    name = "2016",       
                    marker = dict(color = 'rgba(88, 43, 105, 0.85)'), 
                    text = veri2016.üni_isim)

veri_ = [çizgi1, çizgi2 ,çizgi3]  
yerleşim = dict(title = '2014-2015-2016 İlk 100 Üniversitenin Alıntı ve Dünya Sıralaması',
                xaxis = dict(title = 'Dünya Sıralaması', ticklen = 5, zeroline = False) ,
                yaxis = dict(title = 'Alıntı' , ticklen = 5 , zeroline = False))

fig = dict(data = veri_, layout = yerleşim)  
plot(fig, filename = '2-sacilim 2014-2015-2016 ilk 100-alıntı puanları.html') 

#ÇUBUK GRAFİĞİ
#2014 YILININ İLK 5 VERİSİNİ ALALIM
veri2014 = veri[veri.yıl == 2014].iloc[:5 , :]
#İLK GRAFİK
çizgi1 = go.Bar(x = veri2014.üni_isim , y = veri2014.alıntı,
                name = "Alıntı" , marker = dict(color = 'rgba(255 , 127 , 39 , 0.5)' , #ÇUBUK RENGİ
                                  line = dict(color = 'rgb(0 , 0 , 0)' , width = 1.5)) , #ÇUBUK ETRAFINDAKİ ÇİZGİLERİN KALINLIKLARI VE RENKLERİ
                text = veri2014.ülke)

#İKİNCİ GRAFİK
çizgi2 = go.Bar(x = veri2014.üni_isim , y = veri2014.öğretim,
                name = "Öğretim" , marker = dict(color = 'rgba(64 , 0 , 128 , 0.5)' , #ÇUBUK RENGİ
                                  line = dict(color = 'rgb(0 , 0 , 0)' , width = 1.5)) , #ÇUBUK ETRAFINDAKİ ÇİZGİLERİN KALINLIKLARI VE RENKLERİ
                text = veri2014.ülke)

veri_ = [çizgi1 , çizgi2]
yerleşim = go.Layout(barmode = "group")
fig = go.Figure(data = veri_ , layout = yerleşim)
plot(fig)

#DAİRESEL GRAFİK
#2016 YILININ İLK 8 ÜNİVERSİTESİNİ ALALIM
veri2016 = veri[veri.yıl == 2016].iloc[:8 , :]

dilim1 = veri2016.öğrenci_sayısı
dilim1_liste = [float(each.replace(',' , '.')) for each in veri2016.öğrenci_sayısı] #str(2,4) --> str(2.4) --> float(2.4)
etiketler = veri2016.üni_isim

#İLK GRAFİK
çizgi = go.Pie(labels = etiketler , values = dilim1_liste ,
                hoverinfo = 'label+value+percent' , #HOVERİNFO : VERİDE GEZİNİRKEN ÇIKMASI İSTENE DEĞERLER TEXTİNFO : METİN OLARAK ÇIKMASI İSTENEN
                textinfo = 'value+percent' , #TEXTİNFO : METİN OLARAK ÇIKMASI İSTENEN
                textfont = dict(size = 8) ,
                rotation = 180 , 
                hole = 0.3 , #HOLE : PASTANIN ORTASINDA DELİK OLMASI İÇİN
                marker = dict(line = dict(color = '#000000' , width = 1)))
veri_ = [çizgi]
yerleşim = dict(title = '2016 Yılında Dünya Sıralamasında İlk 8 De Bulunan Üniversitelerin Öğrenci Sayıları ve Oranları' ,
                legend = dict(orientation = "h"))
fig = dict(data = veri_ , layout = yerleşim)
plot(fig)
