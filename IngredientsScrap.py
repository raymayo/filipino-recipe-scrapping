import json
import requests
from bs4 import BeautifulSoup
import re
from colorama import init, Fore

all_array = []  
# all_array = ['','']  
        
        
# json_file_path = './test.json'
# json_file_path = './recipes/appetizer_recipes.json'
json_file_path = './recipes/lunch_recipes.json'

# Open the JSON file for reading
with open(json_file_path, 'r') as json_file:
    # Load the JSON data
    data = json.load(json_file)
    
 
# Now, 'data' contains the content of the JSON file as a Python data structure
# You can access and manipulate the data as needed
for recipe in data:
        
    base_url = recipe['recipe-link']
    
    url = f'{base_url}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.1 Safari/537.36'} 
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    container = soup.find('section', class_='wprm-entry-content')
    

    
    ingredients_container = container.findAll('ul', class_='wprm-recipe-ingredients');
    
    pattern = r'\([^)]*\)'
    
    ingredient_array = []
    

    

    for ul in ingredients_container :
        
        
        
        ingredients = ul.findAll('li', class_='wprm-recipe-ingredient')
    
        words_to_remove = ['7 ','1-inch','5 f','0 f',' inch ','10','2','3','4','5','6','8','9','1','11','12','13','14','15','16','17','18','19','20','½','⅓','¼','⅔','¾','⅛','0','cups ','cup ','tbsp','tsp','grams','maui','minced','mince','slices','each','ripe','thumb-sized','thumb-size','teaspoons','frozen','diced',' and ','grated','toasted','seedless','ounces',' for ','deep-frying','cutlets','deveined',' with ','tails','strips','liquid','flavoring','slightly','unflavored','flavor','extract','torn','little','portions','quartered','hard-boiled','unripe','finger','lbs','drumettes','cooked','sauteed','tidbits','sifted','+','cold','all-purpose','.','reserved','young','lardchilled','bunch','japanese','heated','chinese','cooking','thawed',' water ','manila','packed','ounces','teaspoon','clear','cubed','cans','in oil' ,'tablespoons','drained' ,'tablespoon','head','softened','ml','pounds','peeled','julienned','thumb','size','dissolved in','drained','cored','roma','thinly','thin','strips','cut',' ice ','into','granules','instant','homemade','slivers','guisado','1-inch','cubes','juice of','chopped','jumbo',' - ','- ',' -','thumb-size','boneless','lengths','peel','skinless','ice cold',' can ','whole','optional','cracked','diced',' stick ','melted','desiccated','kept','finely','fine','plus','dusting','more','kneading',' lukewarm','warm','sprinkling','on top','from','one','from eggs','pounded','separated',' lightly','whites', 'pound','evaporated', 'cloves', 'medium', 'small', 'beaten','peices','rolling', 'between','mashed','chunks','chilled', 'bones','on the','semi-sweet','torta','packet','dried','sharp','shavings','brushing','active dry','room temperature','temperature of','temperature', 'crushed','very','soft','unsweetened','sweetened','smelt', '1slices','block','firm',' x ', 'pieces ', 'package ',' well', 'seeded', '2-inch ', 'sized', 'serving', 'pieces', 'freshly','roasted','unsalted',' at ', 'fresh', 'ends','coating', 'trimmed', 'Inch','-inch', 'rounds', 'diagonally','f f', 'two','temperature', 'triangles','shredded','piece','large', 'stemmed', 'thai','quarted','lengthwise', 'thirds', 'to taste','to a',' to ',' a ', 'wide', '¼', 'thick', 'sliced', 'thinly',', ', ',','        ','       ','      ','     ','    ','   ','toinch','drops','baby','butterfliedgutteddebd','diluted','inwater','galunggongdebdflaked','packages','silken',' leaftied knot','chunky-style','meatremoved','shell','hulled','halved','preferably colorless','american processed']
        
        # words_to_remove = ['z']
        
        # def removeWord(input,remove):
        #     for word in words_to_remove:
        #         input = input.replace(word,'')

        #     print(re.sub(pattern, '', input))




        print(recipe['recipe-link'])     
        for ingr in ingredients:
            ingr_name = ingr.text.lower()

            for word in words_to_remove:
                ingr_name = ingr_name.replace(word,'')
            final_ingr = re.sub(pattern, '', ingr_name).strip()
            # ingredient_array.append(final_ingr)
            # print(final_ingr)   
            if final_ingr in all_array:
                print()
            else :
                all_array.append(final_ingr)
                print(all_array)
                        
                with open('lunch.json', 'w') as json_file:
                    json.dump(all_array, json_file, indent=4)
                        
print(Fore.RED + 'ALL INGREDIENTS HAVE BEEN SAVED!!!')





            
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
        