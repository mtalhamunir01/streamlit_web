import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie
import base64
import os
from bokeh.models.widgets import Div


cwd = os.getcwd()
print(cwd)
st.set_page_config(page_title="My Webpage", page_icon=":computer:", layout="wide")
with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)




#####################
#####################
# Navigation

st.markdown(
    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
    unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #330000;">
  <a class="navbar-brand" href="#i-am" target="_blank"> 
  <span class="gold">Muhammad Talha</span> 
  <span class="white">Munir</span> 
  </a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#i-am">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education-certificates">Education & Certificate</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#my-projects">My Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)


# --- Personal Details Expanded ---

with st.container():
    left_column, right_column = st.columns([3, 1])
    with left_column:
        st.markdown(
            "## I am",
            unsafe_allow_html=True)
        st.markdown(
            "<p style='font-size:50px; color: #cc7a00; text-align: left;margin:0;padding:0;line-height: 1.25em;text-align: left '>Muhammad Talha Munir</p>",
            unsafe_allow_html=True)
        st.markdown(
            "<p style='font-size:25px; color:#C0C0C0; text-align: left;margin:0;padding:2;line-height: 1.25em;text-align: left;padding-bottom: 15px;'>Data Scientist | ML Engineer</p>",
            unsafe_allow_html=True)
        st.markdown(
            "<p style='font-size:17px; color: #808075; text-align: left;margin:0;padding:2;line-height: 1.25em;text-align: left '>A Certified Data Scientist, capable to ensure accuracy and integrity around data and insights among various industries. Moderately skilled in data-driven solutions, data visualization, machine learning and deep learning.</p>",
            unsafe_allow_html=True)

        m = st.markdown("""
        <style>
        div.stButton > button:first-child {
            background-color: #ffffff;
            color:#0A0A0A;
        }
        div.stButton > button:hover {
            background-color: #72ab00;
            color:#0A0A0A;
            border-color: #72ab00;

        div.stButton > button:visited  {
            background-color: #72ab00;
            color:#0A0A0A;
            border-color: #72ab00;
            }

        div.stButton > button:focus  {
            background-color: #72ab00;
            color:#0A0A0A;
            border-color: #72ab00;
            }        
        </style>""", unsafe_allow_html=True)
        with open("data/Talha CV.pdf", "rb") as file:

            btn = st.download_button(
                label="RESUME",
                data=file,
                file_name="dowloaded.pdf",
                mime="application/octet-stream"
            )
        if st.button('My Projects'):
            js = "window.location.href = '#my-projects'"
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
    with right_column:
        image = Image.open('images/Profile Pic.png')
        st.image(image, width=400)


st.markdown("""<hr style="height:1px;border:none;color:#ffffff;background-color:#ffffff;" /> """, unsafe_allow_html=True)


# --- Personal Details Text ---

st.markdown('## PERSONAL DETAILS', unsafe_allow_html=True)
st.warning('''
A few interesting facts about me. I am also an avid gamer, who loves to play competitive strategy games. Moreover, I am keen on learning. Each day I push myself to learn something new and exciting, whether that's about machine learning, software engineering, or anything else.
''')



st.markdown("""<hr style="height:1px;border:none;color:#ffffff;background-color:#ffffff;" /> """, unsafe_allow_html=True)



# Loading Images for Interest Areas
NLP = ("images/nlp_2.jpg")
CLOUD = ("images/cloud.jpg")
ML = ("images/ml.jpg")
analysis = ("images/analytics.png")
parallel = ("images/parallel.png")
statistics = ("images/statistics.jpg")
mlops = ("images/mlops-og.png")


# --- Interest Areas ---

# with st.container():
#     st.title("Areas of Interest")
#     st.markdown(
#         "<p style='font-size:23px; color: #F8F8FF; text-align: center;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>Take a look at some of the things I love working on.</p>",
#         unsafe_allow_html=True)
#     col1, col2, col3 = st.columns(3)

#     with col1:
#         st.markdown(
#             """
#             <style>
#             .logo-text {
#                 font-weight:25 !important;
#                 font-size:25px !important;
#                 color: #C0C0C0 !important;
#                 text-align: center
#             }
#             .logo-img1 {
#                 display: block;
#                 float:center;
#                 margin-left: auto;
#                 margin-right: auto;
#                 width: 100px;
#             }
#             </style>
#             """,
#             unsafe_allow_html=True)
#         st.markdown(
#             f"""<img class="logo-img1" src="data:image/png;base64,{base64.b64encode(open(analysis, "rb").read()).decode()}"> <p class="logo-text">Data Analytics</p> """,
#             unsafe_allow_html=True)

#         # st.image(CLOUD, width =100)
#         # st.markdown("<p style='font-size:25px; color: #5D6D7E; text-align: left;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>CLOUD</p>", unsafe_allow_html=True)
#         st.markdown(
#             "<p style='font-size:20px; color: #5D6D7E; text-align: center;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>I love telling a story. Getting to the heart of a problem and coming up with a solution.</p>",
#             unsafe_allow_html=True)
#         # st.image(CLOUD, width =100)
#         # st.markdown("<p style='font-size:25px; color: #5D6D7E; text-align: left;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>CLOUD</p>", unsafe_allow_html=True)
#         st.markdown(
#             """
#             <style>
#             .logo-text {
#                 font-weight:25 !important;
#                 font-size:25px !important;
#                 color: #C0C0C0 !important;
#                 text-align: center
#             }
#             .logo-img1 {
#                 display: block;
#                 float:center;
#                 margin-left: auto;
#                 margin-right: auto;
#                 width: 100px;
#             }
#             </style>
#             """,
#             unsafe_allow_html=True)
#         st.markdown(
#             f"""<img class="logo-img3" src="data:image/png;base64,{base64.b64encode(open(NLP, "rb").read()).decode()}"> <p class="logo-text">NLP</p> """,
#             unsafe_allow_html=True)
#         # st.image(NLP, width =200)
#         # st.markdown("<p style='font-size:25px; color: #5D6D7E; text-align: left;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>NLP</p>", unsafe_allow_html=True)
#         st.markdown(
#             "<p style='font-size:20px; color: #5D6D7E; text-align: center;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>I love to do text analytics to some of the hardest questions in business.</p>",
#             unsafe_allow_html=True)
#     with col2:
#         st.markdown(
#             """
#             <style>
#             .logo-text {
#                 font-weight:25 !important;
#                 font-size:25px !important;
#                 color: #C0C0C0 !important;
#                 text-align: center
#             }
#             .logo-img2 {
#                 display: block;
#                 float:center;
#                 margin-left: auto;
#                 margin-right: auto;
#                 width: 150px;
#             }
#             </style>
#             """,
#             unsafe_allow_html=True)
#         st.markdown(
#             f"""<img class="logo-img2" src="data:image/png;base64,{base64.b64encode(open(ML, "rb").read()).decode()}"> <p class="logo-text">Machine Learning</p> """,
#             unsafe_allow_html=True)
#         # st.image(NLP, width =200)
#         # st.markdown("<p style='font-size:25px; color: #5D6D7E; text-align: left;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>NLP</p>", unsafe_allow_html=True)
#         st.markdown(
#             "<p style='font-size:20px; color: #5D6D7E; text-align: center;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>I am passionate about learning the theory that is pushing the cutting edge of ML.</p>",
#             unsafe_allow_html=True)
#         # st.image(CLOUD, width =100)
#         # st.markdown("<p style='font-size:25px; color: #5D6D7E; text-align: left;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>CLOUD</p>", unsafe_allow_html=True)
#         # st.markdown("<p style='font-size:25px; color: #5D6D7E; text-align: center;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>I am passionate about learning the theory that is pushing the cutting edge of ML.</p>", unsafe_allow_html=True)
#         st.markdown(
#             """
#             <style>
#             .logo-text {
#                 font-weight:25 !important;
#                 font-size:25px !important;
#                 color: #C0C0C0 !important;
#                 text-align: center
#             }
#             .logo-img4 {
#                 display: block;
#                 float:center;
#                 margin-left: auto;
#                 margin-right: auto;
#                 width: 110px;
#             }
#             </style>
#             """,
#             unsafe_allow_html=True)
#         st.markdown(
#             f"""<img class="logo-img1" src="data:image/png;base64,{base64.b64encode(open(CLOUD, "rb").read()).decode()}"> <p class="logo-text">CLOUD</p> """,
#             unsafe_allow_html=True)
#         st.markdown(
#             "<p style='font-size:20px; color: #5D6D7E; text-align: center;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>I utilize AWS & GCP to develop and productionize machine learning systems.</p>",
#             unsafe_allow_html=True)
#     with col3:
#         st.markdown(
#             """
#             <style>
#             .logo-text {
#                 font-weight:25 !important;
#                 font-size:25px !important;
#                 color: #C0C0C0 !important;
#                 text-align: center
#             }
#             .logo-img5 {
#                 display: block;
#                 float:center;
#                 margin-left: auto;
#                 margin-right: auto;
#                 width: 250px;
#             }
#             </style>
#             """,
#             unsafe_allow_html=True)
#         st.markdown(
#             f"""<img class="logo-img5" src="data:image/png;base64,{base64.b64encode(open(mlops, "rb").read()).decode()}"> <p class="logo-text">MLOps</p> """,
#             unsafe_allow_html=True)
#         # st.image(NLP, width =200)
#         # st.markdown("<p style='font-size:25px; color: #5D6D7E; text-align: left;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>NLP</p>", unsafe_allow_html=True)
#         st.markdown(
#             "<p style='font-size:20px; color: #5D6D7E; text-align: center;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>I have in-depth knowledge of MLOps (machine learning operations) and love to learn about more it.</p>",
#             unsafe_allow_html=True)
#         st.markdown(
#             """
#             <style>
#             .logo-text {
#                 font-weight:25 !important;
#                 font-size:25px !important;
#                 color: #C0C0C0 !important;
#                 text-align: center
#             }
#             .logo-img3 {
#                 display: block;
#                 float:center;
#                 margin-left: auto;
#                 margin-right: auto;
#                 width: 120px;
#             }
#             </style>
#             """,
#             unsafe_allow_html=True)
#         #st.markdown(
#          #   f"""<img class="logo-img3" src="data:image/png;base64,{base64.b64encode(open(statistics, "rb").read()).decode()}"> <p class="logo-text">STATS</p> """,
#          #   unsafe_allow_html=True)
#         # st.image(NLP, width =200)
#         # st.markdown("<p style='font-size:25px; color: #5D6D7E; text-align: left;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>NLP</p>", unsafe_allow_html=True)
#         #st.markdown(
#         #   "<p style='font-size:20px; color: #5D6D7E; text-align: center;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>I Love to Learn Stats.</p>",
#         #   unsafe_allow_html=True)

#         # st.image(CLOUD, width =100)
#         # st.markdown("<p style='font-size:25px; color: #5D6D7E; text-align: left;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>CLOUD</p>", unsafe_allow_html=True)
#         # st.markdown("<p style='font-size:25px; color: #5D6D7E; text-align: center;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>I am passionate about learning the theory that is pushing the cutting edge of ML.</p>", unsafe_allow_html=True)
#         st.markdown(
#             f"""<img class="logo-img4" src="data:image/png;base64,{base64.b64encode(open(parallel, "rb").read()).decode()}"> <p class="logo-text">Parallel Computing</p> """,
#             unsafe_allow_html=True)
#         # st.image(NLP, width =200)
#         # st.markdown("<p style='font-size:25px; color: #5D6D7E; text-align: left;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>NLP</p>", unsafe_allow_html=True)
#         st.markdown(
#             "<p style='font-size:20px; color: #5D6D7E; text-align: center;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>HIVE, Hadoop,PySpark and Databriks</p>",
#             unsafe_allow_html=True)


def load_lottieurl_1(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_anlyt = load_lottieurl_1("https://assets3.lottiefiles.com/packages/lf20_wknogr2w.json")
lottie_ml = load_lottieurl_1("https://assets7.lottiefiles.com/packages/lf20_edouagsj.json")
lottie_ops = load_lottieurl_1("https://assets3.lottiefiles.com/packages/lf20_obkemuop.json")
lottie_nlp = load_lottieurl_1("https://assets2.lottiefiles.com/packages/lf20_kaelaowc.json")
lottie_cloud = load_lottieurl_1("https://assets7.lottiefiles.com/private_files/lf30_k68apabx.json")

with st.container():
    st.title("Areas of Interest")
    st.markdown(
        "<p style='font-size:23px; color: #F8F8FF; text-align: center;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>Take a look at some of the things I love working on.</p>",
        unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <style>
            .logo-text {
                font-weight:25 !important;
                font-size:25px !important;
                color: #C0C0C0 !important;
                text-align: center;
                margin: 0;
                padding-top:0
            }

            </style>
            """,
            unsafe_allow_html=True)
        st_lottie(lottie_anlyt, height=150, key='anlyt')
        st.markdown("""<p class="logo-text">Data Analytics</p> """,unsafe_allow_html=True)

        st.markdown(
            "<p style='font-size:20px; color: #5D6D7E; text-align: center;margin:0;padding:2;line-height: 1.25em;'>Getting to the root of any problem and finding an optimal solution to it with a lovely story, That's what excites me most.</p>",
            unsafe_allow_html=True)
    
    with col2:

        st.markdown(
            """
            <style>
            .logo-text {
                font-weight:25 !important;
                font-size:25px !important;
                color: #C0C0C0 !important;
                text-align: center;
                margin: 0;
                padding-top:0
            }

            </style>
            """,
            unsafe_allow_html=True)
        st_lottie(lottie_ml, height=150, key='ml')
        st.markdown("""<p class="logo-text">Machine Learning</p> """, unsafe_allow_html=True)
        
        st.markdown(
            "<p style='font-size:20px; color: #5D6D7E; text-align: center;margin:0;padding:2;line-height: 1.25em;'>Passionate about learning the theory, that is pushing the cutting edge of ML.</p>",
            unsafe_allow_html=True)
    
    with col3:
        st.markdown(
            """
            <style>
            .logo-text {
                font-weight:25 !important;
                font-size:25px !important;
                color: #C0C0C0 !important;
                text-align: center;
                margin: 0;
                padding-top:0
            }

            </style>
            """,
            unsafe_allow_html=True)

        st_lottie(lottie_ops, height=150, key='ops')
        st.markdown("""<p class="logo-text">MLOps</p> """,unsafe_allow_html=True)

        st.markdown(
            "<p style='font-size:20px; color: #5D6D7E; text-align: center;margin:0;padding:2;line-height: 1.25em;'>I am developing in-depth knowledge of MLOps (machine learning operations) and learning more about it bit by bit.</p>",
            unsafe_allow_html=True)

    nc,col11,col22,nc = st.columns([1,2,2,1])

    with col11:
        st.markdown(
            """
            <style>
            .logo-text {
                font-weight:25 !important;
                font-size:25px !important;
                color: #C0C0C0 !important;
                text-align: center;
                margin: 0;
                padding-top:0
            }

            </style>
            """,
            unsafe_allow_html=True)
        st_lottie(lottie_nlp, height=150, key='')
        st.markdown("""<p class="logo-text">NLP</p> """,unsafe_allow_html=True)

        st.markdown(
            "<p style='font-size:20px; color: #5D6D7E; text-align: center;margin:0;padding:2;line-height: 1.25em;'>Right now, I am challenging  myself to do text analytics to some of the hardest questions in business.</p>",
            unsafe_allow_html=True)
    
    with col22:
        st.markdown(
            """
            <style>
            .logo-text {
                font-weight:25 !important;
                font-size:25px !important;
                color: #C0C0C0 !important;
                text-align: center;
                margin: 0;
                padding-top:0
            }

            </style>
            """,
            unsafe_allow_html=True)
        st_lottie(lottie_cloud, height=150, key='cloud')
        st.markdown("""<p class="logo-text">Cloud</p> """,unsafe_allow_html=True)

        st.markdown(
            "<p style='font-size:20px; color: #5D6D7E; text-align: center;margin:0;padding:2;line-height: 1.25em;'>I am on the path to utilizing AWS & GCP for the development and production of ML Operations.</p>",
            unsafe_allow_html=True)














#####################
# Custom function for printing text
def txt(a, b):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt2(a, b):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f"<span class=gold1>{a}</span>",unsafe_allow_html=True)
    with col2:
        st.markdown(b)


def txt3(a, b):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt4(a, b, c):
    col1, col2, col3 = st.columns([1.5, 2, 2])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)
    with col3:
        st.markdown(c)


#####################
st.markdown("""<hr style="height:1px;border:none;color:#ffffff;background-color:#ffffff;" /> """, unsafe_allow_html=True)



# --- Education & Certification ---

st.markdown('''
## Education & Certificates
''')
txt('**Convolutional Neural Networks in TensorFlow** , *deeplearning.ai – [Coursera](https://coursera.org/share/f21970ea7a257aab7b2506625814cb9d)*',
    '2022 – Present')
txt('**Introduction to TensorFlow for Artificial Intelligence, Machine Learning, and Deep Learning** , *deeplearning.ai – [Coursera](https://coursera.org/share/b25881c4ed18e4fc4ea69bd3afffad2c)*',
    '2022 – Present')
txt('**Data Science with Python** , *[Codanics](https://drive.google.com/file/d/1zJ7r2wESoxbtfxCpiOfmG8dTrk09QYXb/view)*',
    '2022 – Present')
txt('**Bachelors in Electrical Engineering** , *University of Engineering and Technology , Taxila*, Pakistan',
    '2015 – 2019')
txt('**Pre-Engineering** , *Punjab Group of Colleges Multan* ,  Pakistan',
    '2013 – 2019')
 
# txt('**IBM Data Science** , *Coursera – IBM*',
#     'Present')
# txt('**Deep Learning Specialization** , *Coursera – deeplearning.ai*',
#     'Present')
# txt('**Machine Learning on Google Cloud** , *Coursera – Google*',
#     'Present')
# txt('**Practical Machine Learning on H2O** , *Coursera – H2O.ai*',
#     'Present')
#####################


st.markdown("""<hr style="height:1px;border:none;color:#ffffff;background-color:#ffffff;" /> """, unsafe_allow_html=True)


# --- Working Experience ---

st.markdown('''
## Work Experience
''')

txt('**Internee** at Dems Group – DEMS Pvt. Ltd',
    '2018 – 2018')
st.markdown('''
- Project Supervision.
- Manager Engineering Department.
- Customer Care Department.
- Planning and Design Department.
''')

# txt('**System Analyst**, VEON',
#     '2017 – present')
# st.markdown('''
# **Summary**: Responsible for leading & executing advanced analytics & data science initiatives for the revenue assurance in the organization. Worked with key stakeholders to scope, develop, & present ML models.
# - Designed and implemented a machine learning system that predicts grey traffic with `83%` `accuracy`.
# - Perform revenue controls and a variety of statistical analyses using `Microsoft excel`, `python`, and `SQL`.
# - Developed early iteration of ETL pipelines using RAID (WEDO) and Python (including `SQLAlchemy`, `paramiko`, `Dask`, `Hadoop`, `Hive`) with logging, data cataloging, & job status tracking for processing `1M+` text and binary files.
# - Designed data models & schema, created DDL & DML scripts for Oracle RDBMS Database.
# ''')

# txt('**Enterprise Application Integration Planning**, VEON',
#     '2012 – 2017')
# st.markdown('''
# **Summary**: Responsible for leading & assist in the development of technology roadmaps to evolve the API estate in conjunction with internal and external TELCO solution providers
# - API tester with full system development lifecycle experience, including designing, developing, and implementing test plans, test cases, and test processes fueling swift corrective actions, significant cost savings, and fault-free audits.
# - Hands-on technology professional accustomed to working in complex, project-based environments. Multifaceted experience in QA software testing, software development, and user-acceptance testing.
# - Review requirements, specifications, and technical design documents to provide timely and meaningful feedback.
# - Create detailed, comprehensive, and well-structured test plans and test cases.
# - Estimate, prioritize, plan and coordinate testing activities.
# - Design, develop, and execute automation scripts using open source tools.
# - Identify, record, document thoroughly, and track bugs
# - Perform thorough regression testing when bugs are resolved.
# - Develop and apply testing processes for new and existing products to meet client needs.
# - Investigate the causes of non-conforming software and train users to implement solutions.
# ''')

#####################
st.markdown("""<hr style="height:1px;border:none;color:#ffffff;background-color:#ffffff;" /> """, unsafe_allow_html=True)



# --- Skills ---

with st.container():
    
    # st.markdown('''<span class='gold1'>Muhammad Talha</span>''' , unsafe_allow_html=True)
    st.markdown('''## Skills''')

    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("Programming")
    with col2:
        st.markdown('''<span class='gold1'>Python</span>[<span class='gold1'>pandas</span>,<span class='gold1'>numpy</span>,<span class='gold1'>os</span>],<span class='gold1'>google.colab</span>,<span class='gold1'>SQL</span> [
        <span class='gold1'>MySQL</span>]''',unsafe_allow_html=True)

    with col1:
        st.markdown("Data Visualization")
    with col2:
        st.markdown('''<span class='gold1'>matplotlib</span>,<span class='gold1'>seaborn</span>,<span class='gold1'>plotly</span>''',unsafe_allow_html=True) 

    with col1:
        st.markdown('Machine Learning')
    with col2:
        st.markdown('''<span class='gold1'>scikit-learn</span>,<span class='gold1'>sciPy</span>''',unsafe_allow_html=True)

    with col1:
        st.markdown('Model Deployment')
    with col2:
        st.markdown('''<span class='gold1'>streamlit</span>,<span class='gold1'>Docker</span>''',unsafe_allow_html=True)
    
    with col1:
        st.markdown('Deep Learning')
    with col2:
        st.markdown('''<span class='gold1'>TensorFlow</span>,<span class='gold1'>Keras</span>''',unsafe_allow_html=True)

    with col1:
        st.markdown('Cloud')
    with col2:
        st.markdown('''<span class='gold1'>AWS</span>,<span class='gold1'>GCP</span>''',unsafe_allow_html=True)


st.markdown("""<hr style="height:1px;border:none;color:#ffffff;background-color:#ffffff;" /> """, unsafe_allow_html=True)


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_l4fgppor.json")



# ---- PROJECTS ----


with st.container():
    st.write("---")
    st.markdown('''
    ## My Projects
    ''')
    #st.header("My Projects")
    st.write("## coming soon")


st.markdown("""<hr style="height:1px;border:none;color:#ffffff;background-color:#ffffff;" /> """, unsafe_allow_html=True)


# ---- WHAT I DO ----


with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I'm a Data Scientist & Machine learning enthusiast with moderate experience.

I am developing my expertise around deep learning, MlOps, and complete machine learning workflow, from the project conception (including asking the question: is machine learning the best solution?) to model deployment in production, passing through the data collection process, and optimization.

I prefer to work on long-term and hourly projects, but I'm open to working on exciting projects of all sizes.
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=400, key="coding")


st.markdown("""<hr style="height:1px;border:none;color:#ffffff;background-color:#ffffff;" /> """, unsafe_allow_html=True)
   

# ---- CONTACT ----


with st.container():

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/mtalhamunir123@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column,nc ,right_column, nc1 = st.columns([3,1,1,1])
    with left_column:
        st.header("Get In Touch With Me!")
        st.write("##")
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.markdown('''## Social Media''')
        st.write("""
            
            [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mtalhamunir01)

            [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mtalhamunir01/)

            [![Twitter](https://img.shields.io/badge/Twitter-%231DA1F2.svg?style=for-the-badge&logo=Twitter&logoColor=white)](https://twitter.com/mtalhamunir01)

            [![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)](https://www.instagram.com/mtalhamunir01/)

            [![MAIL Badge](https://img.shields.io/badge/-mtalhamunir123@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:mtalhamunir@gmail.com)](mailto:mtalhamunir123@gmail.com)
            
            ##### *© M Talha Munir, 2022*
            """
            ) 
