Name:           python-google-genai
Version:        3.1.0
Release:        %autorelease
Summary:        Google GenAI Python SDK

# JS and CSS in documentation are MIT
# everything else is Apache-2.0
License:        Apache-2.0 AND MIT
URL:            https://github.com/googleapis/python-genai
Source:         %{pypi_source google_genai}
# https://github.com/googleapis/python-genai/pull/1902
Patch1:         0001-add-build-backend-to-key-to-be-complient-with-PEP517.patch      

BuildSystem:    pyproject
BuildOption(install):  --assert-license google
BuildOption(generate_buildrequires): --extras aiohttp,httpx,httpx2,local-tokenizer,local-tokenizer-transformers,pyopenssl

BuildArch:      noarch
# local-tokenizer depends in build time on torch that is x86_64 aarch64 only
ExclusiveArch:  x86_64 aarch64 noarch
BuildRequires:  python3-devel
# not stated in pyproject
Requires:       python3-mcp
BuildRequires:  python3-mcp
# required to run dynamic buildrequires
BuildRequires:  python3-pkginfo
# checks
BuildRequires:  python3-sentencepiece
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-asyncio}
BuildRequires:  python3-pillow
# soft deps
Recommends:     python3-sentencepiece


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
Google Gen AI Python SDK provides an interface
for developers to integrate Google''s generative models into their Python
applications. It supports the Gemini Developer API and Vertex AI APIs
} 

%description %_description

%package -n     python3-google-genai
Summary:        %{summary}

%description -n python3-google-genai %_description

# local-tokenizer cannot be build now - see above
%pyproject_extras_subpkg -n python3-google-genai aiohttp

%prep -a
%pyproject_patch_dependency google-auth:drop_upper
%pyproject_patch_dependency tenacity:drop_upper

%check
export GOOGLE_GENAI_REPLAYS_DIRECTORY=/tmp
# All -e flags must be on one line: RPM macro expansion only passes arguments
# from the same line, so multi-line continuation only applies the first -e.
# Excluded modules:
#  - test_embed_content, test_edit_image, test_function_call_streaming,
#    test_generate_*, test_segment_image: read image/audio/video data files at
#    module level (before any test runs); data files not installed to BUILDROOT
#  - test_create_with_inlined_requests: same module-level file read
#  - shared/models/test_edit_image, test_segment_image: same
#  - test_types, test_blobs: excluded from import check only (run via pytest)
#  - private/test_send_message_private: private SDK test
%pyproject_check_import -e google.genai.tests.types.test_types -e google.genai.tests.transformers.test_blobs -e google.genai.tests.models.test_embed_content -e google.genai.tests.batches.test_create_with_inlined_requests -e google.genai.tests.models.test_edit_image -e google.genai.tests.models.test_function_call_streaming -e "google.genai.tests.models.test_generate_*" -e google.genai.tests.models.test_generate_content -e google.genai.tests.models.test_generate_content_part -e google.genai.tests.models.test_generate_content_tools -e google.genai.tests.models.test_generate_videos -e google.genai.tests.models.test_segment_image -e google.genai.tests.shared.models.test_upscale_image -e google.genai.tests.shared.models.test_edit_image -e google.genai.tests.shared.models.test_segment_image -e google.genai.tests.private.test_send_message_private
# Run unit tests; skip those requiring live API access (no replay files
# bundled in the source tarball) or network/environment not available in mock.
#
# Skipped directories (all tests use ReplayApiClient needing API credentials):
#   models, caches, batches, files, tokens, tunings, shared - replay API tests
#   live_api, gaos, documents, file_search_stores, interactions, operations,
#   public_samples - require live API or special environment
#
# Skipped individual files:
#   afc/test_generate_content_stream_afc_thoughts.py - uses replay API client
#   chats/test_send_message*.py - uses replay API client
#   transformers/test_blobs.py - image_jpeg fixture reads data not in BUILDROOT
#   client/test_httpx2_client.py - SSL/truststore assertions fail in mock env
#   client/test_retries.py - tries to connect to aiplatform.googleapis.com
#   live/test_live.py - websocket connect test requires network
#   live/test_send_realtime_input.py - reads image/video data files
%pytest google/genai/tests/ \
    --ignore=google/genai/tests/models \
    --ignore=google/genai/tests/caches \
    --ignore=google/genai/tests/batches \
    --ignore=google/genai/tests/files \
    --ignore=google/genai/tests/tokens \
    --ignore=google/genai/tests/tunings \
    --ignore=google/genai/tests/shared \
    --ignore=google/genai/tests/live_api \
    --ignore=google/genai/tests/gaos \
    --ignore=google/genai/tests/documents \
    --ignore=google/genai/tests/file_search_stores \
    --ignore=google/genai/tests/interactions \
    --ignore=google/genai/tests/operations \
    --ignore=google/genai/tests/public_samples \
    --ignore=google/genai/tests/afc/test_generate_content_stream_afc_thoughts.py \
    --ignore=google/genai/tests/chats/test_send_message.py \
    --ignore=google/genai/tests/chats/test_send_message_continuation_token.py \
    --ignore=google/genai/tests/transformers/test_blobs.py \
    --ignore=google/genai/tests/client/test_httpx2_client.py \
    --ignore=google/genai/tests/client/test_retries.py \
    --ignore=google/genai/tests/live/test_send_realtime_input.py \
    --ignore=google/genai/tests/live/test_live.py

%files -n python3-google-genai -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
