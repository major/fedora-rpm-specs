Name: libtfmxaudiodecoder
Version: 1.0.2
Release: 1%{?dist}

Summary: C wrapper library for TFMX & FC music files
License: GPL-2.0-or-later
URL: https://github.com/mschwendt/libtfmxaudiodecoder
Source0: https://github.com/mschwendt/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc-c++
BuildRequires: libtool
BuildRequires: make

%description
This music player backend library provides a C API for TFMX and
Future Composer music files from the Commodore Amiga era of computing.


%package devel
Summary: Files needed for developing with %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the files that are needed when building
software that uses %{name}.


%prep
%autosetup -p1

%build
%configure --disable-static
%make_build


%install
%make_install


%files
%license COPYING
%doc README.md README_BAD.md TFMX.md TFMX_HIP_FC.md
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/tfmxaudiodecoder.h


%changelog
* Sat Feb 07 2026 Michael Schwendt <mschwendt@fedoraproject.org> - 1.0.2-1
- update to 1.0.2

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Dec 19 2025 Michael Schwendt <mschwendt@fedoraproject.org> - 1.0.1-1
- update to 1.0.1

* Mon Dec 01 2025 Michael Schwendt <mschwendt@fedoraproject.org> - 1.0.0-1
- update to 1.0.0 release

* Fri Nov 14 2025 Michael Schwendt <mschwendt@fedoraproject.org> - 1.0.0-0.2.20251114git9634c94
- latest snapshot, also for Audacious plugin

* Sun Nov 09 2025 Michael Schwendt <mschwendt@fedoraproject.org> - 1.0.0-0.2.20251109gitcdd9b3a
- latest snapshot

* Tue Nov 04 2025 Michael Schwendt <mschwendt@fedoraproject.org> - 1.0.0-0.2.20251104git740c78b
- spec changes as suggested during Fedora review

* Tue Nov 04 2025 Michael Schwendt <mschwendt@fedoraproject.org> - 1.0.0-0.1.20251104git740c78b
- update snapshot

* Mon Nov 03 2025 Michael Schwendt <mschwendt@fedoraproject.org> - 1.0.0-0.1.20251103gita03654e
- update FSF address in all source files to please rpmlint

* Sun Nov 02 2025 Michael Schwendt <mschwendt@fedoraproject.org> - 1.0.0-0.1.20251102git7f0a34d
- create spec file based on libfc14audiodecoder.spec
