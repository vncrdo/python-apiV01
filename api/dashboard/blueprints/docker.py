
import flask
import docker

blueprint = flask.Blueprint('docker', __name__)

connection = docker.DockerClient()

@blueprint.route('/docker', methods=[ 'GET' ])
def get_docker():

    context = {
        'page': 'docker',
        'containers' : connection.containers.list() 
    }

    return flask.render_template('docker.html', context=context)
