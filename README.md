**StarX** 

[MyGit Repository](https://mygit.th-deg.de/mb04502/StarX)

[Link to Wiki](https://mygit.th-deg.de/mb04502/StarX/-/wikis/home)

# Project Description
StarX is a data-driven application designed to analyze and provide clear insights into car prices in India. Using a detailed dataset covering a wide range of vehicles, it helps users understand pricing trends, identify key factors that influence car prices, and make informed decisions. The application also offers personalized pricing recommendations, ensuring users have the right information to evaluate and compare options effectively.

# Project Installation and Running

Follow these steps to set up and run the StarX application. Make sure to have the correct versions of Python and Streamlit installed. We assume you have git installed already.

- It is recommended to use a bash shell or Linux shell for the project.

1. Clone the repository:  
   `git clone https://mygit.th-deg.de/mb04502/StarX`

2. Navigate to the project folder:  
   `cd starx`

3. Create a virtual environment

   - On Windows:
      `python -m venv .venv`
   - On macOS/Linux: 
      `python3 -m venv .venv`

4. Activate the virtual environment:  
   - On Windows:  
     `.venv\Scripts\activate`
   - On macOS/Linux:  
     `source .venv/bin/activate`

5. Install dependencies:  
   `pip install -r requirements.txt`

6. Start the app:  
   `streamlit run main.py`

Versions used are:
   - Python - 3.9.6
   - Streamlit - 1.41.1
   - scikit-learn - 1.6.1
   - pandas - 2.2.3
   - matplotlib - 3.9.4
   - seaborn - 0.13.2


# Project Data

The dataset used in this project is sourced from [Kaggle](https://www.kaggle.com/datasets/abhikalpsrivastava15/quikr-cars-dataset). It provides information about used cars available for sale in India, with the following features:

- **Name**: The model name of the car.
- **Label**: The car's classification (e.g., "PLATINUM").
- **Location**: The city where the car is listed for sale.
- **Price**: The listed price of the car in Indian Rupees.
- **Kms_driven**: The total kilometers the car has been driven.
- **Fuel_type**: The type of fuel the car uses (e.g., Petrol, Diesel).
- **Owner**: The ownership status (e.g., 1st Owner, 2nd Owner).
- **Year**: The manufacturing year of the car.
- **Company**: The car manufacturer (e.g., Ford, Maruti, Hyundai).

This dataset is used to analyze trends in used car pricing and identify factors that influence the price, such as brand, manufacturing year, fuel type, and more.

### Outlier Removal
Outliers were removed using the **Quantile Method**:
- **Kms_driven**: Rows above the 99th percentile were removed to exclude excessively high mileage.
- **Price**: Rows above the 98th percentile were removed to avoid skewness from overly expensive cars.

### Handling Missing Data
Missing values were filled with column means to ensure consistency.

### Synthetic Data Generation
Fake rows were added using random values within the original data's min and max range, ensuring realism and balance.


# Basic Usage
To start the project, first ensure that all the required dependencies are installed. You can do this by running the following command:

   `pip install -r requirements.txt`

Once the environment is set up, you can run the project using the following command:

   `streamlit run main.py`

   
## Key Use Cases
- **Data Analysis**: Analyze car prices, kilometers driven, and other factors affecting the price.
- **Visualizations**: View graphical representations of the data, such as price distribution and mileage vs. price.
- **Data Cleaning**: Remove outliers based on statistical analysis and visual inspections.
- **Car Recommendation**: Recommend a car based on user input, such as budget, fuel type, and location.


# Implementation of the Requests
StarX implements the requests as follows

1. _A multi-page Web App with Streamlit (https://streamlit.io) has to be developed._
   - StarX consists of 9 pages, all pages have to be run in the correct order since they depend on the actions from the previous page

2. _For source code and documentation, a MyGit repository and Wiki has to be used._
   - MyGit repository and Wiki have been used, see links at the top of this README file.

3. _Develop and describe 3 Personas in the Wiki._
   - 3 Personas have been developed. See Wiki section Personas.

      [Link to Personas](https://mygit.th-deg.de/mb04502/StarX/-/wikis/3.-Personas)

4. _Find 5 use cases for the application._
   - 5 Use cases were described. See Wiki under section Use Cases.

      [Link to Use Cases](https://mygit.th-deg.de/mb04502/StarX/-/wikis/4.-Use-Cases)

5. _A requirements.txt file must be used to list the used Python modules, which can be used to install them._
   - A requirements.txt file is created and can be found in the root directory of the Project.

6. _A README.md file must be created with the structure described in part 01._
   - README.md has been used and it is the file open currently. It is also located in the root directory of the Project.

7. _The module venv for a virtual project environment must be used._
   - venv is used and it has been described in the 'Project Installation and running' section of this README file.

8. _A free data source must be used. You may find it for example at Kaggle, SciKit (but not the built-in
ones), or other._
   - Kaggle was used to find the dataset for this project. More information is described in the Wiki under the Data section.

      [Link to Data](https://mygit.th-deg.de/mb04502/StarX/-/wikis/2.-Data)

9. _There must be a data import (predefined format and content of CSV)._
   - Data is imported when the main.py file is run. This is then stored in a session state and then used by the other pages.

10. _The data must be analyzed in the app (e.g. with Pandas, a Jupyter notebook must not be submitted), so that an app user gets on overview (e.g. of correlations, min/max, median, …). The result must be visualized in the app._
      - The data is analysed and an overview is given to the user in Page 1 after which the Data is transformed in Page 2, then the correlations, min/max and other metrics are descibed in the Data Transformation tab. For more information see "Data Statistics" and "Data Transformation" tab after running the app. 

11. _The data must be described in a Wiki section. The description must include the feature variables, their values incl. basic statistics like min/max, transformation (if done) and a description of the target variable._
      - The Data is described in Wiki, the link to the Data Section in the Wiki is [here](https://mygit.th-deg.de/mb04502/StarX/-/wikis/2.-Data).


12. _Identify and update outliers, if some exists. Explain your approach in the data chapter of the Wiki._
      - Outlers were found in the data by plotting graphs of the Data, these were removed by Quantile-based-approach, more information is under the Data section in the Wiki.

13. _The data must be transformed so that it can be used in the app. Follow the descriptions in https://developers.google.com/machine-learning/crash-course/numerical-data and following chapters about data._
      - The None-numeric values were transformed to numeric depending on how frequent the value appeared, more information is under the Data section in the Wiki.

14. _Add 25-50% realistic fake data sets. What is the effect to the training of the model? Explain you approach for generating the fake data and its influence on the model in the data chapter of the Wiki._
      - Realistic fake data was added, this resulted into a higher mean squared error (MSE). The approach used was by using a uniformly distributed random varible that would return a number between the minimum and maximum of that column. The impact has been described in the Wiki.

15. _Create several input widgets (at least 3, where 2 must be different) that change some feature variables._  
   - The input widgets were used in the **Model Training** tab of the project. The code for this can be found under `pages/07_Model_Training.py`. The input widgets used include:
     - **Slider**: Allows users to set a range of values for Years and Kms_Driven features.  
     - **Selectbox**: Provides a dropdown menu to select from predefined categories. This was used for Location and Company variables.  
     - **Radio Buttons**: Enables selection of a single option from a set of choices. This was used for Fuel Type variable.

16. _At least 2 Scikit-Learn model training algorithms (e.g. from Aurélien Géron, Chapter 4) must be applied in order to predict some variable(s). Argue in the Wiki about which one is best suited for the app._
      - 3 Scikit-Learn models were used, these are Linear Regression, Lasso Regression and Ridge Regression. All of these were applied to both the Original Processed data and the Fake Augmented Data and 6 models in total were trained.

17. _Select at least two use cases for which the “right fit” question for chatbots has a positive answer. Argue about why using a chatbot for the feature makes sense and write this in the Wiki._
      - The two use cases for the cases for which the chatbot works are:
         - **Price Prediction for Budget-Friendly Car**: Rahul Sharma asks the system that they want to have the price of a car predicted, the system takes the input and gives a prediction.
         - **Finding the Best Deal for Car Upgrade**: Priya Singh asks the chatbot for help with the best deal, the chatbot asks her the price range and gives her the best deals in that range.

18. _Create a system persona for the chatbot and document it in the Wiki._
   - The System Persona for the chatbot is **Ankit Verma**, the lead developer of the StarX app. He embodies the app's mission of providing a seamless and data-driven user experience. Ankit's detailed background, motivations, and contributions can be found in the [Personas](https://mygit.th-deg.de/mb04502/StarX/-/wikis/3.-Personas) section of the project's Wiki.  


19. _Create at least 3 sample dialogs for each use case you select for the chatbot. Document them in the Wiki._
      - Three sample dialogs were added for each use case. This can be found under the section of  ChatBot Dialog Flow in the Wiki.

20. _Create a high-level (dialog) flow for the use cases. Also document it in the Wiki._
      - High level dialog flow was made and has been described in the wiki under the [ChatBot Dialog Flow](https://mygit.th-deg.de/mb04502/StarX/-/wikis/6.-ChatBot-Dialog-Flow). It shows dialog flow for 2 use cases.

21. _Create a rasa chat bot that must be included for the use cases. Add the source files to the MyGit repository._
      - An alternative for rasa is used, it performs the same tasks but with less compatibility issues. The Chatbot was implemented by keyword spotting techniques and implements 2 of the use cases.

22. _Create a video/screencast of your project. The video must show at least 3 use cases, one of them with the rasa chatbot. The video must be uploaded to the MyGit repository._
      - A video of the project has been recorded and the link to the video has been added in the Wiki in the home page.


# Work done
| Request Number | By Both   | Muhammad Ahtisham Bhatti | Love |
|----------------|-----------|--------------------------|------|
| 1              |     ✔     |                          |      |
| 2              |     ✔     |                          |      |
| 3              |           |             ✔            |      |
| 4              |           |             ✔            |      |
| 5              |           |             ✔            |      |
| 6              |           |                          |  ✔   |
| 7              |           |                          |  ✔   |
| 8              |           |             ✔            |      |
| 9              |           |                          |  ✔   |
| 10             |           |             ✔            |      |
| 11             |           |                          |  ✔   |
| 12             |           |             ✔            |      |
| 13             |           |                          |  ✔   |
| 14             |           |                          |  ✔   |
| 15             |           |             ✔            |      |
| 16             |           |                          |  ✔   |
| 17             |     ✔     |                          |      |
| 18             |           |             ✔            |      |
| 19             |           |                          |  ✔   |
| 20             |           |                          |  ✔   |
| 21             |           |             ✔            |      |
| 22             |     ✔     |                          |      |
