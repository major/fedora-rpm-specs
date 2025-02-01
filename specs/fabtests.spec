Name:           fabtests
Version:        1.22.0
Release:        %autorelease
Summary:        Test suite for libfabric API
# COPYING says the license is your choice of BSD or GPLv2.
# include/jsmn.h and common/jsmn.c are licensed under MIT.
License:        (BSD-2-Clause OR GPL-2.0-only) AND MIT
Url:            https://github.com/ofiwg/libfabric
Source:         https://github.com/ofiwg/libfabric/releases/download/v%{version}/%{name}-%{version}.tar.bz2
Patch0:         0001-adjust-shebang-lines-in-rft_yaml_to_junit_xml-and-ru.patch
Patch1:		0001-Fix-build-failure.patch
BuildRequires:  libfabric-devel >= %{version}
%ifarch %{valgrind_arches}
BuildRequires:  valgrind-devel
%endif
BuildRequires:  gcc
BuildRequires:  make
Requires:       python3-pytest

%description
Fabtests provides a set of examples that uses libfabric - a high-performance
fabric software library.

%prep
%setup -q -n %{name}-%{version}
%patch -P0 -p2
%patch -P1 -p2

%build
%configure \
%ifarch %{valgrind_arches}
  --with-valgrind
%endif

make %{?_smp_mflags} V=1

%install
%make_install
# remove unpackaged files from the buildroot
rm -f %{buildroot}%{_libdir}/*.la

%files
%{_datadir}/%{name}/
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man7/*
%doc AUTHORS README
%license COPYING

%changelog
%autochangelog
