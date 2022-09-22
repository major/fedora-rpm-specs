Name:           mingw-cxxtest
Version:        3.10.1
Release:        27%{?dist}
Summary:        A JUnit-like testing framework for C++

License:        LGPLv2+
URL:            http://cxxtest.tigris.org
Source0:        http://cxxtest.tigris.org/files/documents/6421/43281/cxxtest-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  mingw32-filesystem

%description
CxxTest is a JUnit/CppUnit/xUnit-like framework for C++.
Its advantages over existing alternatives are that it:
 - doesn't require RTTI
 - doesn't require member template functions
 - doesn't require exception handling
 - doesn't require any external libraries (including memory management,
   file/console I/O, graphics libraries)


%package -n mingw32-cxxtest
Summary:        A JUnit-like testing framework for C++
Requires:       mingw32-filesystem

# Remove the -doc subpackage as it duplicates what's in native cxxtest-doc
Obsoletes:      mingw32-cxxtest-doc < 3.10.1-5

%description -n mingw32-cxxtest
CxxTest is a JUnit/CppUnit/xUnit-like framework for C++.
Its advantages over existing alternatives are that it:
 - doesn't require RTTI
 - doesn't require member template functions
 - doesn't require exception handling
 - doesn't require any external libraries (including memory management,
   file/console I/O, graphics libraries)


%prep
%setup -q -n cxxtest

%build


%install
mkdir -p $RPM_BUILD_ROOT/%{mingw32_includedir}/cxxtest
install -D -p -m 644 cxxtest/* $RPM_BUILD_ROOT/%{mingw32_includedir}/cxxtest


%files -n mingw32-cxxtest
%doc COPYING
%{mingw32_includedir}/cxxtest/


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 08 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.10.1-9
- Put the files in the correct package

* Wed Mar 07 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.10.1-8
- Renamed the source package to mingw-cxxtest (RHBZ #800855)
- Use mingw macros without leading underscore

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.10.1-7
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 22 2011 Adam Stokes <astokes@fedoraproject.org> - 3.10.1-4
- Initial Build
