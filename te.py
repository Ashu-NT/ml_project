import os

FOLDER_NAME = ["migration","core","infra","ui"]

project_path = r"C:\Users\ALL COMPUTERS\Desktop\Projects\project_mangement_app"

for root, dirs, files in os.walk(project_path):
    # Compute relative path
    rel_path = os.path.relpath(root, project_path)

    # --- CONTROL WHICH FOLDERS os.walk ENTERS ---
    if rel_path == ".":
        # At ROOT → keep only allowed folders
        dirs[:] = [d for d in dirs if d in FOLDER_NAME]
        rel_path = "ROOT"
    else:
        # If not ROOT → skip folders not in FOLDER_NAME
        top_folder = rel_path.split(os.sep)[0]
        if top_folder not in FOLDER_NAME:
            dirs[:] = []  # stop walking deeper
            continue
    # ------------------------------------------------

    # Prepare output directory
    output_dir = os.path.join(project_path, "exports_2")
    os.makedirs(output_dir, exist_ok=True)

    # Output file name
    safe_name = rel_path.replace("\\", "_").replace("/", "_")
    output_file = os.path.join(output_dir, f"{safe_name}_code.txt")

    # Write .py files
    with open(output_file, "w", encoding="utf-8") as outfile:
        outfile.write(f"### Subfolder: {rel_path} ###\n\n")

        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                outfile.write(f"\n# ===== {file} =====\n\n")
                with open(file_path, "r", encoding="utf-8") as infile:
                    outfile.write(infile.read())
