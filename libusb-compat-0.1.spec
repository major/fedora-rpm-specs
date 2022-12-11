Name:           libusb-compat-0.1
Version:        0.1.8
Release:        %autorelease -b 0
Summary:        Compatibility shim around libusb-1.0 offering the old 0.1 API
License:        LGPLv2+
URL:            https://github.com/libusb/libusb-compat-0.1
Source0:        https://github.com/libusb/libusb-compat-0.1/releases/download/v%{version}/libusb-compat-%{version}.tar.bz2
Patch0:         libusb-config-multilib.patch
BuildRequires:  gcc libtool
BuildRequires:  libusb1-devel
BuildRequires:  make
Provides:       deprecated()
# libusb was removed in F34
Provides:       libusb = 1:%{version}-%{release}
Obsoletes:      libusb < 1:%{version}-%{release}
# libusb-compat-0.1 version 0.1.6 and later dlopen'ed the library
Requires:       libusb1%{?_isa}

%description
This package provides a shim / compatibility layer on top of libusb1
offering the old 0.1 API for applications which do not have been ported
to the new 1.0 API yet. Where ever possible applications really should
use and / or be ported to the new 1.0 API instead of relying on this
compatibility library.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      libusb-devel < 1:%{version}-%{release}

%description devel
This package contains the header files, libraries and documentation needed to
develop applications that use libusb-0.1. However new applications should use
libusb-1.0 library instead of this one.


%package        tests-examples
Summary:        Tests and examples for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       libusb-tests-examles = 1:%{version}-%{release}
Obsoletes:      libusb-tests-examles < 1:%{version}-%{release}

%description tests-examples
This package contains tests and examples for %{name}.


%prep
%autosetup -n libusb-compat-%{version}
autoreconf -ivf


%build
%configure --disable-static --enable-examples-build
%make_build


%install
%make_install
rm $RPM_BUILD_ROOT%{_libdir}/libusb.la
for i in lsusb testlibusb; do
    install -m 755 examples/.libs/$i \
        $RPM_BUILD_ROOT%{_bindir}/libusb-compat-0.1-$i
done


%check
LD_LIBRARY_PATH=libusb/.libs ldd -r $RPM_BUILD_ROOT%{_bindir}/libusb-compat-0.1-lsusb
LD_LIBRARY_PATH=libusb/.libs $RPM_BUILD_ROOT%{_bindir}/libusb-compat-0.1-lsusb
LD_LIBRARY_PATH=libusb/.libs $RPM_BUILD_ROOT%{_bindir}/libusb-compat-0.1-testlibusb


%ldconfig_scriptlets


%files
%doc AUTHORS NEWS README
%license COPYING
%{_libdir}/libusb-0.1.so.*

%files devel
%{_includedir}/usb.h
%{_libdir}/libusb.so
%{_libdir}/pkgconfig/libusb.pc
%{_bindir}/libusb-config

%files tests-examples
%{_bindir}/libusb-compat-0.1-lsusb
%{_bindir}/libusb-compat-0.1-testlibusb


%changelog
%autochangelog
