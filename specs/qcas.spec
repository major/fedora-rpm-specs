# Architectures currently not supported
# http://xcas.e.ujf-grenoble.fr/XCAS/viewtopic.php?f=19&t=1723
ExcludeArch: aarch64 %{power64} s390x

Name:          qcas
Summary:       Qt5 GUI application for Giac
Version:       0.5.3
Release:       26%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:       GPL-3.0-or-later
URL:           http://webusers.imj-prg.fr/~frederic.han/qcas
Source0:       https://git.tuxfamily.org/qcas/qcas.git/snapshot/%{name}-%{version}.zip
Source1:       %{name}.desktop
Source2:       %{name}.appdata.xml
Source3:       %{name}-qt4.desktop

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: qt5-qtbase-devel, qt5-qtsvg-devel
BuildRequires: gmp-devel
BuildRequires: giac-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
Requires:      %{name}-data = %{version}-%{release}
Requires:       giac%{?_isa}

%description
Minimal Qt5 interface for Giac.

%package        qt4
Summary:        Qt4 GUI application for Giac
BuildRequires:  qt-devel
Requires:      %{name}-data = %{version}-%{release}
Requires:       giac%{?_isa}
%description    qt4
Minimal Qt4 interface for Giac.

### This library is used by giacpy ####
%package        -n libqcas
Summary:        Private library of Qcas
Requires:       gcc-gfortran%{?_isa}
BuildRequires:  giac-devel

%description    -n libqcas
Private library of Qcas.

%package        -n libqcas-devel
Summary:        Development files of lib%{name}
Requires:       lib%{name}%{?_isa} = %{version}-%{release}

%description    -n libqcas-devel
This package contains libraries and header files for developing
applications that use lib%{name}.
#######################################

%package        data
Summary:        Data files of Qcas
Requires:       giac-doc
BuildArch:      noarch
%description    data
Data files of Qcas.

%prep
%autosetup -n %{name}-%{version}
rm -rf libtommath

%build
mkdir build && pushd build
%{qmake_qt5} ../%{name}.pro \
 QMAKE_CFLAGS_RELEASE="$RPM_OPT_FLAGS" \
 QMAKE_CXXFLAGS_RELEASE="$RPM_OPT_FLAGS" \
 QMAKE_LFLAGS="$RPM_LD_FLAGS"
%make_build

sed -e 's|CONFIG+=staticlib|#CONFIG+=staticlib|g' -i ../lib%{name}.pro
%{qmake_qt5} ../lib%{name}.pro QMAKE_STRIP=echo
%make_build
popd

mkdir build2 && pushd build2
%{qmake_qt4} ../%{name}.pro \
 QMAKE_CFLAGS_RELEASE="$RPM_OPT_FLAGS" \
 QMAKE_CXXFLAGS_RELEASE="$RPM_OPT_FLAGS" \
 QMAKE_LFLAGS="$RPM_LD_FLAGS"
%make_build
popd

%install
pushd build
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 ./qcas %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_libdir}
install -p -m 755 ./lib%{name}.* %{buildroot}%{_libdir}
ln -sf libqcas.so.1.0.0 %{buildroot}%{_libdir}/libqcas.so
ln -sf libqcas.so.1.0.0 %{buildroot}%{_libdir}/libqcas.so.1
ln -sf libqcas.so.1.0.0 %{buildroot}%{_libdir}/libqcas.so.1.0

mkdir -p %{buildroot}%{_includedir}/lib%{name}
install -pm 644 ui_MainWindow.h \
 ../qt/MainWindow.h \
 ../qt/output.h \
 ../qt/CasManager.h \
 ../qt/geometry.h \
 ../qt/config.h \
 ../qt/giacpy.h \
 ../qt/sizeof_void_p.h %{buildroot}%{_includedir}/lib%{name}/
mkdir -p %{buildroot}%{_includedir}/lib%{name}/gui
install -pm 644 ../qt/gui/WizardMatrix.h \
 ../qt/gui/WizardEquation.h \
 ../qt/gui/WizardCatalog.h \
 ../qt/gui/WizardAlgo.h \
 ../qt/gui/spreadsheet.h \
 ../qt/gui/qtmmlwidget.h \
 ../qt/gui/FormalSheet.h \
 ../qt/gui/FormalLineWidgets.h \
 ../qt/gui/FormalLine.h \
 ../qt/gui/CentralTabWidget.h \
 ../qt/gui/prefdialog.h \
 ../qt/gui/plotfunctiondialog.h  %{buildroot}%{_includedir}/lib%{name}/gui/
popd
pushd build2
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 ./qcas %{buildroot}%{_bindir}/qcas-qt4
popd
mkdir -p %{buildroot}%{_datadir}/qcas
cp -a qt/doc qt/lang qt/images %{buildroot}%{_datadir}/qcas
install -pm 644 qt/aide_cas %{buildroot}%{_datadir}/qcas
install -pm 644 qt/aide_cas %{buildroot}%{_datadir}/qcas/doc

mkdir -p %{buildroot}%{_datadir}/pixmaps
install -p -m 644 qt/images/icon.png %{buildroot}%{_datadir}/pixmaps/qcas.png

# Install desktop file
desktop-file-install %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-install %{SOURCE3} %{buildroot}%{_datadir}/applications/%{name}-qt4.desktop

# Install appdata file
mkdir -p %{buildroot}%{_datadir}/metainfo
install -pm 644 %{SOURCE2} %{buildroot}%{_datadir}/metainfo/
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

%ldconfig_scriptlets -n libqcas

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop

%files qt4
%{_bindir}/%{name}-qt4
%{_datadir}/applications/%{name}-qt4.desktop

%files -n libqcas
%license COPYING
%{_libdir}/libqcas.so.*

%files -n libqcas-devel
%{_libdir}/libqcas.so
%{_includedir}/lib%{name}/

%files data
%license COPYING
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/metainfo/%{name}.appdata.xml

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.3-25
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 19 2020 Antonio Trande <sagitter@fedoraproject.org> 0.5.3-14
- Rebuild for giac-1.6.0.7

* Wed Feb 05 2020 Antonio Trande <sagitter@fedoraproject.org> 0.5.3-13
- New rebuild for giac-1.5.0.85

* Tue Feb 04 2020 Antonio Trande <sagitter@fedoraproject.org> 0.5.3-12
- Rebuild for giac-1.5.0.85

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 10 2018 Antonio Trande <sagitter@fedoraproject.org> 0.5.3-8
- Rebuild for giac-1.5.0.3

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Antonio Trande <sagitter@fedoraproject.org> 0.5.3-5
- Rebuild for giac-1.4.9.45
- Use %%ldconfig_scriptlets

* Wed Jan 17 2018 Antonio Trande <sagitter@fedoraproject.org> 0.5.3-4
- Reorganize header files

* Sat Dec 23 2017 Antonio Trande <sagitter@fedoraproject.org> 0.5.3-3
- Fix symbolic links

* Sat Dec 23 2017 Antonio Trande <sagitter@fedoraproject.org> 0.5.3-2
- Fix library permissions
- Add ldconfig scripts

* Fri Dec 22 2017 Antonio Trande <sagitter@fedoraproject.org> 0.5.3-1
- Update to 0.5.3

* Fri Dec 22 2017 Antonio Trande <sagitter@fedoraproject.org> 0.5.2-5
- Fix dependencies

* Wed Dec 20 2017 Antonio Trande <sagitter@fedoraproject.org> 0.5.2-4
- Fix symbolic link

* Mon Dec 18 2017 Antonio Trande <sagitter@fedoraproject.org> 0.5.2-3
- Fix libqcas's dependencies

* Sat Dec 16 2017 Antonio Trande <sagitter@fedoraproject.org> 0.5.2-2
- Fix appdata file's path
- Install libqcas

* Fri Dec 01 2017 Antonio Trande <sagitter@fedoraproject.org> 0.5.2-1
- First package
