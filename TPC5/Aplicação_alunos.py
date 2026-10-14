
import pickle


def criarTurma():
    return []


def inserirAluno(turma):
    nome = input("Nome do aluno: ")
    id = input("ID do aluno: ")

    notaTPC = float(input("Nota do TPC: "))
    notaProj = float(input("Nota do Projeto: "))
    notaTeste = float(input("Nota do Teste: "))

    aluno = (nome, id, [notaTPC, notaProj, notaTeste])
    turma.append(aluno)

    print("Aluno inserido com sucesso!")


def listarTurma(turma):
    for aluno in turma:
        print(aluno)


def consultarAluno(turma):
    id = input("ID do aluno a consultar: ")

    for aluno in turma:
        if aluno[1] == id:
            print(aluno)
            return

    print("Aluno não encontrado.")


def guardarTurma(turma):
    with open("turma.dat", "wb") as f:
        pickle.dump(turma, f)

    print("Turma guardada com sucesso!")


def carregarTurma():
    try:
        with open("turma.dat", "rb") as f:
            turma = pickle.load(f)
        print("Turma carregada com sucesso!")
        return turma
    except FileNotFoundError:
        print("O ficheiro não existe.")
        return []


def menu():
    print("\n--- GESTÃO DE ALUNOS ---")
    print("1: Criar uma turma")
    print("2: Inserir um aluno na turma")
    print("3: Listar a turma")
    print("4: Consultar um aluno por ID")
    print("8: Guardar a turma em ficheiro")
    print("9: Carregar uma turma dum ficheiro")
    print("0: Sair da aplicação")


def main():
    turma = []
    opcao = -1

    while opcao != 0:
        menu()
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            turma = criarTurma()
            print("Turma criada!")

        elif opcao == 2:
            inserirAluno(turma)

        elif opcao == 3:
            listarTurma(turma)

        elif opcao == 4:
            consultarAluno(turma)

        elif opcao == 8:
            guardarTurma(turma)

        elif opcao == 9:
            turma = carregarTurma()

        elif opcao == 0:
            print("A sair da aplicação...")

        else:
            print("Opção inválida.")


main()
