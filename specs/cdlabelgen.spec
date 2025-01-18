Name: cdlabelgen
Summary: Generates frontcards and traycards for inserting in CD jewelcases
Version: 4.3.0
Release: 23%{?dist}
Source: http://www.aczoom.com/pub/tools/cdlabelgen-%{version}.tgz
URL: http://www.aczoom.com/tools/cdinsert/
# Automatically converted from old format: BSD with advertising - review is highly recommended.
License: LicenseRef-Callaway-BSD-with-advertising
BuildArch: noarch
BuildRequires: perl-generators

%description
Cdlabelgen is a utility which generates frontcards and traycards (in
PostScript(TM) format) for CD jewelcases.

%prep
%setup -q
iconv -f iso8859-1 -t utf8 ChangeLog > ChangeLog.utf8 && \
touch -r ChangeLog ChangeLog.utf8 && \
mv ChangeLog.utf8 ChangeLog

%build
# nothing to build

%install
mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/cdlabelgen,%{_mandir}/man1}
install -pm755 cdlabelgen $RPM_BUILD_ROOT%{_bindir}/
install -pm644 postscript/* $RPM_BUILD_ROOT%{_datadir}/cdlabelgen/
install -pm644 cdlabelgen.1 $RPM_BUILD_ROOT%{_mandir}/man1/

%files
%doc ChangeLog README cdlabelgen.html
%{_bindir}/cdlabelgen
%{_datadir}/cdlabelgen/
%{_mandir}/man1/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 4.3.0-22
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 05 2014 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 4.3.0-1
- update to 4.3.0
- drop obsolete specfile parts

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 4.2.0-3
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 25 2012 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 4.2.0-1
- updated to 4.2.0

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 30 2008 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 4.1.0-1
- updated to 4.1.0
- fixed rpmlint warnings

* Thu Sep 06 2007 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 4.0.0-1
- updated to 4.0.0
- preserve timestamps upon install

* Fri Aug 17 2007 Harald Hoyer <harald@rawhide.home> - 3.6.0-2
- changed License tag to BSD with advertising

* Thu Sep 21 2006 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 3.6.0-1
- update to 3.6.0
- mass rebuild

* Thu Jul 21 2005 Matthias Saou <http://freshrpms.net/> 3.5.0-1
- Update to 3.5.0.
- Update URL and Source to new locations.

* Tue Sep 21 2004 Harald Hoyer <harald@redhat.com> 3.0.0
- Updated to new version 3.0.0

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Oct 08 2003 Harald Hoyer <harald@redhat.com> 2.6.1-1
- Updated to new version 2.6.1

* Thu May 22 2003 Harald Hoyer <harald@redhat.com> 2.6.0-1
- Updated to new version 2.6.0

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Oct  7 2002 Mike A. Harris <mharris@redhat.com> 2.3.0-4
- All-arch rebuild

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 2.3.0-3
- automated rebuild

* Sun May 26 2002 Tim Powers <timp@redhat.com> 2.3.0-2
- automated rebuild

* Tue Feb 26 2002 Mike A. Harris <mharris@redhat.com> 2.3.0-1
- Updated to new version 2.3.0 by different author

* Tue Feb 26 2002 Mike A. Harris <mharris@redhat.com> 1.5.0-11
- s/Copyright/License/ tag
- fixed buildroot tag to point to _tmppath
- Rebuilt in new environment

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon May 21 2001 Tim Powers <timp@redhat.com>
- built for the distro

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Mon Jul 10 2000 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Jun 5 2000 Tim Powers <timp@redhat.com>
- fix man page location

* Mon May 8 2000 Tim Powers <timp@redhat.com>
- rebuilt for 7.0

* Tue Jan 4 2000 Tim Powers <timp@redhat.com>
- removed unneeded defines
- rebuilt for 6.2

* Mon Aug 23 1999 Preston Brown <pbrown@redhat.com>
- adopted for Powertools 6.1.

