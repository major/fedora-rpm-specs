Name:           perl-Image-PNG-Libpng
Version:        0.57
Release:        9%{?dist}
Summary:        Perl interface to the libpng library
# lib/Image/PNG/Const.pm:   GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/Image/PNG/Libpng.pod: GPL-1.0-or-later OR Artistic-1.0-Perl
## Not in any binary package
# Makefile.PL:              GPL-1.0-or-later OR Artistic-1.0-Perl
# repackage.sh:             GPL-2.0-or-later
# t/libpng/PngSuite.LICENSE:    FSFUL-like (contrib/pngsuite bundled from libpng)
## Stripped from the source archive
# examples/life.png:        CC-BY-NC-2.5
# examples/life-gray.png:   CC-BY-NC-2.5
# t/emoticon.png:           CC-BY-NC-2.5
# t/tantei-san.png:         "I don't have permission to disseminate it."
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Image-PNG-Libpng
# Original archive from
# <https://cpan.metacpan.org/authors/id/B/BK/BKB/Image-PNG-Libpng-%%{version}.tar.gz>
# contains files with a bad license. They were stripped with ./repackage.sh
# script. <https://github.com/benkasminbullock/image-png-libpng/issues/36>.
Source0:        Image-PNG-Libpng-%{version}_repackaged.tar.gz
Source1:        repackage.sh
# Adapt tests to the stripped source archive. Not suitable for an upstream.
# <https://github.com/benkasminbullock/image-png-libpng/issues/36>.
Patch0:         Image-PNG-Libpng-0.57-Remove-tests-depending-on-proprietary-files.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
# git-core for a binary Image-PNG-Libpng-0.57-Remove-tests-depending-on-proprietary-files.patch
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Constant)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# pkgconf-pkg-config for pkg-config tool
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(libpng)
# Run-time:
BuildRequires:  perl(constant)
# Data::Dumper not used at tests
# Data::Validate::URI not used at tests
# LWP::Simple not used at tests
BuildRequires:  perl(XSLoader)
# Optional run-time:
# JSON::Create not used at tests
# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)

# Remove private modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(IPNGLT\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(IPNGLT\\)

%description
Image::PNG::Libpng is a Perl library for accessing the contents of PNG
(Portable Network Graphics) images. It enables Perl to read and write files in
the PNG format.

%package tools
Summary:        Tools for inspecting PNG images
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Suggests:       perl(Data::Validate::URI)
Suggests:       perl(JSON::Create)
Suggests:       perl(LWP::Simple)

%description tools
pnginspect tool prints a text representation of the data within a PNG image
file to standard output. If you have Data::Validate::URI and LWP::Simple
installed, you can also use it to examine PNG files on the web.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -S git -n Image-PNG-Libpng-%{version}
# Do not install author scripts
for F in get-pixel.pl nicemake.pl t/make-tEXT.pl; do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
done
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL --check INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# t/io.t and others write into CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/t "$DIR"
pushd "$DIR"
prove -I . -j 1
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
# Tests are not parallel-safe, they overwrite same-named files
make test

%files
%doc Changes
%dir %{perl_vendorarch}/auto/Image
%{perl_vendorarch}/auto/Image/PNG
%dir %{perl_vendorarch}/Image
%{perl_vendorarch}/Image/PNG
%{_mandir}/man3/Image::PNG::*

%files tools
%{_bindir}/pnginspect
%{_mandir}/man1/pnginspect.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.57-9
- Perl 5.38 rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.57-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Petr Pisar <ppisar@redhat.com> - 0.57-7
- Convert a License tag to the SPDX format

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.57-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.57-5
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.57-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.57-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.57-2
- Perl 5.34 rebuild

* Tue Apr 27 2021 Petr Pisar <ppisar@redhat.com> - 0.57-1
- 0.57 bump
- Package the tests

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 04 2021 Petr Pisar <ppisar@redhat.com> - 0.56-1
- 0.56 bump

* Mon Dec 21 2020 Petr Pisar <ppisar@redhat.com> - 0.54-1
- 0.54 bump

* Sun Dec 13 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.52-1
- 0.52 bump

* Thu Dec 10 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.49-1
- 0.49 bump

* Tue Nov 24 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.48-1
- 0.48 bump

* Mon Nov 02 2020 Petr Pisar <ppisar@redhat.com> 0.47-1
- Specfile autogenerated by cpanspec 1.78.
