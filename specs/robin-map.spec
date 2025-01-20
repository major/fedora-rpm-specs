%global debug_package %{nil}

Name:           robin-map
Version:        1.3.0
Release:        4%{?dist}
Summary:        C++ implementation of a fast hash map and hash set using robin hood hashing

License:        MIT
URL:            https://github.com/Tessil/robin-map
Source0:        https://github.com/Tessil/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  cmake gcc-c++
BuildRequires:  boost-devel
BuildRequires:  boost-static

%description
The robin-map library is a C++ implementation of a fast hash map and hash set
using open-addressing and linear robin hood hashing with backward shift
deletion to resolve collisions.

*** This is a header only library. ***
The package you want is %{name}-devel.


%package devel
Summary:        %{summary}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_packaging_header_only_libraries
Provides:       robin-map-static = %{version}-%{release}

%description devel
The robin-map library is a C++ implementation of a fast hash map and hash set
using open-addressing and linear robin hood hashing with backward shift
deletion to resolve collisions.

Four classes are provided: tsl::robin_map, tsl::robin_set, tsl::robin_pg_map
and tsl::robin_pg_set. The first two are faster and use a power of two growth
policy, the last two use a prime growth policy instead and are able to cope
better with a poor hash function. Use the prime version if there is a chance of
repeating patterns in the lower bits of your hash (e.g. you are storing
pointers with an identity hash function). See GrowthPolicy for details.

A benchmark of tsl::robin_map against other hash maps may be found here. This
page also gives some advices on which hash table structure you should try for
your use case (useful if you are a bit lost with the multiple hash tables
implementations in the tsl namespace).


%prep
%autosetup -p1


%build
%cmake


%install
%cmake_install


%check
pushd tests
%cmake
%cmake_build
%{_vpath_builddir}/tsl_robin_map_tests


%files devel
%license LICENSE
%doc README.md
%{_datadir}/cmake/tsl-%{name}/*.cmake
%{_includedir}/tsl/


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Sep 01 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 1.3.0-3
- Add -static virtual Provide for header-only library

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Apr 27 2024 Richard Shaw <hobbes1069@gmail.com> - 1.3.0-1
- Update to 1.3.0.

* Thu Mar 21 2024 Richard Shaw <hobbes1069@gmail.com> - 1.2.2-1
- Update to 1.2.2.

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Richard Shaw <hobbes1069@gmail.com> - 1.2.1-1
- Update to 1.2.1.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Apr  6 2022 Richard Shaw <hobbes1069@gmail.com> - 1.0.1-1
- Update to 1.0.1.

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 21 2020 Richard Shaw <hobbes1069@gmail.com> - 0.6.3-1
- Update to 0.6.3.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Richard Shaw <hobbes1069@gmail.com> - 0.6.2-1
- Update to 0.6.2.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 27 2019 Richard Shaw <hobbes1069@gmail.com> - 0.6.1-1
- Update to 0.6.1.

* Tue Feb 12 2019 Richard Shaw <hobbes1069@gmail.com> - 0.6.0-2
- Add patch for GCC 9 warnings.

* Mon Feb 11 2019 Richard Shaw <hobbes1069@gmail.com> - 0.6.0-1
- Update to 0.6.0.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 11 2018 Richard Shaw <hobbes1069@gmail.com> - 0.2.0-1
- Initial packaging.
