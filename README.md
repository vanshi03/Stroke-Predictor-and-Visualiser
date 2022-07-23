# Stroke-Predictor-and-Visualiser
## I created a website on stroke prediction and visualisation
### Blueprint 🔷
<ul>
  <li>Build a model , Language used : Python</li>
  <li>Develop front-end of website, Language used : HTML,CSS</li>
  <li>Integrate both fron-end and back-end(model) , Framework used : Flask</li>
</ul>

### 1️⃣ Building the model
<ul>
  <li>Import modules and read the dataset</li>
  <li>Preprocess the data</li>
  <li>Understand the features </li>
  <li>Visualise the correlation of input variables with target variables</li>
  <li>Convert Categorical data to numeric data using encoding</li>
  <li>Divide the data into input and output variables</li>  
  <li>Balance the dataset using SMOTE Analysis</li>  
  <li>Split data into training and testing</li>
  <li>Feature Scaling</li>
  <li>Calculating and Visualising cross-validation scores using different binary classification models</li>  
  <li>Calculating and Visualising accuracy of different binary classification models</li>
  <li>Selecting model with best and highest accuracy</li>
  <li>Saving the model in .pkl file</li>
</ul>


### 2️⃣ Developing the front-end
*Since we will be integrating our front-end and model using flask , make sure to save your files in mentioned file heirarchy*<br>
HTML Files : templates/file_name.html<br>
CSS Files : static/css_file_name.css
<ul>
  -----HTML-----
  <li>Make an index.html file inside template folder</li>
  <li>Develop an HTML form</li>
  <li>The form after submission will go to a flask file(app.py) , so form-action will be the route/url to the method that will be called after form submission</li>
  <li>Values of dropdown-option should match with the values you got after encoding your data while building the model</li>
  <li>Create variable inside jinja synatx : {{}} so that later this variable can be used to display your result after from processing</li>
  <br>
  <li> Make another Visualisation.html file to display your visualisation</li>
  <li> Use an iframe or img src to render the url of the saved visualisation</li>
  ----CSS-----
  <li>Make an css file inside static folder and style your form</li>
  <li>Link your css toindex.html using jinja : {{}}</li>
</ul>

### 3️⃣ Integration
Prerequisite : Install the flask framework on your system using $ pip install Flask
<ul>
  <li>Create a python file -> app.py </li>
  <li>Import flask and other libraries in this file</li>
  <li>Load your model(model.pkl)</li>
  <li>Route your root directory using @app.route('/')</li>
  <li>Render index.html template inside a method</li>
  <li>Next after routing to index.html now route to form by mentioning the url u mentioned in form-action</li>
  <li>Make a method that will contain functionalities you want after your form submits</li>
  <li>For prediction part use your model and form-data </li>
  <li>Render it to your index.html where the result will be viewed</li>
  <li>For Visualisation part you'll save your visualisation of model(here, random forest) in .svg format inside static\images\img_name.svg</li>
  <li>Render it to your Visualisation.html where the Visualisation will be viewed</li> 
</ul>

### How to run your flask application
<ul>
  <li>Open Anaconda prompt</li>
  <li>Go to the directory where your files are saved</li>
  <li>Type <b>python app.py</b></li>
  <li>Copy the url and paste it in your web browser</li>
</ul>

Attaching some screenshots for your reference
![Capture](https://user-images.githubusercontent.com/56712218/180594872-59164bf7-be24-4abd-8df3-dfc23f67676b.PNG)
![88_pred](https:/![Cannot_pred](https://user-images.githubusercontent.com/56712218/180594881-2bdeaba9-fa5d-47ac-8018-5d8c36a18f67.PNG)
/user-images.githubusercontent.com/56712218/180594878-0b1e5ad5-0ff3-45fa-b177-63998891ea5e.PNG)
**Since visualisation is quite large this is only a part of visualisation , you an view full visualsation inside static\images\Visualisation1.svg
![11](https://user-images.githubusercontent.com/56712218/180594898-a391b8ea-12e9-4a3f-83c4-3254e4055e2a.PNG)

Enter your information and View the result😎
Voila!!🤞🤞
