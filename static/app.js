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

// Colapse tasks inside of the timeline
$('h3').click(function(e){
    $(this).siblings().toggleClass('hidden')
})

// Create a new tasklist by rightclicking on h3
$("h3").contextmenu(function(e) {
    e.preventDefault();
    // select tasklist id
    $taskId = $(this).attr('id')
    // display form to add task
    $('#main-tasks-forms').removeClass('hidden')
    // add id to hidden form field
    $('#tasklist_timeline').val($taskId)
});

$('#cancel-tasklist').click(function(e){
    $($('#main-tasks-forms').addClass('hidden'))
})

// ==========  Tasks  ==============
// strikethrough tasks when complete and collapse subtasks
$('.item').click(function(e){
    $(this).toggleClass('complete-True')
    $(this).nextUntil('li').toggleClass('hidden')
})

// right click tasklist and edit or make new subtask for it
$('.item').contextmenu(function(e) {
    e.preventDefault();
    $('#edit-main-tasks').removeClass('hidden')
    // get tasklist id for forms
    $taskId = $(this).attr('id')

    // prefill edit form options with text and tasklist id
    $('#edit_tasklist_id').val($taskId)
    $current_val = $(this).contents().get(0).nodeValue.trim()
    $('#edit_tasklist_name').val($current_val)
    $('#tasklist_id').val($taskId)
});

$('#close-tasklist-form').click(function(){
    $('#edit-main-tasks').addClass('hidden')
})

// strikethrough subtasks when complete
$('.subtask').click(function(){
    $(this).toggleClass('complete-True')
})

$('.add-subtask-btn').click(function(e){
    $('.subtask-form').toggleClass('hidden')
    // get tasklist_id from parent
    $tl_id = $(this).parent().attr('id')
    $('#list_id').val($tl_id)
})



$('#add-subtask-popup').click(function(e){

})
// select subtask id
$subtaskId = $(this).attr('id')
$('.subtask-form').toggleClass('hidden')
// add id to hidden form field
$('#list_id').val($subtaskId)








$('.primary-task').click(function(e){
    $('edit-task-form').toggleClass('hidden')
})

$('.del-task-btn').click(function(e){
    $('list-add-form').toggleClass('hidden')
})
