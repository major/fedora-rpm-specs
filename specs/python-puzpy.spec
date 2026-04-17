%global srcname puzpy

Name:           python-%{srcname}
# PyPI tarball does not contain test files
Version:        0.6.0
Release:        %autorelease
Summary:        Python crossword puzzle library

License:        MIT
URL:            https://github.com/alexdej/puzpy
Source:         %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
# Disable irrelevant tests that pull in unpackaged deps
Patch:          puzpy-drop-unneeded-deps.diff

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Implementation of .puz crossword puzzle file parser based on the .puz file
format documentation.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
%autosetup -N -n %{srcname}-%{version}
%autopatch -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest -v

%files -n python3-%{srcname}
%license %{python3_sitelib}/puzpy-%{version}.dist-info/licenses/LICENSE
%doc CHANGELOG.md README.md
%pycached %{python3_sitelib}/puz.py
%{python3_sitelib}/%{srcname}-%{version}.dist-info

%changelog
%autochangelog
