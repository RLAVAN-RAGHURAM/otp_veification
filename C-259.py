from etherpad_lite import EtherpadLiteClient

ether_client=EtherpadLiteClient(base_params={'api_key':'5ff7ea9032814c34a8f8daf05038aa9d48d29052678ca34eb40c69a981b118f9'})

group=ether_client.createGroup()
print("Your Group is",group)

new_pad=ether_client.createPad(padID="WhiteHat",text="Hello everyone")
print("Your New Pad",new_pad)


