%global with_snapshot 1
%global gitdate 20231007
%global commit 6e71f6be0c1ccd6d1dab052ae4e6610e3b031aa7
%global shortcommit %(c=%{commit}; echo ${c:0:8})

%global desc %{expand: \
AsmJit is a lightweight library suitable for low-latency machine code 
generation written in C++. It can generate machine code for X86, X86_64, and
AArch64 architectures. It has a type-safe API that allows C++ compiler to do
semantic checks at compile-time even before the assembled code is generated
or executed.}

Name:		asmjit
Version:	0.0%{?with_snapshot:^%{gitdate}git%{shortcommit}}
Release:	%autorelease
Summary:	A lightweight library suitable for low-latency machine code generation

License:	Zlib
URL:		https://asmjit.com
%if %{with_snapshot}
Source0:	https://github.com/asmjit/asmjit/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%else
Source0:	https://github.com/asmjit/asmjit/archive/v%{version}/%{name}-%{version}.tar.gz
%endif

Patch0:		asmjit-fedora.patch

ExclusiveArch:	aarch64 x86_64

BuildRequires:	cmake >= 3.5
BuildRequires:	gcc-c++
BuildRequires:	ninja-build

%description
%{desc}

%package devel
Summary:	Headers and libraries for %{name}
Provides:	%{name}%{?_isa} = %{version}-%{release}

%description devel
%{desc}

%prep
%if %{with_snapshot}
%autosetup -p1 -n %{name}-%{commit}
%else
%autosetup -p1
%endif

%build
%cmake -G Ninja \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_EXPORT_COMPILE_COMMANDS=ON \
	-DASMJIT_STATIC=0 \
	-DASMJIT_TEST=1
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE.md
%doc README.md
%{_libdir}/lib%{name}.so.0*

%files devel
%doc README.md
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/%{name}/

%changelog
%autochangelog
