%global debug_package %{nil}

Name:		unetbootin
Version:	702
Release:	10%{?dist}
Summary:	Create bootable Live USB drives for a variety of Linux distributions
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://unetbootin.github.io/
Source0:	https://sourceforge.net/projects/%{name}/files/UNetbootin/%{version}/%{name}-source-%{version}.tar.gz
Patch0:     unetbootin-675-desktop.patch
# Syslinux is only available on x86 architectures
ExclusiveArch:	%{ix86} x86_64

BuildRequires: make
BuildRequires:	gcc-c++
BuildRequires:	desktop-file-utils
BuildRequires:	qt5-linguist
BuildRequires:	qt5-qtbase-devel
# Not picked up automatically, required for operation
Requires:	p7zip-plugins
Requires:	syslinux
Requires:	syslinux-extlinux

%description
UNetbootin allows you to create bootable Live USB drives for a variety of
Linux distributions from Windows or Linux, without requiring you to burn a CD.
You can either let it download one of the many distributions supported
out-of-the-box for you, or supply your own Linux .iso file if you've already
downloaded one or your preferred distribution isn't on the list.


%prep
%setup -c
%patch -P0 -p1
# Fix desktop file
sed -i '/^RESOURCES/d' unetbootin.pro

%build
lupdate-qt5 unetbootin.pro
lrelease-qt5 unetbootin.pro
%{?qmake_qt5}%{!?qmake_qt5:qmake-qt5}}
%make_build


%install
install -D -p -m 755 unetbootin %{buildroot}%{_bindir}/unetbootin
# Install desktop file
desktop-file-install --vendor="" --remove-category=Application --dir=%{buildroot}%{_datadir}/applications unetbootin.desktop
# Install localization files
install -d %{buildroot}%{_datadir}/unetbootin
install -c -p -m 644 unetbootin_*.qm %{buildroot}%{_datadir}/unetbootin/
# Install pixmap
install -D -p -m 644 unetbootin_512.png %{buildroot}%{_datadir}/pixmaps/unetbootin.png


%files
%doc README.TXT
%{_bindir}/unetbootin
%{_datadir}/unetbootin/
%{_datadir}/applications/unetbootin.desktop
%{_datadir}/pixmaps/unetbootin.png

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 702-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 702-9
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 702-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 702-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 702-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 702-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 702-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 702-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 702-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb 05 2021 Filipe Rosset <rosset.filipe@gmail.com> - 702-1
- Update to 702 version fixes rhbz#1925265

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 700-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 30 2020 Filipe Rosset <rosset.filipe@gmail.com> - 700-1
- Update to 700 version fixes rhbz#1896098

* Mon Aug 24 2020 Filipe Rosset <rosset.filipe@gmail.com> - 681-1
- Update to 681 version fixes rhbz#1846251

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 677-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr 03 2020 Mohan Boddu <mboddu@bhujji.com> - 677-1
- Rebuilt for 677 version

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 657-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 657-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 657-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 657-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 09 2018 Filipe Rosset <rosset.filipe@gmail.com> - 657-3
- added gcc-c++ as BR

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 657-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Filipe Rosset <rosset.filipe@gmail.com> - 657-1
- Rebuilt for new upstream release 657, fixes rhbz #1508431

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 655-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 655-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Filipe Rosset <rosset.filipe@gmail.com> - 655-1
- Rebuilt for new upstream release 655, fixes rhbz #1471101

* Tue May 02 2017 Filipe Rosset <rosset.filipe@gmail.com> - 647-1
- Rebuilt for new upstream release 647, fixes rhbz #1444678

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 625-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 10 2016 Filipe Rosset <rosset.filipe@gmail.com> - 625-1
- clean up the spec, attempt to fix FTBFS rhbz #1308209

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 619-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> - 619-2
- use %%qmake_qt4 macro to ensure proper build flags

* Sun Nov 08 2015 Kalpa Welivitigoda - 619-1
- Update to 619.

* Sun Sep 13 2015 Kalpa Welivitigoda - 613-1
- Update to 613.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 608-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 608-4
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 608-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 608-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun 02 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 608-1
- Update to 608.

* Tue Apr 22 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 603-1
- Change naming to reflect upstream versioning scheme.
- Update to 603.

* Thu Aug 22 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 0-15.585bzr
- Update to 585.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-14.581bzr
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-13.581bzr
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Sep 17 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0-11.581bzr
- Update to 581.

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-12.577bzr
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 08 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0-11.577bzr
- Update to 577.

* Tue Jun 12 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0-11.575bzr
- Update to 575.

* Fri Apr 06 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0-11.568bzr
- Added missing syslinux-extlinux dependency (BZ #810411).
- Update to 568.

* Fri Feb 03 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0-11.565bzr
- Update to revision 565.
- Added icons (BZ #787202).

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-11.555bzr
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Oct 01 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0-10.555bzr
- Update to revision 555.

* Mon May 09 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0-10.549bzr
- Bump spec.

* Thu Apr 28 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0-9.549bzr
- Update to revision 549.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-9.494bzr
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Oct 15 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0-8.494bzr
- Update to revision 494. 

* Tue Jun 22 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0-8.485bzr
- Update to revision 485.

* Tue Jun 22 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0-8.471bzr
- Update to revision 471.

* Mon Mar 29 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0-8.419bzr
- Update to revision 419.

* Wed Feb 03 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0-8.393bzr
- Update to revision 393.

* Sun Dec 06 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0-7.377bzr
- Update to revision 377.

* Fri Oct 23 2009 Milos Jakubicek <xjakub@fi.muni.cz> 0-6.358bzr
- Fix FTBFS: bump release to be able to tag in new branch and sync source name

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-6.357bzr
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 16 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0-6.356bzr
- Add ExclusiveArch to prevent build on architectures lacking syslinux.

* Fri Jul 10 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0-5.356bzr
- Fix EPEL install.

* Fri Jul 10 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0-4.356bzr
- Fix EPEL build.

* Fri Jul 10 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0-3.356bzr
- Added localizations.

* Fri Jul 10 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0-2.356bzr
- Fixed source URL.
- Changed Req: p7zip to p7zip-plugins.
- Use included desktop file.

* Fri Jul 10 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0-1.356bzr
- First release.
