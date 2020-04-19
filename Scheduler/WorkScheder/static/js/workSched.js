var works = '夜明日休'
var worksColor = {
  '夜': 'lightseagreen',
  '明': 'lightseagreen',
  '日': 'royalblue',
  '休': 'darkgray'
}
var domain = JSON.parse(document.getElementById('domain').textContent);

var rotateWorkSched = function() {}
var addWorkSched = function(work_sched) {
  for ( ws of work_sched ) {
    var color = worksColor[ws['sched']]
    calendar.addEvent({
      'title':           ws['sched'],
      'start':           ws['date'],
      'backgroundColor': color,
      'borderColor':     color,
    });
  }
};

var getWorkSched = function(year, month) {
  var uri = '/api/worksched/' + year +'/'+ month

  fetch(uri).then(function(response) {
    return response.json();
  }).then(function(json) {
    addWorkSched(json)
  });
}

var upd_workSched = function(element, workSched) {
  element.text                  = workSched
  element.style.backgroundColor = worksColor[workSched];
  element.style.borderColor     = worksColor[workSched];
}
