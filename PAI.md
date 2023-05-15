```python
from google.colab import drive
drive.mount('/content/drive')
```

    Mounted at /content/drive



```python
!jupyter nbconvert --to markdown "/content/drive/MyDrive/Cola"
```

    [NbConvertApp] WARNING | pattern './MyDrive/Colab Notebooks/Python_Algorithm_Interview.ipynb' matched no files
    This application is used to convert notebook files (*.ipynb)
            to various other formats.
    
            WARNING: THE COMMANDLINE INTERFACE MAY CHANGE IN FUTURE RELEASES.
    
    Options
    =======
    The options below are convenience aliases to configurable class-options,
    as listed in the "Equivalent to" description-line of the aliases.
    To see all configurable class-options for some <cmd>, use:
        <cmd> --help-all
    
    --debug
        set log level to logging.DEBUG (maximize logging output)
        Equivalent to: [--Application.log_level=10]
    --show-config
        Show the application's configuration (human-readable format)
        Equivalent to: [--Application.show_config=True]
    --show-config-json
        Show the application's configuration (json format)
        Equivalent to: [--Application.show_config_json=True]
    --generate-config
        generate default config file
        Equivalent to: [--JupyterApp.generate_config=True]
    -y
        Answer yes to any questions instead of prompting.
        Equivalent to: [--JupyterApp.answer_yes=True]
    --execute
        Execute the notebook prior to export.
        Equivalent to: [--ExecutePreprocessor.enabled=True]
    --allow-errors
        Continue notebook execution even if one of the cells throws an error and include the error message in the cell output (the default behaviour is to abort conversion). This flag is only relevant if '--execute' was specified, too.
        Equivalent to: [--ExecutePreprocessor.allow_errors=True]
    --stdin
        read a single notebook file from stdin. Write the resulting notebook with default basename 'notebook.*'
        Equivalent to: [--NbConvertApp.from_stdin=True]
    --stdout
        Write notebook output to stdout instead of files.
        Equivalent to: [--NbConvertApp.writer_class=StdoutWriter]
    --inplace
        Run nbconvert in place, overwriting the existing notebook (only
                relevant when converting to notebook format)
        Equivalent to: [--NbConvertApp.use_output_suffix=False --NbConvertApp.export_format=notebook --FilesWriter.build_directory=]
    --clear-output
        Clear output of current file and save in place,
                overwriting the existing notebook.
        Equivalent to: [--NbConvertApp.use_output_suffix=False --NbConvertApp.export_format=notebook --FilesWriter.build_directory= --ClearOutputPreprocessor.enabled=True]
    --no-prompt
        Exclude input and output prompts from converted document.
        Equivalent to: [--TemplateExporter.exclude_input_prompt=True --TemplateExporter.exclude_output_prompt=True]
    --no-input
        Exclude input cells and output prompts from converted document.
                This mode is ideal for generating code-free reports.
        Equivalent to: [--TemplateExporter.exclude_output_prompt=True --TemplateExporter.exclude_input=True --TemplateExporter.exclude_input_prompt=True]
    --allow-chromium-download
        Whether to allow downloading chromium if no suitable version is found on the system.
        Equivalent to: [--WebPDFExporter.allow_chromium_download=True]
    --disable-chromium-sandbox
        Disable chromium security sandbox when converting to PDF..
        Equivalent to: [--WebPDFExporter.disable_sandbox=True]
    --show-input
        Shows code input. This flag is only useful for dejavu users.
        Equivalent to: [--TemplateExporter.exclude_input=False]
    --embed-images
        Embed the images as base64 dataurls in the output. This flag is only useful for the HTML/WebPDF/Slides exports.
        Equivalent to: [--HTMLExporter.embed_images=True]
    --sanitize-html
        Whether the HTML in Markdown cells and cell outputs should be sanitized..
        Equivalent to: [--HTMLExporter.sanitize_html=True]
    --log-level=<Enum>
        Set the log level by value or name.
        Choices: any of [0, 10, 20, 30, 40, 50, 'DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL']
        Default: 30
        Equivalent to: [--Application.log_level]
    --config=<Unicode>
        Full path of a config file.
        Default: ''
        Equivalent to: [--JupyterApp.config_file]
    --to=<Unicode>
        The export format to be used, either one of the built-in formats
                ['asciidoc', 'custom', 'html', 'latex', 'markdown', 'notebook', 'pdf', 'python', 'rst', 'script', 'slides', 'webpdf']
                or a dotted object name that represents the import path for an
                ``Exporter`` class
        Default: ''
        Equivalent to: [--NbConvertApp.export_format]
    --template=<Unicode>
        Name of the template to use
        Default: ''
        Equivalent to: [--TemplateExporter.template_name]
    --template-file=<Unicode>
        Name of the template file to use
        Default: None
        Equivalent to: [--TemplateExporter.template_file]
    --theme=<Unicode>
        Template specific theme(e.g. the name of a JupyterLab CSS theme distributed
        as prebuilt extension for the lab template)
        Default: 'light'
        Equivalent to: [--HTMLExporter.theme]
    --sanitize_html=<Bool>
        Whether the HTML in Markdown cells and cell outputs should be sanitized.This
        should be set to True by nbviewer or similar tools.
        Default: False
        Equivalent to: [--HTMLExporter.sanitize_html]
    --writer=<DottedObjectName>
        Writer class used to write the
                                            results of the conversion
        Default: 'FilesWriter'
        Equivalent to: [--NbConvertApp.writer_class]
    --post=<DottedOrNone>
        PostProcessor class used to write the
                                            results of the conversion
        Default: ''
        Equivalent to: [--NbConvertApp.postprocessor_class]
    --output=<Unicode>
        overwrite base name use for output files.
                    can only be used when converting one notebook at a time.
        Default: ''
        Equivalent to: [--NbConvertApp.output_base]
    --output-dir=<Unicode>
        Directory to write output(s) to. Defaults
                                      to output to the directory of each notebook. To recover
                                      previous default behaviour (outputting to the current
                                      working directory) use . as the flag value.
        Default: ''
        Equivalent to: [--FilesWriter.build_directory]
    --reveal-prefix=<Unicode>
        The URL prefix for reveal.js (version 3.x).
                This defaults to the reveal CDN, but can be any url pointing to a copy
                of reveal.js.
                For speaker notes to work, this must be a relative path to a local
                copy of reveal.js: e.g., "reveal.js".
                If a relative path is given, it must be a subdirectory of the
                current directory (from which the server is run).
                See the usage documentation
                (https://nbconvert.readthedocs.io/en/latest/usage.html#reveal-js-html-slideshow)
                for more details.
        Default: ''
        Equivalent to: [--SlidesExporter.reveal_url_prefix]
    --nbformat=<Enum>
        The nbformat version to write.
                Use this to downgrade notebooks.
        Choices: any of [1, 2, 3, 4]
        Default: 4
        Equivalent to: [--NotebookExporter.nbformat_version]
    
    Examples
    --------
    
        The simplest way to use nbconvert is
    
                > jupyter nbconvert mynotebook.ipynb --to html
    
                Options include ['asciidoc', 'custom', 'html', 'latex', 'markdown', 'notebook', 'pdf', 'python', 'rst', 'script', 'slides', 'webpdf'].
    
                > jupyter nbconvert --to latex mynotebook.ipynb
    
                Both HTML and LaTeX support multiple output templates. LaTeX includes
                'base', 'article' and 'report'.  HTML includes 'basic', 'lab' and
                'classic'. You can specify the flavor of the format used.
    
                > jupyter nbconvert --to html --template lab mynotebook.ipynb
    
                You can also pipe the output to stdout, rather than a file
    
                > jupyter nbconvert mynotebook.ipynb --stdout
    
                PDF is generated via latex
    
                > jupyter nbconvert mynotebook.ipynb --to pdf
    
                You can get (and serve) a Reveal.js-powered slideshow
    
                > jupyter nbconvert myslides.ipynb --to slides --post serve
    
                Multiple notebooks can be given at the command line in a couple of
                different ways:
    
                > jupyter nbconvert notebook*.ipynb
                > jupyter nbconvert notebook1.ipynb notebook2.ipynb
    
                or you can specify the notebooks list in a config file, containing::
    
                    c.NbConvertApp.notebooks = ["my_notebook.ipynb"]
    
                > jupyter nbconvert --config mycfg.py
    
    To see all available configurables, use `--help-all`.
    


# 파이썬과 CS

## 빅오, 자료형

### 빅오

 * 빅오 $Big-O$ 란 입력값이 무한대로 향할 때 함수의 상한을 설명하는 수학적 표기방법
 * 점근적 실행 시간 Asympototic Running Time을 표기
 * 파일의 크기 $n$가 커짐에 따라 $O(n)$ 일정량을 넘기면 비행기를 통한 물리적 전송 $O(1)$이 더 빠를 수 있다
 * 빅오 표기법은 주어진 (최선/평균/최악)의 경우의 수행 시간의 상한을 나타낸다

### 시간복잡도 Time Complexity

 * 사전적 정의로는 알고리즘을 수행하는 데 걸리는 시간을 설명하는 계산 복잡도 Computational Complexity를 의미
 * 이를 표현하기 위해 빅오 $Big-O$를 사용
 *$Big-O$로 시간 복잡도를 표현할 때는 최고차항만을 표기하며 계수는 무시  
ex)$4n^3+3n+4$의 경우 최고차항인 $4n^2$만을 고려하고, 계수를 제외한 $n^2$만을 기준으로 삼기에 시간 복잡도는 $O(n^2)$이다.

### $Big-O$표기법의 종류

#### 각 방식의 속도 순서
$ O(1) < O(\log n) < O(n) < O(n \log n) < O(n^2) < O(2^n) < O(n!)$

#### $O(1)$ 
* 입력값의 크기와 상관없이 실행시간이 일정함
* 상수실행 시간에서 상수값이 너무 커질 경우 일정한 시간의 의미가 상쇄
* 대표적으로는 해시 테이블의 조회 및 삽입이 해당됨

#### $O(\log n)$ 
* 로그의 존재로 입력값의 영향을 상대적으로 덜 받음
* 웬만한 $n$의 크기에 대해서도 견고함
* 대표적으로는 이진 검색이 해당됨

#### $O(n)$ 
* 입력값만큼 실행시간에 영향을 받는데, 수행시간 == 입력값에 비례
* 선형 시간 Linear-Time 알고리즘
* 정렬되지 않은 리스트에서 최댓값 또는 최솟값을 찾는 경우가 해당 값을 찾기 위해 
 
 모든 입력값을 적어도 한 번 이상 확인해야함

#### $O(n \log n)$ 
* 모든 수에 대해 한 번 이상은 비교해야 하는 비교 기반 정렬 알고리즘은  
$O(n \log n)$보다 빠르기 힘듦
* 대부분의 효율이 좋은 정렬 알고리즘이 해당 (병합정렬 등)
* 입력값이 최선인 경우 비교를 하지 않아 $O(n)$이 될 수 있으며, 팀소트 Timsort가 이에 해당 되는 경우


#### $O(n^2)$ 
* 비효율적인 정렬 알고리즘이 이에 해당 (버블정렬 등)

#### $O(2^n)$ 
* 피보나치 수열을 재귀로 계산 하는 알고리즘이 해당
* $O(n^2)$와 혼동하는 경우가 있을 수 있지만, $n$의 크기가 커질수록 차이가 매우 큼

#### $O(n!)$ 
* 각 도시를 방문하고 가장 짧은 경로를 찾는 외판원 문제  
Travelling Salesman Problem(TSM)을 브루트 포스 Brute Force로 풀이할 경우가 해당
* 입력값이 조금만 커져도 웬만한 다항 시간 내에 계산이 어려움

#### 상한과 최악

* 빅오($O$)는 상한 Upper Bound
* 빅세타($𝜣$)는 평균
* 빅오메가($𝜴$)는 하한 Lower Bound
* 업계와 학계의 시각을 다르게 볼 수 있음
* 상한과 최악의 경우는 다름
* 빅오표기법은 정확하게 쓰기에는 너무 길고 복잡한 함수를 '적당히 정확하게' 표현하는 방법
* 최악의 경우/평균적인 경우의 시간 복잡도와는 관계가 없음

#### 분할 상환 분석 p.106

#### 병렬화 p.106

## 자료형


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```

## 리스트, 딕셔너리

### 리스트
 * 순서대로 저장하는 Sequence형 자료형
 * 변경이 가능한 mutablelist

 * list 내 값의 유무 탐색은 이진 검색이 효율적
 * 값의 정렬이 필요하지만, list는 입력 순서에 따른 정렬만이 되어있어 요소의 순차 조회발생
 * 최악의 경우 항상 $O(n)$이 소요

|연산|&nbsp;시간복잡도&nbsp;|설명|
|:---|:---:|:---|
|len(a)|$O(1)$|전체 요소의 길이 리턴|
|a[i]|$O(1)$|인덱스 i의 요소 리턴|
|a[i:j]|$O(k)$|i부터 j까지 슬라이스 된 $k$리턴, 객체 $k$에 대한 조회가 있어 $O(k)$|
|elem in a|$O(n)$|elem 요소의 존재유무확인, 순차탐색으로 $O(n)$|
|a.count(elem)|$O(n)$|elem 요소의 개수 리턴|
|a.index(elem)|$O(n)$|elem 요소의 인덱스 리턴|
|a.append(elem)|$O(1)$|리스트 마지막에 elem 요소 추가|
|a.pop()|$O(n)$|리스트 마지막 요소 추출, 스택Stack 연산|
|a.pop(0)|$O(1)$|리스트 첫 번째 요소 추출, 큐Queue연산, 전체복사가 발생해서 $O(n)$<br>큐연산을 자주 할 경우, 리스트보다 $O(1)$에 가능한 데큐Deque 권장|
|del a[i]|$O(n)$|i에 따라 달라지며 최악의 경우 $O(n)$|
|a.sort()|$O(n  \log n)$|팀소트Timsort를 사용한 정렬, 최선의 경우 $O(n)$가능|
|max(a), min(a)|$O(n)$|최댓값, 최솟값을 계산하기 위해 전체 선형 탐색|
|a.reverse|$O(n)$|순서를 역순 배치, 리스트의 특성상 입력순의 역순|

#### Python에서 List의 특징
 * Python은 원시자료형을 갖지 않음
 * Cpython에서 리스트는 요소에 대한 포인터목록ob_item을 가진 구조체Struct로 구현
 * 요소의 추가나 삭제시 ob_item의 사이즈 조절
 * 객체로 구성된 모든 자료형을 포인터로 연결 <br>=> 연결리스트에 대한 포인터목록을 배열의 형태로 구현
 * 각각의 자료형의 길이가 다르기때문에 연속된 메모리 할당이 불가능
 * 각각의 객체에 대해서 참조구현을 통해 구성
 * 따라서 조회시 모든 포인터의 위치와 타입 코드, 값 등을 대조하는 등의<br>추가적인 작업이 필연적으로 발생
 * 기능성을 위해 속도가 희생됨

#### 슬라이싱 Slicing


```python
list [a:b] 
#리스트의 a번째 인덱스부터 b번째 인덱스 이전까지
#  [start:stop:step]의 순서로 step의 값을 통해 홀수번째나 짝수번째 추출 가능
```


```python
list = (1, 2, 3)
list[3]
# 인덱스의 값이 넘어갈경우 IndexError발생
# try문을 통한 예외처리가능
```

### 딕셔너리
 * 키와 값을 함께 저장하는 Sequence형 자료형
 * Python 3.7부터 입력된 순서를 유지
 * 실무환경에서 3.6이하의 버전에선 입력순서가 없을 수 있음
 


```python

```

## 문자열 조작


```python

```

# 선형 자료구조

## 배열


```python

```

## 연결 리스트


```python

```

## 스택, 큐


```python

```

## 데크, 우선순위 큐


```python

```

## 해시 테이블


```python

```

# 비선형 자료구조

## 그래프


```python

```


```python

```

## 최단 경로 문제


```python

```


```python

```

## 트리


```python

```


```python

```

## 힙


```python

```


```python

```

## 트라이


```python

```


```python

```

# 알고리즘

## 정렬 


```python

```


```python

```

## 이진 검색


```python

```


```python

```

## 비트 조작


```python

```


```python

```

## 슬라이딩 윈도우


```python

```


```python

```

## 그리디 알고리즘


```python

```


```python

```

## 분할 정복


```python

```


```python

```

## 다이나믹 프로그래밍


```python

```


```python

```
