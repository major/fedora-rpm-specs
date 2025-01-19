
Name:           krecipes
Version:        2.1.0
Release:        23%{?dist}
Summary:        Application to manage recipes and shopping-lists

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://userbase.kde.org/Krecipes
Source0:        http://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz

# Fix FTBFS with GCC 6 (#1307698), upstream patch by Pino Toscano
# http://commits.kde.org/krecipes/f6d4f709ec57835b3fa4a660239a07321c9d02ff
Patch100:       krecipes-2.1.0-gcc6.patch

BuildRequires:  desktop-file-utils
BuildRequires:  shared-mime-info
BuildRequires:  gettext
BuildRequires:  kdelibs4-devel
BuildRequires:  kdelibs4-webkit-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  sqlite-devel
BuildRequires: make

%{?_kde4_macros_api:Requires: kde4-macros(api) = %{_kde4_macros_api}}
%{?_kde4_version:Requires: kdelibs4%{?_isa} >= %{_kde4_version}}
Requires:       kde-runtime%{?_kde4_version: >= %{_kde4_version}}
Requires:       oxygen-icon-theme
Requires:       hicolor-icon-theme
Requires:       qt4-sqlite
Requires:       qt4-mysql
Requires:       qt4-postgresql

%description
Krecipes is a program that lets you to manage your recipes, create
shopping lists, choose a recipe based on available ingredients and plan
your menu/diet in advance.


%prep
%setup -q -n %{name}-%{version}
%patch -P100 -p1 -b .gcc6

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install DESTDIR=%{buildroot} -C %{_target_platform}

desktop-file-validate \
  %{buildroot}%{_kde4_datadir}/applications/kde4/%{name}.desktop

%find_lang %{name} --with-kde

%files -f %{name}.lang
%doc TODO AUTHORS README COPYING ChangeLog
%{_kde4_bindir}/krecipes
%{_kde4_datadir}/applications/kde4/krecipes.desktop
%{_kde4_datadir}/mime/packages/krecipes-mime.xml
%{_kde4_iconsdir}/hicolor/*/apps/*
%{_kde4_iconsdir}/oxygen/*/*/*
%{_kde4_appsdir}/krecipes/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.0-22
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.0-7
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.0-5
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 14 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.1.0-1
- Update to 2.1.0
- Update URL from SourceForge to https://userbase.kde.org/Krecipes
- Drop BR qimageblitz-devel, not used anymore
- Backport upstream patch to fix FTBFS with GCC 6 (#1307698)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.10.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.9.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.0-0.8.beta2
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.7.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 12 2014 Rex Dieter <rdieter@fedoraproject.org> 2.0-0.6.beta2
- update mime scriptlets

* Thu Jun 19 2014 Rex Dieter <rdieter@fedoraproject.org> 2.0-0.5.beta2
- BR: kdelibs4-webkit-devel

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.4.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.3.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.2.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 23 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.0-0.1.beta2
- Update to 2.0 beta2 (long overdue), now kdelibs4-based
- Clean up specfile

* Tue Jul 31 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.0-0.6.beta2
- Fix FTBFS with g++ 4.7

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.5.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.4.beta2
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.3.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.2.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 17 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 1.0-0.1.beta2
- Update to 1.0beta2 as it fixes a crash that prevents krecipes from starting
  with sqlite backend.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 16 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.9.1-11
- re-enable mysql/postgresql support
- re-enable mostly harmless X11 patch

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Mar 31 2008 Rex Dieter <rdieter@fedoraproject.org> - 0.9.1-9
- gcc43 patch (#433986)
- BR: gettext
- --without-mysql --without-postgresql

* Thu Mar 13 2008 Dennis Gilmore <dennis@ausil.us> - 0.9.1-8
- fix BuildRequires

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.1-7
- Autorebuild for GCC 4.3

* Wed Aug 29 2007 Dennis Gilmore <dennis@ausil.us> - 0.9.1-6
- rebuild for F8
- clarify license GPLv2+

* Sat Sep 02 2006 Dennis Gilmore <dennis@ausil.us> - 0.9.1-5
- rebuild for fc6

* Sat Feb 18 2006 Dennis Gilmore <dennis@ausil.us> - 0.9.1-4
-rebuild for fc5

* Wed Dec 21 2005 Dennis Gilmore <dennis@ausil.us> - 0.9.1-3
-Rebuild for gcc 4.1

* Mon Dec 05 2005 Dennis Gilmore <dennis@ausil.us> - 0.9.1-2
- retag because patch wasnt uploaded

* Sun Dec 04 2005 Dennis Gilmore <dennis@ausil.us> - 0.9.1-1
- update to 0.9.1  this fixes a bug in mysql database creation

* Sat Dec 03 2005 Dennis Gilmore <dennis@ausil.us> - 0.9-3
- fix BuildRequies for libacl and add patch for X check.

* Wed Nov 30 2005 Dennis Gilmore <dennis@ausil.us> - 0.9-2
- fix missing files

* Wed Nov 30 2005 Dennis Gilmore <dennis@ausil.us> - 0.9-1
- update to 0.9

* Thu Oct 20 2005 Dennis Gilmore <dennis@ausil.us> - 0.8.1-3
- add BuildRequires desktop-file-utils  http://fedoraproject.org/wiki/QAChecklist
- add %%post and %%postun scriptlets  to notify of new icons per
- http://standards.freedesktop.org/icon-theme-spec/icon-theme-spec-latest.html#implementation_notes

* Sat Jul 30 2005 <dennis@ausil.us> - 0.8.1-2
- Remove hard requirement for qt-MySQL and qt-Postgresql
- add exlicit QT lib and include dirs  for x86_64 build
- Fix summary to not read like a marketing ploy.

* Sun Jul 24 2005 <dennis@ausil.us> - 0.8.1-1
- Initial build
