Name:           perl-Net-DAVTalk
Version:        0.23
Release:        1%{?dist}
Summary:        Client for DAV servers
License:        Artistic-2.0
URL:            https://metacpan.org/release/Net-DAVTalk
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRONG/Net-DAVTalk-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6.0
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DateTime::Format::ISO8601)
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(HTTP::Tiny) >= 0.016
BuildRequires:  perl(JSON)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Tie::DataUUID) >= 1.02
BuildRequires:  perl(URI) >= 1.60
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(XML::Fast) >= 0.11
BuildRequires:  perl(XML::Spice) >= 0.03
# Tests:
BuildRequires:  perl(Test::More)
Requires:       perl(HTTP::Tiny) >= 0.016
Requires:       perl(Tie::DataUUID) >= 1.02
Requires:       perl(URI) >= 1.60
Requires:       perl(XML::Fast) >= 0.11
Requires:       perl(XML::Spice) >= 0.03

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((HTTP::Tiny|Tie::DataUUID|URI|XML::Fast|XML::Spice)\\)$

%description
This is a Perl library for accessing DAV servers.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Net-DAVTalk-%{version}
# Remove author tests
for F in \
    t/boilerplate.t \
    t/manifest.t \
    t/pod.t \
    t/pod-coverage.t \
    ; do
    rm "$F"
    perl -i -ne 'print $_ unless m{\A\Q'"$F"'\E}' MANIFEST
done
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
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Wed Jan 22 2025 Michal Josef Špaček <mspacek@redhat.com> - 0.23-1
- 0.23 bump (BZ#2339404)

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 12 2022 Michal Josef Špaček <mspacek@redhat.com> - 0.22-4
- Simplify spec file
- Update license to SPDX format

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-2
- Perl 5.36 rebuild

* Mon Mar 14 2022 Michal Josef Špaček <mspacek@redhat.com> - 0.22-1
- 0.22 bump

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-4
- Perl 5.34 rebuild

* Wed Apr 21 2021 Michal Josef Špaček <mspacek@redhat.com> - 0.20-3
- Add README to package, contain license
- Unify build root to same style

* Tue Apr 20 2021 Michal Josef Špaček <mspacek@redhat.com> - 0.20-2
- Package tests

* Thu Apr 15 2021 Michal Josef Špaček <mspacek@redhat.com> - 0.20-1
- 0.20 bump

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-2
- Perl 5.32 rebuild

* Wed May 06 2020 Petr Pisar <ppisar@redhat.com> - 0.19-1
- 0.19 bump

* Tue Apr 07 2020 Petr Pisar <ppisar@redhat.com> - 0.18-1
- 0.18 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Petr Pisar <ppisar@redhat.com> - 0.17-1
- 0.17 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-2
- Perl 5.30 rebuild

* Fri May 10 2019 Petr Pisar <ppisar@redhat.com> - 0.16-1
- 0.16 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-5
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-2
- Perl 5.26 rebuild

* Mon Mar 20 2017 Petr Pisar <ppisar@redhat.com> - 0.14-1
- 0.14 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 25 2016 Petr Pisar <ppisar@redhat.com> - 0.12-1
- 0.12 bump

* Fri Nov 11 2016 Petr Pisar <ppisar@redhat.com> 0.11-1
- Specfile autogenerated by cpanspec 1.78.
