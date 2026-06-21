%global mainlibsover 12
%global addrlibsover 3

Name:           libkdumpfile
Version:        0.5.6
Release:        %autorelease
Summary:        Kernel coredump file access

License:        LGPL-3.0-or-later OR GPL-2.0-or-later
URL:            https://codeberg.org/ptesarik/libkdumpfile
Source:         %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
# drop macros removed from binutils 2.46
Patch:          drop-bfd-true-false-macros.diff

BuildRequires:  gcc-c++
BuildRequires:  doxygen
BuildRequires:  make
BuildRequires:  binutils-devel
BuildRequires:  libzstd-devel
BuildRequires:  lzo-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
# this last existed in Fedora 41 and EL 9
%if 0%{?fedora} < 44
Obsoletes:      python3-libkdumpfile < 0.5.5-1
%endif
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
BuildArch:      noarch
# keep this until F38 is EOL (so Fedora < 41) as 0.5.1 was not noarch due to
# doxygen being run *after* rather than *before* build so it indexes "built"
# Python sources too
# likewise, EPEL 8 and 9 are affected
%if (0%{?fedora} && 0%{?fedora} < 41) || (0%{?rhel} && 0%{?rhel} < 10)
Obsoletes:      %{name}-doc < 0.5.2-1
%endif

%description    doc %{_description}

The %{name}-doc package contains documentation for %{name}.

%package        util
Summary:        Utilities to read kernel core dumps
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    util %{_description}
The %{name}-devel package contains misc utilities built with %{name}.


%prep
%autosetup -p1


%conf
autoreconf -fiv


%build
%configure

%{__make} doxygen-doc
%make_build


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

%files util
%{_bindir}/dumpattr
%{_bindir}/kdumpid
%{_bindir}/listxendoms
%{_bindir}/showxlat
%{_mandir}/man1/kdumpid.1*

%changelog
%autochangelog
