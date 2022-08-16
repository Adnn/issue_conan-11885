# Issue Conan 11885

Minimal example to illustrate an issue with multiconfig generation.

## Usage

    git clone https://github.com/Adnn/issue_conan-11885.git
    cd issue_conan-11885/
    ./test.sh
    
When targetting Visual Studio (in default Conan profile), this should fail with:

    error LNK2038: mismatch detected for '_ITERATOR_DEBUG_LEVEL': value '2' doesn't match value '0' in main.obj
