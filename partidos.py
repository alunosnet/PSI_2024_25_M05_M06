partido_a={'a','b','c'}
partido_b={'a','k','y'}
partido_c={'a','b','z','t'}

#listar os elementos repetidos em pelo menos 2 partidos
partido_a_b = partido_a.intersection(partido_b)
partido_a_c = partido_a.intersection(partido_c)
partido_b_c = partido_b.intersection(partido_c)
repetidos_todos = partido_a_b | partido_a_c | partido_b_c
print(f"Os elementos repetidos em pelo menos 2 partidos são: {repetidos_todos}")

#listar os elementos repetidos entre todos os partidos
partido_a_b_c = partido_a & partido_b & partido_c
print(f"Elementos comuns a todos os partidos: {partido_a_b_c}")

#listar os elementos dos partidos retirando os repetidos
print(f"Partido A:{partido_a.difference(repetidos_todos)}")
print(f"Partido B: {partido_b.difference(repetidos_todos)}")
print(f"Partido C: {partido_c.difference(repetidos_todos)}")
