# Real version
%global cpan_version v3.3.3

Name:           perl-Test-Compile
Version:        %(echo '%{cpan_version}' | tr -d 'v')
Release:        3%{?dist}
Summary:        Check whether Perl module files compile correctly
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Compile
Source0:        https://cpan.metacpan.org/authors/id/E/EG/EGILES/Test-Compile-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(FindBin)
# Test::More version is described in Changes
BuildRequires:  perl(Test::More) >= 1.3
# Optional tests
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Warnings)


%{?perl_default_filter}
# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude_from %{?__requires_exclude_from:%__requires_exclude_from|}^%{_libexecdir}/%{name}/lib

%description
Test::Compile lets you check the validity of a Perl module file or Perl script
file, and report its results in standard Test::Simple fashion.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
# Optional tests
Requires:       perl(Test::Exception)
Requires:       perl(Test::Warnings)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Test-Compile-%{cpan_version}

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
mkdir -p %{buildroot}%{_libexecdir}/%{name}/lib/Test/Compile
for F in Test/Compile.pm Test/Compile/Internal.pm; do
    ln -s %{perl_vendorlib}/$F %{buildroot}%{_libexecdir}/%{name}/lib/$F
done
# Remove author tests
rm %{buildroot}%{_libexecdir}/%{name}/t/999-*
perl -i -ne 'print $_ unless m{\@INC = grep .* \@INC;}' %{buildroot}%{_libexecdir}/%{name}/t/scripts/messWithLib.pl
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TEST
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Test*
%{_mandir}/man3/Test::Compile*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue May 07 2024 Jitka Plesnikova <jplesnik@redhat.com> - 3.3.3-1
- 3.3.3 bump (rhbz#2278779)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 17 2023 Jitka Plesnikova <jplesnik@redhat.com> - 3.3.1-1
- 3.3.1 bump (rhbz#2223238)

* Fri Jul 14 2023 Jitka Plesnikova <jplesnik@redhat.com> - 3.3.0-1
- 3.3.0 bump (rhbz#2222144)

* Thu Apr 06 2023 Jitka Plesnikova <jplesnik@redhat.com> - 3.2.2-1
- 3.2.2 bump

* Mon Apr 03 2023 Jitka Plesnikova <jplesnik@redhat.com> - 3.2.0-2
- Fix failing test

* Mon Apr 03 2023 Jitka Plesnikova <jplesnik@redhat.com> - 3.2.0-1
- 3.2.0 bump

* Tue Mar 28 2023 Jitka Plesnikova <jplesnik@redhat.com> - 3.1.1-1
- 3.1.1 bump
- Package tests

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 06 2022 Jitka Plesnikova <jplesnik@redhat.com> - 3.1.0-1
- 3.1.0 bump

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 3.0.1-3
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 3.0.1-1
- 3.0.1 bump

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.2-1
- 2.4.2 bump

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.1-4
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.1-1
- 2.4.1 bump

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.0-2
- Perl 5.32 rebuild

* Mon Mar 30 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.0-1
- 2.4.0 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 23 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.3.1-1
- 2.3.1 bump

* Thu Oct 10 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.3.0-1
- 2.3.0 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.2-1
- 2.2.2 bump

* Tue Jul 09 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.1-1
- 2.2.1 bump

* Mon Jul 08 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.0-1
- 2.2.0 bump

* Wed Jul 03 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.1.2-1
- 2.1.2 bump

* Mon Jul 01 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.1.1-1
- 2.1.1 bump

* Thu Jun 27 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.1.0-1
- 2.1.0 bump

* Mon Jun 24 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.0.1-1
- 2.0.1 bump

* Tue Jun 18 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.0.0-1
- 2.0.0 bump

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.3.0-11
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.3.0-8
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.3.0-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.3.0-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 25 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.3.0-1
- 1.3.0 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.1-2
- Perl 5.22 rebuild

* Tue Dec 09 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.1-1
- 1.2.1 bump

* Fri Nov 14 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.0-1
- 1.2.0 bump

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.24-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.24-2
- Perl 5.18 rebuild

* Mon Feb 25 2013 Petr Šabata <contyk@redhat.com> - 0.24-1
- 0.24 bump (docs only)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 24 2013 Petr Šabata <contyk@redhat.com> - 0.23-1
- 0.23 bump

* Wed Oct 31 2012 Petr Šabata <contyk@redhat.com> - 0.22-1
- 0.22 bumpity

* Thu Sep 13 2012 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-1
- 0.21 bump
- Remove the filter of ::Internal module. It is no longer 'beta' and could
  be used directly to test a CPAN distribution.

* Thu Aug 09 2012 Petr Šabata <contyk@redhat.com> - 0.20-1
- 0.20 bump

* Wed Aug 08 2012 Petr Šabata <contyk@redhat.com> - 0.19-2
- Filter the ::Internal module from requires too

* Mon Aug 06 2012 Petr Šabata <contyk@redhat.com> - 0.19-1
- 0.19 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-1
- 0.18 bump

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.17-2
- Perl 5.16 rebuild

* Fri Feb 24 2012 Petr Šabata <contyk@redhat.com> - 0.17-1
- 0.17 bump

* Mon Feb 20 2012 Petr Šabata <contyk@redhat.com> - 0.16-1
- 0.16 bump

* Fri Feb 03 2012 Petr Pisar <ppisar@redhat.com> - 0.15-1
- 0.15 bump

* Fri Jan 13 2012 Marcela Mašláňová <mmaslano@redhat.com> - 0.14-1
- bump to 0.14

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.13-5
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.13-3
- 661697 rebuild for fixing problems with vendorach/lib

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.13-2
- Mass rebuild with perl-5.12.0

* Sat Mar 20 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.13-1
- PERL_INSTALL_ROOT => DESTDIR, perl_default_filter
- auto-update to 0.13 (by cpan-spec-update 0.01)
- altered br on perl(ExtUtils::MakeMaker) (0 => 6.42)
- altered br on perl(Test::More) (0.70 => 0.88)
- added a new br on CPAN (inc::Module::AutoInstall found)

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.08-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 16 2008 Marcela Mašláňová <mmaslano@redhat.com> 0.08-1
- Specfile autogenerated by cpanspec 1.77.
