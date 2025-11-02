# Instagram A İ O

Instagram A İ O is a Python script that allows you to perform bulk operations on Instagram profiles and posts. It supports fetching Reels links, scraping profile data, downloading videos from posts, and downloading profile pictures. The script uses Instaloader for Instagram data retrieval, requests for downloading content, and colorama for colored terminal output.

## Features

-*Fetch Reels Links (Bulk):
Extract Reels links from multiple Instagram profiles and save them to text files. Supports retries and error handling.

-Scrape Profile Data (Bulk):
Collect detailed profile information (username, full name, biography, followers, following, post count, profile picture URL, verification status) for multiple Instagram accounts and save it to text files.

-Download Videos from Links (Bulk):
Download videos from a list of Instagram post URLs with logs for each download.

-Download Profile Pictures (Bulk):
Download profile pictures for multiple Instagram profiles.

-Optional Login Support:
Log in to Instagram to access private profiles and improve reliability when fetching data.

-Retry Mechanism:
Automatically retries failed requests to reduce errors caused by temporary network or Instagram restrictions.

-Colored Terminal Output:
Uses colorama and ANSI codes for a visually appealing menu and status messages.

## Requirements

The following Python libraries are required:

- `instaloader`
 – Download Instagram photos, videos, and metadata.

- `requests`
 – Perform HTTP requests to download media.

- `colorama`
 – Colorize terminal output.

You can install these dependencies using pip:

pip install instaloader requests colorama

## Usage

Run the script:

```bash 
python instagram_aio.py
```

Optional login:
Enter your Instagram username and password to access private profiles. Press Enter to skip login.

Select a task from the menu:

[1] Fetch Reels Links (Bulk)

[2] Scrape Profile Data (Bulk)

[3] Download Videos from Links (Bulk)

[4] Download Profile Pictures (Bulk)

[5] Exit

Enter the required input (usernames or post URLs, comma-separated).

Results are saved as .txt or .mp4/.jpg files in the same directory.

## Notes

Logging in improves reliability but is optional.

Reels and post downloads only work for public or accessible profiles.

The script automatically retries failed requests to reduce errors.

Colored terminal output is supported in Windows, Linux, and macOS.
