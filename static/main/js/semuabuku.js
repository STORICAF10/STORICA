async function refreshProducts() { 
    function addProduct() {
        fetch("{% url 'main:cari_buku' %}", {
            method: 'POST',
            body: new FormData(document.querySelector('#form'))
        }).then(refreshProducts)

        document.getElementById("form").reset()
        return false
    }

    document.getElementById("button_cari").onclick = addProduct      
}

refreshProducts()
