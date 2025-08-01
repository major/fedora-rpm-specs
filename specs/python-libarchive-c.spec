Name:          python-libarchive-c
Version:       5.3
Release:       %autorelease
Summary:       Python interface to libarchive
License:       CC0-1.0
URL:           https://github.com/Changaco/python-libarchive-c

%global forgeurl %{url}
%global tag %{version}
%forgemeta

Source:        https://github.com/Changaco/python-libarchive-c/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch:         0001-Allow-rmd160-digest-to-be-missing-in-tests.patch

BuildRequires: libarchive-devel
BuildArch:     noarch

%global _description %{expand:
The libarchive library provides a flexible interface for reading and
writing archives in various formats such as tar and cpio. libarchive
also supports reading and writing archives compressed using various
compression filters such as gzip and bzip2.

A Python interface to libarchive. It uses the standard ctypes module
to dynamically load and access the C library.}

%description %_description

%package -n python%{python3_pkgversion}-libarchive-c
Summary:       %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-libarchive-c}
BuildRequires: python%{python3_pkgversion}-setuptools
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-pytest
Requires:      libarchive

%description -n python%{python3_pkgversion}-libarchive-c %_description

%prep
%autosetup -n %{name}-%{version} -p1

%build
%py3_build

%install
%py3_install
%{_fixperms} %{buildroot}

%check
%{?el7:export LANG=en_US.UTF-8}
pytest-%{python3_version} -s -vv tests %{?el7:-k "not test_check_archiveentry_using_python_testtar"}

%global _docdir_fmt %{name}

%files -n python%{python3_pkgversion}-libarchive-c
%doc README.rst
%license LICENSE.md
%{python3_sitelib}/libarchive*

%changelog
%autochangelog
