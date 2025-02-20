%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}

Name: xpa
Version: 2.1.20
Release: %autorelease
Summary: The X Public Access messaging system

License: MIT
URL: http://hea-www.harvard.edu/RD/xpa/
Source0: https://github.com/ericmandel/xpa/archive/%{version}/%{name}-%{version}.tar.gz
Patch0: xpa-makefile.patch
Patch1: xpa-configure-c99.patch

BuildRequires: gcc
BuildRequires: make
BuildRequires: libXt-devel
BuildRequires: tcl8-devel

Requires: tcl(abi) = 8.6

%description
The XPA messaging system provides seamless communication between many kinds 
of Unix programs, including X programs and Tcl/Tk programs. 
It also provides an easy way for users to communicate with these 
XPA-enabled programs by executing XPA client commands in the shell or by 
utilizing such commands in scripts.
This package contains command-line utilities for managing XPA.

%package devel
Summary: Headers for developing programs that will use %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-tcl%{?_isa} = %{version}-%{release}

%description devel
These are the header files and libraries needed to develop a %{name} 
application.

%package libs
Summary: The XPA messaging system runtime libraries
%description libs
The XPA messaging system provides seamless communication between many kinds 
of Unix programs, including X programs and Tcl/Tk programs. 
This package contains the %{name} run-time library

%package tcl
Summary: The XPA messaging system TCL interface
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Provides: tcl-xpa = %{version}-%{release}
%description tcl
The XPA messaging system provides seamless communication between many kinds 
of Unix programs, including X programs and Tcl/Tk programs. 
This package contains the %{name} TCL interface

%package doc
Summary: Documentation for %{name}
BuildArch: noarch

%description doc
This package contains the documentation for %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}
# Remove ps files in html docs
rm -rf %{_builddir}/%{name}-%{version}/doc/*.ps

%build
%configure --includedir=%{_includedir}/xpa --datadir=%{_datadir}/xpa \
	--enable-shared --with-tcl=%{_libdir} \
	--with-x --enable-threaded-xpans
# Race condition
# the utilities are built before the shared library
# and linked with the static library
#make %{?_smp_mflags}
make 
#make %{?_smp_mflags} tclxpa
make tclxpa

%install
make INSTALL_ROOT=%{buildroot} install
mkdir -p %{buildroot}%{tcl_sitearch}/tclxpa
cp -a pkgIndex.tcl %{buildroot}%{tcl_sitearch}/tclxpa
mv %{buildroot}%{_libdir}/libtcl* %{buildroot}%{tcl_sitearch}/tclxpa

%ldconfig_scriptlets libs

%files
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%{name}

%files libs
%license LICENSE
%{_libdir}/libxpa.so.*

%files tcl
%{tcl_sitearch}/tclxpa

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/xpa.pc
%{_includedir}/*
%{_mandir}/man3/*
%{_mandir}/mann/*
%exclude %{_libdir}/*.a

%files doc
%license LICENSE
%doc doc/*.html
#%doc doc/*.pdf

%changelog
%autochangelog
