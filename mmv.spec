Name:		mmv
Version:	1.01b
Release:	39%{?dist}
Summary:	Move/copy/append/link multiple files

License:	GPL+
URL:		http://packages.qa.debian.org/m/mmv.html
Source0:	http://ftp.debian.org/debian/pool/main/m/mmv/mmv_1.01b.orig.tar.gz
Source1:	copyright
Source2:	changelog
Patch0:		mmv-debian-patches-as-of-mmv-1.01b-15.patch
Patch1:		mmv-debian-man-page-fixes.patch
Patch2:		mmv-debian-format-security.patch
Patch3:		mmv-debian-better-diagnostics-for-directories-584850.patch
Patch4:		mmv-debian-man-page-examples.patch
Patch5:		mmv-debian-man-page-warning-149873.patch
Patch6:		mmv-1.01b-makefile.patch

BuildRequires: make
BuildRequires:  gcc
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
%setup -q -n mmv-1.01b.orig
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
cp -p %{SOURCE1} . 
cp -p %{SOURCE2} .

%build
make CONF="$RPM_OPT_FLAGS -fpie $(getconf LFS_CFLAGS)" LDCONF="-pie" %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
ln -s mmv $RPM_BUILD_ROOT/%{_bindir}/mcp
ln -s mmv $RPM_BUILD_ROOT/%{_bindir}/mad
ln -s mmv $RPM_BUILD_ROOT/%{_bindir}/mln
ln -s mmv.1.gz $RPM_BUILD_ROOT/%{_mandir}/man1/mcp.1.gz
ln -s mmv.1.gz $RPM_BUILD_ROOT/%{_mandir}/man1/mad.1.gz
ln -s mmv.1.gz $RPM_BUILD_ROOT/%{_mandir}/man1/mln.1.gz

%files
%doc copyright changelog
%defattr(-,root,root,-)
%doc ANNOUNCE ARTICLE READ.ME
%{_bindir}/mmv
%{_bindir}/mcp
%{_bindir}/mad
%{_bindir}/mln
%{_mandir}/man1/*

%changelog
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
