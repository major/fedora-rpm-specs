%if ! (0%{?rhel})
# Perform optional tests
%{bcond_without perl_Module_Install_ReadmeFromPod_enables_optional_test}
# Support output to PDF
%{bcond_without perl_Module_Install_ReadmeFromPod_enables_pdf}
%else
%{bcond_with perl_Module_Install_ReadmeFromPod_enables_optional_test}
%{bcond_with perl_Module_Install_ReadmeFromPod_enables_pdf}
%endif

Name:           perl-Module-Install-ReadmeFromPod
Version:        0.30
Release:        28%{?dist}
Summary:        Module::Install extension to automatically convert POD to a README
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Install-ReadmeFromPod
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Module-Install-ReadmeFromPod-%{version}.tar.gz
# Regenerate README in UTF-8
Patch0:         Module-Install-ReadmeFromPod-0.26-Regenerate-README-in-UTF-8.patch
# Remove a bogus test that fails on PDF binary files randomly, CPAN RT#130221
Patch1:         Module-Install-ReadmeFromPod-0.30-Do-not-test-PDF-file-for-new-lines.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Install::AutoLicense)
BuildRequires:  perl(Module::Install::AuthorRequires) >= 0.02
BuildRequires:  perl(Module::Install::GithubMeta)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(strict)
# Build script uses lib/Module/Install/ReadmeFromPod.pm
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Capture::Tiny) >= 0.05
BuildRequires:  perl(IO::All)
# Module::Install::Base version from Module::Install in Makefile.PL
BuildRequires:  perl(Module::Install::Base) >= 1
BuildRequires:  perl(Pod::Html)
BuildRequires:  perl(Pod::Man)
BuildRequires:  perl(Pod::Markdown) >= 2
BuildRequires:  perl(Pod::Text) >= 3.13
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Optional run-time:
%if %{with perl_Module_Install_ReadmeFromPod_enables_pdf}
BuildRequires:  perl(App::pod2pdf)
%endif
# Tests:
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::InDistDir)
BuildRequires:  perl(Test::More) >= 0.47
%if %{with perl_Module_Install_ReadmeFromPod_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
%endif
%if %{with perl_Module_Install_ReadmeFromPod_enables_pdf}
Suggests:       perl(App::pod2pdf)
%endif
Requires:       perl(Capture::Tiny) >= 0.05
Requires:       perl(IO::All)
# Module::Install::Base version from Module::Install in Makefile.PL
Requires:       perl(Module::Install::Base) >= 1
Requires:       perl(Pod::Html)
Requires:       perl(Pod::Man)
Requires:       perl(Pod::Markdown) >= 2
Requires:       perl(Pod::Text) >= 3.13

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Module::Install::Base\\)$

%description
Module::Install::ReadmeFromPod is a Module::Install extension that
generates a README file automatically from an indicated file containing
POD, whenever the author runs Makefile.PL. Several output formats are
supported: plain-text, HTML, PDF or manual page.

%prep
%setup -q -n Module-Install-ReadmeFromPod-%{version}
%patch -P0 -p1
%patch -P1 -p1
# Remove bundled modules
rm -r inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST
# Drop executable bit from documentation
chmod -x tools/git-log.pl

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README tools
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul  9 2024 Software Management Team <packaging-team-maint@redhat.com> - 0.30-25
- Eliminate use of obsolete %%patchN syntax (rhbz#2283636)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-19
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-16
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-14
- Disable support output to PDF on RHEL

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-12
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jul 29 2019 Petr Pisar <ppisar@redhat.com> - 0.30-10
- Remove a bogus test that fails on PDF binary files randomly (CPAN RT#130221)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-8
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-5
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-2
- Perl 5.26 rebuild

* Mon Feb 20 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-1
- 0.30 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-2
- Perl 5.24 rebuild

* Thu Apr 28 2016 Petr Pisar <ppisar@redhat.com> - 0.26-1
- 0.26 bump

* Tue Apr 26 2016 Petr Pisar <ppisar@redhat.com> - 0.24-1
- 0.24 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-4
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 26 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-1
- 0.22 bump

* Sun Aug 04 2013 Petr Pisar <ppisar@redhat.com> - 0.20-4
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 22 2012 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-1
- 0.20 bump

* Fri Jun 22 2012 Jitka Plesnikova <jplesnik@redhat.com> 0.18-1
- Specfile autogenerated by cpanspec 1.78.
