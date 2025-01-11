
%global qt_module qtquick3d

#global unstable 1
%if 0%{?unstable}
%global prerelease rc2
%endif

%global examples 1

Summary: Qt6 - Quick3D Libraries and utilities
Name:    qt6-%{qt_module}
Version: 6.8.1
Release: 3%{?dist}

License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)

%if 0%{?unstable}
Source0: https://download.qt.io/development_releases/qt/%{majmin}/%{qt_version}/submodules/%{qt_module}-everywhere-src-%{qt_version}-%{prerelease}.tar.xz
%else
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz
%endif
Patch0:  qtquick3d-fix-build-with-gcc11.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: qt6-rpm-macros >= %{version}
BuildRequires: qt6-qtbase-static >= %{version}
BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: qt6-qtdeclarative-devel
BuildRequires: qt6-qtdeclarative-static
BuildRequires: qt6-qtquicktimeline-devel
BuildRequires: qt6-qtshadertools-devel

#if 0{?fedora}
# BuildRequires: pkgconfig(assimp) >= 5.0.0
#endif

%description
The Qt 6 Quick3D library.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
Requires: qt6-qtdeclarative-devel%{?_isa}
%description devel
%{summary}.

%if 0%{?examples}
%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
# BuildRequires: qt6-qtquick3d-devel >= %{version}
%description examples
%{summary}.
%endif

%prep
%autosetup -n %{qt_module}-everywhere-src-%{qt_version}%{?unstable:-%{prerelease}} -p1


%build
%if 0%{?rhel} >= 10
%ifarch x86_64
# The bundled embree attempts to limit optimization to SSE4.1 and disable AVX,
# but RHEL 10 defaults to -march=x86-64-v3 which includes AVX, resulting in
# build failures due to missing symbols from the AVX code which is not built.
CXXFLAGS="$CXXFLAGS -mno-avx"
%endif
%endif

# QT is known not to work properly with LTO at this point.  Some of the issues
# are being worked on upstream and disabling LTO should be re-evaluated as
# we update this change.  Until such time...
# Disable LTO
%define _lto_cflags %{nil}

%cmake_qt6 \
  -DQT_BUILD_EXAMPLES:BOOL=%{?examples:ON}%{!?examples:OFF} \
  -DQT_INSTALL_EXAMPLES_SOURCES=%{?examples:ON}%{!?examples:OFF}
#   -DQT_FEATURE_system_assimp=ON

%cmake_build


%install
%cmake_install

# hardlink files to %{_bindir}, add -qt6 postfix to not conflict
mkdir %{buildroot}%{_bindir}
pushd %{buildroot}%{_qt6_bindir}
for i in * ; do
  case "${i}" in
    balsam|meshdebug|shadergen|balsamui|instancer|materialeditor|shapegen)
      ln -v  ${i} %{buildroot}%{_bindir}/${i}-qt6
      ;;
    *)
      ln -v  ${i} %{buildroot}%{_bindir}/${i}
      ;;
  esac
done
popd

## .prl/.la file love
# nuke .prl reference(s) to %%buildroot, excessive (.la-like) libs
pushd %{buildroot}%{_qt6_libdir}
for prl_file in libQt6*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd


%ldconfig_scriptlets

%files
%license LICENSES/GPL*
%{_qt6_archdatadir}/sbom/%{qt_module}-%{qt_version}.spdx
%{_qt6_libdir}/libQt6Quick3D.so.6*
%{_qt6_libdir}/libQt6Quick3DAssetImport.so.6*
%{_qt6_libdir}/libQt6Quick3DRuntimeRender.so.6*
%{_qt6_libdir}/libQt6Quick3DUtils.so.6*
%{_qt6_libdir}/libQt6Quick3DIblBaker.so.6*
%{_qt6_libdir}/libQt6Quick3DParticles.so.6*
%{_qt6_libdir}/libQt6Quick3DAssetUtils.so.6*
%{_qt6_libdir}/libQt6Quick3DEffects.so.6*
%{_qt6_libdir}/libQt6Quick3DHelpers.so.6*
%{_qt6_libdir}/libQt6Quick3DHelpersImpl.so*
%{_qt6_libdir}/libQt6Quick3DParticleEffects.so.6*
%{_qt6_libdir}/libQt6Quick3DGlslParser.so.6*
%{_qt6_libdir}/libQt6Quick3DXr.so.6*
%dir %{_qt6_qmldir}/QtQuick3D/
%{_qt6_qmldir}/QtQuick3D/
%dir %{_qt6_plugindir}/assetimporters
%{_qt6_plugindir}/assetimporters/*.so

%files devel
%{_bindir}/balsam-qt6
%{_bindir}/meshdebug-qt6
%{_bindir}/shadergen-qt6
%{_bindir}/balsamui-qt6
%{_bindir}/instancer-qt6
%{_bindir}/materialeditor-qt6
%{_bindir}/shapegen-qt6
%{_qt6_bindir}/balsam
%{_qt6_bindir}/meshdebug
%{_qt6_bindir}/shadergen
%{_qt6_bindir}/balsamui
%{_qt6_bindir}/instancer
%{_qt6_bindir}/materialeditor
%{_qt6_bindir}/shapegen
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_libdir}/qt6/modules/*.json
%{_qt6_includedir}/QtQuick3D
%{_qt6_includedir}/QtQuick3DAssetImport
%{_qt6_includedir}/QtQuick3DIblBaker
%{_qt6_includedir}/QtQuick3DParticles
%{_qt6_includedir}/QtQuick3DRuntimeRender
%{_qt6_includedir}/QtQuick3DUtils
%{_qt6_includedir}/QtQuick3DAssetUtils
%{_qt6_includedir}/QtQuick3DHelpers
%{_qt6_includedir}/QtQuick3DHelpersImpl
%{_qt6_includedir}/QtQuick3DGlslParser
%{_qt6_includedir}/QtQuick3DXr
%{_qt6_libdir}/cmake/Qt6/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6Quick3DIblBaker
%{_qt6_libdir}/cmake/Qt6Quick3DIblBaker/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6Quick3DParticles
%{_qt6_libdir}/cmake/Qt6Quick3DParticles/*.cmake
%{_qt6_libdir}/cmake/Qt6/FindWrapQuick3DAssimp.cmake
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/*.cmake
%{_qt6_libdir}/cmake/Qt6Qml/*.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%ifarch x86_64 aarch64
%dir %{_qt6_libdir}/cmake/Qt6BundledEmbree/
%{_qt6_libdir}/cmake/Qt6/FindWrapBundledEmbreeConfigExtra.cmake
%{_qt6_libdir}/cmake/Qt6BundledEmbree/*.cmake
%endif

%dir %{_qt6_libdir}/cmake/Qt6Quick3D/
%{_qt6_libdir}/cmake/Qt6BundledOpenXR/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6BundledOpenXR/
%{_qt6_libdir}/cmake/Qt6Quick3DXr/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6Quick3DXr/
%{_qt6_libdir}/cmake/Qt6Quick3D/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6Quick3DAssetImport/
%{_qt6_libdir}/cmake/Qt6Quick3DAssetImport/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6Quick3DRuntimeRender/
%{_qt6_libdir}/cmake/Qt6Quick3DRuntimeRender/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6Quick3DTools/
%{_qt6_libdir}/cmake/Qt6Quick3DTools/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6Quick3DUtils/
%{_qt6_libdir}/cmake/Qt6Quick3DUtils/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6Quick3DAssetUtils/
%{_qt6_libdir}/cmake/Qt6Quick3DAssetUtils/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6Quick3DEffects/
%{_qt6_libdir}/cmake/Qt6Quick3DEffects/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6Quick3DHelpers/
%{_qt6_libdir}/cmake/Qt6Quick3DHelpers/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6Quick3DHelpersImpl/
%{_qt6_libdir}/cmake/Qt6Quick3DHelpersImpl/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6Quick3DGlslParserPrivate
%{_qt6_libdir}/cmake/Qt6Quick3DGlslParserPrivate/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6Quick3DParticleEffects
%{_qt6_libdir}/cmake/Qt6Quick3DParticleEffects/*.cmake
%ifarch x86_64 aarch64
%{_qt6_libdir}/libQt6BundledEmbree.a
%endif
%{_qt6_libdir}/libQt6BundledOpenXR.a
%{_qt6_libdir}/libQt6Quick3DXr.prl
%{_qt6_libdir}/libQt6Quick3DXr.so
%{_qt6_libdir}/libQt6Quick3D.prl
%{_qt6_libdir}/libQt6Quick3D.so
%{_qt6_libdir}/libQt6Quick3DAssetImport.prl
%{_qt6_libdir}/libQt6Quick3DAssetImport.so
%{_qt6_libdir}/libQt6Quick3DRuntimeRender.prl
%{_qt6_libdir}/libQt6Quick3DRuntimeRender.so
%{_qt6_libdir}/libQt6Quick3DUtils.prl
%{_qt6_libdir}/libQt6Quick3DUtils.so
%{_qt6_libdir}/libQt6Quick3DIblBaker.prl
%{_qt6_libdir}/libQt6Quick3DIblBaker.so
%{_qt6_libdir}/libQt6Quick3DParticles.prl
%{_qt6_libdir}/libQt6Quick3DParticles.so
%{_qt6_libdir}/libQt6Quick3DAssetUtils.prl
%{_qt6_libdir}/libQt6Quick3DAssetUtils.so
%{_qt6_libdir}/libQt6Quick3DEffects.prl
%{_qt6_libdir}/libQt6Quick3DEffects.so
%{_qt6_libdir}/libQt6Quick3DHelpers.prl
%{_qt6_libdir}/libQt6Quick3DHelpers.so
%{_qt6_libdir}/libQt6Quick3DHelpersImpl.prl
%{_qt6_libdir}/libQt6Quick3DHelpersImpl.so
%{_qt6_libdir}/libQt6Quick3DGlslParser.prl
%{_qt6_libdir}/libQt6Quick3DGlslParser.so
%{_qt6_libdir}/libQt6Quick3DParticleEffects.prl
%{_qt6_libdir}/libQt6Quick3DParticleEffects.so
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_plugindir}/qmltooling/libqmldbg_quick3dprofiler.so
%{_qt6_libdir}/pkgconfig/*.pc

%if 0%{?examples}
%files examples
%{_qt6_examplesdir}/
%endif

%changelog
* Thu Jan 09 2025 Jan Grulich <jgrulich@redhat.com> - 6.8.1-3
- Fix directory ownership
  Resolves: rhbz#2292578

* Thu Dec 05 2024 Jan Grulich <jgrulich@redhat.com> - 6.8.1-2
- Move Software Bill of Materials from -devel

* Thu Nov 28 2024 Jan Grulich <jgrulich@redhat.com> - 6.8.1-1
- 6.8.1

* Fri Oct 11 2024 Jan Grulich <jgrulich@redhat.com> - 6.8.0-1
- 6.8.0

* Mon Aug 05 2024 Jan Grulich <jgrulich@redhat.com> - 6.7.2-3
- Re-enable examples on s390x

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 01 2024 Jan Grulich <jgrulich@redhat.com> - 6.7.2-1
- 6.7.2

* Tue May 21 2024 Jan Grulich <jgrulich@redhat.com> - 6.7.1-1
- 6.7.1

* Tue Apr 02 2024 Jan Grulich <jgrulich@redhat.com> - 6.7.0-1
- 6.7.0

* Mon Feb 19 2024 Jan Grulich <jgrulich@redhat.com> - 6.6.2-2
- Examples: also install source files

* Thu Feb 15 2024 Jan Grulich <jgrulich@redhat.com> - 6.6.2-1
- 6.6.2

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 27 2023 Jan Grulich <jgrulich@redhat.com> - 6.6.1-1
- 6.6.1

* Tue Oct 10 2023 Jan Grulich <jgrulich@redhat.com> - 6.6.0-1
- 6.6.0

* Sun Oct 01 2023 Justin Zobel <justin.zobel@gmail.com> - 6.5.3-1
- new version

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 21 2023 Jan Grulich <jgrulich@redhat.com> - 6.5.2-1
- 6.5.2

* Wed Jul 12 2023 Jan Grulich <jgrulich@redhat.com> - 6.5.1-3
- Rebuild for qtbase private API version change

* Wed Jul 12 2023 Jan Grulich <jgrulich@redhat.com> - 6.5.1-2
- Rebuild for qtbase private API version change

* Mon May 22 2023 Jan Grulich <jgrulich@redhat.com> - 6.5.1-1
- 6.5.1

* Tue Apr 04 2023 Jan Grulich <jgrulich@redhat.com> - 6.5.0-1
- 6.5.0

* Thu Mar 23 2023 Jan Grulich <jgrulich@redhat.com> - 6.4.3-1
- 6.4.3

* Tue Jan 31 2023 Jan Grulich <jgrulich@redhat.com> - 6.4.2-3
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Jan Grulich <jgrulich@redhat.com> - 6.4.2-1
- 6.4.2

* Wed Nov 23 2022 Jan Grulich <jgrulich@redhat.com> - 6.4.1-1
- 6.4.1

* Mon Oct 31 2022 Jan Grulich <jgrulich@redhat.com> - 6.4.0-1
- 6.4.0

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 13 2022 Jan Grulich <jgrulich@redhat.com> - 6.3.1-1
- 6.3.1

* Wed May 25 2022 Jan Grulich <jgrulich@redhat.com> - 6.3.0-2
- Enable examples

* Wed Apr 13 2022 Jan Grulich <jgrulich@redhat.com> - 6.3.0-1
- 6.3.0

* Fri Feb 25 2022 Jan Grulich <jgrulich@redhat.com> - 6.2.3-2
- Enable s390x builds

* Mon Jan 31 2022 Jan Grulich <jgrulich@redhat.com> - 6.2.3-1
- 6.2.3

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 14 2021 Jan Grulich <jgrulich@redhat.com> - 6.2.2-1
- 6.2.2

* Fri Oct 29 2021 Jan Grulich <jgrulich@redhat.com> - 6.2.1-1
- 6.2.1

* Thu Sep 30 2021 Jan Grulich <jgrulich@redhat.com> - 6.2.0-1
- 6.2.0

* Mon Sep 27 2021 Jan Grulich <jgrulich@redhat.com> - 6.2.0~rc2-1
- 6.2.0 - rc2

* Sat Sep 18 2021 Jan Grulich <jgrulich@redhat.com> - 6.2.0~rc-1
- 6.2.0 - rc

* Mon Sep 13 2021 Jan Grulich <jgrulich@redhat.com> - 6.2.0~beta4-1
- 6.2.0 - beta4

* Thu Aug 12 2021 Jan Grulich <jgrulich@redhat.com> - 6.1.2-1
- 6.1.2

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 07 2021 Jan Grulich <jgrulich@redhat.com> - 6.1.1-1
- 6.1.1

* Thu May 06 2021 Jan Grulich <jgrulich@redhat.com> - 6.1.0-1
- 6.1.0

* Mon Apr 05 2021 Jan Grulich <jgrulich@redhat.com> - 6.0.3-1
- 6.0.3

* Thu Feb 04 2021 Jan Grulich <jgrulich@redhat.com> - 6.0.1-1
- 6.0.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Jan Grulich <jgrulich@redhat.com> - 6.0.0-1
- 6.0.0
