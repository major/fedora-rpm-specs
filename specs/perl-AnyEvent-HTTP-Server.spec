%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(AnyEvent|Digest::SHA1|JSON::XS\\)$

Name:           perl-AnyEvent-HTTP-Server
Version:        1.99998
Release:        7%{?dist}
Summary:        AnyEvent HTTP/1.1 Server
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://github.com/Mons/AnyEvent-HTTP-Server-II
Source0:        https://github.com/Mons/AnyEvent-HTTP-Server-II/archive/refs/tags/%{version}/AnyEvent-HTTP-Server-II-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(AnyEvent) >= 5
BuildRequires:  perl(AnyEvent::Handle)
BuildRequires:  perl(AnyEvent::Socket)
BuildRequires:  perl(AnyEvent::Util)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::SHA1) >= 2
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(feature)
BuildRequires:  perl(JSON::XS) >= 3
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# tests
BuildRequires:  perl(EV)
BuildRequires:  perl(Class::XSAccessor)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Easy) >= 0.04
BuildRequires:  perl(Test::Pod)

Requires:       perl(AnyEvent) >= 5
Requires:       perl(Digest::SHA1) >= 2
Requires:       perl(JSON::XS) >= 3

%description
AnyEvent::HTTP::Server is a very fast asynchronous HTTP server written in
perl. It has been tested in high load production environments and may be
considered both fast and stable.

%prep
%setup -q -n AnyEvent-HTTP-Server-II-%{version}
perl -MConfig -pi -e 's,#!.*perl,$Config{startperl},' ex/*.pl

%build
unset AUTHOR
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}

%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%files
%doc Changes ex README.md
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.99998-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.99998-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Feb  2 2024 Yanko Kaneti <yaneti@declera.com> - 1.99998-5
- SPDX migration

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.99998-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.99998-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.99998-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 30 2023 Yanko Kaneti <yaneti@declera.com> - 1.99998-1
- Update to 1.99998

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.99996-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 11 2022 Yanko Kaneti <yaneti@declera.com> - 1.99996-1
- Update to 1.99996

* Mon Aug  8 2022 Yanko Kaneti <yaneti@declera.com> - 1.99995-1.20220727gitd464672
- Recent snapshot

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.99981-14.20190523gitb09c2c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.99981-13.20190523gitb09c2c7
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.99981-12.20190523gitb09c2c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.99981-11.20190523gitb09c2c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.99981-10.20190523gitb09c2c7
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.99981-9.20190523gitb09c2c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.99981-8.20190523gitb09c2c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.99981-7.20190523gitb09c2c7
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.99981-6.20190523gitb09c2c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.99981-5.20190523gitb09c2c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun  8 2019 Yanko Kaneti <yaneti@declera.com> - 1.99981-4.20190523gitb09c2c7
- Incorporate some more review feedback

* Thu Jun  6 2019 Yanko Kaneti <yaneti@declera.com> - 1.99981-3.20190523gitb09c2c7
- Incorporate review feedack (#1713315)

* Thu May 23 2019 Yanko Kaneti <yaneti@declera.com> - 1.99981-2.20190523gitb09c2c7
- First try
- Specfile autogenerated by cpanspec 1.78 and modified after
