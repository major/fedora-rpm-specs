Name: ghostwriter
Version: 24.12.1
Release: 2%{?dist}

License: GPL-3.0-or-later AND Apache-2.0 AND CC-BY-4.0 AND CC-BY-SA-4.0 AND MPL-1.1 AND BSD-2-Clause AND BSD-3-Clause AND LGPL-3.0-only AND MIT AND ISC
Summary: Cross-platform, aesthetic, distraction-free Markdown editor
URL: https://invent.kde.org/office/%{name}
Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros

BuildRequires: hunspell-devel

BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Sonnet)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6DocTools)

BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6WebChannel)
BuildRequires: cmake(Qt6WebEngineWidgets)
BuildRequires: cmake(Qt6Widgets)

Provides: bundled(cmark-gfm) = 0.29.0.gfm.6
Provides: bundled(fontawesome-fonts) = 5.10.2
Provides: bundled(nodejs-mathjax-full) = 3.1.2
Provides: bundled(nodejs-react) = 17.0.1
Provides: bundled(QtAwesome) = 5

Requires: hicolor-icon-theme

Recommends: cmark%{?_isa}
Recommends: multimarkdown%{?_isa}
Recommends: pandoc%{?_isa}

# Required qt6-qtwebengine is not available on some arches.
ExclusiveArch: %{qt6_qtwebengine_arches}

%description
Ghostwriter is a text editor for Markdown, which is a plain text markup
format created by John Gruber. For more information about Markdown, please
visit John Gruber’s website at http://www.daringfireball.net.

Ghostwriter provides a relaxing, distraction-free writing environment,
whether your masterpiece be that next blog post, your school paper,
or your novel.

%prep
%autosetup -p1

%build
%cmake_kf6
%cmake_build

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.metainfo.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop

%install
%cmake_install
%find_lang %{name} --all-name --with-qt --with-man

%files -f %{name}.lang
%doc CHANGELOG.md CONTRIBUTING.md README.md
%license COPYING
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}.*
%{_kf6_metainfodir}/org.kde.%{name}.metainfo.xml
%{_mandir}/man1/ghostwriter.*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 24.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 07 2025 Steve Cossette <farchord@gmail.com> - 24.12.1-1
- 24.12.1

* Sat Dec 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.12.0-1
- 24.12.0

* Fri Nov 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.90-1
- 24.11.90

* Fri Nov 15 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.80-1
- 24.11.80

* Tue Nov 05 2024 Steve Cossette <farchord@gmail.com> - 24.08.3-1
- 24.08.3

* Tue Oct 08 2024 Steve Cossette <farchord@gmail.com> - 24.08.2-1
- 24.08.2

* Wed Sep 25 2024 Alessandro Astone <ales.astone@gmail.com> - 24.08.1-1
- 24.08.1

* Thu Aug 22 2024 Steve Cossette <farchord@gmail.com> - 24.08.0-1
- 24.08.0

* Wed Aug 14 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 24.07.90-1
- 24.07.90

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.05.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.2-1
- 24.05.2

* Fri Jun 14 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.1-1
- 24.05.1

* Sun Jun 09 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 24.05.0-2
- Use KF5

* Fri May 17 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.0-1
- 24.05.0

* Fri Apr 12 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.2-1
- 24.02.2

* Fri Mar 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.1-1
- 24.02.1

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.0-1
- 24.02.0

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.95-1
- 24.01.95

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90

* Sat Dec 30 2023 Marie Loise Nolden <loise@kde.org> - 24.01.85-1
- 24.01.85

* Thu Oct 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.2-1
- 23.08.2

* Sat Sep 16 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.1-1
- 23.08.1

* Sat Aug 26 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.0-1
- 23.08.0

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.3-1
- 23.04.3

* Tue Jun 06 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.2-1
- 23.04.2

* Sat May 13 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.1-1
- 23.04.1

* Thu Apr 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.0-1
- 23.04.0

* Sat Apr 01 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 23.03.90-2
- Switched to Ninja.
- Explicitly set Release configuration.
- Sorted all BuildRequires by name for better readability.
- Updated bundled libraries versions. Fixes rhbz#2128046.

* Fri Mar 31 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.90-1
- 23.03.90

* Mon Mar 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.80-1
- 23.03.80

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Sep 19 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2.2.0-1
- Updated to version 2.2.0.

* Wed Sep 14 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2.1.6-1
- Updated to version 2.1.6.

* Sun Sep 11 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2.1.5-1
- Updated to version 2.1.5.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 19 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2.1.4-1
- Updated to version 2.1.4.

* Sun May 29 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2.1.3-1
- Updated to version 2.1.3.

* Mon Mar 14 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2.1.2-1
- Updated to version 2.1.2 with CVE-2022-24724 vulnerability fix.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Dec 26 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2.1.1-1
- Updated to version 2.1.1.

* Sun Nov 21 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2.1.0-1
- Updated to version 2.1.0.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jun 27 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.2-1
- Updated to version 2.0.2.

* Tue May 18 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.1-1
- Updated to version 2.0.1.

* Sun May 09 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.0-2
- Added supported Markdown exporters as weak dependencies.

* Sun May 09 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.0-1
- Updated to version 2.0.0.

* Sun Jan 31 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.0-0.1.rc4
- Updated to version 2.0.0 (RC4).

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb 23 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.8.1-1
- Updated to version 1.8.1.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 29 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 1.8.0-1
- Updated to version 1.8.0.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 10 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.7.4-1
- Updated to version 1.7.4.

* Sat Oct 27 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.7.3-1
- Initial SPEC release.
