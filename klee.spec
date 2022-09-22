%if 0%{?rhel} == 9
%bcond_with    stp
%bcond_without z3
%else
%bcond_without stp
%bcond_without z3
%endif

Name:           klee
Version:        2.3
Release:        6%{?dist}
Summary:        Symbolic Execution Engine

%define uclibc_version 1.3
%define uclibc_dir     %{name}-uclibc-%{name}_uclibc_v%{uclibc_version}

# Licenses
#
# * KLEE:
#   * Most files are under NCSA.
#   * cmake/GetGitRevisionDescription.cmake* are under Boost.
#   * cmake/modules/FindSQLite3.cmake is under MIT.
#   * lib/Support/RNG.cpp and runtime/klee-libc/stpcpy.c are under BSD.
#   * runtime/Freestanding/memcmp.c and runtime/klee-libc/{atoi.c,memchr.c,
#     strcat.c,strncmp.c,strncpy.c,strtol.c,strtoul.c} are under BSD with
#     advertising.
# * KLEE uClibc is under LGPLv2.

License:        NCSA and Boost and MIT and BSD and BSD with advertising and LGPLv2
URL:            https://%{name}.github.io

# KLEE
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

# KLEE uClibc
Source1:        https://github.com/%{name}/%{name}-uclibc/archive/refs/tags/%{name}_uclibc_v%{uclibc_version}.tar.gz
Source2:        https://www.uclibc.org/downloads/uClibc-locale-030818.tgz

# KLEE officially supports x86_64 only.
ExclusiveArch:  x86_64
# https://github.com/klee/klee/pull/1487
Patch0:         use-system-gtest.patch
# https://github.com/klee/klee/pull/1477
Patch1:         llvm14.patch
# https://github.com/klee/klee/pull/1547
Patch2:         z3-4.11.patch

BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gperftools-devel
BuildRequires:  libacl-devel
BuildRequires:  libcap-devel
BuildRequires:  libselinux-devel
BuildRequires:  llvm-devel
BuildRequires:  make
BuildRequires:  ninja-build
BuildRequires:  sqlite-devel
%if %{with stp}
BuildRequires:  stp-devel
%endif
%if %{with z3}
BuildRequires:  z3-devel
%endif
BuildRequires:  zlib-devel

# Needed for tests.
BuildRequires:  gtest-devel
BuildRequires:  python3-lit
BuildRequires:  python3-tabulate

%description
Symbolic virtual machine built on top of the LLVM compiler infrastructure.

%prep
# Prepare KLEE
%autosetup -p1

# Prepare KLEE uClibc
%setup -q -T -D -a 1
cd %{uclibc_dir}
cp %{SOURCE2} extra/locale/

%build
# Build KLEE uClibc
BUILD_DIR="$PWD"
cd %{uclibc_dir}

# We do not want to use Fedora's default compiler flags as this library is a
# build dependency for KLEE only!
./configure --with-cc clang --make-llvm-lib # custom, not autotools
%make_build

# KLEE
cd "$BUILD_DIR"
%cmake -GNinja                                   \
       -DENABLE_DOXYGEN:BOOL=OFF                 \
       -DENABLE_POSIX_RUNTIME:BOOL=ON            \
       -DENABLE_KLEE_UCLIBC:BOOL=ON              \
       -DKLEE_UCLIBC_PATH:PATH='%{uclibc_dir}'   \
       -DENABLE_SOLVER_METASMT:BOOL=OFF          \
%if %{with stp}
       -DENABLE_SOLVER_STP:BOOL=ON               \
%else
       -DENABLE_SOLVER_STP:BOOL=OFF              \
%endif
%if %{with z3}
       -DENABLE_SOLVER_Z3:BOOL=ON                \
%else
       -DENABLE_SOLVER_Z3:BOOL=OFF               \
%endif
       -DENABLE_UNIT_TESTS:BOOL=ON
%cmake_build

%install
%cmake_install

%check
%cmake_build --target check

%files
%doc NEWS README.md
%license LICENSE.TXT

%{_bindir}/gen-bout
%{_bindir}/gen-random-bout
%{_bindir}/kleaver
%{_bindir}/klee
%{_bindir}/klee-replay
%{_bindir}/klee-stats
%{_bindir}/klee-zesti
%{_bindir}/ktest-tool
%{_libdir}/klee/

# Following files are meant to be used by users of KLEE and not by developers.
#
# * <klee/klee.h> contains definitions of functions used by the executed
#   bitcode to interact with KLEE itself,
# * libkleeRuntest is a support library that can be linked to the source code
#   for which the tests were generated to replay a concrete test case.
#
# For more information see https://klee.github.io/tutorials/testing-function.

%dir %{_includedir}/klee
%{_includedir}/klee/klee.h
%{_libdir}/libkleeRuntest.so
%{_libdir}/libkleeRuntest.so.1.0

%changelog
* Fri Aug 19 2022 Jerry James <loganjerry@gmail.com> - 2.3-6
- Rebuild for z3 4.11
- Add z3-4.11.patch due to Z3_TRUE removal

* Wed Aug 10 2022 Lukáš Zaoral <lzaoral@redhat.com> - 2.3-5
- Rebuild for z3 4.10 (rhbz#2117070)

* Mon Jul 25 2022 Lukáš Zaoral <lzaoral@redhat.com> - 2.3-4
- Enable Z3 solver backend
- Enable libacl and libcap integration in POSIX runtime

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Apr 05 2022 Lukáš Zaoral <lzaoral@redhat.com> - 2.3-2
- Update KLEE uClibc to v1.3

* Mon Apr 04 2022 Lukáš Zaoral <lzaoral@redhat.com> - 2.3-1
- Update to 2.3

* Tue Jan 25 2022 Lukáš Zaoral <lzaoral@redhat.com> - 2.2-5
- uClibc must be built with clang (#2045767)
  - Caused by CC=gcc set by implicit %%set_build_flags in %%build

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Oct 15 2021 Lukáš Zaoral <lzaoral@redhat.com> - 2.2-3
- Rebuild for llvm-13.0.0 (#2014582)

* Wed Oct 13 2021 Lukáš Zaoral <lzaoral@redhat.com> - 2.2-2
- Fix compilation with LLVM 13
- Enable uClibc and POSIX runtime support as requested by upstream.
- Due to uClibc, package is now buildable only on x86_64.
- Enable SELinux support

* Thu Jul 15 2021 Lukáš Zaoral <lzaoral@redhat.com> - 2.2-1
- First release
