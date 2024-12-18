# **Twitch Highlight Downloader Automation**

This repository contains a Python script that automates the process of fetching and downloading highlights from your Twitch channel created within the last 48 hours. It leverages the **Twitch API** to retrieve video details and uses the **TwitchDownloaderCLI** to download the videos locally.

---

## **Features**

- **Automated Retrieval of Highlights**:  
  Fetches highlights from the Twitch API for your channel, filtering by a specified time range (default: last 48 hours).

- **Video Downloads Using TwitchDownloaderCLI**:  
  Automatically downloads highlights using the TwitchDownloaderCLI tool.

- **Secure Credential Handling**:  
  - Sensitive data, such as the Twitch Client ID and OAuth token, is stored in a `.env` file.
  - The `.env` file is ignored in version control using `.gitignore`.

- **Custom Output Directory**:  
  Saves downloaded highlights to a folder named `twitch_highlights`, which is created automatically if it doesn’t already exist.

---

## **Prerequisites**

### **Tools and Libraries**
1. **TwitchDownloaderCLI**:  
   - Download and install from the [official repository](https://github.com/lay295/TwitchDownloader).
   - Ensure it is added to your system's PATH.

2. **Python 3.7+**:  
   - Install Python and the required libraries:
     ```bash
     pip install requests python-dotenv
     ```

3. **Twitch API Credentials**:  
   - Create an application in the [Twitch Developer Console](https://dev.twitch.tv/console).
   - Generate a **Client ID** and **OAuth token**.

---

## **Installation and Setup**

### **Clone the Repository**
```bash
git clone https://github.com/your-username/twitch-highlight-downloader.git
cd twitch-highlight-downloader
```

### **Set Up Environment Variables**
1. Create a `.env` file in the root directory:
   ```bash
   touch .env
   ```

2. Add the following lines to `.env`:
   ```env
   TWITCH_CLIENT_ID=your_client_id
   TWITCH_OAUTH_TOKEN=your_oauth_token
   ```

3. Ensure `.env` is ignored by Git:
   ```bash
   echo ".env" >> .gitignore
   ```

---

## **Usage**

### **Running the Script**
1. **Ensure `TwitchDownloaderCLI` is installed and configured.**
2. Execute the script:
   ```bash
   python download_highlights.py
   ```

### **Output**
- The script will:
  - Retrieve all highlights created within the last 48 hours.
  - Download each highlight as an `.mp4` file to the `twitch_highlights` folder.

---

## **Considerations**

1. **Rate Limits**:  
   The Twitch API enforces rate limits. If you're fetching highlights for a large user base or repeatedly testing, ensure you stay within the [Twitch API limits](https://dev.twitch.tv/docs/rate-limits).

2. **Time Range**:  
   The script is configured to retrieve highlights from the last 48 hours. Modify the `TWO_DAYS_AGO` variable in the script if you need a different range.

3. **Error Handling**:  
   Basic error handling is included to manage HTTP errors from the Twitch API. Improve this logic for production use.

4. **Platform Compatibility**:  
   The script assumes a Unix-based shell environment (macOS/Linux). Windows users should ensure `subprocess.run` is compatible with their system's CLI setup.

5. **Dependencies**:  
   Ensure Python 3.7+ and required libraries (`requests`, `python-dotenv`) are installed.

---

## **Example Workflow**

1. A Twitch user has created highlights over the past 48 hours.
2. This script:
   - Retrieves the highlights from the Twitch API.
   - Uses `TwitchDownloaderCLI` to save the highlights as `.mp4` files.
3. The final `.mp4` files are stored in the `twitch_highlights` directory, ready for use.

---

## **Contribution**

Feel free to open issues or submit pull requests to improve the script. Suggestions for enhanced error handling, extended functionality, or additional CLI integrations are welcome!

---

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for details.