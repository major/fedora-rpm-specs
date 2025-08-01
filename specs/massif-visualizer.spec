Name:           massif-visualizer
Summary:        Visualizer for Massif heap memory profiler data files
Version:        25.07.90
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/massif_visualizer/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

Requires:       kf6-filesystem

BuildRequires:  kf6-rpm-macros
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  libappstream-glib
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KChart6)

BuildRequires:  cmake(KGraphViewerPart) >= 2.5.0

BuildRequires:  shared-mime-info

%description
Massif Visualizer is a tool that visualizes massif data.

You run your application in Valgrind with "--tool=massif" and then open the
generated "massif.out.<pid>" in the visualizer. Gzip or Bzip2 compressed massif
files can also be opened transparently.


%prep
%autosetup -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/*.appdata.xml
%find_lang %{name} --with-kde


%files -f %{name}.lang
%{_kf6_bindir}/massif-visualizer
%{_kf6_datadir}/mime/packages/massif.xml
%{_kf6_datadir}/applications/org.kde.massif-visualizer.desktop
%{_kf6_datadir}/config.kcfg/massif-visualizer-settings.kcfg
%{_kf6_datadir}/icons/hicolor
%{_kf6_datadir}/massif-visualizer/icons/hicolor/22x22/actions/shortentemplates.png
%{_kf6_metainfodir}/org.kde.massif-visualizer.appdata.xml
%license COPYING
%doc AUTHORS


%changelog
* Fri Jul 25 2025 Steve Cossette <farchord@gmail.com> - 25.07.90-1
- 25.07.90

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 25.07.80-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jul 11 2025 Steve Cossette <farchord@gmail.com> - 25.07.80-1
- 25.07.80

* Thu Jul 03 2025 Steve Cossette <farchord@gmail.com> - 25.04.3-1
- 25.04.3

* Wed Jun 04 2025 Steve Cossette <farchord@gmail.com> - 25.04.2-1
- 25.04.2

* Wed May 14 2025 Steve Cossette <farchord@gmail.com> - 25.04.1-1
- 25.04.1

* Sat Apr 12 2025 Steve Cossette <farchord@gmail.com> - 25.04.0-1
- 25.04.0

* Thu Mar 20 2025 Steve Cossette <farchord@gmail.com> - 25.03.80-1
- 25.03.80 (Beta)

* Tue Mar 04 2025 Steve Cossette <farchord@gmail.com> - 24.12.3-1
- 24.12.3

* Fri Feb 21 2025 Steve Cossette <farchord@gmail.com> - 24.12.2-2
- Rebuild for ppc64le enablement

* Wed Feb 05 2025 Steve Cossette <farchord@gmail.com> - 24.12.2-1
- 24.12.2

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 24.12.1-2
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

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue May 21 2024 Sandro Mani <manisandro@gmail.com> - 0.8.0-2
- Fix typo kfi6-filesystem -> kf6-filesystem

* Thu May 16 2024 Marie Loise Nolden <loise@kde.org> - 0.8.0-1
- 0.8.0 using Qt6/KF6

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 15 2018 Lubomir Rintel <lkundrak@v3.sk> - 0.7.0-1
- Update to 0.7.0

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.4.0-13
- update URL

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 01 2016 Rex Dieter <rdieter@fedoraproject.org> 0.4.0-8
- update URL (#1325300)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.4.0-5
- Rebuilt for GCC 5 C++11 ABI change

* Tue Feb 10 2015 Lubomir Rintel <lkundrak@v3.sk> - 0.4.0-4
- BR kgraphviewer
- Fix ARM build

* Tue Feb 10 2015 Lubomir Rintel <lkundrak@v3.sk> - 0.4.0-3
- Update desktop database (Zbigniew Jędrzejewski-Szmek, rh #1190055)
- Fix license tag (Zbigniew Jędrzejewski-Szmek, rh #1190055)

* Fri Feb 06 2015 Lubomir Rintel <lkundrak@v3.sk> - 0.4.0-2
- Streamline BRs
- Fix %%license tag

* Thu Feb 05 2015 Lubomir Rintel <lkundrak@v3.sk> - 0.4.0-1
- Initial packaging
