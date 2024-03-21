import speech_recognition as sr
import pyaudio
from web_command import google_search, youtube_search, youtube_main_page, reddit_search, reddit_main_page
from add_file import create_pptx_file, create_xlsx_file, create_txt_file, create_doc_file

r = sr.Recognizer()
r.pause_threshold = 0.5



def listen_command():
    try:
        with sr.Microphone() as mic:
            r.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = r.listen(source=mic)
            query = r.recognize_google(audio_data=audio, language='ru-RU').lower()
        print(query)
        return query

        
    except sr.UnknownValueError:
        return 'Я не понял, что ты сказал'
    except sr.WaitTimeoutError:
        return ''


def process_user_request(request):

    doc = nlp(request)
    
    keywords = []
    for token in doc:
        if token.pos_ == "NOUN":
            keywords.append(token.lemma_)
    


def main():
    while True:
        query = listen_command()


        google_words = ('искать', 'гугл', 'найди', 'найти', 'search', 'google', 'find', 'найди')
        youtube_search_words = ('search video', 'search in youtube', ' искать видео', 'искать в ютуб','видео','youtube','ютуб','video')
        reddit_words = ('reddit', 'редит', 'реддит', 'сабредит', 'сабреддит', 'subreddit', 'subredit')
        reddit_search_words = ('search subreddit', 'search subredit', 'search in reddit', 'search in redit',
                               ' искать сабреддит', ' искать сабредит', 'искать в реддит', 'искать в reddit')
        create_file = ('create file','создать файл','create document','создать документ','саздать файл')

        if any(element in query for element in google_words):
            print('Что вы хотите найти?')
            google_search(listen_command())
            continue
        elif any(element in query for element in youtube_search_words):
            print('Что вы хотите найти?')
            youtube_search(listen_command())
            continue
        elif any(element in query for element in reddit_search_words):
            print( 'Какую тему ходите обсудить?' )
            reddit_search(listen_command())
            continue
        elif any(element in query for element in create_file):
            print('какой файл создать?')
            query = listen_command()

            if query == "презентация":
                create_pptx_file()
            elif query == "таблица":
                create_xlsx_file()
            elif query == "txt" or "тииксти" or "тиксти":
                create_txt_file()
            elif query == "docx" or "doc":
                create_doc_file()
            else:
                print("Неизвестный тип файла. Повторите ввод.")
            continue

        else:
            print( 'Я не понял команды, повторите пожалуйста' )


main()
