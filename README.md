# googlemapreview 구글 맵 리뷰 크롤링

**-THIS IS ONLY FOR STUDY USAGE<br>
-연구용 코드입니다**

## 구글 맵 리뷰에 대하여 About Google Maps Review
구글 지도에서 방문한 장소에 대한 리뷰를 자발적으로 작성하게 합니다.<br>
리뷰는 누구에게나 공개됩니다.<br>
구글의 자동화된 스팸 탐지 방법을 사용하여 스팸일 가능성이 높은 리뷰 삭제됩니다.<br>
신고시스템으로 허위로 간주되거나 구글의 리뷰 정책을 준수하지 않는 것으로 간주 되는 리뷰는 삭제될 수 있습니다.<br>

## 리뷰 정확도 Review Accuracy
안드로이드 폰 같은 경우 구글의 위치 공유, 기록, 정확도 서비스가 수집되어 사용자의 이동 경로가 구글 지도에 저장됩니다.<br>
이 정보를 통해 구글은 사용자가 방문한 곳의 평가를 해달라는 알림을 보내 자발적 리뷰를 권합니다.<br>
IOS 폰 같은 경우는 사용자가 구글맵을 설치후 위치기록을 사용 설정하게 해야 가능합니다.<br>
물론 구글 회원이라면 누구나 리뷰를 등록할 수 있습니다. 하지만 구글 리뷰 정책에 위반될시 구글은 리뷰를 삭제할 권리를 보유합니다.<br>

## 결과물 Output
구글 맵 리뷰 228개를 통한 대저생태공원에 대한 평가 분석<br>
![output](https://github.com/hansnam1105/googlemapreview/blob/master/result/ex1.png)
![output2](https://github.com/hansnam1105/googlemapreview/blob/master/result/ex2.png)


## 참고 및 방법
[크롬 개발자 도구를 통해 모든 리뷰 크롤링](https://zzsza.github.io/development/2019/03/12/crawling-in-developer-tools-console/)

json 파일 만든후 파이썬 코드 실행하면 됩니다.

[파이썬 형태소 분석으로 워드클라우드 그리기](https://thinkwarelab.wordpress.com/2016/08/30/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%98%95%ED%83%9C%EC%86%8C-%EB%B6%84%EC%84%9D%EC%9C%BC%EB%A1%9C-%EC%9B%8C%EB%93%9C%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C-%EA%B7%B8%EB%A6%AC%EA%B8%B0/)

[파이썬을 이용한 빅데이터 분석, 워드 클라우드 사용](https://nearman.tistory.com/entry/4-%EC%9B%8C%EB%93%9C%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%B6%84%EC%84%9D-%EC%9B%8C%EB%93%9C-%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C-%EC%82%AC%EC%9A%A9?category=809080)

[형태소 분석 및 품사 태깅](https://konlpy-ko.readthedocs.io/ko/v0.4.3/morph/)
