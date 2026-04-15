Experiment 9

Aim

To write a program to create and display a Pandas DataFrame with multiple columns of categorical data.

Algorithm

1. Import the pandas library as pd.
2. Create a dictionary with 10 keys: menu, price, brands, cars, games, animals, colors, cities, sports, devices.
3. Assign each key a list of 10 string or integer values.
4. Convert the dictionary into a Pandas DataFrame using pd.DataFrame().
5. Print the DataFrame.

Output

```
      menu  price     brands           cars        games   animals   colors     cities     sports   devices
0    Pizza    350      Gucci       Mercedes          GTA       Cat      Red      Delhi    Cricket     Phone
1   Burger    200        LV           BMW   Candy Crush      Lion     Blue     Mumbai   Football    Laptop
2    Fries    150      Dior          Audi          WWM   Leopard    Green  Bangalore     Tennis    Tablet
3     Coke     70  Louboutin   Aston Martin          RDR     Tiger    Black    Chennai     Hockey     Watch
4    Pasta    220       YSL        Ferrari         RDR2   Panther    White   Kolkata  Basketball        PC
5   Biryani    250    Chanel         Honda        Wukong  Cheetah   Yellow  Hyderabad   Kabaddi    Camera
6   Butter    170   Versace       Toyota      Valorant      Dog   Purple     Pune        F1        TV
7  Tiramisu    350    Hermes       Porsche          COD     Wolf     Pink     Jaipur       Golf   Speaker
8  Pancakes    250    Armani       Bugatti          WT   Elephant   Orange       Goa     Boxing   Console
9  Ice Cream   110     Rolex           KTM      Genshin      Fox    Brown     Kochi        F1     Drone

