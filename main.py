import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/",methods=['GET'])
def hello_world():
    value = request.args.get('value')
    
    TimeComplexityDict = {
        "array":{
            "access":"O(1)",
            "search":"O(N)",
            "insertion":"O(N)",
            "deletion":"O(N)"
        },
        "stack":{
            "access":"O(N)",
            "search":"O(N)",
            "insertion":"O(1)",
            "deletion":"O(1)"
        },
        "queue":{
            "access":"O(N)",
            "search":"O(N)",
            "insertion":"O(1)",
            "deletion":"O(1)"
        },
        "single linked list":{
            "access":"O(N)",
            "search":"O(N)",
            "insertion":"O(1)",
            "deletion":"O(1)"
        },
        "double linked list":{
            "access":"O(N)",
            "search":"O(N)",
            "insertion":"O(1)",
            "deletion":"O(1)"
        },
        "hash map":{
            "access":"O(N)",
            "search":"O(N)",
            "insertion":"O(N)",
            "deletion":"O(N)"
        },
        "BST":{
            "access":"O(N)",
            "search":"O(N)",
            "insertion":"O(N)",
            "deletion":"O(N)"
        },
        "Binary Tree":{
            "access":"O(N)",
            "search":"O(N)",
            "insertion":"O(N)",
            "deletion":"O(N)"
        }
    }
    if( value not in TimeComplexityDict.keys()):
        return "Record not found", 400
    
    return TimeComplexityDict[value],200
    


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))