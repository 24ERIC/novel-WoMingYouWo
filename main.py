from datetime import datetime
import os
import subprocess
from bs4 import BeautifulSoup


def create_new_folder_file_in_database(title):
    global filepath
    global htmlpath
    
    folder_name = datetime.now().strftime("%Y_%-m_%-d_%-H-%-M-%-S")
    folder_path = f"./docs/{folder_name}"

    # Create the folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)

    # get file name
    formatted_time = datetime.now().strftime("%Y_%-m_%-d_%-H-%-M-%-S")
    filepath = f"{folder_path}/{formatted_time}-{title}.md"
    htmlpath = f"{folder_path}/{formatted_time}-{title}.html"
    

    # Create the new file
    with open(filepath, 'w') as file:
        file.write("")
    
    content = """
    <!DOCTYPE html>
    <html>
    <head>
        <!-- Import element definition -->
        <script type="module" src="https://cdn.jsdelivr.net/gh/zerodevx/zero-md@2/dist/zero-md.min.js"></script>
    </head>
    <body>
        <!-- Profit! -->
        <zero-md src=" """ + f"./{formatted_time}-{title}.md" + """ "></zero-md>
    </body>
    </html>
    """

    with open(f"{folder_path}/{formatted_time}-{title}.html", 'w') as file:
        file.write(content)



def extract_title_from_new_article():
    with open("new_article.md", 'r') as file:
        first_line = file.readline().strip()

        if first_line.startswith("title: "):
            title = first_line[len("title: "):]
            return title



def transfer_content_from_new_article_to_database():
    with open("new_article.md", 'r') as file:
        # Read all lines starting from the second line
        lines = file.readlines()[1:]
    


    with open(filepath, 'w') as database_file:
        database_file.writelines(lines)

    reset_new_article()


def reset_new_article():
    with open("new_article.md", 'w') as file:
        file.write("title: \n")
        file.write("# title: ")


def add_code_to_html(html_file_path, code):
    with open(html_file_path, 'r+') as file:
        lines = file.readlines()

        # Find the index of the "<!-- Generate Content below -->" comment
        index = None
        for i, line in enumerate(lines):
            if '<!-- Generate Content below -->' in line:
                index = i
                break

        if index is not None:
            # Insert the code at the specified index
            lines.insert(index + 1, code)

            # Write the modified content back to the file
            file.seek(0)
            file.writelines(lines)
            file.truncate()

        else:
            print('Error: Comment not found in the HTML file.')

def count_characters():
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

        # Count the characters
        character_count = len(content)

    return character_count


def modify_html_number():
    number_to_add = count_characters()

    with open("index.html", 'r', encoding='utf-8') as file:
        content = file.read()

        # Parse the HTML content
        soup = BeautifulSoup(content, 'html.parser')

        # Find the span element with the id "number_of_char"
        span_element = soup.find('span', id='number_of_char')

        # Get the current number
        current_number = int(span_element.string)

        # Calculate the new number
        new_number = current_number + number_to_add

        # Update the number
        span_element.string = str(new_number)

    # Write the modified HTML back to the file
    with open("index.html", 'w', encoding='utf-8') as file:
        file.write(str(soup))





if __name__ == '__main__':
    # get file title
    title = extract_title_from_new_article()

    # create new page
    create_new_folder_file_in_database(title)

    # move content
    transfer_content_from_new_article_to_database()

    # modify html
    add_code_to_html('./index.html',
    """
            <div class="posts-line">
            <div class="posts-title">
                <time class="posts-date" datetime="">
            """ + "    " + datetime.now().strftime("%Y-%m-%d") + """
                </time>
                <a href=\"""" + htmlpath + """\">""" + title + """</a>
            </div>
            </div>
            
    """)
    
    modify_html_number()

    subprocess.run(['git', 'add', '*'])
    subprocess.run(['git', 'commit', '-m', 'update-new-post'])
    subprocess.run(['git', 'push'])