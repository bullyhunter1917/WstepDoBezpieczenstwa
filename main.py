from Website import create_website

if __name__=='__main__':
    app = create_website()

    app.run(debug=True)