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
  - name: TODO - all other contributors
    orcid: TODO
    affiliation: TODO
  - name: Zena Lapp^[corresponding author]
    orcid: 0000-0003-4674-2176
    affiliation: 1
  - name: Brooke N. Wolford^[corresponding author]
    orcid: TODO
    affiliation: 1
affiliations:
  - name: Department of Computational Medicine & Bioinformatics, University of Michigan
    index: 1
date: 30 Apr. 2021
bibliography: paper.bib
---

# Summary

<!-- pasted from our PyCon 2020 talk proposal -->
We are Bioinformatics PhD students at the University of Michigan who started a
local chapter of Girls Who Code to provide a fun and supportive environment for
high school women to learn the power of coding. Our goal was to cover basic
coding topics and data science concepts through live-coding and hands-on
practice. However, we couldn’t find a resource that exactly met our needs. Over
the past three years, we have developed a curriculum and instructional format
using Jupyter notebooks to effectively teach introductory Python for data
science. This method, inspired by The Carpentries organization
[@wilson_software_2016], uses bite-sized lessons followed by independent
practice time to reinforce coding concepts, and culminates in a data science
capstone project using real-world data. We believe our open curriculum is a
valuable resource to the wider education community and hope that educators will
use and improve our lessons, challenge problems, and teaching best-practices.
Anyone can contribute to our educational materials on GitHub
(https://github.com/GWC-DCMB).


# Statement of Need

As women in the Department of Computational Medicine and Bioinformatics at the University of Michigan, we experience the gender gap in our field first hand. 
XX% of doctoral students in our field are women and XX% of bioinformatics faculty are women (REF). 
Previous research has shown that women leave computer science and related majors during their undergraduate careers because they feel less prepared than the men in their cohort (REF). 
The majority of the Club’s founders began coding in our undergraduate careers or later. 
We wanted to provide a safe place for local young women to begin coding in high school, and develop confidence in themselves and their computational skills before college. 
A national organization, Girls Who Code, whose mission and values aligned with ours was founded in 2012. 
Girls Who Code’s mission is to close the gender gap in technology (https://girlswhocode.com/2015report/). 
In 2017 we began a student organization at the University of Michigan, and for the past four academic years we have registered annually as a recognized Girls Who Code Club because the national organization provided name recognition, curriculum resources, guidance for a capstone Impact Project, and a framework for launching a Club. 
In 2019 we launched a Data Science Summer Experience which is unaffiliated with the national Girls Who Code organization.

The national Girls Who Code organization provides a curriculum that teaches website and application development through programming languages like HTML and Java. 
However, our biomedical science graduate students generally have limited experience with these languages. 
Data Scientist was rated the #1 job in America by Glassdoor in 2016-2019, #3 in 2020, and #2 in 2021 (https://www.glassdoor.com/research/best-jobs-2019/#). 
We believe career exploration in data science will optimally prepare our students for careers that provide financial stability. 
By leveraging the data science expertise of our Club facilitators, we created a specialized curriculum focused on computational data science in the Python programming language.

Girls Who Code encourages participants to learn programming skills while working on an Impact Project website or application throughout the Club (https://hq.girlswhocode.com/project-gallery?). 
We created an open source Data Science curriculum that teaches the requisite Python and statistics skills to complete a Capstone Project, which is a data analysis project on a data set of interest. 
Using this curriculum, we employ participatory live coding as used by The Carpentries (pmid:24715981) which is an effective method that engages learners (https://doi.org/10.1371/journal.pcbi.1008090). 
With paired activities our curriculum follows the “I do, we do, you do” didactic paradigm (Fisher D, Frey N. Better Learning Through Structured Teaching: A Framework for the Gradual Release of Responsibility. ASCD; 2013.).
We provide open-source resources for both in-person and virtual versions of our curriculum, including videos corresponding to each lesson.
While we developed this curriculum for our Girls Who Code Club and Summer Experience, we believe that it can be widely used for teaching introductory coding for data science. 

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
instructors took notes on their experience and fixed any problems afterward.
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



## Learning Objectives



## Course Content



## Instructional Design
<!-- teaching philosophy / pedagogy -->



## Experience of Use

We have used this curriculum to teach Summer Experince and Club in person in 2019 and virtually in 2020.
For the in person instances, we taught the curriculum through live coding, a tenchique we learned from [The Carpentries](https://carpentries.org/) where the instructor types and explains the code while the learners follow along in real time.
For the virtual instances, we used a flipped classroom approach where the learners watch videos of instructors explaining the material through "live" coding and follow along. 
For both in person and virtual instances, we had several facilitators present at each session to answer questions and help learners debug. 
Furthermore, one or two facilitators were assigned to each project group to help learners define data analysis questions, develop and execute a data analysis plan, visualize and communicate their findings, and troubleshoot coding problems. 

We credit the success of our curriculum not only to the skill of the instructors, but also to the way we organized and executed the lessons and project:
1. The instructors and learners all used Google co-lab to write and execute code in Jupyter notebooks.
We chose this option because learners do not have to install any programs to use Google co-lab and you can easily open and edit the Jupyter notebooks from GitHub.  
1. Assigning facilitators to groups allows learners to build a more personal connection with their facilitators, making them feel more comfortable asking questions.
1. We use the "sticky note" system from The Carpentries by which learners can ask for help by putting up a colored sticky note (or Zoom emoji).
1. We exposed the learners to different aspects of data science by bringing in speakers from academics and industry. 
This allowed them to better put what they were learning into context and think about how they might use the skills they were learning in potential future careers.

### Learner experiences 

We surveyed learners anonymously after each Club and Summer Experience and found that they all felt like they had improved their skills in Python programming, problem solving and critical thinking, and collaboration. 
Furthermore, for the 2019 instance of Club we asked that all participants take a pre-test and a post-test. 
While only five participants recorded their post-test, all of them answered more questions correctly on the post-test than the pre-test (range 1-8 more questions correct out of 11). 
 
Overwhelmingly, learners' favorite parts are the guest speakers and the project. 
These aspects of our curriculum expose learners to new fields and allow them to apply their newfound coding skills to asking an interesting question. 
About a third of participants claim that they are now more interested in pursuing a career in computer or data science. 

# Acknowledgements

We thank the Department of Computational Medicine and Bioinformatics at the
University of Michigan for sponsoring our student organization.

TODO: thank admins who help us: Mary Freer, who else?

We thank the students who have participated in our Club and Summer Experience events.

# Funding

KLS and MD received support from the NIH Training Program in Bioinformatics (T32
GM070449).
ZL, BNW, and MD received support from the National Science Foundation Graduate Research
Fellowship Program under Grant No. DGE 1256260.
ZL and BNW recieved support from the NIH Training Program in Genomic Science (T32-HG000040-22).

Any opinions, findings, and conclusions or recommendations expressed in this
material are those of the authors and do not necessarily reflect the views of
the National Science Foundation.

# Author Contributions



# Conflicts of Interest

None.

# References