Summary:	Tool to check and undelete partition, PhotoRec recovers lost files
Summary(pl.UTF8):	Narzędzie sprawdzające i odzyskujące partycje
Summary(fr.UTF8):	Outil pour vérifier et restaurer des partitions
Summary(ru_RU.UTF8): Программа для проверки и восстановления разделов диска
Name:		testdisk
Version:	7.2
Release:	4%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
Source0:	https://www.cgsecurity.org/testdisk-%{version}.tar.bz2
URL:		https://www.cgsecurity.org/wiki/TestDisk
BuildRequires: make
BuildRequires:	desktop-file-utils
BuildRequires:	e2fsprogs-devel
BuildRequires:	libewf-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libuuid-devel
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	ntfs-3g-devel
BuildRequires:	qt5-linguist
BuildRequires:	qt5-qtbase-devel
BuildRequires:	zlib-devel
Obsoletes:	testdisk-doc < 6.12

%description
Tool to check and undelete partition. Works with FAT12, FAT16, FAT32,
NTFS, ext2, ext3, ext4, btrfs, BeFS, CramFS, HFS, JFS, Linux Raid, Linux
Swap, LVM, LVM2, NSS, ReiserFS, UFS, XFS.
PhotoRec is a signature based file recovery utility. It handles more than
440 file formats including JPG, MSOffice, OpenOffice documents.

%description -l pl.UTF8
Narzędzie sprawdzające i odzyskujące partycje. Pracuje z partycjami:
FAT12, FAT16, FAT32, NTFS, ext2, ext3, ext4, btrfs, BeFS, CramFS, HFS, JFS,
Linux Raid, Linux Swap, LVM, LVM2, NSS, ReiserFS, UFS, XFS.
PhotoRec is a signature based file recovery utility. It handles more than
440 file formats including JPG, MSOffice, OpenOffice documents.

%description -l fr.UTF8
TestDisk vérifie et récupère les partitions. Fonctionne avec
FAT12, FAT16, FAT32, NTFS, ext2, ext3, ext4, btrfs, BeFS, CramFS, HFS, JFS,
Linux Raid, Linux Swap, LVM, LVM2, NSS, ReiserFS, UFS, XFS.
PhotoRec utilise un mécanisme de signature pour récupérer des fichiers
perdus. Il reconnait plus de 440 formats de fichiers dont les JPEG, les
documents MSOffice ou OpenOffice.

%description -l ru_RU.UTF8
Программа для проверки и восстановления разделов диска.
Поддерживает следующие типы разделов:
FAT12, FAT16, FAT32, NTFS, ext2, ext3, ext4, btrfs, BeFS, CramFS, HFS, JFS,
Linux Raid, Linux Swap, LVM, LVM2, NSS, ReiserFS, UFS, XFS.
PhotoRec is a signature based file recovery utility. It handles more than
440 file formats including JPG, MSOffice, OpenOffice documents.

%package -n qphotorec
Summary:	Signature based file carver. Recover lost files

%description -n qphotorec
QPhotoRec is a Qt version of PhotoRec. It is a signature based file recovery
utility. It handles more than 440 file formats including JPG, MSOffice,
OpenOffice documents.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/qphotorec.desktop

%if 0%{?rhel} && 0%{?rhel} < 8
%post -n qphotorec
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun -n qphotorec
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans -n qphotorec
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
%endif

%files
%doc AUTHORS ChangeLog NEWS README.md THANKS
%license COPYING
%doc documentation.html
%{_bindir}/fidentify
%{_bindir}/photorec
%{_bindir}/testdisk
%{_mandir}/man8/fidentify.8*
%{_mandir}/man8/photorec.8*
%{_mandir}/man8/testdisk.8*
%{_mandir}/zh_CN/man8/fidentify.8*
%{_mandir}/zh_CN/man8/photorec.8*
%{_mandir}/zh_CN/man8/testdisk.8*

%files -n qphotorec
%{_bindir}/qphotorec
%{_mandir}/man8/qphotorec.8*
%{_mandir}/zh_CN/man8/qphotorec.8*
%{_datadir}/applications/qphotorec.desktop
%{_datadir}/icons/hicolor/48x48/apps/qphotorec.png
%{_datadir}/icons/hicolor/scalable/apps/qphotorec.svg

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 7.2-3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Feb 22 2024 Christophe Grenier <grenier@cgsecurity.org> - 7.2-1
- Update to latest version https://www.cgsecurity.org/wiki/TestDisk_7.2_Release

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 01 2021 Adam Williamson <awilliam@redhat.com> - 7.1-7
- Rebuild for new ntfs-3g soname

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 10 2019 Christophe Grenier <grenier@cgsecurity.org> - 7.1-1
- Update to latest version https://www.cgsecurity.org/wiki/TestDisk_7.1_Release

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 20 2018 Neal Gompa <ngompa@datto.com> - 7.0-14
- Explicitly indicate qt4-devel BR
- Use macros for make invocations
- Drop Group tag
- Drop icon cache scriptlets for Fedora
- Drop redundant attr settings for files
- Mark COPYING as a license file

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Tom Callaway <spot@fedoraproject.org> - 7.0-9
- rebuild for new ntfs-3g

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Mar 28 2016 Tom Callaway <spot@fedoraproject.org> - 7.0-7
- rebuild with ntfs-3g override

* Mon Mar 28 2016 Tom Callaway <spot@fedoraproject.org> - 7.0-6
- rebuild for new ntfs-3g

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jul 25 2015 Christophe Grenier <grenier@cgsecurity.org> - 7.0-4
- add missing doc documentation.html

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 23 2015 Christophe Grenier <grenier@cgsecurity.org> - 7.0-2
- move qphotorec to a separate subpackage

* Sat Apr 18 2015 Christophe Grenier <grenier@cgsecurity.org> - 7.0-1
- Update to latest version
- This version includes some security fixes.

* Wed Apr  8 2015 Tom Callaway <spot@fedoraproject.org> - 6.14-6
- rebuild for ntfs-3g soname bump

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 27 2014 Kalev Lember <kalevlember@gmail.com> - 6.14-3
- Rebuilt for ntfs-3g soname bump

* Wed Nov 06 2013 Christophe Grenier <grenier@cgsecurity.org> - 6.14-2
- Patch for additional ext2 check (Bug #1027026)

* Mon Sep 09 2013 Christophe Grenier <grenier@cgsecurity.org> - 6.14-1
- Update to latest version http://www.cgsecurity.org/wiki/TestDisk_6.14_Release

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 01 2013 Nicolas Chauvet <kwizart@gmail.com> - 6.13-6
- Rebuilt for libewf

* Sun Jan 27 2013 Christophe Grenier <grenier@cgsecurity.org> - 6.13-5
- rebuild for new ntfs-3g

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 6.13-4
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 6.13-3
- rebuild against new libjpeg

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Feb 12 2012 Christophe Grenier <grenier@cgsecurity.org> - 6.13-1
- Update to latest version

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 12 2011 Christophe Grenier <grenier@cgsecurity.org> - 6.12.2
- Rebuild for ntfs-3g

* Thu May 12 2011 Christophe Grenier <grenier@cgsecurity.org> - 6.12.1
- Update to latest version

* Sat Apr 16 2011 Christophe Grenier <grenier@cgsecurity.org> - 6.11-9
- Rebuild for ntfs-3g

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 27 2010 Christophe Grenier <grenier@cgsecurity.org> 6.11-7
- Move binaries to /usr/bin (#628050)

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 6.11-6
- rebuilt with new openssl

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Christophe Grenier <grenier@cgsecurity.org> 6.11-4
- Add "BuildRequires:  libuuid-devel"

* Wed May  6 2009 Christophe Grenier <grenier@cgsecurity.org> 6.11-3
- Use upstream patch v2

* Fri Apr 24 2009 Christophe Grenier <grenier@cgsecurity.org> 6.11-2
- Add upstream patch that add missing bound checks when parsing EXIF information

* Sun Apr 19 2009 Christophe Grenier <grenier@cgsecurity.org> 6.11-1
- Update to latest version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jul 31 2008 Christophe Grenier <grenier@cgsecurity.org> 6.10-1
- Update to latest version

* Wed Mar 19 2008 Christophe Grenier <grenier@cgsecurity.org> 6.9-2
- Fix for new API in libewf > 20070512

* Wed Feb 13 2008 Christophe Grenier <grenier@cgsecurity.org> 6.9-1
- Update to latest version

* Mon Dec 10 2007 Christophe Grenier <grenier@cgsecurity.org> 6.8-6
- Don't disable libewf during compilation

* Mon Dec  3 2007 Christophe Grenier <grenier@cgsecurity.org> 6.8-5
- Don't require ntfsprogs-devel on ppc and ppc64

* Mon Dec  3 2007 Christophe Grenier <grenier@cgsecurity.org> 6.8-4
- Rename TestDisk list functions to avoid conflict with latest ntfsprogs-devel 2.0.0

* Sun Dec  2 2007 Christophe Grenier <grenier@cgsecurity.org> 6.8-3
- Use libewf for support of the Expert Witness Compression Format (EWF)

* Thu Aug 16 2007 Christophe Grenier <grenier@cgsecurity.org> 6.8-2
- Fix the license in the spec file

* Tue Aug 14 2007 Christophe Grenier <grenier@cgsecurity.org> 6.8-1
- Update to latest version

* Fri Jun 29 2007 Christophe Grenier <grenier@cgsecurity.org> 6.7-1
- Update to latest version

* Sun Feb 18 2007 Christophe Grenier <grenier@cgsecurity.org> 6.6-1
- Update to latest version

* Mon Feb 5 2007 Christophe Grenier <grenier@cgsecurity.org> 6.5-3
- Fix russian description in spec file

* Sun Nov 26 2006 Christophe Grenier <grenier@cgsecurity.org> 6.5-2
- Use ntfsprogs to provide NTFS listing capabilities to TestDisk

* Tue Oct 24 2006 Christophe Grenier <grenier@cgsecurity.org> 6.5-1
- Update to latest version

* Mon Aug 28 2006 Christophe Grenier <grenier@cgsecurity.org> 6.4-3
- Rebuild for Fedora Extras 6

* Wed Jun 21 2006 Christophe Grenier <grenier@cgsecurity.org> 6.4-2
- FC3 and FC4 has a release of 2, need to align

* Wed Jun 21 2006 Christophe Grenier <grenier@cgsecurity.org> 6.4-1
- Update to latest version

* Mon Mar  6 2006 Christophe Grenier <grenier@cgsecurity.org> 6.3-1
- Update to latest version

* Tue Feb 28 2006 ChangeLog Grenier <grenier@cgsecurity.org> 6.2-4
- Rebuild for Fedora Extras 5

* Mon Jan 23 2006 Christophe Grenier <grenier@cgsecurity.org> 6.2-3
- same spec for all arches hence add dist

* Sun Jan 4 2004 Christophe Grenier <grenier@cgsecurity.org> 5.0
- 5.0

* Wed Oct 1 2003 Christophe Grenier <grenier@cgsecurity.org> 4.5
- 4.5

* Wed Apr 23 2003 Christophe Grenier <grenier@cgsecurity.org> 4.4-2

* Sat Mar 29 2003 Pascal Terjan <CMoi@tuxfamily.org> 4.4-1mdk
- 4.4

* Fri Dec 27 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 4.2-2mdk
- rebuild for rpm and glibc

* Sun Oct 06 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 4.2-1mdk
- 4.2

* Mon Sep 02 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 4.1-1mdk 
- By Pascal Terjan <pascal.terjan@free.fr>
	- first mdk release, adapted from PLD.
	- gz to bz2 compression.
- fix %%tmppath
- %%make instead %%{__make}
