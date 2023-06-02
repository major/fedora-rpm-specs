%global sover 0.2

Name:           libunicode
Version:        0.3.0
Release:        %autorelease
Summary:        Modern C++17 Unicode library
License:        Apache-2.0
URL:            https://github.com/contour-terminal/libunicode
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# fix to enable the customized defined ucd path
Patch0:         fix-ucd.patch

ExclusiveArch:  x86_64 aarch64

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  fmt-devel
BuildRequires:  range-v3-devel
BuildRequires:  unicode-ucd

%if %{?fedora} <= 38
BuildRequires:  catch-devel
%else
BuildRequires:  catch2-devel
%endif

%description
The goal of libunicode library is to bring painless unicode support to C++
with simple and easy to understand APIs. The API naming conventions are chosen
to look familiar to those using the C++ standard libary.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        tools
Summary:        Tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tools
The %{name}-tools package contains tools about %{name}.

%prep
%autosetup

%build
%cmake -DLIBUNICODE_UCD_DIR=%{_datadir}/unicode/ucd
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md Changelog.md
%{_libdir}/%{name}*.so.%{sover}*

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%dir %{_libdir}/cmake/%{name}
%{_libdir}/cmake/%{name}/*.cmake
%{_libdir}/%{name}*.so

%files tools
%{_bindir}/unicode-query

%changelog
%autochangelog
