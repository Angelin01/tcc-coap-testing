import asyncio
import aiocoap as coap
import aiocoap.resource as resource


class SimpleResource(resource.Resource):
	def __init__(self):
		super().__init__()
		self._content = b""

	async def render_post(self, request):
		self._content = request.payload
		return coap.Message(code=coap.CHANGED)

	async def render_get(self, request):
		return coap.Message(payload=self._content)


def main():
	root = resource.Site()

	root.add_resource((".well-known", "core"),
                      resource.WKCResource(root.get_resources_as_linkheader))
	root.add_resource(("testing", "things"), SimpleResource())

	asyncio.Task(coap.Context.create_server_context(root))
	asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
	main()
