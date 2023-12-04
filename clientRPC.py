from rpc import client

client_rpc = client.Client('127.0.0.1',8888)

# print(client_rpc.subtract((10,10)))
client_rpc.divide((10,10))
client_rpc.multiply((10,10))
client_rpc.multiply((20,10))
client_rpc.is_prime(10,100000,1)
client_rpc.is_prime(10,100,1)
client_rpc.is_prime(10,12345,1)

# prime_numbers = [number for number, is_prime in zip(list_numbers, is_prime_list) if is_prime]
#print(f'Numeros primos {is_prime_list} total = {len(is_prime_list)}')



# prime_numbers = [number for number, is_prime in zip(list_numbers, is_prime_list) if is_prime]
#print(f'Numeros primos cache{is_prime_list} total = {len(is_prime_list)}')

# is_prime_list_mp = client.mp_is_prime(list_numbers)
# prime_numbers_mp = list(filter(lambda x: x[1], zip(list_numbers, is_prime_list_mp)))
# print(f'Numeros primos MP{[number for number,_ in prime_numbers_mp]} total = {len(prime_numbers_mp)}')

# print(client.subtract((10,5,2)))
# print(client.sum((10,20,10)))
# print(client.divide((10,2,2)))
# print(client.multiply((10,2,2)))
# print('chegou')