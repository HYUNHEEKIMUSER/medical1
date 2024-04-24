--20,000/10,000 문자형을 뺴기 연산을 해서 10,000 출력하세요
--number로 형변환
select to_char(to_number('20,000','99,999')-to_number('10,000','99,999'),'99,999') from dual;

select commission_pct from employees;
--실제월급 = 월급 + (월급*커미션) 실제월급으로 해서 출력하세요
select*from employees;
select salary, salary + (salary*nvl(commission_pct,0)) from employees;
--commission_pct null 값만 출력
select emp_name, commission_pct from employees where commission_pct is null;
--manager_id null이면 0입력
select nvl(manager_id,0) from employees order by manager_id desc;
--manager_id null이면 ceo입력
select nvl(to_char(manager_id),'ceo') from employees order by manager_id desc;
