%global common_description %{expand:
prompt_toolkit is a library for building powerful interactive command line
applications in Python.}

Name:           python-prompt-toolkit
Version:        3.0.41
Release:        %autorelease
Summary:        Library for building powerful interactive command line applications in Python
License:        BSD-3-Clause
URL:            https://github.com/prompt-toolkit/python-prompt-toolkit
Source:         %{pypi_source prompt_toolkit}
BuildArch:      noarch


%description %{common_description}


%package -n python3-prompt-toolkit
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
# https://github.com/jonathanslenders/python-prompt-toolkit/issues/94
Recommends:     python3-pygments


%description -n python3-prompt-toolkit %{common_description}


%prep
%autosetup -n prompt_toolkit-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files prompt_toolkit


%check
%pytest


%files -n python3-prompt-toolkit -f %{pyproject_files}
%doc README.rst AUTHORS.rst CHANGELOG


%changelog
%autochangelog
