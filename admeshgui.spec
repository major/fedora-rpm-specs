Name:           admeshgui
%global         camelname ADMeshGUI
Version:        1.0.1
Release:        18%{?dist}
Summary:        STL viewer and manipulation tool
# Code is AGPLv3 logo/license is LGPLv3 or CC-BY-SA
License:        AGPLv3 and (LGPLv3 or CC-BY-SA)
URL:            https://github.com/vyvledav/%{camelname}
Source0:        https://github.com/vyvledav/%{camelname}/archive/v%{version}.tar.gz

# https://github.com/admesh/ADMeshGUI/commit/1732bc83cb2c949089d98cd9be0e922ac4af4a28
Patch0:         %{name}-qt571.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(libadmesh) >= 0.98.2
BuildRequires:  pkgconfig(Qt5Core) >= 5.4
BuildRequires:  pkgconfig(Qt5Gui) >= 5.4
BuildRequires:  pkgconfig(Qt5OpenGL) >= 5.4
BuildRequires:  pkgconfig(Qt5Svg) >= 5.4
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.4
BuildRequires:  pkgconfig(Qt5) >= 5.4
BuildRequires:  stlsplit-devel
BuildRequires: make

Requires:       hicolor-icon-theme

Provides:       %{camelname}%{_isa} = %{version}-%{release}
Provides:       %{camelname} = %{version}-%{release}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} >= 37 || 0%{?rhel} >= 10
ExcludeArch:    %{ix86}
%endif

%description
Extension for ADMesh tool in the form of graphical user interface. ADMesh tool
allows to manipulate and repair 3D models in the STL format. This graphical
user interface allows the user to view the model in 3D viewer, to perform
selected actions and to get visual feedback of those.

%prep
%setup -qn %{camelname}-%{version}
%patch0 -p1


%build
%{qmake_qt5} PREFIX=%{buildroot}/usr
make %{?_smp_mflags}

%install
make install

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml


%files
%license LICENSE LOGO-LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/appdata/admeshgui.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/icons/hicolor/symbolic/apps/%{name}-symbolic.svg


%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.1-8
- Remove obsolete scriptlets

* Mon Aug 07 2017 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-7
- Fix FTBFS

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> 1.0.1-2
- use %%qmake_qt5 macro to ensure proper build flags

* Wed Sep 16 2015 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-1
- update

* Fri May 22 2015 Miro Hrončok <mhroncok@redhat.com> - 1.0-1
- Initial package
