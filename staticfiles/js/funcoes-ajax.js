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

function process_response(funcionarios){
    func_select = document.getElementById('funcionarios');
    func_select.innerHTML = '';

    funcionarios.forEach(function(funcionario){
        var option = document.createElement("option");
        option.text = funcionario.fields.nome;
        func_select.add(option)
    });
}

function filtraFuncionarios(){
    depart_id = document.getElementById('departamentos').value;
    $.ajax({
        type: 'GET',
        url: '/filtra-funcionarios/',
        data: {
            outro_param: depart_id
        },
        success: function(result){
            process_response(result);
            $("#mensagem").text('Funcionarios carregados');
        }
    });
}