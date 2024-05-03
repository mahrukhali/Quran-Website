from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from flask import Flask, redirect, url_for, request, render_template,g,session
app = Flask(__name__)

app.secret_key = 'mahrukh'
data = [
    {
        "id": "1",
        "img":"/static/images/para1.png",
        "separa": "Alif Lam Meem",
        "verses": "https://quran.com/en/an-nasr/1-3",
        "video": "https://www.youtube.com/watch?v=XcFS3SIA4hI",
        "ayahs": "7",
        "summary": "The first verse invokes the name of the one God/Allah (in Arabic, “b-ismi-llah”), in whose name Muslims pray and do all things. This is the most widely spoken phrase among Muslims, said before meals and all important undertakings.One of God’s most important characteristics is that he is compassionate and merciful. He will forgive all who repent and submit to his will.",
        "surahs": ["Al-Fatiha Verse 1", "Al-Baqarah Verse 141"]
    },
    {
        "id": "2",
         "img":"/static/images/para2.png",
        "separa": "Sayaqool",
        "verses": "https://www.clearquran.com/002.html",
        "video": "https://www.youtube.com/watch?v=V8DoOh9P9xE",
        "ayahs": "286",
        "summary": "Chapter 2 is the first of 29 chapters that begin with a combination of Arabic letters. These combinations are formed from fourteen letters and chapter two begins with alif, lam and meem. God did not reveal a specific meaning attached to any of these combinations although over the course of Islamic scholarship theories have been suggested. This is the book, a guide for those who are God conscious. In the opening chapter God taught us how to ask for guidance and in the second chapter He presents us with a book of guidance.",
        "surahs": ["Al-Baqarah Verse 142"]
    },
    {
        "id": "3",
        "img":"/static/images/para3.png",
        "separa": "Tilkal Rusul",
        "verses": "https://www.clearquran.com/003.html",
        "video": "https://www.youtube.com/watch?v=QIxmilsyEhk",
        "ayahs": "200",
        "summary": "God warns the believers not to seek protection from the unbelievers except for safety from tyranny. Remember that God knows everything concealed or revealed, He has power over everything. Fear retribution but know that He is compassionate to those who are devoted to Him.",
        "surahs": ["Al-Baqarah Verse 253", "Al-Imran Verse 92"]
    },
    {
        "id": "4",
        "img":"/static/images/para4.png",
        "separa": "Lan Tana Loo",
        "verses": "https://www.clearquran.com/004.html",
        "video": "https://www.youtube.com/watch?v=V8DoOh9P9xE",
        "ayahs": "176",
        "summary": "The theme of Chapter 4 seems to be about socio-economics, with an emphasis on following the messenger to attain these goals. Establishing justice is also emphasized, and is another prevalent theme of the chapter.Ch 4 has its first section (4/1-18) address mankind to establish a just and organic society in terms of dependency. This happens when we take care of those who are alone with no one to care for them (al-yateem).",
        "surahs": ["Al-Imran Verse 93", "An-Nisa Verse 23"]
    },
    {
        "id": "5",
        "img":"/static/images/para5.png",
        "separa": "Wal Mohsanat",
        "verses": "https://www.clearquran.com/004.html",
        "video": "https://www.youtube.com/watch?v=w4uUvBMrVjc",
        "ayahs": "120",
        "summary": "The chapter relates to food, and a central theme is the regulation of lawful and unlawful food, obedience to which is considered as part of the pledge between God and the believers. It also talks about hunting for food during the pilgrimage. God had also taken pledges from the Jews and Christians and the chapter deals with what they did to their pledges. Some passages deal with the afterlife and the verdict of the messengers on the behavior of their communities.",
        "surahs": ["An-Nisa Verse 24"]
    },
    {
        "id": "6",
        "img":"/static/images/para6.png",
        "separa": "La Yuhibbullah",
        "verses": "https://www.clearquran.com/005.html",
        "video": "https://www.youtube.com/watch?v=jOfjatghBoI",
        "ayahs": "165",
        "summary": "Chapter six of the Quran is called The Cattle; some translations use the more encompassing word livestock. The title comes from the discussion about livestock in verses 136- 39. This chapter of 165 verses was revealed in Mecca. In a similar way to other chapters revealed in Mecca we find the emphasis on monotheism or the Oneness of God.",
        "surahs": ["An-Nisa Verse 148", "Al-Ma'idah Verse 81"]
    },
    {
        "id": "7",
        "img":"/static/images/para7.png",
        "separa": "Wa Iza Samiu",
        "verses": "https://www.clearquran.com/006.html",
        "video": "https://www.youtube.com/watch?v=lu7Qyad1M9I",
        "ayahs": "206",
        "summary": "Surah Araf is the 7th chapter of the Quran with 206 verses. It was revealed in Mecca and is the longest Makki surah. Surah Araf talks of the covenant between God and mankind in which all human beings stood as witness to the oneness of God, his Lordship and the Hereafter. The recitation of surah Araf will bring about more sustenance and create a barrier against Satan on the Last Day.",
        "surahs": ["Al-Ma'idah Verse 82", "Al-An'am Verse 110"]
    },
    {
        "id": "8",
        "img":"/static/images/para8.png",
        "separa": "Wa Lau Annana",
        "verses": "https://www.clearquran.com/007.html",
        "video": "https://www.youtube.com/watch?v=eTcU3Zf0sY8",
        "ayahs": "75",
        "summary": "Surah Anfal also called Surah Badr is the 8th chapter of the Quran which discusses the first battle between the Muslims and the polytheists of Mecca in the 2nd year after Hijra. There are beautiful points to be understood and acted upon. It teaches that one needs to prefer the command of God and His messenger over one’s own personal interest. After all, even one’s own interest lies in the acceptance of the divine rulings.",
        "surahs": ["Al-An'am Verse 111", "Al-A'raf Verse 87"]
    },
    {
        "id": "9",
         "img":"/static/images/para9.png",
        "separa": "Qalal Malao",
        "verses": "https://www.clearquran.com/008.html",
        "video": "https://www.youtube.com/watch?v=Q1vMm80sAnk",
        "ayahs": "129",
        "summary": "It discusses the qualities of the true believers, how to divide the war spoils, the migration to Madinah, and how should Muslims deal with the disbelievers at war. Surah Al-Anfal talks about the rules and regulations of dividing the war spoils, in addition to the attributes of a true believer. Also, the surah cleared any misunderstanding regarding the battle of Badr.",
        "surahs": ["Al-A'raf Verse 88", "Al-Anfal Verse 40"]
    },
    {
        "id": "10",
         "img":"/static/images/para10.png",
        "separa": "Wa A'lamu",
        "verses": "https://www.clearquran.com/009.html",
        "video": "https://www.youtube.com/watch?v=KWvLj5y46sA",
        "ayahs": "109",
        "summary": "This chapter makes a brief reference to the Prophet Jonah (v. 98), which gives it its title, to indicate that as the people of Jonah benefited by his warning, so would the Arabs ultimately believe in the Prophet Muhammad. While this chapter asserts the truth of revelation, it also lays stress on the merciful dealing of God with mankind. It tells us that He does not send punishment quickly and that evidence of His mercy is also found in nature.",
        "surahs": ["Al-Anfal Verse 41", "At-Tauba Verse 92"]
    }
]


@app.route('/')
def Quran():
   return render_template('welcome.html')

@app.route('/view/<int:item_id>')
def view_item(item_id):
    # Find the item with the given ID from your data
    item = next((item for item in data if item['id'] == str(item_id)), None)
    
    if item:
        session['my_variable'] = item
        search_text = request.args.get('searchText', '')
        # Calculate the length of the search text
        search_text_length = len(search_text)
        return render_template('view_item.html', item=item, search_text=search_text, search_text_length=search_text_length)
    else:
        return 'Item not found', 404  # Return a 404 error if the item is not found

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        # Search logic
       
        search_term = request.form.get('searchTerm', '').strip()
        search_text_length = len(search_term)
        print("Search term:", search_term)
        if not search_term:
        
            if request.path == '/':
                    return redirect(url_for('Quran'))  

        
            elif request.path == 'submit':
                    print("come here")
                    return render_template('submit.html') 
                  
            else:
                    print('else')
                    return redirect(url_for('view_item', item_id=session['my_variable']['id']))
                  
                    
                
        
        
       
        search_words = search_term.lower().split()
        
        # Perform search through the data
        search_results = []
        for item in data:

                values_str = ' '.join(str(value).lower() for value in item.values())
                if all(word in values_str for word in search_words):
                    search_results.append(item)
        # search_results = []
        # for item in data:
        #     if search_term.lower() in item['separa'].lower():
        #         search_results.append(item)
        
        print("Search results:\n", search_results)
        print("blank")
        
        if search_results:
            print("Entered 2")
            print(search_results)
            return render_template('submit.html', search_results=search_results, search_text=search_term,search_text_length=search_text_length)
        else:
            print("Entered 3")
            return render_template('submit.html', search_results=[], search_text=search_term, no_results=True)
    else:
        # If it's a GET request, render the template with data
        print("Entered 4")
        return render_template('submit.html')



# @app.route('/add', methods=['GET', 'POST'])
# def add_item():
#     errors = {}  # Initialize errors dictionary
#     success_message = None
#     new_item_id = None
    
#     if request.method == 'POST':
#         # Get form data
#         separa = request.form.get('separa').strip()
#         ayahs = request.form.get('ayahs').strip()
#         surahs = [surah.strip() for surah in request.form.get('surahs').split(',')]
#         verses = request.form.get('verses').strip()
#         video = request.form.get('video').strip()
#         summary= request.form.get('summary').strip()

#         # Perform error detection
#         if not separa:
#             errors['separa'] = 'Separa is required.'
#         if not ayahs:
#             errors['ayahs'] = 'Ayahs is required.'
#         print(len(surahs))
#         print(surahs)
#         print("Entered the add route")
#         if surahs[0] == '':
#             errors['surahs'] = 'At least one surah is required.'
#         if not verses:
#             errors['verses'] = 'Please provide link.'
#         if not video:
#             errors['video'] = 'Please provide link.'
#         if not summary:
#             errors['summary'] = 'Summary is required.'
#         elif separa.isdigit():
#             errors['separa'] = 'Separa can not be a number'
#         elif not ayahs.isdigit():
#             errors['ayahs'] = 'Ayahs must be a number.'
      
#         elif verses.isdigit():
#             errors['verses'] = 'Verses can not be a number.'
#         elif video.isdigit():
#             errors['video'] = 'Video can not be a number.'
#         elif summary.isdigit():
#             errors['summary'] = 'Summary can not be a number.'
        


#         if errors:
#             return render_template('add_item.html', errors=errors)

#         # Generate a unique ID for the new item (e.g., by counting existing items)
#         new_id = str(len(data) + 1)
        
#         # If input is valid, add the new entry to the database with the generated ID
#         new_item = {
#             'id': new_id,
#             'separa': separa,
#             'ayahs': int(ayahs),
#             'surahs': surahs,
#             'verses': verses,
#             'video': video,
#             'summary': summary
#             # Add other fields as needed
#         }
#         data.append(new_item)
#         new_item_id = new_id
#         success_message = 'Data added successfully. t'
     

#     # If it's a GET request or if there are errors, render the form
#     return render_template('add_item.html', errors=errors, success_message=success_message, new_item_id=new_item_id)


from uuid import uuid4

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        request_data = request.json
        
        # Validate the data if necessary
        if not all(key in request_data for key in ['img','separa', 'ayahs', 'surahs','summary', 'verses', 'video']):
            return jsonify({"error": "Missing required fields"}), 400
        
        # Extract item details from the request data
        img = request_data['img']
        separa = request_data['separa']
        ayahs = request_data['ayahs']
        # surahs=request_data['surahs']
        summary = request_data['summary']
        verses = request_data['verses']
        video = request_data['video']
        surahs = request_data.get('surahs', [])
        if isinstance(surahs, str):
            # If surahs is a string, split it by comma to create a list
            surahs = [surah.strip() for surah in surahs.split(',')]
        
        
        max_id = max((int(item['id']) for item in data), default=0)
        
        # Generate the next ID
        new_item_id = str(max_id + 1)
        
        # Append the new item to your existing data
        new_item = {
            'id': new_item_id,
            'img':img,
            'surahs':surahs,
            'separa': separa,
            'ayahs': ayahs,
            'summary': summary,
            'verses': verses,
            'video': video
        }
        data.append(new_item)
        
        # Return a response indicating success
        return jsonify({"message": "New item added successfully", "id": new_item_id}), 200
        
    elif request.method == 'GET':
        # If it's a GET request, render the add_item form
        return render_template('add_item.html')

@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    # Find the item with the given ID from your data
    item = next((item for item in data if item['id'] == str(item_id)), None)

    errors = {}  # Empty dictionary for errors

    if request.method == 'POST':
        # Update the item with the new data
        item['img'] = request.form['img']
        item['separa'] = request.form['separa']
        item['ayahs'] = int(request.form['ayahs'])
        item['summary'] = request.form['summary']
        item['verses'] = request.form['verses']
        item['video'] = request.form['video']
        # Update surahs by splitting the input string into a list
        
        item['surahs'] = [surah.strip() for surah in request.form['surahs'].split(',')]
        # Update other fields as needed

        # Redirect to the view page for the updated item
        return redirect(url_for('view_item', item_id=item_id))

    # Render the edit form with pre-filled data
    return render_template('edit_item.html', item=item, errors=errors)


if __name__ == '__main__':
    app.run(debug=True)