import asyncio
import aiocoap as coap
from os import urandom


async def main():
	context = await coap.Context.create_client_context()

	msg_type = -1
	while msg_type == -1:
		type_in = input("Select if the messages will be confirmable or non confirmable\n0 - Confirmable\n1 - Non Confirmable\n")
		if type_in.isdigit() and 0 <= int(type_in) <= 1:
			msg_type = None if int(type_in) == 0 else coap.NON
		else:
			print("Invalid type")

	while True:
		bytes_in = input("Insert the number of bytes to send\n")

		if bytes_in.isdigit():
			bytes_to_send = int(bytes_in)
			if bytes_to_send > 0:
				print(f"Sending {bytes_to_send} random bytes")
				request = coap.Message(code=coap.POST, payload=urandom(bytes_to_send), uri="coap://localhost/testing/things", mtype=msg_type)
			elif bytes_to_send == 0:
				print("Sending empty message")
				request = coap.Message(code=coap.POST, payload=b"", uri="coap://localhost/testing/things", mtype=msg_type)
			else:
				break

			response = await context.request(request).response
			print(f"Response code: {response.code}, payload: {response.payload}")
		else:
			print("Invalid number")


if __name__ == "__main__":
	asyncio.get_event_loop().run_until_complete(main())