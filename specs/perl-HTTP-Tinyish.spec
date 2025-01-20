Name:           perl-HTTP-Tinyish
Version:        0.19
Release:        4%{?dist}
Summary:        HTTP::Tiny compatible HTTP client wrappers
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTTP-Tinyish
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/HTTP-Tinyish-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Temp)
# BuildRequires:  perl(File::Which)
# BuildRequires:  perl(HTTP::Tiny) >= 0.054
# BuildRequires:  perl(IPC::Run3)
# BuildRequires:  perl(LWP) >= 5.802
# BuildRequires:  perl(LWP::Protocol::https)
# BuildRequires:  perl(LWP::UserAgent)
# BuildRequires:  perl(parent)
# Tests only
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(:HTTP-Tinyish:backend) = %{version}
Recommends:     perl(HTTP::Tinyish::LWP)

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(HTTP::Tiny\\)$

%description
HTTP::Tinyish is a wrapper module for HTTP client modules LWP, HTTP::Tiny
and HTTP client software curl and wget.

%package        Curl
Summary:        HTTP::Tinyish curl backend
Requires:       curl
Provides:       perl(:HTTP-Tinyish:backend) = %{version}

%description Curl
%{summary}.

%package        HTTPTiny
Summary:        HTTP::Tinyish HTTP::Tiny backend
Requires:       perl(HTTP::Tiny) >= 0.054
Provides:       perl(:HTTP-Tinyish:backend) = %{version}

%description HTTPTiny
%{summary}.

%package        LWP
Summary:        HTTP::Tinyish LWP backend
Provides:       perl(:HTTP-Tinyish:backend) = %{version}
Recommends:     perl(LWP::Protocol::https)

%description LWP
%{summary}.

%package        Wget
Summary:        HTTP::Tinyish wget backend
Requires:       wget
Provides:       perl(:HTTP-Tinyish:backend) = %{version}

%description Wget
%{summary}.

%prep
%setup -q -n HTTP-Tinyish-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
# Nothing is really tested; this could be completely
# disabled to save us some builddeps but oh well.
%{make_build} test

%files
%license LICENSE
%doc Changes README
%dir %{perl_vendorlib}/HTTP
%dir %{perl_vendorlib}/HTTP/Tinyish
%{perl_vendorlib}/HTTP/Tinyish.pm
%{perl_vendorlib}/HTTP/Tinyish/Base.pm
%{_mandir}/man3/HTTP::Tinyish.*

%files Curl
%license LICENSE
%{perl_vendorlib}/HTTP/Tinyish/Curl.pm

%files HTTPTiny
%license LICENSE
%{perl_vendorlib}/HTTP/Tinyish/HTTPTiny.pm

%files LWP
%license LICENSE
%{perl_vendorlib}/HTTP/Tinyish/LWP.pm

%files Wget
%license LICENSE
%{perl_vendorlib}/HTTP/Tinyish/Wget.pm

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 0.19-3
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Mar 31 2024 Emmanuel Seyman <emmanuel@seyman.fr> - 0.19-1
- Update to 0.19

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 26 2022 Emmanuel Seyman <emmanuel@seyman.fr> - 0.18-1
- Update to 0.18

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-7
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-4
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 12 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 0.17-1
- Update to 0.17

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-2
- Perl 5.32 rebuild

* Sun May 17 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 0.16-1
- Update to 0.16
- Specify full path to perl everywhere
- Use %%{make_install} instead of "make pure_install"
- Use %%{make_build} instead of make

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 30 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 0.15-1
- Update to 0.15

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-2
- Perl 5.28 rebuild

* Sun Apr 22 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 0.14-1
- Update to 0.14
- Add a version to the virtual provide HTTP-Tinyish:backend

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-2
- Perl 5.26 rebuild

* Sun Feb 12 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 0.12-1
- Update to 0.12

* Mon Feb 06 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 0.11-1
- Update to 0.11

* Sun Jan 08 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 0.10-1
- Update to 0.10

* Sun Nov 20 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 0.09-1
- Update to 0.09

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Petr Šabata <contyk@redhat.com> - 0.07-1
- 0.07 bump

* Fri Dec 11 2015 Petr Šabata <contyk@redhat.com> - 0.06-2
- Address the reviewer's concerns

* Thu Dec 10 2015 Petr Šabata <contyk@redhat.com> 0.06-1
- Initial packaging
