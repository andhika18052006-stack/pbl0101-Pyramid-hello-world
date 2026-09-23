from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from datetime import datetime

def hello_world(request):
    waktu_saat_ini = datetime.now().strftime("%Y-%m-%d %H:%M:S")

    html_content = f"""
    <h1>HELLO WORLD</h1>
    <p>#PBW3BIPBL0101</P>
    <p><b>251080200013</p></b>
    <p><b>Andhika_Pratama</b></p>
    <p>Framework Pilihan &rarr; python[6] - Pyramid</p>
    <p>TIME : {waktu_saat_ini}</p>
    """
    return Response(html_content, content_type='text/html')

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
