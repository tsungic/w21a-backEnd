from flask import Flask, request, Response
import dbcreds
import mariadb
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/posts', methods =['GET', 'POST', 'PATCH', 'DELETE'])
def posts():
    if request.method =='POST':
        post = request.json
        print(post)
        conn = mariadb.connect(
            host=dbcreds.host,
            port=dbcreds.port,
            user=dbcreds.user,
            password=dbcreds.password,
            database=dbcreds.database
        )
        cursor = conn.cursor()

        cursor.execute("INSERT INTO posts (content) VALUES (?)", [post.get("content")])
        conn.commit()

        success = cursor.rowcount

        if cursor !=None:
            cursor.close()
        if conn !=None:
            conn.close
            if(success):
                return Response(
                    "The post was added",
                    mimetype="application/json",
                    status=200
                )
            return Response(
                "failed",
                mimetype=""
                
            )
    
    elif request.method =='GET':

        conn = mariadb.connect(
            host=dbcreds.host,
            port=dbcreds.port,
            user=dbcreds.user,
            password=dbcreds.password,
            database=dbcreds.database
        )
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM posts")
        results = cursor.fetchall()
        posts=[]
        for item in results:
            post={ "id" : item[0] , "contents" : item[1]}
            posts.append(post)
        return Response(json.dumps(posts, default = str), mimetype ="application/json", status = 200)

        conn = None
        cursor = None
        
    
    elif request.method == 'PATCH':
        post = request.json
        print(post)
        conn = mariadb.connect(
            host=dbcreds.host,
            port=dbcreds.port,
            user=dbcreds.user,
            password=dbcreds.password,
            database=dbcreds.database
        )
        cursor = conn.cursor()

        cursor.execute("UPDATE posts SET content=? WHERE id = ?", [post.get("id"), post.get("content")])
        conn.commit()

        success = cursor.rowcount

        if cursor !=None:
            cursor.close()
        if conn !=None:
            conn.close
            if(success):
                return Response(
                    "The post was updated",
                    mimetype="application/json",
                    status=200
                )
            return Response(
                "failed",
                mimetype=""
                
            )
    
    
    elif request.method == 'DELETE':
        post = request.json
        print(post)
        conn = mariadb.connect(
            host=dbcreds.host,
            port=dbcreds.port,
            user=dbcreds.user,
            password=dbcreds.password,
            database=dbcreds.database
        )
        cursor = conn.cursor()

        cursor.execute("DELETE from posts WHERE id = ?", [post.get("id")])
        conn.commit()

        success = cursor.rowcount

        if cursor !=None:
            cursor.close()
        if conn !=None:
            conn.close
            if(success):
                return Response(
                    "The post was deleted",
                    mimetype="application/json",
                    status=200
                )
            return Response(
                "failed",
                mimetype=""
                
            )
    


