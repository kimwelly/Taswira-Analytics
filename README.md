Taswira Plane Finder

AI-assisted fetal ultrasound plane finding in novice blind sweeps. Moringa School capstone · Group 11 · Taswira Analytics · November 2026

A lightweight model that watches a short ultrasound sweep (about 200 pictures) taken by a midwife with little training, finds the key views of the baby (head, tummy, heart, spine, thigh bone), keeps the best pictures for a specialist and answers "Good scan" or "Please scan again". Exploratory extras: a breech flag and a brain defect screening step with safe, non-diagnostic messages.

Study prototype only. It is not a medical device, does not diagnose and has not been clinically validated.

Repository
File	What it is
taswira_final_short_results.ipynb	Main notebook, run end to end, with results and conclusions
README.md	This file
Data (not included; download separately)
Dataset	Use	Link
NatalIA PBF-US1 (dummy-belly blind sweeps)	Training and main test	Zenodo
FETAL_PLANES_DB (Spain)	Real images added to training	Zenodo
African fetal planes (5 countries)	Real-scan test only	Zenodo
Fetal Brain Abnormalities Ultrasound	Defect screening demo	Roboflow

Place the datasets next to the notebook:

NatalIA PBFUS1/
FETAL_PLANES_DB/FETAL_PLANES_DB_data.csv  (+ images)
African_planes/Zenodo_dataset/African_planes_database.csv  (+ images)
Fetal Brain Abnormalities Ultrasound.v1i.multiclass.zip
taswira_final_short_results.ipynb
How to run
bash
pip install tensorflow==2.15 scikit-learn pandas numpy matplotlib seaborn pillow ipywidgets
jupyter notebook taswira_final_short_results.ipynb

Run all cells. Image features are computed once and cached, so later runs are fast.

Method in brief

Clean and crop each picture → extract features with frozen EfficientNet-B0 and MobileNetV2 → logistic regression with hard-negative mining → 5-fold cross-validation grouped by sweep → sweep-level decision (best 5 frames + rescan advice) → export to TFLite.

Key results
Question	Result
Finds key views in dummy sweeps (plane macro-F1)	0.39 (target 0.70)
Good picture in the top 5	77 of 100 views
Scan-again advice (good sweeps passed / empty caught)	83 / 47 in 100
Right view on real African scans: dummy only → with Spanish images	21 → 80 in 100
Phone-ready model size	7.1 MB
Breech flag accuracy (dummy)	82 in 100 (guessing: 54)
Brain defect check: own dataset / normal African heads flagged	AUC 1.00 / 25% false alarms

Main finding: practice data from a dummy belly alone does not carry over to real scans; adding real images is essential.

Limitations

One dummy belly at 23 weeks with one probe; targets not met; no Kenyan data or real midwife sweeps; defect data unverified and not transferable; breech flag is feasibility only. See section 11 and the appendix of the notebook.

Next steps

Kenyan data (AIMIX), real midwife sweeps, fine-tuning, phone testing and clinical validation.
