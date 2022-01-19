from flask import request
from flask_restx import Api, Resource
from app.db import Resolution


api = Api(
    prefix="/api",
    doc="/api/doc/",
    title="Resolution API",
    description="API for managing your resolution"
)


class ResolutionAPI(Resource):
    """represents resolution API"""

    def get(self) -> dict:
        """represents response of GET method"""

        resolutions = Resolution.query.all()
        resolutions = [resolution.jsonify() for resolution in resolutions]

        return {"status": True, "data": resolutions}, 200

    def post(self) -> dict:
        """represents response of POST method"""

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

    def get(self, id: int) -> dict:
        """represents response of GET method"""

        resolution = Resolution.query.get(id)

        if resolution is None:
            # can't find resolution row with given id
            return {
                "status": False,
                "message": "can't find resolution with the given id"
            }, 404

        return {"status": True, "data": resolution.jsonify()}, 200

    def delete(self, id: int) -> dict:
        """represents response of DELETE method"""

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
