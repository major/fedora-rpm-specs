# This is not archful information, and mimics RPM's paths
%global _debconfigdir %{_prefix}/lib/debbuild

Name:           debbuild
Version:        20.04.0
Release:        16%{?dist}
Summary:        Build Debian-compatible .deb packages from RPM .spec files

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/debbuild/debbuild
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  perl-generators
BuildRequires:  perl(Pod::Man)
BuildRequires: make


%if 0%{?rhel} && 0%{?rhel} < 7
Requires:       /usr/bin/lsb_release
%endif

Requires:       bash
Requires:       bzip2
Requires:       dpkg
Requires:       dpkg-dev
Requires:       fakeroot
Requires:       gzip
Requires:       patch
Requires:       spax
Requires:       xz

%if 0%{?fedora} || 0%{?rhel} >= 8
Recommends:     git-core
Recommends:     quilt
Recommends:     unzip
Recommends:     zip
Recommends:     zstd
%endif

%{?perl_default_filter}

%description
debbuild attempts to build Debian-friendly semi-native packages from
RPM spec files, RPM-friendly tarballs, and RPM source packages
(.src.rpm files).  It accepts most of the options rpmbuild does, and
should be able to interpret most spec files usefully.


%prep
%autosetup -p1


%build
%configure --debconfigdir=%{_debconfigdir} VERSION=%{version}
make


%install
%make_install

%find_lang %{name}


%files -f %{name}.lang
%{!?_licensedir:%global license %doc}
%doc README.md
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*
%{_debconfigdir}/
%dir %{_sysconfdir}/%{name}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul  25 2024 Miroslav Suchý <msuchy@redhat.com> - 20.04.0-15
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 20.04.0-8
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 20.04.0-5
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 20.04.0-2
- Perl 5.32 rebuild

* Mon Apr 20 2020 Neal Gompa <ngompa13@gmail.com> - 20.04.0-1
- Rebase to 20.04.0
- Switch pax dependency to spax to fix installability on EL8

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Neal Gompa <ngompa13@gmail.com> - 19.11.0-1
- Rebase to 19.11.0
- Update spec based on upstream spec

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 18.6.1-5
- Perl 5.30 rebuild

* Thu Mar  7 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 18.6.1-4
- Remove obsolete requirement for %%post scriptlet

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Neal Gompa <ngompa13@gmail.com> - 18.6.1-1
- Rebase to 18.6.1

* Sun Jul 01 2018 Jitka Plesnikova <jplesnik@redhat.com> - 18.6.0-2
- Perl 5.28 rebuild

* Fri Jun 29 2018 Neal Gompa <ngompa13@gmail.com> - 18.6.0-1
- Rebase to 18.6.0

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 17.5.0-3
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 01 2017 Neal Gompa <ngompa13@gmail.com> - 17.5.0-1
- Rebase to 17.5.0

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 16.6.1-3
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 08 2016 Neal Gompa <ngompa13@gmail.com> - 16.6.1-1
- Update to 16.6.1

* Thu May 19 2016 Jitka Plesnikova <jplesnik@redhat.com> - 16.3.0-2
- Perl 5.24 re-rebuild of bootstrapped packages

* Sun May 15 2016 Neal Gompa <ngompa13@gmail.com> - 16.3.0-1
- Switch to ascherer fork, update to 16.3.0

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.11.2-3
- Perl 5.24 rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 16 2015 Neal Gompa <ngompa13{%}gmail{*}com> - 0.11.2-1
- Update to 0.11.2

* Wed Jul  8 2015 Neal Gompa <ngompa13{%}gmail{*}com> - 0.10.1-5
- Fix previous changelog entry

* Wed Jul  8 2015 Neal Gompa <ngompa13{%}gmail{*}com> - 0.10.1-4
- Add magic definition for storing license file to work on <el7

* Wed Jul  8 2015 Neal Gompa <ngompa13{%}gmail{*}com> - 0.10.1-3
- Fixed perl BuildRequires error for <el7

* Sun Jul  5 2015 Neal Gompa <ngompa13{%}gmail{*}com> - 0.10.1-2
- Fix dependencies on dpkg-dev and xz
- Remove superfluous spec statements (BuildRoot, etc.)
- Make variable usage consistent

* Fri Jun 12 2015 Neal Gompa <ngompa13{%}gmail{*}com> - 0.10.1-1
- Initial packaging
