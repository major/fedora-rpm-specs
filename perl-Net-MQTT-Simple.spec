Name:           perl-Net-MQTT-Simple
Version:        1.26
Release:        5%{?dist}
Summary:        Minimal MQTT version 3 interface

# Chosen from https://opensource.org/licenses/alphabetical
# as allowed by the original licence text
License:        BSD
URL:            https://metacpan.org/release/Net-MQTT-Simple
Source0:        https://cpan.metacpan.org/authors/id/J/JU/JUERD/Net-MQTT-Simple-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter

BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))
Requires:       perl(IO::Socket::IP)

%{?perl_default_filter}

%description
This module consists of only one file and has no dependencies except core
Perl modules, making it suitable for embedded installations where CPAN
installers are unavailable and resources are limited. Only basic MQTT
functionality is provided.

%prep
%setup -q -n Net-MQTT-Simple-%{version}

%build
export PERL_MM_USE_DEFAULT=yes
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 --no-online-tests
make %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Net
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.26-4
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 17 2021 Dave Olsthoorn <daveo@fedoraproject.org> - 1.26-1
- new version

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.25-2
- Perl 5.34 rebuild

* Wed Feb 17 2021 Dave Olsthoorn <dave@bewaar.me> - 1.25-1
- new version

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-1
- 1.24 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 08 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.23-1
- 1.23 bump

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.22-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.22-1
- 1.22 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.21-4
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 30 2017 Dave Olsthoorn <dave@bewaar.me> - 1.21-2
- Fix the things brought up in review

* Thu Oct 26 2017 Dave Olsthoorn <dave@bewaar.me> 1.21-1
- Initial Specfile
