Name:          clusterssh
Version:       4.16
Release:       7%{?dist}
%define modname App-ClusterSSH
%define modver v4.16
Summary:       Secure concurrent multiple server terminal control
License:       GPL+ or Artistic
URL:           https://github.com/duncs/clusterssh
Source0:       https://cpan.metacpan.org/authors/id/D/DU/DUNCS/%{modname}-%{version}.tar.gz
BuildArch:     noarch
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:  xterm
# 2016-05-16 attempt to fix rhbz #1025913 (crash w/o fonts)
Requires:  xorg-x11-fonts-75dpi xorg-x11-fonts-100dpi
BuildRequires: fdupes
BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: xterm
BuildRequires: perl(base)
BuildRequires: perl(CPAN::Changes)
BuildRequires: perl(Cwd)
BuildRequires: perl(Data::Dump)
BuildRequires: perl(English)
BuildRequires: perl(Exception::Class)
BuildRequires: perl(Fcntl)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Copy)
BuildRequires: perl(File::Glob)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Slurp)
BuildRequires: perl(File::Temp)
BuildRequires: perl(File::Which)
BuildRequires: perl(FindBin)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(Getopt::Std)
BuildRequires: perl(lib)
BuildRequires: perl(Locale::Maketext)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Module::Load)
BuildRequires: perl(Net::hostent)
BuildRequires: perl(overload)
BuildRequires: perl(Pod::Usage)
BuildRequires: perl(POSIX)
BuildRequires: perl(Readonly)
BuildRequires: perl(Socket)
BuildRequires: perl(Sort::Naturally)
BuildRequires: perl(strict)
BuildRequires: perl(Sys::Hostname)
BuildRequires: perl(Test::Differences)
BuildRequires: perl(Test::DistManifest)
# 2015-12-28 Test::PerlTidy Not available
#BuildRequires: perl(Test::PerlTidy)
BuildRequires: perltidy
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)
BuildRequires: perl(Test::Trap)
BuildRequires: perl(Tk) >= 800.022
BuildRequires: perl(Tk::Dialog)
BuildRequires: perl(Tk::LabEntry)
BuildRequires: perl(Tk::ROText)
BuildRequires: perl(Tk::Xlib)
BuildRequires: perl(Try::Tiny)
BuildRequires: perl(vars)
BuildRequires: perl(version)
BuildRequires: perl(warnings)
BuildRequires: perl(X11::Keysyms)
BuildRequires: perl(X11::Protocol)
BuildRequires: perl(X11::Protocol::Constants)
BuildRequires: perl(X11::Protocol::Other)
BuildRequires: perl(X11::Protocol::WM)
BuildRequires: perl(XML::Simple)

%description
Control multiple terminals open on different servers to perform administration
tasks, for example multiple hosts requiring the same configuration within a 
cluster. Not limited to use with clusters, however.

%prep
%autosetup -n %{modname}-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0

find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
%fdupes %buildroot
%{_fixperms} %{buildroot}
mkdir -p %{buildroot}/%{_sysconfdir}/bash_completion.d
mv  %{buildroot}/%{_bindir}/clusterssh_bash_completion.dist \
        %{buildroot}/%{_sysconfdir}/bash_completion.d/clusterssh

%files
%doc AUTHORS Changes THANKS TODO
%{_bindir}/ccon
%{_bindir}/crsh
%{_bindir}/csftp
%{_bindir}/cssh
%{_bindir}/ctel

%{_sysconfdir}/bash_completion.d
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_privlib}/*

%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 4.16-6
- Perl 5.36 rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 4.16-3
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 17 2020 Filipe Rosset <rosset.filipe@gmail.com> - 4.16-1
- Update to 4.16 fixes rhbz#1849285

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 4.15-2
- Perl 5.32 rebuild

* Tue May 19 2020 Filipe Rosset <rosset.filipe@gmail.com> - 4.15-1
- Update to 4.15 fixes rhbz#1836808

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 22 2019 Filipe Rosset <rosset.filipe@gmail.com> - 4.14-1
- Update to 4.14

* Sun Aug 18 2019 Filipe Rosset <rosset.filipe@gmail.com> - 4.13.2_02-2
- Disable t/boilerplate.t test until upstream fixes
- https://github.com/duncs/clusterssh/issues/122

* Sun Aug 18 2019 Filipe Rosset <rosset.filipe@gmail.com> - 4.13.2_02-1
- Update to new upstream release v4.13.2_02
- https://github.com/duncs/clusterssh/blob/v4.13.2_02/Changes
- Remove upstreamed patch

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.13.2-6
- Perl 5.30 rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 4.13.2-3
- Perl 5.28 rebuild

* Tue Jun 05 2018 Jitka Plesnikova <jplesnik@redhat.com> - 4.13.2-2
- Specify all dependencies, fixes rhbz #1584576

* Sun Mar 25 2018 Filipe Rosset <rosset.filipe@gmail.com> - 4.13.2-1
- Updated to new 4.13.2 upstream version, fixes rhbz #1528726

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.09-2
- Perl 5.26 rebuild

* Mon Mar 13 2017 Filipe Rosset <rosset.filipe@gmail.com> - 4.09-1
- Updated to new 4.09 upstream version, fixes rhbz #1431337

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 02 2016 Filipe Rosset <rosset.filipe@gmail.com> - 4.08-1
- Updated to new 4.08 upstream version, fixes rhbz #1386433
- Added perl(X11::Protocol::Other) as BR + attempt to fix rhbz #1349177

* Thu May 19 2016 Jitka Plesnikova <jplesnik@redhat.com> - 4.07-2
- Perl 5.24 re-rebuild of bootstrapped packages

* Mon May 16 2016 Filipe Rosset <rosset.filipe@gmail.com> - 4.07-1
- Updated to new 4.07 upstream version, attempt to fix rhbz #1025913

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 4.05-3
- Perl 5.24 rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 28 2015 Mark Chappell <tremble@tremble.org.uk> - 4.05-1
- Upstream update
- Move to Build.PL (Makefile.PL is broken)
- Use correct perl dependency syntax
- Include bash completion scripts
- Correct Licence flag ( add or Artistic )
- Add tests

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.02.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.02.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Feb 22 2014 Filipe Rosset <rosset.filipe@gmail.com> - 4.02.03-1
- Updated to new 4.02.03 upstream version

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.02.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 4.02.01-3
- Perl 5.18 rebuild

* Sun Jul 07 2013 Filipe Rosset <rosset.filipe@gmail.com> - 4.02.01-2
- Added required perl-version package

* Sun Jul 07 2013 Filipe Rosset <rosset.filipe@gmail.com> - 4.02.01-1
- Updated to new 4.02_01 upstream version

* Fri Feb 15 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 3.28-8
- add perl-Pod-Checker as BR to fix the build failure
- podchecker has moved from perl-Pod-Parser to above package

* Fri Feb 15 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 3.28-7
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.28-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 17 2010 Filipe Rosset <filiperosset@fedoraproject.org> - 3.28-2
- Updated to upstream version 3.28

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 19 2009 Patrick "Jima" Laughton <jima@beer.tclug.org> 3.26-1
- Much newer upstream version
- Add dependency on xterm (BZ#506909)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 24 2008 Patrick "Jima" Laughton <jima@beer.tclug.org> 3.22-1
- New upstream version

* Tue Sep 18 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 3.19.1-3
- License clarification
- Switch back to unmodified, upstream-provided tarball

* Tue Aug 15 2006 Duncan Ferguson <duncan_ferguson@users.sf.net> - 3.19.1-2
- Tidyups as per https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=199173

* Mon Jul 24 2006 Duncan Ferguson <duncan_ferguson@users.sf.net> - 3.19.1-1
- Update Changelog, commit all branch changes and release

* Tue Jul 18 2006 Duncan Ferguson <duncan_ferguson@users.sf.net> - 3.18.2.10-2
- Correct download URL (Source0)

* Mon Jul 17 2006 Duncan Ferguson <duncan_ferguson@users.sf.net> - 3.18.2.10-1
- Lots of amendments and fixes to clusterssh code
- Added icons and desktop file
- Submitted to Fedora Extras for review

* Mon Nov 28 2005 Duncan Ferguson <duncan_ferguson@users.sf.net> - 3.18.1-1
- Updates and bugfixes to cssh
- Updates to man page
- Re-engineer spec file

* Tue Aug 30 2005 Duncan Ferguson <duncan_ferguson@users.sf.net> - 3.17.1-2
- spec file tidyups

* Mon Apr 25 2005 Duncan Ferguson <duncan_ferguson@users.sf.net> - 3.0
- Please see ChangeLog in documentation area

