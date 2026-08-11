%bcond mingw %{undefined rhel}

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
%if %{with mingw}
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-libtiff
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-libtiff
%endif

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

%if %{with mingw}
%package -n mingw32-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch

%description -n mingw32-%{name}
%{summary}.

%package -n mingw64-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch

%description -n mingw64-%{name}
%{summary}.

%{?mingw_debug_package}
%endif

%prep
%autosetup -p1 -n %{name}

%build
%cmake -DOPTIMIZE=ACCURACY
%cmake_build
%if %{with mingw}
%mingw_cmake -DCMAKE_DLL_NAME_WITH_SOVERSION=ON
%mingw_make_build
%endif

%install
%cmake_install
%if %{with mingw}
%mingw_make_install
%mingw_debug_install_post
%endif

%files
%doc CHANGES CREDITS README.md TODO
%license COPYING COPYRIGHT
%{_libdir}/libmad.so.0{,.*}

%files devel
%{_libdir}/libmad.so
%{_libdir}/cmake/mad/
%{_libdir}/pkgconfig/mad.pc
%{_includedir}/mad.h

%if %{with mingw}
%files -n mingw32-%{name}
%license COPYING COPYRIGHT
%{mingw32_bindir}/%{name}-0.dll
%{mingw32_libdir}/%{name}.dll.a
%{mingw32_libdir}/cmake/mad/
%{mingw32_libdir}/pkgconfig/mad.pc
%{mingw32_includedir}/mad.h

%files -n mingw64-%{name}
%license COPYING COPYRIGHT
%{mingw64_bindir}/%{name}-0.dll
%{mingw64_libdir}/%{name}.dll.a
%{mingw64_libdir}/cmake/mad/
%{mingw64_libdir}/pkgconfig/mad.pc
%{mingw64_includedir}/mad.h
%endif

%changelog
%autochangelog
