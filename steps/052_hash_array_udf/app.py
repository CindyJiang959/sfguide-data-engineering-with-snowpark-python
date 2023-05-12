import sys
import hashlib
import json

def main(column :str, sphere: str, salt: str) -> str:
    arr = json.loads(column)
    hashed_arr = []
    for value in arr:
        split_string = value.split(":")
        trimmed_string = split_string[-1]
        value_sphere_salt = f'{trimmed_string}{sphere}{salt}'
        hash_object = hashlib.sha256(value_sphere_salt.encode())
        hashed_arr.append(hash_object.hexdigest())
        # hashed_arr.append(trimmed_string)
    return ','.join(hashed_arr)

# For local debugging
# Be aware you may need to type-convert arguments if you add input parameters
if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(main(*sys.argv[1:]))  # type: ignore
    else:
        print(main())  # type: ignore
