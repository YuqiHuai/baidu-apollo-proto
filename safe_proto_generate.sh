function build_py_proto() {
  rm -rf py_proto
  mkdir -p py_proto

  base_dir="modules"

  # Loop through first-level modules
  for module in "$base_dir"/*; do
    [ -d "$module" ] || continue

    # Skip problematic modules
    case "$module" in
      *canbus_vehicle*|*perception*|*control*)
        echo "Skipping $module"
        continue
        ;;
    esac

    echo "Compiling $module"

    # Find protos only inside this module
    proto_files=$(find "$module" -name "*.proto" | grep -v node_modules)

    [ -z "$proto_files" ] && continue

    # Compile this module only
    protoc -I=. --python_out=py_proto $proto_files

    # Run protol for this module
    protol \
      --create-package \
      --in-place \
      --python-out=py_proto \
      protoc \
      --proto-path=$(pwd) \
      $proto_files

  done
}

build_py_proto