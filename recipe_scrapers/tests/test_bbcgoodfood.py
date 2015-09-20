import os
import unittest

from recipe_scrapers.bbcgoodfood import BBCGoodFood


class TestBBCGoodFoodScraper(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.getcwd(),
            'recipe_scrapers',
            'tests',
            'test_data',
            'bbc_good_food.html'
        )) as file_opened:
            self.harvester_class = BBCGoodFood(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'bbcgoodfood.com',
            self.harvester_class.host()
        )

    def test_publisher_site(self):
        self.assertEqual(
            'http://bbcgoodfood.com/',
            self.harvester_class.publisher_site()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            'Cookie Monster cupcakes'
        )

    def test_total_time(self):
        self.assertEqual(
            0,
            self.harvester_class.total_time()
        )

    def test_ingredients(self):
        self.assertListEqual(
            [
                '12 Cupcakes (I used the Lemon and Poppyseed recipe on this website and substituted vanilla for the lemon and poppyseeds)',
                'Frosting',
                'The frosting I\n made using a vegetable shortening (in Aus its called So Lite, I think \nin the US Crisco is similar) and icing sugar mixture.  You could use \nbutter cream but the frosting is pure white and colours beautifully.  \nYou would need to double the buttercream you usually use for 12 cupcakes',
                'Blue colouring - use a good one for the best colour',
                'Coconut - dyed blue to match the frosting',
                '12 Choc chip cookies',
                'Melted white and dark chocolate to make the eyes.'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            "I\n used an icecream scoop full of frosting to get the right shape and then\n dipped in it coconut. Press the coconut on and tidy up the shape.\nWhen\n the frosting has firmed a little cut a slice out near the bottom and \npush a cookie in (you may have to trim the cookie little depending on \nthe size of your cookies). Or make his mouth further up and put cookie \npieces around it.\nThe\n eyes I made by using melted white to make a circle and then dark \nchocolate in the middle.  Don't make them all exactly the same - it adds\n a bit of character to the finished cakes!\nSimple - very messy and lots of fun!",
            self.harvester_class.instructions()
        )