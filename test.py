import os
import requests
from requests_oauthlib import OAuth1


SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "CHANGEME")
imsx = """
      <?xml version = "1.0" encoding = "UTF-8"?>
      <imsx_POXEnvelopeRequest xmlns = "http://www.imsglobal.org/services/ltiv1p1/xsd/imsoms_v1p0">
        <imsx_POXHeader>
          <imsx_POXRequestHeaderInfo>
            <imsx_version>V1.0</imsx_version>
            <imsx_messageIdentifier>999999123</imsx_messageIdentifier>
          </imsx_POXRequestHeaderInfo>
        </imsx_POXHeader>
        <imsx_POXBody>
          <readResultRequest>
            <resultRecord>
              <sourcedGUID>
                <sourcedId>610450-5195818-32098868-35382908-9f20e1be682b7f54e16adb354a4d94fff56666df</sourcedId>
              </sourcedGUID>
            </resultRecord>
          </readResultRequest>
        </imsx_POXBody>
      </imsx_POXEnvelopeRequest>
"""
key = "CHANGEME"
oauth_body = OAuth1(client_key=key,  signature_type='auth_header', client_secret=imsx, force_include_body=True)


# headers = {
#     "Content-Length": str(len(imsx)),
#     "oauth_version":"1.0",
#     "oauth_consumer_key":"CHANGEME",
#     "oauth_signature_method":"HMAC-SHA1",
#     "oauth_signature":"YOa3r8INZOlyq1ifZkz9ZbN9cwk%3D",
#     "Content-type": "application/xml"
# }


response = requests.post(
    "https://canvas.instructure.com/api/lti/v1/tools/610450/ext_grade_passback",
   data=imsx, auth=oauth_body)

check = response.content
rafi = 10

