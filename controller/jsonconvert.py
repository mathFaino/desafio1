import json


class JsonConvert:
    def fromJson(self, data):
        return json.loads(data)

    def toJson(self, data):
        return json.dumps(data)
