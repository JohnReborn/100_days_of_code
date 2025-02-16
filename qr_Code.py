import qrcode 

mycode = qrcode.make("https://www.youtube.com/watch?v=XWF74wsUaLQ")


mycode.make_image(fill_color = 'black',
                  back_color = 'green')
mrcode.save("surpriseQR.png",scale = 8)

