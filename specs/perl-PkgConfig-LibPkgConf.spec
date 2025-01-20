# Locate pkgconfig using Alien::pkgconf.
# Disabled by default because it creates a build cycle (perl-Alien-pkgconf →
# perl-Alien-Build → perl-PkgConfig-LibPkgConf).
%bcond_with perl_PkgConfig_LibPkgConf_enables_Alien_pkgconf
# Perform optional tests
%bcond_without perl_PkgConfig_LibPkgConf_enables_optional_test

Name:           perl-PkgConfig-LibPkgConf
Version:        0.11
Release:        23%{?dist}
Summary:        Interface to pkg-config files via libpkgconf
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/PkgConfig-LibPkgConf
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/PkgConfig-LibPkgConf-%{version}.tar.gz
# Adapt to pkgconf-1.9.4, proposed to an upstream, bug #2172714,
# <https://github.com/PerlAlien/PkgConfig-LibPkgConf/issues/15>
Patch0:         PkgConfig-LibPkgConf-0.11-adapt_to_pkgconf_1.9.4.patch
# Fix retrieving flags from package files whose Name value differs from its
# file name, proposed to an upstream, bug #2172714,
# <https://github.com/PerlAlien/PkgConfig-LibPkgConf/issues/15>
Patch1:         PkgConfig-LibPkgConf-0.11-Fix-resolving-flags-for-packages-with-a-name-differe.patch
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
%if %{with perl_PkgConfig_LibPkgConf_enables_Alien_pkgconf}
# Use Alien::pkgconf instead of some complicated guess
# script/cc_wrapper.pl and script/ld_wrapper.pl not used with Alien::pkgconf
BuildRequires:  perl(Alien::pkgconf) >= 0.12
%else
# script/cc_wrapper.pl and script/ld_wrapper.pl not used with pkgconf
BuildRequires:  pkgconf
%endif
BuildRequires:  pkgconfig(libpkgconf) >= 1.5.0
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.98
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More) >= 0.98
%if %{with perl_PkgConfig_LibPkgConf_enables_optional_test}
# Optional tests:
BuildRequires:  perl(YAML)
%endif
Requires:       perl(Carp)
# libpkgconf.so.4() changed an ABI without changing SONAME
# <https://github.com/pkgconf/pkgconf/issues/347>
Requires:       libpkgconf >= 2.1.0

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::More\\)$

%description
Many libraries in compiled languages such as C or C++ provide *.pc files to
specify the flags required for compiling and linking against those libraries.
Traditionally, the command line program pkg-config is used to query these
files. This package provides a Perl-level API using libpkgconf to these files.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
Requires:       perl(Cwd)
Requires:       perl(Test::More) >= 0.98
%if %{with perl_PkgConfig_LibPkgConf_enables_optional_test}
Requires:       perl(YAML)
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n PkgConfig-LibPkgConf-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1' "$F"
    chmod +x "$F"
done

%build
unset FFI_PLATYPUS_DEBUG
export PKG_CONFIG=%{_bindir}/pkgconf
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a corpus t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# audit_set_log() in t/client.t writed into CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} $RPM_BUILD_ROOT/*

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README
%dir %{perl_vendorarch}/auto/PkgConfig
%{perl_vendorarch}/auto/PkgConfig/LibPkgConf
%dir %{perl_vendorarch}/PkgConfig
%{perl_vendorarch}/PkgConfig/LibPkgConf
%{perl_vendorarch}/PkgConfig/LibPkgConf.pm
%{_mandir}/man3/PkgConfig::LibPkgConf.*
%{_mandir}/man3/PkgConfig::LibPkgConf::*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Neal Gompa <ngompa@fedoraproject.org> - 0.11-22
- Rebuild for pkgconf 2.3.0

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-20
- Perl 5.40 rebuild

* Mon May 27 2024 Petr Pisar <ppisar@redhat.com> - 0.11-19
- Rebuild against pkgconf-2.1.1

* Thu Feb 29 2024 Petr Pisar <ppisar@redhat.com> - 0.11-18
- Rebuild against pkgconf-2.1.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-14
- Perl 5.38 rebuild

* Tue Mar 07 2023 Petr Pisar <ppisar@redhat.com> - 0.11-13
- Fix retrieving flags from package files whose Name value differs from its
  file name (bug #2172714)

* Fri Mar 03 2023 Petr Pisar <ppisar@redhat.com> - 0.11-12
- Adapt to pkgconf-1.9.4 (bug #2172714)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-9
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-6
- Perl 5.34 rebuild

* Tue Mar 23 2021 Petr Pisar <ppisar@redhat.com> - 0.11-5
- Break build cycle (perl-Alien-pkgconf → perl-Alien-Build
  → perl-PkgConfig-LibPkgConf)
- Package tests

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-2
- Perl 5.32 rebuild

* Mon May 18 2020 Petr Pisar <ppisar@redhat.com> - 0.11-1
- 0.11 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.10-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 03 2019 Petr Pisar <ppisar@redhat.com> - 0.10-1
- 0.10 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Petr Pisar <ppisar@redhat.com> - 0.09-2
- Perl 5.28 rebuild

* Fri Jun 29 2018 Petr Pisar <ppisar@redhat.com> - 0.09-1
- 0.09 bump

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-4
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Neal Gompa <ngompa13@gmail.com> - 0.08-2
- Rebuild for pkgconf 1.4.0

* Tue Jan 02 2018 Petr Pisar <ppisar@redhat.com> - 0.08-1
- 0.08 bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-2
- Perl 5.26 rebuild

* Thu Mar 16 2017 Petr Pisar <ppisar@redhat.com> - 0.07-1
- 0.07 bump

* Thu Mar 09 2017 Petr Pisar <ppisar@redhat.com> 0.06-1
- Specfile autogenerated by cpanspec 1.78.
