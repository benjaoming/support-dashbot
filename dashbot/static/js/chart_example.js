(async function() {
  const data = [
    { date: "2024-07-01", count: 650 },
    { date: "2024-06-01", count: 804 },
    { date: "2024-05-01", count: 803 },
    { date: "2024-04-01", count: 900 },
    { date: "2024-03-01", count: 830 },
    { date: "2024-02-01", count: 920 },
    { date: "2024-01-01", count: 900 },
  ];

  new Chart(
    document.getElementById('support-backlog-timeseries'),
    {
      type: 'line',
      data: {
        labels: data.map(row => row.date),
        datasets: [
          {
            label: 'Support backlog GitHub',
            data: data.map(row => row.count)
          }
        ]
      },
      options: {
          scales: {
              x: {
                type: 'time',
                time: {
                    unit: 'month'
                }
              }
          }
      }
    }
  );
})();
