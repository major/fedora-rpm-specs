# Fullarch because %%{perl_vendorarch} is baked into packaged alien.json
%global debug_package %{nil}

Name:           perl-Alien-Brotli
Version:        0.2.2
Release:        9%{?dist}
Summary:        Find and install the Brotli compressor
License:        MIT
URL:            http://metacpan.org/dist/Alien-Brotli
Source0:        http://cpan.metacpan.org/authors/id/R/RR/RRWO/Alien-Brotli-v%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  sed
BuildRequires:  make
BuildRequires:  brotli
BuildRequires:  brotli-devel
BuildRequires:  libbrotli

BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.14
BuildRequires:  perl(Alien::Base)
BuildRequires:  perl(Alien::Build) >= 0.32
BuildRequires:  perl(Alien::Build::MM) >= 0.32
BuildRequires:  perl(Alien::Build::Plugin::Probe::CommandLine)
BuildRequires:  perl(Alien::cmake3) >= 0.02
BuildRequires:  perl(alienfile)
BuildRequires:  perl(base)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Env::ShellWords) >= 0.01
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.52
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Sort::Versions)
BuildRequires:  perl(strict)
BuildRequires:  perl(version) >= 0.77
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Alien)
BuildRequires:  perl(Test::Alien::Diag)
BuildRequires:  perl(Test::More) >= 0.88
# Runtime
Requires:       perl(constant)
# We need specific versions at runtime, since alien.json bakes the version in at build-time
Requires:       brotli %(perl -e 'print qq{ = $1} if qx{brotli --version} =~ m{([\d+\.]+)}')
Requires:       libbrotli %(perl -e 'print qq{ = $1} if qx{brotli --version} =~ m{([\d+\.]+)}')

%description
This distribution installs the brotli compressor, so that it can be used by
other distributions, and provides a way to find the executable.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(Test::Harness)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Alien-Brotli-v%{version}
# Disable test for prerequisites
rm t/00-report-prereqs.{t,dd}
# Stop MakeMaker from throwing warnings
sed -ni '/00-report-prereqs/!p' MANIFEST
sed -ni '/Alien::bc::GNU/!p' Makefile.PL

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
# Remove alienfile
rm %{buildroot}%{perl_vendorarch}/auto/share/dist/Alien-Brotli/_alien/alienfile
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/release*
rm %{buildroot}%{_libexecdir}/%{name}/t/author*
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Alien*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Oct 18 2023 Petr Salaba <salabapetr@email.cz> - 0.2.2-5
- Rebuilt for brotli 1.1.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jan 24 2023 Petr Salaba <psalaba@redhat.com> - 0.2.2-3
- Fix incorrect license
- Remove unused dependencies

* Tue Jan 17 2023 Petr Salaba <psalaba@redhat.com> - 0.2.2-2
- Fix rpmlint issues
- Remove devel package from runtime requirements

* Tue Jan 17 2023 Petr Salaba <psalaba@redhat.com> - 0.2.2-1
- Initial spec
