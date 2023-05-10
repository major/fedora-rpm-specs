Name:       libltc
Version:    1.3.2
Release:    %autorelease
Summary:    Linear/Longitudinal Time Code (LTC) Library

License:    LGPLv3+
URL:        http://x42.github.io/libltc/
Source0:    https://github.com/x42/%{name}/releases/download/v%{version}/libltc-%{version}.tar.gz
# Don't timestamp built HTML documentation, probably Fedora specific
Patch0:     libltc-1.3.2-multilib.patch

BuildRequires: gcc
BuildRequires: doxygen
BuildRequires: make

%description
Linear (or Longitudinal) Timecode (LTC) is an encoding of time code data as a
Manchester-Biphase encoded audio signal. The audio signal is commonly recorded
on a VTR track or other storage media.

libltc provides functionality to encode and decode LTC from/to time code,
including SMPTE date support.

%package devel
Summary:    Development files for libltc
Requires:   %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
This package contains the libraries and header files needed for
developing with libltc.

%prep
%setup -q
%patch -P 0 -p1 -b .multilib

%build
%configure
make %{?_smp_mflags} all dox

%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/libltc.{a,la}

%check
make check

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog COPYING README.md
%{_libdir}/libltc.so.*

%files devel
%doc doc/html
%{_libdir}/libltc.so
%{_includedir}/ltc.h
%{_libdir}/pkgconfig/ltc.pc
%{_mandir}/man3/ltc.h.3*

%changelog
%autochangelog
