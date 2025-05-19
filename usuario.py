class Usuario:
  def __init__(self, nome, cpf, email, senha, funcao):
    self._nome = nome
    self._cpf = cpf
    self._email = email
    self._senha = senha
    self._funcao = funcao # Atendente / Administrador
    
  @property
  def nome(self):
    return self._nome

  @nome.setter
  def nome(self, novo_nome):
    self._nome = novo_nome
  
  @property
  def cpf(self):
    return self._cpf
  
  @cpf.setter
  def cpf(self, novo_cpf):
    self._cpf = novo_cpf
  
  @property
  def email(self):
    return self._email
  
  @email.setter
  def email(self, novo_email):
    self._email = novo_email
  
  @property
  def senha(self):
    return self._senha

  @senha.setter
  def senha(self, nova_senha):
    self._senha = nova_senha
  
  @property
  def funcao(self):
    return self._funcao
  
  @funcao.setter
  def funcao(self, nova_funcao):
    self._funcao = nova_funcao
  
  def ver_dados(self):
    print('\n----- Dados do usuário -----')
    print(f'\nNome: {self._nome} \nCPF: {self._cpf} \nE-mail: {self._email} \nFunção: {self._funcao}')
    
      






