function add_to_basket(product_id){
    let add_basket_content = $('#add_basket_content')
    $.get('/order/add_order/', {
        'product_id':product_id,
        // 'count':count

    },function (response){
        if (response.status ==='not_login'){
            alert('ابتدا وارد شوید')
        }else if(response.status ==='already_add'){
            alert('قبلا اضافه شده ')
        }else if(response.status ==='not_login'){
            alert('لطفا ابتدا وارد شوید')
        }else{
            alert('به سبد خرید اضافه شد')
            // add_basket_content.html(response)
        }



    }
    )
}


function count_product(detail_id,status){
    let basket_content = $('#basket_content')
    $.get('/order/change_count/', {
        'state' : status,
        'detail_id':detail_id
    },function (response){
        if (response.status ==='not_enough'){
             alert('تعداد محصولاتی که وارد کرده اید موجود نیست')
        }
        else {
            basket_content.html(response)
        }
    })
}


function remove_detail(detail_id){
    let basket_content = $('#basket_content')
    $.post('/order/remove_detail/', {
        'detail_id' : detail_id
    },
        function (response){
        alert('با موفقیت حذف شد ')
        basket_content.html(response)
        })

}

// function remove_detail(detail_id) {
//     $.post("/order/remove_detail/", {
//         'detail_id': detail_id
//     }, function (response) {
//         if (response.message === 'success') {
//             $("#detail-" + detail_id).remove();  // حذف از DOM
//         } else {
//             alert("آیتم پیدا نشد!");
//         }
//     });
// }

