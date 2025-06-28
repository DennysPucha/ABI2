import numpy as np

# Función propia para correlación de Pearson
def pearson_corr(x, y):
    x = np.array(x)
    y = np.array(y)
    x_mean = x.mean()
    y_mean = y.mean()
    num = np.sum((x - x_mean) * (y - y_mean))
    den = np.sqrt(np.sum((x - x_mean)**2) * np.sum((y - y_mean)**2))
    return num / den if den != 0 else 0

# Simulación de datos
n_traces = 200
n_samples = 20
real_key = 0x2A

plaintexts = np.random.randint(0, 256, size=n_traces) # Generamos 200 trazas de texto plano aleatorias
    
# Simulamos trazas con modelo de peso de Hamming y ruido
traces = np.array([
    np.random.normal(loc=bin(p ^ real_key).count('1'), scale=0.5, size=n_samples)
    for p in plaintexts
])

# Ataque DPA sin scipy
best_corr = -1
best_guess = None

for guess in range(256):
    model = [bin(p ^ guess).count('1') for p in plaintexts]
    avg_trace = np.mean(traces, axis=1)  # Energía promedio de cada traza
    corr = abs(pearson_corr(avg_trace, model))
    if corr > best_corr:
        best_corr = corr
        best_guess = guess

print("Clave estimada:", best_guess)
