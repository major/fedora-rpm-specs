
Name:           attica
Version:        0.4.2
Release:        32%{?dist}
Summary:        Implementation of the Open Collaboration Services API

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.kde.org
Source0:        http://download.kde.org/stable/attica/attica-%{version}.tar.bz2

BuildRequires:  cmake >= 2.8
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(QtNetwork) >= 4.7

%description
Attica is a Qt library that implements the Open Collaboration Services
API version 1.4.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
%{summary}.


%prep
%setup -q


%build
%cmake -DQT4_BUILD:BOOL=ON
%cmake_build


%install
%cmake_install


%check
# verify pkg-config sanitry/version
export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion libattica)" = "%{version}"


%ldconfig_scriptlets

%files
%doc AUTHORS README
%doc ChangeLog
%license COPYING
%{_libdir}/libattica.so.0.4*

%files devel
%{_includedir}/attica/
%{_libdir}/libattica.so
%{_libdir}/pkgconfig/libattica.pc


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4.2-31
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-21
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.4.2-15
- BR: gcc-c++, use %%license %%ldconfig_scriptlets

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.2-14
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.4.2-7
- Rebuilt for GCC 5 C++11 ABI change

* Wed Feb 18 2015 Rex Dieter <rdieter@fedoraproject.org> 0.4.2-5
- rebuild (gcc5)

* Thu Jan 08 2015 Rex Dieter <rdieter@fedoraproject.org> 0.4.2-5
- drop cmake/el6 hack

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Rex Dieter <rdieter@fedoraproject.org> 0.4.2-3
- .spec cleanup

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Jun 15 2013 Rex Dieter <rdieter@fedoraproject.org> 0.4.2-1
- 0.4.2

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 07 2013 Rex Dieter <rdieter@fedoraproject.org> 0.4.1-1
- 0.4.1

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Rex Dieter <rdieter@fedoraproject.org> 0.4.0-1
- 0.4.0

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 31 2011 Rex Dieter <rdieter@fedoraproject.org> 0.3.0-2
- update %%files for non-standard soname

* Fri Dec 30 2011 Rex Dieter <rdieter@fedoraproject.org> 0.3.0-1
- 0.3.0

* Tue Nov 15 2011 Rex Dieter <rdieter@fedoraproject.org> 0.2.9-1
- 0.2.9

* Sat Feb 26 2011 Rex Dieter <rdieter@fedoraproject.org> 0.2.0-1
- attica-0.2.0

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov 20 2010 Rex Dieter <rdieter@fedoraproject.org> -  0.1.91-1
- attica-0.1.91

* Tue May 18 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.1.4-1
- attica-0.1.4

* Wed Apr 07 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.1.3-1
- attica-0.1.3

* Thu Jan 14 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.1.2-1
- attica-0.1.2
- patch Version in libattica.pc
- %%build: %%_cmake_skip_rpath 

* Fri Dec 18 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.1.1-1
- attica-0.1.1

* Wed Dec  9 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.1.0-3
- upstream tarball
- %%files: tighten up a bit, track sonames

* Mon Dec  7 2009 Lorenzo Villani <lvillani@binaryhelix.net> - 0.1.0-2
- Out of sourcetree build
- Use make install/fast

* Sat Dec 5 2009 lvillani <lvillani@enterprise.binaryhelix.net> 0.1.0-1
- Initial release

