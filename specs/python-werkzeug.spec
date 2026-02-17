%global srcname werkzeug
%global modname werkzeug

# Tests require among others python-greenlet which is not available
# during the early phases of a new Python integration, which in turn blocks
# many other important packages from building.
# With the conditionalized build, the rebuild can proceed
%bcond tests 1

Name:           python-%{modname}
Version:        3.1.5
Release:        %autorelease
Summary:        Comprehensive WSGI web application library

License:        BSD-3-Clause
URL:            https://werkzeug.palletsprojects.com
Source0:        %{pypi_source}

# Fixes PYTHONPATH handling in tests
# Upstream: https://github.com/pallets/werkzeug/pull/2172
Patch:          preserve-any-existing-PYTHONPATH-in-tests.patch

BuildArch:      noarch

%global _description %{expand:
Werkzeug
========

Werkzeug started as simple collection of various utilities for WSGI
applications and has become one of the most advanced WSGI utility
modules.  It includes a powerful debugger, full featured request and
response objects, HTTP utilities to handle entity tags, cache control
headers, HTTP dates, cookie handling, file uploads, a powerful URL
routing system and a bunch of community contributed addon modules.

Werkzeug is unicode aware and doesn't enforce a specific template
engine, database adapter or anything else.  It doesn't even enforce
a specific way of handling requests and leaves all that up to the
developer. It's most useful for end user applications which should work
on as many server environments as possible (such as blogs, wikis,
bulletin boards, etc.).}

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  make
BuildRequires:  python3-devel

%description -n python3-%{modname} %{_description}

%package -n python3-werkzeug-doc
Summary:        Documentation for python3-werkzeug
Requires:       python3-werkzeug = %{version}-%{release}

%description -n python3-werkzeug-doc
Documentation and examples for python3-werkzeug.

%generate_buildrequires
%if %{with tests}
# -t picks test.txt by default which contains too tight pins
%pyproject_buildrequires -g docs,tests
%else
%pyproject_buildrequires -g docs
%endif

%prep
%autosetup -p1 -n %{srcname}-%{version}
find examples/ -type f -name '*.png' -executable -print -exec chmod -x "{}" +

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

pushd docs
# PYTHONPATH to prevent "'Werkzeug' must be installed to build the documentation."
make PYTHONPATH=%{buildroot}/%{python3_sitelib} SPHINXBUILD=sphinx-build-3 html
rm -v _build/html/.buildinfo
popd

%check
%py3_check_import %{modname}
%if %{with tests}
# deselect the test_exclude_patterns test case as it's failing
# when we set PYTHONPATH: https://github.com/pallets/werkzeug/issues/2404
%pytest -Wdefault --deselect tests/test_serving.py::test_exclude_patterns
%endif

%files -n python3-%{modname} -f %{pyproject_files}
%license LICENSE.txt
%doc CHANGES.rst README.md

%files -n python3-werkzeug-doc
%doc docs/_build/html examples

%changelog
%autochangelog
