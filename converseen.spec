Name:		converseen
Version:	0.9.9.8
Release:	1%{?dist}
Summary:	A batch image conversion tool written in C++ with Qt5 and Magick++

License:	GPLv3
URL:		http://converseen.sf.net/
Source0:	http://downloads.sourceforge.net/converseen/%{name}-%{version}.tar.bz2

BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	ImageMagick-devel
BuildRequires:	ImageMagick-c++-devel
BuildRequires:	qt5-qtbase-devel
BuildRequires:	qt5-linguist
  

%description
Converseen is a batch image conversion tool and resizer written in C++ with Qt5
and Magick++.  Converseen allows you to convert images in more than 100
different formats!


%prep
%autosetup


%build
%cmake
%cmake_build


%install
%cmake_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/net.fasterland.%{name}.desktop


%files
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/applications/net.fasterland.%{name}.desktop
%{_datadir}/converseen
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/kservices5/ServiceMenus/%{name}_import.desktop


%changelog
* Thu Sep 15 2022 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.9.8-1
- Update to 0.9.9.8 fixes rhbz#2126958

* Wed Aug 24 2022 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.9.7-1
- Update to 0.9.9.7 fixes rhbz#2121168

* Fri Aug 19 2022 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.9.6-1
- Update to 0.9.9.6 fixes rhbz#2103519

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 21 2022 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.9.5-1
- Update to 0.9.9.5 fixes rhbz#2031546

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Oct 17 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.9.2-2
- Rebuild against new ImageMagick

* Wed Oct 06 2021 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.9.2-1
- Update to 0.9.9.2 fixes rhbz#1979067

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Feb 16 2021 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.9.0-1
- Update to 0.9.9.0 fixes rhbz#1929002

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 17 2020 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.8.1-4
- Fix recent cmake macro change on F-33 rhbz#1863362

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb 16 2020 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.8.1-1
- Update to 0.9.8.1 fixes rhbz#1797385

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.8.0-1
- Update to 0.9.8.0 fixes rhbz#1768272

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 27 2018 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.7.2-1
- Rebuilt for new upstream version 0.9.7.2

* Mon Sep 10 2018 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.7-1
- Rebuilt for new upstream version 0.9.7, fixes RHBZ#1613080

* Tue Aug 28 2018 Michael Cronenworth <mike@cchtml.com> - 0.9.6.2-10
- Rebuild for new ImageMagick 6.9.10

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 27 2017 Michael Cronenworth <mike@cchtml.com> - 0.9.6.2-7
- Rebuild for new ImageMagick

* Tue Sep 05 2017 Adam Williamson <awilliam@redhat.com> - 0.9.6.2-6
- Rebuild for new-old ImageMagick (reversion to 6 from 7)

* Fri Aug 25 2017 Michael Cronenworth <mike@cchtml.com> - 0.9.6.2-5
- Rebuild for new ImageMagick

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Kevin Fenzi <kevin@scrye.com> - 0.9.6.2-3
- Rebuild for new ImageMagick

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr 14 2017 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.6.2-1
- Rebuilt for new upstream version 0.9.6.2, fixes RHBZ#1436884

* Mon Feb 27 2017 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.6.1-1
- Rebuilt for new upstream version 0.9.6.1, fixes RHBZ#1417782

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 18 2017 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.6-1
- Rebuilt for new upstream version 0.9.6, fixes RHBZ#1414398

* Thu Nov 03 2016 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.5.2-1
- Rebuilt for new upstream version 0.9.5.2, fixes rhbz #1380208 #1380164

* Wed Sep 14 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.9.5.1-2
- do not depend on virtual package qt5-devel
- fix directory ownership (%%_datadir/converseen was unowned)

* Wed Sep 14 2016 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.5.1-1
- Rebuilt for new upstream version 0.9.5.1, fixes rhbz #1371339

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.2-2
- Rebuilt for GCC 5 C++11 ABI change

* Mon Mar 23 2015 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.2-1
- Rebuilt for new upstream version 0.9.2, fixes rhbz #1204537

* Mon Mar 09 2015 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.1-1
- Rebuilt for new upstream version 0.9.1, fixes rhbz #1199061, #1197790

* Wed Feb 18 2015 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.0-1
- Rebuilt for new upstream version 0.9.0, fixes rhbz #1170952

* Thu Oct 02 2014 Filipe Rosset <rosset.filipe@gmail.com> - 0.8.4-1
- Rebuilt for new upstream version 0.8.4, fixes rhbz #1148306

* Sun Aug 31 2014 Filipe Rosset <rosset.filipe@gmail.com> - 0.8.3-1
- Rebuilt for new upstream version 0.8.3, fixes rhbz #1134743

* Wed Aug 27 2014 Filipe Rosset <rosset.filipe@gmail.com> - 0.8.2-1
- Rebuilt for new upstream version 0.8.2, fixes rhbz #1103120

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 Richard Hughes <richard@hughsie.com> - 0.7.2-1
- Rebuilt for new upstream version 0.7.2

* Thu May 22 2014 Filipe Rosset <rosset.filipe@gmail.com> - 0.7.1.1-1
- Rebuilt for new upstream version 0.7.1.1 + spec cleanup, fixes rhbz #970061

* Wed Apr 02 2014 Adam Williamson <awilliam@redhat.com> - 0.6.6.1-2
- rebuild for new ImageMagick

* Sun Nov 24 2013 Mario Santagiuliana <fedora@marionline.it> 0.6.6.1-1
- Version 0.6.6.1

* Sun Nov 24 2013 Mario Santagiuliana <fedora@marionline.it> 0.6.6-1
- Version 0.6.6

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 01 2013 Mario Santagiuliana <fedora@marionline.it> 0.6.2-1
- Version 0.6.2

* Sun Apr 21 2013 Mario Santagiuliana <fedora@marionline.it> 0.6
- Version 0.6

* Sat Feb 16 2013 Mario Santagiuliana <fedora@marionline.it> 0.5.3-1
- Version 0.5.3
- Fix rpmlint warnings

* Thu Jan 10 2013 Mario Santagiuliana <fedora@marionline.it> 0.5.2.1-1
- Update to new version 0.5.2.1
- Fix little issue on changelog

* Mon Jan 07 2013 Mario Santagiuliana <fedora@marionline.it> 0.5.2-1
- Update to new version 0.5.2

* Fri Jul 06 2012 Mario Santagiuliana <fedora@marionline.it> 0.5.1-1
- Update to new version 0.5.1

* Thu Mar 22 2012 Mario Santagiuliana <fedora@marionline.it> 0.4.9-4
- Again, new rebuild for fc17
- fix changelog error from Tue to Thu

* Sun Mar 11 2012 Mario Santagiuliana <fedora@marionline.it> 0.4.9-3
- New rebuild

* Mon Mar 05 2012 Mario Santagiuliana <fedora@marionline.it> 0.4.9-2
- New rebuild

* Tue Jan 31 2012 Mario Santagiuliana <fedora@marionline.it> 0.4.9-1
- Update to version 0.4.9

* Mon Jan 23 2012 Mario Santagiuliana <fedora@marionline.it> 0.4.8-4
- Fix %%cmake use

* Mon Jan 23 2012 Mario Santagiuliana <fedora@marionline.it> 0.4.8-3
- Use %%cmake macro instead of cmake

* Wed Jan 18 2012 Mario Santagiuliana <fedora@marionline.it> 0.4.8-2
- Use desktop-file-install
- Remove INSTALL file from doc macro

* Tue Jan 10 2012 Mario Santagiuliana <fedora@marionline.it> 0.4.8-1
- Update to new release 0.4.8

* Tue Jan 10 2012 Mario Santagiuliana <fedora@marionline.it> 0.4.7-29
- Update spec file to include package in Fedora repository

* Thu Dec 01 2011 Francesco Mondello <faster3ck@gmail.com>
- Version 0.4.7
- Optimized GUI for small screen resolutions (netbooks)
- Fixed overwriting with upper suffixes
- Now the window geometry is saved

* Mon Sep 12 2011 Francesco Mondello <faster3ck@gmail.com>
- Version 0.4.5
- Modified the code to work in Windows
- Added Turkish translation
- Added support for Cmake

* Tue Aug 02 2011 Francesco Mondello <faster3ck@gmail.com>
- Version 0.4.3
- Added service menu for Kde
- Fixed overwriting with upper suffixes
- Added Spanish (Chile) translation

* Sun Jun 26 2011 Francesco Mondello <faster3ck@gmail.com>
- Version 0.4.2
- Fixed overwriting dialog when the renaming option is enabled.

* Wed Mar 09 2011 Francesco Mondello <faster3ck@gmail.com>
- Version 0.4.1
- Improved picture previewer
- If the output folder doesn't exists it will be created

* Fri Feb 11 2011 Francesco Mondello <faster3ck@gmail.com>
- Version 0.4:
- Added thread support to image conversions.
- Added a progress bar into the conversion dialog.
- Added drag and drop.
- Improved management of PNG.
- Fixed various bugs and improved the code.
- Added Brazilian Portuguese translation.
- Added German translation.

* Sat Oct 23 2010 Francesco Mondello <faster3ck@gmail.com>
- Version 0.3.2: Added french translation

* Sun Sep 12 2010 Francesco Mondello <faster3ck@gmail.com>
- Initial rpm release to version 0.3.1
