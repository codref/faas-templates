from __main__ import app

@app.route('/something', methods=['GET'])
def my_handler():
    return 'it works!'