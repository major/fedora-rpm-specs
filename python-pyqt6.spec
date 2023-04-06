%if 0%{?fedora} || 0%{?rhel} > 6
%global python3_dbus_dir %(%{__python3} -c "import dbus.mainloop; print(dbus.mainloop.__path__[0])" 2>/dev/null || echo "%{python3_sitearch}/dbus/mainloop")
%endif


Summary: PyQt6 is Python bindings for Qt6
Name:    python-pyqt6
Version: 6.4.0
Release: 7%{?dist}

License: GPLv3
Url:     http://www.riverbankcomputing.com/software/pyqt/
Source0: https://pypi.python.org/packages/source/P/PyQt6/PyQt6-%{version}.tar.gz
Source1: macros.pyqt6


BuildRequires: make
BuildRequires: chrpath
BuildRequires: findutils
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(dbus-python)
BuildRequires: pkgconfig(libpulse-mainloop-glib)

BuildRequires: qt6-qtbase-private-devel

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Bluetooth)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Designer)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Multimedia) 
BuildRequires: cmake(Qt6Nfc)
BuildRequires: cmake(Qt6Network) 
BuildRequires: cmake(Qt6OpenGL)
BuildRequires: cmake(Qt6Positioning)
BuildRequires: cmake(Qt6Quick) cmake(Qt6QuickWidgets)
BuildRequires: cmake(Qt6Sensors)
BuildRequires: cmake(Qt6SerialPort)
BuildRequires: cmake(Qt6Sql) 
BuildRequires: cmake(Qt6Svg) 
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(Qt6WebChannel)
BuildRequires: cmake(Qt6WebSockets)
BuildRequires: cmake(Qt6Quick3D)
BuildRequires: cmake(Qt6Quick3DRuntimeRender)
BuildRequires: cmake(Qt6RemoteObjects)

BuildRequires: python%{python3_pkgversion}-devel python%{python3_pkgversion}
BuildRequires: python%{python3_pkgversion}-dbus
BuildRequires: %{py3_dist PyQt-builder} >= 1.1.0
BuildRequires: %{py3_dist sip}

%description
%{summary}.

%global __provides_exclude_from ^(%{_qt6_plugindir}/.*\\.so)$

%package rpm-macros
Summary: RPM macros %{name}
BuildArch: noarch
%description rpm-macros
%{summary}.

%package -n python%{python3_pkgversion}-pyqt6
Summary: Python 3 bindings for Qt6
Provides: PyQt6 = %{version}-%{release}
Provides: PyQt6%{?_isa} = %{version}-%{release}
Provides: python%{python3_pkgversion}-PyQt6 = %{version}-%{release}
Provides: python%{python3_pkgversion}-PyQt6%{?_isa} = %{version}-%{release}
Requires: python%{python3_pkgversion}-pyqt6-base%{?_isa} = %{version}-%{release}
%{?py_provides:%py_provides python%{python3_pkgversion}-pyqt6}

%description -n python%{python3_pkgversion}-pyqt6
%{summary}.

%package -n python%{python3_pkgversion}-pyqt6-base
Summary: Python 3 bindings for Qt6 base
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
Provides: python%{python3_pkgversion}-PyQt6-base = %{version}-%{release}
Provides: python%{python3_pkgversion}-PyQt6-base%{?_isa} = %{version}-%{release}
Requires: %{name}-rpm-macros = %{version}-%{release}
Requires: python%{python3_pkgversion}-dbus
%{?py_provides:%py_provides python%{python3_pkgversion}-pyqt6-base}

%description -n python%{python3_pkgversion}-pyqt6-base
%{summary}.

%package -n python%{python3_pkgversion}-pyqt6-devel
Summary: Development files for python3-qt6
Requires: python%{python3_pkgversion}-pyqt6%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel
Provides: python%{python3_pkgversion}-PyQt6-devel = %{version}-%{release}
%{?py_provides:%py_provides python%{python3_pkgversion}-pyqt6-devel}

%description -n python%{python3_pkgversion}-pyqt6-devel
Files needed to build other bindings for C++ classes that inherit from any
of the Qt6 classes.

%package doc
Summary: Developer documentation for %{name}
Provides: PyQt6-doc = %{version}-%{release}
BuildArch: noarch
%description doc
%{summary}.


%prep
%autosetup -n PyQt6-%{version}%{?snap:.%{snap}} -p1

%build

PATH=%{_qt6_bindir}:$PATH ; export PATH

# Python 3 build:
sip-build \
  --no-make \
  --qt-shared \
  --confirm-license \
  --qmake=%{_qt6_qmake} \
  --api-dir=%{_qt6_datadir}/qsci/api/python \
  --verbose \
  --dbus=%{_includedir}/dbus-1.0/ \
  --pep484-pyi \
  --qmake-setting 'QMAKE_CFLAGS_RELEASE="%{build_cflags}"' \
  --qmake-setting 'QMAKE_CXXFLAGS_RELEASE="%{build_cxxflags} `pkg-config --cflags dbus-python`"' \
  --qmake-setting 'QMAKE_LFLAGS_RELEASE="%{build_ldflags}"'

%make_build -C build

%install

# Python 3 build:
%make_install INSTALL_ROOT=%{buildroot} -C build
if [ "%{_prefix}" != "/usr" ]; then
  cp -ru %{buildroot}/usr/* %{buildroot}%{_prefix}/ || echo "Nothing to copy"
  rm -rf %{buildroot}/usr/*
fi

# Explicitly byte compile as the automagic byte compilation doesn't work for
# /app prefix in flatpak builds
%py_byte_compile %{__python3} %{buildroot}%{python3_sitearch}/PyQt6

# ensure .so modules are executable for proper -debuginfo extraction
find %{buildroot} -type f -name '*.so' | xargs chmod a+rx

# rpm macros
install -p -m644 -D %{SOURCE1} \
  %{buildroot}%{_rpmmacrodir}/macros.pyqt6
sed -i \
  -e "s|@@NAME@@|%{name}|g" \
  -e "s|@@EPOCH@@|%{?epoch}%{!?epoch:0}|g" \
  -e "s|@@VERSION@@|%{version}|g" \
  -e "s|@@EVR@@|%{?epoch:%{epoch:}}%{version}-%{release}|g" \
  %{buildroot}%{_rpmmacrodir}/macros.pyqt6


%files rpm-macros
%{_rpmmacrodir}/macros.pyqt6

%files -n python%{python3_pkgversion}-pyqt6

%{python3_sitearch}/PyQt6/QtBluetooth.*
%{python3_sitearch}/PyQt6/QtDesigner.*
%{python3_sitearch}/PyQt6/QtHelp.*
%{python3_sitearch}/PyQt6/QtMultimedia.*
%{python3_sitearch}/PyQt6/QtMultimediaWidgets.*
%{python3_sitearch}/PyQt6/QtNfc.*
%{python3_sitearch}/PyQt6/QtPositioning.*
%{python3_sitearch}/PyQt6/QtQml.*
%{python3_sitearch}/PyQt6/QtQuick.*
%{python3_sitearch}/PyQt6/QtQuickWidgets.*
%{python3_sitearch}/PyQt6/QtSensors.*
%{python3_sitearch}/PyQt6/QtSerialPort.*
%{python3_sitearch}/PyQt6/QtSvg.*
%{python3_sitearch}/PyQt6/QtWebChannel.*
%{python3_sitearch}/PyQt6/QtWebSockets.*
%{python3_sitearch}/PyQt6/QtOpenGLWidgets.*
%{python3_sitearch}/PyQt6/QtSvgWidgets.*
%{python3_sitearch}/PyQt6/QtQuick3D.*
%{python3_sitearch}/PyQt6/QtRemoteObjects.*


%files -n python%{python3_pkgversion}-pyqt6-base
%doc NEWS README
%license LICENSE
%{python3_dbus_dir}/pyqt6.abi3.so
%dir %{python3_sitearch}/PyQt6/
%{python3_sitearch}/PyQt6-%{version}%{?snap:.%{snap}}.dist-info
%{python3_sitearch}/PyQt6/__pycache__/__init__.*
%{python3_sitearch}/PyQt6/__init__.py*
%{python3_sitearch}/PyQt6/QtCore.*
%{python3_sitearch}/PyQt6/QtDBus.*
%{python3_sitearch}/PyQt6/QtGui.*
%{python3_sitearch}/PyQt6/QtNetwork.*
%{python3_sitearch}/PyQt6/QtOpenGL.*
%{python3_sitearch}/PyQt6/QtPrintSupport.*
%{python3_sitearch}/PyQt6/QtSql.*
%{python3_sitearch}/PyQt6/QtTest.*
%{python3_sitearch}/PyQt6/QtWidgets.*
%{python3_sitearch}/PyQt6/QtXml.*

# plugins
%{_qt6_plugindir}/PyQt6/
%{_qt6_plugindir}/designer/libpyqt6.so
%{python3_sitearch}/PyQt6/uic/
%{python3_sitearch}/PyQt6/lupdate/
%{_bindir}/pylupdate6
%{_bindir}/pyuic6
%{python3_sitearch}/PyQt6/py.typed
%{python3_sitearch}/PyQt6/sip.pyi

%files -n python%{python3_pkgversion}-pyqt6-devel
%{python3_sitearch}/PyQt6/bindings/


%files doc
#doc doc/*
%doc examples/
# avoid dep on qscintilla-python, own %%_qt6_datadir/qsci/... here for now
%dir %{_qt6_datadir}/qsci/
%dir %{_qt6_datadir}/qsci/api/
%dir %{_qt6_datadir}/qsci/api/python/
%doc %{_qt6_datadir}/qsci/api/python/PyQt6.api


%changelog
* Tue Apr 04 2023 Jan Grulich <jgrulich@redhat.com> - 6.4.0-7
- Rebuild (qt6)

* Wed Mar 29 2023 Tomas Popela <tpopela@redhat.com> - 6.4.0-6
- Rebuild to fix ELN build

* Mon Mar 27 2023 Jan Grulich <jgrulich@redhat.com> - 6.4.0-5
- Rebuild (qt6)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Jan Grulich <jgrulich@redhat.com> - 6.4.0-3
- Rebuild (qt6)

* Thu Nov 24 2022 Jan Grulich <jgrulich@redhat.com> - 6.4.0-2
- Rebuild (qt6)

* Tue Nov 08 2022 Jan Grulich <jgrulich@redhat.com> - 6.4.0-1
- 6.4.0

* Tue Sep 06 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 6.3.1-1
- 6.3.1

* Tue Sep 06 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 6.3.0-1
- Initial PyQt6

