import uuid
from django.test import TestCase
from model_mommy import mommy
from core.models import upload_to_instance


class UploadToInstanceTestCase(TestCase):
    """Testes para a função upload_to_instance."""

    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'

    def test_upload_to_instance(self):
        """Teste se o nome do arquivo gerado é único e mantém a extensão correta."""

        arquivo_gerado = upload_to_instance(None, 'test.png')
        self.assertTrue(len(arquivo_gerado), len(self.filename))


class ServiceModelTestCase(TestCase):
    """Testes para o modelo Service."""

    def setUp(self):
        self.service = mommy.make('Service')

    def test_str_method(self):
        """Teste do método __str__ do modelo Service."""
        self.assertEqual(str(self.service), self.service.service)


class JobTitleModelTestCase(TestCase):
    """Testes para o modelo JobTitle."""

    def setUp(self):
        self.job_title = mommy.make('JobTitle')

    def test_str_method(self):
        """Teste do método __str__ do modelo JobTitle."""
        self.assertEqual(str(self.job_title), self.job_title.job_title)


class EmployeeModelTestCase(TestCase):
    """Testes para o modelo Employee."""

    def setUp(self):
        self.employee = mommy.make('Employee')

    def test_str_method(self):
        """Teste do método __str__ do modelo Employee."""
        self.assertEqual(str(self.employee), self.employee.name)


class FeaturedItemModelTestCase(TestCase):
    """Testes para o modelo FeaturedItem."""

    def setUp(self):
        self.featured_item = mommy.make('FeaturedItem')

    def test_str_method(self):
        """Teste do método __str__ do modelo FeaturedItem."""
        self.assertEqual(str(self.featured_item), self.featured_item.feature)