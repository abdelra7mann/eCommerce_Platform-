var updateBtns = document.getElementsByClassName('update-cart');
for (var i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function() {
		var productId = this.dataset.product;
		var action = this.dataset.action;
		console.log('product: ' + productId + ', action: ' + action);
        console.log('USER:',user)
        if(user === 'anonymousUser'){
            console.log('Not Logged in ')
        }
        else{ userOrderUpdate(productId,action)  }
	});
}

function userOrderUpdate(productId, action) {
    console.log('User is logged in, sending data');
    var url = '/update_data/';
    fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({ 'productId': productId, 'action': action })
        })
        .then(response => response.json())
        .then(data => {
            console.log('data:', data);
            location.reload(); // Reload the page to reflect the updated cart
        })
        .catch(error => {
            console.error('Error:', error);
        });
}


function updateCart() {
    // Send an AJAX request to get the latest cart data
    fetch('/get_cart_data/')
      .then(response => response.json())
      .then(data => {
        // Update the HTML content of the shopping cart
        document.querySelector('#cart-item-count').innerHTML = data.item_count;
        document.querySelector('#cart-total').innerHTML = data.total;
      });
  }
  
  function updateData(request) {
    // ... existing code ...
  
    // Call the updateCart function to update the UI
    updateCart();
  
    return JsonResponse('item was added', safe=False);
  }
  