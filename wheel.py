from PIL import Image, ImageDraw, ImageFont
import random
import io
import math
import colorsys
import urllib
import discord

async def spin_wheel(ctx, game_number, boardlist):
    """General function to spin a wheel for a Mario Party game."""
    selected_board, gif_io, final_img_io = generate_wheel_gif(boardlist)
    boardParsed = urllib.parse.quote(selected_board)

    gif_file = discord.File(gif_io, "spinning_wheel.gif")
    message = await ctx.respond(file=gif_file)

    await asyncio.sleep(5)
    await message.delete()

    github_image_url = f"https://raw.githubusercontent.com/MarioPartyNetplay/Poggers-Rewrite/master/boards/{game_number.upper()}/{boardParsed}.png"

    final_image_file = discord.File(final_img_io, "final_wheel.png")
    await ctx.send(file=final_image_file)

    result_embed = discord.Embed(title=f"\U0001F389 The wheel landed on: {selected_board}!", colour=0x98FB98)
    result_embed.set_image(url=github_image_url)
    result_embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Poggers")

    await ctx.send(embed=result_embed)

def generate_wheel_gif(boardList):
    """Generates a spinning GIF and a final static wheel image with vibrant colors."""
    size = 400  # Image size
    num_slices = len(boardList)
    angle_per_slice = 360 / num_slices
    
    # Generate vibrant colors
    colors = generate_vibrant_colors(num_slices)
    
    frames = []
    selected_index = random.randint(0, num_slices - 1)
    selected_item = boardList[selected_index]
    
    for frame_angle in range(0, 360 * 3 + 15, 15):  # Spin animation
        image = Image.new("RGBA", (size, size), (0, 0, 0, 0))  # Fully transparent background
        draw = ImageDraw.Draw(image)
        
        # Draw wheel slices
        for i in range(num_slices):
            start_angle = i * angle_per_slice + frame_angle  # Rotate with the wheel
            end_angle = start_angle + angle_per_slice
            draw.pieslice((0, 0, size, size), start=start_angle, end=end_angle, fill=colors[i])
        
        # Add text to slices (after all slices are drawn)
        for i in range(num_slices):
            start_angle = i * angle_per_slice + frame_angle
            end_angle = start_angle + angle_per_slice
            text = boardList[i]
            mid_angle = math.radians((start_angle + end_angle) / 2)
            add_text_to_slice(draw, text, mid_angle, size, colors[i])
        
        # Draw arrow at the top
        draw_arrow(draw, size)
        frames.append(image)
    
    # Create final static image with winning board at the top
    final_image = Image.new("RGBA", (size, size), (0, 0, 0, 0))  # Fully transparent background
    final_draw = ImageDraw.Draw(final_image)
    
    # Calculate the rotation needed to position the selected item at the top
    # Top position is at 270 degrees in PIL's coordinate system (0 at 3 o'clock, goes clockwise)
    top_position = 270
    
    # Calculate the current angle of the selected item
    selected_mid_angle = selected_index * angle_per_slice + angle_per_slice / 2
    
    # Calculate rotation needed to move selected item to top
    rotation_angle = top_position - selected_mid_angle
    
    # Draw final wheel with selected board at the top
    for i in range(num_slices):
        # Apply the rotation to position the selected item at the top
        start_angle = i * angle_per_slice + rotation_angle
        end_angle = start_angle + angle_per_slice
        final_draw.pieslice((0, 0, size, size), start=start_angle, end=end_angle, fill=colors[i])
    
    # Re-add text to final image
    for i in range(num_slices):
        start_angle = i * angle_per_slice + rotation_angle
        end_angle = start_angle + angle_per_slice
        text = boardList[i]
        mid_angle = math.radians((start_angle + end_angle) / 2)
        add_text_to_slice(final_draw, text, mid_angle, size, colors[i])
    
    # Redraw arrow in final image
    draw_arrow(final_draw, size)
    
    # Convert GIF and final image to BytesIO
    gif_io = io.BytesIO()
    frames[0].save(gif_io, format="GIF", save_all=True, append_images=frames[1:], duration=50, loop=0)
    gif_io.seek(0)
    
    final_img_io = io.BytesIO()
    final_image.save(final_img_io, "PNG")
    final_img_io.seek(0)
    
    return selected_item, gif_io, final_img_io

def generate_vibrant_colors(num_colors):
    """Generate vibrant, distinct colors for the wheel slices."""
    colors = []
    
    # Vibrant base colors (RGB tuples)
    vibrant_palette = [
        (255, 0, 0),      # Bright Red
        (0, 0, 255),      # Bright Blue
        (0, 200, 0),      # Bright Green
        (255, 255, 0),    # Yellow
        (255, 0, 255),    # Magenta
        (0, 255, 255),    # Cyan
        (255, 165, 0),    # Orange
        (128, 0, 128),    # Purple
        (255, 105, 180),  # Hot Pink
        (0, 128, 128),    # Teal
        (255, 215, 0),    # Gold
        (0, 191, 255)     # Deep Sky Blue
    ]
    
    # If we have fewer slices than colors, randomly select from the palette
    if num_colors <= len(vibrant_palette):
        return random.sample(vibrant_palette, num_colors)
    
    # If we need more colors, use HSV color model to generate evenly distributed hues
    for i in range(num_colors):
        # Distribute hues evenly around the color wheel
        h = i / num_colors
        # Use high saturation and value for vibrant colors
        s = 0.9 + random.uniform(-0.1, 0.1)  # High saturation with slight variation
        v = 0.9 + random.uniform(-0.1, 0.1)  # High value with slight variation
        
        # Convert HSV to RGB
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        # Convert to 0-255 range
        rgb = (int(r * 255), int(g * 255), int(b * 255))
        colors.append(rgb)
    
    # Shuffle to avoid predictable color sequence
    random.shuffle(colors)
    return colors

def add_text_to_slice(draw, text, angle_rad, size, bg_color):
    """Positions text correctly inside each wedge with appropriate contrast."""
    try:
        # Try to load a TrueType font if available
        font = ImageFont.truetype("arial.ttf", 12)
    except IOError:
        # Fallback to default font
        font = ImageFont.load_default()
    
    # Calculate text position based on angle
    center_x, center_y = size // 2, size // 2
    radius = size // 3  # Reduce radius to keep text more centered in wedges
    
    # Position text along the radius
    text_x = center_x + int(radius * math.cos(angle_rad))
    text_y = center_y + int(radius * math.sin(angle_rad))
    
    # Calculate text rotation angle (in degrees)
    rotation_angle = math.degrees(angle_rad)
    if 90 < rotation_angle < 270:
        # Flip text for better readability when upside down
        rotation_angle += 180
    
    # Determine text color based on background brightness for contrast
    r, g, b = bg_color
    brightness = (0.299 * r + 0.587 * g + 0.114 * b) / 255
    text_color = "black" if brightness > 0.5 else "white"
    
    # Draw the text with proper rotation
    draw.text((text_x, text_y), text, fill=text_color, font=font, anchor="mm" if hasattr(draw, 'textbbox') else None)

def draw_arrow(draw, size):
    """Draws an arrow at the top of the wheel."""
    arrow_size = 20
    arrow_x = size // 2
    arrow_y = 10
    draw.polygon(
        [(arrow_x - arrow_size, arrow_y), (arrow_x + arrow_size, arrow_y), (arrow_x, arrow_y + arrow_size)],
        fill="black"
    )

async def spin_wheel_and_show_result(ctx, options, title, description, image_path=None, filename=None):
    """Generic function to spin wheel and show result with embed."""
    # Use the wheel system
    selected, gif_io, _ = generate_wheel_gif(ctx, options)
    
    await ctx.respond(f"Spinning for {description.lower()}...", delete_after=0)

    # Send the GIF
    gif_file = discord.File(gif_io, "spinning_wheel.gif")
    message = await ctx.send(file=gif_file)

    # Wait for suspense
    await asyncio.sleep(5)

    # Delete the GIF message
    await message.delete()
    
    # Create embed
    result_embed = discord.Embed(title=title, description=f"**{selected}**", colour=0x98FB98)
    
    # Add image if provided
    if image_path and filename:
        file = discord.File(image_path, filename=filename)
        result_embed.set_image(url=f"attachment://{filename}")
        result_embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, The Underground Grotto Bot")
        await ctx.send(embed=result_embed, file=file)
    else:
        result_embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, The Underground Grotto Bot")
        await ctx.send(embed=result_embed)