base_dir=$(pwd);

create_archive() {
  app_dir="$1"
  cd "venv-aws/lib/python3.7/site-packages" || exit
  zip -r9 "$base_dir/$app_dir/$app_dir.zip" "."
  cd "$base_dir/$app_dir/" || exit
  zip -g "$app_dir.zip" lambda_function.py
  cd "$base_dir" || return;
}

create_archive "secretary_dial"
create_archive "secretary_dial_call_status"
