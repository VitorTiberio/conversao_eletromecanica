## Autor: Vitor Augusto Tibério - 14658834 ## 

## APE 09 - Curva de Torque e Velocidade com e sem reação de Armadura ## 

## Prof. Elmer Pablo Tito Cari ## 

## Importando as Bibliotecas ## 

import numpy as np 
import matplotlib.pyplot as plt 
import math 

pi = math.pi 

## Definindo as funções ## 
def calcula_corrente_campo(vt, rf): 
    If = vt/rf
    return If

def calcula_tensao_armadura(vt, Ia, Il,ra):
    Ea = vt - (Ia-Il)*ra
    return Ea

def calcula_omega_novo(omega_velho, E_novo, E_velho):
    omega_novo = omega_velho*(E_novo/E_velho)
    return omega_novo

def calcula_torque_induzido(Ea, Ia, omega):
    torque = (Ea*Ia)/(omega*2*pi/60)
    return torque 

def plota_grafico(eixo_x, eixo_y,nome_x,nome_y):
    plt.figure()
    plt.plot(eixo_x, eixo_y)
    plt.xlabel(nome_x)
    plt.ylabel(nome_y)
    plt.xlim(0,600)
    plt.ylim(0,1300)
    plt.show()

def plota_grafico_duplo(eixo_x, eixo_y1, eixo_y2):
    plt.figure()
    plt.plot(eixo_x, eixo_y1)
    plt.plot(eixo_x, eixo_y2)
    plt.xlim(0,600)
    plt.ylim(0,1300)
    plt.show()

## Programa principal ## 

vt = int(input("Insira a tensão de alimentação: "))
N = int(input("Insira o número de espiras: "))
omega = int(input("Insira a velocidade angular (em RPM) da máquina sem carga: "))
rf = int(input('Insira a resistência de campo total: '))
ra = float(input('Insira a resistência de armadura: '))
Ia = [5, 10, 50, 100, 150, 200, 300]
Il = calcula_corrente_campo(vt, rf)
tensao_armadura = []
omega_novo = []
torque_induzido = []
print('Exercício 01: ')
for corrente in Ia: 
    Ea = calcula_tensao_armadura(vt, corrente, Il, ra)
    tensao_armadura.append(Ea)
    omega_n = calcula_omega_novo(omega, Ea, vt)
    omega_novo.append(omega_n)
    torque = calcula_torque_induzido(Ea, corrente, omega_n)
    torque_induzido.append(torque)
    print(f'Para uma corrente de Ia = {corrente}A: Ea = {Ea} V, Velocidade Angular = {omega_n} RPM e o Torque Induzido é {torque} Nm')

# plota_grafico(torque_induzido, omega_novo, "Torque (Nm)", "Velocidade (RPM)")

## Incluindo os efeitos da Armadura ## 

fmmra = [0, 42, 210, 420, 630, 840, 1260]
if_efetiva = []
EA0 = 233
## calculando a nova corrente If* ## 

for posicao in range(len(Ia)):
    if_ef = Ia[posicao]-fmmra[posicao]/N
    if_efetiva.append(if_ef)

## calculando a nova velocidade ## 
omega_efetivo = []
for EA in tensao_armadura: 
    print(EA)
    omega_m = (EA/EA0)*omega
    omega_efetivo.append(omega_m)

