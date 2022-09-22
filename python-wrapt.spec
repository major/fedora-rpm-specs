# Created by pyp2rpm-1.1.1
%global sname wrapt

%if 0%{?fedora} || 0%{?rhel} >= 8
%global with_docs 1
%endif

%{!?_licensedir: %global license %%doc}

Name:           python-%{sname}
Version:        1.14.1
Release:        %autorelease
Summary:        A Python module for decorators, wrappers and monkey patching

License:        BSD
URL:            https://github.com/GrahamDumpleton/wrapt
Source0:        https://github.com/GrahamDumpleton/%{sname}/archive/%{version}.tar.gz

BuildRequires:  gcc

BuildRequires:  python3-devel

%global _description %{expand:
The aim of the wrapt module is to provide a transparent object proxy
for Python, which can be used as the basis for the construction of
function wrappers and decorator functions.}

%description %_description

%if 0%{?with_docs}
%package doc
Summary:        Documentation for the wrapt module

BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

%description doc
Documentation for the wrapt module
%endif

%package -n python3-wrapt
Summary:        A Python module for decorators, wrappers and monkey patching
%{?python_provide:%python_provide python3-wrapt}

%description -n python3-wrapt
The aim of the wrapt module is to provide a transparent object proxy
for Python, which can be used as the basis for the construction of
function wrappers and decorator functions.

%prep
%setup -q -n %{sname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{sname}.egg-info

%build
%py3_build

%if 0%{?with_docs}
# for docs
pushd docs
sphinx-build -b html -d build/doctrees . build/html
popd
%endif

%install
%py3_install

%if 0%{?with_docs}
%files doc
%doc docs/build/html
%endif

%files -n python3-wrapt
%doc README.rst
%license LICENSE
%{python3_sitearch}/%{sname}
%{python3_sitearch}/%{sname}-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
