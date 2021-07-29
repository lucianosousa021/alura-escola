from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula

class AlunoSerializer(serializers.ModelSerializer):
    """ correlaciona os dados de Models com os dados disponibilizados na api"""
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

class CursoSerializer(serializers.ModelSerializer):
    """ correlaciona os dados de Models com os dados disponibilizados na api"""
    class Meta:
        model = Curso
        fields = ['id', 'codigo_curso', 'descricao', 'nivel']

class MatriculaSerializer(serializers.ModelSerializer):
    """ correlaciona os dados de Models com os dados disponibilizados na api"""
    class Meta:
        model = Matricula
        fields = '__all__'

class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()

class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model = Matricula
        fields = ['aluno_nome']