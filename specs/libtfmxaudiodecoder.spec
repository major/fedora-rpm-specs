%global commit 9634c9486f483f899ee97e703cec6887d6ad55b5
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name: libtfmxaudiodecoder
Version: 1.0.0
Release: 0.2.20251114git%{shortcommit}%{?dist}

Summary: C wrapper library for TFMX & FC music files
License: GPL-2.0-or-later
URL: https://github.com/mschwendt/libtfmxaudiodecoder
#Source0: https://github.com/mschwendt/%%{name}/releases/download/%%{name}-%%{version}/%%{name}-%%{version}.tar.bz2
Source0: https://github.com/mschwendt/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

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
%autosetup -p1 -n %{name}-%{commit}

%build
# Snapshots don't include pregenerated Autotools files.
autoreconf -f -i
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
* Fri Nov 14 2025 Michael Schwendt  <mschwendt@fedoraproject.org> - 1.0.0-0.2.20251114git9634c94
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
