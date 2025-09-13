function add_to_favorite(product_id){
    // let count = $('#count_product').val()
    $.get('/dashboard/add_to_favorite/', {
        'product_id':product_id,

    }).then(
        res =>{
            if(res.status ==='success'){
                alert('به علاقه مندی ها افزوده شد')
            }else if(res.status ==='already_add'){
                alert('قبلا اضافه شده ')
            }else if(res.status ==='not_login'){
                alert('لطفا ابتدا وارد شوید')
            }

        }
    )
}


// function add_to_favorite(product_id){
//     $.get('/dashboard/add_to_favorite/', {
//         'product_id': product_id,
//     }).then(
//         res => {
//             const heartButton = $('#heart-' + product_id);
//             const heartIcon = heartButton.find('i');
//
//             if(res.status === 'success'){
//                 // تغییر ظاهر قلب به قرمز
//                 heartButton.addClass('favorite');
//                 heartIcon.removeClass('fa-heart-o').addClass('fa-heart');
//
//                 // نمایش پیام موقت به جای alert
//                 showTempMessage('به علاقه‌مندی‌ها افزوده شد', 'success');
//
//             } else if(res.status === 'already_add'){
//                 // تغییر ظاهر قلب به غیرفعال
//                 heartButton.removeClass('favorite');
//                 heartIcon.removeClass('fa-heart').addClass('fa-heart-o');
//
//                 showTempMessage('از علاقه‌مندی‌ها حذف شد', 'info');
//
//             } else if(res.status === 'not_login'){
//                 // اگر کاربر لاگین نبود، هدایت به صفحه لاگین
//                 window.location.href = '/login/';
//             }
//         }
//     ).fail(function() {
//         showTempMessage('خطا در برقراری ارتباط', 'error');
//     });
// }
//
// // تابع برای نمایش پیام موقت (اختیاری)
// function showTempMessage(message, type) {
//     const messageDiv = $('<div>')
//         .addClass('temp-message ' + type)
//         .text(message)
//         .css({
//             'position': 'fixed',
//             'top': '20px',
//             'right': '20px',
//             'padding': '10px 20px',
//             'border-radius': '5px',
//             'z-index': '9999',
//             'color': 'white',
//             'font-weight': 'bold'
//         });
//
//     if (type === 'success') {
//         messageDiv.css('background-color', 'green');
//     } else if (type === 'info') {
//         messageDiv.css('background-color', 'blue');
//     } else if (type === 'error') {
//         messageDiv.css('background-color', 'red');
//     }
//
//     $('body').append(messageDiv);
//
//     // حذف خودکار پیام بعد از 3 ثانیه
//     setTimeout(function() {
//         messageDiv.fadeOut(300, function() {
//             $(this).remove();
//         });
//     }, 3000);
// }