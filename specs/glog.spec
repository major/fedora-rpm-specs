Name:           glog
Version:        0.3.5
Release:        24%{?dist}
Summary:        A C++ application logging library
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/google/glog
Source0:        https://github.com/google/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  autoconf, gflags-devel >= 2.1.0
BuildRequires: make
Requires:       gflags
Requires:       gflags-devel >= 2.1.0

%description
Google glog is a library that implements application-level
logging. This library provides logging APIs based on C++-style
streams and various helper macros.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup

%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
autoconf
%configure --disable-static
%make_build

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm -rf $RPM_BUILD_ROOT/%{_docdir}/%{name}-%{version}

%ldconfig_scriptlets

%files
%doc ChangeLog COPYING README
%{_libdir}/libglog.so.*

%files devel
%doc doc/designstyle.css doc/glog.html
%{_libdir}/libglog.so
%{_libdir}/pkgconfig/libglog.pc
%dir %{_includedir}/glog
%{_includedir}/glog/*


%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.5-22
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-12
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Jeff Law <law@redhat.com> - 0.3.5-11
- Force C++14 as this code is not C++17 ready

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 10 2018 Filipe Rosset <rosset.filipe@gmail.com> - 0.3.5-6
- spec cleanup and modernization

* Wed Oct 10 2018 Sérgio Basto <sergio@serjux.com> - 0.3.5-5
- Rebuit for gflags-2.2.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sat Jul 29 2017 Filipe Rosset <rosset.filipe@gmail.com> - 0.3.5-1
- Upgrade to latest 0.3.5 fix FTBFS rhbz #1423617 #1300053 and #1473570

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Filipe Rosset <rosset.filipe@gmail.com> - 0.3.3-14
- Spec cleanup

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Mar 25 2016 Björn Esser <fedora@besser82.io> - 0.3.3-12
- Rebuilt for /lib64/libglog.so: undefined reference to
  'gflags::FlagRegisterer::FlagRegisterer'-madness

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.3-9
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 01 2014 John Khvatov <ivaxer@fedoraproject.org> - 0.3.3-6
- Rebuild against gflags.so.2.1

* Thu Apr 24 2014 Dan Fuhry <dfuhry@dattobackup.com> - 0.3.3-4
- Added patch for compatibility with gflags >= 2.1.0.

* Mon Aug 05 2013 John Khvatov <ivaxer@fedoraproject.org> - 0.3.3-3
- Removed installed but untracked docs.
   Fix for https://fedoraproject.org/wiki/Changes/UnversionedDocdirs

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 31 2013 John Khvatov <ivaxer@fedoraproject.org> - 0.3.3-1
- update to 0.3.3

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-4
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 03 2009 John A. Khvatov <ivaxer@fedoraproject.org> - 0.3.0-1
- update to 0.3.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Feb 27 2009 John A. Khvatov <ivaxer@fedoraproject.org> 0.2-5
- fixes for gcc 4.4

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 25 2009 John A. Khvatov <ivaxer@fedoraproject.org> 0.2-2
- update to 0.2

* Thu Dec 4 2008 John A. Khvatov <ivaxer@fedoraproject.org> 0.1.2-6
- fix %%{_includedir}
- fixed documentation

* Wed Dec 3 2008 John A. Khvatov <ivaxer@fedoraproject.org> 0.1.2-5
- Added configure regeneration

* Tue Dec 2 2008 John A. Khvatov <ivaxer@fedoraproject.org> 0.1.2-4
- Initial release
