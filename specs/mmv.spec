Name:		mmv
Version:	2.9.1
Release:	2%{?dist}
Summary:	Move/copy/link multiple files

License:	GPL-3.0-or-later
URL:		https://github.com/rrthomas/mmv
Source0:	https://github.com/rrthomas/mmv/releases/download/v%{version}/mmv-%{version}.tar.gz
BuildRequires:	make gcc gc-devel

%description
This is mmv, a program to move/copy/append/link multiple files
according to a set of wildcard patterns. This multiple action is
performed safely, i.e. without any unexpected deletion of files due to
collisions of target names with existing filenames or with other
target names. Furthermore, before doing anything, mmv attempts to
detect any errors that would result from the entire set of actions
specified and gives the user the choice of either aborting before
beginning, or proceeding by avoiding the offending parts.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install
ln -s mmv.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/mcp.1.gz
ln -s mmv.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/mln.1.gz
ln -s mmv.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/mad.1.gz

%check
make check

%files
%license COPYING
%doc ChangeLog README README.md
%{_bindir}/mmv
%{_bindir}/mcp
%{_bindir}/mln
%{_bindir}/mad
%{_mandir}/man1/*.1*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 08 2024 Jens Kuehnel <JensKuehnel@users.noreply.github.com> - 2.9.1-1
- release 2.9.1
- fixes setuid call as marked by rpmlint

* Sun Oct 06 2024 Jens Kuehnel <JensKuehnel@users.noreply.github.com> - 2.8-1
- release 2.8

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Feb 09 2024 Jens Kuehnel <JensKuehnel@users.noreply.github.com> - 2.6-1
- release 2.6
- readded the mad command

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 21 2023 Jens Kuehnel <bugzilla-redhat@jens.kuehnel.org> - 2.5.1-1
- upgrade to release 2.5.1 based on fork from Reuben Thomas
- Debian has moved as well and was used a upstream by the previous version of this package
- upstream removed multi append (mad) from project 

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.01b-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.01b-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.01b-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.01b-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.01b-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.01b-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.01b-34
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.01b-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.01b-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.01b-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.01b-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.01b-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.01b-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.01b-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.01b-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.01b-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.01b-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01b-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01b-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01b-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Nov 22 2013 Zing <zing@fastmail.fm> - 1.01b-20
- sync with debian mmv_1.01b-18
-     deb pkg format switch to 3.0
-     format-security fix
-     added diagnostic for directories
-     man page improvements

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01b-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01b-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01b-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01b-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01b-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01b-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun  2 2009 Zing <zing@fastmail.fm> - 1.01b-13
- enable LFS support
- updated changelog and copyright files

* Mon Jun  1 2009 Zing <zing@fastmail.fm> - 1.01b-12
- sync with debian mmv_1.01b-15
-     man page formatting fixes
-     wrap cmdname in basename() (debian: #452989)
-     initialize tv_usec (debian: #452993)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01b-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.01b-10
- Autorebuild for GCC 4.3

* Thu Aug 16 2007 Zing <zing@fastmail.fm> - 1.01b-9
- conform to Fedora Licensing Guidelines

* Fri Sep  8 2006 Zing <zing@fastmail.fm> - 1.01b-8
- fix perms on man page
- rebuild for FE6

* Mon Apr 10 2006 Zing <shishz@hotpop.com> - 1.01b-7
- ok, now fix busted perms on doc directory

* Mon Mar 20 2006 Zing <shishz@hotpop.com> - 1.01b-6
- fix permissions on doc files

* Mon Feb 13 2006 Zing <shishz@hotpop.com> - 1.01b-5
- sync with debian mmv_1.01b-14
- symlink man page for mcp/mad/mln

* Sat Oct  1 2005 Zing <shishz@hotpop.com> - 1.01b-4
- use dist tag

* Sat Oct  1 2005 Zing <shishz@hotpop.com> - 1.01b-3
- cleanup changelog

* Wed Sep 28 2005 Zing <shishz@hotpop.com> - 1.01b-2
- don't change source name
- symlink mcp/mad/mln 

* Tue Aug 23 2005 Zing <shishz@hotpop.com> - 1.01b-1
- initial RPM release
- pull from debian mmv_1.01b-12.2
- build executable as a PIE
