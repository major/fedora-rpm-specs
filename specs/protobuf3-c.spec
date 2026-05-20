%global sover 1
%global origname protobuf-c

Name:           protobuf3-c
Version:        1.5.2
# anything below 50 is reserved for "old" protobuf-c
Release:        %autorelease -b 50
Summary:        C bindings for Google's Protocol Buffers

License:        BSD-2-Clause
URL:            https://github.com/protobuf-c/protobuf-c
Source0:        %{url}/releases/download/v%{version}/%{origname}-%{version}.tar.gz

Provides:       protobuf-c = %{version}-%{release}
Obsoletes:      protobuf-c < %{version}-%{release} 

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  protobuf-devel < 4
BuildRequires:  pkgconfig(protobuf)

%description
Protocol Buffers are a way of encoding structured data in an efficient yet
extensible format. This package provides a code generator and run-time
libraries to use Protocol Buffers from pure C (not C++).

It uses a modified version of protoc called protoc-c.

This is bindings for compat package protobuf3

%package compiler
Summary:        Protocol Buffers C compiler
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description compiler
This package contains a modified version of the Protocol Buffers
compiler for the C programming language called protoc-c.

%package devel
Summary:        Protocol Buffers C headers and libraries
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-compiler%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
This package contains protobuf-c headers and libraries.

This is bindings for compat package protobuf3

%prep
%autosetup -p1 -n'%{origname}-%{version}'

%build
%configure --disable-static
%make_build

%check
make check

%install
%make_install
find %{buildroot} -type f -name '*.la' -delete

%files
%license LICENSE
%doc README.md TODO
%{_libdir}/lib%{origname}.so.%{sover}*

%files compiler
%{_bindir}/protoc-c
%{_bindir}/protoc-gen-c

%files devel
%dir %{_includedir}/google
%{_includedir}/%{origname}/
%{_includedir}/google/%{origname}/
%{_libdir}/lib%{origname}.so
%{_libdir}/pkgconfig/lib%{origname}.pc

%changelog
%autochangelog
