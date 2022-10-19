from flask import request, session
from pylti1p3.flask_adapter import (FlaskRequest, FlaskOIDCLogin)

from pylti1p3.tool_config import ToolConfJsonFile
tool_conf = ToolConfJsonFile('path/to/json')

from pylti1p3.tool_config import ToolConfDict
settings = {
    "<issuer_1>": { },  # one issuer ~ one client-id (outdated and not recommended)
    "<issuer_2>": [{ }, { }]  # one issuer ~ many client-ids (recommended method)
}
private_key = '...'
public_key = '...'
tool_conf = ToolConfDict(settings)

client_id = '...' # must be set if implementing the "one issuer ~ many client-ids" concept

tool_conf.set_private_key(iss, private_key, client_id=client_id)
tool_conf.set_public_key(iss, public_key, client_id=client_id)


def login(request_params_dict):
    tool_conf = ...  # See Configuration chapter above

    # FlaskRequest by default use flask.request and flask.session
    # so in this case you may define request object without any arguments:

    request = FlaskRequest()

    # in case of using different request object (for example webargs or something like this)
    # you may pass your own values:

    request = FlaskRequest(
        cookies=request.cookies,
        session=session,
        request_data=request_params_dict,
        request_is_secure=request.is_secure
    )

    oidc_login = FlaskOIDCLogin(
        request=request,
        tool_config=tool_conf,
        session_service=FlaskSessionService(request),
        cookie_service=FlaskCookieService(request)
    )

    return oidc_login.redirect(request.get_param('target_link_uri'))
