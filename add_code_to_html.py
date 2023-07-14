from datetime import datetime
import os

def create_new_folder_file_in_database(title):
    global filepath
    
    folder_name = datetime.now().strftime("%Y_%-m_%-d_%-H-%-M-%-S")
    folder_path = f"./docs/{folder_name}"

    # Create the folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)

    # get file name
    formatted_time = datetime.now().strftime("%Y_%-m_%-d_%-H-%-M-%-S")
    filepath = f"{folder_path}/{formatted_time}-{title}.md"

    # Create the new file
    with open(filepath, 'w') as file:
        file.write("")


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
        file.write("title: ")


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


title = extract_title_from_new_article()

create_new_folder_file_in_database(title)

transfer_content_from_new_article_to_database()


add_code_to_html('./index.html',
"""
        <div class="posts-line">
          <div class="posts-title">
            <time class="posts-date" datetime="">
          """ + "    " + datetime.now().strftime("%Y-%m-%d") + """
            </time>
            <a href=" """ + filepath + """
            ">""" + title + """</a>
          </div>
        </div>
        
""")
# import subprocess

# # Perform git commands
# subprocess.run(['git', 'add', '*'])
# subprocess.run(['git', 'commit', '-m', 'update'])
# subprocess.run(['git', 'push'])