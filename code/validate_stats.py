import pandas as pd

# Load dataset (make sure you have the CSV in the right path locally)
# For GitHub, just describe where it comes from instead of uploading raw data.
# Example: "syracuse_wlax_2023.csv"
file_path = "syracuse_wlax_2023.csv"  

try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print("⚠️ CSV file not found. Please download the Syracuse WLAX 2023 stats and place it in the same folder as this script.")
    exit()

# ---- Validation Calculations ----
# Top scorer
top_scorer = df.loc[df['G'].idxmax(), ['Player', 'G']]

# Most assists
top_assists = df.loc[df['A'].idxmax(), ['Player', 'A']]

# Most points
top_points = df.loc[df['Pts'].idxmax(), ['Player', 'Pts']]

# Possession leader (GB + DC)
df['Possession'] = df['GB'] + df['DC']
top_possession = df.loc[df['Possession'].idxmax(), ['Player', 'Possession']]

# Most caused turnovers
top_ct = df.loc[df['CT'].idxmax(), ['Player', 'CT']]

# Shooting efficiency (Goals/Shots)
df['ShotEff'] = df['G'] / df['Sh']
top_eff = df.loc[df['ShotEff'].idxmax(), ['Player', 'ShotEff']]

# ---- Print results ----
print("✅ Validation Results from Syracuse WLAX 2023 Stats")
print(f"Top Scorer: {top_scorer['Player']} – {top_scorer['G']} goals")
print(f"Most Assists: {top_assists['Player']} – {top_assists['A']} assists")
print(f"Most Points: {top_points['Player']} – {top_points['Pts']} points")
print(f"Possession Leader: {top_possession['Player']} – {top_possession['Possession']} (GB+DC)")
print(f"Most Caused Turnovers: {top_ct['Player']} – {top_ct['CT']}")
print(f"Highest Shooting Efficiency: {top_eff['Player']} – {top_eff['ShotEff']:.2f}")
