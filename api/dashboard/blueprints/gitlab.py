
import flask
import requests


ACCESS_TOKEN = 'Stg8ez5R4ozSrVEjgzxe'

blueprint = flask.Blueprint('gitlab', __name__)

PROJECTS_URL = 'https://gitlab.com/api/v4/projects?owned=true&private_token={}'.format(ACCESS_TOKEN)
PROJECTS_COMMITS= 'https://gitlab.com/api/v4/projects/12680315/repository/commits?private_token={}'.format(ACCESS_TOKEN)



@blueprint.route('/gitlab', methods=[ 'GET' ])
def get_gitlab():

    
    #projects = requests.get(PROJECTS_URL).json()
    context = {
        'page': 'gitlab',
        'projects': requests.get(PROJECTS_URL).json(),
        'commits': requests.get(PROJECTS_COMMITS).json()
        
    }



    return flask.render_template('gitlab.html', context=context)