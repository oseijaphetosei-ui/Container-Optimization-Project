"""
QR Code Generator for Container Optimization App

This script generates a QR code for your deployed Streamlit app.
Once you have your Streamlit Cloud URL, update the URL below and run this script.
"""

def generate_qr_code():
    try:
        import qrcode
        from PIL import Image
    except ImportError:
        print("Installing required packages...")
        import subprocess
        subprocess.check_call(['pip3', 'install', 'qrcode[pil]'])
        import qrcode
        from PIL import Image
    
    # REPLACE THIS WITH YOUR ACTUAL STREAMLIT CLOUD URL
    # You'll get this URL after deploying to Streamlit Cloud
    streamlit_url = "https://your-app-name.streamlit.app"
    
    print("=" * 60)
    print("Container Optimization App - QR Code Generator")
    print("=" * 60)
    
    # Check if URL has been updated
    if "your-app-name" in streamlit_url:
        print("\n⚠️  Please update the URL in this script first!")
        print("\nSteps:")
        print("1. Deploy your app to Streamlit Cloud")
        print("2. Copy your Streamlit URL")
        print("3. Edit this file and replace the URL on line 17")
        print("4. Run this script again\n")
        
        # Ask if user wants to input URL now
        use_input = input("Do you want to enter the URL now? (y/n): ").strip().lower()
        if use_input == 'y':
            streamlit_url = input("\nEnter your Streamlit Cloud URL: ").strip()
        else:
            return
    
    print(f"\nGenerating QR code for: {streamlit_url}")
    
    # Create QR code
    qr = qrcode.QRCode(
        version=1,  # Controls size (1 is 21x21)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
        box_size=10,  # Size of each box in pixels
        border=4,  # Border size in boxes
    )
    
    qr.add_data(streamlit_url)
    qr.make(fit=True)
    
    # Create image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save QR code
    filename = "container_optimizer_qr.png"
    img.save(filename)
    
    print(f"\n✅ QR code generated successfully!")
    print(f"📁 Saved as: {filename}")
    print(f"🔗 Links to: {streamlit_url}")
    print("\nYou can now:")
    print("- Share the QR code image")
    print("- Print it for presentations")
    print("- Add it to your README or documentation")
    print("- Include it in slides or posters")
    print("\n" + "=" * 60)


if __name__ == "__main__":
    generate_qr_code()
