%global common_description %{expand:
This module provides a parser for the multipart/form-data format.
It can read from a file, a socket or a WSGI environment.
The parser can be used to replace cgi.FieldStorage to work around its
limitations.}

Name:           python-multipart
Version:        1.3.0
Release:        %autorelease
Summary:        Parser for multipart/form-data
License:        MIT
URL:            https://github.com/defnull/multipart
Source:         %{pypi_source multipart}
BuildArch:      noarch


%description %{common_description}


%package -n python3-multipart
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
# This package uses the same import namespace:
Conflicts:      python3-python-multipart


%description -n python3-multipart %{common_description}


%prep
%autosetup -n multipart-%{version} -p 1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l multipart


%check
%pytest


%files -n python3-multipart -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
