from django.shortcuts import render

def show_main(request):
    members = [
        {
            'nama': 'Gaara maheswara fahar ramadhan',
            'tanggal_lahir': '08-09-2008',
            'hobi': 'Berteori',
            'motivasi': '"Akan ada saatnya anak mama ini jadi pemain profesional"',
            'instagram': '@alfonsodestephanus',
            'img_url': 'static/images/garra2.jpeg',
            'ig':'https://www.instagram.com/alfonsodestephanus/'
        },
        {
            'nama': 'Alfarel Rafeliano',
            'tanggal_lahir': '12-01-2007',
            'hobi': 'Badminton,game,denger musik,menghayal berdua dengan Adel',
            'motivasi': '"Terus menghayal hingga hanyalan itu menjadi nyata"',
            'instagram': '@alfarellll_',
            'img_url': 'static/images/alvaarel.jpeg',
            'ig': 'https://www.instagram.com/alfarellll_/'
        },
        {
            'nama': 'Satria Abdillah Akbar',
            'tanggal_lahir': '16-05-2008',
            'hobi': 'Nonton Anime, Denger musik, Hunting Anime Di dunia nyata',
            'motivasi': '"Terkadang Menjadi Wibu bukanlah Hal yang buruk"',
            'instagram': '@sabdibar1.0',
            'img_url': 'static/images/satria.jpeg',
            'ig':'https://www.instagram.com/sabdibar1.0/'
        },
        {
            'nama': 'Frizzy Robyan Ilham',
            'tanggal_lahir': '14-04-2008',
            'hobi': 'Mainin bola bukan hati orang',
            'motivasi': '"Jangan menyerah dan terus berjuang kawan."',
            'instagram': '@frizzyrobyanilham',
            'img_url': 'static/images/frizzi.jpeg',
            'ig':'https://www.instagram.com/frizzyrobyanilham/'
        },
        {
            'nama': 'Muhammad Ali',
            'tanggal_lahir': '07-10-2007',
            'hobi': 'Main basket, game,denger musik,berharap kamu balik lagi ke aku padahal gabisa',
            'motivasi': '"Lakukan apa yang kamu sukai dan kejarlah apa yang kamu impikan"',
            'instagram': '@liiialiiiii10',
            'img_url': 'static/images/ali2.jpeg',
            'ig': 'https://www.instagram.com/liiialiiii10/'
        }
    ]
    return render(request, 'main.html', {'members': members})

def show_game(request):
    games = [
        {
            'nama': 'Flappy Bird',
            'deskripsi': 'Terbanglah bersama Flappy Bird, mengendalikan burung kecil dengan sekali ketukan layar! Hindari pipa-pipa menantang dan kalahkan teman-teman dengan skor tertinggi Anda. Rasakan ketegangan yang intens seiring berjalannya waktu dan nikmati keseruan yang adiktif. Siapkah Anda untuk menaklukkan langit dalam permainan yang menantang ini? Ayo mainkan Flappy Bird sekarang dan buktikan kemampuan Anda!',
            'img_url': 'https://assets.ggwp.id/2023/04/sejarah-game-flappy-bird-2.jpg'
        },
        {
            'nama': 'Bulls Eye',
            'deskripsi': 'Uji Keterampilan Memanah Anda! Bulls Eye Archery membawa sensasi memanah langsung ke layar Anda. Tarik panah, bidik sasaran, dan raih Bulls Eye! Grafis SVG yang memukau membuat pengalaman memanah semakin mendebarkan. Siapkan diri Anda untuk tantangan terbesar!',
            'img_url': 'https://i.pinimg.com/474x/30/8d/61/308d61626cc060d580acd57f3dc24b4f.jpg'
        }
    ]
    return render(request, 'game.html', {'games': games})

def show_video(request):
    context={}
    return render(request, 'video.html', context)

def show_flappy(request):
    context={}
    return render(request, 'flappy.html', context)

def show_bulls_eye(request):
    context={}
    return render(request, 'bulls_eye.html', context)