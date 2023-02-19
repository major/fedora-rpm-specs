Name:		mactel-boot
Version:	0.9
Release:	29%{?dist}
Summary:	Intel Mac boot files

License:	GPLv2+
URL:		http://www.codon.org.uk/~mjg59/mactel-boot/
Source:		http://www.codon.org.uk/~mjg59/mactel-boot/%{name}-%{version}.tar.bz2
Source1:	mactel-boot-setup
Patch0: mactel-boot-c99.patch

ExclusiveArch:	x86_64

Requires:	coreutils

BuildRequires: make
BuildRequires:  gcc
%description
Files for booting Fedora on Intel-based Apple hardware using EFI.

%prep
%autosetup -p1

%build
make PRODUCTVERSION="Fedora %{fedora}" %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
install -D -m 644 SystemVersion.plist $RPM_BUILD_ROOT/boot/efi/System/Library/CoreServices/SystemVersion.plist
echo "This file is required for booting" >$RPM_BUILD_ROOT/boot/efi/mach_kernel
touch $RPM_BUILD_ROOT/boot/efi/System/Library/CoreServices/boot.efi
touch $RPM_BUILD_ROOT/boot/efi/.VolumeIcon.icns
install -D %{SOURCE1} $RPM_BUILD_ROOT/usr/libexec/mactel-boot-setup

%files
%license GPL
%license Copyright
/usr/share/man/man1/hfs-bless.1.gz
/boot/efi/mach_kernel
%dir /boot/efi/System/
%dir /boot/efi/System/Library/
%dir /boot/efi/System/Library/CoreServices/
/boot/efi/System/Library/CoreServices/SystemVersion.plist
/usr/sbin/hfs-bless
/usr/libexec/mactel-boot-setup
%attr(0755, root, root) %ghost /boot/efi/System/Library/CoreServices/boot.efi
%attr(0644, root, root) %ghost /boot/efi/.VolumeIcon.icns

%triggerin -- grub-efi grub2-efi fedora-logos generic-logos
/usr/libexec/mactel-boot-setup

%changelog
* Fri Feb 17 2023 Florian Weimer <fweimer@redhat.com> - 0.9-29
- Port to C99 (#2170958)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 13 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.9-20
- Own all the directories, use %%license

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Sep 06 2012 Matthew Garrett <mjg@redhat.com> - 0.9-7
- update mactel-boot-setup for F18

* Mon May 14 2012 Matthew Garrett <mjg@redhat.com> - 0.9-6
- Fix destination path for disk label install

* Wed Apr 25 2012 Matthew Garrett <mjg@redhat.com> - 0.9-5
- Move trigger functionality into an external script

* Thu Apr 19 2012 Matthew Garrett <mjg@redhat.com> - 0.9-4
- Blessing must take place after linking

* Thu Apr 19 2012 Matthew Garrett <mjg@redhat.com> - 0.9-3
- Hardlink the bootloader to boot.efi, rather than symlinking
- Redo the spec file to make better use of macros

* Tue Feb 28 2012 Matthew Garrett <mjg@redhat.com> - 0.9-2
- add support for volume labels

* Tue Feb 07 2012 Matthew Garrett <mjg@redhat.com> - 0.9-1
- new upstream, uses kernel ioctl rather than editing the fs by hand

* Wed Dec 14 2011 Matthew Garrett <mjg@redhat.com> - 0.1-4
- Fix symlinks

* Tue Dec 13 2011 Matthew Garrett <mjg@redhat.com> - 0.1-3
- rename binary to hfs-bless
- make sure writes actually hit disk

* Mon Nov 21 2011 Matthew Garrett <mjg@redhat.com> - 0.1-2
- switch to using triggers
- ensure that the filesystem is HFS+ before running bless

* Fri Nov 18 2011 Matthew Garrett <mjg@redhat.com> - 0.1-1
- initial release
