import requests
import hashlib
import sys

def request_api_data(query_char):
  '''Faz o request e aguarda a resposta'''
  url = 'https://api.pwnedpasswords.com/range/' + query_char
  res = requests.get(url)
  if res.status_code != 200: 
    raise RuntimeError(f'ERRO: {res.status_code}, verifique a API!')
  return res

def get_password_leaks_count(hashes, hash_to_check):
  hashes = (line.split(':') for line in hashes.text.splitlines())
  for h, count in hashes:
    if h == hash_to_check:
      return count
  return 0

def pwned_api_check(password):
  '''Verificar se a senha existe na API'''
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper() 
  first5_char, tail = sha1password[:5], sha1password[5:]
  response = request_api_data(first5_char)
  return get_password_leaks_count(response, tail)

def main(args):
  '''Recebe os argumentos e printa no cmd'''
  for password in args:
    count = pwned_api_check(password)
    if count:
      print(f'{password} encontrada {count} vezes. voce provavelmente deveria trocar sua senha!')
    else:
      print(f'{password} nao encontrada. Esta segura!')
  return 'Pronto!'

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))
