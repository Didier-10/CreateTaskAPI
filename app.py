from flask import Flask
from models.create_task_models import CreateTaskModel
from flask_swagger_ui import get_swaggerui_blueprint
from services.create_task_services import CreateTaskService
from routes.create_task_routes import CreateTaskRoutes
from schemas.create_task_schemas import CreateTaskSchema
from flask_cors import CORS

app = Flask(__name__)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Access API'
    }
)

app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

db_connector = CreateTaskModel()
db_connector.connect_to_database()

task_service = CreateTaskService(db_connector)
task_schema = CreateTaskSchema()

task_blueprint = CreateTaskRoutes(task_service, task_schema)
app.register_blueprint(task_blueprint)

CORS(app, resources={r'/api/tasks': {'origins': 'http://localhost:3000'}})

if __name__ == '__main__':
    try:
        app.run(debug=True)
    finally:
        db_connector.close_connection()