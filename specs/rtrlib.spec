Name:           rtrlib
Version:        0.8.0
Release:        2%{?dist}
Summary:        Small extensible RPKI-RTR-Client C library
Group:          Development/Libraries
License:        MIT AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause
URL:            http://rpki.realmv6.org/
Source0:        https://github.com/rtrlib/rtrlib/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  binutils
BuildRequires:  gcc
BuildRequires:  tar
BuildRequires:  cmake 
BuildRequires:  libssh-devel >= 0.5.0
BuildRequires:  doxygen
BuildRequires:  git-core
BuildRequires:  libcmocka
Requires:       libssh >= 0.5.0

Patch0: disable-live-tests.patch

%description
RTRlib is an open-source C implementation of the  RPKI/Router Protocol
client. The library allows one to fetch and store validated prefix origin
data from a RTR-cache and performs origin verification of prefixes. It
supports different types of transport sessions (e.g., SSH, unprotected TCP)
and is easily extendable.

%package devel
Summary:        Small extensible RPKI-RTR-Client C library. Development files
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libssh-devel >= 0.5.0

%description devel
RTRlib is an open-source C implementation of the  RPKI/Router Protocol
client. The library allows one to fetch and store validated prefix origin
data from a RTR-cache and performs origin verification of prefixes. It
supports different types of transport sessions (e.g., SSH, unprotected TCP)
and is easily extendable.

This package contains development files.

%package doc
Summary:        Small extensible RPKI-RTR-Client C library. Documentation
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
RTRlib is an open-source C implementation of the  RPKI/Router Protocol
client. The library allows one to fetch and store validated prefix origin
data from a RTR-cache and performs origin verification of prefixes. It
supports different types of transport sessions (e.g., SSH, unprotected TCP)
and is easily extendable.
.
This package contains documentation files.

%package -n rtr-tools
Summary:        RPKI-RTR command line tools
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n rtr-tools
Tools for the RTRlib
Rtrclient is command line that connects to an RPKI-RTR server and prints
protocol information and information about the fetched ROAs to the console.
Rpki-rov is a command line tool that connects to an RPKI-RTR server and
allows to validate given IP prefixes and origin ASes.

%prep
%autosetup -S git -n %{name}-%{version}

%build
%cmake -DCMAKE_BUILD_TYPE=Release .
%cmake_build %{?_smp_mflags}

%install
%cmake_install

%ldconfig_scriptlets

%check
%cmake_build --target test

%files
%{_libdir}/lib*.so.0
%{_libdir}/lib*.so.0.*
%doc CHANGELOG
%license LICENSE

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/rtrlib.pc
%{_includedir}/rtrlib
%doc CHANGELOG
%license LICENSE

%files doc
%{_docdir}/rtrlib

%files -n rtr-tools
%{_bindir}/rtrclient
%{_bindir}/rpki-rov
%{_mandir}/man1/rtrclient.1.gz
%{_mandir}/man1/rpki-rov.1.gz
%doc CHANGELOG
%license LICENSE

%changelog
* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Oct 30 2025 Michal Ruprich <mruprich@redhat.com> - 0.8.0-1
- Initial package import

* Sun Mar 15 2020 Martin Winter <mwinter@opensourcerouting.org> - 0.8.0-1
- Update RPM spec changelog to fix changelog error

* Thu Dec 14 2017 Martin Winter <mwinter@opensourcerouting.org> - 0.5.0-1
- RPM Packaging added
