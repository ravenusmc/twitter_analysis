//The code in this file will be for the maps.html file and will mainly contain a lot 
//of the D3.JS for creating the maps. 

function get_day() {

    var option_box = document.getElementById("option_box");
    var day = Number(option_box.options[option_box.selectedIndex].value);
    d3.select("svg").remove();
    createMap(day);
}

function createMap(day){

        d3.csv("/my/data/endpoint", function(data) {

        //Creating an array to refine my data, by the day, in the loop below. It will eventually become 
        //an array of objects. 
        data_sorted = [];
        
        //This loop will sort the data by the day that the user selects and build the map off
        //of that data. 
        for (var i = 1; i < data.length; i++){

            if (data[i].day == day){
                state = data[i].state;
                avg = data[i].avg;
                //This object will be placed into the array that was created above
                data_obj = {}
                data_obj.state = state;
                data_obj.avg = avg;
                data_sorted.push(data_obj);
            }  

        }

        console.log(data_sorted);


        var width = 800;
        var height = 800;
        var svg = d3.select("#us-map")
                    .append("svg")
                    .attr("width",width)
                    .attr("height",height);

        var projection = d3.geo.albersUsa().translate([width/2,height/2]);
        projection = projection.scale(1000)
        var path = d3.geo.path().projection(projection);

        //Setting up basic look of the map
        d3.json("/json", function(data) {
          svg.append("path")
            .datum(data)
            .attr('d',path)
            .attr('fill',"rgb(237,248,233)")
            .attr('stroke','black');
        });

        //Setting up the color for the map as well as the range. 
        var color = d3.scale.quantize()
                .range(["rgb(237,248,233)","rgb(186,228,179)","rgb(116,196,118)","rgb(49,163,84)","rgb(0,109,44)"]);

        //Set input domain for color scale
        color.domain([
            d3.min(data_sorted, function(d) { return d['avg']; }),
            d3.max(data_sorted, function(d) { return d['avg']; })
        ]);

        //I have to use a geoJSON file to match up the state name with its geographical location
        d3.json("/json", function(json) {
            //Merge the data and GeoJSON
            //Loop through once for each data value
            for (var i = 0; i < data_sorted.length; i++) {
                //Grab state name
                var dataState = data_sorted[i].state;
                //Grab data value, and convert from string to float
                var dataValue = parseFloat(data_sorted[i]['avg']);
                //Find the corresponding state inside the GeoJSON
                for (var j = 0; j < json.features.length; j++) {
                    var jsonState = json.features[j].properties.name;
                    if (dataState == jsonState) {
                        //Copy the hate crime value into the JSON
                        json.features[j].properties.value = dataValue;
                        //Stop looking through the JSON
                        break;
                    }
                }
            }

            //Bind data and create one path per GeoJSON feature
            svg.selectAll("path")
               .data(json.features)
               .enter()
               .append("path")
               .attr("d", path)
               .style("fill", function(d) {
                    //Get data value
                    var value = d.properties.value;
                    if (value) {
                        //If value exists…
                        return color(value);
                    } else {
                        //If value is undefined…
                        return "#ccc";
                    }
               })
               .append("title")
               .text(function(d){
                    return "State: " + d.properties.name + ',' + " Value: " + d.properties.value;
                });
        })
    });
}