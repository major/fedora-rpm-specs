%global srcname puzpy

Name:           python-%{srcname}
# PyPI tarball does not contain test files
Version:        0.2.6
Release:        %autorelease
Summary:        Python crossword puzzle library

License:        MIT
URL:            https://github.com/alexdej/puzpy
Source:         %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Implementation of .puz crossword puzzle file parser based on the .puz file
format documentation.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%check
%tox

%files -n python3-%{srcname}
%doc CHANGELOG.rst README.rst
%pycached %{python3_sitelib}/puz.py
%{python3_sitelib}/%{srcname}-%{version}.dist-info

%changelog
%autochangelog
