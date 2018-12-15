import pandas
import secrets
import string
from account.models import User, Ninja
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError


class Command(BaseCommand):
    help = 'Importa base de usuários do Seja Ninja'

    def add_arguments(self, parser):
        parser.add_argument('data_file', nargs='+', type=str)

    def handle(self, *args, **options):
        self.passwords = {}
        for data_file in options['data_file']:
            self.import_file(data_file)
        for email in sorted(self.passwords.keys()):
            print("%s\t%s" % (email, self.passwords[email]))

    def import_file(self, data_file):
        User.objects.all().delete()
        users = pandas.read_csv(data_file)
        for i in range(len(users)):
            self.import_user(users.iloc[i])

    def generate_password(self):
        alphabet = string.ascii_letters + string.digits
        return ''.join(secrets.choice(alphabet) for i in range(8))

    def import_user(self, data):
        email = data.Email
        if not isinstance(email, str):
            return
        password = self.generate_password()
        self.passwords[email] = password
        name = data['Nome Completo']
        try:
            user = User.objects.create(email=email, password=password, first_name=name)
        except IntegrityError:
            return
        ninja = dict(
            user=user,
            nome=name,
            cidade=data.Cidade,
            estado=data.Estado,
            pais=data['País'],
            telefone=data.Telefone,
            dataNascimento=data['Data de Nascimento'],
            genero=data['Gênero'],
            etnia=data['Etnia'],
        )
        Ninja.objects.create(**ninja)
