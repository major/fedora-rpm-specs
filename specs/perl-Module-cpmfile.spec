Name:           perl-Module-cpmfile
Version:        0.006
Release:        10%{?dist}
Summary:        Parse cpmfile
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-cpmfile
Source0:        https://cpan.metacpan.org/authors/id/S/SK/SKAJI/Module-cpmfile-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter 
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Config)
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.130
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(YAML::PP) >= 0.027
# Tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::CPANfile) >= 1.1004
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(utf8)
Requires:       perl(CPAN::Meta::Requirements) >= 2.130
Requires:       perl(Exporter) >= 5.57
Requires:       perl(YAML::PP) >= 0.027

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Util\\)

# Filter unversion dependencies
%global __requires_exclude %{__requires_exclude}|^perl\\(CPAN::Meta::Requirements\\)\s*$
%global __requires_exclude %{__requires_exclude}|^perl\\(Exporter\\)\s*$
%global __requires_exclude %{__requires_exclude}|^perl\\(YAML::PP\\)\s*$

%description
cpmfile (usually saved as cpm.yml) is yet another file format for
describing module dependencies, and Module::cpmfile helps you parse it.

cpmfile will be used mainly by App::cpm.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Module-cpmfile-%{version}

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*
# Remove empty man pages
rm -rf %{buildroot}/%{_mandir}/man3/Module::cpmfile::Util*
rm -rf %{buildroot}/%{_mandir}/man3/Module::cpmfile::Prereqs*

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
./Build test

%files
%license LICENSE
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.006-2
- Perl 5.36 rebuild

* Sun Feb 20 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.006-1
- 0.006 bump

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 04 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.005-1
- 0.005 bump

* Sun Dec 12 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.003-1
- 0.003 bump

* Tue Aug 03 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.002-1
- 0.002 bump

* Thu Jul 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.001-1
- Specfile autogenerated by cpanspec 1.78.
