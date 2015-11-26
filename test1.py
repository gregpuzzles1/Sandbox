from bs4 import BeautifulSoup

txt = '''<a id="body_BusinessSearchResultSummaryList_repBusinessList_lnkBusinessProfile_1" class="sr-item-link" href="http://www.mocality.co.ke/b/natros-pharmacy/natrosoh/innercore/medical-services/_/_/0cfe6a11-7bee-41f8-8d2e-6a472557201f?skw=pharmacys&amp;rcnt=10">Natros Pharmacy</a>
<a id="body_BusinessSearchResultSummaryList_repBusinessList_lnkBusinessProfile_2" class="sr-item-link
" href="http://www.mocality.co.ke/b/natros-pharmacy/natrosoh/innercore/medical-services/_/_/0cfe6a11-
7bee-41f8-8d2e-6a472557201f?skw=pharmacys&amp;rcnt=10">Natros Pharmacy</a>'''
match = 'body_BusinessSearchResultSummaryList_repBusinessList_lnkBusinessProfile'
match1 = u'sr-item-link'

soup = BeautifulSoup(txt, "html.parser")
for a in soup.findAll('a'):
        if a.has_attr('class') and a['class'] == match1:
        	print a['href'], a.contents

        print a['class']