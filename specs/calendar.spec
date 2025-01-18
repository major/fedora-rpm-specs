%define alphatag 20240528cvs

Summary: Reminder utility
Name:    calendar
Version: 1.37
Release: 10.%{alphatag}%{?dist}
License: BSD-3-Clause AND BSD-2-Clause AND ISC
URL:     http://www.openbsd.org/cgi-bin/cvsweb/src/usr.bin/calendar

# The source archive is generated with the export-calendar-source.sh
# script.  Update the script's TAG variable when a new version of
# OpenBSD is released.  The version number we use for the calendar
# program is the CVS revision ID of the calendar.c file.  This is
# determined by the script so it can make the source archive.
Source0: %{name}-%{version}-%{alphatag}.tar.gz
Source1: Makefile.linux
Source2: export-calendar-source.sh

Patch0:  %{name}-1.37-linux.patch

BuildRequires: gcc
BuildRequires: make
Requires: cpp

%description
The OpenBSD calendar command is a reminder utility.  Calendar reads
a mix of configuration files and standard calendar databases and
then displays lines that begin with either today's date or
tomorrow's.  The output of the command shows upcoming events for the
week.

%prep
%autosetup -n %{name}-%{version}-%{alphatag}
cp %{SOURCE1} Makefile

for c in calendars/*.*/* ; do
    fromcode="$(grep '^LANG=' "$c" | sed 's/^LANG=\(.*\)\.\(.*\)\(@.*\)\{0,1\}/\2/')"
    if [ ! -z "$fromcode" ]; then
        iconv -f "$fromcode" -t "UTF-8" "$c" > "$c.conv"
        mv "$c.conv" "$c"
    fi
done

%build
%make_build

%install
%make_install

%files
%attr(755,root,root) %{_bindir}/calendar
%{_mandir}/man1/calendar.1.gz
%{_datadir}/calendar

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.37-10.20240528cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.37-9.20240528cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue May 28 2024 David Cantrell <dcantrell@redhat.com> - 1.37-8.20240528cvs
- Upgrade to calendar(1) from OpenBSD 7.5

* Thu Mar 28 2024 Evan Goode <egoode@redhat.com> - 1.37-7.20240209cvs
- Bump release to stay newer than Fedora 37 package

* Fri Feb 09 2024 David Cantrell <dcantrell@redhat.com> - 1.37-6.20240209cvs
- Upgrade to calendar(1) from OpenBSD 7.4
- Use non-deprecated syntax for the %%patch macro

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.37-5.20221115cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.37-4.20221115cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.37-3.20221115cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.37-2.20221115cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 15 2022 David Cantrell <dcantrell@redhat.com> - 1.37-20221115cvs
- Upgrade to calendar(1) from OpenBSD 7.2
- Use SPDX license expression in the License tag

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.37-7.20211220cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.37-6.20211220cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 20 2021 David Cantrell <dcantrell@redhat.com> - 1.37-20211220cvs
- Upgrade to calendar(1) from OpenBSD 7.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.37-4.20200430cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.37-3.20200430cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.37-2.20200430cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 30 2020 David Cantrell <dcantrell@redhat.com> - 1.37-1.20200430cvs
- Upgrade to calendar(1) from OpenBSD 6.6
- Include missing calendar data files (#1809218)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.37-2.20190827cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 27 2019 David Cantrell <dcantrell@redhat.com> - 1.37-1.20190827cvs
- Upgrade to calendar(1) from OpenBSD 6.5
- Correct translation filenames in Makefile.linux

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.35-4.20190227cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 07 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.35-2.20190227cvs
- Fix downgradepath

* Wed Feb 27 2019 David Cantrell <dcantrell@redhat.com> - 1.35-1.20190227cvs
- Upgrade to calendar-1.35 from OpenBSD 6.4
- Fix path to 'cpp' in pathnames.h (#1653311)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.35-2.20180719cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 David Cantrell <dcantrell@redhat.com> - 1.35-1.20180719cvs
- Upgrade to calendar-1.35 from OpenBSD 6.3

* Thu Jul 19 2018 David Cantrell <dcantrell@redhat.com> - 1.28-10.20140613cvs
- BR gcc per https://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-9.20140613cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-8.20140613cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-7.20140613cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-6.20140613cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-5.20140613cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-4.20140613cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.28-3.20140613cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.28-2.20140613cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 David Cantrell <dcantrell@redhat.com> - 1.28-1.20140613cvs
- Rebase to the version of 'calendar' from OpenBSD 5.5

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26-8.20110531cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26-7.20110531cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26-6.20110531cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26-5.20110531cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26-4.20110531cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 02 2011 David Cantrell <dcantrell@redhat.com> - 1.26-3.20110531cvs
- Must increment release number regardless of cvstag

* Tue May 31 2011 David Cantrell <dcantrell@redhat.com> - 1.26-1.20110531cvs
- Upgraded to calendar source from OpenBSD 4.9 (corrects two dates)
- Require cpp (#708609)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26-2.20110115cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 15 2011 David Cantrell <dcantrell@redhat.com> - 1.26-1.20110115cvs
- Upgraded to calendar source from OpenBSD 4.8

* Fri May 21 2010 David Cantrell <dcantrell@redhat.com> - 1.25-10.20091114cvs
- Do not use RPM macros for basic commands in the spec file

* Wed Feb 24 2010 David Cantrell <dcantrell@redhat.com> - 1.25-9.20091114cvs
- Add missing parens around srandom() and random() calls

* Sat Nov 14 2009 David Cantrell <dcantrell@redhat.com> - 1.25-8.20091114cvs
- Upgraded to calendar snapshot from OpenBSD 4.6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 09 2009 David Cantrell <dcantrell@redhat.com> - 1.25-6
- Honor RPM_OPT_FLAGS and fix debuginfo (#494717)

* Tue Mar 03 2009 David Cantrell <dcantrell@redhat.com> - 1.25-5
- Convert output to locale's character coding

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 17 2009 David Cantrell <dcantrell@redhat.com> - 1.25-3
- Use cvs status to get the revision number of calendar.c

* Tue Feb 17 2009 David Cantrell <dcantrell@redhat.com> - 1.25-2
- Fixed problems in export-calendar-source.sh
- Set permissions on export-calendar-source.sh to 0644

* Thu Feb 12 2009 David Cantrell <dcantrell@redhat.com> - 1.25-1
- Packaged OpenBSD's calendar(1) command from OpenBSD 4.4
