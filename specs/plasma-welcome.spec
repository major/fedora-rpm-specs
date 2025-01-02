%global orgname org.kde.plasma-welcome

Name:           plasma-welcome
Version:        6.2.5
Release:        1%{?dist}
License:        GPL-2.0-or-later and BSD-3-Clause
Summary:        Plasma Welcome
Url:            https://invent.kde.org/plasma/%{name}

Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz

# Upstream patches

BuildRequires:  gcc-c++
BuildRequires:  qt6-qtbase-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Svg)

BuildRequires:  cmake(KF6Kirigami2)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6Svg)

BuildRequires:  cmake(Plasma)

Requires:       kf6-kuserfeedback

Provides:       plasma-welcome-app = %{version}-%{release}
Obsoletes:      plasma-welcome-app < 5.27.0-2

%description
A Friendly onboarding wizard for Plasma.

%prep
%autosetup -n %{name}-%{version} -p1
# It is for generate pot file for translate so we can ignore it.
rm Messages.sh

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name --with-html

%check
# commented out until upstream fixes duplicate entries
#appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/%{orgname}.*.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/%{orgname}.desktop

%files -f %{name}.lang
%license LICENSES/{BSD-3-Clause.txt,GPL-2.0-or-later.txt,FSFAP.txt}
%doc README.md
%{_kf6_bindir}/plasma-welcome
%{_kf6_datadir}/applications/%{orgname}.desktop
%{_kf6_metainfodir}/%{orgname}.*.xml
%{_kf6_plugindir}/kded/kded_plasma-welcome.so


%changelog
* Tue Dec 31 2024 Steve Cossette <farchord@gmail.com> - 6.2.5-1
- 6.2.5

* Tue Nov 26 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.2.4-1
- 6.2.4

* Tue Nov 05 2024 Steve Cossette <farchord@gmail.com> - 6.2.3-1
- 6.2.3

* Tue Oct 22 2024 Steve Cossette <farchord@gmail.com> - 6.2.2-1
- 6.2.2

* Tue Oct 15 2024 Steve Cossette <farchord@gmail.com> - 6.2.1-1
- 6.2.1

* Thu Oct 03 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.2.0-1
- 6.2.0

* Thu Sep 12 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.90-1
- 6.1.90

* Tue Sep 10 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.5-1
- 6.1.5

* Fri Aug 09 2024 Steve Cossette <farchord@gmail.com> - 6.1.4-1
- 6.1.4

* Wed Jul 24 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.3-3
- rebuilt

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 16 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.3-1
- 6.1.3

* Wed Jul 03 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.2-1
- 6.1.2

* Tue Jun 25 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.1-1
- 6.1.1

* Thu Jun 13 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.0-1
- 6.1.0

* Fri May 24 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.0.90-1
- 6.0.90

* Wed May 22 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.0.5-1
- 6.0.5

* Tue Apr 16 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.0.4-1
- 6.0.4

* Tue Mar 26 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.0.3-1
- 6.0.3

* Tue Mar 12 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.0.2-1
- 6.0.2

* Wed Mar 06 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.0.1-1
- 6.0.1

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.0.0-1
- 6.0.0

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.93.0-1
- 5.93.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.92.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.92.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 10 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.92.0-1
- 5.92.0

* Thu Dec 21 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.91.0-1
- 5.91.0

* Wed Dec 06 2023 Alessandro Astone <ales.astone@gmail.com> - 5.90.0-2
- Backport patch to fix live installer

* Sun Dec 03 2023 Alessandro Astone <ales.astone@gmail.com> - 5.90.0-1
- Update to 5.90.0

* Sun Nov 12 2023 Alessandro Astone <ales.astone@gmail.com> - 5.27.80-1
- 5.27.80

* Tue Oct 24 2023 Steve Cossette <farchord@gmail.com> - 5.27.9-1
- 5.27.9

* Tue Sep 12 2023 justin.zobel@gmail.com - 5.27.8-1
- 5.27.8

* Tue Aug 01 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.7-1
- 5.27.7

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.27.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jun 25 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.6-1
- 5.27.6

* Wed May 10 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.5-1
- 5.27.5

* Tue Apr 04 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.4-1
- 5.27.4

* Tue Mar 14 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.3-1
- 5.27.3

* Tue Feb 28 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.2-1
- 5.27.2

* Tue Feb 21 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.1-1
- 5.27.1

* Fri Feb 17 2023 Timothée Ravier <tim@siosm.fr> - 5.27.0-2
- Rename to Plasma Welcome to follow upstream naming (fedora#2170929)

* Thu Feb 09 2023 Marc Deop <marcdeop@fedoraproject.org> - 5.27.0-1
- 5.27.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.26.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 19 2023 Marc Deop <marcdeop@fedoraproject.org> - 5.26.90-1
- 5.26.90

* Tue Sep 20 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 0-1.20220922git2d3f9f7
- Commit build 2d3f9f7
- Feature: post-upgrade message
- BR cmake(KF5Plasma) added.

* Mon Sep 05 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 0-1.20220902git0163cda
- Initial build plasma welcome app
