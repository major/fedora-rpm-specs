%define			prever	pre20040408
Summary:		A bootloader which can be started from the SRM console
Name:			aboot
Version:		1.0
Release:		0.24.%{prever}%{?dist}
ExclusiveArch:	alpha
License:		GPLv2+
URL:			http://www.sf.net/projects/aboot
Source0:		http://aboot.sourceforge.net/tarballs/aboot-%{version}_%{prever}.tar.bz2
Patch0:			aboot_1.0~%{prever}-2.diff.gz
Patch1:			aboot-1.0.doc_install_fix.patch
Patch2:			aboot-optflags.patch
BuildRequires:	kernel-devel, docbook-utils
BuildRequires: make

%description
The aboot program is the preferred way of booting Linux when using SRM
firmware (the firmware normally used to boot an DEC UNIX). Aboot supports
the creation of bootable block devices and contains a program which can
load Linux kernels from a filesystem which is bootable by SRM.  Aboot
also supports direct booting from various filesystems (ext2, ISO9660,
UFS), booting of executable object files (ELF and ECOFF), booting of
compressed kernels, network booting (using bootp), partition tables in
DEC UNIX format, and interactive booting and default configurations for
SRM consoles that cannot pass long option strings.

If you are installing Fedora or Red Hat Linux on an Alpha, you'll need to
install the aboot package.

%prep
%setup -q -n %{name}-%{version}_%{prever}
%patch0 -p1
%patch1 -p1 -b .doc_install_fix
%patch2 -p1 -b .optflags

%build
sed -ie "s^KSRC.*=.*$^KSRC=/lib/modules/`uname -r`/build^" Makefile
export OPTFLAGS="%{optflags}"
make
cd doc/man && make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
chmod go= $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8
make root=$RPM_BUILD_ROOT bindir=$RPM_BUILD_ROOT/sbin install

mv -f sdisklabel/README sdisklabel/README-sdisklabel || true

%files
%doc INSTALL README ChangeLog TODO aboot.conf sdisklabel/README-sdisklabel COPYING
%attr(644, root, root) /boot/bootlx
/sbin/abootconf
/sbin/e2writeboot
/sbin/isomarkboot
/sbin/swriteboot
%defattr(0644,root,root)
%{_mandir}/man8/*
%{_mandir}/man5/*
%{_mandir}/man1/*

%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.24.pre20040408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.23.pre20040408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.22.pre20040408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.21.pre20040408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.20.pre20040408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.19.pre20040408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.18.pre20040408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.17.pre20040408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.16.pre20040408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.15.pre20040408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.14.pre20040408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.13.pre20040408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.12.pre20040408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.11.pre20040408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.10.pre20040408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.9.pre20040408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.8.pre20040408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.7.pre20040408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.6.pre20040408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.5.pre20040408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.4.pre20040408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.3.pre20040408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.2.pre20040408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Sep 27 2007 Oliver Falk <oliver@linux-kernel.at> - 1.0-0.1.pre20040408
- bz#294641:
  - New versioning - versioning guidelines
  - Add patch to add global rpm cflags and use 'em
  - Fix manpage attrs - defattr

* Fri Sep 21 2007 Oliver Falk <oliver@linux-kernel.at> - 1.0_pre20040408-2
- Fix some rpmlint warnings, bz#294641
- Fix license: GPLv2+, bz#294641

* Mon Aug 20 2007 Oliver Falk <oliver@linux-kernel.at> - 1.0_pre20040408-1
- Rebuild in koji
- Cleanup spec; Merge RH, AC, MDK spec
- To be included into upstream fp.o hopefully

* Mon Apr  18 2005 Balint Cristian <rezso@rdsor.ro>
- Latest from CVS
- Build for alphacore 1.0
- Fix build with 2.6

* Tue Nov 30 1999 Matt Wilson <msw@redhat.com>
- changed to use ext2 patch based from Ruediger Oertel <ro@suse.de>

* Mon Nov 22 1999 Matt Wilson <msw@redhat.com>
- patched ext2 read code to deal with rev1 filesystems
- added a patch to properly guess IDE cdroms
  (well, sort of)

* Tue Sep 07 1999 Cristian Gafton <gafton@redhat.com>
- add patch to allow it to boot on *large* disks

* Mon Apr 26 1999 Cristian Gafton <gafton@redhat.com>
- patch from Jay Estabrook to make it work with EXT2 filesystems larger
  than 2Gb

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 9)

* Tue Jan 19 1999 Erik Troan <ewt@redhat.com>
- built for Red HAt 6.0

* Tue Sep 15 1998 Richard Henderson <rth@cygnus.com>
- use aboot.lds for elf, so that the phdr comes out right.
- relax the need to have a compiled kernel installed.
- make sdisklabel take partition sizes in sectors, not kilobytes.

* Thu Aug 20 1998 Maciej W. Rozycki <macro@ds2.pg.gda.pl>
- corrected a small but essential error in the ELF patch

* Mon Aug  3 1998 Maciej W. Rozycki <macro@ds2.pg.gda.pl>
- added a patch to allow booting of ELF images created with binutils >= 2.9
- compiled against glibc 2.0.94

* Sun May 31 1998 Maciej W. Rozycki <macro@ds2.pg.gda.pl>
- made changes needed for glibc2 and 2.1.x kernels

