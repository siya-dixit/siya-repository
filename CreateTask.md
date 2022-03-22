3. i. Describes the overall purpose of the program
ii. Describes what functionality of the program is demonstrated in the video
iii. Describes the input and output of the program demonstrated in the video
ai. The overall purpose of the program is providing recipes for people to make at home so they can further their creativity and discover new talents and hobbies. 
ii. The search function is demonstrated in the video, along with the get recipe button which gives you the recipe. 
iii. The input demonstrated is soup, giving the output of different soups across the world. 

3b. i. The first program code segment must show how data have been stored in the list.
ii. The second program code segment must show the data in the same list being used, such as creating new data from the existing data or accessing multiple elements in the list, as part of fulfilling the program’s purpose. Then, provide a written response that does all three of the following:
iii. Identifies the name of the list being used in this response
iv. Describes what the data contained in the list represent in your program
v. Explains how the selected list manages complexity in your program code by explaining why your program code could not be written, or how it would be written differently, if you did not use the list
```
function getMealList(){
        let searchInputTxt = document.getElementById('search-input').value.trim();

        let url = `https://www.themealdb.com/api/json/v1/1/search.php?s=${searchInputTxt}`
        fetch(url)
            .then(response => response.json())
            .then(data => {
```
```
let html = "";
                if(data.meals){
                    data.meals.forEach(meal => {
                        html += `
                    <div class = "meal-item" data-id = "${meal.idMeal}">
                        <div class = "meal-img">
                            <img src = "${meal.strMealThumb}" alt = "food">
                        </div>
                        <div class = "meal-name">
                            <h3>${meal.strMeal}</h3>
                            <a href = "#" class = "recipe-btn">Get Recipe</a>
                        </div>
                    </div>
```

3c.Capture and paste two program code segments you developed during the administration of this task that contain a student-developed procedure that implements an algorithm used in your program and a call to that procedure.
i. The first program code segment must be a student-developed procedure that:
   □ Defines the procedure’s name and return type (if necessary)
   □ Contains and uses one or more parameters that have an effect on the functionality of the procedure
   □ Implements an algorithm that includes sequencing, selection, and iteration
ii. The second program code segment must show where your student-developed procedure is being called in your program.
iii. Describes in general what the identified procedure does and how it contributes to the overall functionality of the program
iv. Explains in detailed steps how the algorithm implemented in the identified procedure works. Your explanation must be detailed enough for someone else to recreate it.
```
function mealRecipeModal(meal){
        console.log(meal);
        meal = meal[0];
        let html = `
        <h2 class = "recipe-title">${meal.strMeal}</h2>
        <p class = "recipe-category">${meal.strCategory}</p>
        <div class = "recipe-instruct">
            <h3>Instructions:</h3>
            <p>${meal.strInstructions}</p>
        </div>
        <div class = "recipe-meal-img">
            <img src = "${meal.strMealThumb}" alt = "">
        </div>
        <div class = "recipe-link">
            <a href = "${meal.strYoutube}" target = "_blank">Watch Video</a>
        </div>
    `;
        mealDetailsContent.innerHTML = html;
        mealDetailsContent.parentElement.classList.add('showRecipe');
    }
```
```
                `;
                    });
                    mealList.classList.remove('notFound');
                } else{
                    html = "huh?";
                    mealList.classList.add('notFound');
                }

                mealList.innerHTML = html;
```

iii. The procedure in the code is the modal to show the recipe and instructions for the food of your choice.

iv. The algorithm takes the information from the list and displays it in HTML.

3 d. Provide a written response that does all three of the following: Approx. 200 words (for all subparts of 3d combined)
i. Describes two calls to the procedure identified in written response 3c. Each call must pass a different argument(s) that causes a different segment of code in the algorithm to execute.
First call:  Chicken
Second call: Sandwich
ii. Describes what condition(s) is being tested by each call to the procedure Condition(s) tested by the first call: Condition(s) tested by the second call: iii. Identifies the result of each call
Result of the first call:
Chicken Handi
Chicken Congee
Chicken Karaage
Chicken Marengo
Tandoori chicken
Chicken Couscous
Kung Pao Chicken
Chicken Basquaise
Chicken Parmentier
Brown Stew Chicken
Katsu Chicken curry
Nutty Chicken Curry
General Tso's Chicken
Jerk chicken with rice & peas
Result of the second call: Lasagna Sandwiches: 1. In a small bowl, combine the first four ingredients; spread on four slices of bread. Layer with bacon, tomato and cheese; top with remaining bread. 2. In a large skillet or griddle, melt 2 tablespoons butter. Toast sandwiches until lightly browned on both sides and cheese is melted, adding butter if necessary. Nutrition Facts 1 sandwich: 445 calories, 24g fat (12g saturated fat), 66mg cholesterol, 1094mg sodium, 35g carbohydrate (3g sugars, 2g fiber), 21g protein., Chick-Fil-A Sandwich: Wrap the chicken loosely between plastic wrap and pound gently with the flat side of a meat tenderizer until about 1/2 inch thick all around. Cut into two pieces, as even as possible. Marinate in the pickle juice for 30 minutes to one hour (add a teaspoon of Tabasco sauce now for a spicy sandwich). Beat the egg with the milk in a bowl. Combine the flour, sugar, and spices in another bowl. Dip the chicken pieces each into the egg on both sides, then coat in flour on both sides. Heat the oil in a skillet (1/2 inch deep) to about 345-350. Fry each cutlet for 2 minutes on each side, or until golden and cooked through. Blot on paper and serve on toasted buns with pickle slices., Grilled Mac and Cheese Sandwich: Make the mac and cheese 1. Bring a medium saucepan of generously salted water (you want it to taste like seawater) to a boil. Add the pasta and cook, stirring occasionally, until al dente, 8 to 10 minutes, or according to the package directions. The pasta should be tender but still chewy. 2. While the pasta is cooking, in a small bowl, whisk together the flour, mustard powder, garlic powder, salt, black pepper, and cayenne pepper. 3. Drain the pasta in a colander. Place the empty pasta pan (no need to wash it) over low heat and add the butter. When the butter has melted, whisk in the flour mixture and continue to cook, whisking frequently, until the mixture is beginning to brown and has a pleasant, nutty aroma, about 1 minute. Watch carefully so it does not scorch on the bottom of the pan. 4. Slowly whisk the milk and cream into the flour mixture until everything is really well combined. Cook, whisking constantly, until the sauce is heated through and just begins to thicken, about 2 minutes. Remove from the heat. Gradually add the cheese while stirring constantly with a wooden spoon or silicone spatula and keep stirring until the cheese has melted into the sauce. Then stir in the drained cooked pasta. 5. Line a 9-by-13-inch (23-by-33-centimeter) rimmed baking sheet with parchment paper or aluminum foil. Coat the paper or foil with nonstick cooking spray or slick it with butter. Pour the warm mac and cheese onto the prepared baking sheet and spread it evenly with a spatula. Coat another piece of parchment paper with cooking spray or butter and place it, oiled or buttered side down, directly on the surface of the mac and cheese. Refrigerate until cool and firm, about 1 hour. Make the grilled cheese 6. Heat a large cast-iron or nonstick skillet over medium-low heat. 7. In a small bowl, stir together the 4 tablespoons (55 grams) butter and garlic powder until well blended. 8. Remove the mac and cheese from the refrigerator and peel off the top layer of parchment paper. Carefully cut into 8 equal pieces. Each piece will make 1 grilled mac and cheese sandwich. (You can stash each individual portion in a double layer of resealable plastic bags and refrigerate for up to 3 days or freeze it for up to 1 month.) 9. Spread 3/4 teaspoon garlic butter on one side of each bread slice. Place half of the slices, buttered-side down, on a clean cutting board. Top each with one slice of Cheddar, then 1 piece of the mac and cheese. (Transfer from the baking sheet by scooting your hand or a spatula under each piece of mac and cheese and then flipping it over onto a sandwich.) Place 1 slice of Jack on top of each. Finish with the remaining bread slices, buttered-side up. 10. Using a wide spatula, place as many sandwiches in the pan as will fit without crowding it. Cover and cook until the bottoms are nicely browned, about 4 minutes. Turn and cook until the second sides are browned, the cheese is melted, and the mac and cheese is heated through, about 4 minutes more. 11. Repeat with the remaining ingredients. Cut the sandwiches in half, if desired, and serve.  
