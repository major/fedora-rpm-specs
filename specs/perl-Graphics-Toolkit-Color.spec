Name:           perl-Graphics-Toolkit-Color
Version:        1.972
Release:        2%{?dist}
Summary:        Color palette constructor
# lib/Graphics/Toolkit/Color.pm:        GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/Graphics/Toolkit/Color/Name.pm:       GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/Graphics/Toolkit/Color/Name/Constant.pm:  GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/Graphics/Toolkit/Color/Name/Scheme.pm:    GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/Graphics/Toolkit/Color/Space.pm:      GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/Graphics/Toolkit/Color/Space/Hub.pm:  GPL-1.0-or-later OR Artistic-1.0-Perl
# LICENSE:      GPL-1.0-or-later OR Artistic-1.0-Perl
# README:       GPL-1.0-or-later OR Artistic-1.0-Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Graphics-Toolkit-Color
Source0:        https://cpan.metacpan.org/authors/id/L/LI/LICHTKIND/Graphics-Toolkit-Color-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.12.0
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Exporter) >= 5
# Optional run-time:
# Graphics::ColorNames::$schema, where $schema is a user-supplied string, is
# loaded under eval in Graphics::Toolkit::Color::Name::try_get_scheme(). These
# schemata are spread over many packages, we cannot and should not list all of
# them we know of. None of them is used at tests.
# Tests:
BuildRequires:  perl(Test::More) >= 1.3
Requires:       perl(Exporter) >= 5

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Exporter|Test::More|)\\)$

%description
Read-only, color-holding Perl objects with methods to obtain their RGB, HSL,
and YIQ values and if possible a name. This is because humans access colors on
hardware level (eye) in RGB, on cognition level in HSL (brain) and on cultural
level (language) with names. There objects also have methods for measuring
color distances and generating related color objects like gradients and
complements. Having easy access to all three and some color math should enable
you to get the color palette you desire.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness 
Requires:       perl(Test::More) >= 1.3

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n Graphics-Toolkit-Color-%{version}
chmod +x t/*.t

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
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING README
%dir %{perl_vendorlib}/Graphics
%dir %{perl_vendorlib}/Graphics/Toolkit
%{perl_vendorlib}/Graphics/Toolkit/Color*
%{_mandir}/man3/Graphics::Toolkit::Color*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.972-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Mon Sep 01 2025 Petr Pisar <ppisar@redhat.com> - 1.972-1
- 1.972 bump

* Thu Aug 21 2025 Petr Pisar <ppisar@redhat.com> - 1.92-1
- 1.92 bump

* Fri Aug 15 2025 Petr Pisar <ppisar@redhat.com> - 1.91-1
- 0.91 bump

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.71-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.71-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.71-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.71-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.71-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Sep 22 2023 Petr Pisar <ppisar@redhat.com> - 1.71-1
- 1.71 bump

* Thu Sep 21 2023 Petr Pisar <ppisar@redhat.com> - 1.70-1
- 1.70 bump

* Tue Sep 12 2023 Petr Pisar <ppisar@redhat.com> - 1.61-1
- 1.61 bump

* Tue Aug 22 2023 Petr Pisar <ppisar@redhat.com> - 1.54-1
- 1.54 bump

* Fri Aug 11 2023 Petr Pisar <ppisar@redhat.com> - 1.53-1
- 1.53 bump

* Thu Aug 10 2023 Petr Pisar <ppisar@redhat.com> - 1.51-1
- 1.51 bump

* Mon Jul 24 2023 Petr Pisar <ppisar@redhat.com> - 1.09-1
- 1.09 bump

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 25 2023 Petr Pisar <ppisar@redhat.com> - 1.08-1
- 1.08 bump

* Mon Jan 23 2023 Petr Pisar <ppisar@redhat.com> - 1.07-1
- 1.07 bump

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 08 2022 Petr Pisar <ppisar@redhat.com> - 1.04-1
- 1.04 bump

* Mon Oct 24 2022 Petr Pisar <ppisar@redhat.com> 1.00-1
- 1.00 version packaged
