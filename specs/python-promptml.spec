Name:           python-promptml
Version:        0.7.1
Release:        %autorelease
Summary:        A simple markup language for defining AI Prompts as Code (APaC)

License:        MIT
URL:            https://github.com/narenaryan/promptml/
Source:         %{pypi_source promptml}
Patch1:         soften-requirements.patch

BuildSystem:    pyproject
BuildOption(install):  -l promptml

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
PromptML is built to provide a way for prompt
engineers to define the AI prompts in a deterministic way. This is a Domain
Specific Language (DSL) which defines characteristics of a prompt including
context, objective, instructions and it's metadata. A regular prompt is an
amalgamation of all these aspects into one entity. PromptML splits it into
multiple sections and makes the information explicit.}

%description %_description

%package -n     python3-promptml
Summary:        %{summary}

%description -n python3-promptml %_description

%check
%{py3_test_envvars} %{python3} -m unittest

%files -n python3-promptml -f %{pyproject_files}


%changelog
%autochangelog
