Name:		kcc
Version:	2.3
Release:	62%{?dist}
License:	GPL-2.0-or-later

BuildRequires:	gcc
BuildRequires: make

## missed upstream.
Source:		ftp://ftp.sra.co.jp/pub/os/linux/JE/sources/base/%{name}.tar.gz
Source1:	kcc.1
Patch0:		kcc-2.3-dontstrip.patch
Patch1:		kcc-2.3-varargs.patch
Patch2:		kcc-2.3-fix-segv.patch
Patch3:		kcc-2.3-timestamp.patch
Patch4:		kcc-2.3-c99.patch

Summary:	Kanji Code Converter
%description
kcc is a kanji code converter with an auto detection.

%prep
%setup -q -n %{name}
%patch -P0 -p1 -b .dontstrip
%patch -P1 -p1 -b .varargs
%patch -P2 -p1 -b .segv
%patch -P3 -p1 -b .timestamp
%patch -P4 -p1 -b .c99

%build
make "CFLAGS=-std=gnu99 $RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/ja/man1
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
make BINPATH="$RPM_BUILD_ROOT%{_bindir}" install 
make MANPATH="$RPM_BUILD_ROOT%{_mandir}" JMANDIR="ja" install.man
for i in `find $RPM_BUILD_ROOT%{_mandir}/ja -type f`; do
	iconv -f euc-jp -t utf-8 $i > $i.new && mv -f $i.new $i && chmod 444 $i
done
install -m0644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/
gzip -9 $RPM_BUILD_ROOT%{_mandir}/man1/kcc.1

%files
%doc README
%license COPYING
%{_bindir}/kcc
%lang(ja) %{_mandir}/ja/man1/kcc.1*
%{_mandir}/man1/kcc.1*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-61
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec  1 2022 Akira TAGOH <tagoh@redhat.com> - 2.3-56
- Convert License tag to SPDX.

* Wed Oct 26 2022 Florian Weimer <fweimer@redhat.com> - 2.3-55
- Updates for C99 compatibility (#2141799).
- Build in C99 mode because of old-style function definitions.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Akira TAGOH <tagoh@redhat.com> - 2.3-45
- Add BR: gcc

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul  2 2015 Akira TAGOH <tagoh@redhat.com> - 2.3-39
- Add a dist tag (#1237175)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 12 2008 Akira TAGOH <tagoh@redhat.com> - 2.3-28
- Rebuild for gcc-4.3.

* Fri Sep 21 2007 Akira TAGOH <tagoh@redhat.com> - 2.3-27
- clean up the spec file.

* Thu Aug 23 2007 Akira TAGOH <tagoh@redhat.com> - 2.3-26
- Rebuild

* Wed Aug  8 2007 Akira TAGOH <tagoh@redhat.com> - 2.3-25
- Update License tag.
- clean up the spec file.

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.3-24.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.3-24.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.3-24.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Mar 17 2005 Akira TAGOH <tagoh@redhat.com> - 2.3-24
- rebuilt

* Thu Feb 10 2005 Akira TAGOH <tagoh@redhat.com> - 2.3-23
- rebuilt

* Tue Jun 22 2004 Akira TAGOH <tagoh@redhat.com> 2.3-22
- kcc-2.3-fix-segv.patch: applied to fix segfaults with invalid options. (#126338)
- add kcc.1 from Debian package.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Sep 30 2003 Akira TAGOH <tagoh@redhat.com> 2.3-19
- converted Japanese manpage to UTF-8.

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu May 22 2003 Jeremy Katz <katzj@redhat.com> 2.3-17
- gcc 3.3 doesn't implement varargs.h, include stdarg.h instead

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Nov 13 2002 Akira TAGOH <tagoh@redhat.com> 2.3-15
- rebuild.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Jun 18 2002 Akira TAGOH <tagoh@redhat.com>
- clean up a spec.
- s/Copyright/License/
- kcc-2.3-dontstrip.patch: fix the stripped binary.

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Tue Dec 19 2000 Akira Tagoh <tagoh@redhat.com>
- rebuild for 7.1

* Mon Sep 11 2000 Matt Wilson <msw@redhat.com>
- added %%defattr(-,root,root)

* Fri Aug  4 2000 ISHIKAWA Mutsumi <ishikawa@redhat.com>
- built for RedHat 7.0
- adopt fhs

* Sun Mar 26 2000 Chris Ding <cding@redhat.com>
- ja -> ja_JP.eucJP

* Tue Mar 21 2000 Chris Ding <cding@redhat.com>
- ja_JP.eucJP -> ja

* Wed Mar 15 2000 Matt Wilson <msw@redhat.com>
- rebuild for 6.2j
- gzip man pages

* Tue Feb 29 2000 Chris Ding <cding@redhat.com>
- ja_JP.ujis -> ja_JP.eucJP

* Thu Oct  7 1999 Matt Wilson <msw@redhat.com>
- rebuilt against 6.1

* Sun May 30 1999 FURUSAWA,Kazuhisa <kazu@linux.or.jp>
- 1st Release for i386 (glibc2.1).
- Original Packager: Atsushi Yamagata <yamagata@plathome.co.jp>

* Wed Jan 20 1999 Atsushi Yamagata <yamagata@plathome.co.jp>
- version up to 2.3
- /usr/local -> /usr
- Extensions/Japanese -> Utilities/Text

* Fri May  1 1998 FURUSAWA,Kazuhisa <kazu_f@big.or.jp>
- 9th release
