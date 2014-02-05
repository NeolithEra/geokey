from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

import json

from opencomap.apps.backend import authorization
from opencomap.libs.serializers import ObjectSerializer
from opencomap.libs.decorators.http import handle_http_errors, handle_malformed
from opencomap.libs.views import render_to_json, render_to_success

@login_required
@require_http_methods(["PUT"])
@handle_http_errors
@handle_malformed
def update(request, project_id, featuretype_id):
	featuretype = authorization.featuretypes.update(request.user, project_id, featuretype_id, json.loads(request.body))
	return render_to_json("featuretype", ObjectSerializer().serialize(featuretype))

@login_required
@require_http_methods(["PUT"])
@handle_http_errors
@handle_malformed
def updateField(request, project_id, featuretype_id, field_id):
	field = authorization.featuretypes.updateField(request.user, project_id, featuretype_id, field_id, json.loads(request.body))
	return render_to_json("field", ObjectSerializer().serialize(field))

@login_required
@require_http_methods(["PUT"])
@handle_http_errors
@handle_malformed
def addLookupValue(request, project_id, featuretype_id, field_id):
	field = authorization.featuretypes.addLookupValue(request.user, project_id, featuretype_id, field_id, json.loads(request.body))
	return render_to_json("field", ObjectSerializer().serialize(field))

@login_required
@require_http_methods(["DELETE"])
@handle_http_errors
@handle_malformed
def removeLookupValue(request, project_id, featuretype_id, field_id, lookup_id):
	field = authorization.featuretypes.removeLookupValue(request.user, project_id, featuretype_id, field_id, lookup_id)
	return render_to_json("field", ObjectSerializer().serialize(field))