%global cpan_version 0.9914
Name:           perl-CPANPLUS
Version:        0.991.400
Release:        11%{?dist}
Summary:        Ameliorated interface to the Comprehensive Perl Archive Network
# Other files:                              GPL-1.0-or-later OR Artistic-1.0-Perl
## Unbundled, not used
# inc/bundle/Locale/Maketext/Simple.pm:     MIT
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CPANPLUS
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/CPANPLUS-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(Locale::Maketext::Simple)
BuildRequires:  perl(Module::Loaded)
# Run-time:
BuildRequires:  perl(Archive::Extract)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBIx::Simple)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Fetch)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Unix)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Log::Message)
BuildRequires:  perl(Module::CoreList) >= 2.22
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(Module::Load::Conditional)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Object::Accessor)
BuildRequires:  perl(overload)
BuildRequires:  perl(Package::Constants)
BuildRequires:  perl(Params::Check)
# Parse::CPAN::Meta also for loading t/testrules.yml at tests
BuildRequires:  perl(Parse::CPAN::Meta)
BuildRequires:  perl(strict)
BuildRequires:  perl(Term::ReadLine)
BuildRequires:  perl(Term::UI)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More)
# lib/CPANPLUS/Internals.pm:465
Requires:       perl(File::Glob)
# File::Path not found in lib/CPANPLUS/Internals/Utils.pm:68 and
# generated from lib/CPANPLUS/Internals/Extract.pm
# lib/CPANPLUS/Internals/Utils.pm:323
Requires:       perl(File::stat)
# bin/cpanp-boxed:10
Requires:       perl(FindBin)
# lib/CPANPLUS/Module.pm:477
Requires:       perl(Module::CoreList) >= 2.22
# lib/CPANPLUS/Configure.pm:181
Requires:       perl(Module::Pluggable)

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Your::Module::Here|Test)\\)

%description
The CPANPLUS library is an API to the CPAN mirrors and a collection of
interactive shells, command line programs, etc., that use this API.

%prep
%setup -q -n CPANPLUS-%{cpan_version}
# Removed unused bootstrap modules (required only when updating CPANPLUS with
# CPANPLUS when Module::Build is preferred by CPANPLUS)
rm -rf bundled
perl -i -ne 'print $_ unless m{^bundled/}' MANIFEST
# Remove bundled modules
rm -rf inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
export HARNESS_OPTIONS=$(perl -e \
    'for (@ARGV) { $j=$1 if m/\A-j(\d+)\z/; }; print "j$j" if $j' -- \
    %{?_smp_mflags})
make test

%files
%doc ChangeLog README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.991.400-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.991.400-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.991.400-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.991.400-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.991.400-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.991.400-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 15 2022 Michal Josef Špaček <mspacek@redhat.com> - 0.991.400-5
- Update license to SPDX format

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.991.400-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.991.400-3
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.991.400-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 05 2022 Michal Josef Špaček <mspacek@redhat.com> - 0.991.400-1
- 0.9914 bump

* Mon Aug 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.991.200-1
- 0.9912 bump

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.991.000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.991.000-3
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.991.000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 21 2020 Petr Pisar <ppisar@redhat.com> - 0.991.000-1
- 0.9910 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.990.800-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.990.800-2
- Perl 5.32 rebuild

* Tue Apr 14 2020 Petr Pisar <ppisar@redhat.com> - 0.990.800-1
- 0.9908 bump

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.990.600-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Petr Pisar <ppisar@redhat.com> - 0.990.600-1
- 0.9906 bump

* Tue Dec 10 2019 Petr Pisar <ppisar@redhat.com> - 0.990.400-1
- 0.9904 bump

* Fri Nov 29 2019 Petr Pisar <ppisar@redhat.com> - 0.990.200-1
- 0.9902 bump

* Fri Nov 29 2019 Petr Pisar <ppisar@redhat.com> - 0.918.0-1
- 0.9180 bump

* Fri Jul 26 2019 Petr Pisar <ppisar@redhat.com> - 0.917.800-3
- Make parallel testing more reliable (CPAN RT#59085)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.917.800-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Petr Pisar <ppisar@redhat.com> - 0.917.800-1
- 0.9178 bump

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.917.600-7
- Perl 5.30 re-rebuild of bootstrapped packages

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.917.600-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.917.600-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.917.600-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.917.600-3
- Perl 5.28 re-rebuild of bootstrapped packages

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.917.600-2
- Perl 5.28 rebuild

* Thu Jun 07 2018 Petr Pisar <ppisar@redhat.com> - 0.917.600-1
- 0.9176 bump

* Wed May 23 2018 Petr Pisar <ppisar@redhat.com> - 0.917.400-1
- 0.9174 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.917.200-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 11 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.917.200-1
- 0.9172 bump

* Fri Sep 15 2017 Petr Pisar <ppisar@redhat.com> - 0.917.000-1
- 0.9170 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.916.800-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.916.800-3
- Perl 5.26 re-rebuild of bootstrapped packages

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.916.800-2
- Perl 5.26 rebuild

* Mon May 15 2017 Petr Pisar <ppisar@redhat.com> - 0.916.800-1
- 0.9168 bump

* Wed Apr 12 2017 Petr Pisar <ppisar@redhat.com> - 0.916.600-1
- 0.9166 bump

* Fri Mar 03 2017 Petr Pisar <ppisar@redhat.com> - 0.916.400-1
- 0.9164 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.916.200-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 16 2017 Petr Pisar <ppisar@redhat.com> - 0.916.200-1
- 0.9162 bump

* Tue Oct 04 2016 Petr Pisar <ppisar@redhat.com> - 0.91.60-2
- Correct a typo in cpan2dist manual
- Fix a test failing with underscored Cwd version (CPAN RT#116479)

* Fri May 20 2016 Petr Pisar <ppisar@redhat.com> - 0.91.60-1
- 0.9160 bump

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.91.56-4
- Perl 5.24 re-rebuild of bootstrapped packages

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.91.56-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.91.56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 16 2015 Petr Pisar <ppisar@redhat.com> - 0.91.56-1
- 0.9156 bump

* Tue Jul 07 2015 Petr Pisar <ppisar@redhat.com> - 0.91.54-1
- 0.9154 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.91.52-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.91.52-6
- Perl 5.22 re-rebuild of bootstrapped packages

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.91.52-5
- Perl 5.22 rebuild

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.91.52-4
- Perl 5.20 re-rebuild of bootstrapped packages

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.91.52-3
- Perl 5.20 rebuild

* Thu Jun 12 2014 Petr Pisar <ppisar@redhat.com> - 0.91.52-2
- 0.9152 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.91.48-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 04 2014 Petr Pisar <ppisar@redhat.com> - 0.91.48-1
- 0.9148 bump

* Mon Feb 03 2014 Petr Pisar <ppisar@redhat.com> - 0.91.46-1
- 0.9146 bump
- Run tests in parallel

* Wed Dec 11 2013 Petr Pisar <ppisar@redhat.com> - 0.91.44-1
- 0.9144 bump

* Mon Aug 26 2013 Petr Pisar <ppisar@redhat.com> - 0.91.42-1
- 0.9142 bump

* Wed Aug 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.91.40-2
- Perl 5.18 re-rebuild of bootstrapped packages

* Mon Aug 05 2013 Petr Pisar <ppisar@redhat.com> - 0.91.40-1
- 0.9140 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.91.38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 0.91.38-2
- Perl 5.18 rebuild
- Specify all dependencies

* Tue May 21 2013 Petr Pisar <ppisar@redhat.com> - 0.91.38-1
- 0.9138 bump

* Mon Apr 29 2013 Petr Pisar <ppisar@redhat.com> - 0.91.36-1
- 0.9136 bump

* Thu Apr 04 2013 Petr Pisar <ppisar@redhat.com> - 0.91.34-2
- Keep bundled inc::Module::Install modules at boot-strap (bug #947489)

* Thu Jan 24 2013 Petr Pisar <ppisar@redhat.com> 0.91.34-1
- Specfile autogenerated by cpanspec 1.78.
