alter session set "_ORACLE_SCRIPT"=true;
--����� ���� "" ���ֱ�
create user ora_user identified by 1111;
--���� �ο�
grant connect, resource, dba to ora_user;

--���� ����
drop user title;

--���ѻ���
revoke connect, resource, dba from ORA_USER;





