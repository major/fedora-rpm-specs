# Run optional test
%bcond_without perl_Dist_Zilla_Plugin_Git_Contributors_enables_optional_test

Name:           perl-Dist-Zilla-Plugin-Git-Contributors
Version:        0.037
Release:        3%{?dist}
Summary:        Add contributor names from git to your distribution
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Zilla-Plugin-Git-Contributors
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Dist-Zilla-Plugin-Git-Contributors-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Data::Dumper)
# This is a Dist::Zilla plugin
BuildRequires:  perl(Dist::Zilla) >= 4.300039
BuildRequires:  perl(Dist::Zilla::Role::MetaProvider)
BuildRequires:  perl(Dist::Zilla::Role::PrereqSource)
BuildRequires:  perl(Git::Wrapper) >= 0.038
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(List::UtilsBy) >= 0.04
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Path::Tiny) >= 0.048
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Unicode::Collate) >= 0.53
BuildRequires:  perl(version)
# Tests:
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(open)
BuildRequires:  perl(parent)
BuildRequires:  perl(Sort::Versions)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::DZil)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
# Test::Warnings not used
BuildRequires:  perl(utf8)
%if %{with perl_Dist_Zilla_Plugin_Git_Contributors_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Dist::Zilla::Plugin::PodWeaver)
BuildRequires:  perl(Module::Runtime::Conflicts)
BuildRequires:  perl(Moose::Conflicts)
BuildRequires:  perl(Pod::Weaver::Section::Contributors)
%endif
Requires:       perl(Data::Dumper)
# This is a Dist::Zilla plugin
Requires:       perl(Dist::Zilla) >= 4.300039
Requires:       perl(Dist::Zilla::Role::MetaProvider)
Requires:       perl(Dist::Zilla::Role::PrereqSource)
# Git::Wrapper 0.038 from META, CPAN RT#127045
Requires:       perl(Git::Wrapper) >= 0.038

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Git::Wrapper\\)(| >= 0\\.035)$

# Hide private modules
%global __requires_exclude %{__requires_exclude}|^perl\\(GitSetup\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\((GitSetup|My::Git::Wrapper)\\)

%description
This is a Dist::Zilla plugin that extracts all names and email addresses
from git commits in your repository and adds them to the distribution
metadata under the x_contributors key.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{with perl_Dist_Zilla_Plugin_Git_Contributors_enables_optional_test}
Requires:       perl(Dist::Zilla::Plugin::PodWeaver)
Requires:       perl(Module::Runtime::Conflicts)
Requires:       perl(Moose::Conflicts)
Requires:       perl(Pod::Weaver::Section::Contributors)
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Dist-Zilla-Plugin-Git-Contributors-%{version}
%if !%{with perl_Dist_Zilla_Plugin_Git_Contributors_enables_optional_test}
rm t/04-podweaver-warning.t
perl -i -ne 'print $_ unless m{^t/04-podweaver-warning\.t}' MANIFEST
%endif
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
export PERL_MM_FALLBACK_SILENCE_WARNING=1
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
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
%license LICENCE
%doc Changes README
%dir %{perl_vendorlib}/Dist
%dir %{perl_vendorlib}/Dist/Zilla
%dir %{perl_vendorlib}/Dist/Zilla/Plugin
%dir %{perl_vendorlib}/Dist/Zilla/Plugin/Git
%{perl_vendorlib}/Dist/Zilla/Plugin/Git/Contributors.pm
%{_mandir}/man3/Dist::Zilla::Plugin::Git::Contributors.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.037-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.037-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Feb 21 2024 Petr Pisar <ppisar@redhat.com> - 0.037-1
- 0.037 bump
- Install the tests

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.036-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.036-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.036-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.036-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.036-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.036-6
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.036-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.036-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.036-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.036-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 05 2021 Petr Pisar <ppisar@redhat.com> - 0.036-1
- 0.036 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.035-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.035-6
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.035-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.035-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.035-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.035-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 10 2018 Petr Pisar <ppisar@redhat.com> - 0.035-1
- 0.035 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.034-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.034-2
- Perl 5.28 rebuild

* Mon Apr 23 2018 Petr Pisar <ppisar@redhat.com> - 0.034-1
- 0.034 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.032-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 07 2017 Petr Pisar <ppisar@redhat.com> - 0.032-1
- 0.032 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.030-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.030-2
- Perl 5.26 rebuild

* Mon May 15 2017 Petr Pisar <ppisar@redhat.com> - 0.030-1
- 0.030 bump

* Thu Mar 23 2017 Petr Pisar <ppisar@redhat.com> 0.029-1
- Specfile autogenerated by cpanspec 1.78.
