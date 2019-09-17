base_dir=$(pwd)

create_archive() {
  app_dir="$1"
  zip_file="$base_dir/$app_dir/$app_dir.zip"

  if [ -f /tmp/foo.txt ]; then
    rm "$zip_file"
  fi

  cd "venv-aws/lib/python3.7/site-packages" || exit
  zip -r9 "$zip_file" "."
  cd "$base_dir/$app_dir/" || exit
  zip -g "$app_dir.zip" lambda_function.py
  cd "$base_dir" || return
}

create_archive "secretary_dial"
create_archive "secretary_dial_call_status"
