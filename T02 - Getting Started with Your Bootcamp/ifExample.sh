# test if the directory exists (-d flag) and make the if_folder
if test -d new_folder; then
  mkdir if_folder
fi

# this will only create the hyperionDev directory if the if_folder
# exists else the new-projects directory will be crerated
if test -d if_folder; then
  mkdir hyperionDev
else
  mkdir new-projects
fi
