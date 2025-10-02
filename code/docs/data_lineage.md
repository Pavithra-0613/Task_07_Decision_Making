# 📂 Data Lineage – Syracuse Women’s Lacrosse 2023 Stats

📌 **Source**  
- Official Syracuse University Athletics website – Women’s Lacrosse 2023 Season Stats (PDF).  
- Publicly available summary of season-long performance for each player.  

📌 **Cleaning Steps (done in Task 5)**  
1. Downloaded PDF from athletics site.  
2. Extracted the main stats table into Excel → saved as CSV.  
3. Removed header/footer rows and non-player entries.  
4. Reformatted into **one row per player** with columns:  
   - Player, GP (Games Played), G (Goals), A (Assists), Pts (Points), Sh (Shots), Gw (Game-Winning Goals),  
     GB (Ground Balls), DC (Draw Controls), TO (Turnovers), CT (Caused Turnovers).  
5. Saved as `syracuse_wlax_2023.csv`.  

📌 **Usage in Repo**  
- The file is **not uploaded to GitHub** (per research instructions).  
- To reproduce:  
  - Download the same stats PDF from the official SU site.  
  - Clean → save as `syracuse_wlax_2023.csv`.  
  - Place the CSV in the same folder as `code/validate_stats.py`.  
  - Run the script.  

📌 **Limitations**  
- Season totals only (no minutes, injuries, advanced splits).  
- Two added calculated fields:  
  - **Shooting Efficiency = Goals ÷ Shots**  
  - **Possession Impact = GB + DC**  

✅ This ensures anyone can reproduce results without sharing the raw CSV.
