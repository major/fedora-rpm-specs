Name:           perl-WWW-Form-UrlEncoded
Version:        0.26
Release:        19%{?dist}
Summary:        Parser and builder for application/x-www-form-urlencoded
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/WWW-Form-UrlEncoded
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/WWW-Form-UrlEncoded-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl-interpreter >= 0:5.008001

BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(JSON::PP) >= 2
BuildRequires:  perl(Module::Build) > 0.4005
BuildRequires:  perl(Test::More) >= 0.98

BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)


# N/A in Fedora
# Suggests: perl(WWW::Form::UrlEncoded::XS)

%description
WWW::Form::UrlEncoded provides application/x-www-form-urlencoded parser and
builder. This module aims to have compatibility with other CPAN modules
like HTTP::Body's urlencoded parser.

%prep
%setup -q -n WWW-Form-UrlEncoded-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
BREAK_BACKWARD_COMPAT=1 ./Build

%install
BREAK_BACKWARD_COMPAT=1 ./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
BREAK_BACKWARD_COMPAT=1 ./Build test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.26-12
- Convert licence to SPDX.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-10
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-7
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-4
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.26-1
- Update to 0.26.
- Drop WWW-Form-UrlEncoded-0.23-arch.patch,
  use BREAK_BACKWARD_COMPAT=1 instead.

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-3
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 02 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.25-1
- Update to 0.25.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.24-5
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.24-2
- Perl 5.26 rebuild

* Wed Mar 01 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.24-1
- Update to 0.24.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Oct 22 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.23-2
- Reflect feedback from review.

* Sat Oct 08 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.23-1
- Initial Fedora packages.
