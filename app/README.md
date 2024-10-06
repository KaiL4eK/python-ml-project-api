# Web server application to serve ML code in it

## Structure and recommendations

- [main.py](main.py) - Main entrypoint for application, where `app` object is created
- [core/settings.py](core/settings.py) - Main application settings definition
- [core/constants.py](core/constants.py) - Application constants
- [models](models) - Definition of models (pydantic based) for in/out structures of requests
- [routes](routes) - Routing definition, grouping endpoints
  - Here versioning is added, for real production versioning probably you need to version models, services and other parts
- [services](services) - Main logic/functions code
  - Try to store logic definition here, don`t import your modules in other directories
- [celery](celery) - Celery gateway/worker definition

## Some recomendations

- Code in `models` and `core` has to contain minimum dependencies
- `routes` depends on `services`, `worker`, `models`, `core`
  - E.g. don't import code from `routes` into `services` or `models`
