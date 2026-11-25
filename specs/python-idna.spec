%global srcname idna

# hypothesis is not available on RHEL
%bcond hypothesis %{undefined rhel}

Name:           python-%{srcname}
Version:        3.20
Release:        %autorelease
Summary:        Internationalized Domain Names in Applications (IDNA)

License:        BSD-3-Clause
URL:            https://github.com/kjd/idna
Source:         https://pypi.io/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz

# Classify a non-canonical "fake" A-label such as xn---bbk as non_canonical_alabel
# rather than invalid_alabel. Python 3.16 made the punycode decoder reject a
# leading delimiter outright (https://github.com/python/cpython/issues/161090),
# which changed the error code and broke the test suite (rhbz#2576582).
# Proposed upstream.
Patch:          https://github.com/kjd/idna/pull/288.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
%if %{with hypothesis}
BuildRequires:  python3dist(hypothesis)
%endif

%description
A library to support the Internationalised Domain Names in Applications (IDNA)
protocol as specified in RFC 5891 <http://tools.ietf.org/html/rfc5891>.  This
version of the protocol is often referred to as "IDNA2008" and can produce
different results from the earlier standard from 2003.

The library is also intended to act as a suitable drop-in replacement for the
"encodings.idna" module that comes with the Python standard library but
currently only supports the older 2003 specification.

%package -n python3-%{srcname}
Summary:        Internationalized Domain Names in Applications (IDNA)

%description -n python3-%{srcname}
A library to support the Internationalised Domain Names in Applications (IDNA)
protocol as specified in RFC 5891 <http://tools.ietf.org/html/rfc5891>.  This
version of the protocol is often referred to as "IDNA2008" and can produce
different results from the earlier standard from 2003.

The library is also intended to act as a suitable drop-in replacement for the
"encodings.idna" module that comes with the Python standard library but
currently only supports the older 2003 specification.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%if %{without hypothesis}
%pytest --ignore=tests/test_idna_properties.py
%else
%pytest
%endif

%files -n python3-%{srcname} -f %pyproject_files
%license LICENSE.md
%doc README.md
%{_bindir}/%{srcname}

%changelog
%autochangelog
