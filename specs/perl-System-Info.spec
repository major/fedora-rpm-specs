Name:           perl-System-Info
Version:        0.066
Release:        1%{?dist}
Summary:        Factory for system specific information objects
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/System-Info
Source0:        https://cpan.metacpan.org/authors/id/H/HM/HMBRAND/System-Info-%{version}.tgz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
#BuildRequires:  perl(Haiku::SysInfo)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Carp)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Warnings)

%description
System::Info tries to present system-related information, like number of
CPU's, architecture, OS and release related information in a system-
independent way. This releases the user of this module of the need to know
if the information comes from Windows, Linux, HP-UX, AIX, Solaris, Irix, or
VMS, and if the architecture is i386, x64, pa-risc2, or arm.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n System-Info-%{version}
chmod -x examples/*

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
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
%doc ChangeLog CONTRIBUTING.md examples README SECURITY.md
%dir %{perl_vendorlib}/System
%{perl_vendorlib}/System/Info*
%{_mandir}/man3/System::Info*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Jan 07 2025 Jitka Plesnikova <jplesnik@redhat.com> - 0.066-1
- 0.066 bump (rhbz#2335834)

* Tue Aug 27 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.065-1
- 0.065 bump (rhbz#2307711)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.064-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.064-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.064-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Aug 01 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.064-1
- 0.064 bump (rhbz#2227759)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.063-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.063-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 09 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.063-1
- 0.063 bump

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.062-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.062-3
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.062-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 05 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.062-1
- 0.062 bump

* Thu Aug 12 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.061-1
- 0.061 bump
- Package tests

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.060-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.060-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.060-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.060-1
- 0.060 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.059-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.059-4
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.059-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.059-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.059-1
- 0.059 bump

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.058-5
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.058-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.058-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.058-2
- Perl 5.28 rebuild

* Thu May 03 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.058-1
- 0.058 bump

* Mon Feb 12 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.057-1
- 0.057 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.056-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 25 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.056-1
- 0.056 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.055-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.055-1
- Initial release
