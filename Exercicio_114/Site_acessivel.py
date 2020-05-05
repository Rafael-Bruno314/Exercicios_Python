import urllib
import urllib.request

try:
  site = urllib.request.urlopen('https://www.php.net/')
except urllib.error.URLError:
  print('O site não está acessível no momento.')
else:
  print('Consegui acessar o site com sucesso!')
