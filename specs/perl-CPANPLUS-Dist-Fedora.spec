%global pkgname CPANPLUS-Dist-Fedora

# Do not perform tests that need the Internet
%bcond_with perl_CPAN_Dist_Fedora_enables_network

Name:           perl-CPANPLUS-Dist-Fedora
Version:        0.4.4
Release:        10%{?dist}
Summary:        CPANPLUS backend to build Fedora/RedHat RPMs
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CPANPLUS-Dist-Fedora
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(Module::Build) >= 0.28
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(CPANPLUS::Dist::Base)
BuildRequires:  perl(CPANPLUS::Error)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(parent)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Pod::POM)
BuildRequires:  perl(Pod::POM::View::Text)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Template)
%if %{with perl_CPAN_Dist_Fedora_enables_network}
BuildRequires:  gcc rpm rpm-build
%endif
# Tests:
BuildRequires:  perl(blib)
%if %{with perl_CPAN_Dist_Fedora_enables_network}
BuildRequires:  perl(CPANPLUS::Backend)
%endif
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)
Requires:       gcc
Requires:       rpm
Requires:       rpm-build

# Filter modules bundled for tests
%if %{without perl_CPAN_Dist_Fedora_enables_network}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(CPANPLUS::Backend\\)
%endif

%description
This is a distribution class to create Fedora packages from CPAN modules, 
and all its dependencies. This allows you to have the most recent copies of 
CPAN modules installed, using your package manager of choice, but without 
having to wait for central repositories to be updated.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{with perl_CPAN_Dist_Fedora_enables_network}
Requires:       perl(CPANPLUS::Backend)
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -qn %{pkgname}-%{version}

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
%if %{with perl_CPAN_Dist_Fedora_enables_network}
export TEST_CPANPLUS_FEDORA=1
%else
unset TEST_CPANPLUS_FEDORA
%endif
cd %{_libexecdir}/%{name} && exec prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
%if %{with perl_CPAN_Dist_Fedora_enables_network}
export TEST_CPANPLUS_FEDORA=1
%else
unset TEST_CPANPLUS_FEDORA
%endif
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.4.4-3
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 07 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.4.4-1
- 0.4.4 bump

* Sun Oct 03 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.4.3-1
- 0.4.3 bump
- Package tests

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.4.2-3
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 04 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.4.2-1
- 0.4.2 bump

* Tue Nov 03 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.4.1-1
- 0.4.1 bump

* Tue Nov 03 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.4.0-1
- 0.4.0 bump

* Thu Oct 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.3-1
- 0.2.3 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.2-2
- Perl 5.32 rebuild

* Wed Jan 29 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.2-2
- 0.2.2 bump

* Mon Aug 26 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.1-1
- 0.2.1 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.0-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 04 2018 Petr Pisar <ppisar@redhat.com> - 0.2.0-2
- Perl 5.28 rebuild

* Mon Jul 02 2018 Petr Pisar <ppisar@redhat.com> - 0.2.0-1
- 0.2.0 bump

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.0.10-2
- Perl 5.28 rebuild

* Thu May 24 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.0.10-1
- 0.0.10 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.0.9-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.0.9-2
- Perl 5.24 rebuild

* Mon Feb 29 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.0.9-1
- 0.0.9 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 11 2015 Petr Pisar <ppisar@redhat.com> - 0.0.6-1
- 0.0.6 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.0.4-4
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.0.4-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 26 2013 Christopher Meng <rpm@cicku.me> - 0.0.4-1
- Initial Package.
