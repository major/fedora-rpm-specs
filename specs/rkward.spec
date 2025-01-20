Name:           rkward
Version:        0.7.5
Release:        6%{?dist}
Summary:        Graphical frontend for R language

License:        GPL-2.0-or-later
URL:            https://%{name}.kde.org/
Source0:        https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-format-security-fix.patch

BuildRequires:  gcc-c++, cmake, extra-cmake-modules
BuildRequires:  R-core-devel
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Qml)
%ifarch %{qt5_qtwebengine_arches}
BuildRequires:  cmake(Qt5WebEngine)
%endif
BuildRequires:  kf5-rpm-macros
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5WebKit)
BuildRequires:  hicolor-icon-theme, desktop-file-utils
Requires:       hicolor-icon-theme, shared-mime-info

%description
RKWard aims to provide an easily extensible, easy to use IDE/GUI for the
R-project. RKWard tries to combine the power of the R-language with the
(relative) ease of use of commercial statistics tools. Long term plans
include integration with office suites

%prep
%autosetup -p1

%build
%cmake_kf5

%cmake_build

%install
%cmake_install

desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop

## File lists
# locale's
%find_lang %{name} --with-kde || touch %{name}.lang

%files -f %{name}.lang
%doc README COPYING TODO AUTHORS
%doc %{_datadir}/doc/HTML/en/%{name}/
%doc %{_datadir}/doc/HTML/en/%{name}plugins/
%doc %lang(it) %{_datadir}/doc/HTML/it/%{name}/
%doc %lang(nl) %{_datadir}/doc/HTML/nl/%{name}/
%doc %lang(nl) %{_datadir}/doc/HTML/nl/%{name}plugins/
%doc %lang(sv) %{_datadir}/doc/HTML/sv/%{name}/
%doc %lang(sv) %{_datadir}/doc/HTML/sv/%{name}plugins/
%doc %lang(uk) %{_datadir}/doc/HTML/uk/%{name}/
%doc %lang(uk) %{_datadir}/doc/HTML/uk/%{name}plugins/
%{_datadir}/applications/org.kde.%{name}.desktop
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/22x22/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svgz
%{_datadir}/org.kde.syntax-highlighting/syntax/r*.xml
%{_datadir}/kservices5/%{name}.protocol
%{_datadir}/ktexteditor_snippets/data/RKWard*.xml
%{_datadir}/metainfo/org.kde.%{name}.appdata.xml
%{_datadir}/mime/packages/vnd.%{name}.r.xml
%{_datadir}/mime/packages/vnd.kde.%{name}-output.xml
%{_datadir}/mime/packages/vnd.kde.rmarkdown.xml
%{_datadir}/%{name}/
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%lang(ca) %{_mandir}/ca/man1/%{name}.1*
%lang(de) %{_mandir}/de/man1/%{name}.1*
%lang(it) %{_mandir}/it/man1/%{name}.1*
%lang(nl) %{_mandir}/nl/man1/%{name}.1*
%lang(sv) %{_mandir}/sv/man1/%{name}.1*
%lang(uk) %{_mandir}/uk/man1/%{name}.1*
%{_libexecdir}/%{name}.rbackend

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 0.7.5-4
- R-maint-sig mass rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Sep 09 2023 Iñaki Úcar <iucar@fedoraproject.org> - 0.7.5-1
- update to 0.7.5
- switch to SPDX

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 0.7.4-4
- R-maint-sig mass rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 20 2022 Tom Callaway <spot@fedoraproject.org> - 0.7.4-2
- drop unused BR on pcre-devel

* Thu Jul 28 2022 Tom Callaway <spot@fedoraproject.org> - 0.7.4-1
- update to 0.7.4
- R 4.2.1

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun  7 2021 Tom Callaway <spot@fedoraproject.org> - 0.7.2-4
- rebuild for R 4.1.0

* Tue May  4 2021 Tom Callaway <spot@fedoraproject.org> - 0.7.2-3
- rebuild for R 4.0.5

* Mon Feb 15 2021 Tom Callaway <spot@fedoraproject.org> - 0.7.2-2
- properly apply lang tags

* Mon Feb 15 2021 Tom Callaway <spot@fedoraproject.org> - 0.7.2-1
- update to 0.7.2
- rebuild for R 4.0.4

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 13 2020 Tom Callaway <spot@fedoraproject.org> - 0.7.1-6
- rebuild for R 4.0.3
- adjust for new cmake macros

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Tom Callaway <spot@fedoraproject.org> - 0.7.1-3
- rebuild for R 4.0.2

* Fri May  8 2020 Tom Callaway <spot@fedoraproject.org> - 0.7.1-2
- rebuild for R 4.0.0

* Tue Mar  3 2020 Tom Callaway <spot@fedoraproject.org> - 0.7.1-1
- update to 0.7.1, R 3.6.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 2019 Tom Callaway <spot@fedoraproject.org> - 0.7.0-11
- rebuild for R 3.6.2

* Sat Oct 19 2019 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.7.0-10
- rebuild in Rawhide after unretirement

* Fri Aug 16 2019 Tom Callaway <spot@fedoraproject.org> - 0.7.0-9
- rebuild for R 3.6.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Tom Callaway <spot@fedoraproject.org> - 0.7.0-7
- rebuild for R 3.6.0

* Mon Mar 11 2019 Tom Callaway <spot@fedoraproject.org> - 0.7.0-6
- rebuild for R 3.5.3

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Tom Callaway <spot@fedoraproject.org> - 0.7.0-4
- rebuild for R 3.5.2

* Fri Sep 14 2018 Tom Callaway <spot@fedoraproject.org> - 0.7.0-3
- rebuild for R 3.5.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 14 2018 Tom Callaway <spot@fedoraproject.org> - 0.7.0-1
- update to 0.7.0, R 3.5.0

* Wed Mar 28 2018 Tom Callaway <spot@fedoraproject.org> - 0.6.5-14
- rebuild for R 3.4.4

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.5-12
- Remove obsolete scriptlets

* Mon Dec  4 2017 Tom Callaway <spot@fedoraproject.org> - 0.6.5-11
- rebuild for R 3.4.3

* Fri Oct 27 2017 Tom Callaway <spot@fedoraproject.org> - 0.6.5-10
- rebuild for R 3.4.2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Tom Callaway <spot@fedoraproject.org> - 0.6.5-7
- rebuild for R 3.4.1

* Mon May 15 2017 Tom Callaway <spot@fedoraproject.org> - 0.6.5-6
- rebuild for R 3.4.0

* Wed Mar  8 2017 Tom Callaway <spot@fedoraproject.org> - 0.6.5-5
- rebuild for R 3.3.3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 31 2016 Tom Callaway <spot@fedoraproject.org> - 0.6.5-3
- rebuild for R 3.3.2

* Wed Jul  6 2016 Tom Callaway <spot@fedoraproject.org> - 0.6.5-2
- rebuild for R 3.3.1

* Tue May 10 2016 Tom Callaway <spot@fedoraproject.org> - 0.6.5-1
- update to 0.6.4, R 3.3.0

* Fri Mar 18 2016 Tom Callaway <spot@fedoraproject.org> - 0.6.4-1
- update to 0.6.4, R 3.2.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 11 2015 Tom Callaway <spot@fedoraproject.org> - 0.6.3-6
- R 3.2.3

* Fri Aug 14 2015 Tom Callaway <spot@fedoraproject.org> - 0.6.3-5
- R 3.2.2

* Fri Jun 19 2015 Tom Callaway <spot@fedoraproject.org> - 0.6.3-4
- R 3.2.1

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 30 2015 Tom Callaway <spot@fedoraproject.org> - 0.6.3-2
- R 3.2.0

* Tue Mar 10 2015 Tom Callaway <spot@fedoraproject.org> - 0.6.3-1
- update to 0.6.3
- R 3.1.3

* Sat Jan 31 2015 Rex Dieter <rdieter@fedoraproject.org> 0.6.2-2
- Requires: kate4-part (plasma5, kde-apps cleanup)

* Sat Nov  1 2014 Tom Callaway <spot@fedoraproject.org> - 0.6.2-1
- update to 0.6.2
- R 3.1.2

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 16 2014 Tom Callaway <spot@fedoraproject.org> - 0.6.1-9
- rebuild for R 3.1.1

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 21 2014 Tom Callaway <spot@fedoraproject.org> - 0.6.1-7
- rebuild for R 3.1.0

* Sun Mar 23 2014 Tom Callaway <spot@fedoraproject.org> - 0.6.1-6
- update for R 3.0.3

* Sun Dec 22 2013 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.6.1-5
- Add blas-devel and lapack-devel as BR

* Wed Oct 16 2013 Tom Callaway <spot@fedoraproject.org> - 0.6.1-4
- update for R 3.0.2

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 17 2013 Tom Callaway <spot@fedoraproject.org> - 0.6.1-2
- rebuild for 3.0.1

* Thu Apr 11 2013 Tom Callaway <spot@fedoraproject.org> - 0.6.1-1
- update to 0.6.1 (build for R3)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 29 2012 Tom Callaway <spot@fedoraproject.org> - 0.6.0-2
- rebuild for R 2.15.2

* Mon Oct 29 2012 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.6.0-1
- Update to release 0.6.0

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul  2 2012 Tom Callaway <spot@fedoraproject.org> 0.5.7-6
- rebuild for R 2.15.1

* Sat Mar 31 2012 Tom Callaway <spot@fedoraproject.org> 0.5.7-5
- rebuild for R 2.15.0

* Mon Jan  9 2012 Tom Callaway <spot@fedoraproject.org> 0.5.7-4
- rebuild for R 2.14.1

* Tue Nov 15 2011 Rex Dieter <rdieter@fedoraproject.org> 0.5.7-3
- Requires: kate-part (#744443)

* Wed Nov  9 2011 Tom Callaway <spot@fedoraproject.org> 0.5.7-2
- rebuild for R 2.14.0

* Tue Oct 25 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.7-1
- Update to 0.5.7

* Fri Oct  7 2011 Tom Callaway <spot@fedoraproject.org> 0.5.6-3
- rebuild for R 2.13.2

* Mon Jul 11 2011 Tom Callaway <spot@fedoraproject.org> 0.5.6-2
- rebuild for R 2.13.1

* Tue Jun 21 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.6-1
- Update to 0.5.6

* Fri Apr 15 2011 Tom Callaway <spot@fedoraproject.org> 0.5.5-2
- rebuild for R 2.13.0

* Sun Mar 20 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.5-1
- Update to 0.5.5

* Sun Feb 27 2011 Tom Callaway <spot@fedoraproject.org> 0.5.4-4
- rebuild for R 2.12.2

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Tom Callaway <spot@fedoraproject.org> 0.5.4-2
- rebuild for R 2.12.1

* Sun Nov 07 2010 pingou <pingou@pingoured.fr> - 0.5.4-1
- Update to 0.5.4
- Remove patch from Rex (upstreamed)

* Mon Jun 28 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.5.3-3
- FTBFS: patch handbook for kde-4.5 (#599758)
- update icon scriptlets
- use %%find_lang --with-kde
- %%files: use %%_kde4_appsdir macro

* Mon Jun 28 2010 pingou <pingou@pingoured.fr> - 0.5.3-2
- Change BR kdelibs4-devel to kdelibs-devel

* Mon May 31 2010 pingou <pingou@pingoured.fr> - 0.5.3-1
- Update to 0.5.3

* Wed Nov 25 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.5.2-2
- Rebuild for Qt 4.6.0 RC1 in F13 (was built against Beta 1 with unstable ABI)

* Mon Nov 09 2009 pingou <pingou@pingoured.fr> - 0.5.2-1
- Update to 0.5.2

* Mon Aug 03 2009 pingou <pingou@pingoured.fr> - 0.5.1-1
- Update to 0.5.1 

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0d-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 20 2009 pingou <pingou@pingoured.fr> - 0.5.0d-1
- Update to release 0.5.0d

* Wed Apr 22 2009 pingou <pingou@pingoured.fr> - 0.5.0c-2
- Rebuild for R-2.9.0
- Uses %%global instead of %%define

* Tue Mar 31 2009 pingou <pingou@pingoured.fr> - 0.5.0c-1
- Update to version 0.5.0c
- Remove the BuildRequires on PyQt-devel

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0b-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 05 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.5.0b-11
- Rebuild for fixed kde-filesystem (macros.kde4) (get rid of rpaths)

* Sun Nov 30 2008 pingou <pingou -AT- pingoured.fr> 0.5.0b-10
- Own directory rkward -- #473660

* Wed Oct 29 2008 pingou <pingou -AT- pingoured.fr> 0.5.0b-9
- Move the sed to prep 

* Wed Oct 29 2008 pingou <pingou -AT- pingoured.fr> 0.5.0b-8
- Rebuild for R 2.8.0 
- Remove the Rdevices.h which make the build failed

*Fri Jun 06 2008 Pingou <pingoufc4@yahoo.fr> 0.5.0b-7
- Correct a typo in files

*Fri Jun 06 2008 Pingou <pingoufc4@yahoo.fr> 0.5.0b-6
- Correct the files section for the icons

*Fri Jun 06 2008 Pingou <pingoufc4@yahoo.fr> 0.5.0b-5
- Correct version

*Fri Jun 06 2008 Pingou <pingoufc4@yahoo.fr> 0.5.0b-4
- Correct typo in changelog

*Fri Jun 06 2008 Pingou <pingoufc4@yahoo.fr> 0.5.0b-3
- Rebuild

*Thu May 01 2008 Pingou <pingoufc4@yahoo.fr> 0.5.0b-2
- Update to release 0.5.0b

*Tue Apr 15 2008 Pingou <pingoufc4@yahoo.fr> 0.5.0b-pre1-1
- Update to release 0.5.0b-pre1

* Wed Apr 02 2008 Rex Dieter <rdieter@fedoraproject.org> 0.5.0a-4
- BR: kdelibs4-devel
- d-f-i: fix double vendor

*Mon Feb 25 2008 Pingou <pingoufc4@yahoo.fr> 0.5.0a-3
- Change kde-config to kde4-config to fix the build

*Mon Feb 25 2008 Pingou <pingoufc4@yahoo.fr> 0.5.0a-2
- Change a BR to fix to build

*Mon Feb 25 2008 Pingou <pingoufc4@yahoo.fr> 0.5.0a-1
- Update to 0.5.0a for KDE4

*Sun Feb 10 2008 Pingou <pingoufc4@yahoo.fr> 0.4.9-3
- Change the Requires

*Tue Jan 15 2008 Pingou <pingoufc4@yahoo.fr> 0.4.9-2
- Change on the BR to fix rawhide build

*Tue Jan 15 2008 Pingou <pingoufc4@yahoo.fr> 0.4.9-1
- Update to 0.4.9

*Sun Jan 06 2008 Pingou <pingoufc4@yahoo.fr> 0.4.9pre1-1
- Update to 0.4.9pre1

*Tue Dec 11 2007 Pingou <pingoufc4@yahoo.fr> 0.4.8a-4
- Add qt-devel to the BR

*Tue Dec 11 2007 Pingou <pingoufc4@yahoo.fr> 0.4.8a-3
- Set the default environment for Qt

*Tue Dec 11 2007 Pingou <pingoufc4@yahoo.fr> 0.4.8a-2
- Changes on the BR

*Mon Oct 22 2007 Pingou <pingoufc4@yahoo.fr> 0.4.8a-1
- Update to 0.4.8a

*Mon Oct 22 2007 Pingou <pingoufc4@yahoo.fr> 0.4.8-2
- Problem in CVS

*Mon Oct 22 2007 Pingou <pingoufc4@yahoo.fr> 0.4.8-1
- Update to 0.4.8 and R 2.6

*Tue Aug 07 2007 Pingou <pingoufc4@yahoo.fr> 0.4.7-3
-Remove the diff (was my mistakes)

*Tue Aug 07 2007 Pingou <pingoufc4@yahoo.fr> 0.4.7-3
-Add the %%post and %%postun section

*Tue Jul 03 2007 Pingou <pingoufc4@yahoo.fr> 0.4.7-2
-Correction on the build
-correction in the consistensy on the variables

*Thu Jun 14 2007 Pingou <pingoufc4@yahoo.fr> 0.4.7-1
-First build for Fedora

