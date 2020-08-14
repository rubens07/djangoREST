$.ajax({
    url: 'http://127.0.0.1:8000/artigos/autor/',
    dataType: 'json',
    success: autores => {
        var item = ``
        $.each(autores, function(){
            item += `<li class="list-group-item">${this.nome}</li>
                    <ul class="list-grid">
                        <li class="list-group-item">${this.endereco}</li>
                        <li class="list-group-item">${this.site ? this.site : "Não informado"}</li>
                        <li class="list-group-item">${this.email}</li>
                    </ul><br>`
        });
        $('#autores').append(item)
    }
})