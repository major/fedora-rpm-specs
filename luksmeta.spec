Name:           luksmeta
Version:        9
Release:        %autorelease
Summary:        Utility for storing small metadata in the LUKSv1 header

License:        LGPL-2.1-or-later
URL:            https://github.com/latchset/%{name}
Source0:        https://github.com/latchset/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.bz2

Patch01: luksmeta-9-tests.patch
Patch02: luksmeta-9-relax-layout-assumptions.patch
Patch03: Define-log-callback-function-to-use-with-libcryptset.patch

BuildRequires:  gcc
BuildRequires:  asciidoc
BuildRequires:  pkgconfig
BuildRequires:  cryptsetup-devel
BuildRequires:  cryptsetup
BuildRequires: make
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description
LUKSMeta is a command line utility for storing small portions of metadata in
the LUKSv1 header for use before unlocking the volume.

%package -n lib%{name}
Summary:        Library for storing small metadata in the LUKSv1 header

%description -n lib%{name}
LUKSMeta is a C library for storing small portions of metadata in the LUKSv1
header for use before unlocking the volume.

%package -n lib%{name}-devel
Summary:        Development files for libluksmeta
Requires:       lib%{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description -n lib%{name}-devel
This package contains development files for the LUKSMeta library.

%prep
%autosetup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -rf %{buildroot}/%{_libdir}/libluksmeta.la

%check
make %{?_smp_mflags} check

%ldconfig_scriptlets -n lib%{name}

%files
%{_bindir}/luksmeta
%{_mandir}/man8/luksmeta.8*

%files -n lib%{name}
%license COPYING
%{_libdir}/libluksmeta.so.*

%files -n lib%{name}-devel
%{_includedir}/luksmeta.h
%{_libdir}/libluksmeta.so
%{_libdir}/pkgconfig/luksmeta.pc

%changelog
%autochangelog
