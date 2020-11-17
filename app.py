from flask import Flask, render_template
import time

app = Flask(__name__)

@app.route('/')
def hola(name=None):
    return render_template('hola.html')

@app.route('/calcula/<param1>/<param2>')
def calcula(param1=None,param2=None):
    if param1 and param2 :
        ###########################################
        # Here you will do some complex calculations
        # I recommend encapsulate your code in a module,
        # import it here, make the calculation in a separate
        # thread, send back the results using server push...
        # but, as this is just an exercise, just copy/paste
        # your code here ;)
        ###########################################
        time.sleep(3) # Simulating complex calculations...
        return {'resultado':param1+param2}
    return {'error':'At least one parameter is null'}
