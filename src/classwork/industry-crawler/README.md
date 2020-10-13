# Industry Crawler

This application contains a web-crawler that downloads industry information from an [official/public government page](https://www.osha.gov/pls/imis/sic_manual.html). The implementation relies on nested-structures (tree-like data), string operations, and recursive search using python.

Objectives: 

* Real world data extraction using a custom web-crawler. 
* Understanding of data modeling by using object-oriented programming. 
* Usage of list/dict comprehension, recursion, and other pythonic-patterns. 


## Usage

* Download the data with the following command:

```commandline
$ python industry-crawler download --filename industries.json
```

Expected output: create a file named `industries.json`.

* Show industries

```commandline
$ python industry-crawler show --filename industries.json --until 'SIC Single Industry'
```

Expected output: show the industries on the terminal.
