Summary: A spam filter for Usenet news servers
Name: cleanfeed
Version: 20020501
Release: 34%{?dist}
# Confirmed with upstream, website
License: Artistic-2.0
URL: http://www.bofh.it/~md/cleanfeed/
Source0: http://www.bofh.it/~md/cleanfeed/cleanfeed-20020501.tgz
Patch0: cleanfeed-20020501-redhat.patch
Patch1: cleanfeed-20020501-ro.patch
BuildArch: noarch
BuildRequires: perl-generators
BuildRequires: sed
Requires(pre): shadow-utils

%description
Cleanfeed is an automatic spam filter for Usenet news servers and
routers (INN, Cyclone, Typhoon, Breeze and NNTPRelay).  Cleanfeed
looks for duplicated messages, repeated patterns, and known spamming
sites and domains.  It can be configured to block binary posts to
non-binary newsgroups, to cancel already-rejected articles, and to
reject some spamming from local users.

Install the cleanfeed package if you need a spam filter for a Usenet
news server.

%prep
%setup -q
%patch -P0 -p1 -b .rh
%patch -P1 -p1

%build
sed '1 i #!/usr/bin/perl' cleanfeed > filter_innd.pl

%pre
getent group news >/dev/null || groupadd -r news
getent passwd news >/dev/null || \
    useradd -r -g news -d %{_sysconfdir}/news -s /sbin/nologin \
    -c "cleanfeed user" news
exit 0

%install
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/news
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/news/bin/filter
install -m 0644 cleanfeed.local.sample $RPM_BUILD_ROOT/%{_sysconfdir}/news/cleanfeed.local
install -m 0644 bad_* $RPM_BUILD_ROOT/%{_sysconfdir}/news/
install -m 0755 filter_innd.pl \
	$RPM_BUILD_ROOT/%{_datadir}/news/bin/filter/filter_innd.pl

%files
%license LICENSE
%doc CHANGES README HACKING TODO
%attr(-,news,news) %config(noreplace)  %{_sysconfdir}/news/cleanfeed.local
%attr(-,news,news) %config(noreplace)  %{_sysconfdir}/news/bad_*
%attr(755,news,news) %dir %{_datadir}/news/bin/filter
%attr(-,news,news) %{_datadir}/news/bin/filter/filter_innd.pl

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20020501-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20020501-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Apr 20 2024 Miroslav Suchý <msuchy@redhat.com> - 20020501-32
- convert license to SPDX

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20020501-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20020501-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20020501-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20020501-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20020501-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20020501-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20020501-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20020501-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20020501-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20020501-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20020501-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20020501-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20020501-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20020501-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20020501-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20020501-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20020501-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20020501-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Feb 12 2015 Dominik Mierzejewski <rpm@greysector.net> - 20020501-12
- clean up spec file
- add sed to BR

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20020501-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20020501-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 20020501-10
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20020501-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20020501-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 20 2012 Roman Rakus <rrakus@redhat.com> - 20020501-7
- create user and group if needed
  Resolves: #786940

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20020501-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20020501-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 23 2010 Roman Rakus <rrakus@redhat.com> - 20020501-4
- Merge Review changes (#225645)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20020501-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20020501-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Aug  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 20020501-1
- update to 20020501
- fix license tag

* Wed Jul 23 2008 Roman Rakus <rrakus@redhat.com> - 0.95.7b-23
- Mark config file cleanfeed.conf as noreplace

* Mon Jun 16 2008 Roman Rakus <rrakus@redhat.com> - 0.95.7b-22
- Added dist to release tag

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.95.7b-21.1.1
- rebuild

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Sep 21 2004 Than Ngo <than@redhat.com> 0.95.7b-21
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Nov 19 2002 Tim Powers <timp@redhat.com>
- rebuild in current collinst

* Mon Jul 29 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- adjust dir perms #70016

* Tue Jul 23 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- adjust path for newest inn package

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Jun 18 2001 Nalin Dahyabhai <nalin@redhat.com>
- move buildroot to %%{_tmppath}
- s/Copyright:/License:/
- rebuild in new environment to get perl requirements

* Wed May 09 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- fix ro-variable bug #39228

* Sun Aug  6 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- add dir /usr/bin/filter/ with perms like in inn

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jun 18 2000 Matt Wilson <msw@redhat.com>
- use %%{_mandir}
- buildable as non-root

* Thu Mar 02 2000 Cristian Gafton <gafton@redhat.com>
- fix location to match inn-2.2.2 in /usr/bin/filter

* Thu Feb 03 2000 Cristian Gafton <gafton@redhat.com>
- fix description
- man pages are compressed

* Tue Aug 10 1999 Cristian Gafton <gafton@redhat.com>
- don't require perl-MD5 anymore (that was merged in the main perl package)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Thu Jan 21 1999 Bill Nottingham <notting@redhat.com>
- build for 6.0

* Thu Sep 03 1998 Cristian Gafton <gafton@redhat.com>
- update to 0.95.7b

* Fri May 01 1998 Cristian Gafton <gafton@redhat.com>
- spec file cleanups
- patch to get rod of /usr/local/bin/perl

* Mon Apr 13 1998 Bryan C. Andregg <bandregg@redhat.com>
- first package

