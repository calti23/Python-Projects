import turtle
turtle.Turtle();

t = turtle.Turtle();
w = turtle.Screen();
#BAŞLIK
w.title("Grafik Çalışması");
#PENCERE BOYUTU
w.setup(width = 720,height = 420);
#ARKA PLAN RENGİ
w.bgcolor("White");

#DAİRE ÇİZİMİ
t.up();
#FARE İMLECİ KONUMU
t.goto(0,-100);
#BEYAZ RENK
t.color('red');
#BEYAZ RENGİ DOLDUR
t.begin_fill();
#DAİRE YARIÇAPI
t.circle(100);
t.end_fill();

#YILDIZ ÇİZMEYE HAZIRLIK
t.goto(-75,30);
t.fillcolor('black');
t.begin_fill();
#YILDIZ İÇİN TEKRAR EDEN ÜÇGEN ÇİZİMİ
for i in range(5):
    t.forward(150);
    t.right(144);
t.end_fill();

#YAZI YAZMA
t.goto(-150,-130);
t.write("EYLÜL BU SANA GELSİN :D" , font=("Articulate" , 17 , "bold"));

#İMLECİ UZAKLAŞTIR
t.goto(-999,0);

#PROGRAMI KAPAT
t.exitonclick();



