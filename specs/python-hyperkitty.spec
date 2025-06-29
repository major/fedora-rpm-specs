# Build doc by default
%bcond_without doc

# mailman3's TestableMaster can't be used outside of a
# source checkout?
%bcond_with tests

Name:           python-hyperkitty
Version:        1.3.12
Release:        %autorelease
Summary:        A web interface to access GNU Mailman v3 archives
License:        GPL-3.0-or-later
URL:            https://gitlab.com/mailman/hyperkitty
# PyPI still stuck on 1.3.9
# Source:         %%{pypi_source HyperKitty}
Source:         %{url}/-/archive/%{version}/hyperkitty-%{version}.tar.gz
# don't check out modules from git
Patch:          HyperKitty-tox-localdeps.patch
# Allow Django 5.2, for Python 3.14 compatibility
Patch:          hyperkitty-django52.diff

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel

%if %{with doc}
BuildRequires:  make
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-sphinx_rtd_theme
%endif

%global _description %{expand:
HyperKitty is an open source Django application under development. It aims to
provide a web interface to access GNU Mailman v3 archives.}

%description %{_description}


%package -n hyperkitty
Summary:        %{summary}

Recommends:     python%{python3_version}dist(cmarkgfm)

%description -n hyperkitty %{_description}


%package -n hyperkitty-doc
Summary:        Documentation for hyperkitty
Suggests:       hyperkitty = %{version}-%{release}

%description -n hyperkitty-doc %{_description}

This package contains the documentation for hyperkitty.


%prep
%autosetup -p1 -n hyperkitty-%{version}
# fix shebang
sed -i 's|#!/usr/bin/env python|#!/usr/bin/python3|' \
  example_project/manage.py


%generate_buildrequires
%if %{with tests}
%pyproject_buildrequires -t
%else
%pyproject_buildrequires
%endif


%build
%pyproject_wheel

%if %{with doc}
(cd doc && PYTHONPATH=..:${PYTHONPATH} make html)
%endif


%install
%pyproject_install
%pyproject_save_files hyperkitty


%check
# requires the Django app to be configured
# pyproject_check_import
%if %{with tests}

PYTHONPATH=$(pwd)/src:${PYTHONPATH} \
%tox
%endif


%files -n hyperkitty -f %{pyproject_files}
%license COPYING.txt
%doc AUTHORS.txt README.rst

%if %{with doc}
%files -n hyperkitty-doc
%license COPYING.txt
%doc doc/_build/html/*
%endif


%changelog
%autochangelog
