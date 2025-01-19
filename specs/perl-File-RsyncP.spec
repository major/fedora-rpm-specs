Name:       perl-File-RsyncP
Version:    0.76
Release:    19%{?dist}
Summary:    A perl implementation of an Rsync client
# https://fedoraproject.org/wiki/Licensing:FAQ?rd=Licensing/FAQ#What_about_the_RSA_license_on_their_MD5_implementation.3F_Isn.27t_that_GPL-incompatible.3F
License:    GPL-2.0-only AND GPL-3.0-only AND ( GPL-1.0-or-later OR Artistic-1.0-Perl )
URL:        https://metacpan.org/release/File-RsyncP
Source0:    https://cpan.metacpan.org/authors/id/C/CB/CBARRATT/File-RsyncP-%{version}.tar.gz
# Adapt a configure check to GCC 12, bug #2046804, CPAN RT#141822
Patch0:     File-RsyncP-0.76-Fix-configure-check-with-optimizing-and-lto-enabled-.patch
Patch1:     perl-File-RsyncP-configure-c99.patch
# Build
BuildRequires: coreutils
BuildRequires: findutils
BuildRequires: gcc
BuildRequires: make
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires: perl(AutoLoader)
BuildRequires: perl(Config)
BuildRequires: perl(constant)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(DynaLoader)
BuildRequires: perl(Encode)
BuildRequires: perl(Exporter)
BuildRequires: perl(Fcntl)
BuildRequires: perl(File::Path)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(Socket)
BuildRequires: perl(strict)
BuildRequires: perl(vars)
# Tests only
# nothing

%description
File::RsyncP is a perl implementation of an Rsync client. It is compatible with
Rsync 2.5.5 - 2.6.3 (protocol versions 26-28). It can send or receive files,
either by running rsync on the remote machine, or connecting to an rsyncd
daemon on the remote machine.

%prep
%autosetup -p1 -n File-RsyncP-%{version}
# Update config.guess/sub to fix builds on new architectures (aarch64/ppc64le)
cp /usr/lib/rpm/redhat/config.* FileList/

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
make %{?_smp_flags}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -a -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/File/
%{perl_vendorarch}/auto/File/
%{_mandir}/man3/File*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.76-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.76-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.76-17
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.76-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.76-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Florian Weimer <fweimer@redhat.com> - 0.76-14
- Further C compatibility fix

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.76-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.76-12
- Perl 5.38 rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.76-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Florian Weimer <fweimer@redhat.com> - 0.76-10
- Port configure script to C99

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.76-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.76-8
- Perl 5.36 rebuild

* Tue Mar 22 2022 Adam Williamson <awilliam@redhat.com> - 0.76-7
- Rebuild with no changes to fix update mess on F36

* Fri Mar 18 2022 Petr Pisar <ppisar@redhat.com> - 0.76-6
- Adapt a configure check to GCC 12 (bug #2046804)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.76-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.76-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.76-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.76-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 29 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.76-1
- 0.76 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.74-19
- Perl 5.32 rebuild

* Mon Jun 08 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.74-18
- Fix path to config.{guess,sub} (bz#1843864)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.74-15
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.74-12
- Perl 5.28 rebuild

* Mon Feb 19 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.74-11
- Add build-require gcc

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.74-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.74-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.74-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.74-2
- Perl 5.22 rebuild

* Tue Feb 03 2015 Petr Šabata <contyk@redhat.com> - 0.74-1
- 0.74 bump
- Minor license change
- Corrected the License tag

* Mon Jan 12 2015 Petr Šabata <contyk@redhat.com> - 0.72-1
- 0.72 bump; fix stalled transfers (#1177212)

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.70-13
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.70-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.70-11
- Update config.guess/sub for aarch64/ppc64le

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.70-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.70-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.70-8
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.70-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.70-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.70-5
- Perl 5.16 rebuild
- Specify all dependencies

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.70-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 23 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.70-3
- Own vendor_perl/File dirs.

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.70-2
- Perl mass rebuild

* Tue Apr 05 2011 Petr Sabata <psabata@redhat.com> - 0.70-1
- 0.70 bump
- Utilizing parallel make
- Removing obsolete Buildroot stuff

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.68-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.68-9
- 661697 rebuild for fixing problems with vendorach/lib

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.68-8
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.68-7
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.68-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.68-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.68-4
Rebuild for new perl

* Tue Feb 12 2008 Mike McGrath <mmcgrath@redhat.com> - 0.68-3
- Rebuild for gcc43

* Mon Oct 15 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.68-2.1
- add BR: perl(ExtUtils::MakeMaker)

* Wed Aug 22 2007 Mike McGrath <mmcgrath@redhat.com> - 0.68-2
- Rebuild for BuildID
- License change

* Mon Jun 04 2007 Mike McGrath <mmcgrath@redhat.com> - 0.68-1
- Upstream released new version

* Sun Sep 10 2006 Mike McGrath <imlinux@gmail.com> - 0.62-2
- Rebuild

* Fri Jul 21 2006 Mike McGrath <imlinux@gmail.com> - 0.62-2
- Fixed whitespace issue and removed SMP flags on make

* Thu Jul 20 2006 Mike McGrath <imlinux@gmail.com> - 0.62-1
- Updated to 0.62 and applied two known patches

* Thu Jul 20 2006 Mike McGrath <imlinux@gmail.com> - 0.52-1
- Initial Fedora Packaging
