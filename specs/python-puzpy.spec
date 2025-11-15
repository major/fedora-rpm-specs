%if (%{defined fedora} && 0%{?fedora} <= 42) || (%{defined rhel} && 0%{?rhel} == 10)
%bcond old_setuptools 1
%else
%bcond old_setuptools 0
%endif

%global srcname puzpy

Name:           python-%{srcname}
# PyPI tarball does not contain test files
Version:        0.3.2
Release:        %autorelease
Summary:        Python crossword puzzle library

License:        MIT
URL:            https://github.com/alexdej/puzpy
Source:         %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
# Disable this test, saves a dependency and it's irrelevant
Patch:          puzpy-disable-update_readme_test.diff
Patch100:       puzpy-undo-setuptools-bump.diff

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
%autosetup -N -n %{srcname}-%{version}
%autopatch -p1 -M 99

%if %{with old_setuptools}
%autopatch -p1 100
%endif

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%check
%tox

%files -n python3-%{srcname}
%if %{with old_setuptools}
%license %{python3_sitelib}/puzpy-%{version}.dist-info/LICENSE
%else
%license %{python3_sitelib}/puzpy-%{version}.dist-info/licenses/LICENSE
%endif
%doc CHANGELOG.md README.md
%pycached %{python3_sitelib}/puz.py
%{python3_sitelib}/%{srcname}-%{version}.dist-info

%changelog
%autochangelog
