Name:           homebank
Version:        5.5.6
Release:        2%{?dist}
Summary:        Free easy personal accounting for all  

License:        GPLv2+
URL:            http://homebank.free.fr
Source0:        http://homebank.free.fr/public/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  atk-devel cairo-devel desktop-file-utils gettext gtk3-devel
BuildRequires:  intltool libappstream-glib libofx-devel perl(XML::Parser)
BuildRequires:  libsoup-devel
BuildRequires: make

%description
HomeBank is the free software you have always wanted to manage your personal
accounts at home. The main concept is to be light, simple and very easy to use.
It brings you many features that allows you to analyze your finances in a
detailed way instantly and dynamically with powerful report tools based on
filtering and graphical charts.

%package doc
Summary: Documentation files for homebank
BuildArch: noarch
Requires: %{name} = %{version}-%{release}
%description doc
Documentation files for homebank


%prep
%autosetup
chmod -x NEWS
chmod -x ChangeLog
chmod -x README
chmod -x AUTHORS
chmod -x COPYING
chmod -x doc/TODO
chmod -x src/*.*

%build
%configure
%make_build

%install
make install DESTDIR=%{buildroot} INSTALL='install -p'
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install                                    \
        --delete-original                               \
        --dir %{buildroot}%{_datadir}/applications   \
        --mode 0644                                     \
        %{buildroot}%{_datadir}/applications/%{name}.desktop
%find_lang %{name}
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml

%ldconfig_scriptlets

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README
%license COPYING
%{_bindir}/%{name}
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/images
%{_datadir}/%{name}/icons
%{_datadir}/%{name}/datas
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/mime-info/%{name}.*
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/application-registry/%{name}.applications
%{_datadir}/appdata/%{name}.appdata.xml

%files doc
%doc doc/TODO
%{_datadir}/%{name}/help

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 5.5.6-1
- Update to 5.5.6 (fixes rhbz#2101905)

* Mon Apr 18 2022 Filipe Rosset <rosset.filipe@gmail.com> - 5.5.5-1
- Update to 5.5.5 fixes rhbz#2076316

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 11 2022 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 5.5.4-1
- Update to 5.5.4 (Fixes rhbz#1991241)

* Wed Aug 11 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 5.5.3-1
- Update to 5.5.3

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 08 2021 Filipe Rosset <rosset.filipe@gmail.com> - 5.5.2-1
- Update to 5.5.2 fixes rhbz#1958531

* Mon May 03 2021 Filipe Rosset <rosset.filipe@gmail.com> - 5.5.1-1
- Update to 5.5.1 fixes rhbz#1936313

* Sat Feb 06 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 5.5-1
- Update to 5.5

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 05 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 5.4.3-1
- Update to 5.4.3

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 16 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 5.4.2-1
- Update to 5.4.2

* Thu Apr 23 2020 Filipe Rosset <rosset.filipe@gmail.com> - 5.4.1-1
- Update to 5.4.1 fixes rhbz#1822395

* Mon Feb 10 2020 Filipe Rosset <rosset.filipe@gmail.com> - 5.3.2-1
- Update to 5.3.2 fixes rhbz#1801002

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 12 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 5.3.1-1
- Update to 5.3.1

* Tue Jan 07 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 5.3-1
- Update to 5.3

* Thu Sep 19 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 5.2.8-1
- Update to 5.2.8

* Sun Jul 28 2019 Filipe Rosset <rosset.filipe@gmail.com> - 5.2.7-1
- Update to 5.2.7

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 25 2019 Filipe Rosset <rosset.filipe@gmail.com> - 5.2.6-1
- Update to 5.2.6 fixes rhbz #1711554 and rhbz #1713860

* Sun May 12 2019 Filipe Rosset <rosset.filipe@gmail.com> - 5.2.5-1
- Update to 5.2.5 fixes rhbz #1709028

* Thu Apr 11 2019 Filipe Rosset <rosset.filipe@gmail.com> - 5.2.4-1
- Update to 5.2.4 fixes rhbz #1698572

* Tue Mar 19 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 5.2.3-1
- Update to 5.2.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 09 2018 Filipe Rosset <rosset.filipe@gmail.com> - 5.2.2-1
- Update to new upstream version 5.2.2
- Complete changelog here http://homebank.free.fr/ChangeLog

* Sat Sep 15 2018 Filipe Rosset <rosset.filipe@gmail.com> - 5.2.1-1
- Update to new upstream version 5.2.1

* Sun Sep 09 2018 Filipe Rosset <rosset.filipe@gmail.com> - 5.2-1
- Update to new upstream version 5.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 09 2018 Filipe Rosset <rosset.filipe@gmail.com> - 5.1.8-4
- forget scriptlets entry

* Mon Apr 09 2018 Filipe Rosset <rosset.filipe@gmail.com> - 5.1.8-3
- added gcc as BR
- modernize specfile

* Mon Apr 02 2018 Bill Nottingham <notting@splat.cc> - 5.1.8-2
- Rebuild for libofx soname change

* Sun Mar 18 2018 Filipe Rosset <rosset.filipe@gmail.com> - 5.1.8-1
- New upstream version 5.1.8, fixes rhbz #1557699

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 06 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 5.1.7-1
- Update to 5.1.7

* Thu Sep 14 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 5.1.6-2
- Move -doc to noarch

* Thu Sep 14 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 5.1.6-1
- Update to 5.1.6

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 09 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 5.1.5-1
- Update to 5.1.5

* Tue Feb 14 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 5.1.4-1
- Update to 5.1.4

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 22 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 5.1.3-1
- Update to 5.1.3

* Mon Dec 12 2016 Filipe Rosset <rosset.filipe@gmail.com> - 5.1.2-2
- rebuilt

* Wed Dec 07 2016 Filipe Rosset <rosset.filipe@gmail.com> - 5.1.2-1
- Rebuilt for new upstream version 5.1.2

* Mon Nov 07 2016 Filipe Rosset <rosset.filipe@gmail.com> - 5.1.1-1
- Rebuilt for new upstream version 5.1.1

* Wed Nov 02 2016 Filipe Rosset <rosset.filipe@gmail.com> - 5.1-1
- Rebuilt for new upstream version 5.1, fixes rhbz #1383215 #1385629
- Added libsoup-devel as new BR
- More details at http://homebank.free.fr/ChangeLog

* Mon Sep 12 2016 Filipe Rosset <rosset.filipe@gmail.com> - 5.0.9-1
- Rebuilt for new upstream version 5.0.9, fixes rhbz #1359436

* Sat May 21 2016 Filipe Rosset <rosset.filipe@gmail.com> - 5.0.8-1
- Rebuilt for new upstream version 5.0.8, fixes rhbz #1338404 #1336248

* Wed May 11 2016 Filipe Rosset <rosset.filipe@gmail.com> - 5.0.7-1
- Rebuilt for new upstream version 5.0.7, fixes rhbz #1312448 #1334339

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 01 2015 Filipe Rosset <rosset.filipe@gmail.com> - 5.0.6-1
- Rebuilt for new upstream version 5.0.6, fixes rhbz #1274937 #1276919

* Mon Sep 21 2015 Filipe Rosset <rosset.filipe@gmail.com> - 5.0.5-1
- Rebuilt for new upstream version 5.0.5, fixes rhbz #1264884

* Mon Sep 14 2015 Filipe Rosset <rosset.filipe@gmail.com> - 5.0.4-1
- Rebuilt for new upstream version 5.0.4, fixes rhbz #1262506

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Filipe Rosset <rosset.filipe@gmail.com> - 5.0.3-1
- Rebuilt for new upstream version 5.0.3, fixes rhbz #1228899

* Thu May 07 2015 Filipe Rosset <rosset.filipe@gmail.com> - 5.0.2-1
- Rebuilt for new upstream version 5.0.2, fixes rhbz #1219031

* Mon Apr 06 2015 Filipe Rosset <rosset.filipe@gmail.com> - 5.0.1-1
- Rebuilt for new upstream version 5.0.1, fixes rhbz #1209142, fix AppData packaging issues

* Sat Feb 21 2015 Filipe Rosset <rosset.filipe@gmail.com> - 5.0.0-1
- Rebuilt for new upstream version 5.0.0, fixes rhbz #1190745

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 4.6.3-3
- update icon/mime scriptlets

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 09 2014 Filipe Rosset <rosset.filipe@gmail.com> - 4.6.3-1
- Rebuilt for new upstream version 4.6.3, list of fixed bugs http://homebank.free.fr/ChangeLog

* Sun Jul 27 2014 Filipe Rosset <rosset.filipe@gmail.com> - 4.6.2-1
- Rebuilt for new upstream version 4.6.2, list of fixed bugs http://homebank.free.fr/ChangeLog

* Thu Jun 26 2014 Filipe Rosset <rosset.filipe@gmail.com> - 4.6.1-1
- Rebuilt for new upstream version 4.6.1

* Mon Jun 23 2014 Filipe Rosset <rosset.filipe@gmail.com> - 4.6-1
- Rebuilt for new upstream version 4.6, spec cleanup

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 03 2014 Filipe Rosset <rosset.filipe@gmail.com> - 4.5.6-1
- New upstream version 4.5.6, fix rhbz #1071915 and spec cleanup

* Wed Feb 19 2014 Filipe Rosset <rosset.filipe@gmail.com> - 4.5.5-1
- New upstream version 4.5.5

* Thu Nov 14 2013 Filipe Rosset <rosset.filipe@gmail.com> - 4.5.4-1
- New upstream version 4.5.4
- Fixes bz #1009081 and bz #1014951

* Mon Sep 23 2013 Bill Nottingham <notting@redhat.com> - 4.5-3
- Rebuild against new libofx

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 06 2013 Filipe Rosset <rosset.filipe@gmail.com> - 4.5-1
- Upgraded to upstream version 4.5

* Wed Apr 24 2013 Jon Ciesla <limburgher@gmail.com> - 4.4-7
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Bill Nottingham <notting@redhat.com> - 4.4-4
- rebuild for libofx ABI bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 4.4-2
- Rebuild for new libpng

* Sun May 01 2011 Filipe Rosset <rosset.filipe@gmail.com> - 4.4-1
- Upgraded to upstream version 4.4
- This build include the fix for https://bugs.launchpad.net/homebank/+bug/695790

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 31 2010 Filipe Rosset <rosset.filipe@gmail.com> - 4.3-2
- Enabled deprecated gtk to build on Fedora 15 Rawhide
- Opened bug report upstream https://bugs.launchpad.net/homebank/+bug/695790

* Thu Jul 15 2010 Johan Cwiklinski <johan AT x-tnd DOT be> - 4.3-1
- 4.3

* Sat Mar 06 2010 Johan Cwiklinski <johan AT x-tnd DOT be> - 4.2.1-1
- 4.2.1
- Remove dso link patch (fixed upstream)

* Fri Feb 12 2010 Johan Cwiklinski <johan AT x-tnd DOT be> - 4.2-2
- Fix DSO link bug

* Thu Feb 11 2010 Johan Cwiklinski <johan AT x-tnd DOT be> - 4.2-1
- 4.2

* Fri Jan 01 2010 Johan Cwiklinski <johan AT x-tnd DOT be> - 4.1-1
- 4.1
