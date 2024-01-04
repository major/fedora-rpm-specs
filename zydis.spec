Name:           zydis
Version:        4.0.0
Release:        %autorelease
Summary:        Fast and lightweight x86/x86-64 disassembler and code generation library

License:        MIT
URL:            https://github.com/zyantific/zydis
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# fix the installation location of man pages
Patch0:         https://github.com/zyantific/zydis/commit/c683b1273104b19300a830889e7d827e727c43e9.patch
# Add ZYDIS_BUILD_TESTS option and include tests in CMakeLists.txt
Patch1:         https://github.com/zyantific/zydis/commit/a56a39f15efe64a41013ec142c028e6f72476232.patch

ExcludeArch:    s390x

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  zycore-c-devel
BuildRequires:  doxygen
# build man pages
BuildRequires:  rubygem-ronn-ng

%description
Zydis is fast and lightweight x86/x86-64 disassembler and code generation
library.

- Supports all x86 and x86-64 (AMD64) instructions and extensions
- Optimized for high performance
- No dynamic memory allocation ("malloc")
- Thread-safe by design
- Very small file-size overhead compared to other common disassembler libraries
- Complete doxygen documentation
- Absolutely no third party dependencies — not even libc
  - Should compile on any platform with a working C11 compiler
  - Tested on Windows, macOS, FreeBSD, Linux and UEFI, both user and kernel mode

%package        devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains documentation for %{name}.

%package        tools
Summary:        Tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tools
The %{name}-tools package contains tools about %{name}.

%prep
%autosetup -p1

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DZYAN_SYSTEM_ZYCORE=ON \
    -DZYDIS_BUILD_SHARED_LIB=ON \
    -DZYDIS_BUILD_MAN=ON \
    -DZYDIS_BUILD_TESTS=ON \

%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%{_libdir}/libZydis.so.4.0*

%files devel
%doc README.md
%{_includedir}/Zydis/
%dir %{_libdir}/cmake/zydis
%{_libdir}/cmake/zydis/*.cmake
%{_libdir}/libZydis.so

%files doc
%{_docdir}/Zydis/

%files tools
%{_bindir}/ZydisDisasm
%{_bindir}/ZydisInfo
%{_mandir}/man1/ZydisDisasm.1*
%{_mandir}/man1/ZydisInfo.1*

%changelog
%autochangelog
