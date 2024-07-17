import re

print('''A senha deve conter no minimo 8 digitos.
      Pelo menos uma letra maiuscula.
      Pelo menos uma letra minuscula.
      Pelo menos um digito.
      Pelo menos um caractere especial.
''')

def validar_senha(senha):
    comprimento_minimo = 8
    tem_maiuscula = re.search(r'[A-Z]', senha)
    tem_minusculo = re.search(r'[a-z]', senha)
    tem_digito = re.search(r'[0-9]', senha)
    tem_caractere_especial = re.search(r'[\W_]', senha)

    if len(senha) < comprimento_minimo:
        return "A senha deve ter pelo menos 8 caracteres."

    if not tem_maiuscula:
        return "A senha deve conter pelo menos uma letra maiuscula."

    if not tem_minusculo:
        return "A senha deve conter pelo menos uma letra minuscula."

    if not tem_digito:
        return "A senha deve conter pelo menos um digito."

    if not tem_caractere_especial:
        return ("A senha deve conter pelo menos um caractere especial.")

    return ("A senha é valida.")


senha = input("Digite a senha para validar: ")
valida, mensagem = validar_senha(senha)
print(mensagem)