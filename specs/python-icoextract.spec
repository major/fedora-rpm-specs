# Created by pyp2rpm-3.3.8
%global pypi_name icoextract
%global pypi_version 0.1.5

# NOTE: 'icoextract' itself required for tests
%bcond_with tests

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        %autorelease
Summary:        Windows PE EXE icon extractor

License:        MIT
URL:            https://github.com/jlu5/icoextract
# Tests not available on PyPI
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%if %{with tests}
BuildRequires:  ImageMagick
BuildRequires:  make
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  python3-icoextract
%endif

%description
icoextract is an icon extractor for Windows PE files (.exe/.dll), written in
Python. It also includes a thumbnailer script (exe-thumbnailer) for Linux
desktops.

This project is inspired by extract-icon-py, icoutils, and others.

icoextract aims to be:

  * Lightweight
  * Portable (cross-platform)
  * Fast on large files


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(pefile)
Requires:       python3dist(pillow)
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
icoextract is an icon extractor for Windows PE files (.exe/.dll), written in
Python. It also includes a thumbnailer script (exe-thumbnailer) for Linux
desktops.

This project is inspired by extract-icon-py, icoutils, and others.

icoextract aims to be:

  * Lightweight
  * Portable (cross-platform)
  * Fast on large files


%prep
%autosetup -n %{pypi_name}-%{pypi_version}


%build
%py3_build


%install
%py3_install

# Exec permission
pushd %{buildroot}%{python3_sitelib}/%{pypi_name}
chmod a+x __init__.py
popd

pushd %{buildroot}%{python3_sitelib}/%{pypi_name}/scripts
chmod a+x {extract,icolist,thumbnailer}.py
popd


%if %{with tests}
%check
pushd tests
make
%{python3} test_extract.py
%{python3} test_thumbnailer.py
popd
%endif


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{pypi_name}
%{_bindir}/exe-thumbnailer
%{_bindir}/icolist
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info


%changelog
%autochangelog
