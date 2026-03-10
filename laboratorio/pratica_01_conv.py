import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- 1. PARÂMETROS E CONSTANTES (Conforme Dados da Bancada) ---
l_fc = 0.4916         # Comprimento do núcleo (m)
A = 0.00061182         # Seção transversal (m²)
N = 800              # Espiras por bobina
R_sh = 1.0           # Resistor de shunt (Ohms)
R = 1e6              # Resistor do integrador (1 MOhm)
C = 10e-6            # Capacitor do integrador (10 uF)

# Constantes de Proporcionalidade (Dedução do Item 1.3)
k1 = (R_sh * l_fc) / N   # H = Vx / k1
k2 = (N * A) / (R * C)   # B = Vy / k2

# --- 2. LEITURA DO ARQUIVO EXCEL ---
# Lendo a aba 'Dados' e pulando as linhas de cabeçalho visual
df_raw = pd.read_excel('dados_experimentos.xlsx', sheet_name='Dados', header=None)

# Limpeza: Convertendo tudo para numérico e removendo linhas de texto ou vazias
df = df_raw.apply(pd.to_numeric, errors='coerce').dropna(subset=[2, 3]).reset_index(drop=True)

# --- 3. MAPEAMENTO DAS COLUNAS (Posição 0-indexed) ---
# Coluna 2: Vx (Sem Gap) | Coluna 3: Vy (Sem Gap)
# Coluna 6: Vx (Com Gap) | Coluna 7: Vy (Com Gap)
h_sem = df.iloc[:, 2] / k1
b_sem = df.iloc[:, 3] / k2
h_com = df.iloc[:, 6] / k1
b_com = df.iloc[:, 7] / k2

# Permeabilidade (mu = B/H) - Apenas para o caso sem entreferro
mu_sem = b_sem / h_sem

# --- 4. GERAÇÃO DOS GRÁFICOS SOLICITADOS NO RELATÓRIO ---

# Divisão dos dados para o Laço de Histerese (Subida e Descida)
# Com base na sua coleta, o ponto máximo ocorre por volta do índice 10 ou 11
split = 11 

# GRÁFICO 1: Laço de Histerese (B x H) - Sem e Com Entreferro
plt.figure(figsize=(10, 6))
plt.plot(h_sem[:split+1], b_sem[:split+1], 'b-o', label='Sem Entreferro (Subida)')
plt.plot(h_sem[split:], b_sem[split:], 'b--x', label='Sem Entreferro (Descida)')
plt.plot(h_com[:split+1], b_com[:split+1], 'r-o', label='Com Entreferro (Subida)')
plt.plot(h_com[split:], b_com[split:], 'r--x', label='Com Entreferro (Descida)')
plt.title('Laço de Histerese $B \\times H$')
plt.xlabel('Intensidade de Campo $H$ (A/m)')
plt.ylabel('Densidade de Fluxo $B$ (T)')
plt.grid(True, linestyle=':')
plt.legend()
plt.savefig('histerese_comparativo.png', dpi=300)

# GRÁFICO 2: Curva de Magnetização (B x H) - Caso Sem Entreferro
plt.figure(figsize=(8, 5))
plt.plot(h_sem[:split+1], b_sem[:split+1], 'k-o', label='Curva de Magnetização')
plt.title('Curva de Magnetização - Sem Entreferro')
plt.xlabel('$H$ (A/m)')
plt.ylabel('$B$ (T)')
plt.grid(True)
plt.legend()
plt.savefig('magnetizacao_sem_gap.png', dpi=300)

# GRÁFICO 3: Permeabilidade (mu x H) - Caso Sem Entreferro
plt.figure(figsize=(8, 5))
plt.plot(h_sem, mu_sem, 'g-s', label='Permeabilidade $\mu$')
plt.title('Curva de Permeabilidade - Sem Entreferro')
plt.xlabel('$H$ (A/m)')
plt.ylabel('$\mu$ (H/m)')
plt.grid(True)
plt.legend()
plt.savefig('permeabilidade_sem_gap.png', dpi=300)

plt.show()
print("Gráficos gerados e salvos com sucesso!")