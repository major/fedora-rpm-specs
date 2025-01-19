
Name:    kdepim
Summary: KDE Personal Information Metapackage
Epoch:   7
Version: 17.12.3
Release: 17%{?dist}

# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL:     https://community.kde.org/KDE_PIM

# handled by qt5-srpm-macros, which defines %%qt5_qtwebengine_arches
%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}

Requires: %{name}-common = %{epoch}:%{version}-%{release}

%global majmin_ver %(echo %{version} | cut -d. -f1,2)
Requires: akregator >= %{majmin_ver}
Requires: kaddressbook >= %{majmin_ver}
Requires: kalarm >= %{majmin_ver}
Requires: knotes >= %{majmin_ver}
Requires: kmail >= %{majmin_ver}
# kontact already pulls in kaddressbook, kmail, korganizer
Requires: kontact >= %{majmin_ver}
Requires: korganizer >= %{majmin_ver}

BuildRequires:  kf5-rpm-macros

%description
%{summary}, including:
* akregator: feed aggregator
* blogilo: blogging application, focused on simplicity and usability}
* kmail: email client
* knotes: sticky notes for the desktop
* kontact: integrated PIM management
* korganizer: journal, appointments, events, todos

%package        common
Summary:        Common  files for %{name}
Obsoletes:      kdepim-libs < 7:16.12
%description    common
%{summary}.


%prep
# blank

%build
# blank


%install
# blank

%files
# empty

%files common 
# empty


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7:17.12.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 7:17.12.3-16
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7:17.12.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7:17.12.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7:17.12.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7:17.12.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7:17.12.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7:17.12.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7:17.12.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7:17.12.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7:17.12.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7:17.12.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7:17.12.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7:17.12.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7:17.12.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7:17.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 7:17.12.3-1
- 17.12.13, drop blogilo references

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7:16.12.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7:16.12.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7:16.12.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 7:16.12.2-3
- nevermind, kdepim-common needs epoch now to ensure upgrade path

* Wed Feb 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 7:16.12.2-2
- -common: Epoch: 0

* Mon Feb 13 2017 Rex Dieter <rdieter@fedoraproject.org> - 7:16.12.2-1
- 16.12.2, Requires: %%name-common

* Tue Feb 07 2017 Rex Dieter <rdieter@fedoraproject.org> - 7:16.12.1-2
- -common: Obsoletes: kdepim-libs

* Mon Jan 23 2017 Rex Dieter <rdieter@fedoraproject.org> - 7:16.12.1-1
- metapackage

* Sat Dec 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 7:16.08.3-2
- Rebuild for gpgme 1.18

* Mon Dec 05 2016 Rex Dieter <rdieter@fedoraproject.org> - 7:16.08.3-1
- 16.08.3

* Fri Oct 28 2016 Than Ngo <than@redhat.com> - 7:16.08.2-2
- don't build on ppc64/s390x as qtwebengine is not supported yet

* Thu Oct 13 2016 Rex Dieter <rdieter@fedoraproject.org> - 7:16.08.2-1
- 16.08.2

* Wed Oct 12 2016 Than Ngo <than@redhat.com> - 7:16.08.1-2
- CVE-2016-7968, CVE-2016-7967

* Thu Sep 08 2016 Rex Dieter <rdieter@fedoraproject.org> - 7:16.08.1-1
- 16.08.1

* Sun Sep 04 2016 Rex Dieter <rdieter@fedoraproject.org> - 7:16.08.0-1
- 16.08.0

* Thu Aug 04 2016 Rex Dieter <rdieter@fedoraproject.org> - 7:16.04.3-3
- pull in upstream knotesglobalconfig_paths.patch

* Wed Jul 20 2016 Rex Dieter <rdieter@fedoraproject.org> - 7:16.04.3-2
- docs/HTML/en/kmail2 -> kmail symlink hack, makes Kmail Handbook link work

* Sun Jul 10 2016 Rex Dieter <rdieter@fedoraproject.org> - 7:16.04.3-1
- 16.04.3

* Thu Jun 30 2016 Rex Dieter <rdieter@fedoraproject.org> - 7:16.04.2-2
- akregator,kaddressbook,kmail,korganizer: Requires: kdepim-addons

* Sun Jun 12 2016 Rex Dieter <rdieter@fedoraproject.org> - 7:16.04.2-1
- 16.04.2

* Mon May 30 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.1-3
- kmail: fix versioned kleopatra dep
- drop remnants of old/unused -devel subpkg

* Thu May 26 2016 Rex Dieter <rdieter@fedoraproject.org> - 7:16.04.1-2
- -libs: Obsoletes: kdepim-libs < 7:16.04.0
  many libs were split out into their own packages in the 16.04 release

* Mon May 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 7:16.04.1-1
- 16.04.1
- initial support  for bootstrap, %%check: 'make test'
- move plugins to multilib'd -lib subpkgs
