import os

import flask
import flask_restful
from flask import (request,
                   jsonify,
                   render_template,
                   Flask,
                   request,
                   url_for,
                   flash,
                   redirect)
import json
from pylti.flask import lti

app = flask.Flask(__name__)
api = flask_restful.Api(app)

app.config.update(
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "CHANGEME"),
    PYLTI_CONFIG = {
        "consumers": {
            os.environ.get("CONSUMER_KEY", "CHANGEME"):{
                "secret" : os.environ.get("LTI_SECRET", "CHANGEME"),
            }
        }
    }
)

class HelloWorld(flask_restful.Resource):
    def error(exception=None):
        """render error page"""
        exvar = str(exception)
        return jsonify({"error": exvar})

    def get(self):
        return {'hello': 'world'}

    # Purpose of this function is to return the post request from the lms
    @app.route('/heyo/', methods = ['GET', 'POST', 'DELETE'])
    @lti(request="initial", error=error, app=app)
    def parrot(lti=lti):
        if request.method == 'POST':
            """modify/update the information for <user_id>"""
            # you can use <user_id>, which is a str but could
            # changed to be int or whatever you want, along
            # with your lxml knowledge to make the required
            # changes
            d = request.form.to_dict()
            return jsonify(d)

    # Opens up the submission box
    @app.route('/submission/', methods=['GET', 'POST', 'DELETE'])
    @lti(request="initial", error=error, app=app)
    def submission_box(lti=lti):
        d = request.form.to_dict()
        return jsonify(d)
        return render_template("submission_box.html")

    # Opens up the submission box
    @app.route('/grade/', methods=['GET', 'POST', 'DELETE'])
    def grade_post():
        if request.method == 'POST':
            d = {
                "grade 1" : 97,
                "grade 2": 96,
            }
            return jsonify(d)

        return render_template("grade_post.html")

    # collects the submission and reopens the submission box
    @app.route('/submit/', methods=['GET', 'POST', 'DELETE'])
    def submit():
        # d = request.form.to_dict()
        # return jsonify(d)
        if request.method == 'POST':
            content = request.form['content']

            if not content:
                flash('Content is required!')
            else:
                print("got it")
                f = open("C:\\Users\\sense\\Downloads\\demofile4.txt", "a")
                f.write(content)
                f.close()
        return "success"


api.add_resource(HelloWorld, '/')

if __name__ == "__main__":
    app.run(debug=True)


submisison_req = {
  "context_id": "140945f93bb882482cb426260e2348992dc7f968",
  "context_label": "Testing",
  "context_title": "Testing Enviroment",
  "custom_canvas_api_domain": "canvas.instructure.com",
  "custom_canvas_assignment_id": "32098868",
  "custom_canvas_assignment_points_possible": "67",
  "custom_canvas_assignment_title": "lets see",
  "custom_canvas_course_id": "5195818",
  "custom_canvas_enrollment_state": "active",
  "custom_canvas_module_id": "",
  "custom_canvas_module_item_id": "71284470",
  "custom_canvas_user_id": "35382883",
  "custom_canvas_user_login_id": "108676458294816858207",
  "custom_canvas_workflow_state": "available",
  "ext_ims_lis_basic_outcome_url": "https://canvas.instructure.com/api/lti/v1/tools/610450/ext_grade_passback",
  "ext_lti_assignment_id": "21a15157-eb6e-4f4d-8d1e-ca73a28cbb79",
  "ext_outcome_data_values_accepted": "url,text",
  "ext_outcome_result_total_score_accepted": "true",
  "ext_outcome_submission_needs_additional_review_accepted": "true",
  "ext_outcome_submission_prioritize_non_tool_grade_accepted": "true",
  "ext_outcome_submission_submitted_at_accepted": "true",
  "ext_outcomes_tool_placement_url": "https://canvas.instructure.com/api/lti/v1/turnitin/outcomes_placement/610450",
  "ext_roles": "urn:lti:instrole:ims/lis/Instructor,urn:lti:instrole:ims/lis/Student,urn:lti:role:ims/lis/ContentDeveloper,urn:lti:role:ims/lis/Instructor,urn:lti:role:ims/lis/Learner,urn:lti:sysrole:ims/lis/User",
  "launch_presentation_document_target": "iframe",
  "launch_presentation_locale": "en",
  "launch_presentation_return_url": "https://canvas.instructure.com/courses/5195818/external_content/success/external_tool_redirect",
  "lis_outcome_service_url": "https://canvas.instructure.com/api/lti/v1/tools/610450/grade_passback",
  "lis_person_contact_email_primary": "rafi@sense.network",
  "lis_person_name_family": "",
  "lis_person_name_full": "108676458294816858207",
  "lis_person_name_given": "108676458294816858207",
  "lis_result_sourcedid": "610450-5195818-32098868-35382883-88c24725962e1673b5cc5b12e5261f36e702e92e",
  "lti_message_type": "basic-lti-launch-request",
  "lti_version": "LTI-1p0",
  "oauth_callback": "about:blank",
  "oauth_consumer_key": "CHANGEME",
  "oauth_nonce": "Iea8KAuPCrmDZZLYVMTcFsVpxsVr8yiEVM3TT9Bkq4",
  "oauth_signature": "CP7QOb+7Ic8z61Sp/XheqvixiZs=",
  "oauth_signature_method": "HMAC-SHA1",
  "oauth_timestamp": "1662028938",
  "oauth_version": "1.0",
  "resource_link_id": "9708fcad1b6546e6ddbb5c6c7ca2f8aa9df24a24",
  "resource_link_title": "lets see",
  "roles": "Learner,Instructor,ContentDeveloper",
  "tool_consumer_info_product_family_code": "canvas",
  "tool_consumer_info_version": "cloud",
  "tool_consumer_instance_contact_email": "notifications@instructure.com",
  "tool_consumer_instance_guid": "07adb3e60637ff02d9ea11c7c74f1ca921699bd7.canvas.instructure.com",
  "tool_consumer_instance_name": "Free For Teacher",
  "user_id": "ee540bc06b5fe0ec6b19085b1de76062589a339f",
  "user_image": "https://canvas.instructure.com/images/messages/avatar-50.png"
}