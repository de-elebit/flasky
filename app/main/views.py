from datetime import datetime
from flask import Flask, render_template, session, redirect, url_for, flash
from . import main
from .forms import NameForm
from .. import db
from ..models import User


@main.route("/", methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        # user = User.query.filter_by(useranme=form.name.data).first()
        # if user is None:
        #     user = User(form.name.data)
        #     db.session.add(user)
        #     db.session.commit()
        #     session['known'] = False
        #     if app.config['FLASKY_ADMIN']:
        #         send_mail(app.config['FLASKY_ADMIN'], 'New User', 'mail/new_user', user=user)
        # else:
        #     session['known'] = True
        # session['name'] = form.name.data
        # form.name.data = ''
        return redirect(url_for('index'))
    return render_template("index.html",
                           form=form, name=session.get('name'),
                           known=session.get('known', False),
                           current_time=datetime.utcnow())
