# Build conditions for bootstrapping purposes
%bcond_without docs
%bcond_without tests

Name:           python-simplejson
Version:        3.18.1
Release:        %autorelease
Summary:        Simple, fast, extensible JSON encoder/decoder for Python

# The main code is licensed MIT.
# The docs include jquery which is licensed MIT or GPLv2
License:        (MIT or AFL) and (MIT or GPLv2)
URL:            https://github.com/simplejson/simplejson
Source0:        %{pypi_source simplejson}

%description
simplejson is a simple, fast, complete, correct and extensible JSON
<http://json.org> encoder and decoder for Python. It is pure Python code
with no dependencies, but includes an optional C extension for a serious speed
boost.

The encoder may be subclassed to provide serialization in any kind of
situation, without any special support by the objects to be serialized
(somewhat like pickle).

The decoder can handle incoming JSON strings of any specified encoding (UTF-8
by default).

simplejson is the externally maintained development version of the JSON library
included with Python. It gets updated more regularly than the JSON module in
the Python stdlib.

%package -n python3-simplejson
Summary:        Simple, fast, extensible JSON encoder/decoder for Python 3
BuildRequires: gcc
BuildRequires: python3-devel
BuildRequires: python3-setuptools
%if %{with tests}
BuildRequires: python3-pytest
%endif
%if %{with docs}
BuildRequires: python3-sphinx
%endif
%{?python_provide:%python_provide python3-simplejson}

%description -n python3-simplejson
simplejson is a simple, fast, complete, correct and extensible JSON
<http://json.org> encoder and decoder for Python. It is pure Python code
with no dependencies, but includes an optional C extension for a serious speed
boost.

The encoder may be subclassed to provide serialization in any kind of
situation, without any special support by the objects to be serialized
(somewhat like pickle).

The decoder can handle incoming JSON strings of any specified encoding (UTF-8
by default).

simplejson is the externally maintained development version of the JSON library
included with Python. It gets updated more regularly than the JSON module in
the Python stdlib.

%prep
%setup -q -n simplejson-%{version}

%build
%py3_build

%if %{with docs}
PATH=%{_libexecdir}/python3-sphinx:$PATH %{__python3} scripts/make_docs.py

rm docs/.buildinfo
rm docs/.nojekyll
%endif

%install
%py3_install

%if %{with tests}
%check
%pytest
%endif

%files -n python3-simplejson
%license LICENSE.txt
%if %{with docs}
%doc docs
%endif
%{python3_sitearch}/simplejson/
%{python3_sitearch}/simplejson-*.egg-info/

%changelog
%autochangelog
