Summary:	Macros to process XSL formatting objects
Name:		passivetex
Version:	1.25
Release:  41%{?dist}
License:	MIT
URL: https://github.com/sebastianrahtz/passivetex
Source0:	https://github.com/sebastianrahtz/passivetex/archive/master.zip
#Fix leader length.
Patch0:		passivetex-1.21-leader.patch
BuildArch:	noarch
Requires: tex(latex)
Requires(post): tex(latex)
Requires:	tex(xmltex.tex)
BuildRequires: tex(latex)

%description
PassiveTeX is a library of TeX macros which can be used to process an
XML document which results from an XSL transformation to formatting
objects.


%prep
%setup -q -n %{name}-master
%patch -P0 -p1 -b .leader

%install
rm -rf $RPM_BUILD_ROOT
install -m 0755 -p -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/xmltex/passivetex
install -m 0644 -p *.sty *.xmt $RPM_BUILD_ROOT%{_datadir}/texmf/tex/xmltex/passivetex

%build

%post
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null || :
/usr/bin/env - PATH=$PATH:%{_bindir} fmtutil-sys --all > /dev/null 2>&1
exit 0

%postun
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null || :
%{_bindir}/env - PATH=$PATH:%{_bindir} fmtutil-sys --all > /dev/null 2>&1
exit 0

%triggerin -- tetex-latex
%{_bindir}/env - PATH=$PATH:%{_bindir} fmtutil-sys --all > /dev/null 2>&1
exit 0

%files
%doc README.passivetex LICENSE
%{_datadir}/texmf/tex/xmltex/passivetex

%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 04 2018 Than Ngo <than@redhat.com> - 1.25-25
- update url and source
- update license

* Wed May 23 2018 Troy Dawson <tdawson@redhat.com> - 1.25-24
- Update xmltex Requirements to newer format

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 15 2010 Ondrej Vasik <ovasik@redhat.com> - 1.25-12
- change URL to webarchives - to have something reachable,
  old page probably dead

* Mon Dec 14 2009 Ondrej Vasik <ovasik@redhat.com> - 1.25-11
- Merge Review(#226231): Fixed sources, license, buildroot,
  added build section

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 20 2008 Ondrej Vasik <ovasik@redhat.com> - 1.25-8
- changes because of xmltex migration to texlive

* Thu Jan 31 2008 Jeremy Katz <katzj@redhat.com> - 1.25-7
- Ensure xmltex is installed first to avoid infinite loop during installation

* Fri Jan  4 2008 Ondrej Vasik <ovasik@redhat.com> - 1.25-6
- added doc files
- used texconfig-sys rehash instead of texhash
- dist tag, license tag, rpmlint silencing

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.25-5.1.1
- rebuild

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Mar  2 2005 Tim Waugh <twaugh@redhat.com> 1.25-5
- Use fmtutil-sys instead of fmtutil (bug #150089).

* Wed Mar  2 2005 Tim Waugh <twaugh@redhat.com> 1.25-4
- Rebuild for new teTeX.

* Wed Sep 22 2004 Than Ngo <than@redhat.com> 1.25-3
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Jan 16 2004 Tim Waugh <twaugh@redhat.com> 1.25-1
- 1.25.

* Fri Jul  4 2003 Tim Waugh <twaugh@redhat.com> 1.24-2.1
- Rebuilt.

* Fri Jul  4 2003 Tim Waugh <twaugh@redhat.com> 1.24-2
- URL changed (bug #97838).

* Thu May  9 2003 Tim Waugh <twaugh@redhat.com> 1.24-1
- 1.24.

* Thu Mar  6 2003 Tim Waugh <twaugh@redhat.com> 1.23-1
- 1.23.

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Oct 16 2002 Tim Waugh <twaugh@redhat.com> 1.21-1
- 1.21.
- Fix leader length.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Feb 21 2002 Tim Waugh <twaugh@redhat.com> 1.12-3
- Fix group (bug #60178).

* Thu Feb 21 2002 Tim Waugh <twaugh@redhat.com> 1.12-2
- Rebuild in new environment.

* Tue Feb 12 2002 Tim Waugh <twaugh@redhat.com> 1.12-1
- New tarball.
- DEBUg and euro patches no longer required.

* Thu Jan 10 2002 Tim Waugh <twaugh@redhat.com> 1.11-5
- New tarball.
- Fix euro support.

* Wed Jan 09 2002 Tim Powers <timp@redhat.com> 1.11-4
- automated rebuild

* Thu Dec 13 2001 Tim Waugh <twaugh@redhat.com> 1.11-3
- Fix a typo in fotex.sty.

* Wed Dec 12 2001 Tim Waugh <twaugh@redhat.com> 1.11-2
- Trigger recreation of the format file on tetex-latex.

* Fri Dec  7 2001 Tim Waugh <twaugh@redhat.com> 1.11-1
- New upstream release.  Incorporates the body-start() fix.

* Sat Oct  6 2001 Tim Waugh <twaugh@redhat.com> 1.6-2
- New archive from Sebastian.
- Run fmtutil in %%post and %%postun.
- Require new xmltex.
- Fix body-start().

* Sat Oct  6 2001 Tim Waugh <twaugh@redhat.com> 1.6-1
- Built for Red Hat Linux.  Package from PLD.

* Sat Oct  6 2001 PLD Team <pld-list@pld.org.pl>
All persons listed below can be reached at <cvs_login>@pld.org.pl

$Log: passivetex.spec,v $
Revision 1.22  2010/02/15 11:33:50  ovasik
 change URL to webarchives - to have something reachable,old page probably dead

Revision 1.8  2001/08/21 10:12:42  wrobell
- ver. 1.6
- stb

Revision 1.7  2001/03/27 16:55:44  wiget
Requires xmltex

Revision 1.6  2001/03/27 16:53:29  wiget
changed Source URL, updated to 1.5 version, more files in package; now passivetex is more powerfull and work ;-)

Revision 1.5  2001/01/27 03:25:36  kloczek
- added tetex to Prerq,
- simplified %%post, %%postun.

Revision 1.4  2001/01/27 00:08:39  klakier
- added URL

Revision 1.3  2001/01/27 00:07:47  klakier
- added URL

Revision 1.2  2001/01/24 12:41:17  klakier
- small fixes

Revision 1.1  2001/01/24 12:31:43  klakier
- initial
