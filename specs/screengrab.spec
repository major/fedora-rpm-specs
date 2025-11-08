Name:           screengrab
Summary:        Crossplatform tool for fast making screenshots
Version:        3.1.0
Release:        1%{?dist}
License:        GPL-2.0-only
URL:            https://lxqt-project.org/
Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires:  cmake(LayerShellQt)
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(qt6xdg)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  wayland-devel

BuildRequires:  cmake(KF6WindowSystem)

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libpng16)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-xfixes)

BuildRequires:  perl

Requires:       hicolor-icon-theme

%description
An application for creating screenshots. ScreenGrab uses
the Qt framework and thus, it is independent from any
desktop environment.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-qt

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/screengrab.desktop

%files -f %{name}.lang
%license COPYING
%doc AUTHORS CHANGELOG README.md
%{_bindir}/screengrab
%{_datadir}/applications/screengrab.desktop
%{_datadir}/icons/hicolor/scalable/apps/screengrab.svg
%{_metainfodir}/screengrab.metainfo.xml
%{_datadir}/screengrab/screengrab.conf

%changelog
* Thu Nov 06 2025 Shawn W Dunn <sfalken@opensuse.org> - 3.1.0-1
- Update to 3.1.0

* Thu Oct 02 2025 Jan Grulich <jgrulich@redhat.com> - 3.0.0-3
- Rebuild (qt6)

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat May 17 2025 Shawn W. Dunn <sfalken@cloverleaf-linux.org> - 3.0.0-1
- 3.0.0

* Fri Apr 18 2025 Shawn W. Dunn <sfalken@cloverleaf-linux.org> - 2.10.0-1
- 2.10.0

* Wed Dec 18 2024 Steve Cossette <farchord@gmail.com> - 2.9.0-1
- Revival; bump to 2.9.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 28 2016 TI_Eugene <ti.eugene@gmail.com> 1.2.1-1
- Version bump
- Changed source URL
- Clean up docs

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.2-3
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.2-2
- Add an AppData file for the software center

* Mon Jan 19 2015 TI_Eugene <ti.eugene@gmail.com> 1.2-1
- Version bump

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 16 2013 TI_Eugene <ti.eugene@gmail.com> 1.0-1
- Version bump
- %%find_lang added

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.96-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 16 2013 TI_Eugene <ti.eugene@gmail.com> 0.9.96-3
- User CXXFLAGS patch improved

* Fri Mar 08 2013 TI_Eugene <ti.eugene@gmail.com> 0.9.96-2
- src/3rdparty removed (built-in qxt)

* Fri Mar 08 2013 TI_Eugene <ti.eugene@gmail.com> 0.9.96-1
- next version - 0.9.96
- spec fix: License set to GPLv2
- spec fix: Group tag removed
- spec fix: %%description copy/pasted from project home webpage
- spec fix: %%install - 'rm buildroot' removed; 'rm' changed to %%{__rm}
* Thu Mar 07 2013 TI_Eugene <ti.eugene@gmail.com> 0.9.1-3
- spec fix: License tag changed to GPL+LGPL+BSD
- spec fix: cmake call changed to %%cmake macro with BUILD_SHARED_LIBS=OFF
- spec fix: Source0 tag changed to URL
- spec fix: previous changelog record expanded

* Thu Mar 07 2013 TI_Eugene <ti.eugene@gmail.com> 0.9.1-2
- spec fix: gcc-c++ removed from BuildRequires
- spec fix: description wraped
- spec fix: %%clean section removed
- spec fix: %%defattr removed
- spec fix: desktop-file-validate added
- spec fix: Vendor tag removed
- spec fix: changelog cutted up to starting in Fedora
- spec fix: Source tag changed to non-URL with comments
- spec fix: License set to GPLv2

* Thu Mar 07 2013 TI_Eugene <ti.eugene@gmail.com> 0.9.1-1
- initial packaging for Fedora
