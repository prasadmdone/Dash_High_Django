// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';


function getRandomColor() {
    var letters = '0123456789ABCDEF'.split('');
    var color = '#';
    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}
function getRandomColorEachEmployee(count) {
    var data =[];
    for (var i = 0; i < count; i++) {
        data.push(getRandomColor());
    }
    return data;
}

var endpoint = '/api/genderdata'; 
  
    $.ajax({ 
      method: "GET", 
      url: endpoint, 
      success: function(data) { 
        drawPieChart(data,"GenderAgePieChart"); 
      }, 
      error: function(error_data) { 
        console.log(error_data); 
      } 
    }) 

// Pie Chart Example

function drawPieChart(data,id)
{
var ctx = document.getElementById(id);
var chartlabels = data.labels
var chartdata = data.chartdata
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: chartlabels,
    datasets: [{
      data: chartdata,
      backgroundColor: getRandomColorEachEmployee(chartdata.length),
      hoverBackgroundColor: getRandomColorEachEmployee(chartdata.length),
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});
}