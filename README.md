# curriculum-notebooks

[![build](https://github.com/GWC-DCMB/curriculum-notebooks/workflows/build/badge.svg)](https://github.com/GWC-DCMB/curriculum-notebooks/actions)
[![check](https://github.com/GWC-DCMB/curriculum-notebooks/workflows/check/badge.svg)](https://github.com/GWC-DCMB/curriculum-notebooks/actions)
[![license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE.md)
[![doi](http://img.shields.io/badge/DOI-10.1101/2021.06.17.448726-B31B1B.svg)](https://doi.org/10.1101/2021.06.17.448726)

Our Club and Summer Experience formats cover slightly different topics with significant overlap.
This repo contains all of the Jupyter notebooks used in either or both of them.
For the exact curriculum order & topics covered, see the corresponding repos:

- [Club](https://github.com/GWC-DCMB/ClubCurriculum)
- [Summer](https://github.com/GWC-DCMB/SummerExperience)

The Lessons directory contains live coding demos meant to introduce each topic in ~15 minute interactive mini-lessons.
These lessons are delivered in Jupyter Notebooks in a "fill in the blanks" style.
Instructors will guide students through each lesson and the students will follow along,
filling in the blanks on their own documents as we go.

The Practices directory contains practice exercises for students to spend ~30 minutes to solidify skills taught in each mini-lesson.
These practices are delivered in Jupyter Notebooks in a "fill in the blanks" style.
Students will work with partners/groups to fill in blanks within the documents,
using code from the corresponding lesson as a resource.
Instructors will work closely with students to help them complete and understand each practice.

Both Lessons and Practices directories contain `_Keys` subdirectories with correctly completed versions of each exercise.
Sometimes GitHub doesn't render Jupyter notebooks in a timely manner,
so we use continuous integration to compile all notebook keys to PDFs.
Take a look at the [Lesson](Lessons/_Keys/pdf) & [Practice](Practices/_Keys/pdf) Key PDFs if you only want to view them quickly in your browser.


## Links

|   | Lesson Video | Lesson Notebook | Practice Notebook |
|---|---|---|---|
| **Module I: Jupyter Setup** |
| 1 | https://youtu.be/plRRJ1zupgI | None, just watch the video. | [Practice01 Jupyter Setup](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Practices/Practice01_Jupyter-Setup.ipynb) |
| **Module II: Coding Fundamentals** |
| 2 | https://youtu.be/czhcehpotos | [Lesson02 HelloWorld and Variables](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Lessons/Lesson02_HelloWorld_Variables.ipynb) | [Practice02 HelloWorld and Variables](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Practices/Practice02_HelloWorld_Variables.ipynb) |
| 3 | https://youtu.be/cGVIyeGv2bw | [Lesson03 Variables and Types](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Lessons/Lesson03_Variables_Types.ipynb) | [Practice03 Variables and Types](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Practices/Practice03_Variables_Types.ipynb) |
| 4 | https://youtu.be/xY51hfthvrw | [Lesson04 Lists Intro](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Lessons/Lesson04_Lists_Intro.ipynb) | [Practice04 Lists Intro](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Practices/Practice04_Lists_Intro.ipynb) |
| 5 | https://youtu.be/g9U_q5yWjrQ | [Lesson05 Indexing](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Lessons/Lesson05_Indexing.ipynb) | [Practice05 Indexing](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Practices/Practice05_Indexing.ipynb) |
| 6 |   | [Lesson06 2D Lists Intro](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Lessons/Lesson06_2D_Lists_Intro.ipynb)  (legacy lesson) | [Practice06 2D Lists Intro](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Practices/Practice06_2D_Lists_Intro.ipynb) |
| 7 |   | [Lesson07 2D Lists Indexing](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Lessons/Lesson07_2D_Lists_Indexing.ipynb)  (legacy lesson) | [Practice07 2D Lists Indexing](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Practices/Practice07_2D_Lists_Indexing.ipynb) |
| 8 | https://youtu.be/WLhDlhKFB9Q | [Lesson08 Logic](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Lessons/Lesson08_Logic.ipynb) | [Practice08 Logic](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Practices/Practice08_Logic.ipynb) |
| 9 | https://youtu.be/8oNvm0wxSQI | [Lesson09 Conditionals](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Lessons/Lesson09_Conditionals.ipynb) | [Practice09 Conditionals](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Practices/Practice09_Conditionals.ipynb) |
| 10 | https://youtu.be/DWKg4zxW47k | [Lesson10 Loops I](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Lessons/Lesson10_Loops1.ipynb) | [Practice10 Loops I](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Practices/Practice10_Loops1.ipynb) |
| 11 | https://youtu.be/uq5O70xnDO4 | [Lesson11 Loops II](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Lessons/Lesson11_Loops2.ipynb) | [Practice11 Loops II](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Practices/Practice11_Loops2.ipynb) |
| 12 | https://youtu.be/5bSf_BbBjms | [Lesson12 Using Functions and Methods](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Lessons/Lesson12_Functions_and_Methods.ipynb) | [Practice12 Using Functions and Methods](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Practices/Practice12_Functions_and_Methods.ipynb) |
| **Module III: Data Science Essentials** |
| 13 | https://youtu.be/QKno1TQwfWg | [Lesson13 Packages](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Lessons/Lesson13_Packages.ipynb) | [Practice13 Packages](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Practices/Practice13_Packages.ipynb) |
| 14 | https://youtu.be/-zY18Hlhpho | [Lesson14 Pandas Intro](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Lessons/Lesson14_Pandas-Intro.ipynb) | [Practice14 Pandas Intro](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Practices/Practice14_Pandas-Intro.ipynb) |
| 15 | https://youtu.be/3NUfZWbTCnc | [Lesson15 Pandas Reading](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Lessons/Lesson15_Pandas-Reading.ipynb) | [Practice15 Pandas Reading](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Practices/Practice15_Pandas-Reading.ipynb) |
| 16 | https://youtu.be/RbJzkDfo-yY | [Lesson16 Pandas Subsetting I](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Lessons/Lesson16_Pandas-Subsetting-I.ipynb) | [Practice16 Pandas Subsetting I](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Practices/Practice16_Pandas-Subsetting-I.ipynb) |
| 17 | https://youtu.be/4RnR65I3Xmg | [Lesson17 Pandas Subsetting II](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Lessons/Lesson17_Pandas-Subsetting-II.ipynb) | [Practice17 Pandas Subsetting II](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Practices/Practice17_Pandas-Subsetting-II.ipynb) |
| 18 | https://youtu.be/PoGMlBSRGEE | [Lesson18 Dictionaries](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Lessons/Lesson18_Dictionaries.ipynb) | [Practice18 Dictionaries](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Practices/Practice18_Dictionaries.ipynb) |
| 19 | https://youtu.be/98lgF7doe-c  | [Lesson19 Writing Functions](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Lessons/Lesson19_Functions.ipynb) | [Practice19 Writing Functions](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Practices/Practice19_Functions.ipynb) |
| 20 | https://youtu.be/qzTN0qEhMwk | [Lesson20 Numpy Intro](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Lessons/Lesson20_Numpy_Intro.ipynb) | [Practice20 Numpy Intro](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Practices/Practice20_Numpy_Intro.ipynb) |
| **Module IV: Basic Statistical Analysis** |
| 21 | https://youtu.be/qA4NCfefbQg | [Lesson21 Averages](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Lessons/Lesson21_Basic_Stats_I_Averages.ipynb) | [Practice21 Averages](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Practices/Practice21_Basic_Stats_I_Averages.ipynb) |
| 22 | https://youtu.be/g-Jto81Ei0c | [Lesson22 Percents](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Lessons/Lesson22_Basic_Stats_II_Percents.ipynb) | [Practice22 Percents](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Practices/Practice22_Basic_Stats_II_Percents.ipynb) |
| 23 | https://youtu.be/JBuVUdpTHoY | [Lesson23 Correlations](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Lessons/Lesson23_Basic_Stats_III_Correlations.ipynb) | [Practice23 Correlations](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Practices/Practice23_Basic_Stats_III_Correlations.ipynb) |
| 24 | https://youtu.be/j5P5THwDR_Q | [Lesson24 Significance](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Lessons/Lesson24_Basic_Stats_IV_Significance.ipynb) | [Practice24 Significance](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Practices/Practice24_Basic_Stats_IV_Significance.ipynb) |
| **Module V: Data Visualization** |
| 25 | https://youtu.be/I8R8v0-_xmY | [Lesson25 Line Graphs](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Lessons/Lesson25_LineGraphs.ipynb) | [Practice25 Line Graphs](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Practices/Practice25_LineGraphs.ipynb) |
| 26 | https://youtu.be/pFTh8bfezVw | [Lesson26 Scatterplots](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Lessons/Lesson26_Scatterplots.ipynb) | [Practice26 Scatterplots](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Practices/Practice26_Scatterplots.ipynb) |
| 27 | https://youtu.be/p7EsFg0aMRs | [Lesson27 Bar Charts and Histograms](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Lessons/Lesson27_BarCharts_Histograms.ipynb) | [Practice27 Bar Charts and Histograms](https://colab.research.google.com/github/GWC-DCMB/curriculum-notebooks/blob/master/Practices/Practice27_BarCharts_Histograms.ipynb) |

## Citation

We have written a manuscript describing our curriculum and the development
process. It is now available [on
bioRxiv](https://www.biorxiv.org/content/10.1101/2021.06.17.448726). If you
would like to cite our work, please use:

```
Duda et al., (2021). Teaching Python for Data Science: Collaborative development
of a modular & interactive curriculum. bioRxiv.
https://doi.org/10.1101/2021.06.17.448726
```

A bibtex entry for LaTeX users:

```
@article{duda_teaching_2021,
  title = {Teaching {{Python}} for {{Data Science}}: {{Collaborative}} Development of a Modular \& Interactive Curriculum},
  shorttitle = {Teaching {{Python}} for {{Data Science}}},
  author = {Duda, Marlena and Sovacool, Kelly L. and Farzaneh, Negar and Nguyen, Vy Kim and Haynes, Sarah E. and Falk, Hayley and Furman, Katherine L. and Walker, Logan A. and Diao, Rucheng and Oneka, Morgan and Drotos, Audrey C. and Woloshin, Alana and Dotson, Gabrielle A. and Kriebel, April and Meng, Lucy and Thiede, Stephanie N. and Lapp, Zena and Wolford, Brooke N.},
  year = {2021},
  month = jun,
  publisher = {{Cold Spring Harbor Laboratory}},
  doi = {10.1101/2021.06.17.448726},
  url = {https://doi.org/10.1101/2021.06.17.448726},
  journal = {bioRxiv},
  language = {en}
}
```
