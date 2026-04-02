import os
import sys
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont

# Function for transliterating Russian to English
def transliterate(russian_name):
    # Implement a basic transliteration logic
    # Note: This function needs a proper implementation
    # For example purposes, let's just replace a few common letters
    translit_dict = {'а':'a', 'б':'b', 'в':'v', 'г':'g', 'д':'d', 'е':'e', 'ё':'yo', 'ж':'zh',
                     'з':'z', 'и':'i', 'й':'y', 'к':'k', 'л':'l', 'м':'m', 'н':'n', 'о':'o',
                     'п':'p', 'р':'r', 'с':'s', 'т':'t', 'у':'u', 'ф':'f', 'х':'kh', 'ц':'ts',
                     'ч':'ch', 'ш':'sh', 'щ':'shch', 'ъ':'', 'ы':'y', 'ь':'', 'э':'e', 'ю':'yu', 'я':'ya'}
    return ''.join(translit_dict.get(char, char) for char in russian_name)

# Main function to process command line arguments and modify icon
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: python add_info_to_icons.py <icon_name_russian> <timezone_shift> <quality>')
        sys.exit(1)

    icon_name_russian = sys.argv[1]
    timezone_shift = sys.argv[2]
    quality = sys.argv[3]

    # Transliterate the icon name
    icon_name_english = transliterate(icon_name_russian)

    # Load the icon file
    icon_file_path = os.path.join('icons', f'{icon_name_english}.png')  # Path based on transliteration
    if not os.path.isfile(icon_file_path):
        print(f'Icon file for {icon_name_english} not found.')
        sys.exit(1)

    # Open the icon image
    icon_image = PIL.Image.open(icon_file_path)
    draw = PIL.ImageDraw.Draw(icon_image)

    # Define colors
    red = (255, 0, 0)
    salad_green = (127, 255, 0)
    dark_lemon_green = (173, 255, 47)

    # Choose quality color
    quality_color = salad_green if quality.lower() == 'sd' else dark_lemon_green if quality.lower() == 'hd' else (255, 255, 255)

    # Set font (this path will need to be valid)
    font_path = 'path/to/font.ttf'  # Replace with an actual font file
    font = PIL.ImageFont.truetype(font_path, size=20)

    # Add text overlays
    draw.text((icon_image.width - 100, 10), f'Timezone Shift: {timezone_shift}', fill=red, font=font)
    draw.text((icon_image.width - 100, 50), f'Quality: {quality}', fill=quality_color, font=font)

    # Save the modified image
    output_path = os.path.join('icons', 'modified_', f'{icon_name_english}.png')
    icon_image.save(output_path)
    print(f'Modified icon saved as {output_path}').