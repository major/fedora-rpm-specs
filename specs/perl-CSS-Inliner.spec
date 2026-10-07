Name:           perl-CSS-Inliner
Version:        4027
Release:        1%{?dist}
Summary:        Library for converting CSS <style> blocks to inline styles
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/CSS-Inliner
Source0:        https://metacpan.org/modules/by-module/CSS/CSS-Inliner-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(HTML::Query) >= 0.09
BuildRequires:  perl(HTML::TreeBuilder) >= 5.03
BuildRequires:  perl(LWP)
BuildRequires:  perl(URI)
# test
BuildRequires:  perl(charnames)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(Test::More)
# runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Encoding::FixLatin)

%description
Library for converting CSS style blocks into inline styles in an HTML
document. Specifically this is intended for the ease of generating HTML
emails. This is useful as certain email clients don't support top level
<style> declarations despite it being 2017.

%prep
%setup -q -n CSS-Inliner-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc ChangeLog README
%dir %{perl_vendorlib}/CSS/
%{perl_vendorlib}/CSS/Inliner*
%{_mandir}/man3/CSS::Inliner*3pm*

%changelog
* Thu May 21 2026 Xavier Bachelot <xavier@bachelot.org> 4027-1
- Initial specfile
