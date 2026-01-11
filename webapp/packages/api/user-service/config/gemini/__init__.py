# Google Gemini models configuration
# Updated January 2026

models = {
    # =========================================================================
    # Gemini 3 Series (Latest)
    # =========================================================================
    "gemini-3-pro-preview": {
        "returns_thoughts": True,
        "parameters": {
            "temperature": {
                "type": "float",
                "default": 1.0,
                "min": 0.0,
                "max": 2.0,
                "description": "Temperature - Controls the randomness of the output."
            },
            "top_p": {
                "type": "float",
                "default": 0.95,
                "min": 0.0,
                "max": 1.0,
                "description": "Nucleus sampling threshold"
            },
            "top_k": {
                "type": "integer",
                "default": 40,
                "min": 1,
                "max": 100,
                "description": "Top-k sampling"
            },
            "max_tokens": {
                "type": "integer",
                "default": 8192,
                "min": 1,
                "max": 65536,
                "description": "Maximum tokens in response"
            },
            "reasoning_effort": {
                "type": "choice",
                "default": "disable",
                "choices": ["disable", "low", "medium", "high"],
                "description": "Reasoning Effort: Effort level for reasoning during generation"
            },
        },
        "built_in_tools": [
            {
                "id": "google_search",
                "description": "Performs a Google search.",
                "tool_config": {"google_search": {}}
            },
            {
                "id": "urlContext",
                "description": "Provides context from a specified URL.",
                "tool_config": {"urlContext": {}}
            },
            {
                "id": "code_execution",
                "description": "Executes code snippets in a secure environment.",
                "tool_config": {"codeExecution": {}}
            }
        ]
    },

    # =========================================================================
    # Gemini 2.5 Series
    # =========================================================================
    "gemini-2.5-pro": {
        "returns_thoughts": True,
        "parameters": {
            "temperature": {
                "type": "float",
                "default": 1.0,
                "min": 0.0,
                "max": 2.0,
                "description": "Temperature - Controls the randomness of the output."
            },
            "top_p": {
                "type": "float",
                "default": 0.95,
                "min": 0.0,
                "max": 1.0,
                "description": "Nucleus sampling threshold"
            },
            "top_k": {
                "type": "integer",
                "default": 40,
                "min": 1,
                "max": 100,
                "description": "Top-k sampling"
            },
            "max_tokens": {
                "type": "integer",
                "default": 8192,
                "min": 1,
                "max": 65536,
                "description": "Maximum tokens in response"
            },
            "reasoning_effort": {
                "type": "choice",
                "default": "disable",
                "choices": ["disable", "low", "medium", "high"],
                "description": "Reasoning Effort: Effort level for reasoning during generation"
            },
        },
        "built_in_tools": [
            {
                "id": "google_search",
                "description": "Performs a Google search.",
                "tool_config": {"google_search": {}}
            },
            {
                "id": "urlContext",
                "description": "Provides context from a specified URL.",
                "tool_config": {"urlContext": {}}
            },
            {
                "id": "code_execution",
                "description": "Executes code snippets in a secure environment.",
                "tool_config": {"codeExecution": {}}
            }
        ],
    },
    "gemini-2.5-flash": {
        "returns_thoughts": True,
        "parameters": {
            "temperature": {
                "type": "float",
                "default": 1.0,
                "min": 0.0,
                "max": 2.0,
                "description": "Temperature - Controls the randomness of the output."
            },
            "top_p": {
                "type": "float",
                "default": 0.95,
                "min": 0.0,
                "max": 1.0,
                "description": "Nucleus sampling threshold"
            },
            "top_k": {
                "type": "integer",
                "default": 40,
                "min": 1,
                "max": 100,
                "description": "Top-k sampling"
            },
            "max_tokens": {
                "type": "integer",
                "default": 8192,
                "min": 1,
                "max": 65536,
                "description": "Maximum tokens in response"
            },
            "reasoning_effort": {
                "type": "choice",
                "default": "disable",
                "choices": ["disable", "low", "medium", "high"],
                "description": "Reasoning Effort: Effort level for reasoning during generation"
            },
        },
        "built_in_tools": [
            {
                "id": "google_search",
                "description": "Performs a Google search.",
                "tool_config": {"google_search": {}}
            },
            {
                "id": "urlContext",
                "description": "Provides context from a specified URL.",
                "tool_config": {"urlContext": {}}
            },
            {
                "id": "code_execution",
                "description": "Executes code snippets in a secure environment.",
                "tool_config": {"codeExecution": {}}
            }
        ],
    },
    "gemini-2.5-flash-lite": {
        "returns_thoughts": False,
        "parameters": {
            "temperature": {
                "type": "float",
                "default": 1.0,
                "min": 0.0,
                "max": 2.0,
                "description": "Temperature - Controls the randomness of the output."
            },
            "top_p": {
                "type": "float",
                "default": 0.95,
                "min": 0.0,
                "max": 1.0,
                "description": "Nucleus sampling threshold"
            },
            "top_k": {
                "type": "integer",
                "default": 40,
                "min": 1,
                "max": 100,
                "description": "Top-k sampling"
            },
            "max_tokens": {
                "type": "integer",
                "default": 8192,
                "min": 1,
                "max": 32768,
                "description": "Maximum tokens in response"
            },
            "reasoning_effort": {
                "type": "choice",
                "default": "disable",
                "choices": ["disable", "low", "medium", "high"],
                "description": "Reasoning Effort: Effort level for reasoning during generation"
            },
        },
        "built_in_tools": [
            {
                "id": "google_search",
                "description": "Performs a Google search.",
                "tool_config": {"google_search": {}}
            },
            {
                "id": "urlContext",
                "description": "Provides context from a specified URL.",
                "tool_config": {"urlContext": {}}
            },
            {
                "id": "code_execution",
                "description": "Executes code snippets in a secure environment.",
                "tool_config": {"codeExecution": {}}
            }
        ],
    },

    # =========================================================================
    # Gemini 2.0 Series (Legacy)
    # =========================================================================
    "gemini-2.0-flash": {
        "returns_thoughts": False,
        "parameters": {
            "temperature": {
                "type": "float",
                "default": 1.0,
                "min": 0.0,
                "max": 2.0,
                "description": "Temperature - Controls the randomness of the output."
            },
            "top_p": {
                "type": "float",
                "default": 0.95,
                "min": 0.0,
                "max": 1.0,
                "description": "Nucleus sampling threshold"
            },
            "top_k": {
                "type": "integer",
                "default": 40,
                "min": 1,
                "max": 100,
                "description": "Top-k sampling"
            },
            "max_tokens": {
                "type": "integer",
                "default": 8192,
                "min": 1,
                "max": 8192,
                "description": "Maximum tokens in response"
            },
        },
        "built_in_tools": [
            {
                "id": "google_search",
                "description": "Performs a Google search.",
                "tool_config": {"google_search": {}}
            },
            {
                "id": "code_execution",
                "description": "Executes code snippets in a secure environment.",
                "tool_config": {"codeExecution": {}}
            }
        ],
    },
    "gemini-2.0-flash-exp": {
        "returns_thoughts": False,
        "parameters": {
            "temperature": {
                "type": "float",
                "default": 1.0,
                "min": 0.0,
                "max": 2.0,
                "description": "Temperature - Controls the randomness of the output."
            },
            "top_p": {
                "type": "float",
                "default": 0.95,
                "min": 0.0,
                "max": 1.0,
                "description": "Nucleus sampling threshold"
            },
            "top_k": {
                "type": "integer",
                "default": 40,
                "min": 1,
                "max": 100,
                "description": "Top-k sampling"
            },
            "max_tokens": {
                "type": "integer",
                "default": 8192,
                "min": 1,
                "max": 8192,
                "description": "Maximum tokens in response"
            },
        },
        "built_in_tools": [
            {
                "id": "google_search",
                "description": "Performs a Google search.",
                "tool_config": {"google_search": {}}
            },
            {
                "id": "code_execution",
                "description": "Executes code snippets in a secure environment.",
                "tool_config": {"codeExecution": {}}
            }
        ],
    },

    # =========================================================================
    # Gemini 1.5 Series (Legacy)
    # =========================================================================
    "gemini-1.5-pro": {
        "returns_thoughts": False,
        "parameters": {
            "temperature": {
                "type": "float",
                "default": 1.0,
                "min": 0.0,
                "max": 2.0,
                "description": "Temperature - Controls the randomness of the output."
            },
            "top_p": {
                "type": "float",
                "default": 0.95,
                "min": 0.0,
                "max": 1.0,
                "description": "Nucleus sampling threshold"
            },
            "top_k": {
                "type": "integer",
                "default": 40,
                "min": 1,
                "max": 100,
                "description": "Top-k sampling"
            },
            "max_tokens": {
                "type": "integer",
                "default": 8192,
                "min": 1,
                "max": 8192,
                "description": "Maximum tokens in response"
            },
        },
        "built_in_tools": [
            {
                "id": "google_search",
                "description": "Performs a Google search.",
                "tool_config": {"google_search": {}}
            },
            {
                "id": "code_execution",
                "description": "Executes code snippets in a secure environment.",
                "tool_config": {"codeExecution": {}}
            }
        ],
    },
    "gemini-1.5-flash": {
        "returns_thoughts": False,
        "parameters": {
            "temperature": {
                "type": "float",
                "default": 1.0,
                "min": 0.0,
                "max": 2.0,
                "description": "Temperature - Controls the randomness of the output."
            },
            "top_p": {
                "type": "float",
                "default": 0.95,
                "min": 0.0,
                "max": 1.0,
                "description": "Nucleus sampling threshold"
            },
            "top_k": {
                "type": "integer",
                "default": 40,
                "min": 1,
                "max": 100,
                "description": "Top-k sampling"
            },
            "max_tokens": {
                "type": "integer",
                "default": 8192,
                "min": 1,
                "max": 8192,
                "description": "Maximum tokens in response"
            },
        },
        "built_in_tools": [
            {
                "id": "google_search",
                "description": "Performs a Google search.",
                "tool_config": {"google_search": {}}
            },
            {
                "id": "code_execution",
                "description": "Executes code snippets in a secure environment.",
                "tool_config": {"codeExecution": {}}
            }
        ],
    },
    "gemini-1.5-flash-8b": {
        "returns_thoughts": False,
        "parameters": {
            "temperature": {
                "type": "float",
                "default": 1.0,
                "min": 0.0,
                "max": 2.0,
                "description": "Temperature - Controls the randomness of the output."
            },
            "top_p": {
                "type": "float",
                "default": 0.95,
                "min": 0.0,
                "max": 1.0,
                "description": "Nucleus sampling threshold"
            },
            "top_k": {
                "type": "integer",
                "default": 40,
                "min": 1,
                "max": 100,
                "description": "Top-k sampling"
            },
            "max_tokens": {
                "type": "integer",
                "default": 8192,
                "min": 1,
                "max": 8192,
                "description": "Maximum tokens in response"
            },
        },
        "built_in_tools": [
            {
                "id": "google_search",
                "description": "Performs a Google search.",
                "tool_config": {"google_search": {}}
            },
            {
                "id": "code_execution",
                "description": "Executes code snippets in a secure environment.",
                "tool_config": {"codeExecution": {}}
            }
        ],
    },
}