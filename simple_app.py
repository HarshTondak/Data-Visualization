import justpy as jp

def app():
    wp = jp.QuasarPage()

    h1 = jp.QDiv(a=wp, text="Analisys of Course Reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These graphs represents course reviews available")

    return wp

jp.justpy(app)