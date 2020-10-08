#LOS
=========
LORD OF SQL INJECTION 풀이
---------
### #orc#

if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("orc"); <br>
이 문장을 잘 보면 쿼리의 결과로 나온 pw와 GET받은 pw가 같아야만 orc가 풀린다.<br>
즉, admin의 비밀번호를 알아내야 풀 수 있는 문제이다.<br><br>

이런 유형을 Blind injection이라고 부른다고 한다.(구글링)<br><br>

우선 admin에 대한 비밀번호의 길이를 먼저 파악한다.<br>
lenght함수를 이용해 pw의 비밀번호의 길이를 알아준다.<br><br>

?pw=' or id= 'admin' and length(pw)={}%23
