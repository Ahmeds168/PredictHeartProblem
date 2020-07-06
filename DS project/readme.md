In this project I will use scikit-learn  to build Classification Tree , which uses continuous and categorical data from the UCI Machine Learning Repository to predict whether or not a patient has heart disease:

Classification Trees are an exceptionally useful machine learning method when you need to to know how the decisions are being made. For example, if you have to justify the predictions to your boss, Classification Trees are a good method because each step in the decision making process is easy to understand.

In this project I will...

Importing the Data From a File Missing Data

Identifying Missing Data Dealing with Missing Data Formatting the Data for Decision Trees Split data into Dependent and Independent Variables One-Hot-Encoding Building a Preliminary Classification Tree Using Cost Complexity Pruning Visualize Alpha Cross Validation For Finding the Best Alpha Building, Drawing, Interpreting and Evaluating the Final Classification Tree

Task 1: Import the modules that will do all the work The very first thing we do is load in a bunch of python modules. Python, itself, just gives us a basic programming language. These modules give us extra functionality to import the data, clean it up and format it, and then build, evaluate and draw the classification tree.

Task 2: Import the data Now we load in a dataset from the UCI Machine Learning Repository. Specifically, we are going to use the Heart Disease Dataset. This dataset will allow us to predict if someone has heart disease based on their sex, age, blood pressure and a variety of other metrics.

Task 3: Missing Data Part 1: Identifying Missing Data The biggest part of any data analysis project is making sure that the data is correctly formatted and fixing it when it is not. The first part of this process is dealing with Missing Data.

Missing Data is simply a blank space or surrogate value that indicates that we failed to collect data for one of the features. For example, if we forgot to ask someone's age, or forgot to write it down, then we would have a blank space in the dataset for that person's age.

There are two main ways to deal with missing data:

We can remove the rows that contain missing data from the dataset. This is relatively easy to do, but it wastes all of the other values that we collected. How a big of a waste this is depends on how important this missing value is for classification. For example, if we are missing a value for age, and age is not useful for classifying if people have heart disease or not, then it would be a illogical to throw out all of someone's data just because we do not have their age. We can impute the values that are missing. In this context impute is just a fancy way of saying "we can make an educated guess about about what the value should be". Continuing our example where we are missing a value for age, instead of throwing out the entire row of data, we can fill the missing value with the average age or the median age, or use some other, more sophisticated approach, to guess at an appropriate value.

Task 4: Missing Data Part 2: Dealing With Missing Data Since scikit-learn's classification trees do not support datasets with missing values, we need to figure out what to do these question marks. We can either delete these patients from the training dataset, or impute values for the missing data. First let's see how many rows contain missing values. Since only 6 rows have missing values, let's look at them. Now let's count the number of rows in the full dataset. So 6 of the 303 rows, or 2%, contain missing values. Since 303 - 6 = 297, and 297 is plenty of data to build a classification tree, we will remove the rows with missing values, rather than try to impute their values. We do this by selecting all of the rows that do not contain question marks in either the ca or thal columns:

Task 5: Format Data Part 1: Split the Data into Dependent and Independent Variables Now that we have taken care of the missing data, we are ready to start formatting the data for making a Classification Tree.

The first step is to split the data into two parts:

The columns of data that we will use to make classifications The column of data that we want to predict. We will use the conventional notation of X (capital X*) to represent the columns of data that we will use to make classifications and y (lower case *y) to represent the thing we want to predict. In this case, we want to predict hd (heart disease).

Task 6: Format the Data Part 2: One-Hot Encoding Now that we have split the data frame into two pieces, X, which contains the data we will use to make, or predict, classifications, and y, which contains the known classifications.

Task 7: Build A Preliminary Classification Tree At long last, the data is correctly formatted for making a Classification Tree. Now we simply split the data into training and testing sets and build the tree.
