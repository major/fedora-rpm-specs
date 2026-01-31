%global pypi_name PyQt6_WebEngine

%define snap dev2510252014

Name:          python-pyqt6-webengine
Version:       6.10.1
Release:       0.1%{?snap:^%{snap}}%{?dist}
Summary:       Python bindings for Qt6WebEngine
License:       GPL-3.0-only
Url:           https://www.riverbankcomputing.com/software/pyqtwebengine/
Source0:       https://pypi.python.org/packages/source/P/PyQt6_WebEngine/pyqt6_webengine-%{version}%{?snap:.%{snap}}.tar.gz

ExclusiveArch: %{qt6_qtwebengine_arches}

## downstream patches

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: pkgconfig(Qt6WebEngineCore)
BuildRequires: pkgconfig(Qt6WebEngineQuick)
BuildRequires: pkgconfig(Qt6WebEngineWidgets)

BuildRequires: python%{python3_pkgversion}-devel python%{python3_pkgversion}
BuildRequires: python%{python3_pkgversion}-pyqt6 >= 6.2.0
BuildRequires: python%{python3_pkgversion}-pyqt6-devel
BuildRequires: %{py3_dist sip} >= 6
BuildRequires: %{py3_dist PyQt-builder} >= 1.11

%description
%{summary}.

%package -n python%{python3_pkgversion}-pyqt6-webengine
Summary: Python3 bindings for Qt6 WebEngine
Requires:  python%{python3_pkgversion}-pyqt6%{?_isa}
%{?python_provide:%python_provide python%{python3_pkgversion}-pyqt6-webengine}
%description -n python%{python3_pkgversion}-pyqt6-webengine
%{summary}.

%package -n python%{python3_pkgversion}-pyqt6-webengine-devel
Summary: Development files for %{name}
Requires: python3-pyqt6-webengine%{_isa} = %{version}-%{release}
Requires: python3-pyqt6-devel
%description -n python%{python3_pkgversion}-pyqt6-webengine-devel
%{summary}.


%prep
%autosetup -p1 -n pyqt6_webengine-%{version}%{?snap:.%{snap}} -p1

%build
sip-build \
  --no-make \
  --qmake=%{_qt6_qmake} \
  --api-dir=%{_qt6_datadir}/qsci/api/python \
  --target-dir=%{python3_sitearch} \
  --verbose \
  --qmake-setting 'QMAKE_CFLAGS_RELEASE="%{build_cflags}"' \
  --qmake-setting 'QMAKE_CXXFLAGS_RELEASE="%{build_cxxflags} -std=c++17"' \
  --qmake-setting 'QMAKE_LFLAGS_RELEASE="%{build_ldflags}"'

%make_build -C build


%install
%make_install INSTALL_ROOT=%{buildroot} -C build

# ensure .so modules are executable for proper -debuginfo extraction
for i in %{buildroot}%{python3_sitearch}/PyQt6/*.so ; do
test -x $i || chmod a+rx $i
done


%files -n python%{python3_pkgversion}-pyqt6-webengine
%doc README.md
%license LICENSE
%{python3_sitearch}/pyqt6_webengine-%{version}%{?snap:.%{snap}}.dist-info
%{python3_sitearch}/PyQt6/QtWebEngineCore.*
%{python3_sitearch}/PyQt6/QtWebEngineQuick.*
%{python3_sitearch}/PyQt6/QtWebEngineWidgets.*

%files -n python%{python3_pkgversion}-pyqt6-webengine-devel
%license LICENSE
%{python3_sitearch}/PyQt6/bindings/QtWebEngine*/
%dir %{_qt6_datadir}/qsci/
%dir %{_qt6_datadir}/qsci/api/
%dir %{_qt6_datadir}/qsci/api/python/
%{_qt6_datadir}/qsci/api/python/PyQt6-WebEngine.api


%changelog
* Thu Jan 29 2026 Jan Grulich <jgrulich@redhat.com> - 6.10.1-0.1
- Update to snapshot of 6.10.1
