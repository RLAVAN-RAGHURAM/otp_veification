from etherpad_lite import EtherpadLiteClient

ether_client=EtherpadLiteClient(base_params={'api_key':''})

group=ether_client.createGroup()
print("Your Group is",group)

new_pad=ether_client.createPas(padID="BlackHat",text="Hello everyone")
print("Your New Pad",new_pad)


