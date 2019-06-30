
from datetime import datetime

from flask import render_template, redirect, request

from FlaskPolls import app
from FlaskPolls.models import PollNotFound
from FlaskPolls.models.factory import create_repository
from FlaskPolls.settings import REPOSITORY_NAME, REPOSITORY_SETTINGS

repository = create_repository(REPOSITORY_NAME, REPOSITORY_SETTINGS)

@app.route('/')
@app.route('/home')
def home():
    """home page, with a list of all polls."""
    return render_template(
        'index.html',
        title='Polls',
        year=datetime.now().year,
        polls=repository.get_polls(),
    )

@app.route('/contact')
def contact():
    """contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
    )

@app.route('/about')
def about():
    """about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        repository_name=repository.name,
    )

@app.route('/seed', methods=['POST'])
def seed():
    """db with the poll result."""
    repository.add_sample_polls()
    return redirect('/')

@app.route('/results/<key>')
def results(key):
    """results page."""
    poll = repository.get_poll(key)
    poll.calculate_stats()
    return render_template(
        'results.html',
        title='Results',
        year=datetime.now().year,
        poll=poll,
    )

@app.route('/poll/<key>', methods=['GET', 'POST'])
def details(key):
    """details page."""
    error_message = ''
    if request.method == 'POST':
        try:
            choice_key = request.form['choice']
            repository.increment_vote(key, choice_key)
            return redirect('/results/{0}'.format(key))
        except KeyError:
            error_message = 'Please make a selection.'
    return render_template(
        'details.html',
        title='Poll',
        year=datetime.now().year,
        poll=repository.get_poll(key),
        error_message=error_message,
    )

#@app.route("/poll", methods=['POST'])
#def next():
#    """back-return page."""
#     return render_template(
#        'return.html',
#        title='back',
#    )

@app.errorhandler(PollNotFound)
def page_not_found(error):
    """error page."""
    return 'Poll does not exist.', 404


