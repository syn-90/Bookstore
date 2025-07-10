//
//
// function send_comment(article_id){
//     let text = $('#text_content')
//     alert(text.val())
//     console.log(article_id)
//     // )console.log('hi'
//     // $.get('/articels/send_comment/', {
//     //     'article_id' : article_id,
//     //     'text' : text
//     // }).then(
//     //     result =>{
//     //         console.log(result.status)
//     //     }
//     // )
//
// }


function send_comment(article_id) {
    // ابتدا بررسی کنیم المان وجود دارد
    // let text = $('#text_content');
    //
    // if (text.length === 0) {
    //     console.error('المانی با آی دی text_content یافت نشد!');
    //     return;
    // }
    //
    // if (!text.val()) {
    //     alert('لطفا متن نظر را وارد کنید!');
    //     return;
    // }
    return alert('آیدی مقاله: ' + article_id);
    // console.log('آیدی مقاله:', article_id);
    // console.log('متن نظر:', text.val());

    // اینجا میتوانید درخواست AJAX برای ارسال نظر اضافه کنید
}

