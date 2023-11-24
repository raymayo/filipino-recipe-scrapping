import json
import requests
from bs4 import BeautifulSoup
import re
from colorama import init, Fore

all_array = []  

json_file_path = './recipes/lunch_recipes.json'


with open(json_file_path, 'r') as json_file:

    data = json.load(json_file)
    
 
for recipe in data:
        
    base_url = recipe['recipe-link']
    
    url = f'{base_url}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.1 Safari/537.36'} 
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    container = soup.find('section', class_='oc-recipe-content')
    

    
    ingredients_container = container.findAll('ul', class_='wprm-recipe-ingredients');
    
    pattern = r'\([^)]*\)'
    
    ingredient_array = []
    

    
    
    for ul in ingredients_container :
        
        ingredients = ul.findAll('li', class_='wprm-recipe-ingredient')
    
        words_to_remove = ['pieces round','cut into wedges','for color','made by placing 4 slices of tasty bread in a food processor. If not using any food processor, just tear the bread','or 6 pcs hot dogs, cut in half lengthwise','diluted in','cup water','sliced into squares','either grated or thinly sliced','lapu-lapu fish, cleaned, scales removed, and salted','sitaw, cut in 2 inch length','diluted in 3 tablespoons water','a hint of','almejas','arroz amarillo','seasoned','birds eye chili','sherry cooking','fresh shrimp','silver fish','frozen or fresh','cut into steaks','45g','soaked in a cup of water','ground black pepper, and sugar to taste','in can','pata, sliced or whole','and crushed peppercorn to taste','or 3 tbsp fish sauce','or 3 tbsp fish sauce','or 2 teaspoons beef powder','or baked, and then flaked','of the shrimp','soaked in water','flour sticks pancit canton','boiled and shredded',' or wedged','and ground black pepper to taste','1/2','7 ','1-inch','2-inch','5 f','0 f',' inch ','10','2','3','4','5','6','8','9','1','11','12','13','14','15','16','17','18','19','20','½','⅓','¼','⅔','¾','⅛','0','cups ','cup ','tbsp','baguio beans','tsp','orpimento','tri color','steamed','grams','according','instructions','maui','minced','mince','about','kilo','quarts','slices','patis','each','tripe','ripe','thumb-sized','thumb-size','teaspoons','frozen','diced',' and ','grated','toasted','seedless','processed','bundle','using','crosswise','blender','ounces','for frying',' for ','deep-frying','cdo','crispy','cutlets','rings','scales','tasty','deveined',' with ','tails','strips','liquid','flavoring','tahong','slightly','unflavored','boiling','flavor','extract','crosswise','torn','little','portions','quartered','quarters','hard-boiled','unripe','finger','lbs','drumettes','cooked','sauteed','tidbits','sifted','+','cold','all-purpose','.','reserved','young','vegetarian','lardchilled','bunch','japanese','heated','chinese','cooking','thawed','#',' water ','manila','patis','a pinch of','packed','ounces','teaspoon','clear','cubed','cans','in oil' ,'tablespoons','drained','florets' ,'tablespoon',' ap ','heads ','head','softened','ml','pounds','peeled','julienned','julienne','thumbs','thumb','sized','size','dissolved in','drained','cored','romaine','roma','thinly','thin','strips','cut in half','cut',' ice ','into','granules','instant','homemade','slivers','guisado','1-inch','cubes','juice of','chopped','cleaned','jumbo',' - ','- ',' -','boneless','lengths','length','peel','skinless','ice cold',' can ','whole','optional','cracked','diced',' stick ','removed','melted','desiccated','kept','finely','fine',' parts','plus','dusting','more','kneading',' lukewarm','warm','sprinkling','on top','from','bone-in','deboned','one','from eggs','pounded','separated',' lightly','whites','pounding', 'pound','toinch',"bird’s eye chili",'siling pansigang','drops','baby','butterfliedgutteddebd','diluted','inwater','galunggongdebdflaked','packages','pack','silken',' leaftied knot','chunky-style','meatremoved','shelled','shell','hulled','halved','preferably colorless','american processed','▢','oz','/ ','lb','% lean', '%','extra','evaporated', 'cloves', 'medium', 'small', 'beaten','peices','rolling', 'between','mashed','chunks','chilled', 'bones','on the','semi-sweet','derived',"lady's choice",'torta','packet','dried','sharp','shavings','brushing','active dry','room temperature','temperature of','temperature', 'crushed','very','soft','unsweetened','sweetened','smelt', '1slices','block','firm',' x ', 'pieces ', 'package ',' well','raw', 'seeded', '2-inch ', 'sized', 'serving', 'pieces', 'freshly','roasted','unsalted',' at ', 'fresh', 'ends','coating', 'trimmed', 'Inch','-inch', 'rounds', 'diagonally', 'two','temperature', 'triangles','shredded','piece','large', 'stemmed', 'thai','quarted','lengthwise', 'thirds', 'to taste','to a',' to ', 'wide', '¼', 'thick','sliced in', 'sliced', 'thinly',', ', ',','        ','       ','      ','     ','    ','   ']
        
        print(recipe['recipe-link'])     
        for ingr in ingredients:
            ingr_name = ingr.text.lower()

            for word in words_to_remove:
                ingr_name = ingr_name.replace(word,'')
            final_ingr = re.sub(pattern, '', ingr_name).strip()
            print(final_ingr)
        print()
            # ingredient_array.append(final_ingr)
            # print(final_ingr)   
#             if final_ingr in all_array:
#                 print()
#             else :
#                 all_array.append(final_ingr)
#                 print(all_array)
                        
#                 with open('lunch.json', 'w') as json_file:
#                     json.dump(all_array, json_file, indent=4)
                        
# print(Fore.RED + 'ALL INGREDIENTS HAVE BEEN SAVED!!!')





            
            # removeWord(ingr_name, words_to_remove)



        # if len(ingredients_container) >= 2:
        #     second_result = ingredients_container[2]
        #     ingredients = second_result.find_all('li')
            
        #     ingredient_array = []
            
        #     for ingr in ingredients :
                
        #         ingr_name = ingr.text.split('-')
        #         name_sorted = ingr_name[0].lower().split(', ')
                
        #         for name in name_sorted :
        #             print()
                    
        #             ingredient_array += name.split(' and ')
                
        #         # print(ingredient_array)
                
        #         # ingredient_array.append(name_sorted.lower())
        #             new_key = 'ingredients'
        #             new_data = ingredient_array
        #             recipe[new_key] = new_data
                    
        #             print(ingredient_array)
                    
        #             with open(json_file_path, 'w') as json_file:
        #                 json.dump(data, json_file, indent=4)
                        
        #                 print('all saved')
            
        # elif  len(ingredients_container) == 1 :
        #     print("RESULT IS SHORT")   
        # else:
        #     print("Not enough results")
        