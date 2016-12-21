

- [Overview](#overview)
- [Objective](#objective)
- [Course Structure:](#course-structure)
	- [Lecture Times](#lecture-times)
	- [Course Website](#course-website)
	- [Office Hours](#office-hours)
- [Evaluation](#evaluation)
- [Grading](#grading)
- [Absence Policies](#absence-policies)
- [Schedule](#schedule)
- [Slides](#slides)
- [Assignments](#assignments)
- [Final Projects](#final-projects)
- [QA Site](#qa-site)
- [Required Texts](#required-texts)
- [Special Material required for class](#special-material-required-for-class)
- [Policies](#policies)
- [Changes](#changes)


# Overview

We will focus in the study of Machine Learning techniques, and their applications. Emphasis will be on geological, planetary and astronomical applications. Course will cover basic and state of the art techniques, as well as validation techniques for each algorithm.

# Objective

Students will be able to implement and validate different Machine Learning techniques in datasets related to Planetary Sciences, Earth Sciences and Astronomy. Students will learn the difference between supervised and unsupervised learning.

# Course Structure

## Lecture Times

Two lectures will be held per week on Mondays and Wednesdays from 10:00 AM to 10:50 AM. Both lectures will be in room 312 in the Kuiper Space Sciences Building.

## Course Website

Lectures, homework assignments and general information on the course will be available online in the following website: https://leonpalafox.github.io/MLClass/

## Office Hours

I will be available for questions and discussions after lectures. I will have office hours from 13:00 – 14:00 on Tuesdays and Thursdays. Otherwise, the students can make an appointment.

# Evaluation

The evaluation will consist of:

- Final Project will be 60% of the Final Evaluation.
    - The final project will consist in the correct use and validation of one Machine Learning technique in a dataset related to the student field of study.
	- The students can form teams of up to three persons.
	- Graduate students and teams need to write an 8-page report on the data, methodology and conclusions. In addition, make a 10-minute presentation of their work.
	- Undergraduate students and teams need to write a 5-page report on the data, methodology and conclusions. They can write an 8-page report for extra credit. Students have to make a 5-minute presentation of their work. Students can do a 10-minute presentation for extra credit.
	- Teams consisting of Graduate and Undergraduate students need to write an 8-page report and prepare a 10-minute presentation. Undergraduate students in the team will be given extra credit.
- In class participation will be 40% of the Final Evaluation
	- In class participation will consist on programming assignments, assigned readings reports and two quizzes. 
		- Graduate students quizzes will consists of five questions and Undergraduate students’ quizzes will consist of four questions. Undergraduate students can answer the five questions for extra credit.
	- Assignments for Graduate students will have extra requirements. Undergraduate students can meet these requirements for extra credit.

There will be an additional 10% extra credit opportunity by submitting additional reports, extracurricular projects and extra participation during the classes.

Homework assignments submitted after the established due date will be accepted. Assignments submitted after the due date will have a penalty of 20%.

# Grading
Final project: 60%

In-class participation: 40%

Grades are assigned as follows:

-	A≥90%
-	B≥75% and <90%
-	C≥60% and <75%
-	D≥50% and <60%
-	F<50%

# Absence Policies
Attendance to normal sessions is not mandatory.

In case of extraordinary circumstances and the students miss either of the quizzes; there will be opportunity for an additional quiz. The instructor will set the date of the make-up quiz. There will be only a single date for additional quizzes.

Circumstances that merit an additional quiz are:

- Observance of religious holidays
- Sickness 
- Absences preapproved by the UA Dean of Students (or Dean’s designee)
- Field Trips / Conferences / Meetings

# Number of required examinations and papers

For Graduate students, there will be two quizzes, four assignments and one final project.

For Undergraduate students, there will be two quizzes, four assignments and one final project.

# Schedule

1.	[Introduction](http://nbviewer.jupyter.org/github/leonpalafox/MLClass/blob/master/Chapter1Introduction/Introduction.ipynb?flush_cache=true) (Week 1)
  1. What is Machine Learning?
  2. Modern applications of Machine Learning.
  3. [Python-Pandas Introduction.](http://nbviewer.jupyter.org/github/leonpalafox/MLClass/blob/master/Chapter1Introduction/Introduction_PythonPandas.ipynb?flush_cache=true)
2.	Fundamentals (Week 1-2, 1 assignment)
  1. [Matrix Algebra](http://nbviewer.jupyter.org/github/leonpalafox/MLClass/blob/master/Chapter2Fundamentals/MatrixAlgebra.ipynb)
  2. [Probability Distributions](http://nbviewer.jupyter.org/github/leonpalafox/MLClass/blob/master/Chapter2Fundamentals/Probability%20Distributions.ipynb)
3.	Supervised Learning Techniques. (Week 3-6, 1 assignments, 1 quiz)
  1. Regression [First Example](http://nbviewer.jupyter.org/github/leonpalafox/MLClass/blob/master/Chapter3Regression/Regression.ipynb?flush_cache=true) [Second Example](http://nbviewer.jupyter.org/github/leonpalafox/MLClass/blob/master/Chapter3Regression/Regression%202.ipynb) [Data Science](https://github.com/leonpalafox/MLClass/blob/master/Chapter3Regression/House%20Prices%20Analysis.ipynb) 
  2. Classification
    1. [Logistic Regression.](http://nbviewer.jupyter.org/github/leonpalafox/MLClass/blob/master/Chapter3Regression/LogisticRegression.ipynb)
    2. [Support Vector Machines.](http://nbviewer.jupyter.org/github/leonpalafox/MLClass/blob/master/Chapter4SVMs/SVMNotebook.ipynb)
    3. Artificial Neural Networks
    4. [Deep Learning](http://nbviewer.jupyter.org/github/leonpalafox/MLClass/blob/master/Chapter5NNs/AutoEoncoderNN.ipynb)
    5. Convolutional Neural Networks [Convolutions Example](http://nbviewer.jupyter.org/github/leonpalafox/MLClass/blob/master/Chapter5NNs/ConvolutionsExample.ipynb)
		1. [TensorFlow Classifier](https://github.com/leonpalafox/MLClass/blob/master/Chapter5NNs/TensorFlow/CNNDemo.py)
		2. [TensorFlow CNN](https://github.com/leonpalafox/MLClass/blob/master/Chapter5NNs/TensorFlow/CNNDemo.py)
4. Validation Methods (Week 7-8, 1 assignment)
  1. [Cross Validation](http://nbviewer.jupyter.org/github/leonpalafox/MLClass/blob/master/Chapter6Validation/CrossValidationRegression.ipynb)
  2. Bias – Variance Analysis
  3. [ROC and AUC] (http://nbviewer.jupyter.org/github/leonpalafox/MLClass/blob/master/Chapter6Validation/ROC%20and%20AUC.ipynb)
5. Supervised Learning within the context of Planetary Science (Week 9-10)
6. Unsupervised Learning Techniques (Week 11-15, 1 assignment, 1 quiz)
  1. Clustering
    1. [K-Means](http://nbviewer.jupyter.org/github/leonpalafox/MLClass/blob/master/Chapter7Clustering/KMeansExample.ipynb)
    2. Applications
  2. Dimensionality Reduction techniques
    1. (Principal Component Analysis)[https://github.com/leonpalafox/MLClass/blob/master/Chapter8PCAICA/PCA%20Analysis.ipynb] 
    2. [Independent Component Analysis](http://nbviewer.jupyter.org/github/leonpalafox/MLClass/blob/master/Chapter8PCAICA/ICA%20analysis.ipynb)
    3. T-SNE
7. Unsupervised Learning within the context of Planetary Science (Week 15-16)
8. Final Project Presentations (Week 17)

# Slides

- [Lecture 1 - Intro, Front matter](https://github.com/leonpalafox/MLClass/blob/master/Slides/PTYS545B_Lecture1.pdf)
- [Lecture 2 - Outline](https://github.com/leonpalafox/MLClass/blob/master/Slides/PTYS545B_Lecture2.pdf)
- [Lecture 3 - Probability](https://github.com/leonpalafox/MLClass/blob/master/Slides/PTYS545B_Lecture3.pdf)
- [Lecture 4 - Linear Regression](https://github.com/leonpalafox/MLClass/blob/master/Slides/PTYS545B_Lecture4.pdf)
- [Lecture 5 - Linear Regression Part 2](https://github.com/leonpalafox/MLClass/blob/master/Slides/PTYS545B_Lecture5.pdf)
- [Lecture 6 - Logistic Regression](https://github.com/leonpalafox/MLClass/blob/master/Slides/PTYS545B_Lecture6.pdf)
- [Lecture 7 - Support Vector Machine](https://github.com/leonpalafox/MLClass/blob/master/Slides/PTYS545B_Lecture7.pdf)
- [Lecture 8 - Support Vector Machine](https://github.com/leonpalafox/MLClass/blob/master/Slides/PTYS545B_Lecture8.pdf)
- [Lecture 9 - Neural Networks](https://github.com/leonpalafox/MLClass/blob/master/Slides/PTYS545B_Lecture9.pdf)
- [Lecture 10 - Neural Networks and Autoencoders](https://github.com/leonpalafox/MLClass/blob/master/Slides/PTYS545B_Lecture10.pdf)
- [Lecture 11 - Neural Networks and Autoencoders](https://github.com/leonpalafox/MLClass/blob/master/Slides/PTYS545B_Lecture11.pdf)
- [Lecture 12 - Convolutional Neural Networks](https://github.com/leonpalafox/MLClass/blob/master/Slides/PTYS545B_Lecture12.pdf)
- [Lecture 13 - Convolutional Neural Networks](https://github.com/leonpalafox/MLClass/blob/master/Slides/PTYS545B_Lecture13.pdf)
- [Lecture 14 - Convolutional Neural Networks](https://github.com/leonpalafox/MLClass/blob/master/Slides/PTYS545B_Lecture14.pdf)
- [Lecture 15 - Validation Methods](https://github.com/leonpalafox/MLClass/blob/master/Slides/PTYS545B_Lecture15.pdf)
- Lecture 16 - Validation Methods(This class was a done completely in a Python notebook)
- [Lecture 17 - Quiz and Bias-Variance](https://github.com/leonpalafox/MLClass/blob/master/Slides/PTYS545B_Lecture17.pdf)
- [Lecture 18 - ROC and AUC](https://github.com/leonpalafox/MLClass/blob/master/Slides/PTYS545B_Lecture18.pdf)
- [Lecture 19 - ROC and Applications of Machine Learning](https://github.com/leonpalafox/MLClass/blob/master/Slides/PTYS545B_Lecture19.pdf)
- [Lecture 20 - Applications of Machine Learning - Planetary Science](https://github.com/leonpalafox/MLClass/blob/master/Slides/PTYS545B_Lecture20.pdf)
- [Lecture 21 - Applications of Machine Learning - Planetary Science](https://github.com/leonpalafox/MLClass/blob/master/Slides/PTYS545B_Lecture21.pdf)
- [Lecture 22 - Applications of Machine Learning - Planetary Science](https://github.com/leonpalafox/MLClass/blob/master/Slides/PTYS545B_Lecture22.pdf)
- [Lecture 23 - Unsupervised Learning](https://github.com/leonpalafox/MLClass/blob/master/Slides/PTYS545B_Lecture23.pdf)
- [Lecture 24 - K Means](https://github.com/leonpalafox/MLClass/blob/master/Slides/PTYS545B_Lecture24.pdf)
- [Lecture 25 - Principal Component Analysis](https://github.com/leonpalafox/MLClass/blob/master/Slides/PTYS545B_Lecture25.pdf)
- [Lecture 26 - Independent Component Analysis](https://github.com/leonpalafox/MLClass/blob/master/Slides/PTYS545B_Lecture26.pdf)
- [Lecture 27 - t-SNE](https://github.com/leonpalafox/MLClass/blob/master/Slides/PTYS545B_Lecture27.pdf)
- [Lecture 28 - Final Lecture](https://github.com/leonpalafox/MLClass/blob/master/Slides/PTYS545B_Lecture28.pdf)


# Notes

- [Lecture 1 - Ali M. Bramson](https://github.com/leonpalafox/MLClass/blob/master/Notes/Lecture1_notes_Bramson.pdf)
- [Lecture 2 - Jessie Brown](https://github.com/leonpalafox/MLClass/blob/master/Notes/Lecture2_notes_Brown.pdf)
- [Lecture 3 - Ali M. Bramson](https://github.com/leonpalafox/MLClass/blob/master/Notes/Lecture3_notes_Bramson.pdf)
- [Logistic Regression - Alexander Prescott](https://github.com/leonpalafox/MLClass/blob/master/Notes/LogisticRegression - 09142016_notes_Prescott.pdf)
- [Linear Regression - Ali M. Bramson](https://github.com/leonpalafox/MLClass/blob/master/Notes/Linear Regression - Bramson_MLnotes_2016-09-19.pdf)
- [SVMs - Ali M. Bramson](https://github.com/leonpalafox/MLClass/blob/master/Notes/SVMs - Bramson_MLnotes_2016-09-21.pdf)
- [NN - Ali M. Bramson](https://github.com/leonpalafox/MLClass/blob/master/Notes/NN - Bramson_MLnotes_2016-09-26.pdf)
- [NN - Ali M. Bramson](https://github.com/leonpalafox/MLClass/blob/master/Notes/NN - Bramson_MLnotes_2016-09-28.pdf)
- [Overview of the first half of the class - Alexander Prescott](https://github.com/leonpalafox/MLClass/blob/master/Notes/midtermpaper.pdf)

# Assignments

- [Homework 1](https://github.com/leonpalafox/MLClass/blob/master/Assignments/HW1.pdf)
- [Homework 2](https://github.com/leonpalafox/MLClass/blob/master/Assignments/HW2.pdf)
- [Homework 3](https://github.com/leonpalafox/MLClass/blob/master/Assignments/HW3.pdf)

# Final Projects

- [Using t-SNE to analyse exoplanets](https://github.com/leonpalafox/MLClass/blob/master/FinalProjects/AnalysisofExoplanets.pdf)
- [Analysis of the ice distribution of Arcadia Planitia](https://github.com/leonpalafox/MLClass/blob/master/FinalProjects/IceDistributionArcadia.pdf)
- [Analysis of the Kuiper Belt populations](https://github.com/leonpalafox/MLClass/blob/master/FinalProjects/KuiperBeltPopulations.pdf)
- [Using NN to map dunes distribution](https://github.com/leonpalafox/MLClass/blob/master/FinalProjects/MappingDunes.pdf)


# QA Site

- We will be using Piazza (http://piazza.com/arizona/fall2016/ptys595b)

# Required Texts

The course has no mandatory text and is self-contained; however, the following books are helpful resources for students:

- Bishop, Christopher M. Pattern recognition and machine learning. Springer, 2006. 
- Rogers, Simon, and Mark Girolami. A first course in machine learning. CRC Press, 2011. (http://www.dcs.gla.ac.uk/~srogers/firstcourseml/ , Available Online at the UA Library webpage)
- James, Gareth, et al. An introduction to statistical learning. New York: Springer, 2013. (http://www-bcf.usc.edu/~gareth/ISL/)
- Petersen, Kaare Brandt, and Michael Syskind Pedersen. The matrix cookbook. Technical University of Denmark 7 (2008): 15. (https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf)

# Special Material required for class

The students will need access to a Personal Computer with the Matlab Scientific Program or the Python Programming environment

# Policies

The students will be able to use pagers/cellphones in the classroom as long as they set them up in silence mode. 

## Academic Integrity Policy

Students are encouraged to share intellectual views and discuss freely the principles and applications of course materials. However, graded work/exercises must be the product of independent effort unless otherwise instructed. Students are expected to adhere to the UA Code of Academic Integrity as described in the UA General Catalog. See http://deanofstudents.arizona.edu/academic-integrity/students/academic-integrity.

## Threatening behaviour Policy

Threatening Behaviour is prohibited.

The UA Threatening Behaviour by Students Policy prohibits threats of physical harm to any member of the University community, including to oneself. See http://policy.arizona.edu/education-and-student-affairs/threatening-behavior-students.

## Accessibility and Accommodations

It is the University’s goal that learning experiences be as accessible as possible.  If you anticipate or experience physical or academic barriers based on disability or pregnancy, please let me know immediately so that we can discuss options.  You are also welcome to contact Disability Resources (520-621-3268) to establish reasonable accommodations.

Please be aware that the accessible table and chairs in this room should remain available for students who find that standard classroom seating is not usable.

## Notification on offensive content

Some of the datasets used to exemplify Machine Learning algorithms might content topics like rape, murder, deaths by cancer, diabetes and other illnesses.
UA Nondiscrimination and Anti-harassment Policy 
The University is committed to creating and maintaining an environment free of discrimination; see http://policy.arizona.edu/human-resources/nondiscrimination-and-anti-harassment-policy.
Our classroom is a place where everyone is encouraged to express well-formed opinions and their reasons for those opinions. We also want to create a tolerant and open environment where such opinions can be expressed without resorting to bullying or discrimination of others.

# Changes

The information contained in this syllabus other than grade and absence policies may be subject to change with reasonable advance notice.


