class Media():
    
    student_marks = {}

    def __init__(self, aluno, nota1, nota2, nota3):
        self.aluno = aluno
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        notas = [nota1, nota2, nota3]
        Media.student_marks[aluno] = notas
    
    def med_aluno(self): 
        if self.aluno in Media.student_marks:
            lista = list(map(lambda x: x, Media.student_marks.get(self.aluno)))
            media = float(sum(lista)/3)
            print('%.2f' % media)
        else:
            print('O nome informado não consta nos alunos informados. Tente novamente')


aluno1 = Media('Lenio', 7, 8, 7)
aluno1.med_aluno()