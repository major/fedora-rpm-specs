# Build conditions for bootstrapping purposes
%bcond_without docs
%bcond_without tests

Name:           python-simplejson
Version:        3.18.3
Release:        %autorelease
Summary:        Simple, fast, extensible JSON encoder/decoder for Python

# The main code is licensed MIT.
# The docs include jquery which is licensed MIT or GPLv2
License:        (MIT or AFL) and (MIT or GPLv2)
URL:            https://github.com/simplejson/simplejson
Source0:        %{pypi_source simplejson}

%global _description \
simplejson is a simple, fast, complete, correct and extensible JSON\
<http://json.org> encoder and decoder for Python. It is pure Python code\
with no dependencies, but includes an optional C extension for a serious speed\
boost.\
\
The encoder may be subclassed to provide serialization in any kind of\
situation, without any special support by the objects to be serialized\
(somewhat like pickle).\
\
The decoder can handle incoming JSON strings of any specified encoding (UTF-8\
by default).\
\
simplejson is the externally maintained development version of the JSON library\
included with Python. It gets updated more regularly than the JSON module in\
the Python stdlib.

%description %{_description}

%package -n python%{python3_pkgversion}-simplejson
Summary:        Simple, fast, extensible JSON encoder/decoder for Python 3
%{?python_provide:%python_provide python%{python3_pkgversion}-simplejson}
BuildRequires: gcc
BuildRequires: python%{python3_pkgversion}-devel
%if %{with tests}
BuildRequires: python%{python3_pkgversion}-pytest
%endif

%if %{with docs}
%package -n python-simplejson-doc
Summary:        simplejson documentation

BuildRequires: python%{python3_pkgversion}-sphinx

%description -n python-simplejson-doc
Documentation for simplejson
%endif

%description -n python%{python3_pkgversion}-simplejson %{_description}

%generate_buildrequires
%pyproject_buildrequires

%prep
%setup -q -n simplejson-%{version}

%build
%pyproject_wheel

%if %{with docs}
PYTHONPATH=%{pyproject_build_lib} %{__python3} scripts/make_docs.py
rm -f docs/.{buildinfo,nojekyll}
%endif

%install
%pyproject_install
%pyproject_save_files simplejson

%if %{with tests}
%check
%pytest
%endif

%files -n python%{python3_pkgversion}-simplejson -f %{pyproject_files}
%license LICENSE.txt

%if %{with docs}
%files -n python-simplejson-doc
%doc docs
%endif

%changelog
%autochangelog
