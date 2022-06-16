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
// $(document).on('click', function(e) {
//     const $container = $('#form-container')
//     if (!$(e.target).closest($container).length) {
//         $container.hide()
//     }
// })

$('.h3-btn').click(function(e){
    $('.new-tasklist').toggleClass('hidden')
    // get timeline_id from parent
    $tl_id = $(this).parent().attr('id')
    $('#timeline').val($tl_id)
})

$('.add-subtask-btn').click(function(e){
    $('.subtask-form').toggleClass('hidden')
    // get tasklist_id from parent
    $tl_id = $(this).parent().attr('id')
    $('#list_id').val($tl_id)
})





$('.primary-task').click(function(e){
    $('edit-task-form').toggleClass('hidden')
})

$('.del-task-btn').click(function(e){
    $('list-add-form').toggleClass('hidden')
})
