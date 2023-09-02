Name:           openosc
Version:        1.0.6
Release:        %autorelease
Summary:        Open Object Size Check Library
License:        Apache-2.0

%global forgeurl https://github.com/cisco/openosc
%forgemeta
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc
BuildRequires:  make

%description
OpenOSC is an open-source object size check library written in C. It has been
developed in order to promote the use of compiler builtin object size check
capability for enhanced security. It provides robust support for detecting
buffer overflows in various functions that perform operations on memory and
strings. Not all types of buffer overflows can be detected with this library,
but it does provide an extra level of validation for some functions that are
potentially a source of buffer overflow flaws. It protects both C and C++ code.


%package devel
Summary: The OpenOSC development package
Requires: openosc%{?_isa} = %{version}-%{release}

%description devel
OpenOSC development package, containing both header files and runtime library.

%package tools
Summary: The OpenOSC tools package

%description tools
OpenOSC tools package, containing the tools to decode OSC tracebacks and
collect OSC metrics.

%package static
Summary: The OpenOSC static library package
Requires: openosc-devel = %{version}-%{release}

%description static
OpenOSC static package, containing the static library.

%prep
%autosetup -n OpenOSC-%{version}


%build
%configure
%make_build


%install
%make_install


%files
%{_libdir}/lib*.so.0*

%files devel
%{_libdir}/lib*.so
%{_includedir}/*.h

%files tools
%{_bindir}/oscdecode.py
%{_bindir}/oscmetrics.py

%files static
%{_libdir}/lib*.a


%changelog
%autochangelog
