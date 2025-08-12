function add_to_basket(product_id){
    let count = $('#count_product').val()
    $.get('/order/add_order/', {
        'product_id':product_id,
        'count':count

    }).then(
        res =>{
            if(res.status ==='success'){
                alert('به سبد خرید اضافه شد')
            }else if (res.status ==='not_login'){
                alert('ابتدا وارد شوید')
            }else if(res.status ==='over_count'){
                alert('تعداد محصولاتی که وارد کرده اید موجود نیست')
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