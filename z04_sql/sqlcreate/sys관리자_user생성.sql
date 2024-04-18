alter session set "_ORACLE_SCRIPT"=true;
--사용자 생성 "" 없애기
create user ora_user identified by 1111;
--권한 부여
grant connect, resource, dba to ora_user;

--계정 삭제
drop user title;

--권한삭제
revoke connect, resource, dba from ORA_USER;





