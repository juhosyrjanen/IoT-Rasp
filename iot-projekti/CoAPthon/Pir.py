from coapthon.resources.resource import Resource


class Pir(Resource):
	def __init__(self, name="Pir_lukema", obs=True):
		super(Pir, self).__init__(name, visible=True, observable=True, allow_children=True)
		self.payload = "PIR_LUKEMA"

	def render_GET(self, request):
		file = open('lukema.txt','r')
		self.payload = file.read()		
		return self

	def render_PUT(self, request):
		self.payload = request.payload
		return payload

	def render_POST(self, request):
		res = BasicResource()
		res.location_query = request.query
		res.payload = request.payload
		return res

	def render_DELETE(self, request):
		return True
