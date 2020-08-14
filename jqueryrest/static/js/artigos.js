$.ajax({
    url: 'http://127.0.0.1:8000/artigos/artigo/',
    dataType: 'json',
    success: autores => {
        var item = ``
        $.each(autores, function(){
            item += `<li class="list-group-item">${this.titulo}</li>
                    <ul class="list-grid">
                        <li class="list-group-item">${this.data_publicacao}</li>
                        <li class="list-group-item">${this.autor.nome}</li>
                    </ul><br>`
        });
        $('#autores').append(item)
    }
})