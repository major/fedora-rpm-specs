# Support human color names
%bcond_without perl_Graphics_Toolkit_Color_enables_color_names

Name:           perl-Graphics-Toolkit-Color
Version:        1.71
Release:        5%{?dist}
Summary:        Color palette constructor
# lib/Graphics/Toolkit/Color.pm:        GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/Graphics/Toolkit/Color/Constant.pm:   GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/Graphics/Toolkit/Color/Values.pm:     GPL-1.0-or-later OR Artistic-1.0-Perl
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
BuildRequires:  perl(Carp) >= 1.35
BuildRequires:  perl(Exporter) >= 5
%if %{with perl_Graphics_Toolkit_Color_enables_color_names}
# Optional run-time:
# Graphics::ColorNames not used at tests
%endif
# Tests:
BuildRequires:  perl(Test::More) >= 1.3
BuildRequires:  perl(Test::Warn) >= 0.30
Requires:       perl(Carp) >= 1.35
Requires:       perl(Exporter) >= 5
%if %{with perl_Graphics_Toolkit_Color_enables_color_names}
Recommends:     perl(Graphics::ColorNames)
%endif

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Carp|Exporter|Test::More|Test::Warn)\\)$

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
Requires:       perl(Test::Warn) >= 0.30

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Graphics-Toolkit-Color-%{version}
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
