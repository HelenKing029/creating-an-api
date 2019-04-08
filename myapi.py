from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

#This method is used since this article is focusing in creating API,
#but in actual condition, the data store is usually a database.
users = [
    {
        "name": "Helen",
        "age": 34,
        "occupation": "Customer Support"
    },
    {
        "name": "Sarah",
        "age": 32,
        "occupation": "Marketing"
    },
    {
        "name": "Ian",
        "age": 60,
        "occupation": "Manager"
    }
]

courses = [
    {
        "name": "Python",
        "level": 2,
    },
    {
        "name": "JavaScript",
        "level": 1,
    },
    {
        "name": "Java",
        "level": 4,
    },
    {
        "name": "Django",
        "level": 3,
    }
]

#creating our 4 HTTP request methods
class User(Resource):

    def get(self, name):
        for user in users:
            if (name == user["name"]):
                return user, 200
        return "User Not Found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if (name == user["name"]):
                return "User with name {} already exists.".format(name), 400

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def put (self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if (name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200

class User(Resource):

    def get(self, name):
        for course in courses:
            if (name == course["name"]):
                return course, 200
        return "Course Not Found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("level")
        args = parser.parse_args()

        # for course in courses:
        #     if (name == course["name"]):
        #         return "The course with name {} already exists.".format(name), 400

        course = {
            "name": name,
            "level": args["level"],
        }
        courses.append(course)
        return course, 201

    def put (self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("level")
        args = parser.parse_args()

        for course in courses:
            if (name == course["name"]):
                course["level"] = args["level"]
                return course, 200

        course = {
            "name": name,
            "level": args["level"],
        }
        courses.append(course)
        return course, 201

    def delete(self, name):
        global courses
        courses = [course for course in courses if course["name"] != name]
        return "{} is deleted.".format(name), 200

api.add_resource( User, "/user/<string:name>")
api.add_resource( Course, "/Course/<string:name>")

app.run(debug=True)
