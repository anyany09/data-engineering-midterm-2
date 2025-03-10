Here is a final, refined version of the exam with integrated recommendations:

---

# მონაცემთა ინჟინერიის მეორე შუალედური გამოცდა

**ხანგრძლივობა:** 4 საათი  
**ჯამური ქულა:** 100  
**რესურსები:** გამოცდა არის *open-book*. შეგიძლიათ გამოიყენოთ ნებისმიერი პირადი ჩანაწერი, დოკუმენტაცია და ონლაინ რესურსი, თუმცა კოდის პირდაპირი დაკოპირება არ არის რეკომენდებული.

ქვემოთ მოცემულია ორი ძირითადი ნაწილი: (A) თეორიული ამოცანები და (B) პრაქტიკული ამოცანები. *გაითვალისწინეთ,* რომ ქულები გადანაწილებულია თანაბრად ამ ორ ბლოკს შორის (თეორია 40 ქულა, პრაქტიკა 60 ქულა). გთხოვთ, აკონტროლოთ დრო შესაბამისად.

## წარდგენის ინსტრუქცია

1. შექმენით საჯარო GitHub რეპოზიტორია სახელით **`data-engineering-midterm-2`**.
2. რეპოზიტორიაში ატვირთეთ:
    - თეორიული კითხვების პასუხები ერთ Markdown ფაილში, სახელი: **`theory_answers.md`**
    - პრაქტიკული ამოცანების კოდი ცალკეულ დირექტორიებში (მაგ. `problem_7`, `problem_8`, `problem_10`).
    - თითოეული პრაქტიკული ამოცანის დირექტორიაში ჩადეთ **`commands.txt`** ფაილი, სადაც აღწერილი იქნება ტერმინალში შესრულებული ბრძანებების ისტორია (მაგ. `history > commands.txt`).
    - დაწერეთ დეტალური **`README.md`** თითოეული ამოცანისთვის (როგორ გამოვიყენოთ, როგორ გავუშვათ აპლიკაცია).

**გაფრთხილება:** დაუთმეთ საკმარისი დრო როგორც თეორიულ, ისე პრაქტიკულ კითხვებს. რეკომენდებულია დაახლოებით **2 საათი** თითოეულზე.

---

## A. თეორიული ამოცანები (40 ქულა)

(თითო კითხვა: 8 ქულა)

1. **Redis-ის შესახებ**  
   a) აღწერეთ Redis-ის 5 ძირითადი მონაცემთა ტიპი და მათი გამოყენების შემთხვევები.  
   b) განმარტეთ, როგორ უზრუნველყოფს Redis მონაცემთა მდგრადობას (persistence).

2. **Apache Kafka-ს შესახებ**  
   a) აღწერეთ Kafka-ს ძირითადი კომპონენტები (brokers, topics, partitions, consumer groups).  
   b) როგორ უზრუნველყოფს Kafka მასშტაბირებადობას და მაღალ წარმადობას?

3. **Apache Airflow-ს შესახებ**  
   a) რა არის DAG? ახსენით მისი ძირითადი მახასიათებლები.  
   b) განასხვავეთ Airflow-ს Operators და Sensors ერთმანეთისგან.

4. **ETL vs ELT**  
   a) შეადარეთ ეს ორი მიდგომა – რა უპირატესობები და ნაკლოვანებები აქვს თითოეულს?  
   b) მოიყვანეთ კონკრეტული შემთხვევები, როდესაც ერთი მეორეზე უკეთესია.

5. **მონაცემთა შენახვის კონცეფციები**  
   a) აღწერეთ განსხვავებები Data Lake, Data Warehouse და Data Mart-ს შორის.  
   b) როგორ უკავშირდება თითოეული ETL/ELT პროცესებს?

---

## B. პრაქტიკული ამოცანები (60 ქულა)

### 7. Docker და Python (20 ქულა)

**ამოცანის პირობა:**
- შექმენით მარტივი Python აპლიკაცია, რომელიც წაიკითხავს CSV ფაილს (თქვენი არჩევით), ჩაატარებს მარტივ დამუშავებას (მაგ. ფილტრაცია, დაჯგუფება, აგრეგაცია) და შეინახავს შედეგებს ახალ CSV ფაილში.

#### გასათვალისწინებელი მოთხოვნები:
1. **Dockerfile** – შექმენით Dockerfile, რომელიც შექმნის აპლიკაციის კონტეინერს.
2. **shell სკრიპტი** – წერდეს კონტეინერის გაშვებისა და საჭირო არგუმენტების გადაცემის ინსტრუქციას.
3. **commands.txt** – დაიმახსოვრეთ ყველა ტერმინალში შესრულებული ბრძანება.
4. **README.md** – დეტალურად აღწერეთ აპლიკაციის გაშვების ინსტრუქცია (როგორ მოვამზადოთ Docker image, როგორ გავუშვათ კონტეინერი).

**რჩევა:**
- გამოიყენეთ, მაგალითად, `history > commands.txt` აუთენტური ბრძანებების ჩასაწერად.
- ყურადღება მიაქციეთ იმპორტებსა და დამოკიდებულებებს (requirements.txt ან მსგავსი მექანიზმი Dockerfile-ში).

---

### 8. FastAPI და SQLite (20 ქულა)

**ამოცანის პირობა:**
- შექმენით მარტივი FastAPI აპლიკაცია, რომელიც ამოღებს მონაცემებს SQLite მონაცემთა ბაზიდან და გამოიტანს ამ მონაცემებს API ენდპოინტზე.

#### გასათვალისწინებელი მოთხოვნები:
1. **SQLite მონაცემთა ბაზის შექმნის სკრიპტი** – ცხრილების სტრუქტურა და საწყისი მონაცემები.
2. **FastAPI აპლიკაცია** – მინიმუმ ერთი GET ენდპოინტი, რომელიც აბრუნებს მონაცემებს.
3. **Dockerfile** – აპლიკაციის გასაშვებად.
4. **shell სკრიპტი** – აპლიკაციის გაშვება Docker გარემოში.
5. **commands.txt** – ყველა შესრულებული ბრძანება.

**რჩევა:**
- ცხრილების მაგალით-სტრუქტურა (id, name, age…), როგორც თქვენ მიგაჩნიათ საჭიროდ.
- FastAPI-ის დასაყენებლად გამოიყენეთ Dockerfile-ში შესაბამისი ინსტალაცია (e.g. `pip install fastapi uvicorn`).

---

### 10. ნაწილობრივი ფუნქციები (Partial Functions) მონაცემთა ტრანსფორმაციაში (20 ქულა)

**ამოცანის პირობა:**  
Python-ის ფუნქციონალური პროგრამირების ერთ-ერთი ინსტრუმენტია `functools.partial()`, რომელიც საშუალებას გაძლევთ შექმნათ ახალი ფუნქციები უკვე არსებული ფუნქციების საფუძველზე, წინასწარ მიცემული არგუმენტებით. მონაცემთა ინჟინერიაში ეს სასარგებლოა მრავალფეხურიანი ტრანსფორმაციების დროს.

#### a) შექმენით ძირითადი ტრანსფორმაციის ფუნქცია (10 ქულა):

```python
def transform_data(data, column_mapping=None, date_format=None, 
                  numeric_precision=2, missing_values='drop', 
                  filters=None):
    """
    მთავარი ფუნქცია მონაცემთა ტრანსფორმაციისთვის
    
    პარამეტრები:
    - data: დასამუშავებელი მონაცემები (DataFrame)
    - column_mapping: ლექსიკონი, რომელიც სვეტების სახელების გადარქმევას ახდენს
    - date_format: თარიღის ფორმატი გარდაქმნისთვის
    - numeric_precision: რიცხვების დამრგვალების სიზუსტე
    - missing_values: როგორ მოვიქცეთ ცარიელი მნიშვნელობებისას ('drop', 'fill_zero', 'fill_mean')
    - filters: გამოსაყენებელი ფილტრები (ლექსიკონი {column: value})
    
    აბრუნებს:
    - დამუშავებულ მონაცემებს
    """
    # დაწერეთ ფუნქციის ლოგიკა აქ
```

**გასათვალისწინებელი მოქმედებები:**
- სვეტების გადარქმევა `column_mapping`-ის მიხედვით
- თარიღის ფორმატში გარდაქმნა (თუ `date_format` არაა None)
- რიცხვების დამრგვალება `numeric_precision`-ის მიხედვით
- ცარიელი უჯრედების დამუშავება (`drop`, `fill_zero`, ან `fill_mean`)
- მითითებული ფილტრის მონაცენთ შემთხვევაში – მონაცემების გაფილტვრა

#### b) შექმენით სამი სპეციალიზებული პროცესორი `functools.partial()`-ის გამოყენებით (6 ქულა):

1. **`finance_processor`** – ფინანსური ანგარიშებისთვის:
    - სვეტების სახელების სტანდარტიზაცია
    - თარიღის ISO ფორმატში გარდაქმნა
    - რიცხვების 2 ციფრამდე დამრგვალება
    - ცარიელი უჯრედების ნულებით შევსება

2. **`marketing_processor`** – მარკეტინგული მონაცემებისთვის:
    - ალტერნატიული სახელების რუკა
    - რიცხვების მთელ რიცხვებამდე დამრგვალება
    - ცარიელი მნიშვნელობების მოცილება
    - მხოლოდ დადებითი მნიშვნელობების ფილტრაცია

3. **`scientific_processor`** – სამეცნიერო მონაცემებისთვის:
    - რიცხვების 4 ციფრამდე დამრგვალება
    - ცარიელი უჯრედების საშუალო მნიშვნელობით შევსება
    - თარიღის შენახვა timestamp ფორმატში

#### c) დაწერეთ ფუნქცია `process_pipeline` (4 ქულა):

```python
def process_pipeline(data_source, source_type):
    """
    მონაცემთა კონვეიერი, რომელიც სხვადასხვა ტიპის მონაცემებს ამუშავებს
    
    პარამეტრები:
    - data_source: მონაცემთა წყარო (DataFrame)
    - source_type: მონაცემების ტიპი ('finance', 'marketing', 'scientific')
    
    აბრუნებს:
    - დამუშავებულ მონაცემებს
    """
    # დაწერეთ ფუნქციის ლოგიკა, გამოიყენეთ შესაბამისი partial ფუნქცია
```

**ამოცანის შემადგენელი ნაწილები:**
- შემოწმებული მონაცემები (მაგ. CSV ან JSON ფორმატში), რომელიც დატესტავს თქვენს ფუნქციებს.
- მთავარი სკრიპტი, რომელიც კითხულობს მონაცემებს, იყენებს ზემოთქმნილ პროცესორებს და ბეჭდავს საბოლოო შედეგს.
- shell სკრიპტი, რომელიც გაუშვებს მთავარ სკრიპტს (ან Dockerfile, სურვილისამებრ).
- **commands.txt** – ყველა შესრულებული ბრძანების ისტორია.

---

## დამატებითი მითითებები

- დროის უკეთესი მენეჯმენტისთვის შეეცადეთ თეორიულ კითხვებს დაუთმოთ **დაახლოებით 1 საათი**, ხოლო პრაქტიკულ დავალებებს **3 საათი**.
- თუ რაიმე დამატებითი რესურსი დაგჭირდებათ (მაგ. ბიბლიოთეკები, მონაცემთა ფაილები), შეგიძლიათ გამოიყენოთ ნებისმიერ საჯარო წყარო, თუმცა მიუთითეთ წყარო თქვენს README-ში და requirements.txt-ში.
- ეცადეთ, თქვენი კოდი იყოს მაქსიმალურად მკაფიო და დოკუმენტირებული.
- **მნიშვნელოვანია:** რეპოზიტორიის ბმული მიუთითეთ საბოლოო პასუხში.

გისურვებთ წარმატებას!

---

### შეფასების კრიტერიუმები (საერთო 100 ქულა):

1. **თეორია (40 ქულა):**
    - ცნებების სიზუსტე (20 ქულა)
    - მაგალითები და ახსნა (20 ქულა)

2. **პრაქტიკა (60 ქულა):**
    - ამოცანის სისწორე და ფუნქციონალურობა (30 ქულა)
    - კოდის ხარისხი, სტრუქტურა და Docker/commands სისწორე (20 ქულა)
    - README და დოკუმენტაცია (10 ქულა)

გამოცდის განმავლობაში ისარგებლეთ ყველა საჭირო რესურსით, მაგრამ პატივისცემით მოეკიდეთ აკადემიურ პატიოსნებას. წარმატებები!

---

**დრო:** 4 საათი  
**რესურსი:** Open-book  
**რეკომენდებული განაწილება:** ~2 საათი თეორიაზე და ~2 საათი პრაქტიკაზე.  
**სამართავი კითხვები ან პრობლემები:** დაუკავშირდით ზედამხედველს (ინსტრუქტორს).