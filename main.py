from playwright.sync_api import sync_playwright
import time
import os
import random
import datetime
import pytz
from PIL import Image, ImageDraw

def is_within_posting_window():
    central_tz = pytz.timezone('US/Central')
    current_time = datetime.datetime.now(tz=central_tz)
    
    start_time = current_time.replace(hour=19, minute=0, second=0, microsecond=0)
    end_time = current_time.replace(hour=19, minute=10, second=0, microsecond=0)
    
    return start_time <= current_time <= end_time

def remove_element_by_selector(page, selector):
    page.evaluate('(selector) => { document.querySelector(selector).remove(); }', selector)
    
def take_screenshot():
    with sync_playwright() as p:
        
        browser = p.chromium.launch(headless=False, args=["--start-maximized"], channel='msedge')
        page = browser.new_page(java_script_enabled=False,no_viewport=True)
        page.goto("https://fnbr.co/shop", timeout=15000)

        elements = page.query_selector_all('.items-row.shop-items.slosh-mode')
        
        element_selector = "h2.shop-section-title[data-language-tag='shop.title-featured2']"
        element = page.query_selector(element_selector)

        if element:
            # Use the innerText property to change the text content
            new_text = "Creator Code | hipdiscovery "
            page.evaluate(f'element => element.innerText = "{new_text}"', element)
        
        element_selector = "h2.shop-section-title[data-language-tag='shop.title-featured2']"
        element = page.query_selector(element_selector)

        if element:
        # Get the bounding box of the element
            bounding_box = element.bounding_box()

            # Add padding around the element
            padding_left = 10
            padding_right = 10
            padding_top = 10
            padding_bottom = 10

            # Adjust the bounding box to include padding
            bounding_box['x'] -= padding_left
            bounding_box['y'] -= padding_top
            bounding_box['width'] += padding_left + padding_right
            bounding_box['height'] += padding_top + padding_bottom

            # Take a screenshot with the adjusted bounding box
            screenshot_filename = 'shop/1.png'
            page.screenshot(path=screenshot_filename, clip=bounding_box)
            
        # Get today's date
        today = datetime.date.today()

        # Get the day of the week (full name)
        day_name = today.strftime("%A")

        # Get the month (full name)
        month_number = today.strftime("%m")

        # Get the year
        year = today.strftime("%Y")

        # Print the formatted date
        formatted_date = f"{day_name}-{month_number}-{year}"
        
        element_selector = "h2.shop-section-title[data-language-tag='shop.title-featured2']"
        element = page.query_selector(element_selector)

        if element:
            # Use the innerText property to change the text content
            new_text = formatted_date
            page.evaluate(f'element => element.innerText = "ITEM SHOP {new_text}"', element)
        
        element_selector = "h2.shop-section-title[data-language-tag='shop.title-featured2']"
        element = page.query_selector(element_selector)

        if element:
        # Get the bounding box of the element
            bounding_box = element.bounding_box()

            # Add padding around the element
            padding_left = 10
            padding_right = 10
            padding_top = 10
            padding_bottom = 10

            # Adjust the bounding box to include padding
            bounding_box['x'] -= padding_left
            bounding_box['y'] -= padding_top
            bounding_box['width'] += padding_left + padding_right
            bounding_box['height'] += padding_top + padding_bottom

            # Take a screenshot with the adjusted bounding box
            screenshot_filename = 'shop/2.png'
            page.screenshot(path=screenshot_filename, clip=bounding_box)
        
        if element:
            # Use the innerText property to change the text content
            new_text = "Featured Items"
            page.evaluate(f'element => element.innerText = "{new_text}"', element)
        
        element_selector = "h2.shop-section-title[data-language-tag='shop.title-featured2']"
        element = page.query_selector(element_selector)
        
        remove_element_by_selector(page, '.passive-container')
        remove_element_by_selector(page, ".alert.alert-shop")
        remove_element_by_selector(page, ".otd-container")  
        remove_element_by_selector(page, '.shop-title') 
        remove_element_by_selector(page, '.shop-vote-container.live') 
        remove_element_by_selector(page, '.nav-container.container')
        remove_element_by_selector(page, '.col-wide')
        page.evaluate('''(selector) => {
        const element = document.querySelector(selector);
        if (element) {
            element.remove();
        }
    }''', 'p[data-language-tag="shop.line2"]')
        page.evaluate('''(selector) => {
        const element = document.querySelector(selector);
        if (element) {
            element.remove();
        }
    }''', 'p[data-language-tag="shop.line1"]')
        page.evaluate('''(selector) => {
        const element = document.querySelector(selector);
        if (element) {
            element.remove();
        }
    }''', 'p[data-language-tag="shop.line3"]')
        page.evaluate('''(selector) => {
        const element = document.querySelector(selector);
        if (element) {
            element.remove();
        }
    }''', 'h2.shop-section-title[data-language-tag="shop.title-featured"]')
        
        time.sleep(2)  
        
        page.evaluate('''() => {
        const elements = document.querySelectorAll("h3");
        for (const element of elements) {
            if (element.textContent.includes("Previous Item Shop On This Day...")) {
                element.remove();
                break;
            }
        }
    }''')
        
        element = page.query_selector('h2.shop-section-title[data-language-tag="shop.title-featured2"]')
        
        if element:
            bounding_box = element.bounding_box()
            clip = {
                'x': bounding_box['x'] - 10,
                'y': bounding_box['y'] - 10,
                'width': bounding_box['width'] + 20,
                'height': bounding_box['height'] + 15
            }
            screenshot = page.screenshot(clip=clip)
            filename = os.path.join('shop', '3.png')
            with open(filename, 'wb') as f:
                f.write(screenshot)
        
        for index, element in enumerate(elements):
            page.evaluate('(selector) => { const h2Element = document.querySelector(selector).previousElementSibling; if (h2Element && h2Element.tagName === "H2") { h2Element.remove(); } }', '.items-row.shop-items.slosh-mode')

            screenshot = page.screenshot(clip={'x': element.bounding_box()['x'] - 10, 'y': element.bounding_box()['y'] - 50, 'width': element.bounding_box()['width'] + 20, 'height': element.bounding_box()['height'] + 100})


            filename = os.path.join('shop', f"{index + 4}.png")
            with open(filename, 'wb') as f:
                f.write(screenshot)
            
            try:    
                remove_element_by_selector(page, '.items-row.shop-items.slosh-mode')
                page.evaluate('(selector) => { const h2Element = document.querySelector(selector).previousElementSibling; if (h2Element && h2Element.tagName === "H2") { h2Element.remove(); } }', '.items-row.shop-items.slosh-mode')
            except:
                pass
            
            time.sleep(5)
            
        browser.close()
        
def create_collage(image_paths, output_path):
    try:
        image_paths.sort(key=lambda x: int(x.split('.')[0][5:]))

        images = [Image.open(image_path) for image_path in image_paths]
    
        collage_width = max(image.width for image in images)     
        collage_height = sum(image.height for image in images)

        collage = Image.new('RGB', (collage_width, collage_height), (135, 206, 235))  # Sky blue color

        y_offset = 0
        for image in images:
            if image.width >= image.height:
                collage.paste(image, (0, y_offset))
                y_offset += image.height
            else:
                collage.paste(image, (collage_width - image.width, y_offset))
                y_offset += image.height  # Adjust y_offset even for portrait images

            # Clear image cache
            image.load()

        collage.save(output_path, quality=95)
        print("Collage created and saved.")

        for image_path in image_paths:
            image_name = os.path.basename(image_path)
            if image_name not in ('1.png', '2.png'):
                os.remove(image_path)
                print(f"Deleted {image_path}")

    except Exception as e:
        print("An error occurred:", str(e))

def place_collage_in_center(background_path, collage_path, output_path):
    # Open the background image and collage image
    background_img = Image.open(background_path)
    collage_img = Image.open(collage_path)

    # Calculate the dimensions needed for the background image
    collage_width, collage_height = collage_img.size
    bg_width = int(collage_width * 1.1)  # 1.4 times the collage width
    bg_height = int(collage_height * 1.05)  # 1.4 times the collage height

    # Resize the background image while maintaining its aspect ratio
    bg_ratio = bg_width / bg_height
    if bg_ratio > 1:
        bg_height = int(bg_width / bg_ratio)
    else:
        bg_width = int(bg_height * bg_ratio)

    background_img = background_img.resize((bg_width, bg_height))

    # Calculate the position to center the collage image on the background image
    x_position = (bg_width - collage_width) // 2
    y_position = (bg_height - collage_height) // 2

    # Paste the collage image on the background image
    background_img.paste(collage_img, (x_position, y_position))

    # Save the resulting image
    background_img.save(output_path)

def login_to_twitter(username, password):
    
    with sync_playwright() as playwright:
    
        browser = playwright.chromium.launch(headless=True, channel='msedge')
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://twitter.com/login")
        time.sleep(random.uniform(2,4))
        # Fill in the login form
        page.fill('input[autocomplete="username"]', username)
        
        time.sleep(random.uniform(2,4))
        # Press the "Next" button
        page.click('text="Next"')
        time.sleep(random.uniform(2,4))
        # Wait for the password input field to appear
        page.wait_for_selector('input[autocomplete="current-password"]')
        time.sleep(random.uniform(2,4))
        # Fill in the password
        page.fill('input[autocomplete="current-password"]', password)
        time.sleep(random.uniform(2,4))
        # Submit the form
        page.click('div[data-testid="LoginForm_Login_Button"]')
        
        time.sleep(random.uniform(4,5))
        
        page.goto("https://twitter.com/compose/tweet")
        
        tweet_message = ' ‼️‼️‼️‼️‼️‼️\n🎮 Fortnite\n🔁 Today’s Daily Item Shop\n〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️\n🏅Rate today’s options with a GIF\n#Fortnite #FortniteCh4S3 \n#HipDiscovery #HDGaming '

        time.sleep(random.uniform(4,5))
        
        textarea = page.query_selector('[data-testid="tweetTextarea_0"]')
        
        time.sleep(random.uniform(1,2))
        
        textarea.fill(tweet_message)
        
        time.sleep(random.uniform(4,5))

        image_path = 'collage.png'
        
        input_file = page.query_selector('input[type="file"]')
        input_file.set_input_files(image_path)

        try:
            post_button = page.wait_for_selector('div[data-testid="tweetButton"]')
            post_button.click()
        except:
            pass
        
        page.keyboard.press('Enter')
        
        time.sleep(random.uniform(3,5))
        
        try:
            os.remove('collage.png')
            os.remove('output_image.png')
        except:
            pass
            
        context.close()
        browser.close()
        
def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2 - 1, rad * 2 - 1), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im
        
if __name__ == "__main__":
    
    username = input("Enter Twitter Username: @")
    password = input("Enter Twitter Password: ")
    
    website_url = "https://fnbr.co/shop"  
    
    recording_duration = 30
    
    input_folder = "shop" 
    output_path = "collage.png"
    background_image_path = "bg.jpg"
    collage_image_path = "collage.png"
    output_image_path = "output_image.jpg"

    print("Started. Waiting For 7 PM in USA Central Time Zone To Post.")
     
    while True:
        try:
            current_time = datetime.datetime.now()
            central_tz = pytz.timezone('US/Central')
            current_time_ct = current_time.astimezone(central_tz)
            
            start_time = current_time_ct.replace(hour=19, minute=0, second=0, microsecond=0)
            end_time = current_time_ct.replace(hour=19, minute=10, second=0, microsecond=0)
            
            if is_within_posting_window():
                time_until_post = end_time - current_time_ct
                print(f"Current Time (CT): {current_time_ct.strftime('%Y-%m-%d %I:%M:%S %p')} | Time Remaining until Post: {time_until_post}")
                
                try:
                    
                    print("It's within the posting window (7:00 PM to 7:10 PM in USA Central Time). Starting...")
                    take_screenshot()
                    png_image_paths = [os.path.join(input_folder, filename) for filename in os.listdir(input_folder) if filename.lower().endswith(".png")]
                    create_collage(png_image_paths, output_path)
                    place_collage_in_center(background_image_path, collage_image_path, output_image_path)
                    im = Image.open('output_image.jpg')
                    im = add_corners(im, 100)
                    im.save('collage.png')
                    print("Uploading To Twitter.")
                    login_to_twitter(username, password)
                    print("Tweeted! Waiting For 60 Min Before Starting Again.")
                    time.sleep(3600)
                    
                except:
                    pass
            else:
                time_until_post = start_time - current_time_ct
                print(f"Current Time (CT): {current_time_ct.strftime('%Y-%m-%d %I:%M:%S %p')} | Time Until Next Posting Window: {time_until_post}")
                time.sleep(30)
                
        except Exception as e:
            print("An error occurred:", str(e))
            time.sleep(30)
            