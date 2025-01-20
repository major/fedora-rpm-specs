Name:		qvge
Version:	0.6.3
Release:	8%{?dist}
# Automatically converted from old format: MIT and LGPLv3 and BSD - review is highly recommended.
License:	LicenseRef-Callaway-MIT AND LGPL-3.0-only AND LicenseRef-Callaway-BSD
Summary:	Graph editor
URL:		https://arsmasiuk.github.io/qvge/
Source0:	https://github.com/ArsMasiuk/qvge/archive/refs/tags/%{name}-%{version}.tar.gz
# https://github.com/ArsMasiuk/qvge/issues/164
Patch0:		%{name}-%{version}-0.patch
BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	desktop-file-utils
BuildRequires:	libappstream-glib
BuildRequires:	boost-devel
# qt5-qtbase-devel
BuildRequires:	pkgconfig(Qt5Gui)
# qt5-qtx11extras-devel
BuildRequires:	pkgconfig(Qt5X11Extras)
# qt5-qtsvg-devel
BuildRequires:	pkgconfig(Qt5Svg)
# Virtuals
# qpocessinfo (https://github.com/baldurk/qprocessinfo) - BSD
Provides:	bundled(qprocessinfo)
# qsint-widgets (part of https://sourceforge.net/projects/qsint/) - LGLPv3
Provides:	bundled(qsint) = 0.4.0
# qtpropertybrowser (part of https://github.com/qtproject/qt-solutions) - BSD)
Provides:	bundled(qtpropertybrowser) = 2.7
Requires:	shared-mime-info


%description
Multiplatform graph editor written in C++/Qt.
Its main goal is to make possible visually edit two-dimensional graphs in a
simple and intuitive way.


%prep
%autosetup -p0


%build
pushd src
%{qmake_qt5} PREFIX=%{_prefix}
%{make_build}
popd


%install
pushd src
%{make_install} INSTALL_ROOT=%{buildroot}
popd
# prepare license files
mv src/3rdParty/qtpropertybrowser/LICENSE src/3rdParty/qprocessinfo/LICENSE.qtpropertybrowser
mv src/3rdParty/qprocessinfo/LICENSE src/3rdParty/qprocessinfo/LICENSE.qprocessinfo
mv src/3rdParty/qsint-widgets/README.txt src/3rdParty/qsint-widgets/README.qsint


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
# 'make check' not supported with upstream


%files
%license LICENSE src/3rdParty/qprocessinfo/LICENSE.qtpropertybrowser src/3rdParty/qprocessinfo/LICENSE.qprocessinfo src/3rdParty/qsint-widgets/README.qsint
%doc README.md
%{_bindir}/qvgeapp
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/*.xml
%{_datadir}/pixmaps/%{name}.png


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6.3-7
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Nov 20 2022 TI_Eugene <ti.eugene@gmail.com> - 0.6.3-1
- Release bump
- Fixed #2139751

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-0.4git2a44063
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-0.3git2a44063
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-0.2git2a44063
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 19 2021 TI_Eugene <ti.eugene@gmail.com> - 0.6.3-0.1
- Version bump (prerelease)
- Fixed License tag

* Sun May 09 2021 TI_Eugene <ti.eugene@gmail.com> - 0.6.2-4
- Added 'BR: make'
- Added 'R: shared-mime-info'
- 'make check' note
- Licenses cleanups ('License:' tag, appdata.xml, files/license section)

* Mon May 03 2021 TI_Eugene <ti.eugene@gmail.com> - 0.6.2-3
- Bundling definitions added

* Tue Jan 19 2021 TI_Eugene <ti.eugene@gmail.com> - 0.6.2-2
- Licenses fixes
- Desktop files fixes

* Thu Jan 07 2021 TI_Eugene <ti.eugene@gmail.com> - 0.6.2-1
- initial packaging for Fedora
