Name:           rsnapshot
Version:        1.5.1
Release:        1%{?dist}
Summary:        Local and remote filesystem snapshot utility
License:        GPL-2.0-or-later
URL:            https://rsnapshot.org/
Source0:        https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  lvm2
BuildRequires:  make
BuildRequires:  openssh-clients
BuildRequires:  perl-generators
BuildRequires:  rsync
BuildRequires:  %{_bindir}/pod2man

# For running %%check
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DirHandle)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)

Requires:       openssh-clients
Requires:       rsync

%description
This is a remote backup program that uses rsync to take backup snapshots of
filesystems.  It uses hard links to save space on disk.

%prep
%setup -q

%build
%configure \
  --with-perl="%{__perl}" \
  --with-rsync="%{_bindir}/rsync" \
  --with-cp="%{__cp}" \
  --with-rm="%{__rm}" \
  --with-ssh="%{_bindir}/ssh" \
  --with-logger="%{_bindir}/logger" \
  --with-du="%{_bindir}/du"

%install
%make_install

# Rename the installed .default config file to a usable name
mv -f $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf{.default,}

# Reset timestamp of .default config file to pre-%%configure
touch -c -r %{name}.conf.default{.in,} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf

# Change the perms on the utils/ files so rpm doesn't pick up their dependencies
find utils/ -type f -print0 | xargs -r0 chmod 644

%check
%{__make} test

%files
%doc AUTHORS ChangeLog README.md
%license COPYING
%doc %{name}.conf.default utils/
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%{_bindir}/%{name}-diff
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-diff.1*

%changelog
* Sun Feb 09 2025 Robert Scheck <robert@fedoraproject.org> - 1.5.1-1
- Upgrade to 1.5.1 (#2342185)

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 30 2022 Robert Scheck <robert@fedoraproject.org> - 1.4.5-1
- Upgrade to 1.4.5 (#2156839)

* Wed Nov 16 2022 Robert Scheck <robert@fedoraproject.org> - 1.4.4-1
- Upgrade to 1.4.4 (#1974006, thanks to Todd Zullinger)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 31 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.3-3
- Specify all perl dependencies needed for tests

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 11 2019 Robert Scheck <robert@fedoraproject.org> - 1.4.3-1
- Upgrade to 1.4.3 (#1443553, #1646191, #1741427)
- Extend spec file compatibility to cover RHEL/CentOS 6
- Add run-time requirement for perl(Lchown) (#1494775)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 James Hogarth <james.hogarth@gmail.com> - 1.4.2-2
- Backport fix for bz#1388209

* Thu Oct 06 2016 James Hogarth <james.hogarth@gmail.com> - 1.4.2-1
- Update to 1.4.2 and bring spec up to current standards

* Wed Feb 17 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.3.1-16
- Add BR: /usr/bin/pod2man (F24FTBFS, RHBZ#1307997).
- Add %%license.
- Modernize spec.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 10 2013 Steven Roberts <strobert@strobe.net> - 1.3.1-12
- added lvm-quiet patch to correct lvremove handling.  bug 1005911

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.3.1-10
- Perl 5.18 rebuild

* Tue Jul 09 2013 Steven Roberts <strobert@strobe.net> - 1.3.1-9
- fixed invalid changelog dates
- added pod2man patch to deal with missing-back now error in newer fedora

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Sep 06 2009 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.3.1-4
- The include_conf directive doesn't handle backticks as documented.
  This is already fixed upstream in cvs but not in a release yet.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.1-1
- fix license tag
- update to 1.3.1
- remove comment lines (more trouble than they're worth)

* Mon May 28 2007 Chris Petersen <rpm@forevermore.net> 1.3.0-1
- Upgrade to 1.3.0

* Fri Sep  8 2006 Chris Petersen <rpm@forevermore.net> 1.2.9-5
- Rebuild for FC6 glibc update

* Sun Jul 23 2006 Chris Petersen <rpm@forevermore.net> 1.2.9-4
- Bump release number to correspond with fc4.

* Thu May 25 2006 Chris Petersen <rpm@forevermore.net> 1.2.9-2
- Update configfile patch to work with 1.2.9

* Sun May 21 2006 Chris Petersen <rpm@forevermore.net> 1.2.9-1
- Preliminary build for 1.2.9

* Wed May 17 2006 Chris Petersen <rpm@forevermore.net> 1.2.3-2
- Add rsync and openssh-clients build requirements because the configure script checks for them.
- Remove perl requirement because it's detected by rpm.

* Wed May 17 2006 Chris Petersen <rpm@forevermore.net> 1.2.3-1
- Update to version 1.2.3 which is in the downloads directory but not linked on the site.
- Change openssh requirement to openssh-clients
- Update %%post script with better info from the rpmforge spec and nifty logger reports
- Add utils/ to the %%doc files

* Sat May 13 2006 Chris Petersen <rpm@forevermore.net> 1.2.1-1
- Update specfile to be compatible with fedora guidelines

* Sat Jan 29 2005 Nathan Rosenquist <nathan@rsnapshot.org>
- Added upgrade script

* Sat Jan 22 2005 Nathan Rosenquist <nathan@rsnapshot.org>
- Added --with-du option

* Thu Jan 15 2004 Nathan Rosenquist <nathan@rsnapshot.org>
- Added "AutoReqProv: no" for SuSE compatibility

* Fri Dec 26 2003 Nathan Rosenquist <nathan@rsnapshot.org>
- Added util-linux dependency, and --with-logger= option

* Fri Dec 19 2003 Nathan Rosenquist <nathan@rsnapshot.org>
- now fully support autoconf

* Tue Dec 16 2003 Nathan Rosenquist <nathan@rsnapshot.org>
- changed rsnapshot.conf to rsnapshot.conf.default from the source tree

* Wed Nov 05 2003 Nathan Rosenquist <nathan@rsnapshot.org>
- Removed fileutils dependency, added verification info

* Tue Nov 04 2003 Nathan Rosenquist <nathan@rsnapshot.org>
- fixed anonymous rsync error

* Thu Oct 30 2003 Nathan Rosenquist <nathan@rsnapshot.org>
- update to 1.0.3

* Tue Oct 28 2003 Carl Wilhelm Soderstrom <chrome@real-time.com>
- created spec file
