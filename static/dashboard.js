/* globals Chart:false, feather:false */

(function () {
  'use strict'

  feather.replace()

  // Graphs
  var ctx = document.getElementById('myChart')
  // eslint-disable-next-line no-unused-vars
  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: [
        '11.00',
        '12.00',
        '13.00',
        '14.00',
        '15.00',
        '16.000',
        '17.00',
        '18.00',
        '19.00',
        '20.00',
      ],
      datasets: [{
        data: [
          100,
          500,
          250,
          0,
          0,
          750,
          0,
          1004,
          750,
          750,
          
        ],
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#007bff',
        borderWidth: 4,
        pointBackgroundColor: '#007bff'
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: false
          }
        }]
      },
      legend: {
        display: false
      }
    }
  })
})()
