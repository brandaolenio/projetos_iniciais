from datetime import datetime

class Hospital():
  ''' Banco de dados de hospital, desenvolvido durante o curso de WebDev na Sirus Educação '''
  def __init__(self, nome, endereco):
    self.nome = nome
    self.endereco = endereco


class Funcionario(): 
  ''' Classe base dedica aos funcionário do hospital '''
  funcionarios = {}
  ''' Esse dicionário  conterá todos os funcionários contratados pelo hospital'''
  pagmtos_funcionarios = {}
  ''' Esse dicionário  conterá todos os registros de pagamentos a funcionários'''
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
        confirmacao = int(input(f"Confirma a inclusão de {colaborador.nome} {colaborador.sobrenome}, {colaborador.especialidade}, {colaborador.idade} anos, matricula {colaborador.matricula}, CRM nº {colaborador.crm} no banco de dados como 'contratado(a)'? digite 1 para 'sim' e 2 para 'não': "))    
      else:
        confirmacao = int(input(f"Confirma a inclusão de {colaborador.nome} {colaborador.sobrenome}, {colaborador.idade} anos, matrícula {colaborador.matricula} no banco de dados como 'contratado(a)'? digite 1 para 'sim' e 2 para 'não': "))
      
      if confirmacao == 1:
        if isinstance(colaborador, Medico) == True:
          Funcionario.funcionarios[f'{colaborador.nome} {colaborador.sobrenome}, {colaborador.especialidade}'] = f'{colaborador.idade} anos, CRM nº {colaborador.crm}, {colaborador.especialidade}, matricula {colaborador.matricula}'
          print('Operação realizada com sucesso. Tenha um ótimo dia. Até breve!')
        else:
          Funcionario.funcionarios[f'{colaborador.nome} {colaborador.sobrenome}'] = f'{colaborador.idade} anos, matrícula {colaborador.matricula}'
          print('Operação realizada com sucesso. Tenha um ótimo dia. Até breve!')
      elif confirmacao == 2:
        print(f'{colaborador.nome} {colaborador.sobrenome} não foi incluído(a) no banco de dados. Tenha um ótimo dia. Até breve!')
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
        confirmacao = int(input(f"Confirma a inclusão de {colaborador.nome} {colaborador.sobrenome}, {colaborador.especialidade}, {colaborador.idade} anos, matricula {colaborador.matricula}, CRM nº {colaborador.crm} no banco de dados como 'contratado(a)'? digite 1 para 'sim' e 2 para 'não': "))    
      else:
        confirmacao = int(input(f"Confirma a inclusão de {colaborador.nome} {colaborador.sobrenome}, {colaborador.idade} anos, matrícula {colaborador.matricula} no banco de dados como 'contratado(a)'? digite 1 para 'sim' e 2 para 'não': "))
    
      if confirmacao == 1:
        if isinstance(colaborador, Medico) == True:
          Funcionario.funcionarios[f'{colaborador.nome} {colaborador.sobrenome}, {colaborador.especialidade}'] = f'{colaborador.idade} anos, CRM nº {colaborador.crm}, {colaborador.especialidade}, matricula {colaborador.matricula}'
          print('Operação realizada com sucesso. Tenha um ótimo dia. Até breve!')
        else:
          Funcionario.funcionarios[f'{colaborador.nome} {colaborador.sobrenome}'] = f'{colaborador.idade} anos, matrícula {colaborador.matricula}'
          print('Operação realizada com sucesso. Tenha um ótimo dia. Até breve!')
      elif confirmacao == 2:
        print(f'{colaborador.nome} {colaborador.sobrenome} não foi incluído(a) no banco de dados. Tenha um ótimo dia. Até breve!')
      else: 
        print(f'Não compreendi a resposta. Caso queira inserir {colaborador.nome} {colaborador.sobrenome} no banco de dados, tente novamente desde o início.')

  @classmethod
  def pagamento_funcionario(cls, emitente, beneficiario, sal_administrativo=1300, sal_enfermeiros=1500, sal_medicos=2000):  
    ''' Classe que possui os métodos que registra as ordens de pagamentos feitas pelo setor administrativo aos funcionários do hospital,
    identificando, ainda, quem realizou esse pagamento'''
    if [x for x,y in Funcionario.funcionarios.items() if x == emitente and y.endswith('A')]:
      beneficiario_lista = [x for x in Funcionario.funcionarios if x.startswith(beneficiario)]
      if len(beneficiario_lista) > 0:
        beneficiario = beneficiario_lista[0]
        if [x for x,y in Funcionario.funcionarios.items() if x == beneficiario and y.endswith('E')]:
          confirmacao = int(input(f"Deseja confirmar que {emitente} pagou R${sal_enfermeiros} para {beneficiario}, enfermeiro(a)? Digite 1 para 'sim' e 2 para 'não': "))
          if confirmacao == 1:
            if beneficiario in Funcionario.pagmtos_funcionarios:
              Funcionario.pagmtos_funcionarios[beneficiario] = Funcionario.pagmtos_funcionarios[beneficiario], (f'{emitente} pagou R${sal_enfermeiros} para {beneficiario}, enfermeiro(a)')
              print('Operação realizada com sucesso. Ótimo dia! Até breve!')
            else:
              Funcionario.pagmtos_funcionarios[beneficiario] = (f'{emitente} pagou R${sal_enfermeiros} para {beneficiario}, enfermeiro(a)')
              print('Operação realizada com sucesso. Ótimo dia! Até breve!')
          elif confirmacao == 2:
            print(f"O pagamento de R${sal_enfermeiros} a {beneficiario}, enfermeiro(a), não foi processado. Até breve!")
          else:
            print(f'Não compreendi a resposta. Caso deseje realizar o pagamento de R${sal_enfermeiros} a {beneficiario}, enfermeiro(a), tente novamente desde o início')
        elif [x for x,y in Funcionario.funcionarios.items() if x == beneficiario and y.endswith('M')]:
          confirmacao = int(input(f"Deseja confirmar que {emitente} pagou R${sal_medicos} para {beneficiario}? Digite 1 para 'sim' e 2 para 'não': "))
          if confirmacao == 1:
            if beneficiario in Funcionario.pagmtos_funcionarios:
              Funcionario.pagmtos_funcionarios[beneficiario] = Funcionario.pagmtos_funcionarios[beneficiario], (f'{emitente} pagou R${sal_medicos} para {beneficiario}')
              print('Operação realizada com sucesso. Ótimo dia! Até breve!')
            else:
              Funcionario.pagmtos_funcionarios[beneficiario] = (f'{emitente} pagou R${sal_medicos} para {beneficiario}')
              print('Operação realizada com sucesso. Ótimo dia! Até breve!')
          elif confirmacao == 2:
            print(f"O pagamento de R${sal_medicos} a {beneficiario}, não foi processado. Até breve!")
          else:
            print(f'Não compreendi a resposta. Caso deseje realizar o pagamento de R${sal_medicos} a {beneficiario}, tente novamente desde o início')
        elif [x for x,y in Funcionario.funcionarios.items() if x == beneficiario and y.endswith('A')]:
          if emitente != beneficiario:
            confirmacao = int(input(f"Deseja confirmar que {emitente} pagou R${sal_administrativo} para {beneficiario}, setor administrativo? Digite 1 para 'sim' e 2 para 'não': "))
            if confirmacao == 1:
              if beneficiario in Funcionario.pagmtos_funcionarios:
                Funcionario.pagmtos_funcionarios[beneficiario] = Funcionario.pagmtos_funcionarios[beneficiario], (f'{emitente} pagou R${sal_administrativo} para {beneficiario}, setor administrativo')
                print('Operação realizada com sucesso. Ótimo dia! Até breve!')
              else:
                Funcionario.pagmtos_funcionarios[beneficiario] = (f'{emitente} pagou R${sal_administrativo} para {beneficiario}, setor administrativo')
                print('Operação realizada com sucesso. Ótimo dia! Até breve!')
            elif confirmacao == 2:
              print(f"O pagamento de R${sal_administrativo} a {beneficiario}, setor administrativo, não foi processado. Até breve!")
            else:
              print(f'Não compreendi a resposta. Caso deseje realizar o pagamento de R${sal_administrativo} a {beneficiario}, setor administrativo, tente novamente desde o início')
          else:
              print(f'{emitente} consta como responsável pela ordem de pagamento e ao mesmo tempo como beneficiário(a) dessa ordem. O pagamento não foi realizado, pois não se pode emitir ordem de pagamento em favor próprio')
      else:
        print("O(A) beneficiário(a) informado(a) não se encontra nos registros de funcionários contratados pelo hospital. Assim, o pagamento em favor dessa pessoa não foi realizado")
    else:
      print('Apenas funcionários do setor administrativo estão habilitados a realizar pagamentos')
  
  @staticmethod
  def lista_funcionários():
    '''Esse método exibirá a lista de funcionários do hospital em ordem alfabética e divididos por tipos. 
    Quando a pessoa tiver uma especialidade, exibir após o nome.'''
    administrativo = [x for x,y in Funcionario.funcionarios.items() if y.endswith('A')]
    administrativo.insert(0, 'Setor Administrativo')
    enfermeiros = [x for x,y in Funcionario.funcionarios.items() if y.endswith('E')]
    enfermeiros.insert(0, 'Enfermeiros(as)')
    medicos = [x for x,y in Funcionario.funcionarios.items() if y.endswith('M')]
    medicos.insert(0, 'Medicos(as)')
    for i in administrativo:
      print(i, end="\n")
    for j in enfermeiros:
      print(j, end='\n')
    for k in medicos:
      print(k, end='\n')


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
      paciente_entrada.data_entrada = data_entrada
      confirmacao = int(input(f"Confirma a entrada em {datetime.strftime(data_entrada, '%d/%m/%Y')} do(a) paciente {paciente_entrada.nome} {paciente_entrada.sobrenome}, {paciente_entrada.idade} anos, CPF nº {paciente_entrada.cpf}? Se 'sim' digite 1, se 'não' digite 2: "))
      if confirmacao == 1:
        Paciente.pacientes[f'{paciente_entrada.nome} {paciente_entrada.sobrenome}'] = f"{paciente_entrada.idade} anos, CPF nº {paciente_entrada.cpf}, deu entrada no hospital em {datetime.strftime(data_entrada, '%d/%m/%Y')}"
        print('Operação realizada com sucesso. Deseje ao paciente uma ótima recuperação')
      elif confirmacao == 2:
        print(f'Não foi incluída a entrada de {paciente_entrada.nome} {paciente_entrada.sobrenome} na lista de paciente desta unidade hospitalar. Tenha um ótimo dia!')
      else:
        print(f'Não compreendi a resposta. Caso queira registrar a entrada de {paciente_entrada.nome} {paciente_entrada.sobrenome} neste hospital, tente novamente desde o início.')
     
    @classmethod
    def diagnostico(cls, paciente, medico, diagnostico_paciente):
      ''' Esse método registra o diagnóstico dado por um médico a um paciente. '''
      if paciente in Paciente.pacientes:
        med = [x for x in Funcionario.funcionarios if x.startswith(medico)]
        medico = med[0]
        if medico in Funcionario.funcionarios:
          confirmacao = int(input(f"Confirma que o(a) paciente {paciente} recebeu o diagnóstico de {diagnostico_paciente} do(a) médico(a) {medico}? Digite 1 para 'sim' e 2 para 'não': "))
          if confirmacao == 1:
            Paciente.pacientes[paciente] = Paciente.pacientes[paciente], [f'Foi diagnosticado(a) com {diagnostico_paciente} pelo(a) medico(a) {medico}']
            print('Operação realizada com sucesso. Até breve!')
          elif confirmacao == 2:
            print(f'O diagnóstico {diagnostico_paciente} não foi incluído nos registros do(a) paciente {paciente}. Tenha um ótimo dia!')
          else:
            print(f'Não compreendi a resposta. Caso queira inserir no banco de dados do hospital o diagnóstio de {diagnostico_paciente} dado ao(à) {paciente} pelo(a) {medico}, tente novamente desde o início.')            
        else:
          print(f'O(A) médico(a) {medico} não consta nos registros de funcionários deste hospital')
      else:
        print(f'{paciente} não consta na lista de pacientes deste hospital')

    @classmethod
    def saida(cls, paciente_saida):
      ''' Esse método registra a saída do(a) paciente do hospital. '''
      if paciente_saida in Paciente.pacientes:
        confirmacao = int(input(f"Confirma a saída de {paciente_saida} da lista de pacientes deste hospital? Digite 1 para 'sim' e 2 para 'não': "))
        if confirmacao == 1:
          del Paciente.pacientes[paciente_saida]
          print(f'A saída de {paciente_saida} da lista de pacientes foi resgitrada com sucesso. Até breve!')
        elif confirmacao == 2:
          print(f'A saída de {paciente_saida} da lista de pacientes não foi registrada. Até breve!')
        else:
          print(f'Não compreendi a resposta. Caso queira retirar {paciente_saida} da lista de pacientes do hospital, tente novamente desde o início.')            
          

#adm1 = Funcionario('Maria', 'Silva', 25)
#adm2 = Funcionario('Lenio', 'Brandao', 36)
#adm3 = Funcionario('Heitor', 'Leite', 18, 6)
#Funcionario.contratar(adm1)
#Funcionario.contratar(adm2)
#Funcionario.contratar(adm3)
#print(f'{adm1.nome} {adm1.sobrenome}, {adm1.idade}, {adm1.matricula}')
#print(f'{adm2.nome} {adm2.sobrenome}, {adm2.idade}, {adm2.matricula}')
#print(f'{adm3.nome} {adm3.sobrenome}, {adm3.idade}, {adm3.matricula}')
#print(Funcionario.funcionarios)
#enf1 = Enfermeiro('Maria', 'Santos', 25)
#enf2 = Enfermeiro('Lenio', 'Guerreiro', 36)
#enf3 = Enfermeiro('Heitor', 'Brandao', 18, 6)
#Enfermeiro.contratar(enf1)
#Enfermeiro.contratar(enf2)
#Enfermeiro.contratar(enf3)
#print(f'{enf1.nome} {enf1.sobrenome}, {enf1.idade}, {enf1.matricula}')
#print(f'{enf2.nome} {enf2.sobrenome}, {enf2.idade}, {enf2.matricula}')
#print(f'{enf3.nome} {enf3.sobrenome}, {enf3.idade}, {enf3.matricula}')
#print(Funcionario.funcionarios)
#med1 = Medico('Maria', 'Ferreira', 25, 111, 'gastroenterologista')
#med2 = Medico('Luciano', 'Silva', 36, 222, 'cardiologista')
#med3 = Medico('Hugo', 'Santos', 18, 333, 'pneumologista', 6)
#Medico.contratar(med1)
#Medico.contratar(med2)
#Medico.contratar(med3)
#print(f'{med1.nome} {med1.sobrenome}, {med1.especialidade} {med1.idade}, {med1.crm}, {med1.matricula}')
#print(f'{med2.nome} {med2.sobrenome}, {med2.especialidade} {med2.idade}, {med2.crm}, {med2.matricula}')
#print(f'{med3.nome} {med3.sobrenome}, {med3.especialidade} {med3.idade}, {med3.crm}, {med3.matricula}')
#print(Funcionario.funcionarios)
#pac1 = Paciente('Maria', 'Silva', 25, '111.111.111-11')
#pac2 = Paciente('Lenio', 'Brandao', 36, '222.222.222-22')
#pac3 = Paciente('Heitor', 'Leite', 18, '333.333.333-33')
#Paciente.entrada(pac1)
#Paciente.entrada(pac2)
#Paciente.entrada(pac3)
#print(f"{pac1.nome} {pac1.sobrenome}, {pac1.idade}, {pac1.cpf}", datetime.strftime(pac1.data_entrada, '%d/%m/%Y'))
#print(f"{pac2.nome} {pac2.sobrenome}, {pac2.idade}, {pac2.cpf}", datetime.strftime(pac2.data_entrada, '%d/%m/%Y'))
#print(f"{pac3.nome} {pac3.sobrenome}, {pac3.idade}, {pac3.cpf}", datetime.strftime(pac3.data_entrada, '%d/%m/%Y'))
#print(Paciente.pacientes)
#Paciente.saida('Lenio Brandao')
#print(Paciente.pacientes)
#Paciente.diagnostico('Maria Silva', 'Luciano Silva', 'infarto')
#Paciente.diagnostico('Alana Souza', 'Luciano Silva', 'hipertensão arterial')
#Paciente.diagnostico('Maria Silva', 'José Santos', 'cardiopatia congênita')
#print(Paciente.pacientes)
#Funcionario.pagamento_funcionario('Maria Silva', 'Heitor Leite')
#Funcionario.pagamento_funcionario('Maria Silva', 'Lenio Guerreiro')
#Funcionario.pagamento_funcionario('Maria Silva', 'Hugo Santos')
#Funcionario.pagamento_funcionario('Maria Silva', 'Maria Silva')
#Funcionario.pagamento_funcionario('Heitor Leite', 'Maria Silva')
#Funcionario.pagamento_funcionario('Heitor Leite', 'Jose Maria')
#Funcionario.pagamento_funcionario('Joao Ferreira', 'Maria Silva')
#print(Funcionario.pagmtos_funcionarios)
#Funcionario.lista_funcionários()
