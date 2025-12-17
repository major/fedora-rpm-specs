Name:       ydiff
Version:    1.5
Release:    %autorelease
Summary:    View colored, incremental diff
URL:        https://github.com/ymattw/ydiff
License:    BSD-3-Clause
Source0:    https://github.com/ymattw/ydiff/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: less
BuildArch: noarch

Requires: less
Requires: python%{python3_pkgversion}-%{name}
%description
Ydiff is a terminal-based tool to view colored, incremental diffs in
a version-controlled workspace or from stdin, in side-by-side (similar to
``diff -y``) or unified mode, and auto-paged.

%package -n     python3-%{name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{name}}
%description -n python3-%{name}
Python library that implements API used by ydiff tool.

%prep
%autosetup -n %{name}-%{version}
/usr/bin/sed -i '/#!\/usr\/bin\/env python/d' ydiff.py

%build
%py3_build

%check
tests/regression.sh
# upstream pipeline uses `make test` which also has coverage
# and linters but we don't do those here

%install
%py3_install

%files
%doc README.rst
%license LICENSE
%{_bindir}/ydiff

%files -n python3-%{name}
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{name}.py
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
