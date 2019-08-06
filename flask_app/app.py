from flask import Flask, render_template 
from flask import Flask, redirect, url_for, request
import pandas as pd
from get_recs import *
# import numpy as np
# from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

with open('../data/restaurant_df.pkl','rb') as f:
    df = pickle.load(f)

@app.route("/", methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/recs', methods=['GET', 'POST'])
def recs():
    # if request.method == 'POST':
    #     result = request.form
    #     return render_template("recs.html", venue = )

    W, H = get_latent_topics(df)
    cos_sim = get_cosine_sim(W)
    # venue = 
    recs = get_recs("Illegal Pete's", cos_sim)
    return render_template("recs.html", recs=recs)

@app.route('/Abos', methods=['GET', 'POST'])
def abos():
    # if request.method == 'POST':
    #     result = request.form
    #     return render_template("recs.html", venue = )

    W, H = get_latent_topics(df)
    cos_sim = get_cosine_sim(W)
    # venue = 
    recs = get_recs("Abo's Pizza", cos_sim)
    return render_template("recs.html", recs=recs)

@app.route('/Ados', methods=['GET', 'POST'])
def ados():
    # if request.method == 'POST':
    #     result = request.form
    #     return render_template("recs.html", venue = )

    W, H = get_latent_topics(df)
    cos_sim = get_cosine_sim(W)
    # venue = 
    recs = get_recs("Ado's Kitchen and Bar", cos_sim)
    return render_template("recs.html", recs=recs)

@app.route('/Akiyama', methods=['GET', 'POST'])
def akiyama():
    # if request.method == 'POST':
    #     result = request.form
    #     return render_template("recs.html", venue = )

    W, H = get_latent_topics(df)
    cos_sim = get_cosine_sim(W)
    recs = get_recs("Akiyama Sushi Bar and Grill", cos_sim)
    return render_template("recs.html", recs=recs)

@app.route('/Alibaba', methods=['GET', 'POST'])
def alibaba():
    # if request.method == 'POST':
    #     result = request.form
    #     return render_template("recs.html", venue = )

    W, H = get_latent_topics(df)
    cos_sim = get_cosine_sim(W)
    # venue = 
    recs = get_recs("Alibaba Grill", cos_sim)
    return render_template("recs.html", recs=recs)

if  __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True, threaded=True)

names = ['3 Margaritas',
 'A Cup Of Peace',
 'Abbys coffee',
 "Abo's Pizza",
 "Ado's Kitchen and Bar",
 'Agave Mexico Bistro & Tequila House',
 'Akiyama Sushi Bar and Grill',
 'alforat resturant',
 'Alibaba Grill',
 'Allegro Coffee Roasters',
 'Aloy Thai Cuisine',
 'Alpine Modern Cafe',
 'Altitude Cafe',
 'Amante Baseline',
 'Amante Coffee',
 'Amante Uptown',
 'Ampersand Coffee',
 'Amu',
 'AOI Sushi and Izakaya',
 'Aperitivo',
 'Arabesque',
 'Arcana',
 'Attic Bar & Bistro',
 "Audrey Jane's Pizza Garage",
 'Bacco Trattoria & Mozzarella Bar',
 'Backcountry Pizza & Tap House',
 'bartaco Boulder',
 'BASTA',
 'Beleza Coffee Bar',
 "Ben & Jerry's",
 'Bento-ria',
 'Big City Burrito',
 'Big Daddy Bagels',
 "BJ's Restaurant & Brewhouse",
 'Black Cat',
 'Black Pepper Pho',
 'Blackbelly',
 'Blackjack Pizza & Salads',
 'Bohemian Biergarten',
 'Bona Coffee Roasters',
 'Boss Lady Pizza',
 'Boulder Baked',
 'Boulder Chophouse & Tavern',
 'Boulder Cork',
 'Boulder Pho',
 'Boulder Salad',
 'Boxcar Coffee Roasters',
 'Bramble & Hare',
 'Brasserie Ten Ten',
 'Breadworks Bakery & Cafe',
 'Breakfast Champion',
 'Brewing Market',
 'Brooklyn Pizza',
 'Buddha Cafe',
 'Burger Radio',
 'Cafe Aion',
 'Cafe Blue',
 'Cafe Mexicali',
 'Caffè Sole',
 'California Pizza Kitchen',
 "Canyon's Restaurant & Bar",
 'Carabiner Coffee Co.',
 "Carelli's Restaurant",
 'Caspian Mediterranean Deli And Grocery',
 'Celestial Seasonings',
 'Centro Mexican Kitchen',
 'Chautauqua Dining Hall',
 'Cheba Hut Toasted Subs',
 'Chez Thuy',
 'Chimera',
 'Chipotle Mexican Grill',
 'Cilantros Mexican',
 'Cold Stone Creamery',
 'Comida Taco Truck',
 'Corrida',
 "Cosmo's Pizza",
 'Crepes To Go Go',
 'Cuban Fusion',
 'Curry n Kebob',
 "D'Angelo's Italian Deli",
 'Dagabi Cucina',
 "Davey's Diner",
 'Deli at Flatiron Park',
 'Deli Zone',
 'Diaz Farm Taco Truck',
 'Dish Gourmet',
 "Dot's Diner",
 "Dot's Diner on the Hill",
 "Doug's Day Diner",
 'Dushanbe Teahouse',
 'Eco-Cuisine, Inc.',
 'Efrains II Mexican Food Restaurant',
 'Element Bistro',
 "Esteban's",
 "Etai's Bakery Cafe",
 'Eureka!',
 'Extreme Pita',
 'Falafel King',
 "Fast Eddie's Famous Chicago Hot Dogs",
 'Fat Shack - Boulder',
 'Figure Grounds',
 'Fior di Latte',
 'Firehouse Subs',
 'Five Guys',
 'Five On Black',
 'Five Spice Asian Cuisine',
 'Flagstaff House Restaurant',
 'Flatiron Coffee',
 'Flower Child',
 'Flower Pepper',
 'Folsom Thai',
 "Foolish Craig's Cafe",
 'Frasca Food and Wine',
 'Freeze',
 'Fresh Thymes Eatery',
 'Fuji Cafe and Bar',
 'Gaku Ramen',
 'Garbanzo Mediterranean Fresh',
 'Gather',
 'Gelato Boy',
 'Glacier Homemade Ice Cream & Gelato',
 'Gold Hill Inn',
 'Golden Sun',
 'Gondolier Italian Eatery',
 'Good Times Burgers & Frozen Custard',
 'Goody Monster',
 'Great Harvest Bread Company',
 'Gurkhas On The Hill',
 'Häagen-Dazs',
 'Half Fast Subs',
 'Hana Sushi',
 'Haoway Chinese Cafe',
 'Hapa Sushi Grill and Sake Bar',
 'Heifer and the Hen',
 'Il Pastaio',
 "Illegal Pete's",
 'Innisfree Poetry Bookstore And Cafe',
 'Insomnia Cookie',
 'Izote Latin Foods Truck',
 'Jaipur Indian Restaurant',
 'Jamba Juice',
 'Japango',
 "Jason's Deli",
 'Jax Fish House Boulder',
 "Jill's Restaurant & Bistro",
 'Jin Chan',
 'Kalita Grill Greek Café',
 'Kasa Japanese Grill & Bar',
 'kathmandu Restaurant II',
 'Khow Thai Cafe',
 'Kilwins',
 "Kim & Jake's Cakes",
 "Kim's Food To Go",
 'Korea House - Boulder',
 "KT's BBQ",
 'Ku Cha House of Tea',
 'Kung Fu Tea',
 "L'Atelier",
 'La Choza',
 "La'au's",
 'Larkburger',
 'Lazy Dog Sports Bar & Grill',
 'Le French Café',
 'Le Frigo',
 'Le Peep',
 'Leaf Vegetarian Restaurant',
 "Lindsay's Boulder Deli",
 'Little Tibet Restaurant and Bar',
 "Logan's Espresso Cafe",
 'Lollicup',
 'Los Dos Bros',
 "Lucile's",
 "Lucky's Bakehouse & Creamery",
 "Lucky's Cafe",
 'MAD Greens',
 'Mateo',
 'May Wah Cuisine',
 'McDevitt Taco Supply',
 "Miller's BBQ Food Truck",
 'Modmarket',
 "Moe's Bagels",
 "Moe's Original Bar B Que",
 'Motomaki',
 'Mount Everest Cuisine',
 'Mountain Sun Pub & Brewery',
 "Murphy's South",
 "Mustard's Last Stand",
 'My Ramen & Izakaya',
 'Native Foods',
 'nepal cuisine',
 'Next Door Boulder',
 "Nick and Willy's Take And Bake Pizza",
 'Noodles & Company',
 'Nothing Bundt Cakes',
 'OAK at fourteenth',
 "Oregano's Pizza Bistro",
 'Organic Sandwich Company',
 "Osaka's",
 'Oskar Blues',
 'Ozo Coffee',
 "Papa Murphy's",
 'Parkway Cafe',
 'Passport Traveling Eatery',
 "Pasta Jay's",
 'Pei Wei',
 'Pekoe Sip House',
 'Pho Kitchen',
 "Pica's Mexican Taqueria",
 'Pizza Colore',
 'PizzaRev',
 'Pizzeria Locale',
 'Potbelly Sandwich Shop',
 'Protein Bar & Kitchen',
 "Proto's Pizza",
 "Ralphie's Sports Bar and Grill",
 "Ras Kassa's Ethiopian",
 "Rat's Wood Shack",
 'Red Rock Coffee House',
 'Riffs Urban Fare',
 'Rincon Argentino',
 'Rincon Del Sol',
 'Rio Grande',
 'Ripple Pure Frozen Yogurt',
 'River and Woods',
 'Rolling Greens Food Truck',
 "Roxie's Tacos",
 "Rudi's Organic Bakery",
 "Rueben's Burger Bistro",
 'Rush Bowls',
 'Ruthies Boardwalk Social',
 'SALT the Bistro',
 "Salvaggio's Deli",
 "Sancho ' Mexican Restaurant",
 "Santiago's",
 'Santo',
 'scrooge maki',
 "Seb's Portable Wood-Fired Cuisine",
 'Sforno Trattoria Romana',
 "Shamane's Bake Shoppe",
 "Sherpa's Adventure Restaurant & Bar",
 'Shine Restaurant & Gathering Place',
 'Smashburger',
 "Snarf's Sandwiches",
 'Snarfburger',
 'Snooze An A.M. Eatery',
 'South Mouth: Memphis HOT Wings',
 'South Side Walnut Cafe',
 'Southern Sun Pub & Brewery',
 'Spruce Confections',
 'Spruce Farm and Fish',
 'Steakhouse No. 316',
 'Street Legal Pizza',
 'Sushi Zanmai',
 'Sweet Cow',
 'T|ACO',
 'taco junky',
 'Tacos del Norte',
 'Tadka Indian Cuisine',
 'Tahona Tequila Bistro',
 'Taj Restaurant',
 'Tandoori Grill',
 'Tangerine',
 'Tasuki Sushi Bistro',
 "Ted's Montana Grill",
 'Tee & Cakes',
 'Thai Avenue',
 'The Buff Restaurant',
 'The Corner',
 'The Deli',
 'The French Twist',
 'The Goat at the Garage',
 'The Greenbriar Inn',
 'The Hungry Toad',
 'The Kitchen Boulder',
 'The Laughing Goat',
 'The Mediterranean',
 'The Morning Table',
 'The North End at 4580',
 'The Point Cafe',
 'The Roadhouse Boulder Depot',
 'The Root Kava Co.',
 'The Sink',
 'The Unseen Bean',
 'The Wheel & Whisk',
 'The Yellow Deli',
 'thrive',
 'Tibet Kitchen',
 'Tibet’s Food Truck',
 'Tiffins India Cafe',
 "Tod's Espresso Cafe",
 'Tonic',
 "Tra Ling's",
 'Trident Booksellers & Cafe',
 'Tsing Tao Chinese Restaurant',
 'Twisted Pine Brewing Company',
 'University Hill Market & Deli',
 'Verde',
 'Vero Wood Fired Pizza',
 'Via Perla',
 "Vic's Again on 3th",
 "Vic's Coffee",
 'Village Coffee Shop',
 'Vina Pho & Grill',
 'Vitality Bowls Boulder',
 "Wahoo's Fish Taco",
 'Walnut Cafe',
 'Wapos',
 'West End Tavern',
 'What The Fork Food Truck',
 'Wild Standard',
 'Wonder Press',
 'Woodgrain Bagels',
 'World Famous Dark Horse Bar & Grill',
 'Yellowbelly',
 'You and Mee Noodle House',
 'Yurihana Sushi Bar and Pan-Asian Cuisine',
 'Zoe Ma Ma',
 'Zolo Southwestern Grill',
 'zpizza']