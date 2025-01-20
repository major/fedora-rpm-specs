# Disable t/ucd.t, it consumes a lot of memory, CPAN RT#108739
%bcond_with ucdtest

Name:           perl-Text-Bidi
Version:        2.18
Release:        13%{?dist}
Summary:        Unicode bidirectional algorithm using libfribidi
# LICENSE:          GPL-1.0-or-later OR Artistic-1.0-Perl
# t/MirrorTest.txt: Unicode-DFS-2016 (a copy of
#                   <https://www.unicode.org/Public/14.0.0/ucd/BidiMirroring.txt>)
## not in the binary packages
%if !%{with ucdtest}
# t/BidiTest.txt:   Unicode-DFS-2015 (a copy of
#                   <https://www.unicode.org/Public/6.2.0/ucd/BidiTest.txt>)
%endif
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-Bidi
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAMENSKY/Text-Bidi-%{version}.tar.gz
# bidi is a plugin, CPAN RT#108737
Patch0:         Text-Bidi-2.12-Remove-script-attributes-from-bidi.patch
# Respect swig failures, proposed to the upstream,
# <https://github.com/mkamensky/Text-Bidi/pull/13>
Patch1:         Text-Bidi-2.18-Do-not-ignore-Swig-failures.patch
# Adjust a test for an out-tree testing, not suitable for upstream
Patch2:         Text-Bidi-2.16-Skip-nonexisting-scripts.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Prefer pkgconfig for locating fribidi
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(strict)
BuildRequires:  perl(version) >= 0.77
BuildRequires:  perl(warnings)
BuildRequires:  pkgconfig(fribidi) >= 1.0.0
BuildRequires:  swig
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(integer)
BuildRequires:  perl(open)
BuildRequires:  perl(overload)
BuildRequires:  perl(Tie::Array)
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(charnames)
%if %{with ucdtest}
BuildRequires:  perl(Data::Dumper)
%endif
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)
# Optional tests:
# CPAN::Meta 2.120900 not useful

%description
This Perl module provides basic support for the Unicode bidirectional (Bidi)
text algorithm, for displaying text consisting of both left-to-right and
right-to-left written languages (such as Hebrew and Arabic.) It does so via
a SWIG interface file to the libfribidi library.

%package urxvt
Summary:        Unicode bidirectional text support for urxvt
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Requires:       perl(Encode)
Requires:       perl(Text::Bidi)
Requires:       perl(Text::Bidi::Constants)
Requires:       rxvt-unicode

%description urxvt
This extension filters the text displayed by Urxvt, so that Bi-directional 
text (e.g., Hebrew or Arabic mixed with English) is displayed correctly.

%package tests
Summary:        Tests for %{name}
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND Unicode-DFS-2016
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n Text-Bidi-%{version}
# Delete SWIG-generated files to regenerate them
rm private.c lib/Text/Bidi/private.pm
perl -i -ne 'print $_ unless m{^private\.c}' MANIFEST
perl -i -ne 'print $_ unless m{^lib/Text/Bidi/private\.pm}' MANIFEST
# Remove a large unsed test file,
# Disable t/ucd.t, it consumes a lot of memory, CPAN RT#108739
for F in \
    t/BidiTest.txt.gz \
%if !%{with ucdtest}
    t/BidiTest.txt t/ucd.t \
%endif
; do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
done
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
find %{buildroot} -type f -name '*.3pm' -size 0 -delete
%{_fixperms} %{buildroot}/*
install -d -m 0755 %{buildroot}%{_libdir}/urxvt/perl
install -m 0644 -t %{buildroot}%{_libdir}/urxvt/perl misc/bidi
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
# Packaged with %%license
rm %{buildroot}%{_libexecdir}/%{name}/t/license.txt
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset PERL_COMPILE_TEST_DEBUG
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset PERL_COMPILE_TEST_DEBUG
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README
%{_bindir}/fribidi.pl
%dir %{perl_vendorarch}/auto/Text
%{perl_vendorarch}/auto/Text/Bidi
%dir %{perl_vendorarch}/Text
%{perl_vendorarch}/Text/Bidi
%{perl_vendorarch}/Text/Bidi.pm
%{_mandir}/man1/fribidi.pl.1*
%{_mandir}/man3/Text::Bidi.*
%{_mandir}/man3/Text::Bidi::*

%files urxvt
%license LICENSE
%{_libdir}/urxvt/perl/bidi

%files tests
%license t/license.txt
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 2.18-12
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Jitka Plesnikova <jplesnik@redhat.com> - 2.18-10
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 2.18-6
- Perl 5.38 rebuild

* Fri Jan 20 2023 Petr Pisar <ppisar@redhat.com> - 2.18-5
- Respect swig failures

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 28 2022 Petr Pisar <ppisar@redhat.com> - 2.18-3
- Correct tests license to (GPL-1.0-or-later OR Artistic-1.0-Perl) AND
  Unicode-DFS-2016

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 07 2022 Petr Pisar <ppisar@redhat.com> - 2.18-1
- 2.18 bump

* Wed Jun 29 2022 Petr Pisar <ppisar@redhat.com> - 2.17-1
- 2.17 bump
- Correct perl-Text-Bidi-tests license to ((GPL+ or Artistic) and Unicode)
- Migrate License tags to SPDX syntax

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.16-2
- Perl 5.36 rebuild

* Mon Apr 25 2022 Petr Pisar <ppisar@redhat.com> - 2.16-1
- 2.16 bump
- Install the tests
- Fix Text::Bidi::Array::Long on big-endian (bug #2078251)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.15-10
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.15-7
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Petr Pisar <ppisar@redhat.com> - 2.15-5
- Build-require blib for tests

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.15-3
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 25 2018 Petr Pisar <ppisar@redhat.com> - 2.15-1
- 2.15 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.12-10
- Perl 5.28 rebuild

* Tue Jun 05 2018 Petr Pisar <ppisar@redhat.com> - 2.12-9
- Remove empty Text::Bidi::private(3pm) manual page

* Thu Mar  1 2018 Florian Weimer <fweimer@redhat.com> - 2.12-8
- Rebuild with new redhat-rpm-config/perl build flags

* Wed Feb 28 2018 Petr Pisar <ppisar@redhat.com> - 2.12-7
- Adapt to fribidi-1.0 (CPAN RT#124618)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.12-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 03 2016 Petr Pisar <ppisar@redhat.com> - 2.12-1
- 2.12 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.11-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Petr Pisar <ppisar@redhat.com> 2.11-1
- Specfile autogenerated by cpanspec 1.78.
