Name:           primecount
Version:        8.2
Release:        1%{?dist}
Summary:        Fast prime counting function implementation

# BSD-2-Clause: the project as a whole
# Zlib OR BSL-1.0: due to including libdivide headers
License:        BSD-2-Clause AND (Zlib OR BSL-1.0)
URL:            https://github.com/kimwalisch/%{name}/
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  asciidoc
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libdivide-static
%ifarch %{ix86} x86_64 ia64 ppc64le
BuildRequires:  libquadmath-devel
%endif
BuildRequires:  make
BuildRequires:  primesieve-devel

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
Primecount is a command-line program and C++ library that counts the
primes below an integer x<=10**31 using highly optimized implementations
of the combinatorial prime counting algorithms.

Primecount includes implementations of all important combinatorial prime
counting algorithms known up to this date all of which have been
parallelized using OpenMP.  Primecount contains the first ever open
source implementations of the Deleglise-Rivat algorithm and Xavier
Gourdon's algorithm (that works).  Primecount also features a novel load
balancer that is shared amongst all implementations and that scales up
to hundreds of CPU cores.  Primecount has already been used to compute
several world records e.g. pi(10**27)
(http://www.mersenneforum.org/showthread.php?t=20473) and
nth_prime(10**24) (https://oeis.org/A006988).

%package        libs
Summary:        C++ library for fast prime counting
%ldconfig_scriptlets

%description    libs
This package contains a C++ library for counting primes below an
integer.  See the primecount package for a command line interface.

%package        devel
Summary:        Headers and library links for libprimecount
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
This package contains files necessary to develop applications that use
libprimecount.

%prep
%autosetup -p1

# Unbundle libdivide
rm -f include/libdivide.h
ln -s %{_includedir}/libdivide.h include/libdivide.h

%build
# WITH_FLOAT128 should be ON only for architectures:
# - with a __float128 type that is different from long double
# - with libquadmath
# As of GCC 12:
# - All x86/x86_64 CPUs have __float128; it is different from long double
# - ppc64le has __float128; it is the same as long double
# - No other architecture has libquadmath
%ifarch %{ix86} x86_64
export CFLAGS='%{build_cflags} -DLIBDIVIDE_SSE2'
export CXXFLAGS='%{build_cxxflags} -DLIBDIVIDE_SSE2'
%endif
%cmake -DBUILD_LIBPRIMESIEVE=OFF \
       -DBUILD_MANPAGE=ON \
       -DBUILD_SHARED_LIBS=ON \
       -DBUILD_STATIC_LIBS=OFF \
%ifarch %{ix86} x86_64
       -DWITH_FLOAT128=ON \
%endif
       -DBUILD_TESTS=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc README.md
%{_bindir}/primecount
%{_mandir}/man1/primecount.1*

%files          libs
%license COPYING
%{_libdir}/libprimecount.so.8*

%files          devel
%doc ChangeLog doc/*.pdf doc/*.md
%{_includedir}/primecount.h
%{_includedir}/primecount.hpp
%{_libdir}/libprimecount.so
%dir %{_libdir}/cmake/primecount
%{_libdir}/cmake/primecount/*.cmake
%{_libdir}/pkgconfig/primecount.pc

%changelog
* Fri Feb 06 2026 Kim Walisch <walki@fedoraproject.org> - 8.2-1
- Fix missing version in .pc file

* Mon Jan 26 2026 Kim Walisch <walki@fedoraproject.org> - 8.1-9
- S2_easy.cpp: Fix "#pragma omp master" deprecated in OpenMP 5.1
- Fix incorrect release number in previous changelog entry

* Mon Jan 26 2026 Kim Walisch <walki@fedoraproject.org> - 8.1-0
- CMakeLists.txt: Fix CMAKE_PROJECT_VERSION not defined
- AC.cpp: Up to 15% faster due to improved instruction level parallelism
- Sieve_count*.hpp: Improve GCC conditional move code gen
- Automated building Windows binaries using GitHub Actions CI

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Wed Dec 17 2025 Kim Walisch <walki@fedoraproject.org> - 8.0-7
- Yet another rebuild due to automated test network timeout

* Wed Dec 17 2025 Kim Walisch <walki@fedoraproject.org> - 8.0-6
- Rebuild due to Fedora Automated tests timeout

* Tue Dec 16 2025 Kim Walisch <walki@fedoraproject.org> - 8.0-5
- Use ANSI escape sequence to clear terminal text line

* Mon Dec 15 2025 Kim Walisch <walki@fedoraproject.org> - 8.0-4
- Fix status output in --AC option

* Mon Dec 15 2025 Kim Walisch <walki@fedoraproject.org> - 8.0-3
- Rebuild due to bodhi automated test failure (Fedora network down)

* Sun Dec 14 2025 Kim Walisch <walki@fedoraproject.org> - 8.0-2
- Fix flickering when using --status option

* Sun Dec 14 2025 Kim Walisch <walki@fedoraproject.org> - 8.0-1
- api.cpp: Fix broken 128-bit nth prime function
- util.cpp: Fix undefined behavior in to_string()
- calculator.hpp: Add code to detect integer overflows
- LoadBalancerP2.cpp: Faster critical section
- LoadBalancerS2.cpp: Faster critical section
- LoadBalancerAC.cpp: Faster critical section
- nth_prime.cpp: Improve status output
- AC.cpp: Improved instruction level parallelism
- AC_libdivide.cpp: Improved instruction level parallelism
- D.cpp: Refactor runtime dispatch to optimized SIMD algorithm
- S2_hard.cpp: Refactor runtime dispatch to optimized SIMD algorithm
- pi_lmo_parallel.cpp: Add support for runtime dispatch to optimized SIMD algorithm
- Move S2_easy_libdivide.cpp code into S2_easy.cpp
- Move AC_libdivide.cpp code into AC.cpp
- src/app/test.cpp: Speed up tests
- CMakeLists.txt: Set CMAKE_VISIBILITY_INLINES_HIDDEN = ON by default

* Tue Nov 04 2025 Kim Walisch <walki@fedoraproject.org> - 7.20-1
- pi_gourdon.cpp: Quickly verify pi(x) results
- pi_deleglise_rivat.cpp: Quickly verify pi(x) results
- pi_lmo_parallel.cpp: Quickly verify pi(x) results
- CmdOptions.cpp: Add --double-check option
- build_mingw64_arm64.sh: Enable ARM SVE for Mingw-w64 on ARM64
- doc/Easy-Special-Leaves.pdf: Converted Markdown to LaTeX
- doc/Hard-Special-Leaves.pdf: Converted Markdown to LaTeX
- doc/Partial-Sieve-Function.pdf: Converted Markdown to LaTeX
- ci.yml: Add WebAssembly/Emscripten test
- BUILD.md: Add WebAssembly/Emscripten build instructions
- README.md: Updated Algorithms section

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Jun 04 2025 Kim Walisch <walki@fedoraproject.org> - 7.19-2
- nth_prime_sieve.hpp: Add missing include guards
- Update ChangeLog

* Wed Jun 04 2025 Kim Walisch <walki@fedoraproject.org> - 7.19-1
- nth_prime.cpp: Add 128-bit nth_prime function
- nth_prime_sieve.hpp: New sieving algo for nth_prime(n)
- primecount.h: Improved 128-bit C API using portable pc_int128_t struct
- primecount.hpp: Improved 128-bit C++ API using portable pc_int128_t struct
- libprimecount.md: Add new 128-bit C/CPI API functions

* Sat May 17 2025 Kim Walisch <walki@fedoraproject.org> - 7.18-1
- Add CMake find_package(primecount) support
- libprimecount.md: Add CMake find_package(primecount) section
- PhiTiny.cpp: Reduce code bloat
- Move private header files from /include to /src
- src/CMakeLists.txt: Update for private header files in /src
- test/CMakeLists.txt: Update for private header files in /src
- Vector.hpp: Get rid of std::is_trivial which is deprecated in C++26
- Update to latest primesieve-12.9 library
- Update to latest libdivide-5.2.0 library

* Tue Apr 29 2025 Kim Walisch <walki@fedoraproject.org> - 7.17-2
- Sieve_pre_sieve.hpp: Improved pre-sieving using primes ≤ 71

* Mon Apr 28 2025 Kim Walisch <walki@fedoraproject.org> - 7.17-1
- Sieve_pre_sieve.hpp: Improved pre-sieving using primes ≤ 37
- Pre-sieving speeds up S2_hard and D algorithms by up to 5%
- README.md: Fix Markdown math formulas
- Hard-Special-Leaves.md: Fix Markdown math formulas
- Update to primesieve-12.8 library

* Tue Apr 01 2025 Kim Walisch <walki@fedoraproject.org> - 7.16-1
- fast_div.hpp: Fix "Warning: mnemonic suffix used with `div'"
- libdivide.h: Fix "Warning: mnemonic suffix used with `div'"
- LoadBalancerS2.cpp: Tune load balancing
- LoadBalancerAC.cpp: Tune load balancing
- primecount-internal.hpp: Update default CPU cache sizes
- Sieve.cpp: Improve count balancing
- Sieve.cpp: Add multiarch count methods
- Sieve.hpp: New multiarch count methods
- D.cpp: Runtime dispatching changes
- D_multiarch_avx512.cpp: New file
- D_multiarch_arm_sve.cpp: New file
- S2_hard.cpp: Runtime dispatching changes
- S2_hard_multiarch_avx512.cpp: New file
- S2_hard_multiarch_arm_sve.cpp: New file

* Mon Mar 03 2025 Kim Walisch <walki@fedoraproject.org> - 7.15-2
- multiarch_arm_sve.cmake: Update to latest ARM SVE code

* Mon Mar 03 2025 Kim Walisch <walki@fedoraproject.org> - 7.15-1
- Sieve.hpp: Improve ARM SVE bit counting algorithm
- multiarch_arm_sve.cmake: Improve ARM SVE detection
- src/arch/arm/sve.cpp: Detect ARM SVE instruction set
- Update to libprimesieve-12.7

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 31 2024 Kim Walisch <walki@fedoraproject.org> - 7.14-1
- Fix libdivide.h issue with GCC 15.
- Improve AVX512 code.
- Improve ARM SVE code.

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Apr 17 2024 Kim Walisch <walki@fedoraproject.org> - 7.13-1
- CMakeLists.txt: New WITH_MULTIARCH option (default ON).
- Sieve.hpp: New AVX512 popcount algorithm for x86 CPUs.
- Sieve.hpp: New ARM SVE popcount algorithm.
- int128.cmake: Improve int128_t support for Windows.
- OpenMP.cmake: Improve LLVM/Clang OpenMP detection.
- Add preliminary MSVC 128-bit support.

* Tue Apr 02 2024 Kim Walisch <walki@fedoraproject.org> - 7.12-1
- On x86 CPUs check using CPUID if CPU supports POPCNT
- CMakeLists.txt: Remove WITH_POPCNT=OFF option
- New dynamic/adaptive load balancing for AC algorithm
- LogarithmicIntegral.cpp: Fix infinite loop on Linux i386
- RiemannR.cpp: Fix infinite loop on Linux i386
- RiemannR.cpp: Faster and simpler RiemannR_inverse(x)

* Tue Mar 12 2024 Kim Walisch <walki@fedoraproject.org> - 7.11-1
- CMakeLists.txt: Detect Apple Silicon CPUs
- Fix musl libc issue in test/iroot.cpp
- Speed up test/Li.cpp
- Faster RiemannR(x) and RiemannR_inverse(x) implementations
- Renamed option --Ri to -R or --RiemannR
- Renamed option --Ri-inverse to --RiemannR-inverse
- Detect incompatible command-line options
- Increase pi(x) cache size to 2 KiB

* Mon Feb 19 2024 Kim Walisch <walki@fedoraproject.org> - 7.10-5
- Rebuild required because of primesieve-12.0 release

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Kim Walisch <walki@fedoraproject.org> - 7.10-2
- Fix source archive name, must be primecount-X.Y.tar.gz

* Thu Jan 11 2024 Kim Walisch <walki@fedoraproject.org> - 7.10-1
- Improve CMake libatomic detection
- Fix potential integer overflows in Li_inverse(x) and Ri_inverse(x)
- Added new internal nth_prime_approx(n)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 04 2023 Kim Walisch <walki@fedoraproject.org> - 7.9-2
- Fix Appveyor CI tests

* Mon Jul 03 2023 Kim Walisch <walki@fedoraproject.org> - 7.9-1
- Add more unit tests

* Tue Mar 28 2023 Kim Walisch <walki@fedoraproject.org> - 7.8-2
- Updated test/pi_gourdon.cpp and test/pi_deleglise_rivat.cpp

* Tue Mar 28 2023 Kim Walisch <walki@fedoraproject.org> - 7.8-1
- Fix integer overflow in pi(x) for x <= -2^63

* Sun Mar 26 2023 Kim Walisch <walki@fedoraproject.org> - 7.7-2
- Fix -Wstrict-prototypes warning in test/api_c.c

* Sun Mar 26 2023 Kim Walisch <walki@fedoraproject.org> - 7.7-1
- Version 7.7
- Fix primecount_pi(-1) crash
- Fix GCC/Clang -Wstrict-prototypes warnings

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 12 2022 Jerry James <loganjerry@gmail.com> - 7.6-3
- Convert License tag to SPDX

* Wed Dec 07 2022 Kim Walisch <walki@fedoraproject.org> - 7.6-3
- Use primecount-7.6.tar.gz archive released on GitHub

* Wed Dec 07 2022 Kim Walisch <walki@fedoraproject.org> - 7.6-2
- Use latest primecount archive from GitHub

* Wed Dec 07 2022 Kim Walisch <walki@fedoraproject.org> - 7.6-1
- Version 7.6
- Add missing <string_view> header in print.hpp

* Wed Dec 07 2022 Kim Walisch <walki@fedoraproject.org> - 7.5-1
- Version 7.5
- Requires libprimesieve-11

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul  8 2022 Jerry James <loganjerry@gmail.com> - 7.4-1
- Version 7.4

* Tue May  3 2022 Jerry James <loganjerry@gmail.com> - 7.3-1
- Version 7.3

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 11 2021 Jerry James <loganjerry@gmail.com> - 7.2-1
- Version 7.2

* Thu Aug 19 2021 Jerry James <loganjerry@gmail.com> - 7.1-1
- Version 7.1
- Enable LTO on ppc64le

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Jerry James <loganjerry@gmail.com> - 7.0-1
- Version 7.0

* Sat Mar 20 2021 Jerry James <loganjerry@gmail.com> - 6.4-1
- Version 6.4

* Fri Mar  5 2021 Jerry James <loganjerry@gmail.com> - 6.3-1
- Version 6.3

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  8 2021 Jerry James <loganjerry@gmail.com> - 6.2-1
- Version 6.2

* Wed Sep 30 2020 Jerry James <loganjerry@gmail.com> - 6.1-1
- Version 6.1

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 22 2020 Jerry James <loganjerry@gmail.com> - 6.0-1
- Version 6.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Jerry James <loganjerry@gmail.com> - 5.3-1
- Version 5.3

* Mon Nov 18 2019 Jerry James <loganjerry@gmail.com> - 5.2-1
- Version 5.2
- Drop all patches
- Building man page now needs asciidoc instead of help2man

* Fri Sep 20 2019 Jerry James <loganjerry@gmail.com> - 5.1-2
- Add justifications in the patch files
- Generate a man page with help2man

* Thu Sep 19 2019 Jerry James <loganjerry@gmail.com> - 5.1-1
- Initial RPM
