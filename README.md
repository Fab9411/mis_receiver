# mis_receiver
Experiment for the study of misinformation receivers' behaviour.

## Brief summary
In this experiment, participants are asked to perform a basic task: categorizing news articles as fake or reliable. They gain a point each time they correctly guess news' type and zero points when they are not able to do so. Starting from this basic task, you can add many treatments and changes to the experiment. In particular, you can:

- Show fictional sources for each news
- Show real state of news after each round
- Change percentage of fake news over the total (default is 50/50)
- Change percentage of fake news published by each fictional source (default is Source B 100% reliable and Source A 0% reliable, T2: 90%-10%, T3: 80%-20%)
- Show screenshots or images for each news article
- Show different screenshots according to treatment. For example, show website screenshots to control group and Facebook screenshots to treatment group

The standard setting is on 10 rounds, with 5 reliable news and 5 fake news, but you can change both the number of rounds and the percentage of fake news in them. News articles are randomly picked from the two datasets of reliable and fake news. However, this random pick is consistent from a session to the other and for each participant, thanks to the use of a fixed random_state.

## How to make it work
### Dataset
In the demo, the dataset is downloaded by Kaggle (https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset). In order to use your own data, follow this procedure after having deleted the demo dataset:
1. First thing you should do is having a dataset of reliable news (called "true_df") and a dataset of fake news (called "fake_df"), both of them needs to be in csv. Column names must be "title" and "text".
2. Put those two datasets in the data folder of the oTree experiment.

### Images
1. Go in the _static folder of your oTree folder
2. Create a folder named "mis_receiver"
3. Go inside it
4. Create a folder named "images"
5. Go inside it
6. Create a folder named "websites" 
7. Put there all the images you want to show
8. Make sure each image have the same name of the news title they are related to, except for special symbols not allowed for file naming in Windows
From now on, proceed only if you want to show different images according to treatment
9. Return to "images" folder
10. Create a "facebook" folder inside it
11. Put there all images you want to show to participant in the Facebook treatment
12. Again, make sure each image is named with the exact news title they are related to, except for special symbols

## Settings
The administrator, before starting a session, can control each one of the above-mentioned treatments and features.
In particular:
![image](https://user-images.githubusercontent.com/55483523/134367718-caf50986-5f79-4c07-9136-d2157025979c.png)
1. debunking: when active, it shows the real state of news articles after each round
2. source: when active, it shows fictional sources of news articles (default is Source A and Source B, but names can be changed in models.py -> Constants -> def setting_sources)
3. treatment: 
- T1: Source B publish 100% reliabe news and Source A publish 0% reliable news
- T2: Source B publish 90% reliabe news and Source A publish 10% reliable news
- T3: Source B publish 80% reliabe news and Source A publish 20% reliable news
4. images: when active, it shows the proper image for each news article, picking the image from the folder _static/mis_receiver/images/websites
5. social: when active, it shows the proper image for each news article, picking the image from the folder _static/mis_receiver/facebook/websites
