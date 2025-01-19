# Fullarch because %%{perl_vendorarch} is backed into packaged alien.json.
%global debug_package %{nil}

Name:           perl-Alien-autoconf
Version:        0.20
Release:        3%{?dist}
Summary:        Find autoconf
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Alien-autoconf
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Alien-autoconf-%{version}.tar.gz
# Implement system installation, not suitable for upstream,
# <https://github.com/PerlAlien/Alien-autoconf/issues/2>
Patch0:         Alien-autoconf-0.18-Implement-system-installation.patch
BuildRequires:  autoconf >= 2.69
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Alien::Build::MM) >= 0.32
# alienfile version from Alien::Build in META
BuildRequires:  perl(alienfile) >= 0.49
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Which)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Sort::Versions)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Alien::Base) >= 0.038
BuildRequires:  perl(base)
# Tests:
BuildRequires:  perl(Alien::Build::Plugin::Build::Autoconf) >= 0.47
BuildRequires:  perl(Alien::m4)
BuildRequires:  perl(Env)
BuildRequires:  perl(File::chdir)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test2::V0) >= 0.000121
BuildRequires:  perl(Test::Alien) >= 2.52
# alien.json bakes in autoconf version at build-time
Requires:       autoconf %(perl -e 'print qq{ = $1} if qx{autoconf --version} =~ m{([\d+\.]+)}' 2>/dev/null)
Requires:       perl(Alien::Base) >= 0.038

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Alien::Base|Test2::V0|Test::More)\\)$

%description
This distribution provides autoconf so that it can be used by other Perl
distributions that are on CPAN. This is most commonly necessary when creating
other Aliens that target a autoconf project that does not ship with
a configure script.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test2::V0) >= 0.000121

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n Alien-autoconf-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 &&
!s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Remove a useless alienfile which pulls in many dependencies, bug #2134804
rm %{buildroot}/%{perl_vendorarch}/auto/share/dist/Alien-autoconf/_alien/alienfile
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a corpus t %{buildroot}%{_libexecdir}/%{name}
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
%doc Changes README
%dir %{perl_vendorarch}/Alien
%{perl_vendorarch}/Alien/autoconf.pm
%dir %{perl_vendorarch}/auto/Alien
%{perl_vendorarch}/auto/Alien/autoconf
%dir %{perl_vendorarch}/auto/share
%dir %{perl_vendorarch}/auto/share/dist
%{perl_vendorarch}/auto/share/dist/Alien-autoconf
%{_mandir}/man3/Alien::autoconf.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 16 2024 Petr Pisar <ppisar@redhat.com> - 0.20-1
- 0.20 bump

* Tue Feb 20 2024 Petr Pisar <ppisar@redhat.com> - 0.19-6
- Rebuild against autoconf-2.72 (bug #2264959)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 Petr Pisar <ppisar@redhat.com> - 0.19-1
- 0.19 bump

* Fri Oct 14 2022 Petr Pisar <ppisar@redhat.com> 0.18-1
- 0.18 version packaged
