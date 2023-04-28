import requests
from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort


blp = Blueprint("Users", "users", description="Retrieve information about users")


@blp.route("/user/<string:user_id>")
class UserName(MethodView):
    @blp.response(200, description="Success")
    @blp.doc(description="Retrieves user information based on the provided user ID", summary="Retrieve User Information")
    def get(self, user_id):
        """
        Retrieve user information by user ID.

        This endpoint retrieves detailed information about a user based on the provided user ID.

        Parameters:
        - user_id (str): The unique identifier of the user.

        Returns:
        - user_data (dict): The user information in JSON format.

        Raises:
        - 400: If there is an error retrieving the user data.

        """
        response = requests.get(f"https://torre.bio/api/bios/{user_id}")

        if response.status_code == 200:
            response_data = response.json()
            return jsonify(response_data), 200

        abort(400, message="Error retrieving user data")

@blp.route("/user/<string:user_id>/skill/<string:skill_id>/")
class UserExperience(MethodView):
    @blp.response(200, description="Success")
    @blp.doc(description="Retrieve details of a user regarding a specific skill.",
             summary="Get user skill details")
    def get(self, user_id, skill_id):
        """
        Retrieve details of a user regarding a specific skill.

        This endpoint retrieves details of a user regarding a specific skill based on the provided user ID and skill ID.

        Parameters:
        - user_id (str): The ID of the user.
        - skill_id (str): The ID of the skill.

        Returns:
        - user_skill_details : The user skill details in JSON format.

        Raises:
        - 400: If there is an error retrieving the user skill details.
        """
        response = requests.get(f"https://torre.co/api/genome/bios/{user_id}/strengths-skills/{skill_id}/detail")

        if response.status_code == 200:
            response_data = response.json()
            return jsonify(response_data), 200

        abort(400, message="Error retrieving user experiences")

@blp.route("/search/users/skill/<string:skill_name>/proficiency/<string:proficiency>")
class UsersSkill(MethodView):
    @blp.response(200, description="Success")
    @blp.doc(description="Search users based on skill and proficiency.",
            summary="Search users by skill and proficiency")
    def get(self, skill_name, proficiency):
        """
        Search users based on skill and proficiency.

        This endpoint searches for users who have the same proficiency in a specific skill based on the provided skill name and proficiency level.

        Parameters:
        - skill_name (str): The name of the skill.
        - proficiency (str): The proficiency level of the skill.

        Returns:
        - matching_users : The list of matching users in JSON format.

        Raises:
        - 400: If there is an error retrieving users with the same skill and proficiency.
        """
        request_body = {
            "and": [
                { "skill/role": { "text": f"{skill_name}", "proficiency": f"{proficiency}" } }
            ]
        }

        headers = {
            "User-Agent": "Proxy-Server"
        }

        response = requests.post("https://search.torre.co/people/_search", json=request_body, headers=headers)
        
        if response.status_code == 200:
            response_data = response.json()
            return jsonify(response_data), 200
        
        abort(400, message="Error retrieving users with same skill")