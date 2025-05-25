#!/usr/bin/env python3
"""
Script to generate an index.html file listing all PDF files in the current directory.
Perfect for GitHub Pages or any static site hosting.
"""

import os
import glob
from pathlib import Path
from datetime import datetime

def format_file_size(size_bytes):
    """Convert bytes to human readable format"""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024**2:
        return f"{size_bytes/1024:.1f} KB"
    elif size_bytes < 1024**3:
        return f"{size_bytes/(1024**2):.1f} MB"
    else:
        return f"{size_bytes/(1024**3):.1f} GB"

def generate_pdf_index():
    """Generate index.html with all PDF files in current directory"""

    # Find all PDF files in current directory
    pdf_files = glob.glob("*.pdf")
    pdf_files.sort(key=str.lower)  # Sort alphabetically, case-insensitive

    # HTML template
    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PDF Files</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            line-height: 1.6;
            color: #333;
        }}

        h1 {{
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }}

        .pdf-list {{
            list-style: none;
            padding: 0;
        }}

        .pdf-item {{
            background: #f8f9fa;
            margin: 10px 0;
            padding: 15px;
            border-radius: 6px;
            border-left: 4px solid #e74c3c;
            transition: background-color 0.3s ease;
        }}

        .pdf-item:hover {{
            background: #e9ecef;
        }}

        .pdf-link {{
            text-decoration: none;
            color: #2c3e50;
            font-weight: 500;
            display: flex;
            align-items: center;
        }}

        .pdf-link:hover {{
            color: #3498db;
        }}

        .pdf-icon {{
            margin-right: 10px;
            font-size: 1.2em;
        }}

        .file-size {{
            color: #6c757d;
            font-size: 0.9em;
            margin-left: auto;
        }}

        .no-files {{
            text-align: center;
            color: #6c757d;
            font-style: italic;
            padding: 40px 0;
        }}

        .footer {{
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #dee2e6;
            color: #6c757d;
            font-size: 0.9em;
            text-align: center;
        }}
    </style>
</head>
<body>
    <h1>📄 PDF Files</h1>

    <ul class="pdf-list" id="pdfList">
{pdf_items}
    </ul>

    <div class="footer">
        Generated on {timestamp} • {file_count} PDF file(s) found
    </div>

    <script>
        // Add click tracking
        document.querySelectorAll('.pdf-link').forEach(link => {{
            link.addEventListener('click', function() {{
                console.log('Opening PDF:', this.href);
            }});
        }});
    </script>
</body>
</html>"""

    # Generate PDF items HTML
    pdf_items_html = ""

    if pdf_files:
        for pdf_file in pdf_files:
            try:
                # Get file size
                file_size = os.path.getsize(pdf_file)
                formatted_size = format_file_size(file_size)

                # Create display name (remove .pdf extension for display)
                display_name = Path(pdf_file).stem

                # Add HTML for this PDF
                pdf_items_html += f"""        <li class="pdf-item">
            <a href="{pdf_file}" class="pdf-link" target="_blank">
                <span class="pdf-icon">📄</span>
                <span>{display_name}.pdf</span>
                <span class="file-size">{formatted_size}</span>
            </a>
        </li>
"""
            except OSError:
                # Handle case where file size can't be read
                pdf_items_html += f"""        <li class="pdf-item">
            <a href="{pdf_file}" class="pdf-link" target="_blank">
                <span class="pdf-icon">📄</span>
                <span>{pdf_file}</span>
                <span class="file-size">Size unknown</span>
            </a>
        </li>
"""
    else:
        pdf_items_html = """        <li class="no-files">
            No PDF files found in this directory
        </li>"""

    # Generate timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Fill in the template
    final_html = html_template.format(
        pdf_items=pdf_items_html,
        timestamp=timestamp,
        file_count=len(pdf_files)
    )

    # Write to index.html
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f"✅ Generated index.html with {len(pdf_files)} PDF files")
    if pdf_files:
        print("📄 Found PDFs:")
        for pdf in pdf_files:
            size = format_file_size(os.path.getsize(pdf))
            print(f"   • {pdf} ({size})")
    else:
        print("⚠️  No PDF files found in current directory")

if __name__ == "__main__":
    generate_pdf_index()
