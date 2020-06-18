var works = '夜明日休ネ出'
var worksColor = {
  '夜': {'bg':'darkorchid',   'border':'darkorchid'},
  '明': {'bg':'mediumorchid', 'border':'mediumorchid'},
  '日': {'bg':'olivedrab',    'border':'olivedrab'},
  '休': {'bg':'darkgray',     'border':'darkgray'},
  'ネ': {'bg':'crimson',      'border':'crimson'},
  '出': {'bg':'black',        'border':'black'},
}
//var domain = JSON.parse(document.getElementById('domain').textContent);

var rotateWorkSched = function() {}
var addWorkSched = function(work_sched) {
  for ( ws of work_sched ) {
    var bg_color     = worksColor[ws['sched']].bg
    var border_color = worksColor[ws['sched']].border
    calendar.addEvent({
      'title':           ws['sched'],
      'start':           ws['date'],
      'backgroundColor': bg_color,
      'borderColor':     border_color,
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
  element.style.backgroundColor = worksColor[workSched].bg;
  element.style.borderColor     = worksColor[workSched].border;
}
