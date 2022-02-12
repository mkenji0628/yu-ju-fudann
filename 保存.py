from source_chord import Tabelog

tokyo_ramen_review = Tabelog(base_url="https://tabelog.com/tokyo/rstLst/ramen/", test_mode=False, p_ward='東京都内')
# CSV保存


tokyo_ramen_review.df.to_csv("../output/tokyo_ramen_review.csv")
