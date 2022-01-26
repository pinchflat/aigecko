# Image Service Task

## Design/Plan

1. API contracts and between Frontend and Backend. Decided to post image data as request body instead of multipart-forms to provide better REST API compability. (URL based upload is missing at the solution.)
2. Tech stack chosen for frontend is Angular to have multiple projects, familarty, popularity.  
3. Decided to create multiple project so in future different teams can work indepentently after aggreing on common api scheme and endpoints. In future mocked backend can be introduced in frontend which will allow to seperate teams and reduce bottlenecks. Backend team can provide mocked service responses before implementation. 
4. Decided to build projects in docker (standalone builds are possible). Hence anyone with docker knowledge can build same projects without any guidence. (Missing: Geenrating python distribution package)
5. Decided not to generate test code due to time limitation.
6. Instead of serving generated frontend code by flask, decided to serve them via nginx. Backend is isolated by docker networks and accessible via nginx upstream and location configuration. In future this may be changed due to requirement changes. (Authorization, Authentication, etc.)
7. For backend and frontend MVC patterns are applied to provide better isolation.
8. Code should be self explanatory and comments are not preferred. 
   

## Build & Deploy

Project deployments can be done via docker-compose. Execute below command to build and execute the solution

``
docker-compose up --build
``

After execution application will be accessible at http://localhost. Port configuration can be changed in [docker-compose.yml](docker-compose.yml).

## Development Environment

### Backend
1. Install latest stable Python from official site.
2. Execute `pip install -r requirements.txt` in backend folder.
3. Execute `FLASK_APP=app.py flask run` in backend folder.
4. Use `http://localhost:5000` to access service.

### Frontend
1. Install latest stable NodeJs from official site.
2. Execute `npm install -g @angular/cli` to install latest angular.
3. Execute `npm install` in frontend folder.
4. In frontend folder, execute `ng serve --open` to start frontend in development mode.
5. UI will be visible on your default browser (port 4200)

_Backend service need to be up and running for frontend_

## API Endpoints

### Image Upload 

__Path__  : `/image_upload`

__Method__: `POST`

__Params__: `None`

__Body__  : Byte Array (Image data)

Receives image data, saves into local storage and returns image id.

#### Status Codes
| Code | Description |
| :--  | :--     |
| 201  | Image uploaded and created successfully |
| 400  | Image data is missing or uploaded file is not image |
| 500  | Internal server error |

For failures service will not return `id` field.
#### Response Format
```
{
    íd<String> : Image Identifier (UUID in hex format)
    message:<String>: Success or failure message
}
```

_Upload image by URL is missing, it can be done adding one query string and service can download that image by using that url. That feature is planned for last item but due to time limitation it will be implemented in next sprint_

### Analyse Image

__Path__  : `/analyse_image/<id>`

__Method__: `GET`

__Params__: `None`

#### Path Variables
| Variable | Type    | Description |
| :--      | :--     | :--         |
| id       | string  | Image identifier. (See Image Upload )  |

Receives image identifier, returns image dimensions.

#### Status Codes
| Code | Description |
| :--  | :--     |
| 200  | Successul request |
| 400  | Image does not exist for provided image id |
| 500  | Internal server error |

For failures service will return only `message` field.

#### Response Format
```
{
    íd<String> : Image Identifier (UUID in hex format)
    width<int> : Image width in pixels.
    height<int> : Image height in pixels.
    message<String>: Failure message 
}
```

### List Images

__Path__  : ` /list_images`

__Method__: `GET`

__Params__: `None`

Returns array of stored images identifiers.

#### Status Codes
| Code | Description |
| :--  | :--     |
| 200  | Successul request |
| 500  | Internal server error |

#### Response Format
```
Array of Image Identifier
```
