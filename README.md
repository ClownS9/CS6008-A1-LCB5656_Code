# CS6008 A1-LCB5656_CODE

A 2D Platformer Multiplayer (Tales of Unfaced) game project by Dean Boon Joon Meng (LCB5656). This repository indicates the server and the client code of the game as the server will be on python and client will be on Godot Engine.

The server will be running on FastAPI websocket and MySQL database, so the server will send response to the client and the client will send a request to the server.

## Create database config file

Create a new file called .env in server folder then add this inside .env file

```bash
# Database Credentials
DB_USER=root
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=3306
DB_NAME=your_db_name
```

## Executing __main__.py

```bash
python -m app
```

