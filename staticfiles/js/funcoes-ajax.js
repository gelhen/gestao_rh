function utilizouHoraExtra(id, utilizou){
    token = document.getElementsByName('csrfmiddlewaretoken')[0].value;

    function getBool(val) {
        return !!JSON.parse(String(val).toLowerCase());
    }

    $.ajax({
        type: 'POST',
        url: '/horas-extras/utilizou-hora-extra/'+ id +'/',
        data: {
            csrfmiddlewaretoken: token,
            utilizada: utilizou
        },
        success: function(result){
            input = $("#id_utilizada")
            $("#mensagem").text(result.mensagem);
            $("#horas_atualizadas").text(result.horas);
            document.getElementById("id_utilizada").checked = getBool(result.utilizada);
        }
    });
}