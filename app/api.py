from flask import request
from flask_restx import Api, Resource, fields
from app.db import Resolution


api = Api(
    prefix="/api",
    doc="/api/doc/",
    title="Resolution API",
    description="API for managing your resolution"
)


@api.errorhandler(Exception)
def error_handler(error):
    """Exception error handler"""

    return {"status": False, "message": "fail to perform the action"}


# API user input and response
api_input = api.model("Resolution Input", {
    "resolution": fields.String(required=True),
    "percentage": fields.Integer,
    "description": fields.String
})
api_output = api.model("Resolution Output", {
    "id": fields.Integer,
    "resolution": fields.String,
    "percentage": fields.Integer,
    "description": fields.String
})
api_response_data = api.model("API response with data", {
    "status": fields.Boolean,
    "data": fields.Nested(api_output)
})
api_response_multiple_data = api.model("API response with multiple data", {
    "status": fields.Boolean,
    "data": fields.List(fields.Nested(api_output))
})
api_response_message = api.model("API response with message", {
    "status": fields.Boolean,
    "message": fields.String
})


class ResolutionAPI(Resource):
    """represents resolution API"""

    @api.response(200, "Success", api_response_multiple_data)
    def get(self) -> dict:
        """represents GET method"""

        resolutions = Resolution.query.all()
        resolutions = [resolution.jsonify() for resolution in resolutions]

        return {"status": True, "data": resolutions}, 200

    @api.expect(api_input)
    @api.response(200, "Success", api_response_message)
    @api.response(500, "Internal Server Error", api_response_message)
    def post(self) -> dict:
        """represents POST method"""

        # fetch user input
        user_input = request.get_json()
        resolution = user_input.get("resolution")
        percentage = user_input.get("percentage")
        description = user_input.get("description")

        # add new resolution
        new_resolution = Resolution(resolution, percentage, description)
        new_resolution.save()

        return {
            "status": True,
            "message": "successfully added new resolution"
        }, 200


class ResolutionAPIWithId(Resource):
    """represents resolution API with id required"""

    @api.doc(params={"id": "Resolution ID"})
    @api.response(200, "Success", api_response_data)
    @api.response(404, "Resolution Not Found", api_response_message)
    def get(self, id: int) -> dict:
        """represents GET method"""

        resolution = Resolution.query.get(id)

        if resolution is None:
            # can't find resolution row with given id
            return {
                "status": False,
                "message": "can't find resolution with the given id"
            }, 404

        return {"status": True, "data": resolution.jsonify()}, 200

    @api.doc(params={"id": "Resolution ID"})
    @api.response(200, "Success", api_response_message)
    @api.response(404, "Resolution Not Found", api_response_message)
    @api.response(500, "Internal Server Error", api_response_message)
    def delete(self, id: int) -> dict:
        """represents DELETE method"""

        resolution = Resolution.query.get(id)

        if resolution is None:
            # can't find resolution row with given id
            return {
                "status": False,
                "message": "can't find resolution with the given id"
            }, 404

        # remove resolution with the given id
        resolution.remove()

        return {
            "status": True,
            "message": "successfully deleted resolution"
        }, 200

    @api.doc(params={"id": "Resolution ID"})
    @api.expect(api_input)
    @api.response(200, "Success", api_response_message)
    @api.response(404, "Resolution Not Found", api_response_message)
    @api.response(500, "Internal Server Error", api_response_message)
    def put(self, id: int) -> dict:
        """represents PUT method"""

        resolution_obj = Resolution.query.get(id)

        if resolution_obj is None:
            # can't find resolution row with given id
            return {
                "status": False,
                "message": "can't find resolution with the given id"
            }, 404

        # fetch user input
        user_input = request.get_json()
        resolution = user_input.get("resolution")
        percentage = user_input.get("percentage")
        description = user_input.get("description")

        # update resolution
        resolution_obj.resolution = resolution
        resolution_obj.percentage = percentage
        resolution_obj.description = description
        resolution_obj.save()

        return {"status": True, "message": "successfully updated resolution"}
