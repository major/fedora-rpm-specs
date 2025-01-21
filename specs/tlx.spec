Name:           tlx
Version:        0.6.1
Release:        5%{?dist}
Summary:        Sophisticated C++ data structures, algorithms, and helpers

License:        BSL-1.0
URL:            https://panthema.net/tlx
Source0:        https://github.com/tlx/tlx/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make

%description
TLX is a collection of sophisticated C++ data structures, algorithms,
and miscellaneous helpers.  It contains:
- The fast tournament (loser) trees from MCSTL by Johannes Singler, with
  many fixes.
- A fast intrusive reference counter called CountingPtr, which has
  considerably less overhead than std::shared_ptr.
- Efficient and fast multiway merging algorithms from Johannes Singler,
  which were previously included with gcc.  The tlx version has many
  fixes and is available for clang and MSVC++.
- Many string manipulation algorithms for std::string.
- An improved version of the stx-btree implementation, which is
  basically always a better alternative to std::map (but not
  std::unordered_map).
- A copy of siphash for string hashing.
- Efficient sequential string sorting implementations such as radix sort
  and multikey quicksort.
- Much more; see the doxygen documentation.

%package       devel
Summary:       Headers and library links to build with tlx
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description   devel
Headers and library links to build with tlx.

%package       doc
# The content is BSL-1.0.  Other licenses are due to files installed by doxygen.
# doxygen-html/*.png: GPL-1.0-or-later
# doxygen-html/*.js: MIT
License:       BSL-1.0 AND GPL-1.0-or-later AND MIT
Summary:       Doxygen documentation for tlx
BuildArch:     noarch

%description   doc
Doxygen documentation for tlx.

%prep
%autosetup

%build
%cmake \
  -DTLX_BUILD_SHARED_LIBS:BOOL=ON \
  -DTLX_BUILD_STATIC_LIBS:BOOL=OFF \
  -DTLX_BUILD_STRING_SORTING:BOOL=ON \
  -DTLX_BUILD_TESTS:BOOL=ON \
  %{nil}
%cmake_build
doxygen

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc AUTHORS README.md
%{_libdir}/libtlx.so.0.6*

%files         devel
%{_includedir}/%{name}/
%{_libdir}/cmake/tlx/
%{_libdir}/libtlx.so
%{_libdir}/pkgconfig/tlx.pc

%files         doc
%doc doxygen-html

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jun 10 2023 Jerry James <loganjerry@gmail.com> - 0.6.1-1
- Version 0.6.1
- Upstream sets the SOVERSION again

* Wed May 17 2023 Jerry James <loganjerry@gmail.com> - 0.6.0-1
- Version 0.6.0
- Drop upstreamed cstdint patch
- Upstream fails to set the SOVERSION, so we do it for them for now

* Sat Jan 21 2023 Jerry James <loganjerry@gmail.com> - 0.5.20210401-2
- Add cstdint patch to fix FTBFS

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.20210401-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 14 2022 Jerry James <loganjerry@gmail.com> - 0.5.20210401-1
- Version 0.5.20210401
- Convert License tag to SPDX

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.20200222-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.20200222-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.20200222-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.20200222-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.20200222-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun  3 2020 Jerry James <loganjerry@gmail.com> - 0.5.20200222-1
- Version 0.5.2020022
- Drop -endian patch

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.20191212-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 2019 Jerry James <loganjerry@gmail.com> - 0.5.20191212-1
- Initial RPM
