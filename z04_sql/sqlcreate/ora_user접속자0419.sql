select * from employees;
--달러를 원화로 환산
select employee_id,emp_name,salary from employees;
select employee_id,emp_name,salary,salary*1381.79 from employees;

-- 월급 *12 =연봉
select employee_id, emp_name, salary*12 from employees;
-- 연봉의 원화로 환산
select employee_id, emp_name,salary*12 ,(salary*12)*1381.79 from employees;

--커미션은 실제월급 = 월급 + 월급*커미션
--commission_pct
select * from employees;
--nvl(컴럼,0) 커미션이 0일 경우에 설정
select employee_id, emp_name, nvl(commission_pct,0),salary+(salary*nvl(commission_pct,0)) from employees;
select employ_id,emp_name,commission_pct,salary+(salary*commission_pct) from employees;

