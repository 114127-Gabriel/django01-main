from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(verbose_name="Nome", max_length=30)
    last_name = models.CharField(verbose_name="Sobrenome", max_length=30)
    date_of_birth = models.CharField(verbose_name="Data de nascimento", max_length=10)
    cpf = models.CharField(verbose_name="CPF", max_length=14, unique=True)
    phone_number = models.CharField(verbose_name="Telefone", max_length=20)
    email = models.CharField(verbose_name="Email", max_length=50)

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        ordering = ["first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Professional(models.Model):
    first_name = models.CharField(verbose_name="Nome", max_length=30)
    last_name = models.CharField(verbose_name="Sobrenome", max_length=30)
    date_of_birth = models.CharField(verbose_name="Data de nascimento", max_length=10)
    cpf = models.CharField(verbose_name="CPF", max_length=14, unique=True)
    phone_number = models.CharField(verbose_name="Telefone", max_length=20)
    email = models.CharField(verbose_name="Email", max_length=50)
    crm = models.CharField(verbose_name="CRM", max_length=10, unique=True)
    specialty = models.CharField(verbose_name="Especialidade", max_length=20)

    class Meta:
        verbose_name = "Profissional"
        verbose_name_plural = "Profissionais"
        ordering = ["first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Agenda(models.Model):
    STATUS_CHOICES = [
        ("-", "---"),
        ("1", "Agendado"),
        ("2", "No Local"),
        ("3", "Em Atendimento"),
        ("4", "Atendido")
    ]
    # Agendamento
    patiente = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="Paciente")
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE, verbose_name="Profissional")
    date = models.CharField(verbose_name="Data de nascimento", max_length=10)
    hour = models.CharField(verbose_name="Horário de agendamento", max_length=5)
    status = models.CharField(verbose_name="Status", max_length=20, choices=STATUS_CHOICES, default="-")
    obs = models.TextField(verbose_name="Observação", max_length=500,blank=True)
    medical_order = models.ImageField(verbose_name="Pedido Médico", upload_to="projeto/pedidos/",blank=True)
    
    # Atendimento
    medical_report = models.FileField(verbose_name="Laudo Médico",upload_to="projeto/laudos/",blank=True)
    description = models.TextField(verbose_name="Descrição", max_length=100)
    cust = models.DecimalField(verbose_name="Valor", max_digits=10, decimal_places=2)
    start = models.CharField(verbose_name="Início do Atendimento", max_length=5)
    end = models.CharField(verbose_name="Fim do Atendimento", max_length=5, blank=True)

    class Meta:
        verbose_name = "Agenda"
        verbose_name_plural = "Agendas"
        ordering = ["-date"]

    def __str__(self):
        return self.patiente, self.date
