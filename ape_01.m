tabela = readtable('dados.xlsx');

x = tabela.Var1; 
y = tabela.Var2; 

x_reta = linspace(min(x),max(x),100);
ang = -133.055*10^-6; 
b = 997.9*10^-3;

y_reta = b + ang*x_reta;


plot(x,y); 
hold on 
plot(x_reta,y_reta,'g--', 'LineWidth', 2)
xlabel('Intensidade de Campo (H)')
ylabel('Densidade de Fluxo (B) [T]')