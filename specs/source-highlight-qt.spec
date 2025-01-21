Summary:       Library for performing syntax highlighting in Qt documents
Name:          source-highlight-qt
Version:       0.2.3
Release:       46%{?dist}
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:       GPL-3.0-only
URL:           http://srchiliteqt.sourceforge.net/
Source0:       http://downloads.sourceforge.net/project/srchiliteqt/source-highlight-qt/source-highlight-qt-%{version}.tar.gz
BuildRequires: make
BuildRequires: boost-devel
BuildRequires: source-highlight-devel
BuildRequires: qt-devel

%description
Source-highlight-qt is a library for performing syntax highlighting in
Qt documents by relying on GNU Source-Highlight library.

Although the use of GNU Source-highlight library is pretty hidden by
this library, so the programmer must not need the details of GNU
Source-highlight library, yet, some general notions of GNU
Source-highlight might be useful.

%package       devel
Summary:       Header files, libraries and development documentation for %{name}
Requires:      %{name} = %{version}-%{release}
Requires:      source-highlight-devel
Requires:      qt-devel
Requires:      boost-devel

%description   devel
This package contains the header files, static libraries and
development documentation for source-highlight-qt. If you like to
develop programs using source-highlight-qt, you will need to install
source-highlight-qt-devel.

%prep
%setup -q

%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
%configure --with-qt=%{_libdir}/qt4/bin
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -name \*.a -delete
find %{buildroot} -name \*.la -delete
mv %{buildroot}/usr/share/doc/source-highlight-qt/examples __examples
mv %{buildroot}/usr/share/doc/source-highlight-qt/source-highlight-qt.html .
rm -rf %{buildroot}/usr/share/{doc,info}

%check
pushd lib/tests
make check

%ldconfig_scriptlets

%files
%doc AUTHORS COPYING ChangeLog NEWS THANKS TODO.txt
%{_libdir}/libsource-highlight-qt4.so.3*

%files devel
%doc __examples/* source-highlight-qt.html
%{_includedir}/srchiliteqt
%{_libdir}/libsource-highlight-qt4.so
%{_libdir}/pkgconfig/source-highlight-qt4.pc

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.3-45
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 0.2.3-42
- Rebuilt for Boost 1.83

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 0.2.3-40
- Rebuilt for Boost 1.81

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 0.2.3-37
- Rebuilt for Boost 1.78

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 0.2.3-35
- Rebuilt for Boost 1.76

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 0.2.3-32
- Rebuilt for Boost 1.75

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Jeff Law <law@redhat.com> - 0.2.3-30
- Force C++14 as this code is not C++17 ready

* Sat May 30 2020 Jonathan Wakely <jwakely@redhat.com> - 0.2.3-29
- Rebuilt for Boost 1.73

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Jonathan Wakely <jwakely@redhat.com> - 0.2.3-25
- Rebuilt for Boost 1.69

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> - 0.2.3-20
- Rebuilt for Boost 1.64

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 28 2017 Jonathan Wakely <jwakely@redhat.com> - 0.2.3-18
- Rebuilt for Boost 1.63

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Jonathan Wakely <jwakely@redhat.com> - 0.2.3-16
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.2.3-15
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-14
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.2.3-13
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.2.3-11
- Rebuilt for GCC 5 C++11 ABI change

* Wed Jan 28 2015 Petr Machata <pmachata@redhat.com> - 0.2.3-10
- Rebuild for boost 1.57.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 0.2.3-7
- rebuild for boost 1.55.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 28 2013 Petr Machata <pmachata@redhat.com> - 0.2.3-5
- Rebuild for boost 1.54.0

* Wed Jun 26 2013 Terje Rosten <terje.rosten@ntnu.no> - 0.2.3-4
- Add boost-devel as req

* Thu Mar 07 2013 Terje Rosten <terje.rosten@ntnu.no> - 0.2.3-3
- fix req in -devel subpackage

* Fri Mar 01 2013 Terje Rosten <terje.rosten@ntnu.no> - 0.2.3-2
- enable tests
- remove buildroot cleaning

* Mon Feb 25 2013 Terje Rosten <terje.rosten@ntnu.no> - 0.2.3-1
- initial package
