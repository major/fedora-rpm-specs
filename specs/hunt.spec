Summary:	Tool for demonstrating well known weaknesses in the TCP/IP protocol suite
Name:		hunt
Version:	1.5
Release:	44%{?dist}
License:	GPL-2.0-only
Source:		http://lin.fsid.cvut.cz/~kra/hunt/%name-%version.tgz
Patch0:		hunt-1.5-arridx.patch
Patch1:		hunt-1.5-cleanup.patch
Patch2:		hunt-1.5-signness.patch
Patch3:		hunt-1.5-listlen.patch
Patch4:		hunt-1.5-badcmp.patch
Patch5:		hunt-1.5-datatypes.patch
Patch6:		hunt-1.5-format-security.patch
URL:		http://lin.fsid.cvut.cz/~kra/index.html

BuildRequires:  gcc
BuildRequires: make
%description
Hunt is a program for intruding into a connection, watching it and
resetting it. It was inpired by products like Juggernaut or T-sight
but has several features which can not be found in these products.

Note that hunt is operating on Ethernet and is best used for connections
which can be watched through it. However, it is possible to do something
even for hosts on another segments. The hunt doesn't distinguish between
local network connections and connections going to/from Internet. It can
handle all connections it sees.

Connection hijacking is aimed primarily at the telnet traffic but it can
be used for another traffic too.  The reset, watching, arp... features
are common to all connections.


%prep
%setup -q
%patch -P0 -p1 -b .arridx
%patch -P1 -p1 -b .cleanup
%patch -P2 -p1 -b .signness
%patch -P3 -p1 -b .listlen
%patch -P4 -p1 -b .badcmp
%patch -P5 -p1 -b .datatypes
%patch -P6 -p1 -b .format-security


%build
make clean
# Sources aren't c11 compliant
#   Work-around by appending -std=gnu89 to CC
# Makefile uses CC to link, but misses to pass CFLAGS
#   Work-around by passing rpm's CFLAGS as LDFLAGS
make %{?_smp_mflags} hunt \
  CC='%__cc -std=gnu89' \
  CFLAGS="$RPM_OPT_FLAGS -D_REENTRANT" \
  LDFLAGS="$RPM_OPT_FLAGS -D_REENTRANT"


%install
install -d $RPM_BUILD_ROOT%_sbindir $RPM_BUILD_ROOT%_mandir/man1 \
           $RPM_BUILD_ROOT%_libdir/%name

install -p hunt          $RPM_BUILD_ROOT%_sbindir/
install -p tpsetup/*     $RPM_BUILD_ROOT%_libdir/%name/
install -p -m644 man/*.1 $RPM_BUILD_ROOT%_mandir/man1/


%files
%doc CHANGES README* TODO
%license COPYING
%doc %{_mandir}/*/*
%{_sbindir}/*
%{_libdir}/hunt



%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Mar 02 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.5-39
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5-28
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Aug 29 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.5-22
- Address F23FTBFS (RHBZ#1239571):
  - Pass CFLAGS as LDFLAGS to Makefile
  - Append -std=gnu89 to CC.
- Add %%license.
- Modernize spec.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 06 2013 Jon Ciesla <limburgher@gmail.com> - 1.5-18
- Patch to allow use of -Werror=format-security, BZ 1025242.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 28 2013 Jon Ciesla <limburgher@gmail.com> - 1.5-16
- Spec cleanup.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar  1 2009 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.5-10
- do not build the static binary
- fixed some int <-> void * cast issues

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jul 31 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.5-8
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.5-7
- Autorebuild for GCC 4.3

* Fri Sep 15 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.5-6
- rebuilt

* Sat Feb 18 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.5-5
- removed unneeded curlies
- use commands directly instead of the %%__XXX macros

* Thu May 19 2005 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.5-4
- use %%dist instead of %%disttag

* Thu Mar  3 2005 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0:1.5-3
- fixed out-of-range array subscript (BZ #149777)
- fixed lots of warnings regarding different signedness
- fixed some minor compilation warnings
- fixed bad handling of hosts-lists when start-host > end-host

* Fri May  9 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:1.5-0.fdr.2
- updated source-url

* Mon May  5 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:1.5-0.fdr.1
- updated to recent fedora policies
- removed static binary from the filelist
- debugfiles are not included anymore
- s!Copyright!License!
- fixed %%description

* Thu Oct 25 2001 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 1.5-4
- Updated URL

* Wed Jun  6 2001 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de>
- added %%defattr(-,root,root)

* Fri Jun  1 2001 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de>
- typo

* Fri Jun  1 2001 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de>
- updated to 1.5
- cleanups

* Fri May 05 2000 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de>
- Update to 1.4
- Modified the .../contrib/* spec-file a little bit
