Name:		fsarchiver
Version:	0.8.5
Release:	20%{?dist}
Summary:	Safe and flexible file-system backup/deployment tool

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		http://www.fsarchiver.org
Source0:	https://github.com/fdupoux/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:	e2fsprogs-devel => 1.41.4
BuildRequires:	libuuid-devel
BuildRequires:	libblkid-devel
BuildRequires:	e2fsprogs
BuildRequires:	libattr-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	zlib-devel
BuildRequires:	bzip2-devel
BuildRequires:	lzo-devel
BuildRequires:	xz-devel
BuildRequires:	lz4-devel
BuildRequires:	libzstd-devel
BuildRequires: make

%description
FSArchiver is a system tool that allows you to save the contents of a 
file-system to a compressed archive file. The file-system can be restored 
on a partition which has a different size and it can be restored on a 
different file-system. Unlike tar/dar, FSArchiver also creates the 
file-system when it extracts the data to partitions. Everything is 
checksummed in the archive in order to protect the data. If the archive 
is corrupt, you just lose the current file, not the whole archive.

%prep
%autosetup -p1

%build
%configure
%{make_build}


%install
%{make_install}



%files
%doc README THANKS NEWS
%license COPYING
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.5-19
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Adel Gadllah <adel.gadllah@gmail.com> - 0.8.5-1
- New upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 Leigh Scott <leigh123linux@googlemail.com> - 0.8.3-5
- Apply upstream commit to fix F30 FTBFS
- Update spec file

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 02 2018 Adel Gadllah <adel.gadllah@gmail.com> - 0.8.3-1
- New upstream release

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct 09 2016 Adel Gadllah <adel.gadllah@gmail.com> - 0.8.0-1
- Update to 0.8.0

* Wed Mar 02 2016 Adel Gadllah <adel.gadllah@gmail.com> - 0.6.22-1
- Update to 0.6.22

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Adel Gadllah <adel.gadllah@gmail.com> - 0.6.21-2
- Fix build

* Mon Jan 04 2016 Adel Gadllah <adel.gadllah@gmail.com> - 0.6.21-1
- Update to 0.6.21

* Tue Jul 28 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 0.6.19-5
- Remove conflicting types definitions in favour of linux/types.h

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 01 2014 Adel Gadllah <adel.gadllah@gmail.com> - 0.6.19-1
- Update to 0.6.19
- Fixes regression introduced in 0.6.18

* Sat Feb 15 2014 Adel Gadllah <adel.gadllah@gmail.com> - 0.6.18-1
- Update to 0.6.18
- Fixes RH#925370

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 27 2013 Adel Gadllah <adel.gadllah@gmail.com> - 0.6.17-1
- Update to 0.6.17

* Fri Feb 08 2013 Adel Gadllah <adel.gadllah@gmail.com> - 0.6.16-1
- Update to 0.6.16

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Adel Gadllah <adel.gadllah@gmail.com> - 0.6.15-1
- Update to 0.6.15

* Fri Mar 09 2012 Adel Gadllah <adel.gadllah@gmail.com> - 0.6.13-1
- Update to 0.6.13

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec 12 2010 Adel Gadllah <adel.gadllah@gmail.com> - 0.6.11-1
- Update to 0.6.11

* Sat May 15 2010 Adel Gadllah <adel.gadllah@gmail.com> - 0.6.10-1
- Update to 0.6.10

* Sat May 08 2010 Adel Gadllah <adel.gadllah@gmail.com> - 0.6.9-1
- Update to 0.6.9

* Sat Feb 20 2010 Adel Gadllah <adel.gadllah@gmail.com> - 0.6.8-1
- Update to 0.6.8

* Fri Feb 12 2010 Adel Gadllah <adel.gadllah@gmail.com> - 0.6.7-3
- Fix build

* Tue Feb 09 2010 Adel Gadllah <adel.gadllah@gmail.com> - 0.6.7-2
- Fix build

* Tue Feb 09 2010 Adel Gadllah <adel.gadllah@gmail.com> - 0.6.7-1
- Update to 0.6.7

* Fri Jan 08 2010 Adel Gadllah <adel.gadllah@gmail.com> - 0.6.5-1
- Update to 0.6.5

* Mon Dec 28 2009 Adel Gadllah <adel.gadllah@gmail.com> - 0.6.3-1
- Update to 0.6.3

* Tue Dec 22 2009 Adel Gadllah <adel.gadllah@gmail.com> - 0.6.2-1
- Update to 0.6.2
- Apply fix as requested by upstream

* Sat Oct 10 2009 Adel Gadllah <adel.gadllah@gmail.com> - 0.6.1-1
- Update to 0.6.1

* Sun Sep 27 2009 Adel Gadllah <adel.gadllah@gmail.com> - 0.6.0-1
- Update to 0.6.0
- Fixes licensing issue (no longer links against openssl)

* Thu Sep 03 2009 Adel Gadllah <adel.gadllah@gmail.com> - 0.5.9-1
- Update to 0.5.9

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 0.5.8-5
- rebuilt with new openssl

* Mon Aug 17 2009 Adel Gadllah <adel.gadllah@gmail.com> - 0.5.8-4
- Enable XZ support

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jul 12 2009 Adel Gadllah <adel.gadllah@gmail.com> - 0.5.8-2
- BR libblkid-devel

* Sun Jul 12 2009 Adel Gadllah <adel.gadllah@gmail.com> - 0.5.8-1
- Update to 0.5.8

* Tue May 19 2009 Adel Gadllah <adel.gadllah@gmail.com> - 0.5.6-1
- Update to 0.5.6

* Tue May 19 2009 Adel Gadllah <adel.gadllah@gmail.com> - 0.5.5-2
- BR e2fsprogs

* Tue May 19 2009 Adel Gadllah <adel.gadllah@gmail.com> - 0.5.5-1
- Update to 0.5.5

* Fri May 01 2009 Adel Gadllah <adel.gadllah@gmail.com> - 0.5.2-1
- Update to 0.5.2

* Sat Mar 28 2009 Adel Gadllah <adel.gadllah@gmail.com> - 0.4.6-1
- Update to 0.4.6

* Sun Mar 22 2009 Adel Gadllah <adel.gadllah@gmail.com> - 0.4.5-1
- Update to 0.4.5

* Sat Mar 07 2009 Adel Gadllah <adel.gadllah@gmail.com> - 0.4.4-2
- Fix file section
- Fix changelog

* Sat Mar 07 2009 Adel Gadllah <adel.gadllah@gmail.com> - 0.4.4-1
- Update to 0.4.4

* Sat Feb 28 2009 Adel Gadllah <adel.gadllah@gmail.com> - 0.4.3-1
- 0.4.3
- Drop build patch, no longer needed

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 15 2009 Adel Gadllah <adel.gadllah@gmail.com> - 0.4.1-2
- Fix description

* Thu Feb 12 2009 Adel Gadllah <adel.gadllah@gmail.com> - 0.4.1-1
- Initial package
