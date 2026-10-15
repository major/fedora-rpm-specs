Summary:	Library and frontend for decoding MPEG2/4 AAC
Name:		faad2
Epoch:		1
Version:	2.11.4
Release:	%autorelease
License:	GPL-2.0-or-later
URL:		https://github.com/knik0/faad2/
Source:		https://github.com/knik0/faad2/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	libsysfs-devel

Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-xmms < %{version}-%{release}

%description
FAAD 2 is a LC, MAIN and LTP profile, MPEG2 and MPEG-4 AAC decoder, completely
written from scratch.

%package libs
Summary:	Shared libraries of the FAAD 2 AAC decoder

%description libs
FAAD 2 is a LC, MAIN and LTP profile, MPEG2 and MPEG-4 AAC decoder, completely
written from scratch.

This package contains libfaad.

%package devel
Summary:	Development libraries of the FAAD 2 AAC decoder
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
FAAD 2 is a LC, MAIN and LTP profile, MPEG2 and MPEG-4 AAC decoder, completely
written from scratch.

This package contains development files and documentation for libfaad.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
install -m 0755 -d %{buildroot}%{_mandir}/man3
install -D -m 644 docs/libfaad.3 -t %{buildroot}%{_mandir}/man3/

%files
%doc AUTHORS ChangeLog README
%{_bindir}/faad
%{_mandir}/man1/faad.1*

%files libs
%license COPYING
%{_libdir}/libfaad.so.2{,.*}
%{_libdir}/libfaad_drm.so.2{,.*}

%files devel
%{_includedir}/faad.h
%{_includedir}/neaacdec.h
%{_libdir}/pkgconfig/faad2.pc
%{_libdir}/libfaad.so
%{_libdir}/libfaad_drm.so
%{_mandir}/man3/libfaad.3*

%changelog
%autochangelog
