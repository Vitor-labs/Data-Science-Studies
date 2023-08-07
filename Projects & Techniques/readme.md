# Life Cycle of a Data Science Project

see:
- [**CRISP-DM**](#)
- [**CRISP-ML(Q)**](#crisp-mlq)

</br>

# <center> CRISP-DM </center>

Following the CRISP-DM (Cross Industry Standard Process for Data Mining) framework, that consists of a set of good practices (aka methodology) to execute a project in Data Science.

The CRISP-DM methodology consists of six main phases:

1. ## Business Understanding:
    This initial phase involves understanding the project objectives, requirements, and business goals. It aims to clarify the specific problems that need to be solved and how data mining can contribute to achieving those goals.

2. ## Data Understanding:
    now, data scientists gather and explore the available data to gain insights into its structure, quality, and potential usefulness for the project. This step helps in identifying data issues and deciding which data is relevant for the analysis.

3. ## Data Preparation:
    This phase focuses on data cleaning, transformation, and integration. Data scientists perform tasks like handling missing values, encoding categorical variables, and creating derived features to ensure that the data is ready for modeling.

4. ## Modeling:
    The modeling phase is where data scientists apply various data mining techniques to build and evaluate predictive or descriptive models. Different algorithms are tested and tuned to identify the most suitable one for the problem at hand.

5. ## Evaluation:
    here, the performance of the models is assessed using validation techniques such as cross-validation or hold-out samples. The goal is to select the best-performing model that meets the project's requirements.

6. ## Deployment:
    The final phase involves deploying the chosen model into the production environment, making it available for end-users to make predictions or decisions. It also includes documenting the process and results to facilitate future maintenance and improvements.

The CRISP-DM metodology is focused on Data Mining projects

## **Data Mining** :  
The action of process data to gain patterns, and to gain knowledge on that pattern. In the process of data mining, large data sets are first sorted, then patterns are identified and relationships are established to perform data analysis and solve problems.

* Data Mining is divided in some areas:

  <center> <img src="./../Assets/data-mining.drawio.svg"/> </center>

</br>

# <center> CRISP-ML(Q)</center>

for the specific development of machine learning applications, an evolution of the methodology was made, the CRISP-ML(Q) framework. Stands for Cross Industry Standard Process for Machine Learning with Quality assurance. 

<center> <img src="./../Assets/CRISP-ML-removebg-preview.png"/> </center>
CRISP-ML(Q) is implemented with 6 stages as follows:

1. ## Business and Data Understanding
    The applications starts with identifying the scope of the ML application, the success criteria, a data quality verification and the feasibility of the project before setting him up. Defining clear and measurable Key Performance Indicators (KPI) is required.

    - A helpful approach is to define a non-ML heuristic benchmark to communicate the impact of machine learning tasks with the business stakeholders.

    - Applying the Machine Learning Canvas framework would be a structured way to perform this task.
   
    Therefore, one crucial requirement is the documentation of the statistical properties of data and the data generating process. Similarly, data requirements should be stated and documented as well.

2. ## Data Preparation
    The Data Engineering phase, here, data selection, data cleaning, feature engineering, and data standardization tasks are performed.

    We identify valuable and necessary features that do satisfy data quality requirements for future model training by using either filter methods, wrapper methods, or embedded methods for data selection. 
      
      - At this point, we also might tackle the problem of unbalanced classes by applying over-sampling or under-sampling strategies.

      - Add unit testing for data cleaning to mitigate the risk of error propagation to the next phase. 
      
      - Depending on the machine learning task, we might need to perform feature engineering and data augmentation activities. 

      - the normalization task will mitigate the risk of bias to features on larger scales. 

3. ## Model Building and Tuning
    The Model Engineering. Generally, the modeling phase includes model selection, specialization and training tasks. Additionally, depending on the application, we might use a pre-trained model, compress the model, or apply ensemble learning methods.

    Ensure that the method and the results of the modeling phase are reproducible by collecting the model training method’s metadata, like: algorithm, training, validation and testing data set, hyper-parameters, and runtime environment description. The result reproducibility assumes the validation of the model’s mean performance on different random seeds. A helpful framework here is the “Model Cards Toolkit”.

    Finally, we package the ML workflow in a pipeline to create repeatable model training during the modeling phase.

4. ## Evaluation
    Here, the performance of the trained model needs to be validated on a test set. Additionally, the model robustness should be assessed using noisy or wrong input data. Furthermore, it is best practice to develop an explainable ML model to provide trust, meet regulatory requirements, and govern humans in ML-assisted decisions.

    Finally, the model deployment decision should be met automatically based on success criteria or manually by domain and ML experts. All outcomes of the evaluation phase need to be documented.

5. ## Model Deployment
    The ML model deployment denotes a process of the ML model integration into the existing software system. Deployment approaches are specified during the first phase of the ML development life cycle. These approaches will differ depending on the use case and the training and prediction modus, either batch or online.

    The ML model deployment includes the following tasks: inference hardware definition, model evaluation in a production environment, providing user acceptance and usability testing, providing a fall-back plan for model outages, and setting up the deployment strategy to roll out the new model gradually.


6. ## Monitoring and Maintenance 
    When an ML model performs on real-world data, the main risk is the “model staleness” effect when the performance of the ML model drops as it starts operating on unseen data.

    Model performance is affected by hardware performance and the existing software stack. For this, perform the monitoring task when the model performance is continuously evaluated to decide whether the model needs to be re-trained. This is known as the Continued Model Evaluation pattern. The decision from the monitoring task leads to the second task - updating the ML model.

    Additionally to monitoring and re-training, reflecting on the business use case and the ML task might be valuable for adjusting the ML process.

And for each phase the quality assurance approach in CRISP-ML(Q) requires the definition of requirements and constraints, instantiation of the specific tasks, specification of risks that might negatively impact the efficiency and success of the ML application, quality assurance methods to mitigate risks when these risks need to be diminished. As Following:

<center> <img src="./../Assets/quality.drawio.svg"/> </center>

The following table sumarizes the CRISP-ML(Q) core phases and the corresponding tasks:

| Phase | Tasks |
|-------|-------|
| Business and Data Understanding | - Define business objectives - Translate business objectives into ML objectives - Collect and verify data - Assess the project feasibility - Create POC |
| Data Engineering | - Feature selection - Data selection - Class balancing - Cleaning data (noise reduction, data imputation) - Feature engineering (data construction) - Data augmentation - Data standartization |
|ML Model Engineering | - Define quality measure of the model - ML algorithm selection (baseline selection) - Adding domain knowledge to specialize the model - Model training - Optional: applying trainsfer learning (using pre-trained models) - Model compression - Ensemble learning - Documenting the ML model and experiments |
| ML Model Evaluation |	- Validate model's performance - Determine robustess - Increase model's explainability - Make a decision whether to deploy the model - Document the evaluation phase |
| Model Deployment | - Evaluate model under production condition - Assure user acceptance and usability - Model governance - Deploy according to the selected strategy (A/B testing, multi-armed bandits) |
| Model Monitoring and Maintenance | - Monitor the efficiency and efficacy of the model prediction serving - Compare to the previously specified success criteria (thresholds) - Retrain model if required - Collect new data - Perform labelling of the new data points - Repeat tasks from the *Model Engineering* and *Model Evaluation* phases - Continuous, integration, training, and deployment of the model |