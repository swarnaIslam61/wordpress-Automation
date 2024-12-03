# WordPress Automation Script

This project is an automation script for WordPress using Python and Selenium. It automates various tasks in the WordPress admin panel, including login, plugin management, and configuration of the WP Dark Mode plugin.

## Features

- Automated login to WordPress admin panel
- Installation and activation of the WP Dark Mode plugin
- Configuration of WP Dark Mode settings
- Enabling and customizing site animations

## Prerequisites

Before running this script, ensure you have the following installed:

- Python 3.x
- Chrome WebDriver
- Selenium
- python-dotenv

## Installation

1. Clone this repository:

  git clone https://github.com/yourusername/wordpress-automation.git
   cd wordpress-automation


2. Install the required Python packages:
  pip install selenium python-dotenv
  3. Download and install the Chrome WebDriver that matches your Chrome browser version.
  
  4. Create a `.env` file in the project root and add your WordPress credentials:
    usr=your_wordpress_username
   password=your_wordpress_password
   ## Usage
   
   To run the automation script:

   python main.py

The script will perform the following actions:

1. Log in to the WordPress admin panel
2. Navigate to the Plugins section
3. Install and activate the WP Dark Mode plugin if not already installed
4. Configure WP Dark Mode settings
5. Enable and customize site animations

## Configuration

You can modify the script to customize the automation tasks. The main areas you might want to adjust are:

- The WordPress site URL in the `driver.get()` method
- The specific settings for WP Dark Mode
- The site animation configurations

## Troubleshooting

If you encounter any issues:

1. Ensure your `.env` file contains the correct WordPress credentials
2. Check that the Chrome WebDriver version matches your Chrome browser version
3. Verify that all required Python packages are installed
4. Increase the wait times if the script is failing due to elements not loading quickly enough

## Contributing

Contributions to improve the script or add new features are welcome. Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.