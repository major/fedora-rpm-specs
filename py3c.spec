# A header-only library has no debuginfo
%global debug_package %{nil}

Name:           py3c
Version:        1.4
Release:        %autorelease
Summary:        Guide and compatibility macros for porting extensions to Python 3

# Licences differ for subpackages
License:        MIT AND CC-BY-SA-3.0

URL:            http://py3c.readthedocs.io/

Source0:        https://github.com/encukou/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme >= 0.4.3

%description
py3c helps you port C extensions to Python 3.

It provides a detailed guide, and a set of macros to make porting easy
and reduce boilerplate.

%package        devel
License:        MIT
Summary:        Header files for py3c

Requires:       python3-devel

# A header-only library counts as static
Provides:       %{name}-static = %{version}-%{release}
%{?_isa:Provides: %{name}-static%{?_isa} = %{version}-%{release}}

%description devel
%{name}-devel is only required for building software that uses py3c.
Because py3c is a header-only library, there is no matching run-time package.

%package        doc
BuildArch:      noarch
License:        CC-BY-SA-3.0
Summary:        Guide for porting C extensions to Python 3

%description doc
Guide for porting CPython extensions from Python 2 to Python 3, using the
py3c macros.

%prep
%setup -q

%build
%make_build py3c.pc includedir=%{_includedir}

%make_build doc SPHINXBUILD=sphinx-build-3

%check
%make_build test-python3

%install
make install prefix=%{buildroot}%{_prefix} includedir=%{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_pkgdocdir}
cp -rv doc/build/html/* %{buildroot}%{_pkgdocdir}

# Strip buildroot name from the pkgconfig file
sed --in-place -e's!%{buildroot}!!' %{buildroot}%{_datadir}/pkgconfig/py3c.pc

%files devel
%license LICENSE.MIT
%doc README.rst
%{_includedir}/py3c.h
%{_includedir}/py3c/
%{_datadir}/pkgconfig/py3c.pc

%files doc
%license doc/LICENSE.CC-BY-SA-3.0
%doc %{_pkgdocdir}/

%changelog
%autochangelog
