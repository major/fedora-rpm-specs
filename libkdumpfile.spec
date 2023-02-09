%global mainlibsover 10
%global addrlibsover 3

Name:           libkdumpfile
Version:        0.5.1
Release:        %autorelease
Summary:        Kernel coredump file access

License:        LGPLv3+ or GPLv2+
URL:            https://github.com/ptesarik/libkdumpfile
Source:         %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  doxygen
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  libzstd-devel
BuildRequires:  lzo-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  snappy-devel
BuildRequires:  zlib-devel

%global _description %{expand:
libkdumpfile is a library to read kdump-compressed kernel core dumps.}

%description %{_description}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel %{_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}

%description    doc %{_description}

The %{name}-doc package contains documentation for %{name}.

%package -n python3-%{name}
Summary:        Python bindings for %{name}
Obsoletes:      %{name}-python < 0.4.0-6
Provides:       %{name}-python = %{version}-%{release}
Provides:       %{name}-python%{?_isa} = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python3-%{name} %{_description}

The python3-%{name} package contains Python bindings for %{name}.

%package        util
Summary:        Utilities to read kernel core dumps
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    util %{_description}
The %{name}-devel package contains misc utilities built with %{name}.


%prep
%autosetup -p1
# Remove unneeded shebang
sed -e "\|#!/usr/bin/env python|d" -i python/*/*.py


%build
%configure
%make_build
%{__make} doxygen-doc


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
# static artifacts are needed to run tests, but we don't
# want to ship them
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'


%check
%make_build check


%files
%license COPYING COPYING.GPLv2 COPYING.GPLv3 COPYING.LGPLv3
%doc README.md NEWS
%{_libdir}/libaddrxlat.so.%{addrlibsover}{,.*}
%{_libdir}/libkdumpfile.so.%{mainlibsover}{,.*}

%files devel
%{_includedir}/%{name}/
%{_libdir}/libaddrxlat.so
%{_libdir}/libkdumpfile.so
%{_libdir}/pkgconfig/libaddrxlat.pc
%{_libdir}/pkgconfig/libkdumpfile.pc

%files doc
%license COPYING COPYING.GPLv2 COPYING.GPLv3 COPYING.LGPLv3
%doc doc/html

%files -n python3-%{name}
%{python3_sitearch}/%{name}-%{version}-*.egg-info
%{python3_sitearch}/addrxlat/
%{python3_sitearch}/_addrxlat.*.so
%{python3_sitearch}/kdumpfile/
%{python3_sitearch}/_kdumpfile.*.so

%files util
%{_bindir}/dumpattr
%{_bindir}/listxendoms
%{_bindir}/showxlat

%changelog
%autochangelog
