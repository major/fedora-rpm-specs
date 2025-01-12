%bcond mingw %[0%{?fedora} && !0%{?flatpak}]

Summary:        Library for accessing USB devices
Name:           libusb1
Version:        1.0.27
Release:        %autorelease
Source0:        https://github.com/libusb/libusb/releases/download/v%{version}/libusb-%{version}.tar.bz2
License:        LGPL-2.1-or-later
URL:            http://libusb.info
BuildRequires:  systemd-devel doxygen libtool
BuildRequires:  umockdev-devel
BuildRequires:  make
BuildRequires:  gcc
# libusbx was removed in F34
Provides:       libusbx = %{version}-%{release}
Obsoletes:      libusbx < %{version}-%{release}

%if %{with mingw}
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc-c++
%endif

%description
This package provides a way for applications to access USB devices.

libusb is a library for USB device access from Linux, macOS,
Windows, OpenBSD/NetBSD, Haiku and Solaris userspace.

libusb is abstracted internally in such a way that it can hopefully
be ported to other operating systems.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       libusbx-devel = %{version}-%{release}
Obsoletes:      libusbx-devel < %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package devel-doc
Summary:        Development files for %{name}
Requires:       libusb1-devel = %{version}-%{release}
Provides:       libusbx-devel-doc = %{version}-%{release}
Obsoletes:      libusbx-devel-doc < %{version}-%{release}
BuildArch:      noarch

%description devel-doc
This package contains API documentation for %{name}.


%package        tests-examples
Summary:        Tests and examples for %{name}
# The fxload example is GPLv2+, the rest is LGPLv2+, like libusb itself.
License:        LGPLv2+ and GPLv2+
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       libusbx-tests-examples = %{version}-%{release}
Obsoletes:      libusbx-tests-examples < %{version}-%{release}

%description tests-examples
This package contains tests and examples for %{name}.

%if %{with mingw}
%package -n mingw32-%{name}
Summary:       MinGW Windows %{name} library

%description -n mingw32-%{name}
MinGW Windows %{name} library.

%package -n mingw64-%{name}
Summary:       MinGW Windows %{name} library

%description -n mingw64-%{name}
MinGW Windows %{name} library.
%endif

%prep
%autosetup -p1 -n libusb-%{version}
chmod -x examples/*.c
mkdir -p m4
sed -i '/AM_LDFLAGS = -static/d' tests/Makefile.am
%if 0%{fedora} >= 42
autoscan
aclocal
autoconf
automake --add-missing
%endif


%build
mkdir %{_target_os}
pushd %{_target_os}
%define _configure ../configure
%configure --disable-static --enable-examples-build
%{make_build}
pushd doc
make docs
popd
pushd tests
make
popd
popd

%if %{with mingw}
# MinGW build
%mingw_configure --disable-static
%mingw_make_build
%endif


%install
pushd %{_target_os}
%{make_install}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 tests/.libs/init_context $RPM_BUILD_ROOT%{_bindir}/libusb-test-init_context
install -m 755 tests/.libs/set_option $RPM_BUILD_ROOT%{_bindir}/libusb-test-set_option
install -m 755 tests/.libs/stress $RPM_BUILD_ROOT%{_bindir}/libusb-test-stress
install -m 755 tests/.libs/stress_mt $RPM_BUILD_ROOT%{_bindir}/libusb-test-stress_mt
install -m 755 tests/.libs/umockdev $RPM_BUILD_ROOT%{_bindir}/libusb-test-umockdev
install -m 755 examples/.libs/testlibusb \
    $RPM_BUILD_ROOT%{_bindir}/libusb-test-libusb
# Some examples are very device-specific / require specific hw and miss --help
# So we only install a subset of more generic / useful examples
for i in fxload listdevs xusb; do
    install -m 755 examples/.libs/$i \
        $RPM_BUILD_ROOT%{_bindir}/libusb-example-$i
done
rm $RPM_BUILD_ROOT%{_libdir}/*.la
popd

%if %{with mingw}
%mingw_make_install
%endif


%check
pushd %{_target_os}
LD_LIBRARY_PATH=libusb/.libs ldd $RPM_BUILD_ROOT%{_bindir}/libusb-test-stress
LD_LIBRARY_PATH=libusb/.libs $RPM_BUILD_ROOT%{_bindir}/libusb-test-init_context
LD_LIBRARY_PATH=libusb/.libs $RPM_BUILD_ROOT%{_bindir}/libusb-test-set_option
LD_LIBRARY_PATH=libusb/.libs $RPM_BUILD_ROOT%{_bindir}/libusb-test-stress
LD_LIBRARY_PATH=libusb/.libs $RPM_BUILD_ROOT%{_bindir}/libusb-test-umockdev
LD_LIBRARY_PATH=libusb/.libs $RPM_BUILD_ROOT%{_bindir}/libusb-test-libusb
LD_LIBRARY_PATH=libusb/.libs $RPM_BUILD_ROOT%{_bindir}/libusb-example-listdevs
popd


%ldconfig_scriptlets


%files
%license COPYING
%doc AUTHORS README ChangeLog
%{_libdir}/*.so.*

%files devel
%{_includedir}/libusb-1.0
%{_libdir}/*.so
%{_libdir}/pkgconfig/libusb-1.0.pc

%files devel-doc
%doc %{_target_os}/doc/api-1.0 examples/*.c

%files tests-examples
%{_bindir}/libusb-example-fxload
%{_bindir}/libusb-example-listdevs
%{_bindir}/libusb-example-xusb
%{_bindir}/libusb-test-init_context
%{_bindir}/libusb-test-set_option
%{_bindir}/libusb-test-stress
%{_bindir}/libusb-test-stress_mt
%{_bindir}/libusb-test-umockdev
%{_bindir}/libusb-test-libusb

%if %{with mingw}
%files -n mingw32-libusb1
%license COPYING
%doc AUTHORS README ChangeLog
%{mingw32_bindir}/libusb-1.0.dll
%{mingw32_includedir}/libusb-1.0
%{mingw32_libdir}/*.dll.a
%{mingw32_libdir}/pkgconfig/libusb-1.0.pc

%files -n mingw64-libusb1
%license COPYING
%doc AUTHORS README ChangeLog
%{mingw64_bindir}/libusb-1.0.dll
%{mingw64_includedir}/libusb-1.0
%{mingw64_libdir}/*.dll.a
%{mingw64_libdir}/pkgconfig/libusb-1.0.pc
%endif

%changelog
%autochangelog
