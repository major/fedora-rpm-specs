Name:     primesieve
Version:  12.6
Release:  3%{?dist}
Summary:  Fast prime number generator
License:  LicenseRef-Callaway-BSD
URL:      https://github.com/kimwalisch/primesieve
Source0:  https://github.com/kimwalisch/primesieve/archive/v%{version}.tar.gz
Requires: primesieve-libs%{?_isa} = %{version}-%{release}

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  cmake >= 3.7
BuildRequires:  asciidoc

%description
primesieve is a program that generates primes using a highly optimized
sieve of Eratosthenes implementation. primesieve can generate primes
and prime k-tuplets up to 2^64.

%package -n primesieve-libs
Summary: C/C++ library for generating prime numbers

%description -n primesieve-libs
This package contains the shared runtime library for primesieve.

%package -n primesieve-devel
Summary: Development files for the primesieve library
Requires: primesieve-libs%{?_isa} = %{version}-%{release}

%description -n primesieve-devel
This package contains the C/C++ header files and the configuration
files for developing applications that use the primesieve library.
It also contains the API documentation of the library.

%prep
%setup -q -n %{name}-%{version}

%build
%cmake -DBUILD_STATIC_LIBS=OFF -DBUILD_TESTS=ON -DBUILD_MANPAGE=ON
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n primesieve-libs

%check
%ctest

%files -n primesieve
%doc README.md ChangeLog
%{_bindir}/primesieve
%{_mandir}/man1/primesieve.1*

%files -n primesieve-libs
%license COPYING
%{_libdir}/libprimesieve.so.12*

%files -n primesieve-devel
%doc doc/C_API.md doc/CPP_API.md
%{_libdir}/libprimesieve.so
%{_includedir}/primesieve.h
%{_includedir}/primesieve.hpp
%dir %{_includedir}/primesieve
%{_includedir}/primesieve/StorePrimes.hpp
%{_includedir}/primesieve/iterator.h
%{_includedir}/primesieve/iterator.hpp
%{_includedir}/primesieve/primesieve_error.hpp
%dir %{_libdir}/cmake/primesieve
%{_libdir}/cmake/primesieve/*.cmake
%{_libdir}/pkgconfig/primesieve.pc

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 12.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 18 2024 Kim Walisch <walki@fedoraproject.org> - 12.6-2
- Improved CPU cache detection

* Sun Nov 17 2024 Kim Walisch <walki@fedoraproject.org> - 12.6-1
- Added AVX512 and ARM SVE pre-sieving.

* Sat Oct 26 2024 Kim Walisch <walki@fedoraproject.org> - 12.5-1
- Improve thread load balancing for large number of CPU cores.

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 12.4-2
- convert license to SPDX

* Wed Jul 31 2024 Kim Walisch <walki@fedoraproject.org> - 12.4-1
- Improve CPUID code on x86 CPUs.
- Improve popcnt functions.

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 12.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Apr 17 2024 Kim Walisch <walki@fedoraproject.org> - 12.3-2
- Fix incorrect AXV512 example in C_API.md
- Fix incorrect AXV512 example in CPP_API.md

* Tue Apr 16 2024 Kim Walisch <walki@fedoraproject.org> - 12.3-1
- Add runtime POPCNT detection using CPUID for x86 CPUs
- Improve GCC/Clang multiarch preprocessor logic
- CMakeLists.txt: Remove POPCNT/BMI check for x86 CPUs

* Sun Mar 10 2024 Kim Walisch <walki@fedoraproject.org> - 12.1-1
- CMakeLists.txt: Fix undefined reference to pthread_create
- Fix -ffast-math failure of --test option
- Fix musl libc issue in unit tests
- Improve status output

* Mon Feb 19 2024 Kim Walisch <walki@fedoraproject.org> - 12.0-2
- Increase .so version to 12

* Mon Feb 19 2024 Kim Walisch <walki@fedoraproject.org> - 12.0-1
- New --stress-test[=MODE] command-line option
- Faster Riemann R function implementation
- New -R && --RiemannR command line options
- New --RiemannR-inverse command line option
- Add new --timeout option for stress testing
- Improve command-line option handling

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 10 2024 Kim Walisch <walki@fedoraproject.org> - 11.2-3
- New build required after fixing date in 11.2-2 changelog

* Wed Jan 10 2024 Kim Walisch <walki@fedoraproject.org> - 11.2-2
- Update to latest primesieve release archive from GitHub

* Tue Jan 09 2024 Kim Walisch <walki@fedoraproject.org> - 11.2-1
- Fix CMake libatomic detection
- Improved nth prime algorithm
- Fix off by 1 error in OpenMP example in C_API.md
- Fix off by 1 error in OpenMP example in CPP_API.md

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat May 13 2023 Kim Walisch <walki@fedoraproject.org> - 11.1-3
- Update to latest primesieve release archive from GitHub
- Fix incorrect date of version 11.1-1 in changelog

* Sat May 13 2023 Kim Walisch <walki@fedoraproject.org> - 11.1-2
- Fix incorrect date in changelog

* Sat May 13 2023 Kim Walisch <walki@fedoraproject.org> - 11.1-1
- Update to primesieve-11.1
- Vectorized pre-sieving algorithm using x64 SSE2 and ARM NEON
- Added POPCNT algorithm for x64 & AArch64
- Fix -Wstrict-prototypes warnings

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 07 2022 Kim Walisch <walki@fedoraproject.org> - 11.0-1
- Update to primesieve-11.0
- primesieve version now match libprimesieve version (.so version)
- Added new primesieve::iterator::jump_to() method (C++ API)
- Added new primesieve_jump_to() function (C API)
- Mark primesieve_skipto() as deprecated
- Fix use after free in primesieve::iterator::clear()
- Fix use after free in primesieve_iterator_clear()
- Fix potential memory leak in malloc_vector.hpp

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Kim Walisch <walki@fedoraproject.org> - 8.0-2
- Make SONAME explicit
- Fix changelog entry
- Increase version to 8.0-2 for new build

* Thu Jul 07 2022 Kim Walisch <walki@fedoraproject.org> - 8.0-1
- Update to primesieve-8.0
- Added multiarch support (POPCNT, BMI2, AVX512) for x64 CPUs
- Generating an array (or vector) of primes is up to 20% faster
- Main CMakeLists.txt has been split up into multiple modules
- Improved documentation of C & C++ APIs

* Tue May 03 2022 Kim Walisch <walki@fedoraproject.org> - 7.9-2
- Update to latest Fedora spec CMake syntax
- Update documentation files of primesieve-devel

* Tue May 03 2022 Kim Walisch <walki@fedoraproject.org> - 7.9-1
- Update to primesieve-7.9
- Reduced memory usage and faster initialization
- Reduced branch mispredictions by up to 30%
- Improved nth prime approximation
- Increase max sieve array size to 8 KiB

* Sun Jan 30 2022 Kim Walisch <walki@fedoraproject.org> - 7.8-1
- Update to primesieve-7.8
- Improved pre-sieving, up to 10% speedup
- Improved primesieve::iterator, up to 15% speedup

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 08 2021 Kim Walisch <walki@fedoraproject.org> - 7.7-1
- Update to primesieve-7.7
- Improved cache size detection on big.LITTLE CPUs

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 7.6-4
- Rebuilt for removed libstdc++ symbol (#1937698)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 09 2021 Kim Walisch <walki@fedoraproject.org> - 7.6-2
- Fix version number in ChangeLog

* Sat Jan 09 2021 Kim Walisch <walki@fedoraproject.org> - 7.6-1
- Update to primesieve-7.6

* Tue Aug 04 2020 Kim Walisch <walki@fedoraproject.org> - 7.5-6
- Fix CMake doc target issue, indicate path

* Tue Aug 04 2020 Kim Walisch <walki@fedoraproject.org> - 7.5-5
- Fix CMake issue, CMake build directory changed in Fedora 33

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.5-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Kim Walisch <walki@fedoraproject.org> - 7.5-1
- Update to primesieve-7.5

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Kim Walisch <walki@fedoraproject.org> - 7.4-2
- Rename libprimesieve to primesieve-libs
- Rename libprimesieve-devel to primesieve-devel
- Increase CMake version to >= 3.7

* Mon Apr 08 2019 Kim Walisch <walki@fedoraproject.org> - 7.4-1
- Update to primesieve-7.4
- Move Requires before description
- Drop libprimesieve-static package

* Sun Jul 08 2018 Kim Walisch <walki@fedoraproject.org> - 7.0-1
- Update to primesieve-7.0
- Fix erroneous date in changelog

* Sat Mar 24 2018 Kim Walisch <walki@fedoraproject.org> - 6.4-5
- Update to primesieve-6.4

* Fri Feb 16 2018 Kim Walisch <walki@fedoraproject.org> - 6.4-4
- Add libprimesieve package
- Improve summaries and descriptions
- Update to primesieve-6.4-rc2

* Tue Feb 06 2018 Kim Walisch <walki@fedoraproject.org> - 6.4-3
- Fix new issues from package review

* Wed Jan 31 2018 Kim Walisch <walki@fedoraproject.org> - 6.4-2
- Fix issues from package review

* Tue Jan 30 2018 Kim Walisch <walki@fedoraproject.org> - 6.4-1
- Initial package
