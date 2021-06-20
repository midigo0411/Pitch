from ..models import Category, Pitch, Comment, User
from flask import render_template, redirect, url_for, request
from . import main
from flask_login import login_required, current_user
from .forms import CommentForm, PitchForm, UpdateProfilePic
from sqlalchemy import desc
from .. import photos, db





#index page
@main.route('/', methods =['GET', 'POST'])
def index():
    '''
    View the root page function it returns the index page
    '''
    mypitches = Mypitch.get_mypitches()
    form = PitchForm()
    title = 'Home | Mypitch'
