Name:           perl-HTTP-Entity-Parser
Version:        0.25
Release:        14%{?dist}
Summary:        PSGI compliant HTTP Entity Parser
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTTP-Entity-Parser
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/HTTP-Entity-Parser-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  %{__perl}

BuildRequires:  perl-interpreter >= 0:5.008001
BuildRequires:  perl-generators

BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Hash::MultiValue)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Message) >= 6
BuildRequires:  perl(HTTP::MultiPartParser)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(JSON::MaybeXS) >= 1.003007
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(Stream::Buffered)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(WWW::Form::UrlEncoded) >= 0.23

BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)


%description
HTTP::Entity::Parser is a PSGI-compliant HTTP Entity parser. This module
also is compatible with HTTP::Body. Unlike HTTP::Body, HTTP::Entity::Parser
reads HTTP entities from PSGI's environment $env->{'psgi.input'} and parses
it. This module supports application/x-www-form-urlencoded, multipart/form-
data and application/json.

%prep
%setup -q -n HTTP-Entity-Parser-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README.md eg/
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 29 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.25-8
- Convert license to SPDX.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-6
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 30 2020 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.25-1
- Update to 0.25.

* Sat Aug 22 2020 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.24-1
- Update to 0.24.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.23-1
- Update to 0.23.

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 20 2019 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.22-1
- Update to 0.22.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-2
- Perl 5.28 rebuild

* Sun Mar 04 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.21-1
- Update to 0.21.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.20-1
- Update to 0.20.

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-2
- Perl 5.26 rebuild

* Thu Feb 09 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.19-1
- Upstream update.

* Thu Nov 03 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.18-2
- Reflect feedback from review.

* Fri Oct 07 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.18-1
- Initial Fedora package.
