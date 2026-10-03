Name:           perl-HTML-Query
Version:        0.09
Release:        2%{?dist}
Summary:        JQuery-like selection queries for HTML::Element
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/HTML-Query
Source0:        https://www.cpan.org/modules/by-module/HTML/HTML-Query-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Badger) >= 0.03
BuildRequires:  perl(Badger::Class)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# tests
BuildRequires:  perl(Badger::Filesystem)
BuildRequires:  perl(Badger::Test)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(lib)
# runtime
BuildRequires:  perl(HTML::Tree) >= 3.23
Requires:       perl(HTML::Tree) >= 3.23

%description
The HTML::Query module is an add-on for the HTML::Tree module set. It
provides a simple way to select one or more elements from a tree using a
query syntax inspired by jQuery. This selector syntax will be reassuringly
familiar to anyone who has ever written a CSS selector.

%prep
%setup -q -n HTML-Query-%{version}

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
%dir %{perl_vendorlib}/HTML/
%{perl_vendorlib}/HTML/Query.pm
%{_mandir}/man3/HTML::Query.3pm*

%changelog
* Sun Sep 27 2026 Xavier Bachelot <xavier@bachelot.org> 0.09-2
- Review fixes (RHBZ#2501791)

* Thu May 21 2026 Xavier Bachelot <xavier@bachelot.org> 0.09-1
- Initial specfile
