# Task_07_Decision_Making  
**OPT Research Task 7 – Ethical Decision Making**  
Author: **Pavithra Ramasamy Pattuselvam**

---

## 📌 What this is
This repo contains my submission for **Research Task 7** under the OPT program.  
The task: take my prior LLM work (Task 5 – Syracuse Women’s Lacrosse 2023 stats) and produce a **stakeholder-facing decision report** with focus on **ethics, reliability, and process documentation**.  

👉 Full report: `report/Task_07_Report.md`

---

## 🗂 Folder structure


---

## 📂 Dataset
- **Source:** Syracuse Women’s Lacrosse – 2023 official stats (PDF).  
- Cleaned into `syracuse_wlax_2023.csv` (1 row per player).  
- Columns: Player, GP, G, A, Pts, Sh, Gw, GB, DC, TO, CT.  
- ⚠️ **Note:** CSV is *not committed* to GitHub (per task rules).  
- See `docs/data_lineage.md` for full details.  

---

## 🛠 Methods
1. Validated key stats in Python/Excel (top scorer, assists, points, GB+DC, CT, shooting efficiency).  
2. Prompted an LLM with factual → intermediate → judgment questions.  
3. Compared LLM answers vs. actual stats.  
4. Documented uncertainty, bias, and ethical considerations.  

---

## 📊 Snapshot Results
| Question | Correct (Dataset) | LLM | Correct? |
|----------|-------------------|-----|----------|
| Top scorer | Megan Carney – 59 | Meaghan Tyrrell | ❌ |
| Most assists | Emma Ward – 56 | Emma Ward | ✅ |
| Most points | Meaghan Tyrrell – 107 | Meaghan Tyrrell | ✅ |
| Most CT | Katie Goodale – 27 | Emma Tyrrell | ❌ |
| Possession (GB+DC) | Olivia Adamson – 114 | Olivia Adamson – 114 | ✅ |
| Shooting eff. | Katelyn Mashewsk – 1.00 | Katelyn Mashewsk – 1.00 | ✅ |

---

## ✅ Recommendations
- **Operational (Low Risk):** Use LLMs for brainstorming/Q&A; validate all results.  
- **Investigatory (Medium):** Pilot LLM workflows for scouting; add more context data (injury logs, fatigue splits).  
- **High Stakes (High):** Do not rely on LLM alone for roster, HR, or legal decisions; human oversight required.  

---

## ⚖️ Ethics & Reliability
- **Bias:** AI favored star offensive players.  
- **Fairness:** Risk of undervaluing non-scoring roles.  
- **Transparency:** Prompts + raw outputs included in repo.  
- **Uncertainty:** Factual Qs accurate ~70%; judgment calls less reliable.  

---

## 🔁 Reproducibility
- Prompts → `prompts/`  
- Outputs → `outputs/`  
- Validation code → `code/validate_stats.py`  
- Data lineage → `docs/data_lineage.md`  

Run locally (after saving cleaned CSV as `syracuse_wlax_2023.csv`):  
```bash
python code/validate_stats.py
