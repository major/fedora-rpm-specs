Name:           python-google-genai
Version:        2.11.0
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
BuildOption(install):  -l google
# local-tokenizer requires recent protobuf
# https://bugzilla.redhat.com/show_bug.cgi?id=1831350
BuildOption(generate_buildrequires): -x aiohttp

BuildArch:      noarch
BuildRequires:  python3-devel
# not stated in pyproject
Requires:       python3-mcp
BuildRequires:  python3-mcp
# required to run dynamic buildrequires
BuildRequires:  python3-pkginfo
# checks
BuildRequires:  python3-sentencepiece
BuildRequires:  %{py3_dist pytest}
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
# relax from aiohttp<3.13.3 - we already have 3.13.3 in Fedora
sed -i '1,$s/^aiohttp = \["aiohttp<3.13.3"\]/aiohttp = ["aiohttp"]/' pyproject.toml

%check
export GOOGLE_GENAI_REPLAYS_DIRECTORY=/tmp
#%%pyproject_check_import -e google.genai.local_tokenizer \
#        -e google.genai.tests.types.test_types \
#        -e google.genai.tests.transformers.test_blobs \
#        -e google.genai.tests.models.test_embed_content \
#        -e google.genai.tests.batches.test_create_with_inlined_requests \
#        -e google.genai.tests.local_tokenizer* \
#        -e google.genai.tests.models.test_edit_image \
#        -e google.genai.tests.models.test_function_call_streaming \
#        -e google.genai.tests.models.test_generate_* \
#        -e google.genai.tests.models.test_segment_image \
#        -e google.genai.tests.shared.models.test_upscale_image \
#        -e google.genai.tests.shared.models.test_edit_image \
#        -e google.genai.tests.shared.models.test_segment_image \
#        -e google.genai.tests.transformers.test_blobs \
#        -e google.genai.tests.types.test_types \
#        -e google.genai.tests.batches.test_create_with_inlined_requests \
#        -e google.genai.tests.private.test_send_message_private

%files -n python3-google-genai -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
