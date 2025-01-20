Summary:       Perl module for SOAP with WSDL support
Name:          perl-SOAP-WSDL
Version:       3.004
Release:       19%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:       GPL-1.0-or-later OR Artistic-1.0-Perl
URL:           https://metacpan.org/release/SOAP-WSDL
Source:        https://cpan.metacpan.org/modules/by-module/SOAP/SOAP-WSDL-%{version}.tar.gz
# Upstream reference: https://rt.cpan.org/Ticket/Display.html?id=74257
Patch0:        %{name}-use-Test-XML.patch

BuildArch:     noarch
BuildRequires: make
BuildRequires: git
BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: perl(Apache2::Const)
BuildRequires: perl(Apache2::Log)
BuildRequires: perl(Apache2::RequestIO)
BuildRequires: perl(Apache2::RequestRec)
BuildRequires: perl(Apache2::RequestUtil)
BuildRequires: perl(APR::Table)
BuildRequires: perl(base)
BuildRequires: perl(bytes)
BuildRequires: perl(Carp)
BuildRequires: perl(Class::Load)
BuildRequires: perl(Class::Std::Fast)
BuildRequires: perl(Class::Std::Fast::Storable)
BuildRequires: perl(Cwd)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Date::Format)
BuildRequires: perl(Date::Parse)
BuildRequires: perl(diagnostics)
BuildRequires: perl(Encode)
BuildRequires: perl(English)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Find::Rule)
BuildRequires: perl(File::Spec)
BuildRequires: perl(HTTP::Headers)
BuildRequires: perl(HTTP::Request)
BuildRequires: perl(HTTP::Response)
BuildRequires: perl(HTTP::Status)
BuildRequires: perl(IO::File)
BuildRequires: perl(IO::Scalar)
BuildRequires: perl(lib)
BuildRequires: perl(List::Util)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(SOAP::Lite)
BuildRequires: perl(Storable)
BuildRequires: perl(strict)
BuildRequires: perl(Template)
BuildRequires: perl(Test::MockObject)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(URI)
BuildRequires: perl(vars)
BuildRequires: perl(warnings)
BuildRequires: perl(XML::Parser::Expat)
BuildRequires: perl(Template::Plugin::CGI)

Requires:      perl(SOAP::Lite)

%{?perl_default_filter}


%description
SOAP::WSDL provides easy access to Web Services with WSDL descriptions.
The WSDL is parsed and stored in memory. Your data is serialized according
to the rules in the WSDL. The only transport mechanisms currently supported
are HTTP and HTTPS.


%package  Apache
Summary:  SOAP server with WSDL support for Apache2 web server
Requires: %{name} = %{version}-%{release}


%description Apache
The SOAP::WSDL-server package contains a SOAP compliant server capable of
sending messages via the Apache2 web server.


%package  examples
Summary:  Examples for the Perl SOAP::WSDL module
Requires: %{name} = %{version}-%{release}


%description examples
The package contains examples for SOAP::WSDL module.


%prep
%autosetup -S git -n SOAP-WSDL-%{version}
# fix example's permission
chmod a-x example/cgi-bin/*.pl


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build


%install
%make_build pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
chmod 0755 %{buildroot}%{_bindir}/wsdl2perl.pl


%check
%make_build test


%files
%license LICENSE
%doc Changes HACKING README TODO
%{_bindir}/wsdl2perl.pl
%exclude %{perl_vendorlib}/SOAP/WSDL/Server/
%{perl_vendorlib}/SOAP/*
%{_mandir}/man1/wsdl2perl.pl.1*
%{_mandir}/man3/SOAP::*3pm*


%files Apache
%license LICENSE
%{perl_vendorlib}/SOAP/WSDL/Server/


%files examples
%license LICENSE
%doc example/


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.004-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 3.004-18
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.004-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.004-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.004-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.004-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.004-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 14 2022 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 3.004-12
- Add missing BR. Fixes FTBFS (rhbz#2124543).

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.004-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 3.004-10
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.004-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.004-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 3.004-7
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.004-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.004-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.004-4
- Perl 5.32 rebuild

* Tue Mar 17 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.004-3
- Specify all dependencies

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 3.004-1
- Update to the lastest version, (fixes rhbz#1793505)
- Dop patches upstream merged

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.003-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 01 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.003-13
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.003-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.003-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.003-10
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.003-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.003-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.003-7
- Perl 5.26 rebuild

* Mon Feb 20 2017 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 3.003-6
- Yet another rebuild

* Thu Feb 16 2017 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 3.003-5
- Rebuilt for missing BR

* Tue Feb 07 2017 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 3.003-4
- Move man pages, Changes, HACKING, README and TODO to main package,
- Rename subpackage -doc to -examples

* Mon Feb 06 2017 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 3.003-3
- Add missing Test::Pod BR,
- Fix build failure on rawhide

* Wed Feb 01 2017 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 3.003-2
- Split out Apache dependent sub-package

* Tue Jan 31 2017 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 3.003-1
- Initial RPM release
