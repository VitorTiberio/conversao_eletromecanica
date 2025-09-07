## ------------ APE 04 - Transformadores Trifásicos -------------------- ###

## Autor: Vitor Augusto Tibério - 14658834 - Eng. Elétrica - Automação ## 

## Prof. Dr. Elmer Pablo Tito Cari - Escola de Eng. de São Carlos - USP

### --------------------------------------------------------------------- ###

#importando as bibliotecas
import cmath 
import math
import matplotlib.pyplot as plt

### ----------------------- Definindo as Funções -----------------------###:

def regulacao_tensao(potencia_nominal, fp, req_2, xeq_2, tensao_secundario):
    plena_carga = [i/100 for i in range(1,101)]     #cria uma lista com os valores de 0.01 a 1.00 de valores de plena carga                                              
    RV = []                                         #definine uma lista que vai ajudar no plot do gráfico
    for carga in plena_carga:                       #loop para preencher a lista RV
        mag_corrente = (potencia_nominal*carga)/(tensao_secundario*math.sqrt(3))    #calcula magnetude da corrente no secundário
        ang = cmath.acos(fp)                                                        #encontra o ângulo da corrente
        corrente = mag_corrente*cmath.cos(ang) - (cmath.sin(ang)*mag_corrente)*1j   #variável corrente do secundário (complexa)
        zeq_2 = req_2 + xeq_2*1j                                                    #impedância equivalente do secundário
        vp_linha = (tensao_secundario/cmath.sqrt(3)) + corrente*zeq_2               #cálculo de Vp'
        mag_vp , ang_vp = cmath.polar(vp_linha)                                     #valores de magnetude e angulo de Vp'
        #print(f'O valor de Vp_linha para {carga*100}% de plena carga é: {mag_vp}')  
        reg = (mag_vp - (tensao_secundario/cmath.sqrt(3)))/(tensao_secundario/cmath.sqrt(3))*100 #calcula RV
        RV.append(reg)                                                              #adiciona o valor calculado à lista de RV
    
    #plot do gráfico
    plt.figure()
    plt.plot(plena_carga, RV)
    plt.xlabel('Plena Carga')
    plt.ylabel('Regulação de Tensão (em %)')
    plt.title('Gráfico da Regulação de Tnesão com Base na Plena Carga')


def calcula_eficiencia(potencia_nominal, fp, tensao_secundario, Rc, Req_2):
    plena_carga = [i/100 for i in range(1,101)]     #cria uma lista com os valores de 0.01 a 1.00 de valores de plena carga
    eficiencia = []                                 #definine uma lista que vai ajudar no plot do gráfico
    for carga in plena_carga:                       #loop para preencher a lista eficiencia                           
        corrente_nominal = (potencia_nominal*carga)/(tensao_secundario*math.sqrt(3)) #calcula a corrente nominal no secundário
        P_saida = (potencia_nominal*fp*carga)/3                                      #calcula a potência de saída   
        P_nucleo = (((tensao_secundario/math.sqrt(3))**2)/Rc)                        #calcula as perdas no núcleo
        P_cobre = (corrente_nominal*corrente_nominal)*Req_2                          #calcula as perdas no cobre
        rendimento = (P_saida / (P_saida + P_cobre + P_nucleo))*100                  #calcula o rendimento
        #print(f'O redimento para {carga*100}% de plena carga é: {rendimento}')
        eficiencia.append(rendimento)                                               #adiciona o resultado à lista eficiência
    
    #plot do gráfico
    plt.figure()                            #cria uma figura para ser exibida
    plt.plot(plena_carga, eficiencia)       #plota o gráfico (variável x por variável y)
    plt.xlabel('Plena Carga')               #nomeia o eixo X do gráfico
    plt.ylabel('Eficiência (em %)')         #nomeia o eixo Y do gráfico
    plt.title('Gráfico da Eficiência com Base na Plena Carga')

    return ()

### ------------------ Código Principal ---------------------------###

if __name__ == "__main__":

    eficiencias = calcula_eficiencia(10000000, 0.8, 7200, 720.03, 0.041464) #chama a função definida para calculo das eficiências

    rv = regulacao_tensao(10000000, 0.8, 0.041464, 0.62064, 7200)           #chama a função definida para calculo da regulação da tensão

    plt.show()      #plota as figuras simultaneamente