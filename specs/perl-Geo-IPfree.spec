# Perform optional tests
%bcond_without perl_Geo_IPfree_enables_optional_test

%global cpan_name Geo-IPfree
%global cpan_version 1.160000
%global cpan_author ATOOMIC
Name:           perl-%{cpan_name}
# Normalize version to dotted format
Version:        %(echo '%{cpan_version}' | sed 's/\(\....\)\(.\)/\1.\2/')
Release:        11%{?dist}
Summary:        Look up the country of an IPv4 Address
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/%(echo '%{cpan_author}' | sed 's=\(.\)\(.\)=\1/\1\2/\1\2=')/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
# Socket not used at tests
# Tests only:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
%if %{with perl_Geo_IPfree_enables_optional_test}
# Optional tests:
# CPAN::Meta not helpful
# CPAN::Meta::Prereqs not helpful
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
%endif
Requires:       perl(Socket)

%description
This package comes with it's own database to look up the IPv4's country, and
is totally free.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n %{cpan_name}-%{cpan_version}
%if !%{with perl_Geo_IPfree_enables_optional_test}
for F in t/pod.t t/pod_coverage.t; do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
done
%endif
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
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
%if %{with perl_Geo_IPfree_enables_optional_test}
rm %{buildroot}%{_libexecdir}/%{name}/t/pod.t \
    %{buildroot}%{_libexecdir}/%{name}/t/pod_coverage.t
%endif
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset AUTHOR_TESTING
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes misc README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.160.000-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 1.160.000-10
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.160.000-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.160.000-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.160.000-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.160.000-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.160.000-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.160.000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.160.000-3
- Perl 5.36 rebuild

* Fri Feb 04 2022 Petr Pisar <ppisar@redhat.com> - 1.160.000-2
- Help generators to recognize tests as Perl scripts

* Thu Feb 03 2022 Petr Pisar <ppisar@redhat.com> - 1.160.000-1
- 1.160000 bump
- Package the tests

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.151.940-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.151.940-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.151.940-15
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.151.940-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.151.940-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.151.940-12
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.151.940-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.151.940-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.151.940-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.151.940-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.151.940-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.151.940-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.151.940-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.151.940-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.151.940-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.151.940-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jun 03 2016 Petr Pisar <ppisar@redhat.com> - 1.151.940-1
- Normalize version format

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.1.5.1.9.4.0-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5.1.9.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Aug 26 2015 Petr Pisar <ppisar@redhat.com> - 1.1.5.1.9.4.0-1
- 1.151940 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4.3.6.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.1.4.3.6.3.0-2
- Perl 5.22 rebuild

* Wed Feb 18 2015 Petr Pisar <ppisar@redhat.com> - 1.1.4.3.6.3.0-1
- 1.143630 bump

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.1.4.1.6.7.0-2
- Perl 5.20 rebuild

* Tue Jul 01 2014 Petr Pisar <ppisar@redhat.com> - 1.1.4.1.6.7.0-1
- 1.141670 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3.2.8.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 12 2013 Petr Pisar <ppisar@redhat.com> - 1.1.3.2.8.7.0-1
- 1.132870 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3.1.6.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 19 2013 Petr Pisar <ppisar@redhat.com> - 1.1.3.1.6.5.0-2
- Perl 5.18 rebuild

* Wed Jun 26 2013 Petr Pisar <ppisar@redhat.com> - 1.1.3.1.6.5.0-1
- 1.131650 bump

* Fri May 17 2013 Petr Pisar <ppisar@redhat.com> - 1.1.3.0.4.5.0-1
- 1.130450 bump

* Wed Feb 13 2013 Petr Pisar <ppisar@redhat.com> - 1.1.3.0.1.1.0-1
- 1.130110 bump

* Tue Oct 23 2012 Petr Pisar <ppisar@redhat.com> - 1.1.2.2.8.8.0-1
- 1.122880 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2.1.6.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jul 13 2012 Petr Pisar <ppisar@redhat.com> - 1.1.2.1.6.6.0-1
- 1.121660 bump

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 1.1.2.0.4.6.0-2
- Perl 5.16 rebuild

* Tue Mar 20 2012 Petr Pisar <ppisar@redhat.com> - 1.1.2.0.4.6.0-1
- 1.1.2.0.4.6.0 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1.2.8.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Petr Pisar <ppisar@redhat.com> - 1.1.1.2.8.7.0-1
- 1.112870 bump
- Remove BuildRoot and defattr from spec code

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.1.0.2.8.7.0-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0.2.8.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 08 2010 Petr Pisar <ppisar@redhat.com> - 1.1.0.2.8.7.0-2
- Add BuildRequires needed for tests

* Mon Nov 08 2010 Petr Pisar <ppisar@redhat.com> - 1.1.0.2.8.7.0-1
- 1.102870 bump

* Wed Aug 11 2010 Petr Pisar <ppisar@redhat.com> - 1.1.0.1.6.5.0-1
- 1.101650 bump
- Experimental RPM-extensible version numbering

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.4-5
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.4-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 02 2009 Allisson Azevedo <allisson@gmail.com> 0.4-1
- Initial rpm release.
