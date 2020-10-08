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

?pw='or id='admin' and substr(pw,{ },1)=char({ })%23<br><br>

길이가 8일 때 참이 되는 것을 확인했다.<br>
(master 브랜치로 가면 python을 이용해 substr코드가 있을 것이다.)<br>
python을 이용해 돌려주면 pw는 095a9852 것이 나온다!!<br><br>

?pw=095A9852

### #orc#
