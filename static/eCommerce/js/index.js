// $(".like-btn").submit(function (e) { 
//     e.preventDefault();
//     var serialized_data = $(this).serialize();

//     $.ajax({
//         type: "post",
//         url: "{% url 'like-product' %}",
//         data: serialized_data,

//         success: function (response) {
//             alertify.set('notifier','position', 'top-right');
//             alertify.success(response.message);
//         },

//         error: function (response) {
//             alertify.set('notifier','position', 'top-right');
//             alertify.error(response.responseJSON.message);
//         },
//     });
// });