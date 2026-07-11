Name:           perl-Font-FreeType
Version:        0.18
Release:        %{autorelease}
Summary:        Read font files and render glyphs from Perl using FreeType2
URL:            https://metacpan.org/dist/Font-FreeType
Source0:        https://cpan.metacpan.org/authors/id/D/DM/DMOL/Font-FreeType-%{version}.tar.gz

# "This library is free software; you can redistribute it and/or modify
# it under the same terms as Perl itself."
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

# t/data/copyright.txt:
SourceLicense:  Bitstream-Vera AND (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Fedora-Public-Domain

BuildRequires:  coreutils
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Devel::CheckLib)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Pod::Checker)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter

%{?perl_default_filter}

%description
This module allows Perl programs to conveniently read information from font
files. All the font access is done through the FreeType2 library, which
supports many formats. It can render images of characters with high-quality
hinting and antialiasing, extract metrics information, and extract the
outlines of characters in scalable formats like TrueType.


%prep
%autosetup -n Font-FreeType-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}


%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%files
%license Artistic
%license Copying
%doc Changes
%doc TODO
%doc examples
%dir %{perl_vendorarch}/Font
%dir %{perl_vendorarch}/Font/FreeType
%{perl_vendorarch}/Font/FreeType.pm
%{perl_vendorarch}/Font/FreeType/BoundingBox.pm
%{perl_vendorarch}/Font/FreeType/CharMap.pm
%{perl_vendorarch}/Font/FreeType/Face.pm
%{perl_vendorarch}/Font/FreeType/Glyph.pm
%{perl_vendorarch}/Font/FreeType/NamedInfo.pm
%dir %{perl_vendorarch}/auto/Font
%dir %{perl_vendorarch}/auto/Font/FreeType
%{perl_vendorarch}/auto/Font/FreeType/FreeType.so
%{_mandir}/man3/Font::FreeType.3pm.gz
%{_mandir}/man3/Font::FreeType::BoundingBox.3pm.gz
%{_mandir}/man3/Font::FreeType::CharMap.3pm.gz
%{_mandir}/man3/Font::FreeType::Face.3pm.gz
%{_mandir}/man3/Font::FreeType::Glyph.3pm.gz
%{_mandir}/man3/Font::FreeType::NamedInfo.3pm.gz


%changelog
%{autochangelog}
