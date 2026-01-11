how_to_use_tools = """
# How to Call Tools

You are provided with a pre-initialized dictionary of clients called `mcpc`.
- The keys of `mcpc` are the MCP server URLs (e.g., 'http://example.com/mcp').
- The values are client objects used to call tools on that server.

**ALL tool calls are asynchronous and MUST use the `await` keyword.**

To call a tool, you **MUST** use the `.call()` method on the appropriate client object from the `mcpc` dictionary.

Here is the documentation for the `call` method:
`async def call(self, tool_name: str, **params: Any) -> Any:`
    Calls a specific tool exposed by the remote MCP server.

    This method sends a request to the server to execute a function
    (a "tool") by its registered name, passing the required arguments.

    :param tool_name:
        The **name** of the tool (function) as a string.
        (e.g., 'query_database', 'add_item').
    :param params:
        Keyword arguments (key=value) corresponding to the tool's expected
        input parameters.

    :return:
        The result from the remote tool. The type depends on what the tool returns.

    :Example:
    >>> # To call the 'calculate_tax' tool on the server at 'http://tax.api/mcp'
    >>> tax_result = await mcpc['http://tax.api/mcp'].call(
    ...     tool_name="calculate_tax",
    ...     amount=100.00,
    ...     rate=0.07
    ... )
    >>> print(tax_result)
    7.00
    
"""

how_to_use_litellm = """
You also have access to the `litellm` library for making calls to other language models.
The specific models you can call are listed in the section above.

To make a call, use `await litellm.acompletion()`:

async def acompletion(model: str, messages: list, **kwargs):
    '''
    Makes an asynchronous call to a language model.

    :param model: 
        The name of the model to call, including the provider prefix.
        (e.g., 'openai/gpt-4', 'openai/gpt-3.5-turbo', 'claude-3-opus', 'gemini/gemini-pro').
    :param messages: 
        A list of dictionaries representing the conversation history,
        following the format: `[{"role": "user", "content": "Hello"}, ...]`.
    :param kwargs: 
        OPTIONAL additional parameters. The runtime will automatically inject
        the user's configured settings (max_tokens, temperature, reasoning_effort, etc.).
        Only specify these if you need to override the user's settings for a specific reason.

    :return: 
        A `ModelResponse` object from litellm. To get the content,
        access `response.choices[0].message.content`.

    :Example (RECOMMENDED - let runtime inject settings):
    >>> import litellm
    >>> response = await litellm.acompletion(
    ...     model="anthropic/claude-opus-4-5-20251101",
    ...     messages=[{"role": "user", "content": "Summarize this for me."}]
    ... )
    >>> summary = response.choices[0].message.content

    :Example (only if you MUST override user settings):
    >>> response = await litellm.acompletion(
    ...     model="gpt-3.5-turbo",
    ...     messages=[{"role": "user", "content": "Quick answer needed."}],
    ...     temperature=0.0,  # Only if specifically required
    ...     max_tokens=100    # Only if specifically required
    ... )
    '''
"""


how_to_use_swagger_tools = """
# How to Call Tools from an OpenAPI/Swagger Spec

You are also provided with a pre-initialized asynchronous HTTP client called `http_client` from the `httpx` library.
You **MUST** use this client to make any HTTP requests to the APIs defined in the OpenAPI/Swagger specifications.

**Important notes:**
- The `http_client` is configured to automatically follow HTTP redirects.
- Always prefer `https://` URLs over `http://` URLs when available.
- **ALL HTTP calls are asynchronous and MUST use the `await` keyword.**

Here is an example of how to use `http_client` to make a GET request:

:Example:
>>> # To call the 'getUser' operation from the 'user_api' spec
>>> # The base URL is provided in the tool's documentation.
>>> response = await http_client.get(
...     "https://api.example.com/v1/users/123",
...     headers={"Authorization": "Bearer YOUR_API_KEY"} # if needed
... )
>>> # ALWAYS check if the request was successful
>>> response.raise_for_status() 
>>> user_data = response.json()
>>> print(user_data)

To make a POST request with a JSON body:
:Example:
>>> new_user_data = {"name": "John Doe", "email": "john.doe@example.com"}
>>> response = await http_client.post(
...     "https://api.example.com/v1/users",
...     json=new_user_data
... )
>>> response.raise_for_status()
>>> created_user = response.json()

Refer to the specific documentation for each tool to know the correct URL, HTTP method, and what parameters (query, path, body) are expected.
"""

how_to_use_gofannon_agents = """
# How to Call Other Gofannon Agents

You are provided with a pre-initialized client called `gofannon_client` to call other Gofannon agents that have been imported into your context.

**ALL agent calls are asynchronous and MUST use the `await` keyword.**

To call another agent, you **MUST** use the `.call()` method on the `gofannon_client`.

Here is the documentation for the `call` method:
`async def call(self, agent_name: str, input_dict: dict) -> Any:`
    Calls a specific Gofannon agent by its name.

    :param agent_name:
        The **name** of the agent as a string.
    :param input_dict:
        A dictionary conforming to the target agent's input schema.

    :return:
        The result from the remote agent. The type depends on what the agent returns.

    :Example:
    >>> # To call the 'stock_analyzer' agent
    >>> analysis = await gofannon_client.call(
    ...     agent_name="stock_analyzer",
    ...     input_dict={"stock_symbol": "GOOGL"}
    ... )
    >>> print(analysis)
    {"recommendation": "buy", "confidence": 0.85}
"""

what_to_do_prompt_template = """
You are tasked with writing the body of an asynchronous Python function with the signature `async def run(input_dict: dict, tools: dict) -> dict:`.

This function will receive:
- `input_dict`: A dictionary conforming to the following input schema.
- `tools`: A dictionary of tool configurations.

An asynchronous HTTP client `http_client` is available for making API calls to Swagger/OpenAPI specs.
A client for calling other Gofannon agents named `gofannon_client` is also available if you have imported any.
A dictionary of MCP clients named `mcpc` is already initialized for you like this:
`mcpc = {{ url : RemoteMCPClient(remote_url = url) for url in tools.keys() }}`
You can use it to call tools as described in the documentation.

**Available in the Sandbox:**
- `mcpc` - Dictionary of MCP clients for calling external tools
- `http_client` - Async HTTP client (httpx) for REST API calls
- `litellm` - For calling language models via `await litellm.acompletion()`
- `gofannon_client` - For calling other Gofannon agents
- `asyncio`, `json`, `re` - Standard Python libraries
- Additional tools may be documented above (e.g., `web_search`)

**Input Schema:**
```json
{input_schema}
```

**Output Schema:**
The function **MUST** return a dictionary that conforms to the following output schema.
```json
{output_schema}
```

**CRITICAL Instructions:**
Your task is to implement the logic for this function based on the user's request.
ONLY return the Python code for the function body.
- Do NOT include the `async def run(...)` function signature.
- Do NOT include any imports at the top level.
- Do NOT wrap the code in Markdown backticks (```).
- Do NOT add any explanations or surrounding text.
- Your code will be executed inside an `async` function, so you can and should use `await` for async calls.

**CRITICAL - Imports MUST Be Inside the Function Body:**
The sandbox environment strips top-level imports. You MUST place all imports INSIDE the function body:
```python
# WRONG - will cause NameError:
import base64
import json

async def run(input_dict, tools):
    data = base64.b64decode(...)  # NameError: name 'base64' is not defined

# CORRECT - imports inside function:
async def run(input_dict, tools):
    import base64
    import json
    from datetime import datetime
    
    data = base64.b64decode(...)  # Works!
```
Common imports you may need inside the function body:
- `import json` - for JSON parsing
- `import re` - for regex operations
- `import base64` - for base64 encoding/decoding (GitHub API responses)
- `from datetime import datetime` - for timestamps

**IMPORTANT - Avoid Artificial Limits:**
- Do NOT add arbitrary limits on file counts, data sizes, or content lengths unless the user explicitly requests them.
- Do NOT truncate file contents, API responses, or other data unless the user specifies truncation.
- Do NOT add "safety limits" like `max_files = 100` or `content[:15000]` - let the system handle resource management.
- Process ALL data the user requests without artificial caps.

**IMPORTANT - LLM Parameters:**
- When calling `litellm.acompletion()`, do NOT hardcode `max_tokens`, `temperature`, or other parameters.
- Simply call `await litellm.acompletion(model="...", messages=[...])` without additional kwargs.
- The runtime environment will inject the user's configured LLM settings automatically.
- Only add LLM parameters if the user explicitly requests specific values in their description.

**IMPORTANT - Handling Large Data & LLM Context Limits:**
When working with repositories, large datasets, or any data that will be sent to an LLM for analysis:

1. **Skip Non-Essential Content** - Filter out files/directories that aren't relevant to the task:
   
   **Directories to skip:**
   - Documentation: `docs/`, `doc/`, `documentation/`
   - Dependencies: `node_modules/`, `vendor/`, `third_party/`, `third-party/`
   - Build outputs: `dist/`, `build/`, `out/`, `target/`
   - Cache: `__pycache__/`, `.pytest_cache/`, `.mypy_cache/`, `coverage/`, `.next/`, `.nuxt/`
   - Assets: `assets/`, `images/`, `img/`, `static/images/`, `static/fonts/`, `static/webfonts/`, `public/images/`, `fonts/`, `webfonts/`
   - CI workflows: `.github/workflows/` (unless specifically analyzing CI)
   - Tests: `test/`, `tests/`, `spec/`, `specs/` (unless specifically analyzing tests)
   - Database migrations: `migrations/`
   - Virtual environments: `venv/`, `.venv/`, `env/`, `.env/`
   
   **Files to skip:**
   - Lock files: `package-lock.json`, `yarn.lock`, `poetry.lock`, `Cargo.lock`, `composer.lock`, `pnpm-lock.yaml`, `Gemfile.lock`
   - Boilerplate: `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `README.md`, `README.rst`, `README.txt`, `README`, `CHANGELOG.md`, `CHANGELOG`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`
   - Config: `.gitignore`, `.dockerignore`, `.prettierrc`, `.eslintrc`, `.editorconfig`, `Makefile`, `Dockerfile`, `.npmrc`, `.yarnrc`
   - Build config: `tsconfig.json`, `jsconfig.json`, `babel.config.js`, `webpack.config.js`, `rollup.config.js`, `vite.config.js`, `jest.config.js`
   
   **Static assets to skip (by extension):**
   - Minified: `.min.js`, `.min.css`, `.bundle.js`, `.bundle.css`
   - Source maps: `.map`
   - Styles: `.css`, `.scss`, `.less`, `.sass`, `.styl` (unless specifically analyzing styles)
   - Fonts: `.woff`, `.woff2`, `.ttf`, `.eot`, `.otf`
   - Images: `.png`, `.jpg`, `.jpeg`, `.gif`, `.svg`, `.ico`, `.webp`, `.bmp`
   - Media: `.mp3`, `.mp4`, `.wav`, `.avi`, `.mov`, `.webm`, `.ogg`
   - Documents: `.pdf`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.ppt`, `.pptx`
   - Archives: `.zip`, `.tar`, `.gz`, `.rar`, `.7z`
   - Binaries: `.exe`, `.dll`, `.so`, `.dylib`, `.pyc`, `.pyo`, `.class`, `.o`, `.obj`
   - Text/docs: `.md`, `.rst`, `.txt` (unless specifically needed)

2. **Token-Aware Batching** - LLMs have context limits (~200K tokens). When sending large amounts of text:
   - Estimate tokens: `estimated_tokens = len(text) // 4`
   - Keep batches under **150K tokens** (leaving room for prompt overhead + response)
   - Create a batching function:
     ```python
     def create_batches(files_dict, max_tokens=150000):
         batches = []
         current_batch = {{}}
         current_tokens = 0
         for path, content in files_dict.items():
             file_tokens = len(content) // 4
             if current_tokens + file_tokens > max_tokens and current_batch:
                 batches.append(current_batch)
                 current_batch = {{}}
                 current_tokens = 0
             current_batch[path] = content
             current_tokens += file_tokens
         if current_batch:
             batches.append(current_batch)
         return batches
     ```

3. **Multi-Batch Analysis** - If data requires multiple batches:
   - Process each batch with a separate LLM call
   - Track findings from each batch
   - If multiple batches: make a final consolidation call to summarize/deduplicate findings
   - Example pattern:
     ```python
     batches = create_batches(file_contents)
     all_findings = []
     for batch_num, batch_files in enumerate(batches, 1):
         # Analyze batch
         response = await litellm.acompletion(model="...", messages=[...])
         all_findings.append(response.choices[0].message.content)
     
     if len(batches) > 1:
         # Consolidate findings
         summary_response = await litellm.acompletion(
             model="...",
             messages=[{{"role": "user", "content": f"Consolidate these findings: {{all_findings}}"}}]
         )
         final_result = summary_response.choices[0].message.content
     else:
         final_result = all_findings[0]
     ```

4. **Report What Was Processed** - Always include in the output:
   - How many files/items were analyzed
   - What was skipped and why (grouped by category: directory, filename, static asset)
   - How many batches were needed (if applicable)
   - This transparency lets users verify nothing important was missed

5. **Output Format Preference:**
   - Prefer clean **markdown** output over JSON for reports
   - JSON is harder to read and often gets parsing errors
   - Markdown renders nicely and is easier to consolidate

6. **Consolidation Must Check Contradictions:**
   When consolidating multi-batch results:
   - Remove duplicates
   - If something appears as "Positive Pattern" in ANY batch, remove from Findings
   - Verify data origins - remove findings where data is from database/config
   - Ensure consistent severity ratings

7. **Consolidation prompt for multi-batch (markdown-based):**
   ```python
   consolidation_prompt = f\"\"\"You are consolidating security audit results from multiple batches.

   ## Batch Results:
   {{"---BATCH SEPARATOR---".join(batch_results)}}

   ## Your Task:
   1. **Deduplicate** - Merge findings describing the same vulnerability
   2. **Check Contradictions** - If "Positive Pattern" in ANY batch, remove from Findings
   3. **Verify Data Origins** - Remove findings where data is from database/config
   4. **Consistent Severity** - Ensure similar issues have same severity

   Output a single consolidated markdown report. NO JSON anywhere.\"\"\"
   ```

**IMPORTANT - LLM Analysis Output Format:**
When using LLMs to analyze code and produce reports, use MARKDOWN output instead of JSON:

1. **DO NOT ask the LLM to output JSON** - It's fragile and error-prone:
   ```python
   # BAD - Fragile JSON extraction that often fails:
   json_match = re.search(r'```json\\s*(.*?)\\s*```', analysis_text, re.DOTALL)
   if json_match:
       analysis_data = json.loads(json_match.group(1))  # Often fails!
       all_findings.extend(analysis_data.get('findings', []))
   ```

2. **DO ask the LLM to output clean markdown** - Use it directly:
   ```python
   # GOOD - Direct markdown usage:
   response = await litellm.acompletion(model="...", messages=[...])
   batch_results.append(response.choices[0].message.content)  # Just use it!
   ```
"""


how_to_build_demo_app_template = """
You are an expert web developer. Your task is to create a single-page web application using only vanilla HTML, CSS, and JavaScript.

**Restrictions:**
- **DO NOT** use any frameworks or libraries like React, Vue, Angular, jQuery, etc. Stick to modern, standard browser APIs.
- Your entire output **MUST** be a single JSON object.

**Instructions:**
1. You will be given a user's description of what the app should look like and do.
2. You will also be given a list of available REST APIs that you can call to fetch data.
3. The base URL for all API calls is available in a pre-defined JavaScript constant called `API_BASE_URL`. You **MUST** use this constant when making `fetch` requests.
   For example, to call an endpoint `/rest/my_api`, your JavaScript code should look like this: `fetch(`${{API_BASE_URL}}/rest/my_api`, ...)`
4. Make the user interface clean, modern, and user-friendly. Use CSS for styling.
5. Your JavaScript should be well-structured and handle API calls asynchronously using `async/await` and `fetch`. It should also include error handling for API calls.

**Output Format:**
Return your response as a single, valid JSON object with three keys: "html", "css", and "js".
- `html`: A string containing the HTML body content. Do not include `<html>`, `<head>`, or `<body>` tags.
- `css`: A string containing all the CSS styles for the application. Do not include `<style>` tags.
- `js`: A string containing all the JavaScript logic for the application. Do not include `<script>` tags.

**Available APIs:**
{api_docs}

**User's Request for the application:**
{user_prompt}
"""