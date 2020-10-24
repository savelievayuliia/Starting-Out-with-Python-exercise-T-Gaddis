q_shares_bought = 2000
b_price_per_share_usd = 40
buying_commission = 0.03
q_shares_sold = 2000
s_price_per_share_usd = 42.75
b_shares_total_price_usd = q_shares_bought * b_price_per_share_usd
b_shares_commission_usd = b_shares_total_price_usd * buying_commission
s_shares_total_price_usd = q_shares_sold * s_price_per_share_usd
s_shares_commission_usd = s_shares_total_price_usd * buying_commission
joe_profit = s_shares_total_price_usd - b_shares_total_price_usd - b_shares_commission_usd - s_shares_commission_usd
print("Куплено акций на сумму",format(b_shares_total_price_usd,".2f"),"дол США")
print("Продано акций на сумму",format(s_shares_total_price_usd,".2f"),"дол США")
print("Комиссия с покупки акций составила",format(b_shares_commission_usd,".2f"),"дол США")
print("Комиссия с продажи акций составила",format(s_shares_commission_usd,".2f"),"дол США")
print("Прибыль / убыток составили:",format(joe_profit,".2f"),"дол США")