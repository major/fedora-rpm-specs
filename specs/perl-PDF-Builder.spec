# Support HTML language
%bcond_without perl_PDF_Builder_enables_html
# Support Markdown language
%bcond_without perl_PDF_Builder_enables_markdown
# Perform optional tests
%bcond_without perl_PDF_Builder_enables_optional_test
# Fully support PNG images with a libpng library
%bcond_without perl_PDF_Builder_enables_png
# Fully support TIFF images with libtiff library
%bcond_without perl_PDF_Builder_enables_tiff

Name:           perl-PDF-Builder
Version:        3.026
Release:        5%{?dist}
Summary:        Creation and modification of PDF files in Perl
# docs/buildDoc.pl:             same as PDF-Builder
# examples/Column.pl:           LGPL-2.1-or-later
# lib/PDF/Builder/Basic/PDF/Pages.pm:   MIT OR Artistic-1.0-Perl
# lib/PDF/Builder.pm:           LGPL-2.1-or-later
# lib/PDF/Builder/Matrix.pm:    LGPL-2.1-only ("same as PDF::API2")
# LICENSE:                      LGPL-2.1-or-later
# README:                       LGPL-2.1-or-later
# README.md:                    LGPL-2.1-or-later
License:        LGPL-2.1-or-later AND LGPL-2.1-only AND MIT
URL:            https://metacpan.org/release/PDF-Builder
Source0:        https://cpan.metacpan.org/authors/id/P/PM/PMPERRY/PDF-Builder-%{version}.tar.gz
# Renable tests, we have downstream-fixed ghostcript-9.56.1, bug #2123391,
# not suitable for the upstream
Patch0:         PDF-Builder-3.024-Don-t-skip-ghostscript-9.56.-0-1.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.26
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Zlib) >= 1
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Font::TTF::Font)
%if %{with perl_PDF_Builder_enables_tiff}
BuildRequires:  perl(Graphics::TIFF) >= 19
%endif
%if %{with perl_PDF_Builder_enables_html}
# HTML::TreeBuilder >= 5.07 not used at tests
%endif
%if %{with perl_PDF_Builder_enables_png}
BuildRequires:  perl(Image::PNG::Const)
BuildRequires:  perl(Image::PNG::Libpng) >= 0.57
%endif
BuildRequires:  perl(IO::File)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Math::Trig)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
%if %{with perl_PDF_Builder_enables_markdown}
# Text::Markdown >= 1.000031 not used at tests
%endif
BuildRequires:  perl(Unicode::UCD)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Memory::Cycle) >= 1
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
BuildRequires:  perl(version)
%if %{with perl_PDF_Builder_enables_optional_test}
# Optional tests:
# For "gs" program
BuildRequires:  font(dejavusans)
BuildRequires:  ghostscript >= 9.25.0
# For "convert" program
BuildRequires:  ImageMagick >= 6.9.7
# For tiffcp program
BuildRequires:  libtiff-tools
BuildRequires:  perl(GD)
# URW T1 font URWGothic-Book
BuildRequires:  urw-base35-gothic-fonts
%endif
Requires:       perl(Compress::Zlib) >= 1
# They can be disabled at run-time. There is an imperfect pure-Perl fallback.
%if %{with perl_PDF_Builder_enables_tiff}
Recommends:     perl(Graphics::TIFF) >= 19
%endif
%if %{with perl_PDF_Builder_enables_html}
Recommends:  perl(HTML::TreeBuilder) >= 5.07
%endif
%if %{with perl_PDF_Builder_enables_png}
Recommends:     perl(Image::PNG::Const)
Recommends:     perl(Image::PNG::Libpng) >= 0.57
%endif
%if %{with perl_PDF_Builder_enables_markdown}
Recommends:     perl(Text::Markdown) >= 1.000031
%endif

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Compress::Zlib|Test::Memory::Cycle)\\)$

# Remove disabled features.
# Originally I subpackaged PDF::Builder::Resource::XObject::Image/* modules
# which depend on the optional features. But it broke if the
# dependencies were installed, but the plugins were misssing. Also upstream
# exposes the checks for the dependencies in an API and a documentation. We would
# have to divert the code and the documentation from the upstream. Thus
# I decided to keep the plugins there and weaken the dependencies.
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Graphics::TIFF\\)|Image::PNG::)

%description
This Perl library enables you to create, import and modify documents in
Portagble Document Format (mostly compliant to PDF 1.4 version).

%package tests
Summary:        Tests for %{name}
License:        LGPL-2.1-or-later
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::Memory::Cycle) >= 1
%if %{with perl_PDF_Builder_enables_optional_test}
Requires:       font(dejavusans)
# For "gs" program
Requires:       ghostscript >= 9.25.0
# For "convert" program
Requires:       ImageMagick >= 6.9.7
# For tiffcp program
Requires:       libtiff-tools
Requires:       perl(GD)
# URW T1 font URWGothic-Book
Requires:       urw-base35-gothic-fonts
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n PDF-Builder-%{version}
# Remove disabled features
for F in \
%if !%{with perl_PDF_Builder_enables_optional_test}
    t/gd.t \
%endif
;do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
done
# Correct EOLs
perl -i -pe 's/\r$//' Changes CONTRIBUTING.md INFO/ACKNOWLEDGE.md \
    INFO/Changes_2021 INFO/SPONSORS README.md
# Help generators to recognize Perl scripts
chmod +x t/*.t

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/00-all-usable.t
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
%doc Changes contrib CONTRIBUTING.md examples README.md tools
%doc INFO/ACKNOWLEDGE.md INFO/CONVERSION INFO/DEPRECATED INFO/Changes*
%doc INFO/KNOWN_INCOMP INFO/PATENTS INFO/RoadMap INFO/SPONSORS INFO/SUPPORT
%dir %{perl_vendorlib}/PDF
%{perl_vendorlib}/PDF/Builder*
%{_mandir}/man3/PDF::Builder*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.026-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.026-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.026-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.026-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 10 2024 Petr Pisar <ppisar@redhat.com> - 3.026-1
- 3.026 bump

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.025-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jan 23 2023 Petr Pisar <ppisar@redhat.com> - 3.025-1
- 3.025 bump
- License corrected to "LGPL-2.1-or-later AND LGPL-2.1-only AND MIT"

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.024-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 05 2023 Petr Pisar <ppisar@redhat.com> - 3.024-2
- Adapt tests to EPEL9 (bug #2158422)

* Tue Sep 13 2022 Petr Pisar <ppisar@redhat.com> - 3.024-1
- 3.024 bump

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.023-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 3.023-4
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.023-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.023-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 16 2021 Petr Pisar <ppisar@redhat.com> - 3.023-1
- 3.023 bump

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 3.022-2
- Perl 5.34 rebuild

* Mon Mar 29 2021 Petr Pisar <ppisar@redhat.com> - 3.022-1
- 3.022 bump
- Package tests

* Mon Feb 08 2021 Petr Pisar <ppisar@redhat.com> - 3.021-2
- Correct BlackIs1 for LZW- and G3-compressed bitonal images

* Thu Feb 04 2021 Petr Pisar <ppisar@redhat.com> - 3.021-1
- 3.021 bump
- License changed to "LGPLv2+ and (MIT or Artistic)"

* Fri Jan 29 2021 Petr Pisar <ppisar@redhat.com> - 3.019-2
- Clarify a license
- Adapt to Image-PNG-Libpng-0.56

* Mon Nov 02 2020 Petr Pisar <ppisar@redhat.com> 3.019-1
- Specfile autogenerated by cpanspec 1.78.
