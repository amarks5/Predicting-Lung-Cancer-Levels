# Predicting_Lung_Cancer_Levels

## Work Breakdown by Team Member
Presentation: Alexis Marks, Jesse Singh, Laurencio Leyva

Github Setup: Alexis Marks, Jesse Singh

Machine Learning Model: Ali Ahrabi, Laurencio Leyva

Database: 
  - Doris Tai - Exploaratory Data Analysis, SQL schema and SQL scripts.
  - Laurencio Leyva - Exploratory Data Analysis and import to SQL database.

Dashboard: 
  - Alexis Marks - Visualizations for Symptoms vs. Level of Cancer, Gender vs. Level of Cancer, and Lifestyle Choices vs. Level of Cancer.   
  - Jesse Singh - Visualizations for Symptoms vs. Level of Cancer and Lifestyle vs. Level of Cancer. 

## Resources
  - Data: [Link to Dataset](https://www.kaggle.com/rishidamarla/cancer-patients-data) 
  - Description of Data Source: This dataset was sourced from Kaggle, a community forum of datasets. It shows the demographic and lifestyle data of 100 lung cancer patients.

## Tools
  - Tableau
  - Supervised Machine Learning
  - SelectKBest from sklearn.feature_selection
  - train_test_split from sklearn.model_selection
  - StandardScaler from sklearn.preprocessing
  - Machine Learning Model Building
    1. Suppor vector Classifier
    2. Logistic Regression
    3. Decision Tree Classifier
  
## Grid Search
  - Grid search incorporates the entire data set and was used to tune our ML model. The accuracy of this tuning method was optimized by the confusion matrix, classification report and cross-validation.
  - Confusion matrix gives the value of true positive and false negative which helped to predict how much our model is optimized to predict.
  - Classification report was used as a performance evaluation metric for the quality of our models' predictions.
  - Cross-validation was used to evaluate the ML model through a limited data sample. 
  - Saving model for deployment by using pickle

## Topic
The susceptibility to lung cancer based on the following 24 lifestyle and demographic variables: age, gender, air pollution, alcohol use, dust allergy, occupational hazards, genetic risk, chronic lung disease, balanced diet, obesity, smoking, passive smoker, chest pain, coughing of blood, fatigue, weight loss, shortness of breath, wheezing, swallowing difficulty, clubbing of fingernails, frequent cold, dry cough, and snoring.  

## Reason For Topic
The ability to predict and determine the level of lung cancer of a patient will add significant clinical value for the development of therapies to treat and diagnose the disease. 

## Questions to Answer
Which aspects of a person's lifestyle would make them most susceptible to lung cancer? We analyzed the data of 1000 lung cancer patients with respect to different parameters such as their age, gender, alcohol use, genetic risk, and smoking. The purpose is to predict which lifestyle choices would lead to lung cancer.

## Results of Analysis
- Chest pain and coughing of blood were the most prevalent symptoms among patients with high level lung cancer.
- A combination of alcohol abuse, bad diet, occupational hazards, and smoking were the most prevalent lifestyle attributes of patients with high level lung cancer.
- Created a model that can be used to accurately predict cancer susceptibility based on a patient's lifestyle and symptom information.

## Recommendations for Future Analysis
- Limited dataset. As more data is introduced, the model might have to be reevaluated.
- Change scale to 0-5 instead of 0-10.

## Anything Team Would Have Done Differently
- Try to make age and gender more relevant factors to make our model more useful.

## Google Slide Presentation
[Link to Google Slides](https://docs.google.com/presentation/d/1guxs3ptq4deP423Sn5jP52Q2Tn-MhQibTpFD0THmf88/edit?usp=sharing)

[Link to Dashboard](https://public.tableau.com/app/profile/jasmeet.singh8085/viz/FinalProjectWorkbook_16292377158690/SymptomsLifestlyevs_Level?publish=yes)

[Link to Heroku](https://cancer-project-5.herokuapp.com/)
* Storyboard on Google Slides
