Name:          libmad
Version:       0.16.4
Release:       %autorelease
Summary:       MPEG audio decoder library
License:       GPL-2.0-or-later
URL:           https://codeberg.org/tenacityteam/libmad
Source0:       %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:        %{url}/commit/326363f04e583b563f63941db3cf7f50e76aceb2.patch#/cmake_fix.patch
# fix CPU arch detection on x86
Patch1:        libmad-x86.patch
BuildRequires: cmake
BuildRequires: gcc-c++

%description
MAD is a high-quality MPEG audio decoder. It currently supports MPEG-1
and the MPEG-2 extension to Lower Sampling Frequencies, as well as the
so-called MPEG 2.5 format. All three audio layers (Layer I, Layer II,
and Layer III a.k.a. MP3) are fully implemented.

%package devel
Summary:       MPEG audio decoder library development files
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -p1 -n %{name}

%build
%cmake -DOPTIMIZE=ACCURACY
%cmake_build

%install
%cmake_install

%files
%doc CHANGES CREDITS README.md TODO
%license COPYING COPYRIGHT
%{_libdir}/libmad.so.0{,.*}

%files devel
%{_libdir}/libmad.so
%{_libdir}/cmake/mad/
%{_libdir}/pkgconfig/mad.pc
%{_includedir}/mad.h

%changelog
%autochangelog
