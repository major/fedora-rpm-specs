%global __requires_exclude .*BugzillaClient.*

Name:           vym
Version:        2.9.26
Release:        4%{?dist}
Summary:        View your mind

License:        GPL-2.0-or-later
URL:            https://github.com/insilmaril/vym/
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Source1:        %{name}.desktop
Source2:        vym.xml
Source3:	vym-logo-new-16.png
Source4:	vym-logo-new-22.png
Source5:	vym-logo-new-24.png
Source6:	vym-logo-new-32.png
Source7:	vym-logo-new-48.png
Source8:	vym-logo-new-256.png

BuildRequires:  make cmake
BuildRequires:  qt5-qtbase-devel qt5-qtsvg-devel libXext-devel desktop-file-utils
BuildRequires:  qt5-qtscript-devel qt5-linguist

%{?filter_setup:
%filter_from_requires /^perl(BugzillaClient)$/d
%?perl_default_filter
}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(BugzillaClient\\)
Requires:	perl-BZ-Client
# For file operations, we use command-line utilities.
Requires: coreutils zip unzip

%description
VYM (View Your Mind) is a tool to generate and manipulate maps
which show your thoughts. Such maps can help you to improve
your creativity and effectivity. You can use them for time management,
to organize tasks, to get an overview over complex contexts.

%prep
%setup -q

%build

%global docval %{_docdir}

%cmake -DCMAKE_INSTALL_DATAROOTDIR:PATH=share/vym
%cmake_build


%install
mkdir -p %{buildroot}%{_datadir}/vym
%cmake_install

%{__mkdir} -p %{buildroot}%{_datadir}/applications/

desktop-file-install             \
    --dir %{buildroot}%{_datadir}/applications \
    %{SOURCE1}

%{__mkdir} -p %{buildroot}%{_datadir}/icons/hicolor/16x16/apps
%{__cp} -p %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{__cp} -p icons/%{name}.xpm %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.xpm

%{__mkdir} -p %{buildroot}%{_datadir}/icons/hicolor/22x22/apps
%{__cp} -p %{SOURCE4} %{buildroot}%{_datadir}/icons/hicolor/22x22/apps/%{name}.png

%{__mkdir} -p %{buildroot}%{_datadir}/icons/hicolor/24x24/apps
%{__cp} -p %{SOURCE5} %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/%{name}.png

%{__mkdir} -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
%{__cp} -p %{SOURCE6} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

%{__mkdir} -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
%{__cp} -p %{SOURCE7} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{__cp} -p icons/%{name}-editor.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}-editor.png

%{__mkdir} -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
%{__cp} -p %{SOURCE8} %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png


install -m a+rx,u+w -d %{buildroot}%{_datadir}/mime/packages
install -p -m a+r,u+w %{SOURCE2} %{buildroot}%{_datadir}/mime/packages/vym.xml


%files
%license LICENSE.txt
%doc README.md demos/* doc/*
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/16x16/apps/%{name}*
%{_datadir}/icons/hicolor/22x22/apps/%{name}*
%{_datadir}/icons/hicolor/24x24/apps/%{name}*
%{_datadir}/icons/hicolor/32x32/apps/%{name}*
%{_datadir}/icons/hicolor/48x48/apps/%{name}*
%{_datadir}/icons/hicolor/256x256/apps/%{name}*
%{_datadir}/mime/packages/vym.xml


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 27 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.9.26-1
- 2.9.26

* Tue Sep 05 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.9.22-1
- 2.9.22

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 24 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.9.0-1
- 2.9.0

* Fri Mar 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.8.8-6
- migrated to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 21 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.8.8-1
- 2.8.8

* Thu Apr 22 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.8.0-2
- Fix data installation.

* Tue Apr 20 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.8.0-1
- 2.8.0

* Mon Mar 01 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.7.562-1
- 2.7.562

* Tue Feb 09 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.7.557-1
- 2.7.557

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.7.1-1
- 2.7.1

* Mon Apr 15 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.7.0-1
- 2.7.0.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 15 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.6.11-1
- 2.6.11

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.6.8-2
- Rebuild due to bug in RPM (RHBZ #1468476)

* Mon Mar 20 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.6.8-1
- Latest upstream, BZ 1433812.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 03 2017 Jon Ciesla <limburgher@gmail.com> - 2.6.5-1
- Latest upstream, BZ 1409680.

* Fri Dec 30 2016 Jon Ciesla <limburgher@gmail.com> - 2.6.3-1
- Latest upstream, BZ 1409171.

* Thu Oct 27 2016 Jon Ciesla <limburgher@gmail.com> - 2.6.2-1
- Latest upstream.

* Thu Sep 15 2016 Jon Ciesla <limburgher@gmail.com> - 2.6.0-1
- Latest upstream.

* Wed Aug 17 2016 Jon Ciesla <limburgher@gmail.com> - 2.5.21-1
- Latest upstream.

* Mon Jul 25 2016 Jon Ciesla <limburgher@gmail.com> - 2.5.19-1
- Latest upstream, BZ 1359465.

* Tue Feb 23 2016 Jon Ciesla <limburgher@gmail.com> - 2.5.4-1
- Latest upstream, BZ 1310923.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> 2.5.0-2
- use %%qmake_qt5 macro to ensure proper build flags

* Wed Oct 28 2015 Jon Ciesla <limburgher@gmail.com> - 2.5.0-1
- Latest upstream, BZ 1276025.

* Thu Aug 27 2015 Jon Ciesla <limburgher@gmail.com> - 2.4.8-1
- Latest upstream, BZ 1256983.

* Mon Aug 24 2015 Jon Ciesla <limburgher@gmail.com> - 2.4.7-1
- Latest upstream, BZ 1256210.

* Sat Jul 25 2015 Jon Ciesla <limburgher@gmail.com> - 2.4.5-1
- Latest upstream, BZ 1232794.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Jon Ciesla <limburgher@gmail.com> - 2.4.3-1
- Latest upstream, BZ 1222307.

* Tue May 12 2015 Jon Ciesla <limburgher@gmail.com> - 2.4.2-1
- Latest upstream, BZ 1218466.

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.4.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Mon Nov 03 2014 Jon Ciesla <limburgher@gmail.com> - 2.4.0-1
- Latest upstream, BZ 1159546.

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 2.3.24-3
- update desktop/icon/mime scriptlets

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 29 2014 Jon Ciesla <limburgher@gmail.com> - 2.3.24-1
- Latest upstream, BZ 1124296.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 13 2014 Jon Ciesla <limburgher@gmail.com> - 2.3.22-1
- Latest upstream, BZ 1064809.

* Mon Sep 16 2013 Jon Ciesla <limburgher@gmail.com> - 2.3.20-1
- Latest upstream, BZ 1008440.

* Fri Aug 09 2013 Jon Ciesla <limburgher@gmail.com> - 2.3.19-4
- Fix docdir, BZ 993892.

* Mon Aug 05 2013 Jon Ciesla <limburgher@gmail.com> - 2.3.19-3
- Fix FTBFS.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Jon Ciesla <limburgher@gmail.com> - 2.3.19-1
- Latest upstream, BZ 985369.

* Fri Jun 07 2013 Jon Ciesla <limburgher@gmail.com> - 2.3.18-1
- Latest upstream, BZ 971759.

* Tue Apr 09 2013 Jon Ciesla <limburgher@gmail.com> - 2.3.17-1
- Latest upstream, BZ 949893.

* Tue Mar 12 2013 Jon Ciesla <limburgher@gmail.com> - 2.3.15-1
- Latest upstream, BZ 919585.

* Mon Mar 04 2013 Jon Ciesla <limburgher@gmail.com> - 2.3.14-1
- Latest upstream, BZ 915251.

* Sat Feb 09 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 2.3.11-2
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines

* Thu Jan 03 2013 Jon Ciesla <limburgher@gmail.com> - 2.3.11-1
- Latest upstream, BZ 890428.

* Tue Dec 04 2012 Jon Ciesla <limburgher@gmail.com> - 2.3.8-1
- Latest upstream, BZ 883291.

* Mon Nov 12 2012 Jon Ciesla <limburgher@gmail.com> - 2.3.5-1
- Latest upstream, BZ 875835.

* Wed Oct 31 2012 Jon Ciesla <limburgher@gmail.com> - 2.3.3-1
- Latest upstream, BZ 871891.

* Thu Sep 13 2012 Jon Ciesla <limburgher@gmail.com> - 2.3.1-1
- Latest upstream, BZ 856823.

* Mon Jul 23 2012 Jon Ciesla <limburgher@gmail.com> - 2.3.0-1
- Latest upstream, BZ 839920.

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 05 2012 Jon Ciesla <limburgher@gmail.com> - 2.2.4-1
- Latest upstream, BZ 837759.

* Mon Jul 02 2012 Jon Ciesla <limburgher@gmail.com> - 2.2.2-1
- Latest upstream, BZ 836717.

* Wed Jun 13 2012 Jon Ciesla <limburgher@gmail.com> - 2.2.0-1
- Latest upstream, BZ 831552.

* Tue Apr 24 2012 Jon Ciesla <limburgher@gmail.com> - 2.1.11-1
- Latest upstream, BZ 814928.

* Wed Apr 18 2012 Jon Ciesla <limburgher@gmail.com> - 2.1.8-1
- Latest upstream, BZ 813745.

* Mon Apr 16 2012 Jon Ciesla <limburgher@gmail.com> - 2.1.7-1
- Latest upstream, BZ 812523.

* Tue Apr 10 2012 Jon Ciesla <limburgher@gmail.com> - 2.0.12-1
- Latest upstream, BZ 811194.

* Wed Apr 04 2012 Jon Ciesla <limburgher@gmail.com> - 2.0.10-2
- Use icons with transparent background.
- See https://fedorahosted.org/design-team/ticket/165

* Fri Mar 30 2012 Jon Ciesla <limburgher@gmail.com> - 2.0.10-1
- New upstream.
- gcc patch upstreamed.

* Wed Mar 07 2012 Jon Ciesla <limburgher@gmail.com> - 2.0.6-2
- Require needed utilities, BZ 799006.

* Thu Jan 05 2012 Jon Ciesla <limburgher@gmail.com> - 2.0.6-1
- New upstream.
- Patch for gcc 4.7.0.

* Tue Nov 22 2011 Jon Ciesla <limb@jcomserv.net> - 2.0.4-1
- New upstream.

* Mon Nov 14 2011 Jon Ciesla <limb@jcomserv.net> - 2.0.3-1
- New upstream.

* Fri Oct 28 2011 Jon Ciesla <limb@jcomserv.net> - 2.0.2-1
- New upstream.

* Mon Oct 17 2011 Jon Ciesla <limb@jcomserv.net> - 2.0.1-1
- New upstream.

* Fri Oct 07 2011 Jon Ciesla <limb@jcomserv.net> - 1.99.1-1
- New upstream.

* Mon Aug 29 2011 Jon Ciesla <limb@jcomserv.net> - 1.13.41-1
- New upstream.

* Thu Aug 18 2011 Jon Ciesla <limb@jcomserv.net> - 1.13.39-2
- Requires exclusion correction.

* Wed Aug 17 2011 Jon Ciesla <limb@jcomserv.net> - 1.13.39-1
- New upstream.

* Wed Jul 20 2011 Jon Ciesla <limb@jcomserv.net> - 1.13.36-1
- New upstream.

* Thu Jul 07 2011 Jon Ciesla <limb@jcomserv.net> - 1.13.35-1
- New upstream.

* Fri Jun 17 2011 Jon Ciesla <limb@jcomserv.net> - 1.13.32-2
- Bump and rebuild for BZ 712251.

* Wed Jun 08 2011 Jon Ciesla <limb@jcomserv.net> - 1.13.32-1
- New upstream.

* Tue May 24 2011 Jon Ciesla <limb@jcomserv.net> - 1.13.30-1
- New upstream.

* Thu May 19 2011 Jon Ciesla <limb@jcomserv.net> - 1.13.29-2
- Fix requires.

* Mon May 16 2011 Jon Ciesla <limb@jcomserv.net> - 1.13.29-1
- New upstream.

* Wed May 11 2011 Jon Ciesla <limb@jcomserv.net> - 1.13.27-1
- New upstream.

* Sat Nov 06 2010 Jon Ciesla <limb@jcomserv.net> - 1.13.12-1
- New upstream.

* Sat Nov 06 2010 Jon Ciesla <limb@jcomserv.net> - 1.12.8-1
- New upstream.

* Fri Mar 19 2010 Jon Ciesla <limb@jcomserv.net> - 1.12.7-1
- Updated to new upstream version, BZ 543442.

* Wed Dec 02 2009 Jon Ciesla <limb@jcomserv.net> - 1.12.6-1
- Updated to new upstream version, BZ 543442.

* Mon Nov 23 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.12.5-2 
- rebuild (for qt-4.6.0-rc1, f13+)

* Mon Nov 16 2009 Jon Ciesla <limb@jcomserv.net> - 1.12.5-1
- Updated to new upstream version, BZ 537799.

* Tue Aug 04 2009 Jon Ciesla <limb@jcomserv.net> - 1.12.4-0
- Updated to new upstream version.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 05 2008 Jon Ciesla <limb@jcomserv.net> - 1.12.2-1
- Updated to new upstream version.

* Mon Jul 14 2008 Jon Ciesla <limb@jcomserv.net> - 1.12.0-1
- Updated to new upstream version.
- Dropped all patches, applied upstream.

* Tue Jun 10 2008 Jon Ciesla <limb@jcomserv.net> - 1.10.0-4
- Added mime type xml, BZ434929.

* Fri Feb 08 2008 Jon Ciesla <limb@jcomserv.net> - 1.10.0-3
- GCC 4.3 rebuild.

* Wed Jan 09 2008 Jon Ciesla <limb@jcomserv.net> - 1.10.0-2
- Added typeinfo patches.

* Thu Oct 18 2007 Jon Ciesla <limb@jcomserv.net> - 1.10.0-1
- Upgrade to 1.10.0.
- Applied several patches from Till Maas, which he sent upstream.
- Dropped findlang, as it doesn't work with Vym.

* Thu Aug 16 2007 Jon Ciesla <limb@jcomserv.net> - 1.8.1-9
- License tag correction.

* Wed Mar 21 2007 Jon Ciesla <limb@jcomserv.net> - 1.8.1-8
- Converted patches to unified output format.

* Wed Mar 21 2007 Jon Ciesla <limb@jcomserv.net> - 1.8.1-7
- Dropped symlink in favor of path patches.

* Wed Mar 21 2007 Jon Ciesla <limb@jcomserv.net> - 1.8.1-6
- Fixed Source URL.

* Tue Mar 20 2007 Jon Ciesla <limb@jcomserv.net> - 1.8.1-5
- doc link fix, icon fix.

* Mon Mar 19 2007 Jon Ciesla <limb@jcomserv.net> - 1.8.1-4
- Fixed Desktop icon path, make copy timestamps, cleaned scripts.
- Added symlink to fix PDF location.

* Tue Mar 13 2007 Jon Ciesla <limb@jcomserv.net> - 1.8.1-3
- Fixed source url.
- added desktop-file-utils,kdelibs BRs.
- Fixed desktop file handling.

* Tue Mar 13 2007 Jon Ciesla <limb@jcomserv.net> - 1.8.1-2
- Submitting for review.

* Wed Nov 22 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org > - 1.8.1-1
- Initial Package.
