
from pages import Topic, Insight, Page, Report


#	COVER PAGES

#	DEFINING REPORT

R = Report('Supermarket Business Analysis')
R.pdf.set_author('Yusuf Atolagbe')
R.pdf.set_creator('Yusuf Atolagbe')

#	DEFINING PAGEGROUPS
cover_pagegroup = Topic('Cover Pages', R)

branch_pagegroup = Topic('Comparing Branches', R)
product_line_pagegroup = Topic('Comparing Product Lines', R)
payment_type_pagegroup = Topic('Comparing Payment Types', R)
customer_rating_pagegroup = Topic('Analyzing Customer Ratings', R)
members_pagegroup = Topic('Analyzing Membership', R)
working_hours_pagegroup = Topic('Analyzing Working Hours', R)
timeline_pagegroup = Topic('Business Timeline', R)




#		DEFINING INSIGHTS 


branch_insight = Insight([
		{
			'title': 'Most Profiting Branch',
			'image': 'images/sales_per_city.png',
			'description': 'Although, the performances of the three branches are not significantly different, Lagos has the highest sales record.'
		},
		{
			'title': 'Average Customer Rating Per Branch',
			'image': 'images/Rating By City.png',
			'description': 'Abuja Branch has the lowest average customer rating among the branches'
		}
	])

payment_type_insight = Insight([
		{
			'title': 'Popular Payment Types Per City',
			'image':'images/Payment Types Popularity by City.png',
			'description': 'Port Harcourt Branch generates most cash, Abuja Branch gets more payment by card than any other branch while Lagos Branch gets more payment by Epay than any other branch'
		},
		{
			'title': 'Card Payment Lags Behind',
			'image': 'images/payment_type_count.png',
			'description': 'Card payment is the least used. It could be due to networking failures or customer preferrence. No certain conclusion can be made from the given data'
		}
	])

product_line_insight = Insight([
		{
			'title': 'Product Line Quantity Per Purchase',
			'image': 'images/product_line_quantity.png',
			'description': 'The highest sold product line is the Fashion accessories and the lowest is Beauty and Health'
		}, 
		{
			'title': 'Electronic Customers Come With Cash',
			'image': 'images/product_lines_popularity_by_payment.png',
			'description': 'Customers buying electronic accessories are most likely to pay with cash'
		},
		{
			'title': 'The Magic Price Range Per Product Line',
			'image': 'images/product_line_unit_price.png',
			'description': 'Most Sports and Travel items bought range between 19000-22000, Health and Beauty 18000-21000, etc. Hence, the business would be adviced to keep most of their stock within the respective ranges'
		},
		{
			'title': "The Company's Favorites",
			'image': 'images/product_line_quantity.png',
			'description': 'Customers are willing to pay more for Fashion accesssories but are more likely to buy fewer items. However, customers are willing to pay more for Sports and Travel and still buy the same quantity as other categories. Hence, they are our favorite customers.'
		},
		{
			'title': 'Fashion Buyers Still Rule By The Number',
			'image': 'images/product_lines_popularity.png',
			'description': 'Even though customers buy a lower quantity in Fashion accesssories, they still have the most total sales. This means Fashion items have the most customers.'
		}
	])

customer_rating_insight = Insight([
		{
			'title': 'Members And Regular Customers Feel The Same',
			'image': 'images/customer_type_rating_distribution.png',
			'description': 'The rating distributions for members and normal customers are the same which may not be a good sign for the business as we want members to rate higher than regular customers.'
		},
		{
			'title': 'The Chosen Ones Are Unpleased',
			'image': 'images/rating_by_membership.png',
			'description': 'The members give the lowest ratings and the highest ratings as well, the potential net increase in members could be zero as our current customers might leave. A gift card or a kind of promo could help'
		},
		{
			'title': 'Our Favorites Are Not Happy Either',
			'image': 'images/rating_by_product_and_membership.png',
			'description': 'The MEMBER customers buying Sports and Travel items have the lowest ratings. This is bad as they are our favorite customers since they pay more and buy more.'
		}

	])

working_hours_insight = Insight([
	{
		'title': 'Sell Time To Employees',
		'image': 'images/sales_hours.png',
		'description': '4pm-5pm has the lowest sales and the number of workers at that hour can be reduced by 10% reducing the total working hours if the workers are paid by the hour'
	}
])

timeline_insight = Insight([
	{
		'title': 'Daily Rating',
		'image': 'images/daily_rating.png',
		'description': ''
	},
	{
		'title': 'Daily Total',
		'image': 'images/daily_total.png',
		'description': ''
	},
	{
		'title': 'Conclusion',
		'image': 'images/control_chart.png',
		'description': 'The daily total averages 1.3million Naira with a standard deviation of 550 thousand Naira. Statistically, the business is stable.'
	}
	])
	
		


############## INSIGHT DEFINITION END ###################################

demo =  {
			'title': '',
			'image': '',
			'description': ''
}



#	DEFINING PAGES


R.cover_page()
branch_page = Page(branch_pagegroup)
#branch_page.write()
product_line_page = Page(product_line_pagegroup)
#product_line_page.write()
payment_type_page = Page(payment_type_pagegroup)
#payment_type_page.write()
customer_rating_page = Page(customer_rating_pagegroup)
#customer_rating_page.write()
members_page = Page(members_pagegroup)
#members_page.write()
working_hours_page = Page(working_hours_pagegroup)
#working_hours_page.write()
branch_page2 = Page(branch_pagegroup)

product_line_page2 = Page(product_line_pagegroup)

timeline_page = Page(timeline_pagegroup)
  
##################################   	WRITING INSIGHTS     #########################################################################33


branch_page.write_insight(branch_insight)
product_line_page.write_insight(product_line_insight)
payment_type_page.write_insight(payment_type_insight)
customer_rating_page.write_insight(customer_rating_insight)
#members_page.write_insight(members_insight)
working_hours_page.write_insight(working_hours_insight)
#product_line_page.write_insight(product_line_insight)
timeline_page.write_insight(timeline_insight)
#	SAVE PDF FILE

R.save('report.pdf')
