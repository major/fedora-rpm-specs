Name:           primecount
Version:        7.14
Release:        2%{?dist}
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
%{_libdir}/libprimecount.so.7*

%files          devel
%doc ChangeLog doc/*.pdf doc/*.md
%{_includedir}/primecount.h
%{_includedir}/primecount.hpp
%{_libdir}/libprimecount.so
%{_libdir}/pkgconfig/primecount.pc

%changelog
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
