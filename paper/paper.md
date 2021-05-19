---
title: 'Teaching Python for Data Science: Collaborative development of a modular & interactive curriculum'
tags:
  - Data Science
  - Python
  - Jupyter
  - Girls Who Code
authors:
  - name: Marlena Duda
    orcid: TODO
    affiliation: 1
  - name: Kelly L. Sovacool
    orcid: 0000-0003-3283-829X
    affiliation: 1
  - name: Negar Farzaneh
    orcid: TODO
    affiliation: 1
  - name: Vy Kim Nguyen
    orcid: 0000-0002-6128-0523
    affiliation: "1, 8"
  - name: Sarah Haynes
    orcid: 0000-0003-3225-1691
    affiliation: 6
  - name: Hayley Falk
    orcid: 0000-0002-5198-1836
    affiliation: 1
  - name: Katherine L. Furman
    orcid: 0000-0002-0340-4292
    affiliation: "3, 4"
  - name: Logan A. Walker
    orcid: 0000-0002-5378-3315
    affiliation: "5, 1"
  - name: Rucheng Diao
    orcid: TODO
    affiliation: 1
  - name: Morgan Oneka
    orcid: TODO
    affiliation: 1
  - name: Audrey Drotos
    orcid: TODO
    affiliation: TODO
  - name: Alana Woloshin
    orcid: 0000-0002-5224-4221
    affiliation: 7
  - name: Gabrielle Dotson
    orcid: TODO
    affiliation: 1
  - name: April Kriebel
    orcid: 0000-0003-0008-9044
    affiliation: 1
  - name: Lucy Meng
    orcid: TODO
    affiliation: TODO
  - name: Stephanie N. Thiede
    orcid: 0000-0003-0173-4324
    affiliation: 2
  - name: Shweta Ramdas
    orcid: TODO
    affiliation: TODO
  - name: Zena Lapp^[corresponding author]
    orcid: 0000-0003-4674-2176
    affiliation: 1
  - name: Brooke N. Wolford^[corresponding author]
    orcid: 0000-0003-3153-1552
    affiliation: 1
affiliations:
  - name: Department of Computational Medicine & Bioinformatics, University of Michigan
    index: 1
  - name: Department of Microbiology & Immunology, University of Michigan
    index: 2
  - name: Neuroscience Graduate Program, University of Michigan
    index: 3
  - name: Michigan Neuroscience Institute, University of Michigan
    index: 4
  - name: Biophysics Graduate Program, University of Michigan
    index: 5
  - name: Department of Pathology, University of Michigan
    index: 6
  - name: School of Information, University of Michigan
    index: 7
  - name: Department of Environmental Health Sciences, University of Michigan
    index: 8
date: 30 Apr. 2021
bibliography: paper.bib
---

# Summary

<!-- pasted from our PyCon 2020 talk proposal -->
We are bioinformatics trainees at the University of Michigan who started a
local chapter of Girls Who Code to provide a fun and supportive environment for
high school women to learn the power of coding.
Our goal was to cover basic coding topics and data science concepts through
live-coding and hands-on practice.
However, we couldn’t find a resource that exactly met our needs. Therefore, over the past
three years, we have developed a curriculum and instructional format using
Jupyter notebooks to effectively teach introductory Python for data science.
This method, inspired by The Carpentries organization, uses bite-sized lessons
followed by independent practice time to reinforce coding concepts, and
culminates in a data science capstone project using real-world data.
We believe our open curriculum is a valuable resource to the wider education
community and hope that educators will use and improve our lessons, challenge
problems, and teaching best-practices.
Anyone can contribute to [our educational materials on GitHub](https://github.com/GWC-DCMB).


# Statement of Need

As women in the Department of Computational Medicine and Bioinformatics at the
University of Michigan, we experience the gender gap first hand in our field.
During the 1974-1975 academic year, women achieved 18.9% of total Bachelor's
degrees in computer and information sciences in the US [@nces_digest_2012].
By 1983-1984 this peaked at 37.1%, but fell to 17.6% by 2010-2011. We also see this
national trend in the training of the next generation of Bioinformaticians at
Michigan Medicine.
Since accepting its first students in 2001, the U-M Bioinformatics Graduate
Program has graduated 66 male and 22 female doctorates as of 2019.
This disparity begins at the applicant level; during 2016-2019 the average
percentage of females applying directly to the Bioinformatics PhD program is
35.2%, and 41% for female applicants listing Bioinformatics as first or second
choice in the Program in Biomedical Sciences, U-M's biomedical PhD umbrella
program.

Previous research on women's educational experiences in STEM have produced
various explanations for persistent gender disparities
[@benbow_gender_2016].
One explanation is that women in first year computer science courses rate
themselves as being less experienced, prepared, or able to master the course
material than the men [@fisher_undergraduate_1997].
The majority of our organization's founding graduate students (all women) began
coding in our undergraduate careers or later.
We wanted to provide a safe place for local young women to begin coding in high
school, and develop confidence in themselves and their computational skills
before college.
A national organization, Girls Who Code, whose mission and values aligned with
ours, was founded in 2012.
Girls Who Code's mission is to close the gender gap in technology
[@saujani_girls_2015].
Because of our personal experiences and the paucity of women in our field, we
began a student organization at the University of Michigan in 2017.
For the past four academic years we have registered annually as a recognized
Girls Who Code Club because the national organization provided name recognition,
curriculum resources, guidance for a Capstone Impact Project, and a framework
for launching a coding club.
In 2019 we launched a Data Science Summer Experience which is unaffiliated with
the national Girls Who Code organization.

The national Girls Who Code organization provides a curriculum that teaches
website and application development through programming languages like HTML and
Java.
However, our biomedical science graduate students generally have limited
experience with these languages.
Data Scientist was rated the #1 job in America by Glassdoor in 2016-2019, #3 in
2020, and #2 in 2021 [@stansell_breaking_2019].
We believe career exploration in data science will optimally prepare our
students for careers that provide financial stability. <!-- TODO: address comment from AK: "Do we need to establish a clearer link between data science and the use of Python specifically? The PYPL index, used as a proxy for how popular a language is, has ranked Python as it's number one language (https://pypl.github.io/PYPL.html). I'm not sure if this the best way to illustrate the point, but I do think we need more support for the place of Python in the workplace." -->
By leveraging the data science expertise of our Club facilitators, we created a
specialized curriculum focused on computational data science in the Python
programming language.

Girls Who Code encourages participants to learn programming skills while working
on an Impact Project website or application throughout the Club
[@hq_gallery_2021].
We created an open source Data Science curriculum that teaches the requisite
Python and statistics skills to complete a Capstone Project, which is a data
analysis project on a data set of interest.
Using this curriculum, we employ participatory live coding as used by The
Carpentries, which is an effective method that engages learners
[@wilson_software_2016; @nederbragt_ten_2020].
Using paired activities, our curriculum follows the "I do, we do, you do"
didactic paradigm [@fisher_better_2013].
We provide open-source resources for both in-person and virtual versions of our
curriculum, including videos corresponding to each lesson.
While we developed this curriculum for our Girls Who Code Club and Summer
Experience, we believe that it can be widely used for teaching introductory
coding for data science.

# Collaborative Curriculum Development

We assembled a team of volunteers involved in our club to develop a custom
curriculum to teach introductory Python for data science via live coding.
We chose what content to cover based on what our students would need to learn in
order to complete a small data analysis project and communicate their findings
to their peers.
We divided up the content by topic into Jupyter notebooks for each lesson, with
each lesson taking approximately 15-20 minutes to teach via live coding.
Each lesson has a corresponding practice notebook with additional exercises on
the same content taught in the lesson, but with different data or variables
used.
We hosted the curriculum notebooks in a public GitHub repository to facilitate
collaborative development and peer review using pull requests.
In the initial curriculum drafting phase, developers were assigned lesson and
practice notebooks to write.
Once the draft of a lesson was completed, the writer opened a pull request and
asked for review from a different developer.
The reviewer then provided feedback and approved the pull request to be merged
into the main branch after the writer made any requested changes.
This way, more than one person viewed each notebook before it could be
incorporated into the public curriculum, which reduced mistakes and ensured
higher quality content. <!-- TODO: cite U-M Carpentries paper for the development model once it's submitted to bioRxiv?-->
While teaching from the curriculum at the first Data Science Summer Experience,
instructors took notes on their experience and made revisions afterward.
Maintainers continue to monitor the repository and resolve issues as they arise.

Following the onset of the COVID-19 pandemic, we quickly pivoted our club to a
virtual format.
In preparation for the 2020 Summer Experience, we switched to a flipped
classroom style following feedback from our club participants that it was too
difficult to follow along live coding via Zoom.
We recorded facilitators teaching the lesson notebooks as if they were live
coding, then shared them along with a link to the lesson notebooks for students
to code along with while watching the videos.
Each video shows the Jupyter notebook alongside the facilitator themselves
teaching.
This format allowed students to learn at their own pace, then ask questions and
practice when we met together virtually. <!-- TODO: should this actually go later in the curriculum section?-->

Our Jupyter notebooks and links to the lesson videos can be accessed on GitHub:
https://github.com/GWC-DCMB/curriculum-notebooks

# Curriculum

Our curriculum was designed for high school students with no prior coding
experience who are interested in learning Python programming for data science.
However, this course material would be useful for anyone interested in learning
basic programming for data analysis, regardless of age or experience level.

Our curriculum features short lessons to deliver course material in “bite sized”
chunks, followed by practices to solidify the learners' understanding.

## Learning Objectives

Our learning objectives are:

1. Understand fundamental concepts and best practices in coding.
2. Apply data analysis to real world data to answer scientific questions.
3. Create informative summary statistics and data visualizations in Python.

These skills provide a solid foundation for basic data analysis in Python and
participation in our programming exposes students to the many ways coding and
data science can be used to make large impacts across many disciplines.

## Course Content

Our curriculum design consists of 27 modules that cover Jupyter notebook setup,
Python coding fundamentals, use of essential data science packages including
Pandas and numpy, basic statistical analyses, and plotting using seaborn and
matplotlib (Figure 1) [@harris_array_2020; @waskom_seaborn_2021;
@hunter_matplotlib_2007].
Each of the following modules consists of a lesson notebook, used for teaching
the concept via live coding, and a practice notebook containing similar
exercises for the student to complete on their own following the lesson:

1. Jupyter Setup
2. HelloWorld and Variables
3. Variables and Types
4. Lists Intro
5. Indexing
6. 2D Lists Intro
7. 2D Lists Indexing
8. Logic
9. Conditionals
10. Loops I
11. Loops II
12. Functions and Methods
13. Packages
14. Pandas-Intro
15. Pandas-Reading
16. Pandas Subsetting I
17. Pandas Subsetting II
18. Dictionaries
19. Functions
20. Numpy Intro
21. Basic Stats I - Averages
22. Basic Stats II - Percents
23. Basic Stats III - Correlations
24. Basic Stats IV - Significance
25. Plotting I - Line Graphs
26. Plotting II - Scatterplots
27. Plotting III - Bar Charts and Histograms

Each lesson builds on those before it, beginning with relevant content reminders
from the previous lessons and ending with a concise summary of the skills
presented within.
Throughout our program, the students also simultaneously work on a data science
project on a topic of interest using a real world dataset of their choosing.
Through this Capstone Project, learners gain practical experience with each
skill as they learn it in the lessons; including importing and cleaning data,
data visualization, and basic statistical analyses.


## Instructional Design
<!-- teaching philosophy / pedagogy -->

We modeled our instructional design in the style of Software Carpentry [@wilson_software_2016].

1. Each lesson begins with a recapping of the relevant core skills presented in the previous lessons.
1. All lessons are designed to be taught via 15-minute live-coding sessions, where students type and run code in their own notebooks along with the instructor in real time. As in Software Carpentry, we find this to be a highly effective method of teaching coding, since students must actively engage with the material and deal with errors and bugs as they come up.
1. Each lesson ends with a summary of core skills presented within the material.
1. Each short lesson is also accompanied by a subsequent 10-minute independent practice, providing further opportunity for practical experience implementing the coding skill at hand and testing their understanding of the content.

This curriculum was originally developed for in-person instruction, but the onset of the COVID-19 pandemic necessitated restructuring to a virtual format.
To better facilitate virtual instruction, we switched to a flipped classroom style based on feedback from our club participants that it was too difficult to follow along with live coding via Zoom.
We provide video recordings of instructors going through the Jupyter notebooks as if they were live coding in the classroom.
Students then watch the lessons and complete the practice exercises prior to virtual meetings, in which they have the opportunity to ask questions on material they did not understand and go over the practice exercises.
This virtual format is especially beneficial because it 1) allows students to learn at their own pace, and 2) enables dissemination of our curriculum to a wider audience interested in learning introductory Python programming for data science.

For both in-person and virtual instruction, once students have completed the Fundamentals module and reach the Data Science Essentials module they will begin simultaneous work on their data science projects.
Projects are completed in a paired programming style, where partners take turns assuming the “driver” (i.e. the typer) and “navigator” (i.e. the instructor) roles.
Switching off in this way helps both partners assume equal responsibility for the project workload, but more importantly it enables improved knowledge transfer through peer-to-peer learning.

In addition to our coding curriculum, another key component of our programming is hosting guest speakers from diverse fields across academia and industry.
Our guest speakers come to discuss the journey they’ve taken to their career paths as well as how they utilize programming and data science in their jobs.
These varied perspectives are extremely valuable to our learners as they provide several practical examples of programming careers in the real world.

## Experience of Use

We have used this curriculum to teach the Data Science Summer Experience and
Girls Who Code Club in person in 2019 and virtually in 2020-2021.
For the in person instances, we taught the curriculum through participatory live
coding, a technique we learned from [The Carpentries](https://carpentries.org/)
where the instructor types and explains the code while the learners follow along
in real time.
For the virtual instances, we used a flipped classroom approach where the
learners explore the material individually before meeting together.
Learners watch videos of instructors explaining the material through "live"
coding and follow along.
Learners then complete a Practice notebook corresponding to the Lesson.
Facilitators then spend meeting time answering questions and reviewing the core
concepts in the Practice notebook.
For both in person and virtual instances, we had several facilitators present at
each session to answer questions and help learners debug.
Furthermore, one or two facilitators were assigned to each project group to help
learners define data analysis questions, develop and execute a data analysis
plan, visualize and communicate their findings, and troubleshoot coding
problems.

We credit the success of our curriculum not only to the skill of the
instructors, but also to the way we organized and executed the lessons and
project:

1. The instructors and learners used [Google Colaboratory
(Colab)](https://colab.research.google.com/) to write and execute code in
Jupyter notebooks. We chose this option because learners do not have to install
any programs to use Google Colab, and you can easily open and edit the Jupyter
notebooks from GitHub.  When meeting in person, most learners use Google
Chromebooks which have limited programming capabilities, but easy use of a web
browser.
1. Assigning facilitators to groups allows learners to build a more personal
connection with their facilitators, making them feel more comfortable asking
questions.
1. Group projects were performed using paired programming to allow learners to
collaborate and learn from each other.
1. We use the "sticky note" system from The Carpentries by which learners can
ask for help by putting up a colored sticky note (or a Zoom emoji in the case of
virtual meetings) [@becker_responding_2016].
1. We exposed the learners to different aspects of data science by bringing in
guest speakers from academics and industry. This allowed them to better put what
they were learning into context and think about how they might use the skills
they were learning in potential future careers.

### Learner experiences

We surveyed learners anonymously after each Club and Summer Experience and found
that they all felt like they had improved their skills in Python programming,
problem solving and critical thinking, and collaboration.
Furthermore, for the 2019 instance of Club we asked that all participants take a
pre-test and a post-test.
While only five participants recorded their post-test, all of them answered more
questions correctly on the post-test than the pre-test (range 1-8 more questions
correct out of 11).

Overwhelmingly, learners' favorite parts are the guest speakers and the project.
These aspects of our curriculum expose learners to new fields and allow them to
apply their newfound coding skills to asking an interesting question.
About a third of participants claim that they are now more interested in
pursuing a career in computer or data science.

# Acknowledgements

We would like to acknowledge our faculty co-sponsors Maureen Sartor, PhD &
Cristina Mitrea, PhD.
We appreciate the continued support of U-M DCMB staff and faculty including
Julia Eussen, Mary Freer, Linda Peasley, Jane Weisner, Brian Athey, PhD, and
Margit Burmeister, PhD.
We are grateful for the resources provided by the national Girls Who Code
organization.

Our programming is made possible by the dedication of past and present Executive
Committee members, Club and Summer Experience Facilitators & Capstone Project
mentors including Alex Weber, Arushi Varshney, Sophie Hoffman, Hojae Lee,
Ruma Deb, Saige Rutherford, Michelle McNulty, Bailey Peck, Chloe Whicker,
Carolina Rojas Ramirez, Verity Sturm, Zoe Drasner, Sarah Latto, Emily
Roberts, Angel Chu, Vivek Rai, Hillary Miller, Ashton Baker, Murchtricia
Charles, Lauren Jepsen, and Aubrey Annis.
TODO: add 2019, 2020, & 2021 facilitators not already listed.

Our student organization received funding from the U-M Office of Graduate and
Postdoctoral Studies, Girls Who Code Support Fund, Department of Computational
Medicine and Bioinformatics, anonymous donations from Giving Blue Day 2019,
Endowment in Basic Sciences.
The 2019 Summer Experience was sponsored by Zingerman’s Delicatessen, U-M
Statistics Department, U-M Detroit Center, Dell, Cisco, U-M Department of
Computational Medicine and Bioinformatics, U-M Biostatistics Department.
We also thank the students who have participated in our Club and Summer
Experience events.

# Funding

MD, VKN, and KLS received support from the NIH Training Program in Bioinformatics (T32
GM070449).
MD, ZL, and BNW received support from the National Science Foundation Graduate
Research Fellowship Program under Grant No. DGE 1256260.
ZL and BNW received support from the NIH Training Program in Genomic Science
(T32-HG000040-22).
KLF received support from The University of Michigan NIDA Training Program in
Neuroscience (T32-DA7281) and from the NIH Early Stage Training in the
Neurosciences Training Grant (T32-NS076401).
SNT was supported by the Molecular Mechanisms of Microbial Pathogenesis training
grant (NIH T32 AI007528).
VKN was supported by a NIH Research Project Grant on Breast Cancer Disparities (RO1-ES028802) and the CDC through the National Institute for Occupational Safety and Health (NIOSH) Pilot Project Research Training Program (T42-OH008455).
Any opinions, findings, and conclusions or recommendations expressed in this
material are those of the authors and do not necessarily reflect the views of
the National Science Foundation.

# Author Contributions

MD, KLS, ZL, and BNW wrote the initial draft of the manuscript.
All authors contributed to the curriculum and reviewed the manuscript.

# Conflicts of Interest

None.

# References
