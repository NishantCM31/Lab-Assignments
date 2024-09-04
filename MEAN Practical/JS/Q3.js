function showBookTopics(bookId) {
    const topicsDiv = document.getElementById(`book-topics-${bookId}`);
    if (topicsDiv.style.display === 'none') {
        topicsDiv.style.display = 'block';
    } else {
        topicsDiv.style.display = 'none';
    }
}

function submitOrder() {
    const name = document.getElementById('customer-name').value;
    const address = document.getElementById('customer-address').value;
    const paymentDetails = document.getElementById('payment-details').value;
    const copies = document.getElementById('number-of-copies').value;

    if (name && address && paymentDetails && copies) {
        document.getElementById('order-status').innerText = 'Order Confirmed';
    } else {
        document.getElementById('order-status').innerText = 'Order Pending';
    }

    document.getElementById('order-response').style.display = 'block';
}
