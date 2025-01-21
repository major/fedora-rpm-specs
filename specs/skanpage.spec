Name:     skanpage
Version:  24.12.1
Release:  2%{?dist}
Summary:  Utility to scan images and multi-page documents
License:  BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only

URL:      https://invent.kde.org/utilities/%{name}
Source0:  https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## Upstream patches

## Downstream patches
# gcc fails to compile this project with -fopenmp even though it seems unused?
Patch100: disable-openmp.patch

# https://invent.kde.org/utilities/skanpage/-/commit/9d94de32a3a1a9bb9ead8ae8c06743b2052beef7
# The previous commit made qtwebengine a mandatory requirement :(
ExclusiveArch: %{qt6_qtwebengine_arches}

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Pdf)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6Purpose)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KQuickImageEditor)
BuildRequires:  cmake(KSaneCore6)

BuildRequires:  cmake(Tesseract) >= 4
BuildRequires:  cmake(Leptonica)

Requires: qt6-qtquickcontrols2
Requires: kf6-kirigami
Requires: kquickimageeditor-qt6

Recommends: sane-backends-drivers-scanners


%description
Skanpage is a multi-page scanning application built 
using the libksane library and a QML interface. 
It supports saving to image and PDF files.

%prep
%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.kde.%{name}.appdata.xml


%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/org.kde.%{name}.desktop
%{_metainfodir}/org.kde.%{name}.appdata.xml

%{_kf6_datadir}/qlogging-categories6/%{name}.categories
%{_kf6_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_kf6_datadir}/icons/hicolor/48x48/apps/%{name}.png

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 24.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 07 2025 Steve Cossette <farchord@gmail.com> - 24.12.1-1
- 24.12.1

* Sat Dec 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.12.0-1
- 24.12.0

* Fri Nov 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.90-1
- 24.11.90

* Fri Nov 15 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.80-1
- 24.11.80

* Tue Nov 12 2024 Sandro Mani <manisandro@gmail.com> - 24.08.3-2
- Rebuild (tesseract)

* Tue Nov 05 2024 Steve Cossette <farchord@gmail.com> - 24.08.3-1
- 24.08.3

* Tue Oct 08 2024 Steve Cossette <farchord@gmail.com> - 24.08.2-1
- 24.08.2

* Thu Oct 03 2024 Neal Gompa <ngompa@fedoraproject.org> - 24.08.1-2
- Rebuild for tesseract-5.4.1-3 (soversion change) again

* Wed Sep 25 2024 Alessandro Astone <ales.astone@gmail.com> - 24.08.1-1
- 24.08.1

* Wed Sep 25 2024 Michel Lind <salimma@fedoraproject.org> - 24.08.0-2
- Rebuild for tesseract-5.4.1-3 (soversion change from 5.4.1 to just 5.4)

* Thu Aug 22 2024 Steve Cossette <farchord@gmail.com> - 24.08.0-1
- 24.08.0

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.05.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.2-1
- 24.05.2

* Fri Jun 14 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.1-1
- 24.05.1

* Thu Jun 13 2024 Sandro Mani <manisandro@gmail.com> - 24.05.0-2
- Rebuild for tesseract-5.4.1

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

* Sun Jan 28 2024 Sandro Mani <manisandro@gmail.com> - 24.01.90-3
- Rebuild (tesseract)

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90

* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Tue Dec 12 2023 Alessandro Astone <ales.astone@gmail.com> - 24.01.80-1
- 24.01.80

* Wed Oct 25 2023 Vasiliy Glazov <vascom2@gmail.com> - 23.08.2-2
- Added requires kquickimageeditor

* Thu Oct 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.2-1
- 23.08.2

* Sat Sep 16 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.1-1
- 23.08.1

* Sat Aug 26 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.0-1
- 23.08.0

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.3-1
- 23.04.3

* Tue Jun 06 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.2-1
- 23.04.2

* Sat May 13 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.1-1
- 23.04.1

* Fri Apr 14 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.0-1
- 23.04.0

* Fri Mar 31 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.90-1
- 23.03.90

* Mon Mar 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.80-1
- 23.03.80

* Thu Mar 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 22.12.3-1
- 22.12.3

* Tue Jan 31 2023 Marc Deop <marcdeop@fedoraproject.org> - 22.12.2-1
- 22.12.2

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 Justin Zobel <justin@1707.io> - 22.12.1-1
- Update to 22.12.1

* Sun Dec 25 2022 Justin Zobel <justin@1707.io> - 22.12.0-1
- Update to 22.12.0

* Thu Jul 28 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 22.04.3-3
- sane-backends-drivers-scanners recommendation for additional scanner added.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Than Ngo <than@redhat.com> - 22.04.3-1
- 22.04.3

* Sun May 15 2022 Justin Zobel <justin@1707.io> - 22.04.1-1
- Update to 22.04.1

* Sun Feb 27 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 1.0-1
- Initial package for skapage 1.0
