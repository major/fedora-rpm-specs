Name:           bloaty
Version:        1.1
Release:        %autorelease
Summary:        A size profiler for binaries

# The entire source is Apache-2.0, except:
#
# BSD-2-Clause:
#   third_party/freebsd_elf/
# APSL-2.0:
#   third_party/darwin_xnu_macho/ except as below:
# APSL-2.0 AND BSD-4-Clause-UC:
#   third_party/darwin_xnu_macho/mach-o/nlist.h
# APSL-2.0 AND BSD-3-Clause
#   third_party/darwin_xnu_macho/mach-o/reloc.h
#
# Note that the contents of third_party/freebsd_elf/ and
# third_party/darwin_xnu_macho/ *are* used in the Linux build (to support
# examining binaries built for other platforms).
License:        Apache-2.0 AND BSD-2-Clause AND BSD-4-Clause-UC AND BSD-3-Clause
URL:            https://github.com/google/bloaty
Source0:        https://github.com/google/bloaty/archive/v%{version}/%{name}-%{version}.tar.gz
# Patch to use system versions of abseil, google-test and google-mock
Patch0:         bloaty-1.1-absl.patch
# Patch to fix size detection function to use 64 bit types on 32bit architectures
Patch1:         bloaty-1.1-longlong.patch
# Add missing #include needed on GCC13
# https://github.com/google/bloaty/pull/332
Patch2:         %{url}/pull/332.patch
# Add missing `#include <stdexcept>` in `src/range_map.h`
#
# This was satisfied indirectly/implicitly via abseil-cpp prior to version
# 20260107; the missing include was fixed upstream in refactoring commit
# 5b8d313c8783e669db096e8101a757e98d975f9456c7d968dc42d98a4591036c.
Patch3:         0001-Add-missing-include-stdexcept-in-src-range_map.h.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  abseil-cpp-devel
BuildRequires:  capstone-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
BuildRequires:  pkgconfig
BuildRequires:  protobuf-devel
BuildRequires:  re2-devel

BuildRequires:  help2man

%description
Ever wondered what's making your binary big? Bloaty McBloatface will show
you a size profile of the binary so you can understand what's taking up
space inside.

Bloaty works on binaries, shared objects, object files, and static
libraries. Bloaty supports the ELF and Mach-O formats, and has experimental
support for WebAssembly.

%prep
%autosetup -S gendiff -N
%autopatch -p0 -M 1
%autopatch -p1 -m 2


%build
%cmake \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DBLOATY_ENABLE_CMAKETARGETS=OFF \
  -DBUILD_TESTING=ON
%cmake_build
help2man --no-info --output=bloaty.1 %{_vpath_builddir}/bloaty


%install
%cmake_install
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 bloaty.1

%check
%ctest --verbose || exit 0

%files
%license LICENSE
%doc README.md how-bloaty-works.md
%{_bindir}/bloaty
%{_mandir}/man1/bloaty.1*


%changelog
%autochangelog

