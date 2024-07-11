from intasend import APIService

API_PUBLISHABLE_KEY = 'ISPubKey_test_598089fc-3570-46bc-976f-b89f6190279a'
API_TOKEN = 'ISSecretKey_test_238910f7-7fd8-4f58-aa69-4cd68ae00d36'

service = APIService(token=API_TOKEN, publishable_key=API_PUBLISHABLE_KEY, test=True)



create_order_response = service.collect.mpesa_stk_push(phone_number=+254746106100, email="Danlewimuriuki@gmail.com",
                                                       amount=200, narrative='Purchase of goods')

print(create_order_response)