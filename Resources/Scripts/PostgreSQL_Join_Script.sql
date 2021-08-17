-- Create table contains individual scores for each symptoms --
CREATE TABLE symptom_scores(
	Patient_Id VARCHAR(100),
	Age VARCHAR(100), 
	Gender VARCHAR(100),
	Air_Pollution VARCHAR(100), 
	Alcohol_use VARCHAR(100),
	Dust_Allergy VARCHAR(100), 
	OccuPational_Hazards VARCHAR(100), 
	Genetic_Risk VARCHAR(100), 
	chronic_Lung_Disease VARCHAR(100), 
	Balanced_Diet VARCHAR(100), 
	Obesity VARCHAR(100), 
	Smoking VARCHAR(100), 
	Passive_Smoker VARCHAR(100), 
	Chest_Pain VARCHAR(100), 
	Coughing_of_Blood VARCHAR(100), 
	Fatigue VARCHAR(100), 
	Weight_Loss VARCHAR(100), 
	Shortness_of_Breath VARCHAR(100), 
	Wheezing VARCHAR(100), 
	Swallowing_Difficulty VARCHAR(100), 
	Clubbing_of_Finger_Nails VARCHAR(100), 
	Frequent_Cold VARCHAR(100), 
	Dry_Cough VARCHAR(100), 
	Snoring VARCHAR(100)
);

-- Create table contains patient level and average scores --
CREATE TABLE level_avg_scores(
	Patient_Id VARCHAR(100),
	level VARCHAR(100),
	Score VARCHAR(100)
);

-- Remove unwanted row --
SELECT * FROM symptom_scores;
DELETE FROM symptom_scores WHERE age = 'age';
SELECT * FROM level_avg_scores;
DELETE FROM level_avg_scores WHERE score = 'Score';

-- Rename Column name --
ALTER TABLE level_avg_scores 
RENAME COLUMN patient_id TO patient_id_level;

-- Join 2 tables -- 
SELECT *
INTO all_patient_data
FROM symptom_scores
LEFT JOIN level_avg_scores ON (symptom_scores.patient_id = level_avg_scores.patient_id_level);

-- Visualise new table -- 
SELECT * FROM all_patient_data;

-- Drop duplicate patient_id -- 
ALTER TABLE all_patient_data
DROP COLUMN patient_id_level;

-- Visualise new table -- 
SELECT * FROM all_patient_data;
