Name:           disktype
Version:        9
Release:        44%{?dist}
Summary:        Detect the content format of a disk or disk image

License:        MIT
URL:            http://disktype.sourceforge.net/
Source0:        http://downloads.sourceforge.net/disktype/disktype-9.tar.gz

Patch0:         eju2014-disktype.patch

BuildRequires:  gcc
BuildRequires:  libewf-devel
BuildRequires:  make

%description
The purpose of disktype is to detect the content format of a disk or disk
image. It knows about common file systems, partition tables, and boot codes.

%prep
%setup -q
%patch -P0 -p1

%build
sed -i '/CFLAGS   =/d' Makefile
sed -i '/LDFLAGS  =/d' Makefile
%make_build CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" LIBEWF=1

%install
mkdir -p %{buildroot}{%{_bindir},%{_mandir}/man1}
install -m 755 disktype %{buildroot}%{_bindir}
install -p -m 644 disktype.1 %{buildroot}%{_mandir}/man1

%files
%doc HISTORY TODO
%license LICENSE
%{_bindir}/disktype
%{_mandir}/man1/disktype.1*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 9-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Richard Fearn <richardfearn@gmail.com> - 9-39
- Don't glob everything under shared directories in %%files

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 27 2022 Richard Fearn <richardfearn@gmail.com> - 9-37
- Use SPDX license identifier

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Richard Fearn <richardfearn@gmail.com> - 9-31
- Add file systems: btrfs, ext4, f2fs, exfat
- Add LUKS encryption container detection/identification
- Add support for EWF images

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 05 2019 Richard Fearn <richardfearn@gmail.com> - 9-27
- Don't remove buildroot in %%install section

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 24 2018 Richard Fearn <richardfearn@gmail.com> - 9-25
- Add BuildRequires: gcc
  (see https://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 16 2017 Richard Fearn <richardfearn@gmail.com> - 9-23
- Remove unnecessary Group: tag, BuildRoot: tag, and %%clean section

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Richard Fearn <richardfearn@gmail.com> - 9-18
- Remove unnecessary %%defattr

* Wed Sep 23 2015 Richard Fearn <richardfearn@gmail.com> - 9-17
- Enable hardened build

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 01 2013 Nicolas Chauvet <kwizart@gmail.com> - 9-12
- Drop libewf support

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Apr 02 2010 Richard Fearn <richardfearn@gmail.com> - 9-6
- Bump for rebuild against libewf 20100226

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu May  1 2008 Richard Fearn <richardfearn@gmail.com> - 9-3
- update EWF patch so that it doesn't modify CFLAGS/LDFLAGS
- mention EWF in man page

* Fri Apr 25 2008 Richard Fearn <richardfearn@gmail.com> - 9-2
- build using $(RPM_OPT_FLAGS)
- install man page with -p to preserve timestamp
- add patch to support EWF images

* Sat Mar  8 2008 Richard Fearn <richardfearn@gmail.com> - 9-1
- initial package for Fedora

