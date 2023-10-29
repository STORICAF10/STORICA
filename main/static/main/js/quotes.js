async function getProducts() {
    var link = document.getElementById("Urlpalsu").getAttribute("data-url")
    return fetch(link).then((res) => res.json())
}

async function refreshProducts() {
    document.getElementById("akandiajax").innerHTML=""
    const katabijak = await get
    function hapusQuotes() {
        var url = document.getElementById("Url").getAttribute("data-url")
        $.ajax({
            type: 'POST',
            url: `/delete_item/${itemId}/`,
            data: {
                'csrfmiddlewaretoken': '{{ csrf_token }}',
            }}).then(refreshProducts)
    }

    document.getElementById("tombol_hapus").onclick = hapusQuotes     
}

refreshProducts()
