{
    'name': 'Theme Laze',
    'category': 'Theme/Ecommerce',
    'summary': "Theme Laze is a Odoo theme with advanced ecommerce feature, extremely customizable and fully responsive. It's suitable for any e-commerce sites. Start your Odoo store right away with The Laze theme",
    'version': '6.4',
    'author': 'Atharva System',
	'website' : 'http://www.atharvasystem.com',
	'license' : 'OPL-1',
    'description': """
Theme Laze is  is a Odoo theme with advanced ecommerce feature, extremely customizable and fully responsive. It's suitable for any e-commerce sites. Start your Odoo store right away with The Laze theme.
        """,
    'depends': ['website_sale','website_mass_mailing','website_crm','website_blog','website_event','website_sale_wishlist','website_sale_comparison','website_sale_stock'],
    'data': [ 
        'views/website_setting.xml',
		'views/product_brand_view.xml',                                                         
        'views/product_category_view.xml',
        'views/templates.xml',
        'views/assets.xml',
        'views/snippets.xml',  
        'views/customize_template.xml',  
		'views/website_menu_view.xml',
		'views/mega_menu_template.xml', 
		'views/product_slider_templates.xml',
		'security/ir.model.access.csv',
        'views/product_brand_template.xml',
        'views/multi_tab_configure_view.xml',
        'views/snippet_multitab_slider.xml',
		'views/website_blog_config.xml',
		'views/snippet_blog_template.xml',
		'views/product_brand_page.xml',
        'views/breadcum_template.xml'
    ],
    'live_test_url': 'http://theme-laze.atharvasystem.com',    
	'support': 'support@atharvasystem.com',
    'images': ['static/description/laze.png','static/description/laze_screenshot.png'],
    'price': 145.00,
    'currency': 'EUR',
	'installable': True,
    'application': True,    
}
