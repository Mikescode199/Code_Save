//Create vue instance   
var app = new Vue({
    el: '#app',
    //Create delimeiter for django template
    delimiters: ['{$', '$}'],

    data: {
        usuario: "",
        lenguajeProgramacion: 0,
        codigo_foto: '',
        codigo_texto: '',
        informacion_codigo: '',
        categoria : 0,
        privacidad: false

    }
    //Create methods to Post and Get data Api
    //Post Method with Fetch
    ,methods: {        
        postSnippet: function() {
            var url = 'http://localhost:8000/Url_code_saved/Snippet/?format=api';
            var data = {
                'usuario': this.usuario,
                'lenguajeProgramacion': this.lenguajeProgramacion,
                'codigo_foto': this.codigo_foto,
                'codigo_texto': this.codigo_texto,
                'informacion_codigo': this.informacion_codigo,
                'categoria': this.categoria,
                'privacidad': this.privacidad
            };

            const request = new Request(
                {headers: {'X-CSRFToken': csrftoken}}
            );

            fetch(url, request, {
                method: 'POST',
                mode: 'same-origin' ,
                cache: 'no-cache',
                credentials: 'same-origin',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            }).then(function(response) {
                return response.json();
            }).then(function(response) {
                console.log(response);
                if (response.status == '200') {
                    alert('Snippet creado');
                    window.location.href = 'http://localhost:8000/Url_code_saved/Snippet/';
                }
            });
        }

    }
});


//End of Vue
