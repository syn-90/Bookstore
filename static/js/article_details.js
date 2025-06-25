

function send_comment(article_id){
    let text = $('#text_content')
    alert(text.val())
    // $.get('/articels/send_comment/', {
    //     'article_id' : article_id,
    //     'text' : text
    // }).then(
    //     result =>{
    //         console.log(result.status)
    //     }
    // )

}
