# Architectures currently not supported
# http://xcas.e.ujf-grenoble.fr/XCAS/viewtopic.php?f=19&t=1723
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: aarch64 %{ix86} %{power64} s390x

Name:          qcas
Summary:       Qt5 GUI application for Giac
Version:       0.5.4
Release:       %autorelease
License:       GPL-3.0-or-later
URL:           https://webusers.imj-prg.fr/~frederic.han/qcas/
Source0:       https://gitlab.math.univ-paris-diderot.fr/han/qcas/-/archive/%{version}/%{name}-%{version}.tar.gz
Source1:       %{name}.desktop
Source2:       %{name}.appdata.xml
Source3:       %{name}-qt4.desktop

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: gmp-devel
BuildRequires: giac-devel >= 2.0.0
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
Requires:      %{name}-data = %{version}-%{release}
Requires:       giac%{?_isa} >= 2.0.0

%description
Minimal Qt5 interface for Giac.

%package        qt4
Summary:        Qt4 GUI application for Giac
BuildRequires:  qt-devel
Requires:      %{name}-data = %{version}-%{release}
Requires:       giac%{?_isa} >= 2.0.0
%description    qt4
Minimal Qt4 interface for Giac.

### This library is used by giacpy ####
%package        -n libqcas
Summary:        Private library of Qcas
Requires:       gcc-gfortran%{?_isa}
BuildRequires:  giac-devel >= 2.0.0

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
Requires:       giac-doc >= 2.0.0
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
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE2} %{buildroot}%{_metainfodir}/
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop

%files qt4
%{_bindir}/%{name}-qt4
%{_datadir}/applications/%{name}-qt4.desktop

%files -n libqcas
%license COPYING
%{_libdir}/libqcas.so.1
%{_libdir}/libqcas.so.1.0
%{_libdir}/libqcas.so.1.0.0

%files -n libqcas-devel
%{_libdir}/libqcas.so
%{_includedir}/lib%{name}/

%files data
%license COPYING
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_metainfodir}/%{name}.appdata.xml

%changelog
%autochangelog
