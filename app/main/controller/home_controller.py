from flask import render_template, Blueprint

def construct_home(env):
    home_page = Blueprint(__name__, 'home_page', template_folder='app/templates')
    
    @home_page.route('/')
    def get():
        return render_template('index.html', environment=env )

    return(home_page)
