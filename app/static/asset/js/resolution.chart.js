$(document).ready(function (){
  const labels = ["Unfinished", "Almost", "Finished"];
  const data = {
    labels: labels,
    datasets: [{
      label: 'resolution finishing this year',
      backgroundColor: 'rgb(255, 99, 132)',
      borderColor: 'rgb(255, 99, 132)',
      data: [4, 1, 1],
    }]
  };
  const config_line = {
    type: 'line',
    data,
    options: {}
  };
  const config_bar = {
    type: 'bar',
    data,
    options: {}
  };
  var myLineChart = new Chart(
    document.getElementById("resolution-finishing-line-chart"),
    config_line
  );
  var myDoughnutChart = new Chart(
    document.getElementById("resolution-finishing-bar-chart"),
    config_bar
  );
});
