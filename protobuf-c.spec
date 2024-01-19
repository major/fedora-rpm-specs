%global sover 1

Name:           protobuf-c
Version:        1.5.0
Release:        %autorelease
Summary:        C bindings for Google's Protocol Buffers

License:        BSD-2-Clause
URL:            https://github.com/protobuf-c/protobuf-c
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(protobuf)

%description
Protocol Buffers are a way of encoding structured data in an efficient yet
extensible format. This package provides a code generator and run-time
libraries to use Protocol Buffers from pure C (not C++).

It uses a modified version of protoc called protoc-c.

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

%prep
%autosetup -p1

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
%{_libdir}/lib%{name}.so.%{sover}*

%files compiler
%{_bindir}/protoc-c
%{_bindir}/protoc-gen-c

%files devel
%dir %{_includedir}/google
%{_includedir}/%{name}/
%{_includedir}/google/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc

%changelog
%autochangelog
