Name:		pmemkv
Version:	1.5.0
Release:	4%{?dist}
Summary:	Key/Value Datastore for Persistent Memory

License:	BSD
URL:		https://github.com/pmem/pmemkv
Source0:	https://github.com/pmem/pmemkv/archive/%{version}/%{name}-%{version}.tar.gz
# There's some work to port dependencies to non-x86, but we're not there yet.
ExclusiveArch:	x86_64

BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	valgrind
BuildRequires:	valgrind-devel
BuildRequires:	pkg-config
BuildRequires:	pandoc
BuildRequires:	libpmemobj++-devel >= 1.13
BuildRequires:	libpmemobj-devel >= 1.9
BuildRequires:	tbb-devel
BuildRequires:	memkind-devel
BuildRequires:	rapidjson-devel
BuildRequires:	gtest-devel
BuildRequires:  pmempool
BuildRequires:  libunwind-devel

%description
Pmemkv is a family of key:value stores, developed with persistent memory
in mind -- yet rather than being tied to a single backing implementation,
it presents a common interface to a number of engines, both provided by
pmemkv itself and external.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%cmake
%cmake_build


%install
%cmake_install


%check
export PMEM_IS_PMEM_FORCE=1; ctest -j1 --output-on-failure -E 'vcmap__concurrent_put_get_remove_.*'


%files
%{_libdir}/libpmemkv*.so.1*
%license LICENSE

%files devel
%{_includedir}/*.h
%{_includedir}/*.hpp
%{_mandir}/*/*pmemkv*
%{_libdir}/libpmemkv*.so
%{_libdir}/pkgconfig/libpmemkv*.pc


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 28 2022 Adam Borowski <kilobyte@angband.pl> 1.5.0-3
- Disable a flaky test.

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 30 2021 Adam Borowski <kilobyte@angband.pl> 1.5.0-1
- Upstream release 1.5.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb 19 2021 Adam Borowski <kilobyte@angband.pl> 1.4-2
- Disable parallel tests, they kept running out of disk space on koji.

* Thu Feb 18 2021 Adam Borowski <kilobyte@angband.pl> 1.4-1
- Upstream release 1.4
- Avoid ctest env vars being eaten by "cd" inside new macros.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 05 2020 Adam Borowski <kilobyte@angband.pl> 1.3-1
- Upstream release 1.3
- Bump BReqs for pmemobj and pmemobj-cpp.
- Add BReqs for pmempool and libunwind.

* Mon Oct  5 2020 Adam Borowski <kilobyte@angband.pl> 1.1-4
- Adjust to changed Fedora cmake macros.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 12 2020 Adam Borowski <kilobyte@angband.pl> 1.1-1
- Upstream release 1.1
- Bump BReqs for pmemobj and pmemobj-cpp.

* Tue Feb 11 2020 Adam Borowski <kilobyte@angband.pl> 1.0.2-1
- Upstream release 1.0.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 29 2019 Adam Borowski <kilobyte@angband.pl> 1.0.1-1
- Initial packaging
