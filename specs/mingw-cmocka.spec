%?mingw_package_header

Name:           mingw-cmocka
Version:        1.1.8
Release:        %autorelease
Summary:        MinGW Lightweight library to simplify and generalize unit tests for C

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://www.cmocka.org/

Source0:        https://cmocka.org/files/1.1/cmocka-%{version}.tar.xz
Source1:        https://cmocka.org/files/1.1/cmocka-%{version}.tar.xz.asc
Source2:        cmocka.keyring

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  gpgverify
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++

BuildRequires:  cmake
BuildRequires:  pkgconfig


%description
Lightweight library to simplify and generalize unit tests for C.
This library is cross-compiled for MinGW.


# Win32
%package -n mingw32-cmocka
Summary:        MinGW GnuTLS TLS/SSL encryption library
Requires:       pkgconfig

%description -n mingw32-cmocka
Lightweight library to simplify and generalize unit tests for C.
This library is cross-compiled for MinGW.

# Win64
%package -n mingw64-cmocka
Summary:        MinGW GnuTLS TLS/SSL encryption library
Requires:       pkgconfig

%description -n mingw64-cmocka
Lightweight library to simplify and generalize unit tests for C.
This library is cross-compiled for MinGW.

# Win32/static
%package -n mingw32-cmocka-static
Summary:        Static version of the MinGW Windows cmocka library
Requires:       mingw32-cmocka = %{version}-%{release}

%description -n mingw32-cmocka-static
Static version of the MinGW Windows cmocka library.

# Win64/static
%package -n mingw64-cmocka-static
Summary:        Static version of the MinGW Windows cmocka library
Requires:       mingw64-cmocka = %{version}-%{release}

%description -n mingw64-cmocka-static
Static version of the MinGW Windows cmocka library.


%?mingw_debug_package


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n cmocka-%{version}

%build
if test ! -e "obj"; then
  mkdir obj
fi
pushd obj
%mingw_cmake \
  -DWITH_STATIC_LIB=ON \
  -DWITH_CMOCKERY_SUPPORT=ON \
  -DUNIT_TESTING=ON \
  %{_builddir}/cmocka-%{version}

%mingw_make %{?_smp_mflags} VERBOSE=1
popd

%install
pushd obj
%mingw_make_install DESTDIR=%{buildroot}

%if 0%{?mingw_build_win32} == 1
cp build_win32/src/libcmocka-static.a %{buildroot}%{mingw32_libdir}/libcmocka.a
%endif
%if 0%{?mingw_build_win64} == 1
cp build_win64/src/libcmocka-static.a %{buildroot}%{mingw64_libdir}/libcmocka.a
%endif

popd
mkdir -p %{buildroot}%{mingw64_libdir}/cmake/cmocka %{buildroot}%{mingw32_libdir}/cmake/cmocka
test -d %{buildroot}%{mingw64_prefix}/CMake/cmocka && mv %{buildroot}%{mingw64_prefix}/CMake/cmocka/*.cmake %{buildroot}%{mingw64_libdir}/cmake/cmocka
test -d %{buildroot}%{mingw32_prefix}/CMake/cmocka && mv %{buildroot}%{mingw32_prefix}/CMake/cmocka/*.cmake %{buildroot}%{mingw32_libdir}/cmake/cmocka
#There is a spurious -Llib/ in the pkgconfig file
sed -i 's/-Llib//g' %{buildroot}%{mingw64_libdir}/pkgconfig/cmocka.pc
sed -i 's/-Llib//g' %{buildroot}%{mingw32_libdir}/pkgconfig/cmocka.pc
test -f %{buildroot}%{mingw64_bindir}/libcmocka.dll && mv %{buildroot}%{mingw64_bindir}/libcmocka.dll %{buildroot}%{mingw64_bindir}/cmocka.dll
test -f %{buildroot}%{mingw32_bindir}/libcmocka.dll && mv %{buildroot}%{mingw32_bindir}/libcmocka.dll %{buildroot}%{mingw32_bindir}/cmocka.dll

%files -n mingw64-cmocka-static
%{mingw64_libdir}/libcmocka.a

%files -n mingw64-cmocka
%license COPYING
%doc AUTHORS README.md ChangeLog
%{mingw64_libdir}/libcmocka.dll.a
%{mingw64_bindir}/cmocka.dll
%{mingw64_includedir}/*.h
%{mingw64_includedir}/cmockery*
%{mingw64_libdir}/pkgconfig/cmocka.pc
%{mingw64_libdir}/cmake/cmocka*

%files -n mingw32-cmocka-static
%{mingw32_libdir}/libcmocka.a

%files -n mingw32-cmocka
%license COPYING
%doc AUTHORS README.md ChangeLog
%{mingw32_libdir}/libcmocka.dll.a
%{mingw32_bindir}/cmocka.dll
%{mingw32_includedir}/*.h
%{mingw32_includedir}/cmockery*
%{mingw32_libdir}/pkgconfig/cmocka.pc
%{mingw32_libdir}/cmake/cmocka*

%changelog
%autochangelog
