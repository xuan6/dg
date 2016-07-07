/* This file should contain all the JS for Loop dashboard */
window.onload = initialize;

function initialize() {
    // initialize any library here
    $('select').material_select();
    $(".button-collapse1").sideNav()
    $(".button-collapse").sideNav()

    selected_tab="aggregator";

    set_filterlistener();
    get_filter_data();
}

//datepicker
$('.datepicker').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 15, // Creates a dropdown of 15 years to control year
    format: 'yyyy-mm-dd',
    onSet: function(element) {
        if (element.select) {
            this.close();
        }
    }
});


function change_tab(tab){
    selected_tab = tab;
    change_graph();
}

function change_graph(parameter){
    $("#aggregator_visits").show()
    if (selected_tab=="aggregator"){
        update_graphs_aggregator_wise(parameter);
    }
    if (selected_tab == "mandi"){
        update_graphs_mandi_wise(parameter);
    }
    if (selected_tab == "crop"){
        $("#aggregator_visits").hide()
        update_graphs_crop_wise(parameter);
    }
}


function set_filterlistener() {

    $('#get_data').click(function() {
        get_data();
    });


    $('#aggregator_all').on('change', function(e) {
        if (this.checked) {
            $('#aggregators').children().each(function() {
                var aggregators_all = $(this).children()[1].firstChild;
                aggregators_all.checked = true;
            });
        } else {
            $('#aggregators').children().each(function() {
                var aggregators_all = $(this).children()[1].firstChild;
                aggregators_all.checked = false;
            });
        }
    });

    $('#crop_all').on('change', function(e) {
        if (this.checked) {
            $('#crops').children().each(function() {
                var crops_all = $(this).children()[1].firstChild;
                crops_all.checked = true;
            });
        } else {
            $('#crops').children().each(function() {
                var crops_all = $(this).children()[1].firstChild;
                crops_all.checked = false;
            });
        }
    });

    $('#mandi_all').on('change', function(e) {
        if (this.checked) {
            $('#mandis').children().each(function() {
                var mandis_all = $(this).children()[1].firstChild;
                mandis_all.checked = true;
            });
        } else {
            $('#mandis').children().each(function() {
                var mandis_all = $(this).children()[1].firstChild;
                mandis_all.checked = false;
            });
        }
    });
    $('#gaddidar_all').on('change', function(e) {
        if (this.checked) {
            $('#gaddidars').children().each(function() {
                var gaddidar_all = $(this).children()[1].firstChild;
                gaddidar_all.checked = true;
            });
        } else {
            $('#gaddidars').children().each(function() {
                var gaddidar_all = $(this).children()[1].firstChild;
                gaddidar_all.checked = false;
            });
        }
    });

}

function get_filter_data() {
    $.get("/loop/filter_data/", {})
        .done(function(data) {
            data_json = JSON.parse(data);
            aggregators_for_filter = data_json.aggregators;
            mandis_for_filter = data_json.mandis;
            gaddidars_for_filter = data_json.gaddidars;
            fill_aggregator_filter(aggregators_for_filter);
            fill_crop_filter(data_json.crops);
            fill_mandi_filter(mandis_for_filter);
            fill_gaddidar_filter(gaddidars_for_filter);
            get_data();
        });
}


function get_data() {
    var start_date = $('#from_date').val();
    var end_date = $('#to_date').val();
    // Get rest of the filters
    aggregator_ids = [];
    aggregator_names = [];
    crop_ids = [];
    crop_names = [];
    mandi_ids = [];
    mandi_names = [];
    gaddidar_ids = [];
    gaddidar_names = [];

    $('#aggregators').children().each(function() {
        var aggregator_div = $(this).children()[1].firstChild;
        if (aggregator_div.checked) {
            aggregator_ids.push(aggregator_div.getAttribute('data'));
            aggregator_names.push(aggregator_div.getAttribute('value'));
        }
    });

    $('#crops').children().each(function() {
        var crop_div = $(this).children()[1].firstChild;
        if (crop_div.checked) {
            crop_ids.push(crop_div.getAttribute('data'));
            crop_names.push(crop_div.getAttribute('value'));
        }
    });

    $('#mandis').children().each(function() {
        var mandi_div = $(this).children()[1].firstChild;
        if (mandi_div.checked) {
            mandi_ids.push(mandi_div.getAttribute('data'));
            mandi_names.push(mandi_div.getAttribute('value'));
        }
    });
    $('#gaddidars').children().each(function() {
        var gaddidar_div = $(this).children()[1].firstChild;
        if (gaddidar_div.checked) {
            gaddidar_ids.push(gaddidar_div.getAttribute('data'));
            gaddidar_names.push(gaddidar_div.getAttribute('value'));
        }
    });

    if (Date.parse(start_date) > Date.parse(end_date)) {
        //$('.modal-trigger').leanModal();
        $('#modal1').openModal();
    } else {
        get_aggregator_wise_data(start_date, end_date, aggregator_ids, crop_ids, mandi_ids, gaddidar_ids);
        get_data_for_line_graphs(start_date, end_date, aggregator_ids, crop_ids, mandi_ids, gaddidar_ids);
    }
}

function fill_aggregator_filter(data_json) {
    $.each(data_json, function(index, data) {
        create_filter($('#aggregators'), data.user__id, data.name, true);
    });
}

function fill_crop_filter(data_json) {
    $.each(data_json, function(index, data) {
        create_filter($('#crops'), data.id, data.crop_name, true);
    });
}

function fill_mandi_filter(data_json) {
    $.each(data_json, function(index, data) {
        create_filter($('#mandis'), data.id, data.mandi_name, true);
    });
}

function fill_gaddidar_filter(data_json) {
    $.each(data_json, function(index, data) {
        create_filter($('#gaddidars'), data.id, data.gaddidar_name, true);
    });
}

function create_filter(tbody_obj, id, name, checked) {
    var row = $('<tr>');
    var td_name = $('<td>').html(name);
    row.append(td_name);
    var checkbox_html = '<input type="checkbox" class="black" data=' + id + ' id="' + name + id + '" checked="checked" value = ' + name + ' /><label for="' + name + id + '"></label>';
    var td_checkbox = $('<td>').html(checkbox_html);
    row.append(td_checkbox);
    tbody_obj.append(row);
}


function get_aggregator_wise_data(start_date, end_date, aggregator_ids, crop_ids, mandi_ids, gaddidar_ids) {
    $.get("/loop/new_aggregator_wise_data/", {
            'start_date': start_date,
            'end_date': end_date,
            'aggregator_ids[]': aggregator_ids,
            'crop_ids[]': crop_ids,
            'mandi_ids[]': mandi_ids,
            'gaddidar_ids[]': gaddidar_ids
        })
        .done(function(data) {
            aggregator_graphs_json_data = JSON.parse(data);
            update_graphs_aggregator_wise();
        });
}


function update_graphs_aggregator_wise(chart) {
    if (chart==null){
        $('#1stgraph').text("Aggregator Wise")
        aggregator_graph($('#aggregator_mandi'), aggregator_ids, aggregator_names, 'user_created__id', mandi_ids, mandi_names, 'mandi__id',aggregator_graphs_json_data.aggregator_mandi, "quantity__sum");
        $('#2ndgraph').text("Cost per kg")
        repeat_farmers($('#mandi_cost'), aggregator_ids, aggregator_names, 'user_created__id',mandi_ids, mandi_names, 'mandi__id', aggregator_graphs_json_data.total_repeat_farmers);
    }else{
       
        if (chart == "volume") {
           aggregator_graph($('#aggregator_mandi'), aggregator_ids, aggregator_names, 'user_created__id', mandi_ids, mandi_names, 'mandi__id',aggregator_graphs_json_data.aggregator_mandi, "quantity__sum");

        } else if (chart=="amount") {
            aggregator_graph($('#aggregator_mandi'), aggregator_ids, aggregator_names, 'user_created__id', mandi_ids, mandi_names, 'mandi__id',aggregator_graphs_json_data.aggregator_mandi, "amount__sum");

        } else if (chart == "visits"){
            aggregator_graph($('#aggregator_mandi'), aggregator_ids, aggregator_names, 'user_created__id', mandi_ids, mandi_names, 'mandi__id',aggregator_graphs_json_data.aggregator_mandi, "mandi__id__count");
        }

        if (chart=="cost_recovered"){
            $('#2ndgraph').text("Total Cost")
            transport_cost_graph($('#mandi_cost'), aggregator_ids, aggregator_names, 'user_created__id', mandi_ids, mandi_names, 'mandi__id', aggregator_graphs_json_data.transportation_cost_mandi);
        }else if(chart == "cpk_spk"){
            $('#2ndgraph').text("Cost per kg")
            cpk_spk_graph($('#mandi_cost'), aggregator_ids, aggregator_names, 'user_created__id',mandi_ids, mandi_names, 'mandi__id', aggregator_graphs_json_data);
        }      
    }
}

function update_graphs_mandi_wise(chart){
    if (chart==null){
        $('#1stgraph').text("Mandi Wise")
        aggregator_graph($('#aggregator_mandi'), mandi_ids, mandi_names, 'mandi__id', aggregator_ids, aggregator_names, 'user_created__id', aggregator_graphs_json_data.aggregator_mandi, "quantity__sum");
        $('#2ndgraph').text("Cost per kg")
        cpk_spk_graph($('#mandi_cost'), mandi_ids, mandi_names, 'mandi__id', aggregator_ids, aggregator_names, 'user_created__id', aggregator_graphs_json_data);
    }else{
       
        if (chart == "volume") {
           aggregator_graph($('#aggregator_mandi'), mandi_ids, mandi_names, 'mandi__id', aggregator_ids, aggregator_names, 'user_created__id',aggregator_graphs_json_data.aggregator_mandi, "quantity__sum");

        } else if (chart=="amount") {
            aggregator_graph($('#aggregator_mandi'), mandi_ids, mandi_names, 'mandi__id', aggregator_ids, aggregator_names, 'user_created__id',aggregator_graphs_json_data.aggregator_mandi, "amount__sum");

        } else if (chart == "visits"){
            aggregator_graph($('#aggregator_mandi'), mandi_ids, mandi_names, 'mandi__id', aggregator_ids, aggregator_names, 'user_created__id',aggregator_graphs_json_data.aggregator_mandi, "mandi__id__count");
        }

        if (chart=="cost_recovered"){
            $('#2ndgraph').text("Total Cost")
            transport_cost_graph($('#mandi_cost'),  mandi_ids, mandi_names, 'mandi__id', aggregator_ids, aggregator_names, 'user_created__id', aggregator_graphs_json_data.transportation_cost_mandi);
        }else if(chart == "cpk_spk"){
            $('#2ndgraph').text("Cost per kg")
            cpk_spk_graph($('#mandi_cost'), mandi_ids, mandi_names, 'mandi__id', aggregator_ids, aggregator_names, 'user_created__id', aggregator_graphs_json_data);
        }      
    }
}
function update_graphs_crop_wise(chart){
    
    if (chart==null){
        $('#1stgraph').text("crop Wise")
        aggregator_graph($('#aggregator_mandi'), crop_ids, crop_names, 'crop__id', mandi_ids, mandi_names, 'mandi__id', aggregator_graphs_json_data.mandi_crop, "quantity__sum");
        $('#2ndgraph').text("Max Min Rates")
        max_min_graph($('#mandi_cost'), aggregator_graphs_json_data.crop_prices)
    }else{
       
        if (chart == "volume") {
           aggregator_graph($('#aggregator_mandi'), crop_ids, crop_names, 'crop__id', mandi_ids, mandi_names, 'mandi__id', aggregator_graphs_json_data.mandi_crop, "quantity__sum");

        } else if (chart=="amount") {
            aggregator_graph($('#aggregator_mandi'), crop_ids, crop_names, 'crop__id', mandi_ids, mandi_names, 'mandi__id',aggregator_graphs_json_data.mandi_crop, "amount__sum");
        }
    }
}


function aggregator_graph(container, axis, axis_names, axis_parameter, values, values_names, values_parameter, json_data, parameter) {
    var series = [];
    var drilldown ={};
    drilldown['series']= [];

    // These three values are to show at top
    var total_volume = 0;
    var total_amount = 0;
    var total_visits = 0;


    var temp = {};
        temp['name'] = "Total";
        temp['type'] = "bar";
        temp['colorByPoint'] = true;
        temp['data'] = [];

        for (var i=0;i<axis.length;i++){
            temp['data'].push({'name':axis_names[i],'y':0,'drilldown':axis_names[i]});
            drilldown['series'].push({'name':axis_names[i],'id':axis_names[i],'data':[], 'type':'bar'});
            for (var j = 0; j < values_names.length; j++) {
                drilldown['series'][i]['data'].push([values_names[j],0]);
            }
        }
        temp['showInLegend'] = false;
        series.push(temp);
    
    for (var i = 0; i < json_data.length; i++) {

        var agg_index = values.indexOf(json_data[i][values_parameter].toString());
        var index = axis.indexOf(json_data[i][axis_parameter].toString());

        drilldown['series'][index]['data'][agg_index][1]+=json_data[i][parameter]

        series[0]['data'][index]['y'] += json_data[i][parameter];

        total_volume+=json_data[i]["quantity__sum"];
        total_amount+=json_data[i]["amount__sum"];
        total_visits+=json_data[i]["mandi__id__count"];
    }

    series[0]['data'].sort(function(a, b) {
        return b['y'] - a['y'];
    });

    for (var i=0; i<axis.length; i++){
        drilldown['series'][i]['data'].sort(function(a,b){
            return b[1] - a[1]
        });
    }

    $("#aggregator_volume").text("Volume: "+parseFloat(total_volume).toFixed(2))
    $("#aggregator_amount").text("amount: "+parseFloat(total_amount).toFixed(2))
    $("#aggregator_visits").text("visits: "+total_visits)
    plot_drilldown(container, series,drilldown);

}


function transport_cost_graph(container, axis, axis_names, axis_parameter, values, values_names, values_parameter, json_data) {
    var series = [];
    var x_axis = new Array(axis.length);
    console.log(axis.length);
    for (var i = 0; i < axis.length; i++) {
        x_axis[i] = axis_names[i];
    }
    var temp_cost = {};
        temp_cost['name'] = "Total Cost";
        temp_cost['type'] = "bar";
        temp_cost['showInLegend'] = false;
        temp_cost['data'] = [];
        for (var i = 0; i < axis.length; i++) {
           temp_cost['data'].push({'name':axis_names[i], 'y':0});
        }
        temp_cost['pointPadding'] = 0.3;
        temp_cost['pointPlacement'] = 0;
        series.push(temp_cost);
    var temp_cost_recovered = {};
        temp_cost_recovered['name'] = "Cost Recovered";
        temp_cost_recovered['type'] = "bar";
        temp_cost_recovered['showInLegend'] = false;
        temp_cost_recovered['data'] = [];
        for (var i = 0; i < axis.length; i++) {
           temp_cost_recovered['data'].push({'name':axis_names[i], 'y':0});
        }
        temp_cost_recovered['pointPadding'] = 0.4;
        temp_cost_recovered['pointPlacement'] = 0;
        series.push(temp_cost_recovered);
    var json_data_length = json_data.length;
    for (var i = 0; i < json_data_length; i++) {
        var index = axis.indexOf(json_data[i][axis_parameter].toString());

        series[0]['data'][index]['y'] += json_data[i]['transportation_cost__sum'] 
        series[1]['data'][index]['y'] += json_data[i]['farmer_share__sum'];
    }
    plot_stacked_chart(container, series);
}

function cpk_spk_graph(container, axis, axis_names, axis_parameter, values, values_names, values_parameter, json_data) {
    var vol_stats = json_data.aggregator_mandi;
    var cost_stats = json_data.transportation_cost_mandi;
    var series = [];

    values_vol = new Array(axis.length).fill(0.0);
    values_cost_cpk = new Array(axis.length).fill(0.0);
    values_cost_spk = new Array(axis.length).fill(0.0);

    var temp = {};
    var temp_spk = {};
    temp['name'] = 'cpk';
    temp['type'] = "bar";
    temp['showInLegend'] = false;
    temp['data'] =[];
    temp['pointPadding'] = 0.3;
    temp['pointPlacement'] = 0;


    temp_spk['name'] = 'spk';
    temp_spk['type'] = "bar";
    temp_spk['showInLegend'] = false;
    temp_spk['data'] = [];
    temp_spk['pointPadding'] = 0.4;
    temp_spk['pointPlacement'] = 0;

    for (var i = 0; i < axis.length; i++) {
       temp['data'].push({'name':axis_names[i], 'y':0});
       temp_spk['data'].push({'name':axis_names[i], 'y':0});
    }
    series.push(temp);
    series.push(temp_spk);

    for (var i = 0; i < vol_stats.length; i++) {
        var index = axis.indexOf(vol_stats[i][axis_parameter].toString());
        values_vol[index] += vol_stats[i]['quantity__sum'];
    }
    for (var i = 0; i < cost_stats.length; i++) {
        var index = axis.indexOf(cost_stats[i][axis_parameter].toString());
        values_cost_cpk[index] += cost_stats[i]['transportation_cost__sum'] ;
        values_cost_spk[index] += cost_stats[i]['farmer_share__sum'];
    }


    for (var j = 0; j < axis_names.length; j++) {
        series[0]['data'][j]['y'] = values_vol[j] > 0 ? values_cost_cpk[j] / values_vol[j] : 0.0;
        series[1]['data'][j]['y'] = values_vol[j] > 0 ? values_cost_spk[j] / values_vol[j] : 0.0;
    }

    plot_stacked_chart(container, series);
}

function repeat_farmers(container, axis, axis_names, axis_parameter, values, values_names, values_parameter, json_data){
    var series = [];

    var temp_total = {};
        temp_total['name'] = "Total Cost";
        temp_total['type'] = "bar";
        temp_total['showInLegend'] = false;
        temp_total['data'] = [];
        for (var i = 0; i < axis.length; i++) {
           temp_total['data'].push({'name':axis_names[i], 'y':0});
        }
        temp_total['pointPadding'] = 0.3;
        temp_total['pointPlacement'] = 0;
        series.push(temp_total);
    var temp_repeat = {};
        temp_repeat['name'] = "Cost Recovered";
        temp_repeat['type'] = "bar";
        temp_repeat['showInLegend'] = false;
        temp_repeat['data'] = [];
        for (var i = 0; i < axis.length; i++) {
           temp_repeat['data'].push({'name':axis_names[i], 'y':0});
        }
        temp_repeat['pointPadding'] = 0.4;
        temp_repeat['pointPlacement'] = 0;
        series.push(temp_repeat);
    var json_data_length = json_data.length;
    for (var i = 0; i < json_data_length; i++) {
        var index = axis.indexOf(json_data[i][axis_parameter].toString());
        var count = json_data[i]['farmer_count']
        series[0]['data'][index]['y'] += 1;
        if (count>1){
            series[1]['data'][index]['y'] +=1;
        }
    }
    plot_stacked_chart(container, series);
}

function max_min_graph(container, json_data){

    json_data.sort(function(a,b){
        return (b['price__max']-b['price__min'])-(a['price__max']-a["price__min"])
    })

    var x_axis = []
    var series = [{"name":"Max_Min", "data":[]}]

    for (var i=0; i<json_data.length; i++){
        x_axis.push(json_data[i]['crop__crop_name'])
        series[0]['data'].push([json_data[i]['price__min'], json_data[i]['price__max']])
    }

    plot_max_min(container,x_axis, series)
}

function get_data_for_line_graphs(start_date, end_date, aggregator_ids, crop_ids, mandi_ids, gaddidar_ids){
    $.get("/loop/data_for_line_graph/", {
            'start_date': start_date,
            'end_date': end_date,
            'aggregator_ids[]': aggregator_ids,
            'crop_ids[]': crop_ids,
            'mandi_ids[]': mandi_ids,
            'gaddidar_ids[]': gaddidar_ids
        })
        .done(function(data) {
            line_json_data = JSON.parse(data);
            show_line_graphs();
        });
}

function show_line_graphs(){
    var json_data = line_json_data.aggregator_data;
    var dates = line_json_data['dates']
    var all_dates = [];

    var first_date = new Date(dates[0]);
    while (first_date <= new Date(dates[dates.length-1])){
        all_dates.push(first_date.getTime());
        first_date.setDate(first_date.getDate()+1)
    }
    console.log(all_dates);
    var series = [{'name':"Volume", 'type':'spline', 'data':[]}]
    for (var i = 0; i < all_dates.length; i++) {
           series[0]['data'].push([all_dates[i],0]);
    }

    for (var i=0; i<json_data.length; i++){
        var index = all_dates.indexOf(new Date(json_data[i]['date']).getTime());
        console.log(index);
        series[0]['data'][index][1] += json_data[i]['quantity__sum']; 
    }

    var $container = $('#container2')
                .css('position', 'relative');

            $('<div id="detail-container">')
                .appendTo($container);

            $('<div id="master-container">')
                .css({
                    position: 'absolute',
                    top: 300,
                    height: 100,
                    width: '100%'
                })
                    .appendTo($container);

    createMaster(series)
}


function plot_stacked_chart(container_obj, dict){

    if (dict[0]['data'].length>=6){
        var max=5;
    }else{
        var max = dict[0]['data'].length-1;
    } 
    container_obj.highcharts({
        chart: {
            height: 300,
        },

        title: {
            text: null
        },
        xAxis: {
            type: 'category',
            labels: {
                rotation: 0
            },
            min: 0,
            max: max
        },
        scrollbar: {
            enabled: true,
        },
        yAxis: [{
            min: 0,
            title: {
                text: null
            }
        }],
       legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle',
            borderWidth: 0
        },
        tooltip: {
            headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
            pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}</b> <br/>'
        },
    
        plotOptions: {
            bar: {
                grouping: false,
                showCheckbox: true,
                dataLabels: {
                    enabled: true,
                    format: ' ',
                    color: (Highcharts.theme && Highcharts.theme.dataLabelsColor) || 'white',
                    style: {
                        textShadow: '0 0 3px black'
                    }
                }
            }
        },
        series: dict
        
    });
}
function plot_drilldown(container_obj, dict, drilldown) {

    container_obj.highcharts({
        chart: {
            type: 'bar',
            height: 300,
            zoomType: 'x'
        },
        title: {
            text: null
        },
        subtitle: {
            text: null
        },
        xAxis: {
            type: 'category',
        },
        yAxis: {
            title: {
                text: null
            },
            

        },
        legend: {
            enabled: false
        },
        plotOptions: {
            series: {
                borderWidth: 0,
                dataLabels: {
                    enabled: true,
                    format: '{point.y:.0f}'
                }
            }
        },

        tooltip: {
            headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
            pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.0f}</b> <br/>'
        },
        series: dict,
        drilldown: drilldown
    });
}


function plot_max_min (container,x_axis, dict) {

    if (dict[0]['data'].length>=6){
        var max=5;
    }else{
        var max = dict[0]['data'].length-1;
    } 

    container.highcharts({

        chart: {
            type: 'columnrange',
            inverted: true,
            height: 300
        },

        title: {
            text: null
        },

        

        xAxis: {
            categories: x_axis,
            min: 0,
            max: max
        },

        yAxis: {
            title: {
                text: null
            },
            min: 0
        },

        scrollbar: {
            enabled: true,
        }, 

        plotOptions: {
            columnrange: {
                dataLabels: {
                    enabled: true,
                    formatter: function () {
                        return this.y;
                    }
                }
            }
        },

        legend: {
            enabled: false
        },

        series: dict

    });

};


function createDetail(masterChart, dict) {

                // prepare the detail chart
                var myDict=[]
                var detailData = [],
                    detailStart = dict[0]['data'][0][0];

                $.each(masterChart.series, function () {
                    var temp ={};
                    temp['name'] = this.name;
                    temp['type'] = "spline"
                    temp['data'] = new Array();
                    temp['pointStart']= detailStart;
                    temp['pointInterval']= 24 * 3600 * 1000;
                    temp['showInLegend'] = true;
                    $.each(this.data, function () {
                        if (this.x >= detailStart) {
                            temp['data'].push(this.y);
                        }

                    });
                    myDict.push(temp)});

                // create a detail chart referenced by a global variable
                detailChart = $('#detail-container').highcharts({
                    chart: {
                        marginBottom: 120,
                        reflow: false,
                        marginLeft: 50,
                        marginRight: 20,
                        style: {
                            position: 'absolute'
                        }
                    },
                    credits: {
                        enabled: false
                    },
                    
                    xAxis: {
                        type: 'datetime'
                    },
                    yAxis: {
                        title: {
                            text: null
                        },
                        maxZoom: 0.1
                    },
                    tooltip: {
                        // formatter: function () {
                        //     var point = this.points[0];
                        //     return '<b>' + point.series.name + '</b><br/>' + Highcharts.dateFormat('%A %B %e %Y', this.x) + ':<br/>' +
                        //         'Volume= ' + Highcharts.numberFormat(point.y, 2);
                        // },
                        shared: true
                    },
                    legend: {
                        enabled: false
                    },
                    plotOptions: {
                        series: {
                            marker: {
                                enabled: false,
                                states: {
                                    hover: {
                                        enabled: true,
                                        radius: 3
                                    }
                                }
                            }
                        }
                    },
                    legend: {
                        align: 'right',
                        x: 0,
                        verticalAlign: 'top',
                        y: 0,
                        floating: true,
                        backgroundColor: (Highcharts.theme && Highcharts.theme.background2) || 'white',
                        borderColor: '#CCC',
                        borderWidth: 1,
                        shadow: false
                    },
                    series: myDict,

                    exporting: {
                        enabled: false
                    }

                }).highcharts(); // return chart
            }

            // create the master chart
            function createMaster(dict) {
                $('#master-container').highcharts({
                    chart: {
                        reflow: false,
                        borderWidth: 0,
                        backgroundColor: null,
                        marginLeft: 50,
                        marginRight: 20,
                        zoomType: 'x',
                        events: {

                            // listen to the selection event on the master chart to update the
                            // extremes of the detail chart
                            selection: function (event) {
                                var extremesObject = event.xAxis[0],
                                    min = extremesObject.min,
                                    max = extremesObject.max,
                                    detailData = [],
                                    xAxis = this.xAxis[0],
                                    myDict = [];

                                $.each(this.series, function(){
                                    var temp ={};
                                    temp['name']= this.name;
                                    temp['data'] = new Array();
                                    temp['pointStart']= dict[0]['data'][0][0];
                                    temp['pointInterval']= 24 * 3600 * 1000;
                                    $.each(this.data, function(){
                                       if (this.x > min && this.x < max) {
                                            temp['data'].push([this.x, this.y]);
                                        } 
                                    });
                                    myDict.push(temp);
                                });
                                console.log(myDict);
                                // reverse engineer the last part of the data
                              
                                // move the plot bands to reflect the new detail span
                                xAxis.removePlotBand('mask-before');
                                xAxis.addPlotBand({
                                    id: 'mask-before',
                                    from: dict[0]['data'][0][0],    //data[0][0],
                                    to: min,
                                    color: 'rgba(0, 0, 0, 0.2)'
                                });

                                xAxis.removePlotBand('mask-after');
                                xAxis.addPlotBand({
                                    id: 'mask-after',
                                    from: max,
                                    to: dict[0]['data'][dict[0]['data'].length - 1][0],
                                    color: 'rgba(0, 0, 0, 0.2)'
                                });
                                var pos=0;
                                $.each(this.series, function(){
                                    detailChart.series[pos].setData(myDict[pos].data);
                                    pos++;
                                });
                                
                                
                                

                                return false;
                            }
                        }
                    },
                    title: {
                        text: null
                    },
                    xAxis: {
                        type: 'datetime',
                        showLastTickLabel: true,
                        maxZoom: 14 * 24 * 3600000, // fourteen days
                        plotBands: [{
                            id: 'mask-before',
                            from: dict[0]['data'][0][0],
                            to: dict[0]['data'][dict[0]['data'].length - 1][0],
                            color: 'rgba(0, 0, 0, 0.2)'
                        }],
                        title: {
                            text: null
                        }
                    },
                    yAxis: {
                        gridLineWidth: 0,
                        labels: {
                            enabled: false
                        },
                        title: {
                            text: null
                        },
                        min: 0.6,
                        showFirstLabel: false
                    },
                    tooltip: {
                        formatter: function () {
                            return false;
                        }
                    },
                    legend: {
                        enabled: false
                    },
                    credits: {
                        enabled: false
                    },
                    plotOptions: {
                        series: {
                            fillColor: {
                                linearGradient: [0, 0, 0, 70],
                                stops: [
                                    [0, Highcharts.getOptions().colors[0]],
                                    [1, 'rgba(255,255,255,0)']
                                ]
                            },
                            lineWidth: 1,
                            marker: {
                                enabled: false
                            },
                            shadow: false,
                            states: {
                                hover: {
                                    lineWidth: 1
                                }
                            },
                            enableMouseTracking: false
                        }
                    },

                    series: dict,

                    exporting: {
                        enabled: false
                    }

                }, function (masterChart) {
                    createDetail(masterChart, dict);
                })
                    .highcharts(); // return chart instance
            }