from flask_blog import app
#from waitress import serve

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    #serve(app, host='0.0.0.0', port=8080)
