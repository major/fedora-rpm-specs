%global srcname pytaglib

Name:           python-%{srcname}
Version:        3.2.0
Release:        %autorelease
Summary:        Python audio metadata ("tagging") library based on TagLib

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/supermihi/pytaglib
Source:         %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  taglib-devel >= 2.0

%global _description \
pytaglib is a full-featured, easy-to-use, cross-platform audio metadata\
(“tag”) library for Python (all versions supported). It uses the popular,\
fast and rock-solid TagLib C++ library internally.\
\
pytaglib is a very thin wrapper about TagLib (<150 lines of code), meaning\
that you immediately profit from the underlying library’s speed and stability.

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-Cython
BuildRequires:  python3-pytest

%generate_buildrequires
%pyproject_buildrequires

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version} -p1
# remove useless shebang
sed -i -e '1{\@^#!/usr/bin/env python@d}' src/pyprinttags.py

# Remove explicit Cython version, rely on wildcard
sed -i 's/cython==3\.2\.[^"]*/cython==3.*/' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.md CHANGELOG.md
%{_bindir}/pyprinttags
%{python3_sitearch}/%{srcname}-*.dist-info/
%{python3_sitearch}/taglib.*.so
%{python3_sitearch}/pyprinttags.py
%{python3_sitearch}/__pycache__/pyprinttags.*

%changelog
%autochangelog
