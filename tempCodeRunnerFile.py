
# ## html _ category list Area
# cateLiArea = soup.find('div',{"class":'cateLiArea'})

# ## get link (level2,level3)
# AllLink = cateLiArea.findAll('a')

# ## get depth2
# LstDepth2 = AllLink.findAll('a',{'class':'lnk_cate2d'})
# print(LstDepth2)