Name:           zydis
Version:        5.0.0

%global forgeurl https://github.com/zyantific/zydis
%global commit 5091440c2a1f963e00c6e6aceec7c4346e656fa4
%forgemeta

Release:        %autorelease
Summary:        Fast and lightweight x86/x86-64 disassembler and code generation library

License:        MIT
URL:            %forgeurl
Source0:        %forgesource

ExcludeArch:    s390x

BuildRequires:  gcc
BuildRequires:  meson >= 1.3
BuildRequires:  pkgconfig(zycore)
BuildRequires:  doxygen
# build man pages
BuildRequires:  rubygem-ronn-ng
# tests
BuildRequires:  python3

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
%forgesetup

%build
%meson \
    -Dtools=enabled \
    -Dman=enabled \
    -Ddoc=enabled \
    -Dtests=enabled \

%meson_build

%install
%meson_install

%check
%ifnarch %{ix86}
%meson_test
%endif

%files
%license LICENSE
%{_libdir}/libZydis.so.5*

%files devel
%doc README.md
%{_includedir}/Zydis/
%{_libdir}/pkgconfig/zydis.pc
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
