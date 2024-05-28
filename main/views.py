from django.shortcuts import render

def show_main(request):
    members = [
        {
            'nama': 'Gaara maheswara fahar ramadhan',
            'tanggal_lahir': '08-09-2008',
            'hobi': 'Berteori',
            'motivasi': '"Akan ada saatnya anak mama ini jadi pemain profesional"',
            'instagram': '@alfonsodestephanus',
            'img_url': 'static/images/garra2.jpeg'
        },
        {
            'nama': 'Alfarel Rafeliano',
            'tanggal_lahir': '12-01-2007',
            'hobi': 'Badminton,game,denger musik,menghayal berdua dengan Adel',
            'motivasi': '"Terus menghayal hingga hanyalan itu menjadi nyata"',
            'instagram': '@alfarellll_',
            'img_url': 'static/images/alvaarel.jpeg'
        },
        {
            'nama': 'Satria Abdillah Akbar',
            'tanggal_lahir': '16-05-2008',
            'hobi': 'Nonton Anime, Denger musik, Hunting Anime Di dunia nyata',
            'motivasi': '"Terkadang Menjadi Wibu bukanlah Hal yang buruk"',
            'instagram': '@sabdibar1.0',
            'img_url': 'static/images/satria.jpeg'
        },
        {
            'nama': 'Muhammad Ali',
            'tanggal_lahir': '07-10-2007',
            'hobi': 'Main basket, game,denger musik,berharap kamu balik lagi ke aku padahal gabisa',
            'motivasi': '"Lakukan apa yang kamu sukai dan kejarlah apa yang kamu impikan"',
            'instagram': '@liiialiiiii10',
            'img_url': 'static/images/ali2.jpeg'
        },
        {
            'nama': 'Frizzy Robyan Ilham',
            'tanggal_lahir': '14-04-2008',
            'hobi': 'Mainin bola bukan hati orang',
            'motivasi': '"Terkadang Menjadi Wibu bukanlah Hal yang buruk"',
            'instagram': '@frizzyrobyanilham',
            'img_url': 'static/images/frizzi.jpeg'
        }
    ]
    return render(request, 'main.html', {'members': members})

def show_game(request):
    context={}
    return render(request, 'game.html', context)

def show_video(request):
    context={}
    return render(request, 'game.html', context)