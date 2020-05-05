import smtplib

remetente = "jonhyuio@gmail.com"
#destinatário = "rafaelbruno.cunha@gmail.com"
destinatário = input("Digite o email do destinatário: ")

mensagem = """From: {}
To: {}
Subject: Mensagem

  Att. Rafael Bruno
  """.format(remetente, destinatário)

try:
  senha = input("Digite a senha do gmail: ")
  smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
  smtpObj.starttls()
  smtpObj.login(remetente, senha)
  print("Login success")
  smtpObj.sendmail(remetente, destinatário, mensagem.encode("utf8"))
  print("Email enviado com sucesso")
except Exception:
  print("Erro ao enviar")
