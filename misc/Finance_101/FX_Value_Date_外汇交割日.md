- ON: Over-Night隔夜，即当天起息，次日交割
- TN: Tom-Next，即次日（Tom就是Tomorrow）起息，第三日交割
  - In most currency trades, delivery is two days after the transaction date. Tom-next trades arise because most currency traders have no intention of taking delivery of the currency so require their positions to be 'rolled-over' on a daily basis.This simultaneous transaction is an FX swap, and depending on what currency the person holds, they will either be charged or earn a premium. Those traders and investors holding high yielding currencies will roll it over at a more favorable rate (minimal) because of the interest rate differential. This differential is known as the cost of carry. 
  
- SN: Spot-Next，即期起息（即期的天数随币种而不一样，多数为2天），即期的次日交割
  - It denotes the delivery of purchased currency on a day after the spot date.
  - Spot-next is otherwise known as "next business day."
  - 
- 1W: 即期起息，即期后的一周交割
- 1M: 即期起息，即期后的一月交割
- 1Y: : 即期起息，即期后的一年交割

#### T+1 即期交易

- USD/CAD
- USD/TRY, Turk, Lirasi
- USD/PHP, Pilipinas, Pisong
- USD/RUB, Russian, Ruble


#### Introduction 
<http://www.londonfx.co.uk/valdates.html>


Value dates are the dates on which FX trades settle, i.e. the date that the payments of each currency are made. The value dates for most FX trades are "spot", which generally means two business days from the trade date (T+2). The most notable exception to this rule is USD/CAD, which has a spot date one business day from the trade date (T+1). Spot dates for CAD crosses (e.g. GBP/CAD) normally take the spot date of the crossed currency pair and are therefore T+2. 

Forward trades 

It is possible to settle trades on dates other than the spot date, in which case the rate will be adjusted by forward points to compensate for the interest rate differential between the two currencies being traded. In addition to the spot date, there are many standard tenors (periods) on which it is possible to settle an FX trade. These include “1 month”, “tomorrow” (tom) and “6 months”. The post-spot tenors are calculated from the spot date rather than from the trade date. It is also possible to settle on any value date between any standard tenor. This is known as a “broken date”. 

Value date roll-over 

For all currency pairs except NZD/USD, global market convention is that value dates roll forward at 5pm New York time. Value dates for NZD/USD roll forward at 7am Auckland time. This means that the local time of the value date roll-over varies throughout the year, depending on daylight savings time conventions, as follows: 

With effect from	Daylight Savings Time	Time of value date roll-over
London	New York	Auckland	GMT
non-NZD	GMT NZD	London non-NZD	London NZD	NY
NZD	Auckland non-NZD
2nd Sunday in March	GMT	EDT	NZDT	21:00	18:00	21:00	18:00	14:00	10:00
Last Sunday in March	BST	EDT	NZDT	21:00	18:00	22:00	19:00	14:00	10:00
1st Sunday in April	BST	EDT	NZST	21:00	19:00	22:00	20:00	15:00	09:00
Last Sunday in September	BST	EDT	NZDT	21:00	18:00	22:00	19:00	14:00	10:00
Last Sunday in October	GMT	EDT	NZDT	21:00	18:00	21:00	18:00	14:00	10:00
1st Sunday in November	GMT	EST	NZDT	22:00	18:00	22:00	18:00	13:00	11:00


Currency holidays 

For most T+2 currency pairs, if T+1 is a USD holiday, then this does not normally affect the spot date, but if a non-USD currency in the currency pair has a holiday on T+1, then it will make the spot date become T+3. If USD or either currency of a pair have a holiday on T+2, then the spot date will be T+3. This means, for example, that crosses such as EUR/GBP can never have a spot date on 4th July (although such a date could be quoted as an outright). 

USD/TRY spot date 

USD/TRY is traded interbank as T+0 and T+1, and both are supported by Reuters Dealing 3000 Spot Matching (D2). The conventional spot date is generally now T+1, even in the Turkish interbank market. Although T+0 is no longer used as an interbank spot date, it is still possible until 12:00 Istanbul time. 

USD/RUB spot date 

USD/RUB is traded interbank as T+0, T+1 and T+2. Reuters Dealing 3000 Spot Matching (D2) supports T+0 and T+1 for USD/RUB. The most popular of the three value dates is T+1, which could therefore be considered as the spot date. 

Latin American currencies 

USD holidays normally affect the spot date only if T+2 is a USD holiday. If T+1 is a USD holiday, this does not normally prevent T+2 from being the spot date. Certain Latin American currencies (ARS, CLP and MXN) are an exception to this. If T+1 is a USD holiday, then the spot date for the affected currencies will be T+3. For example, if the trade date is a Monday and a USD holiday falls on the Tuesday, then the spot date for EUR/USD will be the Wednesday, but the spot date for USD/MXN will be the Thursday. 

Arab currencies 

Whereas most countries' currencies cannot settle on a Saturday and Sunday, most Arab currencies cannot settle on a Friday and Saturday. Market convention in the interbank market for Arab currencies is that the spot date for Wednesday's trades is taken to be Monday. For AED, BHD, EGP, KWD, OMR and QAR, the spot date for Thursday's trades is also taken to be Monday, because this still leaves two working days for each currency in the pair (i.e. Friday and Monday for the USD, and Sunday and Monday for the Arab currency). This means that Tuesday is never a spot date in these currencies and can only be priced as a broken date. The exceptions to this rule are SAR and JOD, where the spot date for Thursday's trades is taken to be Tuesday, effectively making a three-day weekend (Friday, Saturday, Sunday) for value date purposes. Some banks, particularly Arab banks when trading with their customers, use split settlement for USD/Arab currency pairs, with USD settling on the Friday or Monday, and the Arab currency settling on the Sunday. In such cases of split settlement, the USD payment is always to the bank's advantage, whereby the bank receives USD from its customer on the Friday but pays USD to its customer on the Monday. 

Trade date 

The trade date/time is a timestamp to record when a trade was executed. It is customary to store the trade date/time in GMT/UTC in a database, and for display purposes either to suffix it with "GMT" or "UTC", or otherwise to translate it to a user's local time zone. It is normal that the value date may sometimes not appear as expected in relation to the trade date. For example, to a customer in New York at 22:30 GMT, the spot date for EUR/USD appears as T+3; likewise to a customer in New Zealand at 20:30 GMT, the spot date for EUR/USD appears as T+1. Being a timestamp, the trade date does not change at the time of the value date roll-over.

Some systems include an additional trade date field to indicate the effective trade date for value date calculation purposes, i.e. in order to maintain a constant relationship, e.g. T+2, between trade date and value date. This additional field should not incorporate a time, only a date, and is not normally displayed to price takers. 

Sources of holiday data 

There are many vendors of holiday data for calculating value dates. On almost every FX trader's desk in banks around the world, paper holiday calendars supplied by Copp Clark can be seen. Their data is also available in electronic format at GoodBusinessDay.com and given that the electronic version reflects the paper version that is authoritatively used by interbank traders, it is one of the most reliable electronic sources to use in FX trading systems for value date calculations. 
