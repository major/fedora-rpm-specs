Name:           python-google-genai
Version:        1.56.0
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
# local-tokenizer requires recent protobug
# https://bugzilla.redhat.com/show_bug.cgi?id=1831350
BuildOption(generate_buildrequires): -x aiohttp

BuildArch:      noarch
BuildRequires:  python3-devel
# required to run dynamic buildrequires
BuildRequires:  python3-pkginfo
# checks
BuildRequires:  python3-sentencepiece
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

%check
%pyproject_check_import -e google.genai.local_tokenizer

%files -n python3-google-genai -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
