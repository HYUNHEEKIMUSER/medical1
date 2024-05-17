$(function(){
    
    
    //1. ajax stu_score.json 10개 데이터 출력
    $.ajax({
        url:"json/stu_score.json",
        data:"",
        type:"get",
        dataType:"json",
        success:function(data){
            let htmlData = ' ';
            for(let i=0;i<10;i++){
                htmlData+='<tr id='+data[i].no+'>'
                htmlData+='<td><input type="checkbox" name="stu" class="stuCh" value='+data[i].no+'></td>'
                htmlData+='<td>'+data[i].no+'</td>'
                htmlData+='<td>'+data[i].name+'</td>'
                htmlData+='<td>'+data[i].kor+'</td>'
                htmlData+='<td>'+data[i].eng+'</td>'
                htmlData+='<td>'+data[i].math+'</td>'
                htmlData+='<td>'+data[i].total+'</td>'
                htmlData+='<td>'+data[i].avg+'</td>'
                htmlData+='<td>'+data[i].rank+'</td>'
                htmlData+='<td><button class="delBtn">삭제</button></td>'
                htmlData+='</tr>'

            }
            $("#body").html(htmlData);
        },
        error:function(){
            alert("실패");
        }
    });
//2. 학생 입력 ->학생추가 프로그램 구성
    $("#writeBtn").click(function(){
        alert("test")
        $(".p_all").css("display","block");
    })
    $("#cancelBtn").click(function(){
        $(".p_all").css("display","none");
    })

    $("#confirmBtn").click(function(){
        
        
        let i_no=Math.max.apply(null,no)+1
        no.push(i_no);
        let i_name = $("#name").val();
        let i_kor = Number($("#kor").val());
        let i_eng = Number($("#eng").val());
        let i_math = Number($("#math").val());
        let i_total = Number(i_kor+i_eng+i_math);
        let i_avg = Number((i_total/3).toFixed(2)); //소수점 2자리까지
        let i_rank = 0

        htmlData+='<tr id='+i_no+'>'
        htmlData+='<td><input type="checkbox" name="stu" class="stuCh" value='+i_no+'></td>'
        htmlData+='<td>'+i_no+'</td>'
        htmlData+='<td>'+i_name+'</td>'
        htmlData+='<td>'+i_kor+'</td>'
        htmlData+='<td>'+i_eng+'</td>'
        htmlData+='<td>'+i_math+'</td>'
        htmlData+='<td>'+i_total+'</td>'
        htmlData+='<td>'+i_avg+'</td>'
        htmlData+='<td>'+i_rank+'</td>'
        htmlData+='<td><button class="delBtn">삭제</button></td>'
        htmlData+='</tr>'

        $("#body").append(htmlData);
        $("#name").val("");
        $("#kor").val("");
        $("#eng").val("");
        $("#math").val("");
        $(".p_all").css("display","none");
    
    });

//3. 학생 수정 ->학생성적수정 구성


//4. 학생 삭제 ->선택된 학생이 삭제되게 구성
    $("#deleteBtn").click(function(){
        if($(".stuChk:checked").length<1)
            alert("삭제데이터 클릭해주세요")
            return false;
            
        if(confirm("정말 삭제하시겠습니까?")){
          return false;  
        }
        else{$(".stuChk").each(function(){
            if($(this).is(":checked")==true){
                $("#"+$(this).parent().parent().attr("id")).remove();
            }
        })}
        
    })

    
});//맨 마지막