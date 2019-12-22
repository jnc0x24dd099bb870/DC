import os
import time

import json
import redis
from flask import Blueprint, request, render_template
from extensions import mysql, cache


home_api = Blueprint('home', __name__)
submit_api = Blueprint('submit', __name__)
visitors_api = Blueprint('visitors', __name__)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@submit_api.route('/submit', methods=['GET', 'POST'])
def submit():
    visitor_name = request.form['visitor_name']
    try:
        
        connection = mysql.connect()
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS `visitors` (  `name` VARCHAR(100) NOT NULL);''')
        
        #no sql injection...
        cursor.execute('''INSERT INTO `visitors` (name) VALUES (%s);''', (visitor_name));

        connection.commit()

    except Exception as e:
        return json.dumps({'error':str(e)})

    return render_template('thanks.html', name=visitor_name)


@visitors_api.route('/visitors', methods=['GET', 'POST'])
def visitors():
    try:
   
        connection = mysql.connect()
        cursor = connection.cursor()
        cursor.execute('''SELECT DISTINCT name FROM visitors''')
        result = cursor.fetchall()

        unique_names = []
        for entry in result:
            record = entry[0]
            unique_names.append(record)
    except Exception as e:
        return json.dumps({'error':str(e)})

    return render_template('visitors.html', names=unique_names)

@home_api.route('/', methods=['GET', 'POST'])
def home():
    count = get_hit_count()
    return render_template('home.html', count=count)
