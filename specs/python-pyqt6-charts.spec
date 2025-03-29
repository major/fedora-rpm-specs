%global pypi_name PyQt6_Charts

%define snap dev2503181029

Name:           python-pyqt6-charts
Version:        6.9.0
Release:        0.1%{?snap:^%{snap}}%{?dist}
Summary:        Set of Python bindings for The Qt Charts library
License:        GPL-3.0-only
URL:            https://www.riverbankcomputing.com/software/pyqtchart/
Source0:        https://pypi.python.org/packages/source/P/PyQt6_Charts/pyqt6_charts-%{version}%{?snap:.%{snap}}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-pyqt6-devel >= 6.2.0
BuildRequires:  %{py3_dist sip} >= 6
BuildRequires:  %{py3_dist PyQt-builder} >= 1.10
BuildRequires:  qt6-qtcharts-devel

%description
PyQt6_Charts is a set of Python bindings for The Qt Company's Qt Charts library.
The bindings sit on top of PyQt6 and are implemented as a single module.


%package -n python3-pyqt6-charts
Summary:    %{summary}
%{?python_provide:%python_provide python3-pyqt6-charts}
Requires:   python3-pyqt6

%description -n python3-pyqt6-charts
PyQt6_Charts is a set of Python 3 bindings for The Qt Company's Qt Charts library.
The bindings sit on top of PyQt6 and are implemented as a single module.


%package -n python3-pyqt6-charts-devel
Summary:    Development files for PyQt6_Charts
%{?python_provide:%python_provide python3-pyqt6-charts-devel}
Requires:   python3-pyqt6-charts%{_isa} = %{version}-%{release}
Requires:   python3-pyqt6-devel

%description -n python3-pyqt6-charts-devel
Development files for PyQt6_Charts, such as sip files.


%prep
%autosetup -p1 -n pyqt6_charts-%{version}%{?snap:.%{snap}} -p1


%build
sip-build \
  --no-make \
  --qmake="%{_qt6_qmake}" \
  --api-dir=%{_qt6_datadir}/qsci/api/python \
  --verbose \
  --qmake-setting 'QMAKE_CFLAGS_RELEASE="%{build_cflags}"' \
  --qmake-setting 'QMAKE_CXXFLAGS_RELEASE="%{build_cxxflags}"' \
  --qmake-setting 'QMAKE_LFLAGS_RELEASE="%{build_ldflags}"'

%make_build -C build


%install
%make_install INSTALL_ROOT=%{buildroot} -C build

# Make sure all modules are executable for RPM to get their dependencies, debuginfo, etc.
for i in %{buildroot}%{python3_sitearch}/PyQt6/*.so ; do
test -x $i || chmod a+rx $i
done

%check
# Make sure we don't leak buildroot to dist-info
grep %{buildroot} %{buildroot}%{python3_sitearch}/*.dist-info/* && exit 1 || true


%files -n python3-pyqt6-charts
%license LICENSE
%doc ChangeLog NEWS README.md
%{python3_sitearch}/PyQt6_Charts-%{version}%{?snap:.%{snap}}.dist-info
%{python3_sitearch}/PyQt6/QtCharts.*

%files -n python3-pyqt6-charts-devel
%{python3_sitearch}/PyQt6/bindings/QtCharts/
%dir %{_qt6_datadir}/qsci/
%dir %{_qt6_datadir}/qsci/api/
%dir %{_qt6_datadir}/qsci/api/python/
%{_qt6_datadir}/qsci/api/python/PyQt6-Charts.api


%changelog
%autochangelog
