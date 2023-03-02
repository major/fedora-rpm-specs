%bcond_without tests

Name:           jimtcl
Version:        0.82
Release:        %autorelease
Summary:        A small embeddable Tcl interpreter

License:        BSD-2-Clause-Views
URL:            http://jim.tcl.tk
Source0:        https://github.com/msteveb/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  asciidoc
BuildRequires:  make
# Extension dependencies
BuildRequires:  pkgconfig(hiredis)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(SDL2_gfx)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
%if %{with tests}
BuildRequires:  hostname
%endif

%global _description %{expand:
Jim is an opensource small-footprint implementation of the Tcl programming
language. It implements a large subset of Tcl and adds new features like 
references with garbage collection, closures, built-in Object Oriented 
Programming system, Functional Programming commands, first-class arrays and 
UTF-8 support.}

%description %{_description}


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel %{_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup
rm -rf sqlite3

%build
#configure is not able to locate the needed binaries, so specify it manualy
# export CC=gcc
# export LD=ld
export AR=ar
export RANLIB=ranlib
export STRIP=strip

# compile extensions that are disabled by default
# as modules
# see ./configure --extinfo for list
%configure --shared --disable-option-checking \
  --allextmod \
%ifarch s390x # zlib test fails on s390x
  --without-ext=zlib \
%endif
  --docdir=%{_datadir}/doc/%{name}
%make_build


%install
%make_install INSTALL_DOCS=nodocs
rm %{buildroot}/%{_libdir}/jim/README.extensions


%if %{with tests}
%check
# remove tests that require network access
rm tests/ssl.test
make test
%endif


%files
%license LICENSE
%doc AUTHORS README README.ensemble README.extensions README.namespaces
%doc README.oo README.redis README.sqlite README.utf-8
%doc %{_datadir}/doc/%{name}/Tcl.html
%{_bindir}/jimdb
%{_bindir}/jimsh
%dir %{_libdir}/jim
%{_libdir}/jim/*.tcl
%{_libdir}/jim/*.so
%{_libdir}/libjim.so.*


%files devel
%doc DEVELOPING STYLE
%{_includedir}/*
%{_bindir}/build-jim-ext
%{_libdir}/libjim.so
%{_libdir}/pkgconfig/jimtcl.pc

%changelog
%autochangelog
