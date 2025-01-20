Name:      perl-X10
Summary:   Enables Perl to communicate with X10 devices
Version:   0.04
Release:   27%{?dist}
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:   GPL-3.0-only
URL:       https://metacpan.org/release/X10
Source:    https://cpan.metacpan.org/authors/id/R/RO/ROBF/X10-%{version}.tar.gz
Buildarch: noarch

BuildRequires: make
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: findutils

# Needed during build for the perl test
BuildRequires: perl(Astro::SunTime)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(File::Basename)
BuildRequires: perl(FileHandle)
BuildRequires: perl(IO::Socket)
BuildRequires: perl(POSIX)
BuildRequires: perl(Storable)
BuildRequires: perl(strict)
BuildRequires: perl(Time::ParseDate)
BuildRequires: perl(vars)


%description
X10 Perl module for the Firecracker, ActiveHome, and TwoWay/TW523 interfaces.

%prep
%autosetup -n X10-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_build pure_install DESTDIR=%{buildroot}
# older Perls don't support the NO_PACKLIST flag
find %{buildroot} -type f -name .packlist -delete

%{_fixperms} %{buildroot}/*

%check
%make_build test

%files
%doc Changes README TODO
%doc macros.config scheduler.config

%{_mandir}/man1/x10client.1*
%{_mandir}/man1/x10server.1*

%{_bindir}/x10client
%{_bindir}/x10server

%{perl_vendorlib}/X10.pm
%{perl_vendorlib}/X10/

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.04-26
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.04-19
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-17
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.04-16
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.04-13
- Perl 5.32 rebuild

* Mon Mar 16 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.04-12
- Add missing BRs

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.04-9
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.04-6
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.04-3
- Perl 5.26 rebuild

* Thu Feb 02 2017 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.04-2
- Use %%{_fix_perms} macro

* Fri Jan 20 2017 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.04-1
- Update to release 0.04
- Add man pages for executables

* Thu Jan 12 2017 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.03-5
- Additional feedback from bugzilla 1409869

* Tue Jan 03 2017 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.03-4
- bugzilla 1409869 feedback

* Mon Jan 02 2017 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.03-3
- Add perl-generators buildrequires
- Move make test to %%check

* Sun Jan 01 2017 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.03-2
- Update spec file to modern Fedora packaging guidelines 

* Fri Aug 23 2013 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.03-1
- Initial build using cpan2rpm.
