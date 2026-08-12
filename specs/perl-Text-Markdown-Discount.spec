Name:           perl-Text-Markdown-Discount
Version:        0.18
Release:        2%{?dist}
Summary:        Fast function for converting markdown to HTML (requires C compiler)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Text-Markdown-Discount
Source0:        http://www.cpan.org/modules/by-module/Text/Text-Markdown-Discount-%{version}.tar.gz
# https://salsa.debian.org/perl-team/modules/packages/libtext-markdown-discount-perl/-/raw/debian/0.18-1/debian/patches/use-system-markdown.patch 
Patch0:         perl-Text-Markdown-Discount-0.18-use_system_markdown.patch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  libmarkdown-devel
BuildRequires:  sed
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
# runtime
BuildRequires:  perl(Exporter)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# tests
BuildRequires:  perl(Test::More)

%description
Text::Markdown::Discount is a perl interface to the Discount library, a C
implementation of John Gruber's markdown.

%prep
%setup -q -n Text-Markdown-Discount-%{version}
sed -i -e '/^discount-2.2.7d/d' MANIFEST
rm -rf discount-2.2.7d/
%patch -P0 -p1

%build
perl Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorarch}/auto/Text/
%{perl_vendorarch}/Text/
%{_mandir}/man3/Text::Markdown::Discount.3pm*

%changelog
* Mon Aug 10 2026 Xavier Bachelot <xavier@bachelot.org> 0.18-2
- Fixed from review

* Mon Jul 20 2026 Xavier Bachelot <xavier@bachelot.org> 0.18-1
- Initial specfile
