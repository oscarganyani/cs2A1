#Oscar Ganyani
#Capstone (Lightweight File manager)
#15 August 2022

import subprocess
from flask import Flask
from flask import render_template_string
from flask import redirect
from flask import request
import os

#web app instance
app = Flask(__name__)

#handle root route
@app.route('/')
def root():
    return render_template_string('''
        <html>
            <head>
                <title>File Manager</title>
            </head>
            <body>
                <div align="center">
                    <h1>Local File System</h1>
                    <p><strong>CWD: </strong>{{current_working_directory}}</p>
                </div>
                <ul>
                    <li><a href="/level_up">..</a></li>
                    {% for item in file_list[0: -1] %}
                        {% if '.' not in item%}
                            <li><strong><a href="/cd?path={{current_working_directory + '/' + item}}">{{item}}</strong></li>
                        {%else%}
                            <li>{{item}}</li>
                        {%endif%}
                    {% endfor %}
                </ul>
            </body>
        <html>
    ''', current_working_directory = os.getcwd(), file_list = subprocess.check_output('ls', shell=True).decode('utf-8').split('\n'))

#hangle 'level up' command
@app.route('/level_up')
def level_up():
    #run 'level up' command
    os.chdir('..')

    #redirect to file manager
    return redirect('/')

#hangle 'cd' command
@app.route('/cd')
def cd():
    #run 'cd' command
    os.chdir(request.args.get('path'))

    #redirect to file manager
    return redirect('/')

#run the HTTP server
if __name__ == '__main__':
    app.run(debug=True, threaded=True)