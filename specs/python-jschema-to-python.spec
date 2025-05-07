Name:           python-jschema-to-python
Summary:        Generate source code for Python classes from a JSON schema
Version:        1.2.3
Release:        %autorelease

# SPDX
License:        MIT
URL:            https://github.com/microsoft/jschema-to-python
Source:         %{pypi_source jschema_to_python}

BuildSystem:            pyproject
BuildOption(install):   -l jschema_to_python

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  dos2unix
BuildRequires:  python3dist(pytest)

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package -n     python3-jschema-to-python
Summary:        %{summary}

%description -n python3-jschema-to-python %{common_description}


%prep -a
# Fix CRNL line termination
find . -type f -exec dos2unix --keepdate '{}' '+'


%check -a
%pytest


%files -n python3-jschema-to-python -f %{pyproject_files}
%doc README.rst
%doc SECURITY.md


%changelog
%autochangelog
