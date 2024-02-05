from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(default='example@example.com')

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='veiculos')
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    placa = models.CharField(max_length=10, default='***-****')

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.placa}"

class Orcamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    data = models.DateField()
    descricao = models.TextField()

    def __str__(self):
        return f"Orçamento para {self.veiculo} em {self.data}"
