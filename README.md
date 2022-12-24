# Criando um Sistema Bancário com Python
## Desafio de projeto para iniciantes em desenvolvimento com python da DIO
Link do desafio clicando [aqui](https://web.dio.me/lab/desafio-de-projeto-criando-um-sistema-bancario/learning/e71686b9-439b-44c1-83c1-f45da47dc634)

### Objetivos Gerais
Criar um sistema simples onde é possível depositar, sacar e ver o extrato de uma conta bancária
### Depósito
Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato
### Saque 
O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.
### Extrato 
Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
1500.45 = R$ 1500.45
