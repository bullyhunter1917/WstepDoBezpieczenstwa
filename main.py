from Website import create_website

if __name__=='__main__':
    app = create_website()
    app.app_context().push()

    app.run(debug=True)
