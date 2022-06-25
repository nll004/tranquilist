// =======================================================
//                 app_home.html
// =========================================================

// popup sign in/login form
$('#reg-login').click(function(e){
    e.preventDefault();
    $('#form-container').toggleClass('hidden');
})
// close sign in/login form
$('.close-form').click(function(e){
    console.log(e.target)
    $('#form-container').toggleClass('hidden');
})

// ==========================================================
//                  user_home.html
// ==========================================================

// Create a new tasklist by rightclicking on h3
$("h3").contextmenu(function(e) {
    e.preventDefault();
    // select tasklist id
    $taskId = $(this).attr('id')
    // display form to add task
    $('#background-cover').removeClass('hidden')
    $('#main-tasks-forms').removeClass('hidden')
    // add id to hidden form field
    $('#tasklist_timeline').val($taskId)
});

// Remove add task popup listener from calendar h3
$('#cal-h3').off()

// Colapse tasks inside of the h3 headers
$('h3').click(function(e){
    $(this).siblings().toggleClass('hidden')
})

// strikethrough tasks when complete and collapse subtasks
$('.item').click(function(e){

    $(this).toggleClass('complete-True')
    $(this).nextUntil('li').toggleClass('hidden')
})

// right click task and edit or make new subtask for it
$('.item').contextmenu(function(e) {
    e.preventDefault();
    $('#background-cover').removeClass('hidden')
    $('#edit-main-tasks').removeClass('hidden')
    // get tasklist id from .item to use for forms
    $taskId = $(this).attr('id')
    // prefill edit form options with text and tasklist id
    $('#edit_tasklist_id').val($taskId)
    $current_val = $(this).contents().get(0).nodeValue.trim()
    $('#edit_tasklist_name').val($current_val)
    $('#tasklist_id').val($taskId)
});

// close pop up forms when clicking off of the form
$("#background-cover").click(function(e){
    $("#background-cover").addClass('hidden')
    $('#main-tasks-forms').addClass('hidden')
    $('#edit-main-tasks').addClass('hidden')
})

// strikethrough subtasks when complete
$('.subtask').click(function(){
    $(this).toggleClass('complete-True')
})
