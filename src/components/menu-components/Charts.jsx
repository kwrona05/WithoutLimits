const Chart = ({ data }) => {
  const chartData = {
    labels: data.map((d) => d.timestamp),
    datasets: [
      {
        label: "Heart rate",
        data: data.map((d) => d.heart_rate),
        borderColor: "rgba(75,192,192,1)",
        fill: false,
      },
    ],
  };

  return <Line data={chartData} />;
};
export default Chart;
