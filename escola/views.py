from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosSerializer


class AlunosViewSet(viewsets.ModelViewSet):
    """ Exibe todos os alunos e alunas """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    # Difine o tipo de autenticação
    authentication_classes = [BasicAuthentication]
    # Permitição apenas para usuários autenticados
    permissions = [IsAuthenticated]


class CursosViewSet(viewsets.ModelViewSet):
    """ Exibe todos os cursos """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permissions = [IsAuthenticated]


class MatriculasViewSet(viewsets.ModelViewSet):
    """ Exibe todos as Matriculas """
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permissions = [IsAuthenticated]


class ListaMatriculasAluno(generics.ListAPIView):
    """ Lista as matriculas de um aluno """

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permissions = [IsAuthenticated]


class ListaAlunosMatriculados(generics.ListAPIView):
    """ Lista os alunos e alunas matriculados em um curso """

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer
    authentication_classes = [BasicAuthentication]
    permissions = [IsAuthenticated]
