from datetime import datetime
from pydoc import cram

class Hospital():
  ''' Banco de dados de hospital, desenvolvido durante o curso de WebDev na Sirus Educação '''
  def __init__(self, nome, endereco):
    self.nome = nome
    self.endereco = endereco


class Funcionario(): 
  ''' Classe base dedica aos funcionário do hospital '''
  funcionarios = {}
  ''' Estrutura de dados que conterá todos os funcionários contratados pelo hospital'''
  def __init__ (self, nome, sobrenome, idade, matricula=0):
    self.nome = nome
    self.sobrenome = sobrenome
    self.idade = idade
    self.matricula = matricula

  @classmethod
  def contratar(cls, colaborador):
    ''' Esse método recebe as informações de um funcionário do setor administrativo e o vincula ao banco de funcionários desse setor. 
    Caso a matrícula não seja fornecida,gera um número de matrícula para esse funcionário. '''
    matricula_contratar = ""
    if colaborador.matricula == 0:
      if isinstance(colaborador, Enfermeiro) == True:
        matricula_contratar = str(len(Funcionario.funcionarios) + 1) + '-E'
        colaborador.matricula = matricula_contratar
      elif isinstance(colaborador, Medico) == True:
        matricula_contratar = str(len(Funcionario.funcionarios) + 1) + '-M'
        colaborador.matricula = matricula_contratar  
      else:
        matricula_contratar = str(len(Funcionario.funcionarios) + 1) + '-A'
        colaborador.matricula = matricula_contratar
      
      if isinstance(colaborador, Medico) == True:
        confirmacao = int(input(f"Confirma a inclusão de {colaborador.nome} {colaborador.sobrenome}, {colaborador.especialidade}, {colaborador.idade} anos, matricula {colaborador.matricula}, CRM nº {colaborador.crm} na base de dados como 'contratado(a)'? digite 1 para 'sim' e 2 para 'não': "))    
      else:
        confirmacao = int(input(f"Confirma a inclusão de {colaborador.nome} {colaborador.sobrenome}, {colaborador.idade} anos, matrícula {colaborador.matricula} na base de dados como 'contratado(a)'? digite 1 para 'sim' e 2 para 'não': "))
      
      if confirmacao == 1:
        Funcionario.funcionarios[f'{colaborador.nome} {colaborador.sobrenome}'] = colaborador
        print('Operação realizada com sucesso. Tenha um ótimo dia. Até breve!')
      elif confirmacao == 2:
        print(f'{colaborador.nome} {colaborador.sobrenome} não foi incluído(a) na base de dados. Tenha um ótimo dia. Até breve!')
      else: 
        print(f'Não compreendi a resposta. Caso queira inserir {colaborador.nome} {colaborador.sobrenome} no banco de dados, tente novamente desde o início.')
    
    else:
      if isinstance(colaborador, Enfermeiro) == True:
        colaborador.matricula = str(colaborador.matricula) + '-E'
      elif isinstance(colaborador, Medico) == True:
        colaborador.matricula = str(colaborador.matricula) + '-M'
      else:
        colaborador.matricula = str(colaborador.matricula) + '-A'
    
      if isinstance(colaborador, Medico) == True:
        confirmacao = int(input(f"Confirma a inclusão de {colaborador.nome} {colaborador.sobrenome}, {colaborador.especialidade}, {colaborador.idade} anos, matricula {colaborador.matricula}, CRM nº {colaborador.crm} na base de dados como 'contratado(a)'? digite 1 para 'sim' e 2 para 'não': "))    
      else:
        confirmacao = int(input(f"Confirma a inclusão de {colaborador.nome} {colaborador.sobrenome}, {colaborador.idade} anos, matrícula {colaborador.matricula} na base de dados como 'contratado(a)'? digite 1 para 'sim' e 2 para 'não': "))
    
      if confirmacao == 1:
        Funcionario.funcionarios[f'{colaborador.nome} {colaborador.sobrenome}'] = colaborador
        print('Operação realizada com sucesso. Tenha um ótimo dia. Até breve!')
      elif confirmacao == 2:
        print(f'{colaborador.nome} {colaborador.sobrenome} não foi incluído(a) no banco de dados. Tenha um ótimo dia. Até breve!')
      else: 
        print(f'Não compreendi a resposta. Caso queira inserir {colaborador.nome} {colaborador.sobrenome} no banco de dados, tente novamente desde o início.')


class Enfermeiro(Funcionario):
  ''' Subclasse dedicada aos funcionários enfermeiros. Criada como subclasse da classe Funcionarios '''  


class Medico(Funcionario):
  ''' Subclasse dedicada aos funcionários médicos'''  
  def __init__ (self, nome, sobrenome, idade, crm, especialidade, matricula=0):
    super().__init__(nome, sobrenome, idade, matricula)
    self.crm = crm
    self.especialidade = especialidade


class Paciente():
    ''' Classe dedicada aos pacientes assistidos pelo hospital '''
    pacientes = {}
    ''' lista que conterá os pacientes que deram entrada no hospital '''
    def __init__ (self, nome, sobrenome, idade, cpf):
      self.nome = nome
      self.sobrenome = sobrenome
      self.idade = idade
      self.cpf = cpf

    @classmethod
    def entrada(cls, paciente_entrada):
      ''' Esse método registra as informações do(a) paciente e a data de sua entrada no hospital. '''
      
      entrada_paciente = str(input(f'Qual a data de entrada do(a) paciente {paciente_entrada.nome} {paciente_entrada.sobrenome}? Digite dia(d) mês(m) e ano(aaaa) separados apenas por espaços(sem / ou ,)')).strip()
      data_entrada = datetime.strptime(entrada_paciente, '%d %m %Y').date()
      confirmacao = int(input(f"Confirma a entrada em {datetime.strftime(data_entrada, '%d/%m/%Y')} do(a) paciente {paciente_entrada.nome} {paciente_entrada.sobrenome}, {paciente_entrada.idade} anos, CPF nº {paciente_entrada.cpf}? Se 'sim' digite 1, se 'não' digite 2: "))
      if confirmacao == 1: 
        paciente_entrada.data_entrada = data_entrada
        Paciente.pacientes[f'{paciente_entrada.nome} {paciente_entrada.sobrenome}'] = paciente_entrada
        print('Operação realizada com sucesso. Deseje ao paciente uma ótima recuperação')
      elif confirmacao == 2:
        print(f'Não foi registrada a entrada de {paciente_entrada.nome} {paciente_entrada.sobrenome} no banco de dados da unidade hospitalar. Tenha um ótimo dia!')
      else:
        print(f'Não compreendi a resposta. Caso queira registrar a entrada de {paciente_entrada.nome} {paciente_entrada.sobrenome} na base de dados do hospital, tente novamente desde o início.')

    @classmethod
    def saida(cls, paciente_saida):
      ''' Esse método registra a saída do(a) paciente do hospital. '''
      del Paciente.pacientes[paciente_saida]
    
    @classmethod
    def diagnostico(cls, paciente, medico, diagnostico_paciente):
      ''' Esse método registra o diagnóstico dado por um médico a um paciente. '''
      Paciente.pacientes[paciente] = Paciente.pacientes[paciente], [f'Foi diagnosticado(a) com {diagnostico_paciente} pelo(a) medico(a) {medico}']



#adm1 = Funcionario('Maria', 'Silva', 25)
#adm2 = Funcionario('Lenio', 'Brandao', 36)
#adm3 = Funcionario('Heitor', 'Leite', 18, 6)
#Funcionario.contratar(adm1)
#Funcionario.contratar(adm2)
#Funcionario.contratar(adm3)
#print(f'{adm1.nome} {adm1.sobrenome}, {adm1.idade}, {adm1.matricula}')
#print(f'{adm2.nome} {adm2.sobrenome}, {adm2.idade}, {adm2.matricula}')
#print(f'{adm3.nome} {adm3.sobrenome}, {adm3.idade}, {adm3.matricula}')
#print(len(Funcionario.funcionarios))
#enf1 = Enfermeiro('Maria', 'Santos', 25)
#enf2 = Enfermeiro('Lenio', 'Guerreiro', 36)
#enf3 = Enfermeiro('Heitor', 'Brandao', 18, 6)
#Enfermeiro.contratar(enf1)
#Enfermeiro.contratar(enf2)
#Enfermeiro.contratar(enf3)
#print(f'{enf1.nome} {enf1.sobrenome}, {enf1.idade}, {enf1.matricula}')
#print(f'{enf2.nome} {enf2.sobrenome}, {enf2.idade}, {enf2.matricula}')
#print(f'{enf3.nome} {enf3.sobrenome}, {enf3.idade}, {enf3.matricula}')
#print(len(Funcionario.funcionarios))
#med1 = Medico('Maria', 'Ferreira', 25, 111, 'gastroenterologista')
#med2 = Medico('Luciano', 'Silva', 36, 222, 'cardiologista')
#med3 = Medico('Hugo', 'Santos', 18, 333, 'pneumologista', 6)
#Medico.contratar(med1)
#Medico.contratar(med2)
#Medico.contratar(med3)
#print(f'{med1.nome} {med1.sobrenome}, {med1.especialidade} {med1.idade}, {med1.crm}, {med1.matricula}')
#print(f'{med2.nome} {med2.sobrenome}, {med2.especialidade} {med2.idade}, {med2.crm}, {med2.matricula}')
#print(f'{med3.nome} {med3.sobrenome}, {med3.especialidade} {med3.idade}, {med3.crm}, {med3.matricula}')
#print(len(Funcionario.funcionarios))
#pac1 = Paciente('Maria', 'Silva', 25, '111.111.111-11')
#pac2 = Paciente('Lenio', 'Brandao', 36, '222.222.222-22')
#pac3 = Paciente('Heitor', 'Leite', 18, '333.333.333-33')
#Paciente.entrada(pac1)
#Paciente.entrada(pac2)
#Paciente.entrada(pac3)
#print(f"{pac1.nome} {pac1.sobrenome}, {pac1.idade}, {pac1.cpf}", datetime.strftime(pac1.data_entrada, '%d/%m/%Y'))
#print(f"{pac2.nome} {pac2.sobrenome}, {pac2.idade}, {pac2.cpf}", datetime.strftime(pac2.data_entrada, '%d/%m/%Y'))
#print(f"{pac3.nome} {pac3.sobrenome}, {pac3.idade}, {pac3.cpf}", datetime.strftime(pac3.data_entrada, '%d/%m/%Y'))
#print(len(Paciente.pacientes))
#print(Paciente.pacientes)
#Paciente.saida('Lenio Brandao')
#print(len(Paciente.pacientes))
#Paciente.diagnostico('Maria Silva', 'Paula Santos', 'pancreatite')
#print(Paciente.pacientes['Maria Silva'])