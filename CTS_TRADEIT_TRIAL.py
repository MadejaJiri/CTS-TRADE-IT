import bs4 as bs
import urllib.request
import base64
from slugify import slugify

def main():
    job_positions = get_job_positions()
    jobs = []
    for position in job_positions:
        jobs.append(get_position_info(position))
    print(jobs)    
    for job in jobs:
        save_position_to_file(job)
    

def get_job_positions(url="https://www.cts-tradeit.cz/kariera/"):
    """
    Gets all job positions.
    Returns list of job positions sub-urls
    """
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source,'lxml')
    positions = []
    for url in soup.find_all('a'):
        if url.get("href").startswith("/kariera/") and url.get("href") != "/kariera/":
            positions.append(url.get('href'))
    return positions
    
def get_position_info(position_name):
    """
    Gets info about job position.
    Returns tuple of name and description of the job position
    """
    url = "https://www.cts-tradeit.cz" + position_name
    print(url)
    name = ""
    description = ""
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source,'lxml')
    
    name = soup.find(class_='mb-1').text
    
    description = soup.find(class_='story__text').text
    description = description.split("\n")[1]

    return (name, description)

def save_position_to_file(position):
    position_name = "-".join(position[0].split("\\"))
    position_name_clean = slugify(position_name)  # position name
    print(position_name)
    file_content = position[1]  # position description
    print(file_content)
    
    with open(position_name_clean + ".txt", "w") as f: 
        f.write(file_content) 

if __name__ == "__main__":
    main()
