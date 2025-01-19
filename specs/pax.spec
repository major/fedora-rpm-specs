%global ALTERNATIVES            %{_sbindir}/alternatives

Summary: POSIX File System Archiver
Name: pax
Version: 3.4
Release: 47%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD

# 2018-07-24 upstream maintainer contacted about non-working URLs
# 2020-06-02 moved upstream URLs to point to fedora git as upstream will not host it anymore
Source: https://src.fedoraproject.org/repo/pkgs/rpms/pax/pax-3.4.tar.bz2/md5/fbd9023b590b45ac3ade95870702a0d6/%{name}-%{version}.tar.bz2
URL:    https://src.fedoraproject.org/rpms/%{name}

#use Linux PATH_MAX (4092) for maximum PATHLENGTH instead of pax default 3072
Patch0: pax-3.0-PATHMAX.patch

#fix bug with archiving files of filename length exactly 100 chars
Patch1: pax-3.4-abs100.patch

#do not truncate names when extracting
Patch2: pax-3.4-rdtruncate.patch

#do not fail with gcc-4.6+
Patch3: pax-gcc46.patch

# manpage edits - s/pax/opax/, add cross references
Patch4: pax-3.4-manpage.patch

# Remove -Werror and fix one soon-to-be-issue warning (rhbz#1424041)
Patch5: pax-3.4-disable-Werror.patch

# multiple definition and FALLTHROUGH
Patch6: pax-3.4-gcc10.patch

Requires(post):  %{ALTERNATIVES}
Requires(preun): %{ALTERNATIVES}

BuildRequires: make
BuildRequires: gcc

%description
The 'pax' utility is the POSIX standard archive tool.  It supports the two most
common forms of standard Unix archive (backup) files - CPIO and TAR.

# "desired" alternative constants
%global ALT_NAME                pax
%global ALT_LINK                %{_bindir}/pax
%global ALT_SL1_NAME            pax-man
%global ALT_SL1_LINK            %{_mandir}/man1/pax.1.gz

# "local" alternative constants ("opax" - OpenBSD pax)
%global ALT_PATH                %{_bindir}/opax
%global ALT_SL1_PATH            %{_mandir}/man1/opax.1.gz

# helpers for alternatives
%global ALT_MAN_ORIG            %{_mandir}/man1/pax.1
%global ALT_MAN_NEW             %{_mandir}/man1/opax.1


%prep
%autosetup -p1


%build
%configure
make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install
mv %{buildroot}%{ALT_LINK} %{buildroot}%{ALT_PATH}
mv %{buildroot}%{ALT_MAN_ORIG} %{buildroot}%{ALT_MAN_NEW}
ln -s %{ALT_PATH} %{buildroot}%{ALT_LINK}
ln -s %{ALT_MAN_NEW} %{buildroot}%{ALT_MAN_ORIG}


%files
%license COPYING
%doc ABOUT-NLS AUTHORS ChangeLog NEWS README THANKS
%{ALT_PATH}
%doc %{ALT_SL1_PATH}
%ghost %verify(not md5 size mode mtime) %{ALT_LINK}
%ghost %verify(not md5 size mode mtime) %{ALT_SL1_LINK}


%post
# We need to remove old /usr/bin/pax binary and manpage because the following
# 'update-alternatives' step does not do it itself.  We may remove this once we
# are sure that pax >= 3.4-21 is installed on the system.
for i in "%{ALT_LINK}" "%{ALT_SL1_LINK}"; do
    test -f "$i" && test ! -h "$i" && rm -rf "$i"
done

%{ALTERNATIVES} \
    --install   %{ALT_LINK}     %{ALT_NAME}     %{ALT_PATH}     33 \
    --slave     %{ALT_SL1_LINK} %{ALT_SL1_NAME} %{ALT_SL1_PATH} \

%preun
if [ $1 -eq 0 ]; then
    # only on pure uninstall (not upgrade)
    %{ALTERNATIVES} --remove %{ALT_NAME} %{ALT_PATH}
fi


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 3.4-46
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 02 2020 Petr Kubat <pkubat@redhat.com> - 3.4-35
- Move upstream URLs to fedora git

* Fri Jan 31 2020 Than Ngo <than@redhat.com> - 3.4-34
- Fix FTBFS agains gcc10

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Pavel Raiskup <praiskup@redhat.com> - 3.4-30
- spec cleanup
- put gcc into BuildRequires (rhbz#1605380)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 19 2017 Pavel Raiskup <praiskup@redhat.com> - 3.4-25
- FTBFS for gcc 7 (rhbz#1424041)
- use %%autosetup

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Dec 08 2014 Pavel Raiskup <praiskup@redhat.com> - 3.4-21
- alternatives: remove the non-symlink manual page also (#1161258)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 06 2013 Pavel Raiskup <praiskup@redhat.com> - 3.4-17
- remove old %%{_bindir}/pax binary if existent during update

* Wed May 15 2013 Pavel Raiskup <praiskup@redhat.com> - 3.4-16
- setup the 'alternatives' template (#929349)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 29 2011 Ondrej Vasik <ovasik@redhat.com> - 3.4-12
- fix FTBFS with gcc4.6+ - (#715754)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 19 2009 Ondrej Vasik <ovasik@redhat.com> - 3.4-8
- Merge review #226235: fix use of %%makeinstall as well

* Mon Jan 19 2009 Ondrej Vasik <ovasik@redhat.com> - 3.4-7
- Merge review #226235: do ship doc files,
  do comment patches, use better buildroot and
  defaults for attributes, allow parallel builds

* Fri Aug 29 2008 Ondrej Vasik <ovasik@redhat.com> - 3.4-6
- removed duplicate Source0

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.4-5
- Autorebuild for GCC 4.3

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 3.4-4
- Rebuild for selinux ppc32 issue.

* Mon Jul 16 2007 Radek Brich <rbrich@redhat.com> - 3.4-3
- do not truncate file names when extracting (#205324)

* Wed Jun 20 2007 Radek Brich <rbrich@redhat.com> - 3.4-2
- applied patch for #239000 (pax fails creation of ustar
  if an absolute name is exactly 100 characters long)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 3.4-1.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 3.4-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 3.4-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Aug 15 2005 Peter Vrabec <pvrabec@redhat.com> 3.4-1
- upgrade 3.4

* Fri Mar 18 2005 Peter Vrabec <pvrabec@redhat.com> 3.0-11
- rebuilt

* Thu Oct 21 2004 Peter Vrabec <pvrabec@redhat.com>
- fix PAXPATHLEN (#132857)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Dec 12 2002 Tim Powers <timp@redhat.com> 3.0-5
- rebuild on all arches

* Wed Jul 03 2002 Karsten Hopp <karsten@redhat.de>
- fix documentation (#63671)

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Mar  5 2002 Matt Wilson <msw@redhat.com>
- pull PAX source tarball from the SuSE package (which is based off
  this one yet claims copyright on the spec file)

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Fri Feb 23 2001 Jakub Jelinek <jakub@redhat.com>
- make it build under glibc 2.2.2

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Fri Jun 30 2000 Preston Brown <pbrown@redhat.com>
- debian version, which is a port from OpenBSD's latest.

* Tue Jun 13 2000 Preston Brown <pbrown@redhat.com>
- FHS paths

* Tue May 30 2000 Preston Brown <pbrown@redhat.com>
- adopted for Winston.

