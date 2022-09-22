%global sover 13

Name: log4cxx
Version: 0.13.0
Release: 2%{?dist}
Summary: A port to C++ of the Log4j project

License: ASL 2.0
URL: http://logging.apache.org/log4cxx/index.html
Source0: http://www.apache.org/dist/logging/log4cxx/%{version}/apache-%{name}-%{version}.tar.gz

BuildRequires: apr-devel
BuildRequires: apr-util-devel
BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: gcc-c++

%description
Log4cxx is a popular logging package written in C++. One of its distinctive
features is the notion of inheritance in loggers. Using a logger hierarchy it
is possible to control which log statements are output at arbitrary
granularity. This helps reduce the volume of logged output and minimize the
cost of logging.

%package devel
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: Header files for Log4xcc - a port to C++ of the Log4j project

%description devel
Header files and documentation you can use to develop with %{name}.

%package doc
Summary: Documentation for %{name}
BuildArch: noarch

%description doc
Documentation for %{name}.


%prep
%autosetup -n apache-%{name}-%{version}

%build
%cmake -DBUILD_SITE=ON
%cmake_build

%install
%cmake_install

%check
# Tests are flaky, run for informational purposes.
%ctest || true

%files
%{_libdir}/liblog4cxx.so.%{sover}*

%doc NOTICE KEYS
%license LICENSE


%files devel
%{_includedir}/log4cxx
%{_libdir}/liblog4cxx.so
%{_libdir}/pkgconfig/liblog4cxx.pc
%{_libdir}/cmake/log4cxx

%files doc
%license LICENSE
%doc %{_vpath_builddir}/src/site/html/

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Apr 25 2022 Till Hofmann <thofmann@fedoraproject.org> - 0.13.0-1
- Update to 0.13.0
- Remove upstreamed patch

* Tue Apr 12 2022 Till Hofmann <thofmann@fedoraproject.org> - 0.12.1-1
- Update to 0.12.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 17 2020 Till Hofmann <thofmann@fedoraproject.org> - 0.11.0-1
- Update to 0.11.0
- Switch to cmake
- Run tests

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 23 2016 Till Hofmann <till.hofmann@posteo.de> - 0.10.0-22
- Fix missing isa in devel's Requires:
- Remove unused shlib dependencies
- Do not build static libs

* Fri Dec 23 2016 Till Hofmann <till.hofmann@posteo.de> - 0.10.0-21
- Split documentation into a subpackage
- Remove unnecessary dependencies of devel on pkgconfig, apr-devel

* Thu Dec 22 2016 Till Hofmann <till.hofmann@posteo.de> - 0.10.0-20
- Add patches to fix GCC6 errors

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.10.0-18
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-12
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 01 2009 Caolán McNamara <caolanm@redhat.com> - 0.10.0-9
- Rebuild for new db4

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 25 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 0.10.0-7
- Fix FTBFS: updated log4cxx-cstring.patch for gcc 4.4

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 1 2008 Hayden James - 0.10.0-5
- Simplifed doc files in package

* Sat Nov 29 2008 Hayden James - 0.10.0-4
- Moved doxygen docs into doc folder 
- Removed unnecessary apr-util-devel dependency

* Thu Nov 27 2008 Hayden James - 0.10.0-3
- Remove need for chrpath and other misc changes.

* Thu Nov 27 2008 Hayden James - 0.10.0-2
- Build requires doxygen for documentation

* Sun Nov 16 2008 Hayden James - 0.10.0-1
- Initial package.

