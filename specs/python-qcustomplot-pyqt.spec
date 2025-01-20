%global QCP_VER 2.1.1
Name:          python-qcustomplot-pyqt
Version:       2.1.1.2
Release:       2%{?dist}
Summary:       Python bindings for QCustomPlot2
# https://github.com/salsergey/QCustomPlot-PyQt/issues/7
License:       MIT and GPLv3
Url:           https://github.com/salsergey/QCustomPlot-PyQt
Source0:       %{url}/releases/download/v%{version}/QCustomPlot-PyQt-%{version}.tar.gz
BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: python3-devel
# sip6
BuildRequires: %{py3_dist sip}
BuildRequires: %{py3_dist PyQt-builder}

%description
This is Python bindings for QCustomPlot - Qt C++ library for plotting and data
visualization.


%package -n python3-qcustomplot-pyqt5
Summary:       PyQt5 binding for QCustomPlot2
License:       MIT
BuildRequires: qt5-qtbase-devel
# qcustomplot-qt5-devel
BuildRequires: pkgconfig(qcustomplot-qt5) == %{QCP_VER}
BuildRequires: python3-qt5-devel
Requires:      python3-qt5
Requires:      qcustomplot-qt5 == %{QCP_VER}

%description -n python3-qcustomplot-pyqt5
This is Python-PyQt5 binding for QCustomPlot - Qt C++ library for plotting and
data visualization.


%package -n python3-qcustomplot-pyqt6
Summary:       PyQt6 binding for QCustomPlot2
License:       MIT and GPLv3
BuildRequires: qt6-qtbase-devel
# qcustomplot-qt6-devel
BuildRequires: pkgconfig(qcustomplot-qt6) == %{QCP_VER}
BuildRequires: python3-pyqt6-devel
Requires:      python3-pyqt6
Requires:      qcustomplot-qt6 == %{QCP_VER}

%description -n python3-qcustomplot-pyqt6
This is Python-PyQt6 binding for QCustomPlot - Qt C++ library for plotting and
data visualization.


%prep
%autosetup -n QCustomPlot-PyQt-%{version}
rm -rf src


%build
# qt5
sip-build \
  --build-dir build-qt5 \
  --qmake %{_qt5_qmake} \
  --qcustomplot-lib qcustomplot-qt5 \
  --no-static-qcustomplot \
  --no-make \
  --qmake-setting 'QMAKE_CFLAGS_RELEASE="%{build_cflags}"' \
  --qmake-setting 'QMAKE_CXXFLAGS_RELEASE="%{build_cxxflags}"' \
  --qmake-setting 'QMAKE_LFLAGS_RELEASE="%{build_ldflags}"'
%make_build -C build-qt5
# qt6
sip-build \
  --build-dir build-qt6 \
  --qmake %{_qt6_qmake} \
  --qcustomplot-lib qcustomplot-qt6 \
  --no-static-qcustomplot \
  --no-make \
  --qmake-setting 'QMAKE_CFLAGS_RELEASE="%{build_cflags}"' \
  --qmake-setting 'QMAKE_CXXFLAGS_RELEASE="%{build_cxxflags}"' \
  --qmake-setting 'QMAKE_LFLAGS_RELEASE="%{build_ldflags}"'
%make_build -C build-qt6


%install
pushd build-qt5
%make_install INSTALL_ROOT=%{buildroot}
popd
pushd build-qt6
%make_install INSTALL_ROOT=%{buildroot}
# small hack
chmod a+rx %{buildroot}%{_libdir}/python%{python3_version}/site-packages/QCustomPlot_PyQt*.so


%files -n python3-qcustomplot-pyqt5
%doc README.md examples/
%license LICENSE-MIT.txt LICENSE-gpl-3.0.txt
%{_libdir}/python%{python3_version}/site-packages/QCustomPlot_PyQt5*

%files -n python3-qcustomplot-pyqt6
%doc README.md
%license LICENSE-MIT.txt LICENSE-gpl-3.0.txt
%{_libdir}/python%{python3_version}/site-packages/QCustomPlot_PyQt6*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Sep 28 2024 TI_Eugene <ti.eugene@gmail.com> - 2.1.1.2-1
- Version bump

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.1.1.1-10
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 2.1.1.1-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 05 2023 TI_Eugene <ti.eugene@gmail.com> - 2.1.1.1-4
- Licenses dispatched
- 'examples/' added to pyqt5 subpackage doc

* Thu Jan 05 2023 TI_Eugene <ti.eugene@gmail.com> - 2.1.1.1-3
- Debug packages enabled
- .so permissions fixed

* Fri Dec 30 2022 TI_Eugene <ti.eugene@gmail.com> - 2.1.1.1-2
- Licenses updated
- gcc-c++ requirement added
- QCP sources removed

* Fri Dec 23 2022 TI_Eugene <ti.eugene@gmail.com> - 2.1.1.1-1
- Initial Fedora build
