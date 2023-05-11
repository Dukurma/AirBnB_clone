<h1>0x00. AirBnB clone - The console</h1>
<div>
    <div>Group projectPythonOOP</div>
</div>
<div>
    <ul>
        <li>&nbsp;By:&nbsp;Guillaume</li>
        <li>&nbsp;Weight:&nbsp;5</li>
        <li>&nbsp;Project to be done in teams of&nbsp;2&nbsp;people&nbsp;(your team:&nbsp;Tobiloba Lawal, Julius Njeri)</li>
        <li>&nbsp;Project will start&nbsp;<span title="">May 8, 2023 6:00 AM</span>, must end by&nbsp;<span title="">May 15, 2023 6:00 AM</span></li>
        <li>&nbsp;Checker&nbsp;will be&nbsp;released at&nbsp;<span title="">May 13, 2023 12:00 PM</span></li>
        <li>&nbsp;<strong>Manual QA review must be done</strong> (request it when you are done with the project)</li>
        <li>&nbsp;An auto review will be launched at the deadline</li>
    </ul>
</div>
<div>
    <div>
        <h3>Concepts</h3>
    </div>
    <div>
        <p><em>For this project, we expect you to look at these concepts:</em></p>
        <ul>
            <li><a href="https://intranet.alxswe.com/concepts/66">Python packages</a></li>
            <li><a href="https://intranet.alxswe.com/concepts/74">AirBnB clone</a></li>
        </ul>
    </div>
</div>
<div>
    <div>
        <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230511%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230511T121050Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=844a6e31a34799985f5e35770f4d02ee620b5a784789595a45e3b6c2c6098412" alt=""></p>
        <h2>Background Context</h2>
        <h3>Welcome to the AirBnB clone project!</h3>
        <p>Before starting, please read the&nbsp;<strong>AirBnB</strong> concept page.</p>
        <h4>First step: Write a command interpreter to manage your AirBnB objects.</h4>
        <p>This is the first step towards building your first full web application: the&nbsp;<strong>AirBnB clone</strong>. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration&hellip;</p>
        <p>Each task is linked and will help you to:</p>
        <ul>
            <li>put in place a parent class (called&nbsp;<code>BaseModel</code>) to take care of the initialization, serialization and deserialization of your future instances</li>
            <li>create a simple flow of serialization/deserialization: Instance &lt;-&gt; Dictionary &lt;-&gt; JSON string &lt;-&gt; file</li>
            <li>create all classes used for AirBnB (<code>User</code>,&nbsp;<code>State</code>,&nbsp;<code>City</code>,&nbsp;<code>Place</code>&hellip;) that inherit from&nbsp;<code>BaseModel</code></li>
            <li>create the first abstracted storage engine of the project: File storage.</li>
            <li>create all unittests to validate all our classes and storage engine</li>
        </ul>
        <h3>What&rsquo;s a command interpreter?</h3>
        <p>Do you remember the Shell? It&rsquo;s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:</p>
        <ul>
            <li>Create a new object (ex: a new User or a new Place)</li>
            <li>Retrieve an object from a file, a database etc&hellip;</li>
            <li>Do operations on objects (count, compute stats, etc&hellip;)</li>
            <li>Update attributes of an object</li>
            <li>Destroy an object</li>
        </ul>
        <h2>Resources</h2>
        <p><strong>Read or watch</strong>:</p>
        <ul>
            <li><a href="https://intranet.alxswe.com/rltoken/8ecCwE6veBmm3Nppw4hz5A" title="cmd module" target="_blank">cmd module</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/uEy4RftSdKypoig9NFTvCg" title="cmd module in depth" target="_blank">cmd module in depth</a></li>
            <li><strong>packages</strong> concept page</li>
            <li><a href="https://intranet.alxswe.com/rltoken/KfL9TqwdI69W6ttG6gTPPQ" title="uuid module" target="_blank">uuid module</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/1d8I3jSKgnYAtA1IZfEDpA" title="datetime" target="_blank">datetime</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/IlFiMB8UmqBG2CxA0AD3jA" title="unittest module" target="_blank">unittest module</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/C_a0EKbtvKdMcwIAuSIZng" title="args/kwargs" target="_blank">args/kwargs</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/tgNVrKKzlWgS4dfl3mQklw" title="Python test cheatsheet" target="_blank">Python test cheatsheet</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/EvcaH9uTLlauxuw03WnkOQ" title="cmd module wiki page" target="_blank">cmd module wiki page</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/begh14KQA-3ov29KvD_HvA" title="python unittest" target="_blank">python unittest</a></li>
        </ul>
        <h2>Learning Objectives</h2>
        <p>At the end of this project, you are expected to be able to&nbsp;<a href="https://intranet.alxswe.com/rltoken/uV5eZkRZ_XEqYbgPd-0CWw" title="explain to anyone" target="_blank">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
        <h3>General</h3>
        <ul>
            <li>How to create a Python package</li>
            <li>How to create a command interpreter in Python using the&nbsp;<code>cmd</code> module</li>
            <li>What is Unit testing and how to implement it in a large project</li>
            <li>How to serialize and deserialize a Class</li>
            <li>How to write and read a JSON file</li>
            <li>How to manage&nbsp;<code>datetime</code></li>
            <li>What is an&nbsp;<code>UUID</code></li>
            <li>What is&nbsp;<code>*args</code> and how to use it</li>
            <li>What is&nbsp;<code>**kwargs</code> and how to use it</li>
            <li>How to handle named arguments in a function</li>
        </ul>
        <h3>Copyright - Plagiarism</h3>
        <ul>
            <li>You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.</li>
            <li>You will not be able to meet the objectives of this or any following project by copying and pasting someone else&rsquo;s work.</li>
            <li>You are not allowed to publish any content of this project.</li>
            <li>Any form of plagiarism is strictly forbidden and will result in removal from the program.</li>
        </ul>
        <h2>Requirements</h2>
        <h3>Python Scripts</h3>
        <ul>
            <li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
            <li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
            <li>All your files should end with a new line</li>
            <li>The first line of all your files should be exactly&nbsp;<code>#!/usr/bin/python3</code></li>
            <li>A&nbsp;<code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
            <li>Your code should use the pycodestyle (version&nbsp;<code>2.8.*</code>)</li>
            <li>All your files must be executable</li>
            <li>The length of your files will be tested using&nbsp;<code>wc</code></li>
            <li>All your modules should have a documentation (<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).__doc__)&apos;</code>)</li>
            <li>All your classes should have a documentation (<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&apos;</code>)</li>
            <li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).my_function.__doc__)&apos;</code> and&nbsp;<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&apos;</code>)</li>
            <li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
        </ul>
        <h3>Python Unit Tests</h3>
        <ul>
            <li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
            <li>All your files should end with a new line</li>
            <li>All your test files should be inside a folder&nbsp;<code>tests</code></li>
            <li>You have to use the&nbsp;<a href="https://intranet.alxswe.com/rltoken/op1-rQGlw0wwwqNBsn1yaw" title="unittest module" target="_blank">unittest module</a></li>
            <li>All your test files should be python files (extension:&nbsp;<code>.py</code>)</li>
            <li>All your test files and folders should start by&nbsp;<code>test_</code></li>
            <li>Your file organization in the tests folder should be the same as your project</li>
            <li>e.g., For&nbsp;<code>models/base_model.py</code>, unit tests must be in:&nbsp;<code>tests/test_models/test_base_model.py</code></li>
            <li>e.g., For&nbsp;<code>models/user.py</code>, unit tests must be in:&nbsp;<code>tests/test_models/test_user.py</code></li>
            <li>All your tests should be executed by using this command:&nbsp;<code>python3 -m unittest discover tests</code></li>
            <li>You can also test file by file by using this command:&nbsp;<code>python3 -m unittest tests/test_models/test_base_model.py</code></li>
            <li>All your modules should have a documentation (<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).__doc__)&apos;</code>)</li>
            <li>All your classes should have a documentation (<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&apos;</code>)</li>
            <li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).my_function.__doc__)&apos;</code> and&nbsp;<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&apos;</code>)</li>
            <li>We strongly encourage you to work together on test cases, so that you don&rsquo;t miss any edge case</li>
        </ul>
        <h3>GitHub</h3>
        <p><strong>There should be one project repository per group. If you clone/fork/whatever a project repository with the same name before the second deadline, you risk a 0% score.</strong></p>
        <h2>More Info</h2>
        <h3>Execution</h3>
        <p>Your shell should work like this in interactive mode:</p>
        <pre><code>$ ./console.py
(hbnb) help

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
</code></pre>
        <p>But also in non-interactive mode: (like the Shell project in C)</p>
        <pre><code>$ echo &quot;help&quot; | ./console.py
(hbnb)

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit
(hbnb) 
$
</code></pre>
        <p>All tests should also pass in non-interactive mode:&nbsp;<code>$ echo &quot;python3 -m unittest discover tests&quot; | bash</code></p>
        <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230511%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230511T121050Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=58d28529943ee85d158c37bfecf2b825f7ab677103e4959742acc2ac818a0a74" alt=""></p>
    </div>
</div>
<div>
    <div>
        <div>
            <div>
                <h3>Video library<small>(8&nbsp;total)</small></h3>
            </div>
            <div>
                <div>
                    <div><input placeholder="Search by title" type="search" value=""></div>
                </div>
            </div>
            <div>
                <div><span title="">
                        <div>
                            <div>
                                <div><br></div>
                            </div>
                            <div>HBNB project overview</div>
                        </div>
                    </span><span title="">
                        <div>
                            <div>
                                <div><br></div>
                            </div>
                            <div>HBNB - the console</div>
                        </div>
                    </span><span title="">
                        <div>
                            <div>
                                <div><br></div>
                            </div>
                            <div>Python: Unique Identifier</div>
                        </div>
                    </span><span title="">
                        <div>
                            <div>
                                <div><br></div>
                            </div>
                            <div>Python: Unittests</div>
                        </div>
                    </span><span title="">
                        <div>
                            <div>
                                <div><br></div>
                            </div>
                            <div>Python: BaseModel and inheritance</div>
                        </div>
                    </span><span title="">
                        <div>
                            <div>
                                <div><br></div>
                            </div>
                            <div>Code consistency</div>
                        </div>
                    </span><span title="">
                        <div>
                            <div>
                                <div><br></div>
                            </div>
                            <div>Python: Modules and Packages</div>
                        </div>
                    </span><span title="">
                        <div>
                            <div>
                                <div><br></div>
                            </div>
                            <div>HBNB - storage abstraction</div>
                        </div>
                    </span></div>
            </div>
        </div>
    </div>
</div>
<h2>Tasks</h2>
<div>
    <div>
        <div>
            <h3>0. README, AUTHORS</h3>
            <div>mandatory</div>
        </div>
        <div>
            <ul>
                <li>Write a&nbsp;<code>README.md</code>:<ul>
                        <li>description of the project</li>
                        <li>description of the command interpreter:<ul>
                                <li>how to start it</li>
                                <li>how to use it</li>
                                <li>examples</li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li>You should have an&nbsp;<code>AUTHORS</code> file at the root of your repository, listing all individuals having contributed content to the repository. For format, reference&nbsp;<a href="https://intranet.alxswe.com/rltoken/_8n_z3pf5HWi1l7uv1E9iA" title="Docker's AUTHORS page" target="_blank">Docker&rsquo;s AUTHORS page</a></li>
                <li>You should use branches and pull requests on GitHub - it will help you as team to organize your work</li>
            </ul>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone</code></li>
                    <li>File:&nbsp;<code>README.md, AUTHORS</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>1. Be pycodestyle compliant!</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write beautiful code that passes the pycodestyle checks.</p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>2. Unittests</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>All your files, classes, functions must be tested with unit tests</p>
            <pre><code>guillaume@ubuntu:~/AirBnB$ python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/AirBnB$
</code></pre>
            <p><em>Note that this is just an example, the number of tests you create can be different from the above example</em>.</p>
            <p><strong>Warning:</strong></p>
            <p>Unit tests must also pass in non-interactive mode:</p>
            <pre><code>guillaume@ubuntu:~/AirBnB$ echo &quot;python3 -m unittest discover tests&quot; | bash
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/AirBnB$
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone</code></li>
                    <li>File:&nbsp;<code>tests/</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>3. BaseModel</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a class&nbsp;<code>BaseModel</code> that defines all common attributes/methods for other classes:</p>
            <ul>
                <li><code>models/base_model.py</code></li>
                <li>Public instance attributes:<ul>
                        <li><code>id</code>: string - assign with an&nbsp;<code>uuid</code> when an instance is created:<ul>
                                <li>you can use&nbsp;<code>uuid.uuid4()</code> to generate unique&nbsp;<code>id</code> but don&rsquo;t forget to convert to a string</li>
                                <li>the goal is to have unique&nbsp;<code>id</code> for each&nbsp;<code>BaseModel</code></li>
                            </ul>
                        </li>
                        <li><code>created_at</code>: datetime - assign with the current datetime when an instance is created</li>
                        <li><code>updated_at</code>: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object</li>
                    </ul>
                </li>
                <li><code>__str__</code>: should print:&nbsp;<code>[&lt;class name&gt;] (&lt;self.id&gt;) &lt;self.__dict__&gt;</code></li>
                <li>Public instance methods:<ul>
                        <li><code>save(self)</code>: updates the public instance attribute&nbsp;<code>updated_at</code> with the current datetime</li>
                        <li><code>to_dict(self)</code>: returns a dictionary containing all keys/values of&nbsp;<code>__dict__</code> of the instance:<ul>
                                <li>by using&nbsp;<code>self.__dict__</code>, only instance attributes set will be returned</li>
                                <li>a key&nbsp;<code>__class__</code> must be added to this dictionary with the class name of the object</li>
                                <li><code>created_at</code> and&nbsp;<code>updated_at</code> must be converted to string object in ISO format:<ul>
                                        <li>format:&nbsp;<code>%Y-%m-%dT%H:%M:%S.%f</code> (ex:&nbsp;<code>2017-06-14T22:31:03.285259</code>)</li>
                                        <li>you can use&nbsp;<code>isoformat()</code> of&nbsp;<code>datetime</code> object</li>
                                    </ul>
                                </li>
                                <li>This method will be the first piece of the serialization/deserialization process: create a dictionary representation with &ldquo;simple object type&rdquo; of our&nbsp;<code>BaseModel</code></li>
                            </ul>
                        </li>
                    </ul>
                </li>
            </ul>
            <pre><code>guillaume@ubuntu:~/AirBnB$ cat test_base_model.py
#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = &quot;My First Model&quot;
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print(&quot;JSON of my_model:&quot;)
for key in my_model_json.keys():
    print(&quot;\t{}: ({}) - {}&quot;.format(key, type(my_model_json[key]), my_model_json[key]))

guillaume@ubuntu:~/AirBnB$ ./test_base_model.py
[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {&apos;my_number&apos;: 89, &apos;name&apos;: &apos;My First Model&apos;, &apos;updated_at&apos;: datetime.datetime(2017, 9, 28, 21, 5, 54, 119434), &apos;id&apos;: &apos;b6a6e15c-c67d-4312-9a75-9d084935e579&apos;, &apos;created_at&apos;: datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {&apos;my_number&apos;: 89, &apos;name&apos;: &apos;My First Model&apos;, &apos;updated_at&apos;: datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), &apos;id&apos;: &apos;b6a6e15c-c67d-4312-9a75-9d084935e579&apos;, &apos;created_at&apos;: datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
{&apos;my_number&apos;: 89, &apos;name&apos;: &apos;My First Model&apos;, &apos;__class__&apos;: &apos;BaseModel&apos;, &apos;updated_at&apos;: &apos;2017-09-28T21:05:54.119572&apos;, &apos;id&apos;: &apos;b6a6e15c-c67d-4312-9a75-9d084935e579&apos;, &apos;created_at&apos;: &apos;2017-09-28T21:05:54.119427&apos;}
JSON of my_model:
    my_number: (&lt;class &apos;int&apos;&gt;) - 89
    name: (&lt;class &apos;str&apos;&gt;) - My First Model
    __class__: (&lt;class &apos;str&apos;&gt;) - BaseModel
    updated_at: (&lt;class &apos;str&apos;&gt;) - 2017-09-28T21:05:54.119572
    id: (&lt;class &apos;str&apos;&gt;) - b6a6e15c-c67d-4312-9a75-9d084935e579
    created_at: (&lt;class &apos;str&apos;&gt;) - 2017-09-28T21:05:54.119427

guillaume@ubuntu:~/AirBnB$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone</code></li>
                    <li>File:&nbsp;<code>models/base_model.py, models/__init__.py, tests/</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>4. Create BaseModel from dictionary</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Previously we created a method to generate a dictionary representation of an instance (method&nbsp;<code>to_dict()</code>).</p>
            <p>Now it&rsquo;s time to re-create an instance with this dictionary representation.</p>
            <pre><code>&lt;class &apos;BaseModel&apos;&gt; -&gt; to_dict() -&gt; &lt;class &apos;dict&apos;&gt; -&gt; &lt;class &apos;BaseModel&apos;&gt;
</code></pre>
            <p>Update&nbsp;<code>models/base_model.py</code>:</p>
            <ul>
                <li><code>__init__(self, *args, **kwargs)</code>:<ul>
                        <li>you will use&nbsp;<code>*args, **kwargs</code> arguments for the constructor of a&nbsp;<code>BaseModel</code>. (more information inside the&nbsp;<strong>AirBnB clone</strong> concept page)</li>
                        <li><code>*args</code> won&rsquo;t be used</li>
                        <li>if&nbsp;<code>kwargs</code> is not empty:<ul>
                                <li>each key of this dictionary is an attribute name (<strong>Note</strong> <code>__class__</code> from&nbsp;<code>kwargs</code> is the only one that should not be added as an attribute. See the example output, below)</li>
                                <li>each value of this dictionary is the value of this attribute name</li>
                                <li><strong>Warning</strong>:&nbsp;<code>created_at</code> and&nbsp;<code>updated_at</code> are strings in this dictionary, but inside your&nbsp;<code>BaseModel</code> instance is working with&nbsp;<code>datetime</code> object. You have to convert these strings into&nbsp;<code>datetime</code> object. Tip: you know the string format of these datetime</li>
                            </ul>
                        </li>
                        <li>otherwise:<ul>
                                <li>create&nbsp;<code>id</code> and&nbsp;<code>created_at</code> as you did previously (new instance)</li>
                            </ul>
                        </li>
                    </ul>
                </li>
            </ul>
            <pre><code>guillaume@ubuntu:~/AirBnB$ cat test_base_model_dict.py
#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = &quot;My_First_Model&quot;
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print(&quot;--&quot;)
my_model_json = my_model.to_dict()
print(my_model_json)
print(&quot;JSON of my_model:&quot;)
for key in my_model_json.keys():
    print(&quot;\t{}: ({}) - {}&quot;.format(key, type(my_model_json[key]), my_model_json[key]))

print(&quot;--&quot;)
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print(&quot;--&quot;)
print(my_model is my_new_model)

guillaume@ubuntu:~/AirBnB$ ./test_base_model_dict.py
56d43177-cc5f-4d6c-a0c1-e167f8c27337
[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {&apos;id&apos;: &apos;56d43177-cc5f-4d6c-a0c1-e167f8c27337&apos;, &apos;created_at&apos;: datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), &apos;my_number&apos;: 89, &apos;updated_at&apos;: datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), &apos;name&apos;: &apos;My_First_Model&apos;}
&lt;class &apos;datetime.datetime&apos;&gt;
--
{&apos;id&apos;: &apos;56d43177-cc5f-4d6c-a0c1-e167f8c27337&apos;, &apos;created_at&apos;: &apos;2017-09-28T21:03:54.052298&apos;, &apos;__class__&apos;: &apos;BaseModel&apos;, &apos;my_number&apos;: 89, &apos;updated_at&apos;: &apos;2017-09-28T21:03:54.052302&apos;, &apos;name&apos;: &apos;My_First_Model&apos;}
JSON of my_model:
    id: (&lt;class &apos;str&apos;&gt;) - 56d43177-cc5f-4d6c-a0c1-e167f8c27337
    created_at: (&lt;class &apos;str&apos;&gt;) - 2017-09-28T21:03:54.052298
    __class__: (&lt;class &apos;str&apos;&gt;) - BaseModel
    my_number: (&lt;class &apos;int&apos;&gt;) - 89
    updated_at: (&lt;class &apos;str&apos;&gt;) - 2017-09-28T21:03:54.052302
    name: (&lt;class &apos;str&apos;&gt;) - My_First_Model
--
56d43177-cc5f-4d6c-a0c1-e167f8c27337
[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {&apos;id&apos;: &apos;56d43177-cc5f-4d6c-a0c1-e167f8c27337&apos;, &apos;created_at&apos;: datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), &apos;my_number&apos;: 89, &apos;updated_at&apos;: datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), &apos;name&apos;: &apos;My_First_Model&apos;}
&lt;class &apos;datetime.datetime&apos;&gt;
--
False
guillaume@ubuntu:~/AirBnB$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone</code></li>
                    <li>File:&nbsp;<code>models/base_model.py, tests/</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>5. Store first object</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Now we can recreate a&nbsp;<code>BaseModel</code> from another one by using a dictionary representation:</p>
            <pre><code>&lt;class &apos;BaseModel&apos;&gt; -&gt; to_dict() -&gt; &lt;class &apos;dict&apos;&gt; -&gt; &lt;class &apos;BaseModel&apos;&gt;
</code></pre>
            <p>It&rsquo;s great but it&rsquo;s still not persistent: every time you launch the program, you don&rsquo;t restore all objects created before&hellip; The first way you will see here is to save these objects to a file.</p>
            <p>Writing the dictionary representation to a file won&rsquo;t be relevant:</p>
            <ul>
                <li>Python doesn&rsquo;t know how to convert a string to a dictionary (easily)</li>
                <li>It&rsquo;s not human readable</li>
                <li>Using this file with another program in Python or other language will be hard.</li>
            </ul>
            <p>So, you will convert the dictionary representation to a JSON string. JSON is a standard representation of a data structure. With this format, humans can read and all programming languages have a JSON reader and writer.</p>
            <p>Now the flow of serialization-deserialization will be:</p>
            <pre><code>&lt;class &apos;BaseModel&apos;&gt; -&gt; to_dict() -&gt; &lt;class &apos;dict&apos;&gt; -&gt; JSON dump -&gt; &lt;class &apos;str&apos;&gt; -&gt; FILE -&gt; &lt;class &apos;str&apos;&gt; -&gt; JSON load -&gt; &lt;class &apos;dict&apos;&gt; -&gt; &lt;class &apos;BaseModel&apos;&gt;
</code></pre>
            <p>Magic right?</p>
            <p>Terms:</p>
            <ul>
                <li><strong>simple Python data structure</strong>: Dictionaries, arrays, number and string. ex:&nbsp;<code>{ &apos;12&apos;: { &apos;numbers&apos;: [1, 2, 3], &apos;name&apos;: &quot;John&quot; } }</code></li>
                <li><strong>JSON string representation</strong>: String representing a simple data structure in JSON format. ex:&nbsp;<code>&apos;{ &quot;12&quot;: { &quot;numbers&quot;: [1, 2, 3], &quot;name&quot;: &quot;John&quot; } }&apos;</code></li>
            </ul>
            <p>Write a class&nbsp;<code>FileStorage</code> that serializes instances to a JSON file and deserializes JSON file to instances:</p>
            <ul>
                <li><code>models/engine/file_storage.py</code></li>
                <li>Private class attributes:<ul>
                        <li><code>__file_path</code>: string - path to the JSON file (ex:&nbsp;<code>file.json</code>)</li>
                        <li><code>__objects</code>: dictionary - empty but will store all objects by&nbsp;<code>&lt;class name&gt;.id</code> (ex: to store a&nbsp;<code>BaseModel</code> object with&nbsp;<code>id=12121212</code>, the key will be&nbsp;<code>BaseModel.12121212</code>)</li>
                    </ul>
                </li>
                <li>Public instance methods:<ul>
                        <li><code>all(self)</code>: returns the dictionary&nbsp;<code>__objects</code></li>
                        <li><code>new(self, obj)</code>: sets in&nbsp;<code>__objects</code> the&nbsp;<code>obj</code> with key&nbsp;<code>&lt;obj class name&gt;.id</code></li>
                        <li><code>save(self)</code>: serializes&nbsp;<code>__objects</code> to the JSON file (path:&nbsp;<code>__file_path</code>)</li>
                        <li><code>reload(self)</code>: deserializes the JSON file to&nbsp;<code>__objects</code> (only if the JSON file (<code>__file_path</code>) exists ; otherwise, do nothing. If the file doesn&rsquo;t exist, no exception should be raised)</li>
                    </ul>
                </li>
            </ul>
            <p>Update&nbsp;<code>models/__init__.py</code>: to create a unique&nbsp;<code>FileStorage</code> instance for your application</p>
            <ul>
                <li>import&nbsp;<code>file_storage.py</code></li>
                <li>create the variable&nbsp;<code>storage</code>, an instance of&nbsp;<code>FileStorage</code></li>
                <li>call&nbsp;<code>reload()</code> method on this variable</li>
            </ul>
            <p>Update&nbsp;<code>models/base_model.py</code>: to link your&nbsp;<code>BaseModel</code> to&nbsp;<code>FileStorage</code> by using the variable&nbsp;<code>storage</code></p>
            <ul>
                <li>import the variable&nbsp;<code>storage</code></li>
                <li>in the method&nbsp;<code>save(self)</code>:<ul>
                        <li>call&nbsp;<code>save(self)</code> method of&nbsp;<code>storage</code></li>
                    </ul>
                </li>
                <li><code>__init__(self, *args, **kwargs)</code>:<ul>
                        <li>if it&rsquo;s a new instance (not from a dictionary representation), add a call to the method&nbsp;<code>new(self)</code> on&nbsp;<code>storage</code></li>
                    </ul>
                </li>
            </ul>
            <pre><code>guillaume@ubuntu:~/AirBnB$ cat test_save_reload_base_model.py
#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print(&quot;-- Reloaded objects --&quot;)
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print(&quot;-- Create a new object --&quot;)
my_model = BaseModel()
my_model.name = &quot;My_First_Model&quot;
my_model.my_number = 89
my_model.save()
print(my_model)

guillaume@ubuntu:~/AirBnB$ cat file.json
cat: file.json: No such file or directory
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
-- Create a new object --
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {&apos;my_number&apos;: 89, &apos;updated_at&apos;: datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), &apos;created_at&apos;: datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), &apos;name&apos;: &apos;My_First_Model&apos;, &apos;id&apos;: &apos;ee49c413-023a-4b49-bd28-f2936c95460d&apos;}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo &quot;&quot;
{&quot;BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d&quot;: {&quot;my_number&quot;: 89, &quot;__class__&quot;: &quot;BaseModel&quot;, &quot;updated_at&quot;: &quot;2017-09-28T21:07:25.047381&quot;, &quot;created_at&quot;: &quot;2017-09-28T21:07:25.047372&quot;, &quot;name&quot;: &quot;My_First_Model&quot;, &quot;id&quot;: &quot;ee49c413-023a-4b49-bd28-f2936c95460d&quot;}}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {&apos;name&apos;: &apos;My_First_Model&apos;, &apos;id&apos;: &apos;ee49c413-023a-4b49-bd28-f2936c95460d&apos;, &apos;updated_at&apos;: datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), &apos;my_number&apos;: 89, &apos;created_at&apos;: datetime.datetime(2017, 9, 28, 21, 7, 25, 47372)}
-- Create a new object --
[BaseModel] (080cce84-c574-4230-b82a-9acb74ad5e8c) {&apos;name&apos;: &apos;My_First_Model&apos;, &apos;id&apos;: &apos;080cce84-c574-4230-b82a-9acb74ad5e8c&apos;, &apos;updated_at&apos;: datetime.datetime(2017, 9, 28, 21, 7, 51, 973308), &apos;my_number&apos;: 89, &apos;created_at&apos;: datetime.datetime(2017, 9, 28, 21, 7, 51, 973301)}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
[BaseModel] (080cce84-c574-4230-b82a-9acb74ad5e8c) {&apos;id&apos;: &apos;080cce84-c574-4230-b82a-9acb74ad5e8c&apos;, &apos;updated_at&apos;: datetime.datetime(2017, 9, 28, 21, 7, 51, 973308), &apos;created_at&apos;: datetime.datetime(2017, 9, 28, 21, 7, 51, 973301), &apos;name&apos;: &apos;My_First_Model&apos;, &apos;my_number&apos;: 89}
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {&apos;id&apos;: &apos;ee49c413-023a-4b49-bd28-f2936c95460d&apos;, &apos;updated_at&apos;: datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), &apos;created_at&apos;: datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), &apos;name&apos;: &apos;My_First_Model&apos;, &apos;my_number&apos;: 89}
-- Create a new object --
[BaseModel] (e79e744a-55d4-45a3-b74a-ca5fae74e0e2) {&apos;id&apos;: &apos;e79e744a-55d4-45a3-b74a-ca5fae74e0e2&apos;, &apos;updated_at&apos;: datetime.datetime(2017, 9, 28, 21, 8, 6, 151750), &apos;created_at&apos;: datetime.datetime(2017, 9, 28, 21, 8, 6, 151711), &apos;name&apos;: &apos;My_First_Model&apos;, &apos;my_number&apos;: 89}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo &quot;&quot;
{&quot;BaseModel.e79e744a-55d4-45a3-b74a-ca5fae74e0e2&quot;: {&quot;__class__&quot;: &quot;BaseModel&quot;, &quot;id&quot;: &quot;e79e744a-55d4-45a3-b74a-ca5fae74e0e2&quot;, &quot;updated_at&quot;: &quot;2017-09-28T21:08:06.151750&quot;, &quot;created_at&quot;: &quot;2017-09-28T21:08:06.151711&quot;, &quot;name&quot;: &quot;My_First_Model&quot;, &quot;my_number&quot;: 89}, &quot;BaseModel.080cce84-c574-4230-b82a-9acb74ad5e8c&quot;: {&quot;__class__&quot;: &quot;BaseModel&quot;, &quot;id&quot;: &quot;080cce84-c574-4230-b82a-9acb74ad5e8c&quot;, &quot;updated_at&quot;: &quot;2017-09-28T21:07:51.973308&quot;, &quot;created_at&quot;: &quot;2017-09-28T21:07:51.973301&quot;, &quot;name&quot;: &quot;My_First_Model&quot;, &quot;my_number&quot;: 89}, &quot;BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d&quot;: {&quot;__class__&quot;: &quot;BaseModel&quot;, &quot;id&quot;: &quot;ee49c413-023a-4b49-bd28-f2936c95460d&quot;, &quot;updated_at&quot;: &quot;2017-09-28T21:07:25.047381&quot;, &quot;created_at&quot;: &quot;2017-09-28T21:07:25.047372&quot;, &quot;name&quot;: &quot;My_First_Model&quot;, &quot;my_number&quot;: 89}}
guillaume@ubuntu:~/AirBnB$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone</code></li>
                    <li>File:&nbsp;<code>models/engine/file_storage.py, models/engine/__init__.py, models/__init__.py, models/base_model.py, tests/</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>6. Console 0.0.1</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a program called&nbsp;<code>console.py</code> that contains the entry point of the command interpreter:</p>
            <ul>
                <li>You must use the module&nbsp;<code>cmd</code></li>
                <li>Your class definition must be:&nbsp;<code>class HBNBCommand(cmd.Cmd):</code></li>
                <li>Your command interpreter should implement:<ul>
                        <li><code>quit</code> and&nbsp;<code>EOF</code> to exit the program</li>
                        <li><code>help</code> (this action is provided by default by&nbsp;<code>cmd</code> but you should keep it updated and documented as you work through tasks)</li>
                        <li>a custom prompt:&nbsp;<code>(hbnb)</code></li>
                        <li>an empty line +&nbsp;<code>ENTER</code> shouldn&rsquo;t execute anything</li>
                    </ul>
                </li>
                <li>Your code should not be executed when imported</li>
            </ul>
            <p><strong>Warning:</strong></p>
            <p>You should end your file with:</p>
            <pre><code>if __name__ == &apos;__main__&apos;:
    HBNBCommand().cmdloop()
</code></pre>
            <p>to make your program executable except when imported. Please don&rsquo;t add anything around - the Checker won&rsquo;t like it otherwise</p>
            <pre><code>guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) help

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit

(hbnb) 
(hbnb) help quit
Quit command to exit the program

(hbnb) 
(hbnb) 
(hbnb) quit 
guillaume@ubuntu:~/AirBnB$ 
</code></pre>
            <p><strong>No unittests needed</strong></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone</code></li>
                    <li>File:&nbsp;<code>console.py</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>7. Console 0.1</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Update your command interpreter (<code>console.py</code>) to have these commands:</p>
            <ul>
                <li><code>create</code>: Creates a new instance of&nbsp;<code>BaseModel</code>, saves it (to the JSON file) and prints the&nbsp;<code>id</code>. Ex:&nbsp;<code>$ create BaseModel</code>
                    <ul>
                        <li>If the class name is missing, print&nbsp;<code>** class name missing **</code> (ex:&nbsp;<code>$ create</code>)</li>
                        <li>If the class name doesn&rsquo;t exist, print&nbsp;<code>** class doesn&apos;t exist **</code> (ex:&nbsp;<code>$ create MyModel</code>)</li>
                    </ul>
                </li>
                <li><code>show</code>: Prints the string representation of an instance based on the class name and&nbsp;<code>id</code>. Ex:&nbsp;<code>$ show BaseModel 1234-1234-1234</code>.<ul>
                        <li>If the class name is missing, print&nbsp;<code>** class name missing **</code> (ex:&nbsp;<code>$ show</code>)</li>
                        <li>If the class name doesn&rsquo;t exist, print&nbsp;<code>** class doesn&apos;t exist **</code> (ex:&nbsp;<code>$ show MyModel</code>)</li>
                        <li>If the&nbsp;<code>id</code> is missing, print&nbsp;<code>** instance id missing **</code> (ex:&nbsp;<code>$ show BaseModel</code>)</li>
                        <li>If the instance of the class name doesn&rsquo;t exist for the&nbsp;<code>id</code>, print&nbsp;<code>** no instance found **</code> (ex:&nbsp;<code>$ show BaseModel 121212</code>)</li>
                    </ul>
                </li>
                <li><code>destroy</code>: Deletes an instance based on the class name and&nbsp;<code>id</code> (save the change into the JSON file). Ex:&nbsp;<code>$ destroy BaseModel 1234-1234-1234</code>.<ul>
                        <li>If the class name is missing, print&nbsp;<code>** class name missing **</code> (ex:&nbsp;<code>$ destroy</code>)</li>
                        <li>If the class name doesn&rsquo;t exist, print&nbsp;<code>** class doesn&apos;t exist ** (ex:</code>$ destroy MyModel<code>)</code></li>
                        <li>If the&nbsp;<code>id</code> is missing, print&nbsp;<code>** instance id missing **</code> (ex:&nbsp;<code>$ destroy BaseModel</code>)</li>
                        <li>If the instance of the class name doesn&rsquo;t exist for the&nbsp;<code>id</code>, print&nbsp;<code>** no instance found **</code> (ex:&nbsp;<code>$ destroy BaseModel 121212</code>)</li>
                    </ul>
                </li>
                <li><code>all</code>: Prints all string representation of all instances based or not on the class name. Ex:&nbsp;<code>$ all BaseModel</code> or&nbsp;<code>$ all</code>.<ul>
                        <li>The printed result must be a list of strings (like the example below)</li>
                        <li>If the class name doesn&rsquo;t exist, print&nbsp;<code>** class doesn&apos;t exist **</code> (ex:&nbsp;<code>$ all MyModel</code>)</li>
                    </ul>
                </li>
                <li><code>update</code>: Updates an instance based on the class name and&nbsp;<code>id</code> by adding or updating attribute (save the change into the JSON file). Ex:&nbsp;<code>$ update BaseModel 1234-1234-1234 email &quot;aibnb@mail.com&quot;</code>.<ul>
                        <li>Usage:&nbsp;<code>update &lt;class name&gt; &lt;id&gt; &lt;attribute name&gt; &quot;&lt;attribute value&gt;&quot;</code></li>
                        <li>Only one attribute can be updated at the time</li>
                        <li>You can assume the attribute name is valid (exists for this model)</li>
                        <li>The attribute value must be casted to the attribute type</li>
                        <li>If the class name is missing, print&nbsp;<code>** class name missing **</code> (ex:&nbsp;<code>$ update</code>)</li>
                        <li>If the class name doesn&rsquo;t exist, print&nbsp;<code>** class doesn&apos;t exist **</code> (ex:&nbsp;<code>$ update MyModel</code>)</li>
                        <li>If the&nbsp;<code>id</code> is missing, print&nbsp;<code>** instance id missing **</code> (ex:&nbsp;<code>$ update BaseModel</code>)</li>
                        <li>If the instance of the class name doesn&rsquo;t exist for the&nbsp;<code>id</code>, print&nbsp;<code>** no instance found **</code> (ex:&nbsp;<code>$ update BaseModel 121212</code>)</li>
                        <li>If the attribute name is missing, print&nbsp;<code>** attribute name missing **</code> (ex:&nbsp;<code>$ update BaseModel existing-id</code>)</li>
                        <li>If the value for the attribute name doesn&rsquo;t exist, print&nbsp;<code>** value missing **</code> (ex:&nbsp;<code>$ update BaseModel existing-id first_name</code>)</li>
                        <li>All other arguments should not be used (Ex:&nbsp;<code>$ update BaseModel 1234-1234-1234 email &quot;aibnb@mail.com&quot; first_name &quot;Betty&quot;</code> =&nbsp;<code>$ update BaseModel 1234-1234-1234 email &quot;aibnb@mail.com&quot;</code>)</li>
                        <li><code>id</code>,&nbsp;<code>created_at</code> and&nbsp;<code>updated_at</code> cant&rsquo; be updated. You can assume they won&rsquo;t be passed in the&nbsp;<code>update</code> command</li>
                        <li>Only &ldquo;simple&rdquo; arguments can be updated: string, integer and float. You can assume nobody will try to update list of ids or datetime</li>
                    </ul>
                </li>
            </ul>
            <p>Let&rsquo;s add some rules:</p>
            <ul>
                <li>You can assume arguments are always in the right order</li>
                <li>Each arguments are separated by a space</li>
                <li>A string argument with a space must be between double quote</li>
                <li>The error management starts from the first argument to the last one</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) all MyModel
** class doesn&apos;t exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel My_First_Model
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
[&quot;[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {&apos;created_at&apos;: datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), &apos;id&apos;: &apos;49faff9a-6318-451f-87b6-910505c55907&apos;, &apos;updated_at&apos;: datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}&quot;]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {&apos;created_at&apos;: datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), &apos;id&apos;: &apos;49faff9a-6318-451f-87b6-910505c55907&apos;, &apos;updated_at&apos;: datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name &quot;Betty&quot;
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {&apos;first_name&apos;: &apos;Betty&apos;, &apos;id&apos;: &apos;49faff9a-6318-451f-87b6-910505c55907&apos;, &apos;created_at&apos;: datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), &apos;updated_at&apos;: datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
[&quot;[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {&apos;id&apos;: &apos;2dd6ef5c-467c-4f82-9521-a772ea7d84e9&apos;, &apos;created_at&apos;: datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), &apos;updated_at&apos;: datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}&quot;, &quot;[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {&apos;first_name&apos;: &apos;Betty&apos;, &apos;id&apos;: &apos;49faff9a-6318-451f-87b6-910505c55907&apos;, &apos;created_at&apos;: datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), &apos;updated_at&apos;: datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}&quot;]
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb) 
</code></pre>
            <p><strong>No unittests needed</strong></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone</code></li>
                    <li>File:&nbsp;<code>console.py</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>8. First User</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a class&nbsp;<code>User</code> that inherits from&nbsp;<code>BaseModel</code>:</p>
            <ul>
                <li><code>models/user.py</code></li>
                <li>Public class attributes:<ul>
                        <li><code>email</code>: string - empty string</li>
                        <li><code>password</code>: string - empty string</li>
                        <li><code>first_name</code>: string - empty string</li>
                        <li><code>last_name</code>: string - empty string</li>
                    </ul>
                </li>
            </ul>
            <p>Update&nbsp;<code>FileStorage</code> to manage correctly serialization and deserialization of&nbsp;<code>User</code>.</p>
            <p>Update your command interpreter (<code>console.py</code>) to allow&nbsp;<code>show</code>,&nbsp;<code>create</code>,&nbsp;<code>destroy</code>,&nbsp;<code>update</code> and&nbsp;<code>all</code> used with&nbsp;<code>User</code>.</p>
            <pre><code>guillaume@ubuntu:~/AirBnB$ cat test_save_reload_user.py
#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User

all_objs = storage.all()
print(&quot;-- Reloaded objects --&quot;)
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print(&quot;-- Create a new User --&quot;)
my_user = User()
my_user.first_name = &quot;Betty&quot;
my_user.last_name = &quot;Bar&quot;
my_user.email = &quot;airbnb@mail.com&quot;
my_user.password = &quot;root&quot;
my_user.save()
print(my_user)

print(&quot;-- Create a new User 2 --&quot;)
my_user2 = User()
my_user2.first_name = &quot;John&quot;
my_user2.email = &quot;airbnb2@mail.com&quot;
my_user2.password = &quot;root&quot;
my_user2.save()
print(my_user2)

guillaume@ubuntu:~/AirBnB$ cat file.json ; echo &quot;&quot;
{&quot;BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4&quot;: {&quot;__class__&quot;: &quot;BaseModel&quot;, &quot;id&quot;: &quot;2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4&quot;, &quot;updated_at&quot;: &quot;2017-09-28T21:11:14.333862&quot;, &quot;created_at&quot;: &quot;2017-09-28T21:11:14.333852&quot;}, &quot;BaseModel.a42ee380-c959-450e-ad29-c840a898cfce&quot;: {&quot;__class__&quot;: &quot;BaseModel&quot;, &quot;id&quot;: &quot;a42ee380-c959-450e-ad29-c840a898cfce&quot;, &quot;updated_at&quot;: &quot;2017-09-28T21:11:15.504296&quot;, &quot;created_at&quot;: &quot;2017-09-28T21:11:15.504287&quot;}, &quot;BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f&quot;: {&quot;__class__&quot;: &quot;BaseModel&quot;, &quot;id&quot;: &quot;af9b4cbd-2ce1-4e6e-8259-f578097dd15f&quot;, &quot;updated_at&quot;: &quot;2017-09-28T21:11:12.971544&quot;, &quot;created_at&quot;: &quot;2017-09-28T21:11:12.971521&quot;}, &quot;BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba&quot;: {&quot;__class__&quot;: &quot;BaseModel&quot;, &quot;id&quot;: &quot;38a22b25-ae9c-4fa9-9f94-59b3eb51bfba&quot;, &quot;updated_at&quot;: &quot;2017-09-28T21:11:13.753347&quot;, &quot;created_at&quot;: &quot;2017-09-28T21:11:13.753337&quot;}, &quot;BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4&quot;: {&quot;__class__&quot;: &quot;BaseModel&quot;, &quot;id&quot;: &quot;9bf17966-b092-4996-bd33-26a5353cccb4&quot;, &quot;updated_at&quot;: &quot;2017-09-28T21:11:14.963058&quot;, &quot;created_at&quot;: &quot;2017-09-28T21:11:14.963049&quot;}}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_user.py
-- Reloaded objects --
[BaseModel] (38a22b25-ae9c-4fa9-9f94-59b3eb51bfba) {&apos;id&apos;: &apos;38a22b25-ae9c-4fa9-9f94-59b3eb51bfba&apos;, &apos;created_at&apos;: datetime.datetime(2017, 9, 28, 21, 11, 13, 753337), &apos;updated_at&apos;: datetime.datetime(2017, 9, 28, 21, 11, 13, 753347)}
[BaseModel] (9bf17966-b092-4996-bd33-26a5353cccb4) {&apos;id&apos;: &apos;9bf17966-b092-4996-bd33-26a5353cccb4&apos;, &apos;created_at&apos;: datetime.datetime(2017, 9, 28, 21, 11, 14, 963049), &apos;updated_at&apos;: datetime.datetime(2017, 9, 28, 21, 11, 14, 963058)}
[BaseModel] (2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4) {&apos;id&apos;: &apos;2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4&apos;, &apos;created_at&apos;: datetime.datetime(2017, 9, 28, 21, 11, 14, 333852), &apos;updated_at&apos;: datetime.datetime(2017, 9, 28, 21, 11, 14, 333862)}
[BaseModel] (a42ee380-c959-450e-ad29-c840a898cfce) {&apos;id&apos;: &apos;a42ee380-c959-450e-ad29-c840a898cfce&apos;, &apos;created_at&apos;: datetime.datetime(2017, 9, 28, 21, 11, 15, 504287), &apos;updated_at&apos;: datetime.datetime(2017, 9, 28, 21, 11, 15, 504296)}
[BaseModel] (af9b4cbd-2ce1-4e6e-8259-f578097dd15f) {&apos;id&apos;: &apos;af9b4cbd-2ce1-4e6e-8259-f578097dd15f&apos;, &apos;created_at&apos;: datetime.datetime(2017, 9, 28, 21, 11, 12, 971521), &apos;updated_at&apos;: datetime.datetime(2017, 9, 28, 21, 11, 12, 971544)}
-- Create a new User --
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {&apos;id&apos;: &apos;38f22813-2753-4d42-b37c-57a17f1e4f88&apos;, &apos;created_at&apos;: datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), &apos;updated_at&apos;: datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), &apos;email&apos;: &apos;airbnb@mail.com&apos;, &apos;first_name&apos;: &apos;Betty&apos;, &apos;last_name&apos;: &apos;Bar&apos;, &apos;password&apos;: &apos;root&apos;}
-- Create a new User 2 --
[User] (d0ef8146-4664-4de5-8e89-096d667b728e) {&apos;id&apos;: &apos;d0ef8146-4664-4de5-8e89-096d667b728e&apos;, &apos;created_at&apos;: datetime.datetime(2017, 9, 28, 21, 11, 42, 848280), &apos;updated_at&apos;: datetime.datetime(2017, 9, 28, 21, 11, 42, 848294), &apos;email&apos;: &apos;airbnb2@mail.com&apos;, &apos;first_name&apos;: &apos;John&apos;, &apos;password&apos;: &apos;root&apos;}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo &quot;&quot;
{&quot;BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f&quot;: {&quot;id&quot;: &quot;af9b4cbd-2ce1-4e6e-8259-f578097dd15f&quot;, &quot;updated_at&quot;: &quot;2017-09-28T21:11:12.971544&quot;, &quot;created_at&quot;: &quot;2017-09-28T21:11:12.971521&quot;, &quot;__class__&quot;: &quot;BaseModel&quot;}, &quot;BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba&quot;: {&quot;id&quot;: &quot;38a22b25-ae9c-4fa9-9f94-59b3eb51bfba&quot;, &quot;updated_at&quot;: &quot;2017-09-28T21:11:13.753347&quot;, &quot;created_at&quot;: &quot;2017-09-28T21:11:13.753337&quot;, &quot;__class__&quot;: &quot;BaseModel&quot;}, &quot;BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4&quot;: {&quot;id&quot;: &quot;9bf17966-b092-4996-bd33-26a5353cccb4&quot;, &quot;updated_at&quot;: &quot;2017-09-28T21:11:14.963058&quot;, &quot;created_at&quot;: &quot;2017-09-28T21:11:14.963049&quot;, &quot;__class__&quot;: &quot;BaseModel&quot;}, &quot;BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4&quot;: {&quot;id&quot;: &quot;2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4&quot;, &quot;updated_at&quot;: &quot;2017-09-28T21:11:14.333862&quot;, &quot;created_at&quot;: &quot;2017-09-28T21:11:14.333852&quot;, &quot;__class__&quot;: &quot;BaseModel&quot;}, &quot;BaseModel.a42ee380-c959-450e-ad29-c840a898cfce&quot;: {&quot;id&quot;: &quot;a42ee380-c959-450e-ad29-c840a898cfce&quot;, &quot;updated_at&quot;: &quot;2017-09-28T21:11:15.504296&quot;, &quot;created_at&quot;: &quot;2017-09-28T21:11:15.504287&quot;, &quot;__class__&quot;: &quot;BaseModel&quot;}, &quot;User.38f22813-2753-4d42-b37c-57a17f1e4f88&quot;: {&quot;id&quot;: &quot;38f22813-2753-4d42-b37c-57a17f1e4f88&quot;, &quot;created_at&quot;: &quot;2017-09-28T21:11:42.848279&quot;, &quot;updated_at&quot;: &quot;2017-09-28T21:11:42.848291&quot;, &quot;email&quot;: &quot;airbnb@mail.com&quot;, &quot;first_name&quot;: &quot;Betty&quot;, &quot;__class__&quot;: &quot;User&quot;, &quot;last_name&quot;: &quot;Bar&quot;, &quot;password&quot;: &quot;root&quot;}, &quot;User.d0ef8146-4664-4de5-8e89-096d667b728e&quot;: {&quot;id&quot;: &quot;d0ef8146-4664-4de5-8e89-096d667b728e&quot;, &quot;created_at&quot;: &quot;2017-09-28T21:11:42.848280&quot;, &quot;updated_at&quot;: &quot;2017-09-28T21:11:42.848294&quot;, &quot;email&quot;: &quot;airbnb_2@mail.com&quot;, &quot;first_name&quot;: &quot;John&quot;, &quot;__class__&quot;: &quot;User&quot;, &quot;password&quot;: &quot;root&quot;}}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_user.py
-- Reloaded objects --
[BaseModel] (af9b4cbd-2ce1-4e6e-8259-f578097dd15f) {&apos;updated_at&apos;: datetime.datetime(2017, 9, 28, 21, 11, 12, 971544), &apos;id&apos;: &apos;af9b4cbd-2ce1-4e6e-8259-f578097dd15f&apos;, &apos;created_at&apos;: datetime.datetime(2017, 9, 28, 21, 11, 12, 971521)}
[BaseModel] (2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4) {&apos;updated_at&apos;: datetime.datetime(2017, 9, 28, 21, 11, 14, 333862), &apos;id&apos;: &apos;2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4&apos;, &apos;created_at&apos;: datetime.datetime(2017, 9, 28, 21, 11, 14, 333852)}
[BaseModel] (9bf17966-b092-4996-bd33-26a5353cccb4) {&apos;updated_at&apos;: datetime.datetime(2017, 9, 28, 21, 11, 14, 963058), &apos;id&apos;: &apos;9bf17966-b092-4996-bd33-26a5353cccb4&apos;, &apos;created_at&apos;: datetime.datetime(2017, 9, 28, 21, 11, 14, 963049)}
[BaseModel] (a42ee380-c959-450e-ad29-c840a898cfce) {&apos;updated_at&apos;: datetime.datetime(2017, 9, 28, 21, 11, 15, 504296), &apos;id&apos;: &apos;a42ee380-c959-450e-ad29-c840a898cfce&apos;, &apos;created_at&apos;: datetime.datetime(2017, 9, 28, 21, 11, 15, 504287)}
[BaseModel] (38a22b25-ae9c-4fa9-9f94-59b3eb51bfba) {&apos;updated_at&apos;: datetime.datetime(2017, 9, 28, 21, 11, 13, 753347), &apos;id&apos;: &apos;38a22b25-ae9c-4fa9-9f94-59b3eb51bfba&apos;, &apos;created_at&apos;: datetime.datetime(2017, 9, 28, 21, 11, 13, 753337)}
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {&apos;password&apos;: &apos;63a9f0ea7bb98050796b649e85481845&apos;, &apos;created_at&apos;: datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), &apos;email&apos;: &apos;airbnb@mail.com&apos;, &apos;updated_at&apos;: datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), &apos;last_name&apos;: &apos;Bar&apos;, &apos;id&apos;: &apos;38f22813-2753-4d42-b37c-57a17f1e4f88&apos;, &apos;first_name&apos;: &apos;Betty&apos;}
[User] (d0ef8146-4664-4de5-8e89-096d667b728e) {&apos;password&apos;: &apos;63a9f0ea7bb98050796b649e85481845&apos;, &apos;created_at&apos;: datetime.datetime(2017, 9, 28, 21, 11, 42, 848280), &apos;email&apos;: &apos;airbnb_2@mail.com&apos;, &apos;updated_at&apos;: datetime.datetime(2017, 9, 28, 21, 11, 42, 848294), &apos;id&apos;: &apos;d0ef8146-4664-4de5-8e89-096d667b728e&apos;, &apos;first_name&apos;: &apos;John&apos;}
-- Create a new User --
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {&apos;password&apos;: &apos;root&apos;, &apos;created_at&apos;: datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), &apos;email&apos;: &apos;airbnb@mail.com&apos;, &apos;updated_at&apos;: datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), &apos;last_name&apos;: &apos;Bar&apos;, &apos;id&apos;: &apos;246c227a-d5c1-403d-9bc7-6a47bb9f0f68&apos;, &apos;first_name&apos;: &apos;Betty&apos;}
-- Create a new User 2 --
[User] (fce12f8a-fdb6-439a-afe8-2881754de71c) {&apos;password&apos;: &apos;root&apos;, &apos;created_at&apos;: datetime.datetime(2017, 9, 28, 21, 12, 19, 611354), &apos;email&apos;: &apos;airbnb_2@mail.com&apos;, &apos;updated_at&apos;: datetime.datetime(2017, 9, 28, 21, 12, 19, 611368), &apos;id&apos;: &apos;fce12f8a-fdb6-439a-afe8-2881754de71c&apos;, &apos;first_name&apos;: &apos;John&apos;}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo &quot;&quot;
{&quot;BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f&quot;: {&quot;updated_at&quot;: &quot;2017-09-28T21:11:12.971544&quot;, &quot;__class__&quot;: &quot;BaseModel&quot;, &quot;id&quot;: &quot;af9b4cbd-2ce1-4e6e-8259-f578097dd15f&quot;, &quot;created_at&quot;: &quot;2017-09-28T21:11:12.971521&quot;}, &quot;User.38f22813-2753-4d42-b37c-57a17f1e4f88&quot;: {&quot;password&quot;: &quot;63a9f0ea7bb98050796b649e85481845&quot;, &quot;created_at&quot;: &quot;2017-09-28T21:11:42.848279&quot;, &quot;email&quot;: &quot;airbnb@mail.com&quot;, &quot;id&quot;: &quot;38f22813-2753-4d42-b37c-57a17f1e4f88&quot;, &quot;last_name&quot;: &quot;Bar&quot;, &quot;updated_at&quot;: &quot;2017-09-28T21:11:42.848291&quot;, &quot;first_name&quot;: &quot;Betty&quot;, &quot;__class__&quot;: &quot;User&quot;}, &quot;User.d0ef8146-4664-4de5-8e89-096d667b728e&quot;: {&quot;password&quot;: &quot;63a9f0ea7bb98050796b649e85481845&quot;, &quot;created_at&quot;: &quot;2017-09-28T21:11:42.848280&quot;, &quot;email&quot;: &quot;airbnb_2@mail.com&quot;, &quot;id&quot;: &quot;d0ef8146-4664-4de5-8e89-096d667b728e&quot;, &quot;updated_at&quot;: &quot;2017-09-28T21:11:42.848294&quot;, &quot;first_name&quot;: &quot;John&quot;, &quot;__class__&quot;: &quot;User&quot;}, &quot;BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4&quot;: {&quot;updated_at&quot;: &quot;2017-09-28T21:11:14.963058&quot;, &quot;__class__&quot;: &quot;BaseModel&quot;, &quot;id&quot;: &quot;9bf17966-b092-4996-bd33-26a5353cccb4&quot;, &quot;created_at&quot;: &quot;2017-09-28T21:11:14.963049&quot;}, &quot;BaseModel.a42ee380-c959-450e-ad29-c840a898cfce&quot;: {&quot;updated_at&quot;: &quot;2017-09-28T21:11:15.504296&quot;, &quot;__class__&quot;: &quot;BaseModel&quot;, &quot;id&quot;: &quot;a42ee380-c959-450e-ad29-c840a898cfce&quot;, &quot;created_at&quot;: &quot;2017-09-28T21:11:15.504287&quot;}, &quot;BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba&quot;: {&quot;updated_at&quot;: &quot;2017-09-28T21:11:13.753347&quot;, &quot;__class__&quot;: &quot;BaseModel&quot;, &quot;id&quot;: &quot;38a22b25-ae9c-4fa9-9f94-59b3eb51bfba&quot;, &quot;created_at&quot;: &quot;2017-09-28T21:11:13.753337&quot;}, &quot;BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4&quot;: {&quot;updated_at&quot;: &quot;2017-09-28T21:11:14.333862&quot;, &quot;__class__&quot;: &quot;BaseModel&quot;, &quot;id&quot;: &quot;2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4&quot;, &quot;created_at&quot;: &quot;2017-09-28T21:11:14.333852&quot;}, &quot;User.246c227a-d5c1-403d-9bc7-6a47bb9f0f68&quot;: {&quot;password&quot;: &quot;root&quot;, &quot;created_at&quot;: &quot;2017-09-28T21:12:19.611352&quot;, &quot;email&quot;: &quot;airbnb@mail.com&quot;, &quot;id&quot;: &quot;246c227a-d5c1-403d-9bc7-6a47bb9f0f68&quot;, &quot;last_name&quot;: &quot;Bar&quot;, &quot;updated_at&quot;: &quot;2017-09-28T21:12:19.611363&quot;, &quot;first_name&quot;: &quot;Betty&quot;, &quot;__class__&quot;: &quot;User&quot;}, &quot;User.fce12f8a-fdb6-439a-afe8-2881754de71c&quot;: {&quot;password&quot;: &quot;root&quot;, &quot;created_at&quot;: &quot;2017-09-28T21:12:19.611354&quot;, &quot;email&quot;: &quot;airbnb_2@mail.com&quot;, &quot;id&quot;: &quot;fce12f8a-fdb6-439a-afe8-2881754de71c&quot;, &quot;updated_at&quot;: &quot;2017-09-28T21:12:19.611368&quot;, &quot;first_name&quot;: &quot;John&quot;, &quot;__class__&quot;: &quot;User&quot;}}
guillaume@ubuntu:~/AirBnB$ 
</code></pre>
            <p><strong>No unittests needed for the console</strong></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone</code></li>
                    <li>File:&nbsp;<code>models/user.py, models/engine/file_storage.py, console.py, tests/</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>9. More classes!</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write all those classes that inherit from&nbsp;<code>BaseModel</code>:</p>
            <ul>
                <li><code>State</code> (<code>models/state.py</code>):<ul>
                        <li>Public class attributes:<ul>
                                <li><code>name</code>: string - empty string</li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li><code>City</code> (<code>models/city.py</code>):<ul>
                        <li>Public class attributes:<ul>
                                <li><code>state_id</code>: string - empty string: it will be the&nbsp;<code>State.id</code></li>
                                <li><code>name</code>: string - empty string</li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li><code>Amenity</code> (<code>models/amenity.py</code>):<ul>
                        <li>Public class attributes:<ul>
                                <li><code>name</code>: string - empty string</li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li><code>Place</code> (<code>models/place.py</code>):<ul>
                        <li>Public class attributes:<ul>
                                <li><code>city_id</code>: string - empty string: it will be the&nbsp;<code>City.id</code></li>
                                <li><code>user_id</code>: string - empty string: it will be the&nbsp;<code>User.id</code></li>
                                <li><code>name</code>: string - empty string</li>
                                <li><code>description</code>: string - empty string</li>
                                <li><code>number_rooms</code>: integer - 0</li>
                                <li><code>number_bathrooms</code>: integer - 0</li>
                                <li><code>max_guest</code>: integer - 0</li>
                                <li><code>price_by_night</code>: integer - 0</li>
                                <li><code>latitude</code>: float - 0.0</li>
                                <li><code>longitude</code>: float - 0.0</li>
                                <li><code>amenity_ids</code>: list of string - empty list: it will be the list of&nbsp;<code>Amenity.id</code> later</li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li><code>Review</code> (<code>models/review.py</code>):<ul>
                        <li>Public class attributes:<ul>
                                <li><code>place_id</code>: string - empty string: it will be the&nbsp;<code>Place.id</code></li>
                                <li><code>user_id</code>: string - empty string: it will be the&nbsp;<code>User.id</code></li>
                                <li><code>text</code>: string - empty string</li>
                            </ul>
                        </li>
                    </ul>
                </li>
            </ul>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone</code></li>
                    <li>File:&nbsp;<code>models/state.py, models/city.py, models/amenity.py, models/place.py, models/review.py, tests/</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>10. Console 1.0</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Update&nbsp;<code>FileStorage</code> to manage correctly serialization and deserialization of all our new classes:&nbsp;<code>Place</code>,&nbsp;<code>State</code>,&nbsp;<code>City</code>,&nbsp;<code>Amenity</code> and&nbsp;<code>Review</code></p>
            <p>Update your command interpreter (<code>console.py</code>) to allow those actions:&nbsp;<code>show</code>,&nbsp;<code>create</code>,&nbsp;<code>destroy</code>,&nbsp;<code>update</code> and&nbsp;<code>all</code> with all classes created previously.</p>
            <p>Enjoy your first console!</p>
            <p><strong>No unittests needed for the console</strong></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone</code></li>
                    <li>File:&nbsp;<code>console.py, models/engine/file_storage.py, tests/</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>11. All instances by class name</h3>
            <div>#advanced</div>
        </div>
        <div>
            <p>Update your command interpreter (<code>console.py</code>) to retrieve all instances of a class by using:&nbsp;<code>&lt;class name&gt;.all()</code>.</p>
            <pre><code>guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.all()
[[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {&apos;first_name&apos;: &apos;Betty&apos;, &apos;last_name&apos;: &apos;Bar&apos;, &apos;created_at&apos;: datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), &apos;updated_at&apos;: datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), &apos;password&apos;: &apos;63a9f0ea7bb98050796b649e85481845&apos;, &apos;email&apos;: &apos;airbnb@mail.com&apos;, &apos;id&apos;: &apos;246c227a-d5c1-403d-9bc7-6a47bb9f0f68&apos;}, [User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {&apos;first_name&apos;: &apos;Betty&apos;, &apos;last_name&apos;: &apos;Bar&apos;, &apos;created_at&apos;: datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), &apos;updated_at&apos;: datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), &apos;password&apos;: &apos;b9be11166d72e9e3ae7fd407165e4bd2&apos;, &apos;email&apos;: &apos;airbnb@mail.com&apos;, &apos;id&apos;: &apos;38f22813-2753-4d42-b37c-57a17f1e4f88&apos;}]
(hbnb) 
</code></pre>
            <p><strong>No unittests needed</strong></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone</code></li>
                    <li>File:&nbsp;<code>console.py</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>12. Count instances</h3>
            <div>#advanced</div>
        </div>
        <div>
            <p>Update your command interpreter (<code>console.py</code>) to retrieve the number of instances of a class:&nbsp;<code>&lt;class name&gt;.count()</code>.</p>
            <pre><code>guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.count()
2
(hbnb) 
</code></pre>
            <p><strong>No unittests needed</strong></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone</code></li>
                    <li>File:&nbsp;<code>console.py</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>13. Show</h3>
            <div>#advanced</div>
        </div>
        <div>
            <p>Update your command interpreter (<code>console.py</code>) to retrieve an instance based on its ID:&nbsp;<code>&lt;class name&gt;.show(&lt;id&gt;)</code>.</p>
            <p>Errors management must be the same as previously.</p>
            <pre><code>guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.show(&quot;246c227a-d5c1-403d-9bc7-6a47bb9f0f68&quot;)
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {&apos;first_name&apos;: &apos;Betty&apos;, &apos;last_name&apos;: &apos;Bar&apos;, &apos;created_at&apos;: datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), &apos;updated_at&apos;: datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), &apos;password&apos;: &apos;63a9f0ea7bb98050796b649e85481845&apos;, &apos;email&apos;: &apos;airbnb@mail.com&apos;, &apos;id&apos;: &apos;246c227a-d5c1-403d-9bc7-6a47bb9f0f68&apos;}
(hbnb) User.show(&quot;Bar&quot;)
** no instance found **
(hbnb) 
</code></pre>
            <p><strong>No unittests needed</strong></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone</code></li>
                    <li>File:&nbsp;<code>console.py</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>14. Destroy</h3>
            <div>#advanced</div>
        </div>
        <div>
            <p>Update your command interpreter (<code>console.py</code>) to destroy an instance based on his ID:&nbsp;<code>&lt;class name&gt;.destroy(&lt;id&gt;)</code>.</p>
            <p>Errors management must be the same as previously.</p>
            <pre><code>guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.count()
2
(hbnb) User.destroy(&quot;246c227a-d5c1-403d-9bc7-6a47bb9f0f68&quot;)
(hbnb) User.count()
1
(hbnb) User.destroy(&quot;Bar&quot;)
** no instance found **
(hbnb) 
</code></pre>
            <p><strong>No unittests needed</strong></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone</code></li>
                    <li>File:&nbsp;<code>console.py</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>15. Update</h3>
            <div>#advanced</div>
        </div>
        <div>
            <p>Update your command interpreter (<code>console.py</code>) to update an instance based on his ID:&nbsp;<code>&lt;class name&gt;.update(&lt;id&gt;, &lt;attribute name&gt;, &lt;attribute value&gt;)</code>.</p>
            <p>Errors management must be the same as previously.</p>
            <pre><code>guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.show(&quot;38f22813-2753-4d42-b37c-57a17f1e4f88&quot;)
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {&apos;first_name&apos;: &apos;Betty&apos;, &apos;last_name&apos;: &apos;Bar&apos;, &apos;created_at&apos;: datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), &apos;updated_at&apos;: datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), &apos;password&apos;: &apos;b9be11166d72e9e3ae7fd407165e4bd2&apos;, &apos;email&apos;: &apos;airbnb@mail.com&apos;, &apos;id&apos;: &apos;38f22813-2753-4d42-b37c-57a17f1e4f88&apos;}
(hbnb)
(hbnb) User.update(&quot;38f22813-2753-4d42-b37c-57a17f1e4f88&quot;, &quot;first_name&quot;, &quot;John&quot;)
(hbnb) User.update(&quot;38f22813-2753-4d42-b37c-57a17f1e4f88&quot;, &quot;age&quot;, 89)
(hbnb)
(hbnb) User.show(&quot;38f22813-2753-4d42-b37c-57a17f1e4f88&quot;)
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {&apos;age&apos;: 89, &apos;first_name&apos;: &apos;John&apos;, &apos;last_name&apos;: &apos;Bar&apos;, &apos;created_at&apos;: datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), &apos;updated_at&apos;: datetime.datetime(2017, 9, 28, 21, 15, 32, 299055), &apos;password&apos;: &apos;b9be11166d72e9e3ae7fd407165e4bd2&apos;, &apos;email&apos;: &apos;airbnb@mail.com&apos;, &apos;id&apos;: &apos;38f22813-2753-4d42-b37c-57a17f1e4f88&apos;}
(hbnb) 
</code></pre>
            <p><strong>No unittests needed</strong></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone</code></li>
                    <li>File:&nbsp;<code>console.py</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>16. Update from dictionary</h3>
            <div>#advanced</div>
        </div>
        <div>
            <p>Update your command interpreter (<code>console.py</code>) to update an instance based on his ID with a dictionary:&nbsp;<code>&lt;class name&gt;.update(&lt;id&gt;, &lt;dictionary representation&gt;)</code>.</p>
            <p>Errors management must be the same as previously.</p>
            <pre><code>guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.show(&quot;38f22813-2753-4d42-b37c-57a17f1e4f88&quot;)
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {&apos;age&apos;: 23, &apos;first_name&apos;: &apos;Bob&apos;, &apos;last_name&apos;: &apos;Bar&apos;, &apos;created_at&apos;: datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), &apos;updated_at&apos;: datetime.datetime(2017, 9, 28, 21, 15, 32, 299055), &apos;password&apos;: &apos;b9be11166d72e9e3ae7fd407165e4bd2&apos;, &apos;email&apos;: &apos;airbnb@mail.com&apos;, &apos;id&apos;: &apos;38f22813-2753-4d42-b37c-57a17f1e4f88&apos;}
(hbnb) 
(hbnb) User.update(&quot;38f22813-2753-4d42-b37c-57a17f1e4f88&quot;, {&apos;first_name&apos;: &quot;John&quot;, &quot;age&quot;: 89})
(hbnb) 
(hbnb) User.show(&quot;38f22813-2753-4d42-b37c-57a17f1e4f88&quot;)
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {&apos;age&apos;: 89, &apos;first_name&apos;: &apos;John&apos;, &apos;last_name&apos;: &apos;Bar&apos;, &apos;created_at&apos;: datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), &apos;updated_at&apos;: datetime.datetime(2017, 9, 28, 21, 17, 10, 788143), &apos;password&apos;: &apos;b9be11166d72e9e3ae7fd407165e4bd2&apos;, &apos;email&apos;: &apos;airbnb@mail.com&apos;, &apos;id&apos;: &apos;38f22813-2753-4d42-b37c-57a17f1e4f88&apos;}
(hbnb) 
</code></pre>
            <p><strong>No unittests needed</strong></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone</code></li>
                    <li>File:&nbsp;<code>console.py</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>17. Unittests for the Console!</h3>
            <div>#advanced</div>
        </div>
        <div>
            <p>Write all unittests for&nbsp;<code>console.py</code>, all features!</p>
            <p>For testing the console, you should &ldquo;intercept&rdquo; STDOUT of it, we&nbsp;<strong>highly</strong> recommend you to use:</p>
            <pre><code>with patch(&apos;sys.stdout&apos;, new=StringIO()) as f:
    HBNBCommand().onecmd(&quot;help show&quot;)
</code></pre>
            <p>Otherwise, you will have to re-write the console by replacing&nbsp;<code>precmd</code> by&nbsp;<code>default</code>.</p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone</code></li>
                    <li>File:&nbsp;<code>tests/test_console.py</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button>&nbsp;</div>
            </div>
        </div>
    </div>
</div>
