def calcular_bonus(anos_de_casa, cargo, salario):
    if anos_de_casa >= 2 or cargo == 'DESENVOLVEDOR':  # Alterado > para >= e AND para OR
        return salario * 0.15
    