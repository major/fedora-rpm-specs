Name:           perl-Net-MQTT-Simple
Version:        1.33
Release:        2%{?dist}
Summary:        Minimal MQTT version 3 interface

# Chosen from https://opensource.org/licenses/alphabetical
# as allowed by the original licence text
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-MQTT-Simple
Source0:        https://cpan.metacpan.org/authors/id/J/JU/JUERD/Net-MQTT-Simple-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

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
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 --no-online-tests
%make_build OPTIMIZE="%{optflags}"

%install
%make_install
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Net/
%{_bindir}/mqtt-simple
%{_mandir}/man1/mqtt-simple.1*
%{_mandir}/man3/Net::MQTT::Simple*.3*

%changelog
* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Wed Sep 03 2025 Xavier Bachelot <xavier@bachelot.org> - 1.33-1
- Update to 1.33 (RHBZ#2392719)

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Apr 23 2025 Xavier Bachelot <xavier@bachelot.org> - 1.32-1
- Update to 1.32 (RHBZ#2361810)

* Thu Feb 13 2025 Xavier Bachelot <xavier@bachelot.org> - 1.31-1
- Update to 1.31 (RHBZ#2243849)
- Clean up specfile

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.28-7
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 28 2022 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1.28-1
- Update to 1.28 (#2125846)

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
