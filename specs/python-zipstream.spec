%global srcname zipstream
%global desc zipstream.py is a zip archive generator based on python 3.3's zipfile.py.\
It was created to generate a zip file generator for streaming (ie web apps).

Name:           python-%{srcname}
Version:        1.1.4
Release:        %autorelease
Summary:        ZIP archive generator for Python

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/allanlei/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch


%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{srcname}
%{desc}
Python 3 version.

%prep
%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l '*'

%check
%pyproject_check_import
%{__python3} -m unittest discover -v



%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.* 


%changelog
%autochangelog
