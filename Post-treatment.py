import pandas as pd

# Charger les données du fichier CSV
df = pd.read_csv("positions.csv")

# Calculer la vitesse moyenne de la raquette
vitesse = (df["x"].diff() ** 2 + df["y"].diff() ** 2).apply(lambda x: x ** 0.5).mean()

# Extrapoler la position de la raquette dans les images manquantes
for i in range(1, len(df)):
    if pd.isna(df.loc[i, "x"]):
        temps_ecoule = df.loc[i, "temps"] - df.loc[i-1, "temps"]
        distance_parcourue = temps_ecoule * vitesse
        angle = pd.np.arctan2(df.loc[i-1, "y"] - df.loc[i-2, "y"], df.loc[i-1, "x"] - df.loc[i-2, "x"])
        x_nouveau = df.loc[i-1, "x"] + distance_parcourue * pd.np.cos(angle)
        y_nouveau = df.loc[i-1, "y"] + distance_parcourue * pd.np.sin(angle)
        df.loc[i, "x"] = x_nouveau
        df.loc[i, "y"] = y_nouveau

# Sauvegarder les positions extrapolées dans un nouveau fichier CSV
df.to_csv("positions_extrapolees.csv", index=False)
