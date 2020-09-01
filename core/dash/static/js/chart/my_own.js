// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';



var endpoint = '/api'; 
  
    $.ajax({ 
      method: "GET", 
      url: endpoint, 
      success: function(data) { 
        drawBarGraph(data,"myAreaChart"); 
      }, 
      error: function(error_data) { 
        console.log(error_data); 
      } 
    }) 
  
// Area Chart Example
function drawBarGraph(data, id) { 
      var labels = data.labels; 
      var chartLabel = data.chartLabel; 
      var chartdata = data.chartdata; 
      var ctx = document.getElementById(id).getContext('2d'); 
      var myChart = new Chart(ctx, { 
        type: 'bar', 
        data: { 
          labels: labels, 
          datasets: [{ 
            label: chartLabel, 
            data: chartdata, 
            borderColor: [ 
              'rgba(255, 99, 132, 1)', 
              'rgba(54, 162, 235, 1)', 
              'rgba(255, 206, 86, 1)', 
              'rgba(75, 192, 192, 1)', 
              'rgba(153, 102, 255, 1)', 
              'rgba(255, 159, 64, 1)' 
            ], 
            borderWidth: 1 
          }] 
        }, 
        options: { 
          scales: { 
            yAxes: [{ 
              ticks: { 
                beginAtZero: true 
              } 
            }] 
          } 
        } 
      }); 
    } 