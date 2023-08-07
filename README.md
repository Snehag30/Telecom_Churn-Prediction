
# Telecom Churn Prediction

For Telco companies it is key to attract new customers and at the same time avoid contract terminations (=churn) to grow their revenue generating base. Looking at churn, different reasons trigger customers to terminate their contracts, for example better price offers, more interesting packages, bad service experiences or change of customers’ personal situations.

Churn analytics provides valuable capabilities to predict customer churn and also define the underlying reasons that drive it. This model is build to detect whether customer is likely to churn or not


## Decision Cycle of Subscriber

![decision cycle]([static/Screenshot%20(200).pngScreenshot (200).png](https://github.com/Snehag30/Telecom_Churn-Prediction/blob/main/static/Screenshot%20(200).png))


## Project Flow


## Data collection


The data set for this classification problem is taken from Kaggle and stems from the IBM sample data set collection  
Dataset can be downloaded from [here](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)


## Exploratory Data Analysis

After data collection, several steps are carried out to explore the data. Goal of this step is to get an understanding of the data structure, conduct initial preprocessing, clean the data, identify patterns and inconsistencies in the data (i.e. skewness, outliers, missing values) and build and validate hypotheses.

### Meaning of Features
By inspecting the columns and their unique values, a general understanding about the features can be build. The features can also be clustered into different categories:

#### Classification labels

Churn — Whether the customer churned or not (Yes or No)
#### Customer services booked

PhoneService — Whether the customer has a phone service (Yes, No)  
MultipleLines — Whether the customer has multiple lines (Yes, No, No phone service)  
InternetService — Customer’s internet service provider (DSL, Fiber optic, No)  
OnlineSecurity — Whether the customer has online security (Yes, No, No internet service)  
OnlineBackup — Whether the customer has online backup (Yes, No, No internet service)  
DeviceProtection — Whether the customer has device protection (Yes, No, No internet service)  
TechSupport — Whether the customer has tech support (Yes, No, No internet service)  
StreamingTV — Whether the customer has streaming TV (Yes, No, No internet service)  
StreamingMovies — Whether the customer has streaming movies (Yes, No, No internet service)  
#### Customer account information

Tenure — Number of months the customer has stayed with the company  
Contract — The contract term of the customer (Month-to-month, One year, Two year)  
PaperlessBilling — Whether the customer has paperless billing (Yes, No)  
PaymentMethod — The customer’s payment method (Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic))  
MonthlyCharges — The amount charged to the customer monthly  
TotalCharges — The total amount charged to the customer  
#### Customers demographic info

customerID — Customer ID  
Gender — Whether the customer is a male or a female  
SeniorCitizen — Whether the customer is a senior citizen or not (1, 0)  
Partner — Whether the customer has a partner or not (Yes, No)  
Dependents — Whether the customer has dependents or not (Yes, No)  
## Modelling

Since this is classification problem, the models that I have implemented are Decision tree, Logistic regression and Random forest. Out of these three models Decision tree had given best score which is about 94%. Hence for now I have selected Decision tree as a final prediction model.  
## Future scope

#### Implementing various other classification models
I have implemented three classification models namely Decision tree, Logistic regression and Random forest. But there are various other classification models such as support vector machine, k nearest neighbor etc Implementing these algorithm and finding best among them can be a future task.

#### Sentiment Analysis on Customer Feedback
Performing sentiment analysis on customer feedback received through surveys or social media to gauge customer satisfaction and identify potential churn signals. Incorporating sentiment scores as input features can enhance the model's ability to capture customer sentiment and churn intentions.


## Frontend

![App Screenshot]([static/Screenshot%20(211).pngScreenshot (211).png](https://github.com/Snehag30/Telecom_Churn-Prediction/blob/main/static/Screenshot%20(211).png))

![App Screenshot]([static/Screenshot%20(212).pngScreenshot (212).png](https://github.com/Snehag30/Telecom_Churn-Prediction/blob/main/static/Screenshot%20(212).png)https://github.com/Snehag30/Telecom_Churn-Prediction/blob/main/static/Screenshot%20(212).png)

![App Screenshot]([static/Screenshot%20(213).pngScreenshot (213).png](https://github.com/Snehag30/Telecom_Churn-Prediction/blob/main/static/Screenshot%20(213).png)https://github.com/Snehag30/Telecom_Churn-Prediction/blob/main/static/Screenshot%20(213).png)
