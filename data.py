<!DOCTYPE html>

<html>
<html lang="en"></html>  
    <head>

        <title>
          Latitude 
        </title>
        <!-- CDN -->
        <!-- Boostrap Stylesheet -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

        <!-- Personal css -->
        <link rel="stylesheet" href="/Users/ulissesmiranda/Documents/GitHub/Web-Design-Challenge/Resources/assets/css/style.css" media="screen">

    </head>

    <body>

        <!-- navbar -->
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="#">Latitude </a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNavDropdown">
              <ul class="navbar-nav ml-auto">
                <li class="nav-item active">
                  <a class="nav-link" href="index.html">Home <span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="comparison.html">Comparisons</a>
                </li>
                
                <li class="nav-item">
                    <a class="nav-link" href="data.html">Data</a>
                </li>
                <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" left: 15px>
                    Plots
                  </a>
                  <div class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarDropdownMenuLink">
                    <a class="dropdown-item" href="Max_temp.html">Max Temperature</a>
                    <a class="dropdown-item" href="Humidity.html">Humidity</a>
                    <a class="dropdown-item" href="cloudiness.html">Cloudiness</a>
                    <a class="dropdown-item" href="wind_speed.html">Wind Speed</a>
                  </div>
                </li>
              </ul>
            </div>
          </nav>



<div class="container">
  <div class="row">
    <div class="col-md-7">
      <div class="col-md-12">
        <h2>Summary: Latitude vs. X </h2>
        <hr>
        <div class="thumbnail">
           <img class="img-thumbnail float-left" src="Resources/assets/images/Fig1.png " width="50%" alt="temperature">
        
           <p>The purpose of this project was to analyze how weather changes as you get closer to the equator. To accomplish this analysis, we first pulled data from the OpenWeatherMap API to assemble a dataset on over 500 cities.  
            </p> 
                    
           <p>After assembling the dataset, we used Matplotlib to plot various aspects of the weather vs latitude. Factors we looked at included: temperature, cloudiness, wind speed, and humidity. This site provides the source data and visualizations created as part of the analysis, as well as explanations and descriptions of any trends and correlations witnessed.</p>
        </div>
    </div>  
  </div> 
    
    <div class="col-md-5">
      <div class="col-md-12">
        <h3>Visualizations </h3>
        <hr>
          <div >
            <a href="Max_Temp.html"><img src="Resources/assets/images/Fig1.png "width="49%" alt="temperature"></a>
            <a href="Humidity.html"><img src="Resources/assets/images/Fig2.png "width="49%" alt="temperature"></a>
        <!-- </div> -->

        <!-- <div class="row"> -->
            <a href="Cloudiness.html"><img src="Resources/assets/images/Fig3.png "width="49%" alt="temperature"></a>
            <a href="wind_speed.html"><img src="Resources/assets/images/Fig4.png "width="49%" alt="temperature"></a>
          </div>

      </div>   
         
    </div>
  </div>
  
</div>
        <!-- bootstrap CDN -->
        <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" 
        integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" 
        integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" 
        integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>






    </body>
</html>