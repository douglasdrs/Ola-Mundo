# Para teste, vou criar um simples sistema de cadastro de usuários
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ") 
salario = input("Digite seu salário: ") 

arquivo = open("cadastro_usuarios.txt", "w")
arquivo.write(f"Nome: {nome}\nIdade: {idade}\nSalário: {salario}\n")
arquivo.close()

print("Nome:", nome, "\nIdade:", idade, "anos", "\nSalário: R$",salario,)
print("Cadastro realizado com sucesso!")
