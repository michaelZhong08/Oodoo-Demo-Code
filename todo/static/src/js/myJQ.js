$(document).ready(function(){
    //alert('this is a page!');
    $('#mybtn').on('click',function(){
        $('.some-div').html('1234');
        $.get('/todo/ajaxtest',function(res){
            var data=JSON.parse(res)[0];
            //console.log();
            $('.some-div').html('jsonData:<br>id:'+data.id+'<br>record_date:'+data.record_date+'<br>state:'+data.state);
        });
    })
})