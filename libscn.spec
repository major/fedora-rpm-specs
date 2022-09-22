%global intname scn
%global upname %{intname}lib

Name: libscn
Version: 1.1.2
Release: 3%{?dist}

License: ASL 2.0
Summary: Library for replacing scanf and std::istream
URL: https://github.com/eliaskosunen/%{upname}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: doctest-devel
BuildRequires: fast_float-devel
# Since fast_float is header-only, we are required to BR the -static virtual
# Provide for dependency tracking purposes.
BuildRequires: fast_float-static
BuildRequires: gcc-c++
BuildRequires: google-benchmark-devel
BuildRequires: ninja-build

%description
%{upname} is a modern C++ library for replacing scanf and std::istream.

This library attempts to move us ever so closer to replacing iostreams
and C stdio altogether. It's faster than iostream (see Benchmarks) and
type-safe, unlike scanf. Think {fmt} but in the other direction.

This library is the reference implementation of the ISO C++ standards
proposal P1729 "Text Parsing".

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -n %{upname}-%{version} -p1

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DSCN_BENCHMARKS:BOOL=ON \
    -DSCN_DOCS:BOOL=OFF \
    -DSCN_EXAMPLES:BOOL=OFF \
    -DSCN_INSTALL:BOOL=ON \
    -DSCN_PEDANTIC:BOOL=OFF \
    -DSCN_TESTS:BOOL=ON \
    -DSCN_USE_BUNDLED_FAST_FLOAT:BOOL=OFF \
    -DSCN_WERROR:BOOL=OFF
%cmake_build

%check
%ctest

%install
%cmake_install
rm -rf %{buildroot}%{_datadir}/%{intname}

%files
%doc README.md
%license LICENSE
%{_libdir}/%{name}.so.0*

%files devel
%{_includedir}/%{intname}/
%{_libdir}/cmake/%{intname}/
%{_libdir}/%{name}.so

%changelog
* Sat Aug 06 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 1.1.2-3
- Add BR on fast_float-static

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Mar 19 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1.2-1
- Updated to version 1.1.2.

* Thu Mar 17 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1.1-1
- Updated to version 1.1.1.

* Sun Mar 13 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1-1
- Updated to version 1.1.

* Tue Mar 01 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0-1
- Updated to version 1.0.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 15 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.4-3
- Rebuilt due to google-benchmark 1.6.0 update.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jan 31 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.4-1
- Updated to version 0.4.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 06 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3-2
- Added patch with library destination fixes.

* Tue Aug 04 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3-1
- Initial SPEC release.
