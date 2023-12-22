# Lists copied from gcc.spec
# Current as of 13.2.1 (lines 66, 86, and 76, respectively).
# Note that asan and ubsan are available on all Fedora primary architectures;
# tsan is missing on i686 only.
%ifarch %{ix86} x86_64 ppc ppc64 ppc64le ppc64p7 s390 s390x %{arm} aarch64
%global arch_has_asan 1
%endif
%ifarch %{ix86} x86_64 ppc ppc64 ppc64le ppc64p7 s390 s390x %{arm} aarch64
%global arch_has_ubsan 1
%endif
%ifarch x86_64 ppc64 ppc64le aarch64 s390x
%global arch_has_tsan 1
%endif

# By default, enable sanitizers whenever they are available on the architecture.
%bcond asan 0%{?arch_has_asan:1}
%bcond ubsan 0%{?arch_has_ubsan:1}
%bcond tsan 0%{?arch_has_tsan:1}

Name:           wlcs
Version:        1.7.0
Release:        %autorelease
Summary:        Wayland Conformance Test Suite

# The entire source is GPL-3.0-only, except:
#
# (GPL-2.0-only OR GPL-3.0-only):
#   - CMakeLists.txt
# > Build system file that does not contribute to the licenses of the binary
#   RPMs
#
# (LGPL-2.0-only OR LGPL-3.0-only):
#   - include/geometry/*
#   - include/mutex.h
#   - include/shared_library.h
#   - src/helpers.cpp
#   - src/shared_library.cpp
# > Since (L)GPLv2-only code is not compatible with (L)GPLv3 or (L)GPLv3+ code,
#   and these sources are combined with GPLv3 code, the LGPLv3 option is used
#   in this package. However, we encode both options in the SPDX expression.
#
# GPLv2+:
#   - debian/*
# > Not used in this package
#
# MIT:
#   - src/protocol/gtk-primary-selection.xml
#   - src/protocol/input-method-unstable-v1.xml
#   - src/protocol/pointer-constraints-unstable-v1.xml
#   - src/protocol/primary-selection-unstable-v1.xml
#   - src/protocol/relative-pointer-unstable-v1.xml
#   - src/protocol/wayland.xml
#   - src/protocol/wlr-virtual-pointer-unstable-v1.xml
#   - src/protocol/xdg-output-unstable-v1.xml
#   - src/protocol/xdg-shell-unstable-v6.xml
#   - src/protocol/xdg-shell.xml
#   - tests/test_bad_buffer.cpp
#   - tests/test_surface_events.cpp
#   - tests/text_input_v3_with_input_method_v2.cpp
#   - tests/wlr_virtual_pointer_v1.cpp
#   - tests/xdg_popup_v6.cpp
#   - tests/xdg_surface_stable.cpp
#   - tests/xdg_surface_v6.cpp
#   - tests/xdg_toplevel_stable.cpp
#   - tests/xdg_toplevel_v6.cpp
# > Files in tests/ are all test code that is not installed (so does not
#   contribute to the licenses of the binary RPMs). Files in src/protocol/ are
#   used as inputs to “wayland-scanner” to generate C source files and headers,
#   and are not directly included in the binary RPMs.
#
# HPND-sell-variant:
#   - src/protocol/text-input-unstable-v2.xml
# > Files in src/protocol/ are used as inputs to “wayland-scanner” to generate
#   C source files and headers, and are not directly included in the binary
#   RPMs.
License:        GPL-3.0-only AND (LGPL-2.0-only OR LGPL-3.0-only)
URL:            https://github.com/MirServer/wlcs
Source:         %{url}/archive/v%{version}/wlcs-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++

BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  boost-devel
BuildRequires:  cmake(GTest)
BuildRequires:  gmock-devel
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-scanner)

%if %{with asan}
BuildRequires:  libasan
%endif
%if %{with ubsan}
BuildRequires:  libubsan
%endif
%if %{with tsan}
BuildRequires:  libtsan
%endif

%description
wlcs aspires to be a protocol-conformance-verifying test suite usable by
Wayland compositor implementors.

It is growing out of porting the existing Weston test suite to be run in Mir’s
test suite, but it is designed to be usable by any compositor.

wlcs relies on compositors providing an integration module, providing wlcs with
API hooks to start a compositor, connect a client, move a window, and so on.

This makes both writing and debugging tests easier - the tests are (generally)
in the same address space as the compositor, so there is a consistent global
clock available, it’s easier to poke around in compositor internals, and
standard debugging tools can follow control flow from the test client to the
compositor and back again.


%package        devel
Summary:        Development files for wlcs
Requires:       wlcs%{?_isa} = %{version}-%{release}

%description    devel
wlcs aspires to be a protocol-conformance-verifying test suite usable by
Wayland compositor implementors.

The wlcs-devel package contains libraries and header files for developing
Wayland compositor tests that use wlcs.


%prep
%autosetup
# -Werror makes sense for upstream CI, but is too strict for packaging
sed -r -i 's/-Werror //' CMakeLists.txt


%build
%cmake \
    -DWLCS_BUILD_ASAN=%{?with_asan:ON}%{?!with_asan:OFF} \
    -DWLCS_BUILD_TSAN=%{?with_tsan:ON}%{?!with_tsan:OFF} \
    -DWLCS_BUILD_UBSAN=%{?with_ubsan:ON}%{?!with_ubsan:OFF} \
    -GNinja
%cmake_build


%install
%cmake_install


%check
%ctest


%files
%license COPYING.*
%doc README.rst

%{_libexecdir}/wlcs/


%files devel
%doc README.rst
%doc example/

%{_includedir}/wlcs/
%{_libdir}/pkgconfig/wlcs.pc


%changelog
%autochangelog
