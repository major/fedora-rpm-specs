%global srcname pyasn

Name:           python-%{srcname}
Version:        1.6.1
Release:        %autorelease
Summary:        Offline IP address to Autonomous System Number lookup module

# pyasn itself is MIT, but it builds on other projects under ISC and
# BSD-4-Clause; for details see the LICENSE file and
# https://github.com/hadiasghari/pyasn/issues/25
License:        MIT AND ISC AND BSD-4-Clause
URL:            https://github.com/hadiasghari/pyasn
# PyPI tarball doesn't include tests
Source:         %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
# Fixup commit for 1.6.1
Patch:          %{url}/commit/1d64d6d2f20e0353b46fbf5b94f8bdea8f41e9ce.patch

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
pyasn is a Python extension module that enables very fast IP address to
Autonomous System Number lookups. Current state and Historical lookups can be
done, based on the MRT/RIB BGP archive used as input.

pyasn is different from other ASN lookup tools in that it provides offline and
historical lookups. It provides utility scripts for users to build their own
lookup databases based on any MRT/RIB archive. This makes pyasn much faster
than online dig/whois/json lookups.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

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
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md BACKLOG.txt
%{_bindir}/pyasn_util_asnames.py
%{_bindir}/pyasn_util_convert.py
%{_bindir}/pyasn_util_download.py

%changelog
%autochangelog
