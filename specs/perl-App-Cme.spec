Name:           perl-App-Cme
Version:        1.041
Release:        2%{?dist}
Summary:        Check or edit configuration data with Config::Model
License:        LGPL-2.1-or-later
URL:            https://metacpan.org/release/App-Cme
Source0:        https://cpan.metacpan.org/authors/id/D/DD/DDUMONT/App-Cme-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.20
BuildRequires:  perl(Config)
BuildRequires:  perl(Module::Build) >= 0.34
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(App::Cmd::Setup)
BuildRequires:  perl(base)
BuildRequires:  perl(charnames)
BuildRequires:  perl(Config::Model) >= 2.148
# Config::Model::CursesUI - not used at test
# Config::Model::FuseUI - Fuse is not packaged yet
BuildRequires:  perl(Config::Model::Lister)
BuildRequires:  perl(Config::Model::ObjTreeScanner)
# Config::Model::SimpleUI - not used at test
# Config::Model::TermUI - not used at test
# Config::Model::TkUI - not used at test
# Config::Model::Utils::GenClassPod - not used at test
# Data::Dumper - not used at test
BuildRequires:  perl(Encode)
BuildRequires:  perl(feature)
BuildRequires:  perl(File::HomeDir)
# JSON - not used at test
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(open)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Pod::POM)
BuildRequires:  perl(Pod::POM::View::Text)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Tie::Hash)
# Tk - not used at test
# Tk::ErrorDialog - not used at test
BuildRequires:  perl(utf8)
BuildRequires:  perl(YAML::PP)
# Tests
BuildRequires:  perl(App::Cmd::Tester)
BuildRequires:  perl(English)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Term::ANSIColor) >= 2.01
BuildRequires:  perl(Test::File::Contents)
BuildRequires:  perl(Test::More)
# Test::Perl::Critic - optional test
Requires:       perl(Config::Model::CursesUI)
Requires:       perl(Config::Model::FuseUI)
Requires:       perl(Config::Model::SimpleUI)
Requires:       perl(Config::Model::TermUI)
Requires:       perl(Config::Model::TkUI)
Requires:       perl(Tk)
Requires:       perl(Tk::ErrorDialog)

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Config::Model\\)\s*$

%description
cme and Config::Model are quite modular. The configuration data that you
can edit depend on the other Config::Model distributions installed on your
system.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n App-Cme-%{version}
perl -MConfig -pi -e '!s|\A#!.*perl\b|$Config{startperl}|' bin/cme

%build
perl Build.PL installdirs=vendor
./Build

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

# Install bash_completion script
install -D -m 0644 contrib/bash_completion.cme %{buildroot}%{_sysconfdir}/bash_completion.d/cme

# Install tests - copy tests to tmp
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
cp -a t %{buildroot}/%{_libexecdir}/%{name}
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
unset AUTHOR_TESTING
# Some tests write into temporary files/directories. The easiest solution
# is to copy the tests into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test


%check
unset AUTHOR_TESTING
./Build test

%files
%license LICENSE
%doc Changes README.pod
%{_bindir}/cme
%dir %{perl_vendorlib}/App
%{perl_vendorlib}/App/Cme*
%{_mandir}/man1/cme*
%{_mandir}/man3/App::Cme*
%{_sysconfdir}/bash_completion.d

%files tests
%{_libexecdir}/%{name}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.041-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 25 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.041-1
- 1.041 bump (rhbz#2328491)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.040-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.040-1
- 1.040 bump (rhbz#2258864)

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.039-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.039-1
- 1.039 bump (rhbz#2253785)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.038-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.038-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.038-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.038-2
- Perl 5.36 rebuild

* Thu Mar 24 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.038-1
- 1.038 bump

* Mon Feb 07 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.037-1
- 1.037 bump

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.036-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 13 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.036-1
- 1.036 bump

* Mon Jan 10 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.035-1
- 1.035 bump
- Package tests

* Mon Nov 01 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.034-1
- 1.034 bump

* Thu Sep 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.033-1
- 1.033 bump

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.032-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.032-5
- Perl 5.34 rebuild

* Tue Mar 16 2021 Petr Pisar <ppisar@redhat.com> - 1.032-4
- Adapt to Getopt-Long-Descriptive-0.106 (bug #1938396)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.032-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.032-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.032-1
- 1.032 bump

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.031-3
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.031-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.031-1
- 1.031 bump

* Thu Sep 12 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.030-1
- 1.030 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.029-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.029-4
- Perl 5.30 re-rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.029-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.029-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 21 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.029-1
- 1.029 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.028-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.028-2
- Perl 5.28 rebuild

* Thu Jun 21 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.028-1
- 1.028 bump

* Mon Apr 09 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.027-1
- 1.027 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.026-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 19 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.026-1
- 1.026 bump

* Fri Dec 15 2017 Petr Pisar <ppisar@redhat.com> - 1.025-1
- 1.025 bump

* Mon Oct 23 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.024-1
- 1.024 bump

* Mon Sep 11 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.023-1
- 1.023 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.022-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 22 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.022-1
- 1.022 bump

* Mon Jun 19 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.021-1
- 1.021 bump

* Mon Jun 12 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.020-1
- 1.020 bump

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.019-3
- Perl 5.26 rebuild

* Thu May 25 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.019-2
- Add BR: perl(YAML)

* Tue May 02 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.019-1
- 1.019 bump

* Mon Apr 10 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.018-1
- 1.018 bump

* Mon Mar 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.017-1
- 1.017 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.016-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.016-1
- 1.016 bump

* Mon Oct 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.015-1
- 1.015 bump

* Thu Sep 29 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.014-1
- 1.014 bump

* Mon Jul 11 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.013-1
- 1.013 bump

* Wed Jun 01 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.012-1
- 1.012 bump

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.011-2
- Perl 5.24 rebuild

* Fri Apr 22 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.011-1
- 1.011 bump

* Wed Feb 10 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.010-1
- 1.010 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.009-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.009-2
- Updated due review comments

* Mon Jan 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.009-1
- Initial release
