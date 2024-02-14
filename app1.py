from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir "main.css"
resume_file = current_dir "CV.pdf"
profile_pic = current_dir "profile-pic.png"

# --- GENERAL SETTINGS ---

PAGE_TITLE = "Interactive Digital CV | Sumedha Arya"
PAGE_ICON = ":wave:"
NAME = "Sumedha Arya"
DESCRIPTION = """
Analytics manager | M.A. Economics
"""
EMAIL = "aryasumedha06@gmail.com"
CONTACT = "+91 9871968308"
LinkedIn = {
        "LinkedIn": "https://linkedin.com",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, initial_sidebar_state="expanded")

tab1, tab2 ,tab3, tab4 = st.tabs(["Introduction","Experience Summary","Work Experience and Qualification","Projects"])



# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
    profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.image(profile_pic, width=230)
        st.write("""Python Projects video link:https://youtu.be/Cub8LAowPHc?si=T3ylZZ2I9eOv_vPg""")

    with col2:
        
        PAGE_TITLE = "Interactive Digital CV | Sumedha Arya"
        PAGE_ICON = ":wave:"
        NAME = "Sumedha Arya"
        DESCRIPTION = """
Analytics manager
"""
        EMAIL = "aryasumedha06@gmail.com"
        CONTACT = "+91 9871968308"
        LinkedIn = {
        "LinkedIn": "https://linkedin.com",
}
        
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
    )
        st.write("📱", CONTACT)
        st.write("📧", EMAIL)

# --- HERO SECTION ---
with tab1:
    col3, col4 = st.columns(2)
    with col3:
        st.write('\n')
        st.subheader("CORE COMPETENCIES")
        st.write(
    """
    ✔️	Data Analytics\n
    ✔️  Machine Learning models\n
    ✔️  Statistical models\n
    ✔️	Campaign Analytics\n
    ✔️  Exposure to GCP, AWS\n 
    ✔️	Worked for BFSI clients\n
    ✔️	Automation\n
    ✔️	Model development and deployment\n
    ✔️	Strategic business decisions\n
    ✔️	Pre and Post Campaign Analytics\n
    ✔️  End-to-End ML Pipeline\n
    ✔️  Credit Card Fraud Detection\n
    ✔️	Multi-touch Attribution Modelling\n
    ✔️  Insurance Pricing Forecast\n
    ✔️  Build an ETL Pipeline for Financial Data Analytics on GCP\n
    ✔️	SQL, Python\n
    ✔️	Training & Development\n
    ✔️	Project Management using Wrike, JIRA, Hive\n

    """
)

with col4:
    st.write('\n')
    st.subheader("Profile Summary")
    st.write(":open_book:" 
"""
<span style='color:Black'>
Dynamic and results-driven analytics professional with 6.5 years of experience, seeking a challenging position in a fast-paced, dynamic organization to apply my skills in translating business problems into quantitative approaches,as well as in using statistical and mathematical techniques to gather information and draw conclusions. 
\n
:open_book: <span style='color:Black'>
Experienced in Data Science, MLops, and Decision Sciences, I develop and implement end-to-end data-driven solutions, from model building and data preprocessing to deployment and monitoring, to use agile methodology automation approaches to tackle challenging business problems. I strive to offer workable answers to challenging business issues like growing the business, improving client relations and operational efficiency, while minimizing risk. 
\n
:open_book: <span style='color:Black'>
Expertise in developing models through the use of both supervised and unsupervised machine learning methods. Clearly articulating when collaborating with stakeholders, developing road maps, and implementing agile methods. Assisted in the hiring and training procedures necessary for a streamlined onboarding of new hires and projects.</span> 
\n
:open_book: <span style='color:Black'>
Possess a diverse professional background spanning across multiple industries including apparel, healthcare, banking, e-commerce, and IT; successfully applied analytics methodologies and insights to cater to the unique challenges of each industry, and brought fresh perspectives to various analytical projects.</span>""", unsafe_allow_html=True

)

with tab2: 
    st.write('\n')
    st.subheader("Experience Summary")
    st.write("""

<span style='color:Purple'>📊 **Data Science and Machine Learning:**</span> <span style='color:Black'>Proficient in developing and deploying machine learning models for various applications including credit card fraud detection, customer segmentation, customer churn prediction, insurance pricing forecast, working capital optimization, sentiment analysis, multi-touch attribution model etc. Experienced in utilizing a wide range of machine learning algorithms such as regression classification, clustering, and ensemble methods. (multiple linear regresion - Ridge, Lasso, logistic regression, Decision Tree ,Random Forest ,Support Vactor Machines, Adaboost, Gradient Boosting ,Naive Bayes, Knn, clustering techniques, dimensionality reduction).</span>

<span style='color:Purple'>🌍 **MLops and Model Deployment:**</span> <span style='color:Black'>Skilled in building MLops pipelines and automated model deployment systems to streamline the model development and deployment process. Proficient in implementing continuous integration/continuous deployment (CI/CD) pipelines, monitoring tools, and logging solutions to ensure the reliability and scalability of deployed models.</span>

<span style='color:Purple'>📈 **Predictive Analytics and Forecasting:**</span> <span style='color:Black'>Experienced in utilizing predictive analytics techniques and time-series forecasting models to optimize business processes, forecast demand, and identify trends. Skilled in analyzing historical data, identifying patterns, and deriving actionable insights to support data-driven decision-making.</span>

<span style='color:Purple'>💹 **Sentiment Analysis and NLP:**</span> <span style='color:Black'>Proficient in conducting sentiment analysis and natural language processing (NLP) to extract valuable insights from text data. Experienced in analyzing social media data, customer feedback, and internal communications to gauge sentiment, identify trends, and support brand reputation management.</span>

<span style='color:Purple'>📉 **Data Visualization and Dashboarding:**</span> <span style='color:Black'>Skilled in creating and automating interactive data visualizations and dashboards using tools such as Big Query, LookerStudio, Tableau, and python. Experienced in translating complex analytical findings into intuitive visualizations and actionable insights for stakeholders at all levels of the organization.</span>

<span style='color:Purple'>🏆 **Leadership and Team Collaboration:**</span> <span style='color:Black'>Strong leadership abilities with a proven track record of leading cross-functional teams and driving successful project outcomes. Experienced in collaborating effectively with business stakeholders, IT teams, and other functional groups to define project requirements, prioritize initiatives, and deliver solutions that meet business objectives.</span>

"""
,unsafe_allow_html=True)

# --- EXPERIENCE & QUALIFICATIONS ---
with tab3:

# --- WORK HISTORY ---
    st.write('\n')
    st.subheader("WORK EXPERIENCE")
    st.write("---")

# --- JOB 0
    st.write("🚧", "**Analytics Manager | EssenceMediacom (Group M/WPP) **")
    st.write("09/2021 - Present")
    st.write(
    """
Key Result Areas:
•	Spearheading a dynamic team, orchestrating the streamlining of campaign analytics through multi-phase process automation; ensuring successful execution of agile methodology automation initiatives across various critical data pipelines\n
•	Leveraging a robust toolkit encompassing SQL, Python, domino, Ads Data Hub, Big Query, Google Ads and amplifying the precision and efficiency of data-driven analyses\n
•	Pioneering the application of Creative Testing (A/B testing), Incrementality Analysis, and Brand Lift studies, culminating in a granular comprehension of campaign influence and resonance\n
•	Engineering the deployment and fine-tuning of both Multi Touch Attribution and Last Touch Attribution models, enriching attribution frameworks and augmenting attribution accuracy\n
•   Led a cross-functional team in designing and deploying an end-to-end MLops platform, automating model deployment processes and ensuring scalability and reliability\n
•   Implemented continuous integration/continuous deployment (CI/CD) pipelines, monitoring tools, and logging solutions to streamline model deployment and ensure ongoing performance monitoring\n
•   Collaborated closely with business stakeholders to identify key business challenges and develop innovative data-driven solutions that drive strategic decision-making and operational efficiency\n
•	Directing Python training initiatives, equipping team members with essential skills and cultivating a data-driven culture; proficiently managing projects using JIRA and Confluence, bolstering collaboration and productivity\n
•	Heading the team's recruitment efforts, actively participating in sourcing and selection processes, ensuring the acquisition of top-tier talent to fortify the team's capabilities\n
"""
)



# --- JOB 1
    st.write("🚧", "**Data Analyst | EasyRewardz**")
    st.write("11/2019 - 09/2021")
    st.write(
    """
Key Result Areas:
•	Executed comprehensive data analysis to identify trends and patterns, encompassing cleansing, preparation, and reporting utilizing MySQL and Python, channeling actionable strategic insights to drive business decision-making\n
•	Successfully collaborated with approximately 40 key clients spanning across multiple industries including apparel, healthcare, banking, e-commerce, and IT, ensuring bespoke solutions and fostering enduring partnerships\n
•	Conducted intricate Brand Analysis activities, inclusive of Annual and Monthly Reviews, Comparative Decks, Market Basket Analysis, Cohort Studies, LFL Analysis, and Top Products evaluations, sculpting a profound comprehension of market dynamics\n
•	Devised in-depth Customer Analysis, generating critical reports including Lapsation Reports, Drop Rate Assessment, Bill Banding, Sales Performance Tracking, Segmentation Insights, MOM Reports, Decision Analytics, and Forecasting Projections\n
•	Led Ecommerce product review analysis utilizing Pairwise ranking and sentiment analysis techniques to discern consumer preferences and sentiment trends, informing product optimization strategies. Spearheaded Customer Churn Prediction Analysis leveraging Ensemble Techniques such as Random Forest, Gradient Boosting, and AdaBoost, enhancing retention efforts and bolstering customer loyalty initiatives.\n
•	Spearheaded the dynamic update of pivotal KPIs such as Sales, Bills, ABS, ATV, Latency, and Recency on Dashboard interfaces via adeptly crafted stored procedures and functions utilizing MYSQL, culminating in data-driven insights\n
•	Pioneered the automation of dashboard/ reports through SQL and Python,facilitating expedited and accurate reporting processes\n
•	Demonstrated adeptness in monthly DSR (Daily Sales Report) Matching, revamping and automating bill-level detail reconciliation processes between LPaas data and client data, heightening efficiency and accuracy\n
•	Managed the seamless upkeep of the ETL pipeline, harnessing Advanced SQL techniques to ensure uninterrupted data flow\n
•	Ingeniously integrated SQL with Python, empowering automated scheduling of email communications, expediting data dissemination\n
•	Displayed proficiency in Data Modeling, a skill set that underpinned effective data structuring and manipulation. Utilized project management tools such as JIRA to streamline collaborative efforts.\n
•	Facilitated onboarding of new team members through insightful training sessions\n

"""
)

# --- JOB 2
    st.write('\n')
    st.write("🚧", "**Senior Associate | WNS**")
    st.write("11/2016 - 08/2017")
    st.write(
    """
Key Result Areas:
•	Organized comprehensive secondary research efforts, meticulously curating and updating an expansive database encompassing global infrastructure projects and reflecting them on company's custom dashboard\n
•	Proficiently deciphered recurrent client inquiries, translating them into concise and actionable insights through astute data analysis and reporting\n

"""
)

# --- JOB 3
    st.write('\n')
    st.write("🚧", "**Data Analyst | NextGenVision Technology **")
    st.write("07/2015 - 11/2016")
    st.write(
    """
Key Result Areas:
•	Leveraged a diverse toolkit encompassing Excel, Advanced SAS, Python, and Tableau to intricately predict credit default risk using LightGBM, insurance pricing forecast using XGBoost regressor, customer segmantation models etc. through the adept application of various stastistical tools and techniques, steering towards optimal solutions.\n
•	Pioneered the creation of robust analytical and statistical models, seamlessly fortified by dynamic dashboards within Excel and Tableau, empowering Senior Leadership with decisive insights crucial for informed decision-making.\n
•	Developed and maintained statistical models for credit scoring, fraud detection, and customer churn prediction, resulting in improved risk management and operational efficiency\n
•	Collaborated with IT teams to integrate machine learning models into the decision-making process, streamlining and automating various operational workflows\n
•	Conducted thorough analysis of historical data to identify trends and patterns, enabling the organization to make informed decisions on product pricing and promotions\n
"""
)


    st.write('\n')
    st.subheader("EDUCATION")
    st.write("---")
    st.write("""
2015, M.A. Economics: 60%
Gokhale Institute of
Politics and Economics

2014, PG Diploma- Business and Corporate Law: 68%
Symbiosis Centre for Distance Learning

2010, B.A. Business Economics: 76%
Shivaji College, University of Delhi
             """)




with tab4:

# --- WORK HISTORY ---
    st.write('\n')
    st.subheader("PROJECTS")
    st.write("---")
    st.write("""
    🏆 Pan Card Tempering Detection using opencv, streamlit\n
    🏆 Credit Card Fraud Detection\n
    🏆 Money Laundering Detection Using ML, Dl models, building a GUI using tkinter \n
    🏆 Machine Learning Algorithms for the Detection of Fake Bank Currency, GUI: tkinter\n
    🏆 Customer Engagement: A Segmentation Approach for Credit Card Users with Model Deployment on Web\n
    🏆 Deepfake Detection: Google Vision Transformer (ViT) and ResNet50. Uncover Techniques, Build Skills, and Tackle Images and Video Manipulations with SentinelAI Framework\n
    🏆 Exploring Amazon Grocery Market: ML, DL, Unsupervised Insights, and Generative AI Content Generation\n
    🏆 Chest X-Ray to Words (Image-to-Text): GAN-Based Chest X-Ray Medical Image Generation and Text Synthesis for Pneumonia\n
    🏆 Human vs AI Text Classification: DistilBERT, RoBERTa, and BERT-Based Binary Text Classification for AI Content\n
""")
