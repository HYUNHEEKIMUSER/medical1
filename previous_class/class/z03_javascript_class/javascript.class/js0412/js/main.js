$(function(){

//최초실행-----------------------------------------------------------------------------------------------------------------
    let no = [1,2,3,4,5,6,7,8,9,10];
    let name = ['홍길동','유관순','이순신','김구','강감찬','김유신','홍길순','홍길자','최현묵','이규원'];
    let kor = [100,62,90,64,76,51,89,77,55,73,53];
    let eng = [100,70,62,73,54,55,60,67,77,51,100];
    let math = [100,81,79,50,83,72,79,82,86,50,94];
    let total = [300,213,231,187,213,178,228,226,218,174,247];
    let avg = [100,71,77,62.3,71,59.3,76,75.3,72.7,58,82.3];
//----------------------------------------------------------------------------------------------------------------------------       
    //tbody 부분 10개 행 생성
    let htmlData = ' ';
    for(let i=0; i<no.length;i++){
        htmlData += "<tr id='"+no[i]+"'>";
        htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+no[i]+"'></td>";
        htmlData += "<td>"+no[i]+"</td>";
        htmlData += "<td>"+name[i]+"</td>";
        htmlData += "<td>"+kor[i]+"</td>";
        htmlData += "<td>"+eng[i]+"</td>";
        htmlData += "<td>"+math[i]+"</td>";
        htmlData += "<td>"+total[i]+"</td>";
        htmlData += "<td>"+avg[i]+"</td>";
        htmlData += "<td>0</td>";
        htmlData += "<td><button class='delBtn'>삭제</button></td>";
        htmlData += "</tr>";

    }//for문

    //html 소스를 tbody에 추가(10개목록)
    $("#body").html(htmlData);
//----------------------------------------------------------------------------------------------------------------------------     
   //학생입력버튼 누를 때
    $("#writeBtn").click(function(){
        $('.p_all').css("display","block");
    });

    //학생입력버튼 취소버튼 누를 때
    $("#cancelBtn").click(function(){
        $(".p_all").css("display","none");
    })


//----------------------------------------------------------------------------------------------------------------------------     
    //학생입력확인 버튼 (새로운 성적 추가)
    $("#confirmBtn").click(function(){
        // 글자: text()-innerText, input-val()-value(), html()-innerHtml
        console.log("이름: " +$("#name").val())
        //console.log($("#kor").val())
        //console.log($("#eng").val())
        //console.log($("#math").val())
        //console.log(Math.max.apply(null,no)+1); //배열에서 최대값 구하기
        //no.push(Math.max.apply(null,no)+1); // 배열 추가 push
        
        //공백 확인
        if($('#name').val().length<2){
            alert("이름을 입력해야 등록이 가능합니다.")
            $('#name').focus()//커서 깜빡거림.
            return false;

        }
        
//----------------------------------------------------------------------------------------------------------------------------       
        let i_no = Math.max.apply(null,no)+1

        no.push(i_no);

        let i_name = $("#name").val();
        let i_kor = Number($("#kor").val()); //string이어서 넘버 붙임
        let i_eng = Number($("#eng").val());
        let i_math = Number($("#math").val());
        let i_total = Number(i_kor+i_eng+i_math);
        let i_avg = Number((i_total/3).toFixed(2)); //소수점 2자리까지 반올림.
        let i_rank = 0;


        let htmlData = ' ';
        htmlData += "<tr id='"+i_no+"'>";
        htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+i_no+"'></td>";
        htmlData += "<td>"+i_no+"</td>";
        htmlData += "<td>"+i_name+"</td>";
        htmlData += "<td>"+i_kor+"</td>";
        htmlData += "<td>"+i_eng+"</td>";
        htmlData += "<td>"+i_math+"</td>";
        htmlData += "<td>"+i_total+"</td>";
        htmlData += "<td>"+i_avg+"</td>";
        htmlData += "<td>0</td>";
        htmlData += "<td><button class='delBtn'>삭제</button></td>";
        htmlData += "</tr>";


        //html 소스를 tbody에 추가(10개목록)
        // $("#body").html(htmlData); //기존 html에 덮어쓰기
        // $("#body").prepend(htmlData) //기존 html(테이블) 위쪽에 추가
        $("#body").append(htmlData) //기존htaml(테이블) 아래쪽에 추가
        //input 초기화 val 안에 글자 넣으면 나타남
        $("#name").val("");
        $("#kor").val("");
        $("#eng").val("");
        $("#math").val("");
        $(".p_all").css("display","none"); // display 사라지게 하는 것
        

    }); //학생입력버튼


//----------------------------------------------------------------------------------------------------------------------------       

    //전체 선택하는 법
    $("#allChk").click(function(){
        //체크가 되어있는 것이 맞는 지 확인 한번하기
        if($(this).is(":checked")==true){
            console.log("체크되었습니다.");
            $(".stuChk").each(function(){
                $(this).prop("checked",true);
            });//전체 삭제


        }
        //모든 체크 해제
        else{
            console.log("체크해제 되었습니다.");
            $(".stuChk").each(function(){
                $(this).prop("checked",false);
        });

    };//전체삭제

});

    //table에 있는 삭제버튼 클릭
    $(".delBtn").click(function(){
        console.log("현재 선택된 class id: "+$(this).parent().parent().attr("id"));
        if(confirm("정말 삭제하시겠습니까?")){
            $("#"+$(this).parent().parent().attr("id")).remove()
        }
    });//table삭제

    //table에 새로운 정보가 추가된 후에 삭제할 때
    $(document).on("click",".delBtn",function(){
        console.log("현재 선택된 class id: "+$(this).parent().parent().attr("id"));
        if(confirm("정말 삭제하시겠습니까?")){
            $("#"+$(this).parent().parent().attr("id")).remove()
        }
    });//새로운 정보가 추가된 table삭제




    //하단 삭제버튼 클릭
    $("#deleteBtn").click(function(){
        console.log("체크박스 갯수: "+$(".stuChk").length);
        console.log("체크박스에서 체크된 갯수: "+$(".stuChk:checked").length);
        console.log("체크박스에서 체크된 갯수: "+$("input:checkbox[name='stu']:checked").length);
        
        //체크되어 있는 것이 없는 경우 에러를 띄워줌 (한번 물어보고)
        if($(".stuChk:checked").length<1){
            alert("삭제할 데이터를 체크해주셔야 합니다.");
            return false;

        }//체크if

        //현재 체크박스가 체크가 되어 있는 지 확인 (두번 물어보고)
        if(!confirm("정말 삭제하시겠습니까?")){
            return false; //no 버튼 클릭 시 다시 돌아감. yes는 건너뜀
        }//삭제if

        //모든 체크박스를 가져오기 (마지막으로 실행)
        $(".stuChk").each(function(){
            if($(this).is(":checked")==true){
                console.log("현재 선택된 class 값: "+$(this).val());
                console.log("현재 선택된 id 값: "+$(this).parent().parent().attr("id"));
                $("#"+$(this).parent().parent().attr("id")).remove()
            }
        }); //each
    });

  
});