Name:           perl-Devel-CheckOS
Version:        2.04
Release:        3%{?dist}
Summary:        Check what OS we're running on
# Devel/AssertOS/Extending.pod: CC-BY-SA-2.0-UK
# Devel/CheckOS/Families.pod:   CC-BY-SA-2.0-UK
# Other files:  GPL-2.0-only OR Artistic-1.0-Perl
License:        (GPL-2.0-only OR Artistic-1.0-Perl) AND CC-BY-SA-2.0-UK
URL:            https://metacpan.org/release/Devel-CheckOS
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCANTRELL/Devel-CheckOS-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Find::Rule) >= 0.28
BuildRequires:  perl(parent)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Warnings)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00
Requires:       perl(File::Find::Rule) >= 0.28

# Remove unversioned requires
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::Find::Rule\\)$

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{__requires_exclude}|^perl\\(Devel::AssertOS::(AnOperatingSystem.*\|NotAnOperatingSystem))\s*$

%description
Devel::CheckOS provides a more friendly interface to $^O, and also lets you
check for various OS families such as Unix, which includes things like Linux,
*BSD, AIX, HPUX, Solaris etc.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Devel-CheckOS-%{version}

# Help file to recognise the Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done
chmod +x t/coverage.sh

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/pod.t
mkdir -p %{buildroot}%{_libexecdir}/%{name}/bin
ln -s %{_bindir}/use-devel-assertos %{buildroot}%{_libexecdir}/%{name}/bin
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license ARTISTIC.txt GPL2.txt
%doc CHANGELOG README TODO
%{_bindir}/use-devel-assertos
%dir %{perl_vendorlib}/Devel
%{perl_vendorlib}/Devel/AssertOS*
%{perl_vendorlib}/Devel/CheckOS*
%{_mandir}/man1/use-devel-assertos.1.gz
%{_mandir}/man3/Devel::AssertOS*
%{_mandir}/man3/Devel::CheckOS*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu May 23 2024 Jitka Plesnikova <jplesnik@redhat.com> - 2.04-1
- 2.04 bump (rhbz#2282792)

* Mon May 20 2024 Jitka Plesnikova <jplesnik@redhat.com> - 2.03-1
- 2.03 bump (rhbz#2281550)

* Mon May 06 2024 Jitka Plesnikova <jplesnik@redhat.com> - 2.01-1
- 2.01 bump (rhbz#2278464)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.96-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.96-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.96-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Feb 05 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.96-1
- 1.96 bump

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.95-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.95-1
- 1.95 bump

* Mon Jul 25 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.94-1
- 1.94 bump

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.93-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.93-2
- Perl 5.36 rebuild

* Thu Apr 28 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.93-1
- 1.93 bump

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.87-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.87-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 31 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.87-1
- 1.87 bump

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.86-2
- Perl 5.34 rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.86-1
- 1.86 bump
- Package tests

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.85-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 19 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.852-1
- 1.85 bump

* Tue Oct 06 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.84-1
- 1.84 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.83-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.83-2
- Perl 5.32 rebuild

* Mon Feb 17 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.83-1
- 1.83 bump

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.81-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.81-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.81-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.81-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.81-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.81-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.81-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.81-1
- 1.81 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.80-2
- Perl 5.26 rebuild

* Thu May 25 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.80-1
- 1.80 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.79-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 31 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.79-1
- 1.79 bump

* Mon Oct 24 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.77-1
- 1.77 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.76-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.76-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.76-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.76-2
- Perl 5.22 rebuild

* Mon Mar 16 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.76-1
- 1.76 bump

* Thu Mar 12 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.75-1
- 1.75 bump
- Correct license from (GPLv2 or Artistic) to ((GPLv2 or Artistic) and
  CC-BY-SA)

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.73-2
- Perl 5.20 rebuild

* Tue Aug 05 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.73-1
- 1.73 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.72-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 17 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.72-1
- 1.72 bump

* Sun Aug 04 2013 Petr Pisar <ppisar@redhat.com> - 1.71-3
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.71-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jan 28 2013 Petr Pisar <ppisar@redhat.com> - 1.71-1
- 1.71 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.64-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 16 2012 Petr Pisar <ppisar@redhat.com> - 1.64-6
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.64-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 25 2011 Petr Pisar <ppisar@redhat.com> - 1.64-4
- RPM 4.9 dependency filtering added

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1.64-3
- Perl mass rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1.64-2
- Perl mass rebuild

* Wed Apr 27 2011 Marcela Mašláňová <mmaslano@redhat.com> 1.64-1
- update to 1.64

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.63-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.63-2
- 661697 rebuild for fixing problems with vendorach/lib

* Tue Sep 14 2010 Petr Pisar <ppisar@redhat.com> - 1.63-1
- 1.63 bump
- Remove `dontask' patch as interactive code is not run anymore
- Add versioned Requires, filter unversioned ones out

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.50-7
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.50-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.50-5
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.50-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.50-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 17 2008 Marcela Mašláňová <mmaslano@redhat.com> 1.50-2
- remove two tests, because they can't pass in rpmbuild.

* Tue Dec 16 2008 Marcela Mašláňová <mmaslano@redhat.com> 1.50-1
- Specfile autogenerated by cpanspec 1.77.
