# Web server application to serve ML code in it

## Structure and recommendations

- [main.py](main.py) - Main entrypoint for application, where `app` object is created
- [settings.py](settings.py) - Main application settings definition
- [constants.py](constants.py) - Application constants
- [models](models) - Definition of models (pydantic based) for in/out structures of requests
- [routes](routes) - Routing definition, grouping endpoints
  - Here versioning is added, for real production versioning probably you need to version models, services and other parts
- [services](services) - Main logic/functions code
  - Try to store logic definition here, don`t import your modules in other directories
- [worker](worker) - Celery gateway/worker definition
