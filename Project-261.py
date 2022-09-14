import requests 

equation=input("Enter The Equation : ")
result='https://newton.now.sh/api/v2//simplify/'+equation
data=requests.get(result).json()
print('Operation for giving equation : ',data['operation'])
print("Expression for given equation : ",data['expression'])
print("Result of given equation : ",data['result'])