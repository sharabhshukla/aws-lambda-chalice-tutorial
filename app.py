from chalice import Chalice, Response
from chalicelib.data_models import InputModel
from pydantic import ValidationError


app = Chalice(app_name='helloworld')
app.log.setLevel('INFO')


@app.route('/')
def index():
    app.log.info('This is from the root of the api')
    return {'hello': 'world'}

@app.route('/health')
def health_ping():
    return Response(body={'Status': 'OK'}, status_code=200)


@app.route('/user', methods=['POST'])
def city_fn():
    app.log.info('Entering the user function intiated fromuser endpoint')
    json_body = app.current_request.json_body
    try:
        validated_json = InputModel(**json_body)
        app.log.info('Successfully validated the json body')
        return Response(body=validated_json.json())
    except ValidationError as ve:
        app.log.info('Failed validation of the json body')
        return Response(body=str(ve), status_code=400)




# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
