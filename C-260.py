from etherpad_lite import EtherpadLiteClient
from datetime import datetime

ether_client=EtherpadLiteClient(base_params={'api_key':'5ff7ea9032814c34a8f8daf05038aa9d48d29052678ca34eb40c69a981b118f9'})

new_pad=ether_client.createPad(padID='myNewPad11111',text="Hello everyone")
print("Your New Pad",new_pad)

author=ether_client.createAuthor(name='cloudUser')
print("The Pad Author : ",author)

padcounts=ether_client.padUsersCount(padID='myNewPad11111')
print("Number Of Users : ",padcounts)

timestamp=ether_client.getLastEdited(padID='myNewPad11111')
print("the timestamp in milliseconds : ",timestamp)
lastedit=timestamp['lastEdited']

conversion=datetime.fromtimestamp(lastedit/1000.0)
print("Date Time : ",conversion)

deletepad=ether_client.deletePad(padID='myNewPad11111')
print("Defined Ether Pad Deleted : ",deletepad)