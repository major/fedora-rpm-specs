%global forgeurl https://github.com/ibireme/yyjson
%global date 20231205
%global commit e0bacd5bffb7142a1a29ac6becbca4b87e45b429
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%forgemeta

Name:           yyjson
Version:        0.8.0
Release:        %autorelease
Summary:        A high performance JSON library written in ANSI C
License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

%description
A high performance JSON library written in ANSI C.

Features
- Fast: can read or write gigabytes per second JSON data on modern CPUs.
- Portable: complies with ANSI C (C89) for cross-platform compatibility.
- Strict: complies with RFC 8259 JSON standard, ensuring strict number format
and UTF-8 validation.
- Extendable: offers options to allow comments, trailing commas, NaN/Inf, and
custom memory allocator.
- Accuracy: can accurately read and write int64, uint64, and double numbers.
- Flexible: supports unlimited JSON nesting levels, \u0000 characters, and non
null-terminated strings.
- Manipulation: supports querying and modifying using JSON Pointer, JSON Patch
and JSON Merge Patch.
- Developer-Friendly: easy integration with only one h and one c file.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains development files for %{name}.

%prep
%forgeautosetup -p1

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
    -DYYJSON_BUILD_TESTS=ON \

%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_libdir}/libyyjson.so.0*

%files devel
%{_includedir}/yyjson.h
%{_libdir}/libyyjson.so
%{_libdir}/cmake/yyjson/
%{_libdir}/pkgconfig/yyjson.pc

%changelog
%autochangelog
