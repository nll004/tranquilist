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
    $('#form-container').toggleClass('hidden');
})

// ==========================================================
//                  user_home.html
// ==========================================================
