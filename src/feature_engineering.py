import numpy as np
import pandas as pd

DEPTOS = {1:"Chuquisaca",2:"La Paz",3:"Cochabamba",4:"Oruro",5:"Potosí",
          6:"Tarija",7:"Santa Cruz",8:"Beni",9:"Pando"}

def build_targets(df):
    out = df.copy()
    disc_vars = [f"s09a_01{x}" for x in "abcdefghijkl"]
    has_yes = out[disc_vars].eq(1).any(axis=1)
    all_classified = out[disc_vars].isin([1,2]).all(axis=1)
    out["discriminacion_bin"] = np.where(has_yes, 1,
        np.where(all_classified & ~has_yes, 0, np.nan))

    # Etiquetas leídas del SAV: códigos 1-7 = hechos delictivos; 8 = ninguno.
    crime = out[["s09b_02a","s09b_02b"]].isin([1,2,3,4,5,6,7]).any(axis=1)
    no_crime = out["s09b_02a"].eq(8) & (
        out["s09b_02b"].eq(8) | out["s09b_02b"].isna()
    )
    out["victimizacion_bin"] = np.select([crime, no_crime], [1,0], default=np.nan)
    out["departamento"] = pd.to_numeric(out["depto"], errors="coerce").map(DEPTOS)
    out["area_label"] = pd.to_numeric(out["area"], errors="coerce").map({1:"Urbana",2:"Rural"})
    out["sexo_label"] = pd.to_numeric(out["s01a_02"], errors="coerce").map({1:"Hombre",2:"Mujer"})
    out["edad"] = pd.to_numeric(out["s01a_03"], errors="coerce")
    out["ponderador"] = pd.to_numeric(out["ponderador"], errors="coerce")
    return out
