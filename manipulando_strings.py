curso = "pytHon"

print(curso.lower())

print(curso.upper())

print(curso.title())

print(curso.center(10, "-"))

print("*".join(curso))

texto = "    Olá mundo! "

print(texto + ".")
print(texto.strip() + ".")
print(texto.lstrip() + ".")
print(texto.rstrip() + ".")

nome = "Everson"
idade = 44
profissao = "Analista"
linguagem = "Python"

pessoa = {"nome": "Everson", "idade": 44, "profissao": "Analista", "linguagem": "Python"}

print("Olá, me chamo {0}. Eu tenho {1} anos de idade, trabalho como {2} e estou matriculado no curso de {3}.".format(nome, idade, profissao, linguagem))

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(**pessoa))

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

name = "Everson Okuhara"

print(name[0])
print(name[-7])
print(name[6])
print(name[3:14])

nome2 = "Everson"

mensagem = f"""
    Olá, meu nome é {nome2}
        e estou aprendendo Python.
até mais!
"""
print(mensagem)