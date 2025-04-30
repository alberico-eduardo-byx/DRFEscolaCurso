from django.test import TestCase
from rest_framework.test import APIRequestFactory
from escola.models import Estudante, Curso, Matricula

from escola.views import (
    EstudanteViewSet, 
    CursoViewSet, 
    MatriculaViewSet, 
    ListaMatriculaEstudante, 
    ListaMatriculaCurso
)
from escola.serializers import (
    EstudanteSerializer,
    EstudanteSerializerV2,
    CursoSerializer,
    MatriculaSerializer,
    ListaMatriculasEstudanteSerializer,
    ListaMatriculasCursoSerializer
)


class EstudanteViewSetTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.estudante = Estudante.objects.create(
            nome="Test Student",
            cpf="12345678901",
            data_nascimento="2000-01-01",
            celular="11987654321",
            email="test@example.com"
        )
        
    def test_get_serializer_class_default(self):
        request = self.factory.get('/estudantes/')
        request.version = 'v1'
        view = EstudanteViewSet()
        view.request = request
        
        self.assertEqual(view.get_serializer_class(), EstudanteSerializer)
        
    def test_get_serializer_class_v2(self):
        request = self.factory.get('/estudantes/')
        request.version = 'v2'
        view = EstudanteViewSet()
        view.request = request
        
        self.assertEqual(view.get_serializer_class(), EstudanteSerializerV2)
        
    def test_filter_backends(self):
        view = EstudanteViewSet()
        self.assertEqual(len(view.filter_backends), 3)
        
    def test_ordering_fields(self):
        view = EstudanteViewSet()
        self.assertEqual(view.ordering_fields, ['nome'])
        
    def test_search_fields(self):
        view = EstudanteViewSet()
        self.assertEqual(view.search_fields, ['nome', 'cpf'])


class CursoViewSetTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.curso = Curso.objects.create(
            codigo="CS101",
            descricao="Introduction to Computer Science",
            nivel="B"
        )
        
    def test_queryset(self):
        view = CursoViewSet()
        self.assertEqual(list(view.queryset), list(Curso.objects.all()))
        
    def test_serializer_class(self):
        view = CursoViewSet()
        self.assertEqual(view.serializer_class, CursoSerializer)


class MatriculaViewSetTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.estudante = Estudante.objects.create(
            nome="Test Student",
            cpf="12345678901",
            data_nascimento="2000-01-01",
            celular="11987654321",
            email="test@example.com"
        )
        self.curso = Curso.objects.create(
            codigo="CS101",
            descricao="Introduction to Computer Science",
            nivel="B"
        )
        self.matricula = Matricula.objects.create(
            estudante=self.estudante,
            curso=self.curso,
            periodo="M"
        )
        
    def test_queryset(self):
        view = MatriculaViewSet()
        self.assertEqual(list(view.queryset), list(Matricula.objects.all()))
        
    def test_serializer_class(self):
        view = MatriculaViewSet()
        self.assertEqual(view.serializer_class, MatriculaSerializer)


class ListaMatriculaEstudanteTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.estudante = Estudante.objects.create(
            nome="Test Student",
            cpf="12345678901",
            data_nascimento="2000-01-01",
            celular="11987654321",
            email="test@example.com"
        )
        self.curso = Curso.objects.create(
            codigo="CS101",
            descricao="Introduction to Computer Science",
            nivel="B"
        )
        self.matricula = Matricula.objects.create(
            estudante=self.estudante,
            curso=self.curso,
            periodo="M"
        )
        
    def test_get_queryset(self):
        view = ListaMatriculaEstudante()
        view.kwargs = {'pk': self.estudante.id}
        queryset = view.get_queryset()
        
        self.assertEqual(list(queryset), list(Matricula.objects.filter(estudante_id=self.estudante.id)))
        
    def test_serializer_class(self):
        view = ListaMatriculaEstudante()
        self.assertEqual(view.serializer_class, ListaMatriculasEstudanteSerializer)


class ListaMatriculaCursoTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.estudante = Estudante.objects.create(
            nome="Test Student",
            cpf="12345678901",
            data_nascimento="2000-01-01",
            celular="11987654321",
            email="test@example.com"
        )
        self.curso = Curso.objects.create(
            codigo="CS101",
            descricao="Introduction to Computer Science",
            nivel="B"
        )
        self.matricula = Matricula.objects.create(
            estudante=self.estudante,
            curso=self.curso,
            periodo="M"
        )
        
    def test_get_queryset(self):
        view = ListaMatriculaCurso()
        view.kwargs = {'pk': self.curso.id}
        queryset = view.get_queryset()
        
        self.assertEqual(list(queryset), list(Matricula.objects.filter(curso_id=self.curso.id)))
        
    def test_serializer_class(self):
        view = ListaMatriculaCurso()
        self.assertEqual(view.serializer_class, ListaMatriculasCursoSerializer)