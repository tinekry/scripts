# 1. Ensure our safe storage bin exists
TRASH_DIR="/c/cpp/.trash_bin"
mkdir -p "$TRASH_DIR"

echo "Locating all folders containing the word 'some_word'..."
echo "----------------------------------------------------"

# 2. Find all directories that have 'some_word' in their name (case-insensitive)
find . -type d -iname "*cpp*" | sort -u | while read -r some_word; do
    echo "Processing folder: $some_word"
    
    # 3. Look inside this folder AND all its subfolders for .exe and .o files
    find "$some_word" -type f \( -name "*.exe" -o -name "*.o" \) | while read -r file; do
        base="${file%.*}"
        
        # 4. Check if the matching .cpp source file is right next to it
        if [ -f "${base}.cpp" ]; then
            filename=$(basename "$file")
            dir=$(dirname "$file")
            
            echo "  -> Moving: $dir/$filename"
            
            # Move to the bin with a timestamp so files with matching names don't overwrite
            mv "$file" "$TRASH_DIR/$(date +%s)_$filename"
        fi
    done
done

echo "----------------------------------------------------"
echo "All some_word folders and their subfolders have been cleaned!"