Name:		worker
Version:	5.1.0
Release:	4%{?dist}
Summary:	File Manager for the X11

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://boomerangsworld.de/worker
Source0:	http://boomerangsworld.de/cms/%{name}/downloads/%{name}-%{version}.tar.bz2
Patch0:		Patch0-Fix-For-Python3.patch

BuildRequires:	desktop-file-utils
BuildRequires:	gcc-c++
BuildRequires:	libX11-devel
BuildRequires:	make

%description
A X11 file-manager that features low requirements and easy to access archives.

%prep
%autosetup -p0

#Fix Man pages(UTF-8)
for f in ChangeLog man/fr/worker.1 man/it/worker.1; do
	iconv -f ISO-8859-1 -t UTF-8 $f > $f.new && \
	touch -r $f $f.new && \
	mv $f.new $f
done

%build
%configure
%make_build

%install
%make_install

desktop-file-install	\
--delete-original	\
--dir=%{buildroot}%{_datadir}/applications	\
--remove-category="FileManager"		\
--add-category="System;FileTools"	\
%{buildroot}/%{_datadir}/applications/%{name}.desktop


%files
%doc AUTHORS ChangeLog THANKS
%license COPYING
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/WorkerIcon*.xpm
%{_datadir}/metainfo/de.boomerangsworld.worker.metainfo.xml
%{_mandir}/man1/%{name}.1*
%{_mandir}/*/man1/%{name}.1*
%{_datadir}/%{name}/
%{_datadir}/appdata/%{name}.appdata.xml
%{_bindir}/%{name}


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 5.1.0-3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 15 2024 Filipe Rosset <rosset.filipe@gmail.com> - 5.1.0-1
- Update to 5.1.0 fixes rhbz#2255649

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 05 2023 Filipe Rosset <rosset.filipe@gmail.com> - 4.12.1-1
- Update to 4.12.1 fixes rhbz#2175428

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Sep 19 2022 Filipe Rosset <rosset.filipe@gmail.com> - 4.11.0-1
- Update to 4.11.0 fixes rhbz#2127764

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Apr 28 2022 Filipe Rosset <rosset.filipe@gmail.com> - 4.10.1-1
- Update to 4.10.1 fixes rhbz#2079531

* Mon Mar 21 2022 Filipe Rosset <rosset.filipe@gmail.com> - 4.10.0-1
- Update to 4.10.0 fixes rhbz#2030068

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 07 2021 Filipe Rosset <rosset.filipe@gmail.com> - 4.9.0-1
- Update to 4.9.0 fixes rhbz#1998781

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 02 2021 Filipe Rosset <rosset.filipe@gmail.com> - 4.8.1-1
- Update to 4.8.1 fixes rhbz#1946316

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 4.7.0-2
- Rebuilt for removed libstdc++ symbol (#1937698)

* Wed Feb 03 2021 Filipe Rosset <rosset.filipe@gmail.com> - 4.7.0-1
- Update to 4.7.0 fixez rhbz#1924344

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Filipe Rosset <rosset.filipe@gmail.com> - 4.6.1-1
- Update to 4.6.1 fixes rhbz#1902431

* Tue Aug 25 2020 Filipe Rosset <rosset.filipe@gmail.com> - 4.5.1-1
- Update to 4.5.1 fixes rhbz#1868806

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Apr 12 2020 Filipe Rosset <rosset.filipe@gmail.com> - 4.4.0-1
- Update to 4.4.0 fixes rhbz#1823214

* Sun Feb 16 2020 Filipe Rosset <rosset.filipe@gmail.com> - 4.3.0-1
- Update to 4.3.0 fixes rhbz#1795070

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Filipe Rosset <rosset.filipe@gmail.com> - 4.2.0-1
- Update to 4.2.0 fixes rhbz#1786790

* Sat Sep 21 2019 Filipe Rosset <rosset.filipe@gmail.com> - 4.1.0-1
- Update to 4.1.0 fixes rhbz#1750969

* Mon Aug 05 2019 Filipe Rosset <rosset.filipe@gmail.com> - 4.0.1-1
- Update to 4.0.1

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 24 2019 Filipe Rosset <rosset.filipe@gmail.com> - 4.0.0-1
- Rebuilt for new upstream version 4.0.0 fixes rhbz #1723206

* Sun Apr 07 2019 Filipe Rosset <rosset.filipe@gmail.com> - 3.15.4-1
- Rebuilt for new upstream version 3.15.4 fixes rhbz #1670216 and #1676217

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 11 2018 Filipe Rosset <rosset.filipe@gmail.com> - 3.15.2-1
- Rebuilt for new upstream version 3.15.2 fixes rhbz #1579346 and #1606703

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 09 2018 Filipe Rosset <rosset.filipe@gmail.com> - 3.15.0-3
- added gcc as BR

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Filipe Rosset <rosset.filipe@gmail.com> - 3.15.0-1
- Rebuilt for new upstream version 3.15.0 fixes rhbz #1491078

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Filipe Rosset <rosset.filipe@gmail.com> - 3.11.0-1
- Rebuilt for new upstream version 3.11.0 fixes rhbz #1473062

* Tue Jun 13 2017 Filipe Rosset <rosset.filipe@gmail.com> - 3.10.0-2
- Rebuilt for new upstream version 3.10.0 fixes rhbz #1460412

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Apr 22 2017 Filipe Rosset <rosset.filipe@gmail.com> - 3.9.0-1
- Rebuilt for new upstream version 3.9.0 fixes rhbz #1091751
- Fixes FTBFS in rawhide rhbz #1424545 + spec clean up

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.3.3-4
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 23 2014 Nathan Owe <ndowens at fedoraproject.org 3.3.3-1
 - Updated package to latest available

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 08 2012 Nathan Owe <ndowens at fedoraproject.org> 2.19.2-1
- Updated version

* Sat Feb 25 2012 Nathan Owe <ndowens at fedoraproject.org> 2.19.1-1
- Updated version

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 04 2011 Nathan Owe <ndowens at fedoraproject.org> 2.18.1-1
- Updated to newest version

* Wed Aug 17 2011 Nathan Owe <ndowens at fedoraproject.org> 2.18.0-7
- Fixed defattr typo

* Tue Jul 26 2011 Nathan Owe <ndowens at fedoraproject.org> 2.18.0-6
- Changed email address
- Added 'BuildRoot' for EPEL compatability
- Added defattr and clean section for EPEL

* Tue Jul 19 2011 Nathan Owe <ndowens04 at yahoo.com> 2.18.0-5
- Convert Changelog to UTF-8

* Tue Jul 19 2011 Nathan Owe <ndowens04 at yahoo.com> 2.18.0-4
- Convert Man pages to UTF-8

* Mon Jul 18 2011 Nathan Owe <ndowens04 at yahoo.com> 2.18.0-3
- Fixed Directory Permission problem

* Mon Jul 18 2011 Nathan Owe <ndowens04 at yahoo.com> 2.18.0-2
- Removed Requires

* Sat Jul 16 2011 Nathan Owe <ndowens04 at yahoo.com> 2.18.0-1
- Inital Release
