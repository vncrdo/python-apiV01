import flask
import requests


ACCESS_TOKEN = 'Stg8ez5R4ozSrVEjgzxe'

blueprint = flask.Blueprint('PROJECTS', __name__)

PROJECTS_URL = 'https://gitlab.com/api/v4/projects?owned=true&private_token={}'.format(ACCESS_TOKEN)




@blueprint.route('/PROJECTS', methods=[ 'GET' ])
def get_gitlab():

    
    #projects = requests.get(PROJECTS_URL).json()
    context = {
        'page': 'PROJECTS',
        'projects': requests.get(PROJECTS_URL).json(),
    }

    return flask.render_template('projects.html', context=context)

@blueprint.route('/projects/<int:projectid>' , methods=[ 'GET' ])
def get_commits(projectid):

    PROJECTS_COMMITS= 'https://gitlab.com/api/v4/projects/' + str(projectid) + '/repository/commits?private_token={}'.format(ACCESS_TOKEN)
    context = {
        'page': 'commit',
        'commits': requests.get(PROJECTS_COMMITS).json(),
    }

    return flask.render_template('commits.html', context=context)