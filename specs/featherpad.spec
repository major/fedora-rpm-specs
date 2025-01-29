%global github_name FeatherPad

Name:           featherpad
Version:        1.6.0
Release:        1%{?dist}
Summary:        Lightweight Qt Plain-Text Editor

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/tsujan/%{github_name}
Source0:        %{url}/archive/V%{version}.tar.gz#/%{github_name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(hunspell) >= 1.6
BuildRequires:  pkgconfig(xext)

Requires:       hicolor-icon-theme

%description
FeatherPad is a lightweight Qt plain-text editor for Linux. It is independent
of any desktop environment and has:

* Drag-and-drop support, including tab detachment and attachment;
* X11 virtual desktop awareness (using tabs on current desktop but opening a
  new window on another);
* An optionally permanent search-bar with a different search entry
  for each tab;
* Instant highlighting of found matches when searching;
* A docked window for text replacement;
* Support for showing line numbers and jumping to a specific line;
* Automatic detection of text encoding as far as possible and optional saving
  with encoding;
* Syntax highlighting for common programming languages;
* Printing;
* Text zooming;
* Appropriate but non-interrupting prompts;

%prep
%autosetup -n %{github_name}-%{version} -p 1

%build
%cmake
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%license COPYING
%doc ChangeLog INSTALL NEWS README.md
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/help
%dir %{_datadir}/%{name}/translations
%{_datadir}/metainfo/featherpad.metainfo.xml

%changelog
* Mon Jan 27 2025 Steve Cossette <farchord@gmail.com> - 1.6.0-1
- 1.6.0

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Nov 10 2024 Steve Cossette <farchord@gmail.com> - 1.5.2-1
- 1.5.2

* Mon Jul 29 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 1.5.1-1
- Update to 1.5.1

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4.1-5
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Aug 04 2023 Jonathan Wright <jonathan@almalinux.org> - 1.4.1-1
- Update to 1.4.1 rhbz#2214871

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 27 2023 Jonathan Wright <jonathan@almalinux.org> - 1.4.0-1
- Update to 1.4.0 rhbz#2187721

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 09 2023 Jonathan Wright <jonathan@almalinux.org> - 1.3.5-2
- Update to 1.3.5 rhbz#2159098

* Mon Dec 12 2022 Jonathan Wright <jonathan@almalinux.org> - 1.3.4-1
- Update to 1.3.4 rhbz#2149791

* Sat Nov 26 2022 Jonathan Wright <jonathan@almalinux.org> - 1.3.3-1
- Update to 1.3.3 rhbz#2038534

* Sat Nov 26 2022 Jonathan Wright <jonathan@almalinux.org> - 1.1.1-1
- Update to 1.1.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 28 2021 zsun <sztsian@gmail.com> - 1.1.0-1
- Update to 1.1.0

* Mon Oct 18 2021 Zamir SUN <sztsian@gmail.com> - 1.0.1-1
- Update to 1.0.1

* Mon Oct 18 2021 Zamir SUN <sztsian@gmail.com> - 0.17.1-1
- Update to 0.17.1

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 Zamir SUN <sztsian@gmail.com> - 0.16.0-1
- Update to 0.16.0

* Sun Sep 13 2020 Joe Walker <grumpey0@gmail.com> - 0.15.0-1
- Update to 0.15.0
- Switch to cmake

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 15 2019 Zamir SUN <sztsian@gmail.com> - 0.9.3-1
- Update to 0.9.3

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 10 2018 Christian Dersch <lupinix@mailbox.org> - 0.9.0-1
- new version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.1-2
- Remove obsolete scriptlets

* Fri Oct 20 2017 Christian Dersch <lupinix@mailbox.org> - 0.6.1-1
- new version

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat May  6 2017 Christian Dersch <lupinix@mailbox.org> 0.6-1
- new version (0.6 release)

* Sun Apr  9 2017 Christian Dersch <lupinix@mailbox.org> 0.6-0.1.git20170401.7325229
- initial build (review rhbz #1440542)
