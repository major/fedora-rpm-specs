# Run optional test
%bcond_with perl_PPIx_Regexp_enables_optional_test

Name:           perl-PPIx-Regexp
Version:        0.089
Release:        2%{?dist}
Summary:        Represent a regular expression of some sort
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/PPIx-Regexp
Source0:        https://cpan.metacpan.org/authors/id/W/WY/WYANT/PPIx-Regexp-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(lib)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(PPI::Document) >= 1.238
# PPI::Dumper 1.238 not used at tests
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Task::Weaken)
# Optional run-time:
BuildRequires:  perl(Encode)
# Tests:
BuildRequires:  perl(charnames)
BuildRequires:  perl(open)
BuildRequires:  perl(Test::More) >= 0.88
# YAML not used
%if %{with perl_PPIx_Regexp_enables_optional_test}
# Optional tests:
# Data::Dumper not used
# Text::CSV is not used
BuildRequires:  perl(Time::HiRes)
# YAML not used
%endif
Recommends:     perl(Encode)
Requires:       perl(PPI::Document) >= 1.238
Requires:       perl(PPI::Dumper) >= 1.238
Requires:       perl(Task::Weaken)

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(PPI::Document\\)$
# Filter private modules
%global __requires_exclude %{__requires_exclude}|^perl\\(My::Module::
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(My::Module::

%description
The purpose of the PPIx-Regexp package is to parse regular expressions in a
manner similar to the way the PPI package parses Perl. This class forms the
root of the parse tree, playing a role similar to PPI::Document.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(open)
Requires:       perl(PPI::Document) >= 1.238
%if %{with perl_PPIx_Regexp_enables_optional_test}
Requires:       perl(Time::HiRes)
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n PPIx-Regexp-%{version}
chmod -x eg/*
perl -MConfig -i -p \
    -e 's{^#!/usr/(?:local/bin/|bin/env )perl\b}{$Config{startperl}}' \
    eg/*
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
unset MAKING_MODULE_DISTRIBUTION
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
mkdir -p %{buildroot}%{_libexecdir}/%{name}/inc/My/Module
cp -a inc/My/Module/{Mock_Tokenizer,Test}.pm %{buildroot}%{_libexecdir}/%{name}/inc/My/Module
mkdir -p %{buildroot}%{_libexecdir}/%{name}/eg
cp -a eg/predump %{buildroot}%{_libexecdir}/%{name}/eg
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset AUTHOR_TESTING PPIX_REGEXP_TOKENIZER_TRACE
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING PPIX_REGEXP_TOKENIZER_TRACE
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSES
%doc Changes eg README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.089-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon May 19 2025 Michal Josef Špaček <mspacek@redhat.com> - 0.089-1
- 0.089 bump

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.088-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.088-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.088-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.088-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.088-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 01 2023 Michal Josef Špaček <mspacek@redhat.com> - 0.088-1
- 0.088 bump

* Mon Jan 30 2023 Michal Josef Špaček <mspacek@redhat.com> - 0.087-1
- 0.087 bump

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.086-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 02 2023 Michal Josef Špaček <mspacek@redhat.com> - 0.086-1
- 0.086 bump

* Sat Dec 10 2022 Michal Josef Špaček <mspacek@redhat.com> - 0.085-4
- Update license to SPDX format

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.085-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.085-2
- Perl 5.36 rebuild

* Thu Apr 21 2022 Michal Josef Špaček <mspacek@redhat.com> - 0.085-1
- 0.085 bump

* Tue Apr 05 2022 Michal Josef Špaček <mspacek@redhat.com> - 0.084-1
- 0.084 bump

* Tue Mar 22 2022 Michal Josef Špaček <mspacek@redhat.com> - 0.083-1
- 0.083 bump

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.082-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 05 2022 Michal Josef Špaček <mspacek@redhat.com> - 0.082-1
- 0.082 bump

* Mon Oct 25 2021 Michal Josef Špaček <mspacek@redhat.com> - 0.081-1
- 0.081 bump

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.080-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.080-2
- Perl 5.34 rebuild

* Tue Apr 20 2021 Michal Josef Špaček <mspacek@redhat.com> - 0.080-1
- 0.080 bump

* Fri Mar 26 2021 Petr Pisar <ppisar@redhat.com> - 0.079-1
- 0.079 bump
- Package tests

* Fri Jan 29 2021 Petr Pisar <ppisar@redhat.com> - 0.078-1
- 0.078 bump

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.077-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Petr Pisar <ppisar@redhat.com> - 0.077-1
- 0.077 bump

* Mon Nov 30 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.076-1
- 0.076 bump

* Fri Oct 09 2020 Petr Pisar <ppisar@redhat.com> - 0.075-1
- 0.075 bump

* Wed Sep 09 2020 Petr Pisar <ppisar@redhat.com> - 0.074-1
- 0.074 bump

* Wed Jul 29 2020 Petr Pisar <ppisar@redhat.com> - 0.073-1
- 0.073 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.072-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.072-2
- Perl 5.32 rebuild

* Wed May 20 2020 Petr Pisar <ppisar@redhat.com> - 0.072-1
- 0.072 bump

* Mon Mar 30 2020 Petr Pisar <ppisar@redhat.com> - 0.071-1
- 0.071 bump

* Fri Feb 28 2020 Petr Pisar <ppisar@redhat.com> - 0.070-1
- 0.070 bump

* Mon Feb 10 2020 Petr Pisar <ppisar@redhat.com> - 0.069-1
- 0.069 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.068-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Petr Pisar <ppisar@redhat.com> - 0.068-1
- 0.068 bump

* Mon Sep 02 2019 Petr Pisar <ppisar@redhat.com> - 0.067-1
- 0.067 bump

* Mon Aug 19 2019 Petr Pisar <ppisar@redhat.com> - 0.066-1
- 0.066 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.065-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.065-2
- Perl 5.30 rebuild

* Mon May 27 2019 Petr Pisar <ppisar@redhat.com> - 0.065-1
- 0.065 bump

* Tue Apr 02 2019 Petr Pisar <ppisar@redhat.com> - 0.064-1
- 0.064 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.063-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 09 2018 Petr Pisar <ppisar@redhat.com> - 0.063-1
- 0.063 bump

* Mon Aug 13 2018 Petr Pisar <ppisar@redhat.com> - 0.062-1
- 0.062 bump (removes PPIx::Regexp::Tokenizer::prior() method)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.061-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Petr Pisar <ppisar@redhat.com> - 0.061-1
- 0.061 bump

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.060-2
- Perl 5.28 rebuild

* Mon Jun 18 2018 Petr Pisar <ppisar@redhat.com> - 0.060-1
- 0.060 bump

* Wed May 09 2018 Petr Pisar <ppisar@redhat.com> - 0.059-1
- 0.059 bump

* Fri Apr 27 2018 Petr Pisar <ppisar@redhat.com> - 0.058-1
- 0.058 bump

* Wed Apr 18 2018 Petr Pisar <ppisar@redhat.com> - 0.057-1
- 0.057 bump

* Thu Mar 08 2018 Petr Pisar <ppisar@redhat.com> - 0.056-1
- 0.056 bump

* Fri Feb 09 2018 Petr Pisar <ppisar@redhat.com> - 0.055-1
- 0.055 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.054-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Petr Pisar <ppisar@redhat.com> - 0.054-1
- 0.054 bump

* Tue Oct 31 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.053-1
- 0.053 bump

* Fri Sep 08 2017 Petr Pisar <ppisar@redhat.com> - 0.052-1
- 0.052 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.051-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.051-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.051-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 30 2017 Petr Pisar <ppisar@redhat.com> - 0.051-1
- 0.51 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.050-2
- Perl 5.24 rebuild

* Mon May 09 2016 Petr Pisar <ppisar@redhat.com> - 0.050-1
- 0.050 bump

* Wed Apr 20 2016 Petr Pisar <ppisar@redhat.com> - 0.049-1
- 0.049 bump

* Tue Mar 01 2016 Petr Pisar <ppisar@redhat.com> - 0.048-1
- 0.048 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.047-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Petr Pisar <ppisar@redhat.com> - 0.047-1
- 0.047 bump

* Mon Jan 11 2016 Petr Pisar <ppisar@redhat.com> - 0.046-1
- 0.046 bump

* Mon Jan 04 2016 Petr Pisar <ppisar@redhat.com> - 0.045-1
- 0.045 bump

* Wed Dec 09 2015 Petr Pisar <ppisar@redhat.com> - 0.044-1
- 0.044 bump

* Thu Nov 19 2015 Petr Pisar <ppisar@redhat.com> - 0.043-1
- 0.043 bump

* Mon Oct 12 2015 Petr Pisar <ppisar@redhat.com> - 0.042-1
- 0.042 bump

* Fri Jul 03 2015 Petr Pisar <ppisar@redhat.com> - 0.041-1
- 0.041 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.040-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.040-2
- Perl 5.22 rebuild

* Mon Jun 01 2015 Petr Pisar <ppisar@redhat.com> - 0.040-1
- 0.040 bump

* Fri Apr 03 2015 Petr Pisar <ppisar@redhat.com> - 0.039-1
- 0.039 bump

* Thu Mar 12 2015 Petr Pisar <ppisar@redhat.com> - 0.038-1
- 0.038 bump

* Fri Nov 14 2014 Petr Pisar <ppisar@redhat.com> - 0.037-1
- 0.037 bump

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.036-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.036-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 07 2014 Petr Pisar <ppisar@redhat.com> - 0.036-1
- 0.036 bump

* Tue Nov 19 2013 Petr Pisar <ppisar@redhat.com> - 0.035-1
- 0.035 bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.034-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 Petr Pisar <ppisar@redhat.com> - 0.034-3
- Perl 5.18 rebuild

* Fri May 24 2013 Petr Pisar <ppisar@redhat.com> - 0.034-2
- Specify all dependencies

* Mon May 13 2013 Petr Pisar <ppisar@redhat.com> - 0.034-1
- 0.034 bump

* Thu Feb 28 2013 Petr Pisar <ppisar@redhat.com> - 0.033-1
- 0.033 bump

* Fri Feb 08 2013 Petr Pisar <ppisar@redhat.com> - 0.032-1
- 0.032 bump

* Mon Feb 04 2013 Petr Pisar <ppisar@redhat.com> - 0.031-1
- 0.031 bump

* Thu Jan 24 2013 Petr Pisar <ppisar@redhat.com> - 0.030-1
- 0.030 bump

* Mon Jan 14 2013 Petr Pisar <ppisar@redhat.com> - 0.029-1
- 0.029 bump

* Tue Aug 21 2012 Petr Pisar <ppisar@redhat.com> - 0.028-5
- Run-require Exporter

* Thu Aug 16 2012 Petr Pisar <ppisar@redhat.com> - 0.028-4
- Specify all dependencies

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.028-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Petr Pisar <ppisar@redhat.com> - 0.028-2
- Perl 5.16 rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 0.028-1
- 0.028 bump

* Mon Jun 04 2012 Petr Pisar <ppisar@redhat.com> - 0.027-1
- 0.027 bump

* Mon Feb 27 2012 Petr Pisar <ppisar@redhat.com> - 0.026-1
- 0.026 bump

* Mon Jan 23 2012 Petr Pisar <ppisar@redhat.com> - 0.025-1
- 0.025 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.024-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 19 2011 Petr Pisar <ppisar@redhat.com> - 0.024-1
- 0.024 bump

* Fri Dec 09 2011 Petr Pisar <ppisar@redhat.com> - 0.023-1
- 0.023 bump

* Fri Nov 25 2011 Petr Pisar <ppisar@redhat.com> - 0.022-1
- 0.022 bump

* Tue Jul 26 2011 Petr Pisar <ppisar@redhat.com> - 0.021-1
- 0.021 bump
- Remove RPM 4.8 filter

* Mon Jul 25 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.020-3
- add new filter

* Wed Jun 29 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.020-2
- Perl mass rebuild

* Mon Apr 04 2011 Petr Pisar <ppisar@redhat.com> - 0.020-1
- 0.020 bump

* Wed Mar 02 2011 Petr Pisar <ppisar@redhat.com> - 0.019-1
- 0.019 bump

* Thu Feb 17 2011 Petr Pisar <ppisar@redhat.com> - 0.018-1
- 0.018 bump
- Remove BuildRoot stuff

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.017-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 27 2011 Petr Pisar <ppisar@redhat.com> - 0.017-1
- 0.017 bump

* Thu Jan 06 2011 Petr Pisar <ppisar@redhat.com> - 0.016-1
- 0.016 bump

* Wed Oct 27 2010 Petr Pisar <ppisar@redhat.com> - 0.015-1
- 0.015 bump

* Mon Oct 18 2010 Petr Pisar <ppisar@redhat.com> - 0.014-1
- 0.014 bump

* Mon Oct 04 2010 Petr Pisar <ppisar@redhat.com> - 0.012-1
- 0.012 bump

* Wed Sep 22 2010 Petr Pisar <ppisar@redhat.com> - 0.011-1
- 0.011 bump
- Remove unversioned Requires

* Thu Sep 16 2010 Petr Pisar <ppisar@redhat.com> - 0.010-1
- 0.010 bump

* Tue Jun  8 2010 Petr Pisar <ppisar@redhat.com> - 0.007-1
- Specfile autogenerated by cpanspec 1.78 (bug #598553).
