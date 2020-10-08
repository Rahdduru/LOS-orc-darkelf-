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

### #wolfman#
if($result['id'] == 'admin') solve("wolfman");<br>
푸는 조건은 goblin과 같다. id의 값이 admin이면 된다.<br><br>

다만, <br>
if(preg_match('/ /i', $_GET[pw])) exit("No whitespace ~_~"); <br>
공백을 필터링 하기 때문에 or이나 and처럼 string형태로 치면 공백을 사용할 수 없어 그냥 문자열로 입력되어버린다.<br>
이는 &&나 ||를 이용해 우회가 가능하다. 또한 %23은 #이므로 이를 이용해 주석을 사용해주는 방법 또한 있다.<br>
주석을 이용해 이 문제를 풀어보면 <br><br>

?pw='||id='admin'%23<br>

### #darkelf#

if($result['id'] == 'admin') solve("darkelf"); <br>
이 문제 또한 goblin과 wolfman같이 id가 admin이면 해결된다.<br><br>

다만, 이번에는 논리연산자 or과 and가 필터링 되어버린다.<br>
이 또한 wolfman에서처럼 &&와 ||로 우회가 가능하다.<br><br>

?pw=' || id='admin'%23
