Name:           libunicode
Version:        0.6.0
Release:        %autorelease
Summary:        Modern C++20 Unicode Library
License:        Apache-2.0
URL:            https://github.com/contour-terminal/libunicode
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

ExclusiveArch:  x86_64 aarch64

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  cmake(fmt)
BuildRequires:  cmake(range-v3)
BuildRequires:  unicode-ucd
BuildRequires:  pkgconfig(catch2)

%description
The goal of libunicode library is to bring painless unicode support to C++
with simple and easy to understand APIs. The API naming conventions are chosen
to look familiar to those using the C++ standard libary.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains development files for %{name}.

%package        tools
Summary:        Tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tools
The %{name}-tools package contains tools about %{name}.

%prep
%autosetup -p1

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
    -DLIBUNICODE_UCD_DIR=%{_datadir}/unicode/ucd \

%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_libdir}/libunicode*.so.0.6*

%files devel
%{_includedir}/libunicode/
%{_libdir}/cmake/libunicode/
%{_libdir}/libunicode*.so

%files tools
%{_bindir}/unicode-query

%changelog
%autochangelog
