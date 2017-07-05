// http://stackoverflow.com/questions/1575141/make-div-100-height-of-browser-window

// MAKE THE PLOTS RESPONSIVE
(function() {
  var d3 = Plotly.d3;
  var WIDTH_IN_PERCENT_OF_PARENT = 20,
      HEIGHT_IN_PERCENT_OF_PARENT = 20;

  var gd3 = d3.selectAll(".plotly-graph-div")
     .style({
        width: WIDTH_IN_PERCENT_OF_PARENT + '%',
        height: HEIGHT_IN_PERCENT_OF_PARENT + '%'
      });

  var nodes_to_resize = gd3[0]; //not sure why but the goods are within a nested array
  console.log("node to resze", nodes_to_resize);
  window.onresize = function() {
    for (var i = 0; i < nodes_to_resize.length; i++) {
      console.log("resizing : ", node_to_resize[i]);
      Plotly.Plots.resize(nodes_to_resize[i]);
    }
  };

})();