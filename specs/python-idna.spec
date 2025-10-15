%global srcname idna

Name:           python-%{srcname}
Version:        3.11
Release:        %autorelease
Summary:        Internationalized Domain Names in Applications (IDNA)

License:        BSD-3-Clause
URL:            https://github.com/kjd/idna
Source0:        https://pypi.io/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

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
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

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
# Remove bundled egg-info
rm -rf %{srcname}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pytest

%files -n python3-%{srcname} -f %pyproject_files
%license LICENSE.md
%doc README.rst

%changelog
%autochangelog
