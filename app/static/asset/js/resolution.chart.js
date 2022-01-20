function build_line_chart(resolution)
{
  var labels = ["Unfinished", "Almost", "Finished"];
  var data = {
    labels: labels,
    datasets: [{
      label: 'resolution finishing this year',
      backgroundColor: 'rgb(255, 99, 132)',
      borderColor: 'rgb(255, 99, 132)',
      data: resolution
    }]
  };
  var config_line = {
    type: 'line',
    data,
    options: {
      scales: {
        y: {
          min: 0,
          ticks: {
            stepSize: 1
          }
        }
      }
    }
  };
  var myLineChart = new Chart(
    document.getElementById("resolution-finishing-line-chart"),
    config_line
  );

  return myLineChart;
}

function build_bar_chart(resolution)
{
  var labels = ["Unfinished", "Almost", "Finished"];
  var data = {
    labels: labels,
    datasets: [{
      label: 'resolution finishing this year',
      backgroundColor: 'rgb(255, 99, 132)',
      borderColor: 'rgb(255, 99, 132)',
      data: resolution
    }]
  };
  var config_bar = {
    type: 'bar',
    data,
    options: {
      scales: {
        y: {
          ticks: {
            stepSize: 1
          }
        }
      }
    }
  };
  var myBarChart = new Chart(
    document.getElementById("resolution-finishing-bar-chart"),
    config_bar
  );

  return myBarChart;
}

function create_bar()
{
  var endpoint = window.location.origin + "/api/resolution/";
  var request = new XMLHttpRequest();

  request.onreadystatechange = function(){
    if (this.readyState == 4){
      var response = JSON.parse(this.responseText);
      var almost = 0;
      var finished = 0;
      var unfinished = 0;
      response.data.forEach(function(data){
        if (data.percentage < 60){
          unfinished += 1;
        } else if (data.percentage < 100) {
          almost += 1;
        } else {
          finished += 1;
        }
      });
      build_line_chart([unfinished, almost, finished]);
      build_bar_chart([unfinished, almost, finished]);
    }
  }

  request.open("GET", endpoint, true);
  request.send();
}
