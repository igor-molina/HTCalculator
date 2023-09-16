import datetime


def calcular_horas_trabalhadas(hora_inicio, hora_fim, duracao_intervalo=None):
    try:
        formato = "%H%M" if len(hora_inicio) == 4 else "%H:%M"
        hora_inicio = datetime.datetime.strptime(hora_inicio, formato)
        hora_fim = datetime.datetime.strptime(hora_fim, formato)

        if duracao_intervalo:
            duracao_intervalo = duracao_intervalo.replace(":", "")
            duracao_intervalo = datetime.datetime.strptime(duracao_intervalo, "%H%M")
            hora_fim -= duracao_intervalo

        hora_inicio_timedelta = datetime.timedelta(hours=hora_inicio.hour, minutes=hora_inicio.minute)
        hora_fim_timedelta = datetime.timedelta(hours=hora_fim.hour, minutes=hora_fim.minute)

        diferenca_inicio_fim = hora_fim_timedelta - hora_inicio_timedelta
        diferenca_fim_inicio = hora_inicio_timedelta - hora_fim_timedelta

        if abs(diferenca_inicio_fim) < abs(diferenca_fim_inicio):
            diferenca = diferenca_inicio_fim
        else:
            diferenca = diferenca_fim_inicio

        horas_trabalhadas = diferenca.total_seconds() / 3600

        if horas_trabalhadas < 0:
            raise ValueError("Hora de início posterior à hora de término")

        horas = int(horas_trabalhadas)
        minutos = int((horas_trabalhadas - horas) * 60)

        return f"{horas}:{minutos:02}"

    except ValueError:
        raise ValueError("Formato de hora inválido")


if __name__ == "__main__":
    hora_inicio = input("Digite a hora de início (H:mm ou HHmm): ")
    hora_fim = input("Digite a hora de término (H:mm ou HHmm): ")
    duracao_intervalo = input("Digite a duração do intervalo (H:mm ou HHmm, opcional): ")

    try:
        resultado = calcular_horas_trabalhadas(hora_inicio, hora_fim, duracao_intervalo)
        print(f"Horas trabalhadas: {resultado}")
    except ValueError as e:
        print(f"Erro: {e}")
