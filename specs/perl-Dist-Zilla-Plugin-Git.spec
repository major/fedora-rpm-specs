# Run optional test
%bcond_without perl_Dist_Zilla_Plugin_Git_enables_optional_test

Name:           perl-Dist-Zilla-Plugin-Git
Version:        2.051
Release:        3%{?dist}
Summary:        Update your git repository after release
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Zilla-Plugin-Git
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Dist-Zilla-Plugin-Git-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  git-core >= 1.5.4
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(version) >= 0.80
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
# DateTime not used at tests
BuildRequires:  perl(Dist::Zilla) >= 4
BuildRequires:  perl(Dist::Zilla::Plugin::GatherDir) >= 4.200016
BuildRequires:  perl(Dist::Zilla::Role::AfterBuild)
# Dist::Zilla::Role::AfterMint not used at tests
BuildRequires:  perl(Dist::Zilla::Role::AfterRelease)
BuildRequires:  perl(Dist::Zilla::Role::BeforeRelease)
BuildRequires:  perl(Dist::Zilla::Role::FilePruner)
BuildRequires:  perl(Dist::Zilla::Role::GitConfig)
# Dist::Zilla::Role::PluginBundle not used at tests
BuildRequires:  perl(Dist::Zilla::Role::VersionProvider)
BuildRequires:  perl(File::chdir)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Git::Wrapper) >= 0.021
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(IPC::System::Simple)
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::Has::Sugar)
BuildRequires:  perl(namespace::autoclean) >= 0.09
BuildRequires:  perl(Path::Tiny) >= 0.048
BuildRequires:  perl(String::Formatter)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Type::Utils)
BuildRequires:  perl(Types::Path::Tiny)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(Version::Next)
# Tests:
BuildRequires:  perl(CPAN::Meta::Check) >= 0.011
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Dist::Zilla::File::InMemory)
BuildRequires:  perl(Dist::Zilla::Role::Releaser)
BuildRequires:  perl(Dist::Zilla::Tester)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::Path) >= 2.07
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(lib)
BuildRequires:  perl(Log::Dispatchouli)
BuildRequires:  perl(Test::DZil)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(utf8)
%if %{with perl_Dist_Zilla_Plugin_Git_enables_optional_test}
# Optional tests
BuildRequires:  gnupg
BuildRequires:  perl(Dist::Zilla::Plugin::Config::Git)
BuildRequires:  perl(Module::Runtime::Conflicts)
BuildRequires:  perl(Moose::Conflicts)
%endif
Requires:       perl(DateTime)
Requires:       perl(Dist::Zilla::Plugin::GatherDir) >= 4.200016
Requires:       perl(Dist::Zilla::Role::AfterBuild)
Requires:       perl(Dist::Zilla::Role::AfterMint)
Requires:       perl(Dist::Zilla::Role::AfterRelease)
Requires:       perl(Dist::Zilla::Role::BeforeRelease)
Requires:       perl(Dist::Zilla::Role::FilePruner)
Requires:       perl(Dist::Zilla::Role::GitConfig)
Requires:       perl(Dist::Zilla::Role::PluginBundle)
Requires:       perl(Dist::Zilla::Role::VersionProvider)
Requires:       perl(Version::Next)

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(:VERSION\\) >= 5\\.8\\.|^perl\\(Dist::Zilla\\) >= 2\\.|perl\\(Git::Wrapper\\)$
# Remove private modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Util\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\((Dist::Zilla::Plugin::MyTestArchiver|Git::Wrapper|Util)\\)

%description
This set of plugins for Dist::Zilla can do interesting things for module
authors using Git (http://git-scm.com/) to track their work.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
Requires:       perl(Dist::Zilla::Role::Releaser)
Requires:       perl(Git::Wrapper) >= 0.021
%if %{with perl_Dist_Zilla_Plugin_Git_enables_optional_test}
Requires:       gnupg
Requires:       perl(Dist::Zilla::Plugin::Config::Git)
Requires:       perl(Module::Runtime::Conflicts)
Requires:       perl(Moose::Conflicts)
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Dist-Zilla-Plugin-Git-%{version}
%if !%{with perl_Dist_Zilla_Plugin_Git_enables_optional_test}
rm t/push-gitconfig.t
perl -i -ne 'print $_ unless m{\A\Qt/push-gitconfig.t\E\b}' MANIFEST
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
cp -a corpus t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
# Dist::Zilla::Tester writes to CWD
# (https://github.com/rjbs/Dist-Zilla/issues/698)
set -e
DIR="$(mktemp -d)"
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
unset V
exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset V
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENCE
%doc Changes README
%dir %{perl_vendorlib}/Dist
%dir %{perl_vendorlib}/Dist/Zilla
%dir %{perl_vendorlib}/Dist/Zilla/Plugin
%{perl_vendorlib}/Dist/Zilla/Plugin/Git
%{perl_vendorlib}/Dist/Zilla/Plugin/Git.pm
%dir %{perl_vendorlib}/Dist/Zilla/PluginBundle
%{perl_vendorlib}/Dist/Zilla/PluginBundle/Git.pm
%dir %{perl_vendorlib}/Dist/Zilla/Role
%{perl_vendorlib}/Dist/Zilla/Role/Git
%{_mandir}/man3/Dist::Zilla::Plugin::Git.*
%{_mandir}/man3/Dist::Zilla::Plugin::Git::*
%{_mandir}/man3/Dist::Zilla::PluginBundle::Git.*
%{_mandir}/man3/Dist::Zilla::Role::Git::*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.051-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.051-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Petr Pisar <ppisar@redhat.com> - 2.051-1
- 2.051 bump

* Tue Jan 23 2024 Petr Pisar <ppisar@redhat.com> - 2.049-1
- 2.049 bump

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.048-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.048-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.048-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.048-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.048-4
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.048-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.048-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 12 2021 Petr Pisar <ppisar@redhat.com> - 2.048-1
- 2.048 bump
- Package the tests

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.047-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.047-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 14 2020 Petr Pisar <ppisar@redhat.com> - 2.047-1
- 2.047 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.046-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.046-5
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.046-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.046-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.046-2
- Perl 5.30 rebuild

* Mon Mar 18 2019 Petr Pisar <ppisar@redhat.com> - 2.046-1
- 2.046 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.045-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.045-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.045-2
- Perl 5.28 rebuild

* Mon Jun 04 2018 Petr Pisar <ppisar@redhat.com> - 2.045-1
- 2.045 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.043-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 11 2017 Petr Pisar <ppisar@redhat.com> - 2.043-1
- 2.043 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.042-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.042-2
- Perl 5.26 rebuild

* Mon May 15 2017 Petr Pisar <ppisar@redhat.com> - 2.042-1
- 2.042 bump

* Thu Mar 23 2017 Petr Pisar <ppisar@redhat.com> 2.041-1
- Specfile autogenerated by cpanspec 1.78.
