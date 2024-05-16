from Website import create_website
import os

ASSETS_DIR = os.path.dirname(os.path.abspath(__file__))

if __name__=='__main__':
    app = create_website()
    context = ('cert.pem', 'key.pem')
    app.run(debug=True, ssl_context=context)