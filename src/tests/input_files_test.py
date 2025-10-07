import os
import subprocess

def test_all_input_files_return_yes():
    tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../tests'))
    main_py = os.path.abspath(os.path.join(os.path.dirname(__file__), '../main.py'))

    for filename in os.listdir(tests_dir):
        file_path = os.path.join(tests_dir, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as f:
                result = subprocess.run(
                    ['python3', main_py],
                    stdin=f,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
                output = result.stdout.decode().strip()
                assert output == "YES", f"{filename} did not return YES, got: {output}"

if __name__ == "__main__":
    test_all_input_files_return_yes()
    print("All tests passed.")