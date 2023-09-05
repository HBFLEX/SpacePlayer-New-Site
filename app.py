import time
from flask import Flask, render_template, request
from database import db_session
from models import Downloads, Visits
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

selected_platform = { 'value': '' }

#configurations
app.config['SECRET_KEY'] = '76b0d59da5369832426b19f44b6ed80b'

# remove database sessions at the end of the request or when the app
# shuts down
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

# app routes

@app.route('/')
@app.route('/home')
def home_page():
    context = {'title': 'SpacePlayer - Download a light-weight desktop media app for free'}
    if request.method == 'GET':
        total_visits = Visits.query.first()
        total_visits.num_of_visits += 1
        db_session.commit()
    return render_template('home.html', context=context)


@app.route('/download', methods=['GET', 'POST'])
def download():
    context = { 'title': 'Thank you for downloading my app, have a wonderful day' }
    if request.method == 'POST':
        download_value = request.form['downloads']
        if download_value == 'windows':
            selected_platform.update({ 'value': 'windows' })
            context.update({'platform': 'windows'})

        if download_value == 'linux':
            selected_platform.update({ 'value': 'linux' })
            context.update({'platform': 'linux'})
    return render_template('download.html', context=context)


@app.route('/download/started', methods=['POST'])
def download_started():
    if request.json:
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            incoming_data = request.json

            if incoming_data['isDownloadStarted'] == 'yes':
                if selected_platform['value'] == 'windows':
                    total_downloads = Downloads.query.first()
                    total_downloads.windows_no_of_downloads += 1
                    total_downloads.total_num_of_downloads += 1
                    db_session.commit()
                
                if selected_platform['value'] == 'linux':
                    total_downloads = Downloads.query.first()
                    total_downloads.linux_no_of_downloads += 1
                    total_downloads.total_num_of_downloads += 1
                    db_session.commit()          
    return request.json


@app.route('/hbfl3x/soundplay265/admin')
def dashboard():
    context = {
        'total_num_of_visits': Visits.query.first().num_of_visits,
        'windows_no_of_downloads': Downloads.query.first().windows_no_of_downloads,
        'linux_no_of_downloads': Downloads.query.first().linux_no_of_downloads,
        'total_num_of_downloads': Downloads.query.first().total_num_of_downloads
    }
    return render_template('dashboard.html', context=context)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)