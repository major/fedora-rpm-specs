Name:           perl-rdapper
Version:        1.19
Release:        1%{?dist}
Summary:        Simple console-based RDAP client
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/App-rdapper
# Upstream source repository is <https://github.com/gbxyz/rdapper>, renamed
# from <https://github.com/jodrell/rdapper> that was announced by the author
# at <https://www.ietf.org/mail-archive/web/weirds/current/msg01981.html>.
Source0:        https://cpan.metacpan.org/authors/id/G/GB/GBROWN/App-rdapper-%{version}.tar.gz
# Fix skipping tests, in upstream after 1.19,
# <https://github.com/gbxyz/rdapper/pull/22>
Patch0:         App-rdapper-1.19-t-01-l10n.t-Skip-tests-properly.patch
BuildArch:      noarch
BuildRequires:  bash
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(Getopt::Long)
# I18N::Langinfo not used at tests
BuildRequires:  perl(JSON)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(locale)
BuildRequires:  perl(Locale::Maketext::Gettext)
BuildRequires:  perl(Net::ASN)
BuildRequires:  perl(Net::DNS::Domain)
BuildRequires:  perl(Net::IP)
BuildRequires:  perl(Net::IDN::Encode)
BuildRequires:  perl(Net::RDAP) >= 0.35
BuildRequires:  perl(Net::RDAP::EPPStatusMap)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Term::Size)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(URI)
BuildRequires:  perl(vars)
# Optional run-time:
# PPI not used at tests
# Tests:
BuildRequires:  perl(common::sense)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
Requires:       perl(List::Util) >= 1.33
# To support HTTPS
Requires:       perl(LWP::Protocol::https)
Recommends:     perl(PPI)

# Filter under-specfied dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(List::Util\\)$

%description
"rdapper" is a simple RDAP client. It uses Net::RDAP to retrieve data about
internet resources (domain names, IP addresses, and autonomous systems) and
outputs the information in a human-readable format.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n App-rdapper-%{version}
# Remove pregenerated files
rm locale/*/LC_MESSAGES/*.mo

%build
./mkmo.sh
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Remove unhelpful intermediate files
# <https://github.com/gbxyz/rdapper/issues/16>
rm %{buildroot}%{perl_vendorlib}/auto/share/module/App-rdapper/rdapper.pot
rm %{buildroot}%{perl_vendorlib}/auto/share/module/App-rdapper/*/LC_MESSAGES/*.po
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset RDAPPER_LOCALE_DIR
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset RDAPPER_LOCALE_DIR
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%define l10n_dir() %lang(%1) %{perl_vendorlib}/auto/share/module/App-rdapper/%1

%files
%doc Changes README.md
%{_bindir}/rdapper
%dir %{perl_vendorlib}/App
%{perl_vendorlib}/App/rdapper{,.pm}
%dir %{perl_vendorlib}/auto/share/module/App-rdapper
%{l10n_dir de}
%{l10n_dir en}
%{l10n_dir es}
%{l10n_dir fr}
%{l10n_dir pt}
%{_mandir}/man3/App::rdapper{::,.}*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Sep 02 2025 Petr Pisar <ppisar@redhat.com> - 1.19-1
- 1.19 bump

* Thu Aug 14 2025 Petr Pisar <ppisar@redhat.com> - 1.18-1
- 1.18 bump

* Tue Jul 29 2025 Petr Pisar <ppisar@redhat.com> - 1.17-1
- 1.17 bump

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jul 04 2025 Petr Pisar <ppisar@redhat.com> - 1.15-1
- 1.15 bump

* Fri Jun 27 2025 Petr Pisar <ppisar@redhat.com> - 1.13-1
- 1.13 bump

* Thu May 22 2025 Petr Pisar <ppisar@redhat.com> - 1.12-1
- 1.12 bump

* Wed Mar 19 2025 Petr Pisar <ppisar@redhat.com> - 1.10-1
- 1.10 bump

* Fri Mar 14 2025 Petr Pisar <ppisar@redhat.com> - 1.09-1
- 1.09 bump

* Fri Feb 07 2025 Petr Pisar <ppisar@redhat.com> - 1.06-1
- 1.06 bump

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 07 2025 Petr Pisar <ppisar@redhat.com> - 1.05-1
- 1.05 bump
- Package the tests

* Fri Oct 25 2024 Petr Pisar <ppisar@redhat.com> - 1.04-1
- 1.04 bump

* Fri Sep 27 2024 Petr Pisar <ppisar@redhat.com> - 1.03-1
- 1.03 bump

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 0.08-25
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-18
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-15
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-12
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-9
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-6
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun 07 2016 Petr Pisar <ppisar@redhat.com> 0.08-1
- Specfile autogenerated by cpanspec 1.78.
