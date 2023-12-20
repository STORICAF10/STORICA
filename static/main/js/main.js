async function getProducts() {
    var link = document.getElementById("Urlpalsu").getAttribute("data-url")
    return fetch(link).then((res) => res.json())
}

async function refreshProducts() {
    function addQuotes() {
        var url = document.getElementById("Url").getAttribute("data-url")
        fetch(url, {
            method: 'POST',
            body: new FormData(document.querySelector('#form'))
        }).then(window.location.reload())
        console.log("ditekan")

        document.getElementById("form").reset()
        return false
    }

    document.getElementById("button_add").onclick = addQuotes     
}

refreshProducts()
