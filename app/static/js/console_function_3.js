function processSearchResult(result) {
	if (result['successful']) {
		// var temperatureList = result['data']['temperatureList'];
		// console.log(temperatureList[23]['time']);
		// var t_labels = new Array(24);
		// var t_data = new Array(24);
		// for (var i = 0; i < 24; i++) {
		// 	t_labels[i] = temperatureList[i]['time'];
		// 	t_data[i] = temperatureList[i]['temperature'];
		// }
		// console.log(t_labels[1]);
		// console.log(t_data[1]);

		var lineChartData = {
			labels : ['100','100','100','100','100','100','100','100','100','100','100','100','100'],
			datasets : [
				{
					label: "temperature dataset",
					fillColor : "rgba(220,220,220,0.2)",
					strokeColor : "rgba(220,220,220,1)",
					pointColor : "rgba(220,220,220,1)",
					pointStrokeColor : "#fff",
					pointHighlightFill : "#fff",
					pointHighlightStroke : "rgba(220,220,220,1)",
					data : ['100','456','100','70','100','123','100','56','100','798','100','23','100']
				}
			]
		}

		var ctx = document.getElementById("canvas").getContext("2d");
		window.temperatureChart = new Chart(ctx).Line(lineChartData, {
			responsive: true
		});
	}
	switch(result['error'])
	{
		case 0:
			alert("查询时间不能为空");
			break;
		case 1:
			alert("查询时间错误");
			break;
		default:
			break;
	}
}

function doSearch(start_time,end_time) {
	var postData = {
		'start_time': start_time,
		'end_time': end_time
	}
	console.log('hhhhhh')
	$.ajax({
		type: "POST",
		url: "/control/temperature_chart",
		data: postData,
		dataType: "JSON",
		success: function(result){
			processSearchResult(result);
		}
	});
}

$('.tp_search').click(function() {
	var startTime = $('.start_date_time').val();
	var endTime = $('.end_date_time').val();
	var start_time = Date.parse(startTime);
	var end_time = Date.parse(endTime);
	doSearch(start_time,end_time);
})