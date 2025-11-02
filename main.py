import instaloader
import requests
import os
import time
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# ------------------- ANSI Colors -------------------
RED = "\033[91m"
WHITE = "\033[97m"
RESET = "\033[0m"

# ------------------- Terminal Utilities -------------------
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print(RED + r"""
███████╗██████╗ ███╗   ██╗  ██╗ █████╗ ██████╗  █████╗ 
╚══███╔╝╚════██╗████╗  ██║ ███║██╔══██╗╚════██╗██╔══██╗
  ███╔╝  █████╔╝██╔██╗ ██║ ╚██║╚██████║ █████╔╝╚█████╔╝
 ███╔╝   ╚═══██╗██║╚██╗██║  ██║ ╚═══██║ ╚═══██╗██╔══██╗
███████╗██████╔╝██║ ╚████║  ██║ █████╔╝██████╔╝╚█████╔╝
╚══════╝╚═════╝ ╚═╝  ╚═══╝  ╚═╝ ╚════╝ ╚═════╝  ╚════╝ 
""" + RESET)

def menu():
    print("> INSTAGRAM A İ O")
    print(WHITE + "> Version [v1.0]")
    print("> https://github.com/z3n1938")
    print(RED + "="*60 + RESET)
    print(f"{RED}[{WHITE}1{RED}]{WHITE} Fetch Reels Links (Bulk)")
    print(f"{RED}[{WHITE}2{RED}]{WHITE} Scrape Profile Data (Bulk)")
    print(f"{RED}[{WHITE}3{RED}]{WHITE} Download Videos from Links (Bulk)")
    print(f"{RED}[{WHITE}4{RED}]{WHITE} Download Profile Pictures (Bulk)")
    print(f"{RED}[{WHITE}5{RED}]{WHITE} EXIT")
    print(RED + "="*60 + RESET)
    choice = input(WHITE + "Choice?: " + RESET)
    return choice

# ------------------- Global Instaloader -------------------
L = instaloader.Instaloader()

def login_instagram():
    print(WHITE + "Login (optional, improves access to profiles):" + RESET)
    username = input("Username (or Enter to skip login): ").strip()
    if username:
        password = input("Password: ").strip()
        try:
            L.login(username, password)
            print(Fore.GREEN + "Logged in successfully!" + RESET)
        except Exception as e:
            print(Fore.RED + f"Login failed: {e}" + RESET)

# ------------------- Safe profile fetch with retries -------------------
def safe_fetch_profile(username, retries=3):
    for attempt in range(retries):
        try:
            profile = instaloader.Profile.from_username(L.context, username)
            return profile
        except Exception as e:
            print(Fore.RED + f"Attempt {attempt+1} failed for {username}: {e}")
            time.sleep(2)
    print(Fore.YELLOW + f"Failed to fetch {username} after {retries} attempts." + RESET)
    return None

# ------------------- Instagram Functions -------------------
def fetch_reels_links_bulk(usernames):
    for username in usernames:
        profile = safe_fetch_profile(username)
        if not profile:
            continue

        reels_links = [post.url for post in profile.get_posts() if post.typename == 'GraphVideo']

        if reels_links:
            filename = f"{username}_reels_links.txt"
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(f"Reels Links for @{username}:\n")
                for link in reels_links:
                    file.write(f"{link}\n")
            print(Fore.MAGENTA + f"Reels links saved to {filename}")
        else:
            print(Fore.YELLOW + f"No reels found for @{username}.")

def scrape_profile_data_bulk(usernames):
    for username in usernames:
        profile = safe_fetch_profile(username)
        if not profile:
            continue

        profile_data = {
            'Username': profile.username,
            'Full Name': profile.full_name,
            'Bio': profile.biography,
            'Followers': profile.followers,
            'Following': profile.followees,
            'Posts': profile.mediacount,
            'Is Verified': profile.is_verified,
            'Profile Picture URL': profile.profile_pic_url,
        }

        filename = f"{username}_profile_data.txt"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f"Profile Data for @{username}:\n")
            for key, value in profile_data.items():
                file.write(f"{key}: {value}\n")
        print(Fore.CYAN + f"Profile data saved to {filename}")

def download_videos_bulk(post_urls):
    for post_url in post_urls:
        shortcode = post_url.split("/")[-2]
        try:
            post = instaloader.Post.from_shortcode(L.context, shortcode)
            video_url = post.url
            video_data = requests.get(video_url)

            filename = f"{shortcode}.mp4"
            with open(filename, 'wb') as file:
                file.write(video_data.content)

            log_msg = f"Video {shortcode} downloaded as {filename}"
            with open(f"{shortcode}_download_log.txt", 'w', encoding='utf-8') as log_file:
                log_file.write(log_msg)

            print(Fore.GREEN + log_msg)
        except Exception as e:
            print(Fore.RED + f"Error downloading {post_url}: {e}")

def download_profile_pictures_bulk(usernames):
    for username in usernames:
        profile = safe_fetch_profile(username)
        if not profile:
            continue

        try:
            profile_pic_url = profile.profile_pic_url
            profile_pic_data = requests.get(profile_pic_url)

            filename = f"{username}_profile_pic.jpg"
            with open(filename, 'wb') as file:
                file.write(profile_pic_data.content)

            print(Fore.YELLOW + f"Profile picture of {username} saved as {filename}")
        except Exception as e:
            print(Fore.RED + f"Error downloading profile pic for {username}: {e}")

# ------------------- Main Loop -------------------
def main():
    login_instagram()
    while True:
        clear()
        banner()
        choice = menu()

        if choice == "1":
            usernames = input(WHITE + "Enter Instagram usernames (comma separated): " + RESET).split(",")
            usernames = [u.strip() for u in usernames]
            fetch_reels_links_bulk(usernames)
        elif choice == "2":
            usernames = input(WHITE + "Enter Instagram usernames (comma separated): " + RESET).split(",")
            usernames = [u.strip() for u in usernames]
            scrape_profile_data_bulk(usernames)
        elif choice == "3":
            post_urls = input(WHITE + "Enter Instagram post URLs (comma separated): " + RESET).split(",")
            post_urls = [u.strip() for u in post_urls]
            download_videos_bulk(post_urls)
        elif choice == "4":
            usernames = input(WHITE + "Enter Instagram usernames (comma separated): " + RESET).split(",")
            usernames = [u.strip() for u in usernames]
            download_profile_pictures_bulk(usernames)
        elif choice == "5" or choice.lower() == "exit":
            print(RED + "Exiting... Goodbye!" + RESET)
            break
        else:
            print(RED + "Invalid choice!" + RESET)
        input(RED + "Press Enter to return to menu..." + RESET)

if __name__ == "__main__":
    main()
