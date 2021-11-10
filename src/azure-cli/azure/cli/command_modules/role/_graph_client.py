# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import json

from azure.cli.core.util import send_raw_request
from azure.cli.core.auth.util import resource_to_scopes


class GraphClient:
    def __init__(self, cli_ctx):
        self.cli_ctx = cli_ctx
        self.scopes = resource_to_scopes(cli_ctx.cloud.endpoints.microsoft_graph_resource_id)

        # https://graph.microsoft.com/ (AzureCloud)
        self.resource = cli_ctx.cloud.endpoints.microsoft_graph_resource_id

        # https://graph.microsoft.com/v1.0
        self.base_url = cli_ctx.cloud.endpoints.microsoft_graph_resource_id + 'v1.0'

    def send(self, method, url, param=None, body=None):
        url = self.base_url + url

        if body:
            body = json.dumps(body)
        r = send_raw_request(self.cli_ctx, method, url, resource=self.resource, uri_parameters=param, body=body)
        if r.text:
            dic = r.json()
            if 'value' in dic:
                return dic['value']
            return r.json()
        else:
            return None
