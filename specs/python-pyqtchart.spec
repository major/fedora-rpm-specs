Name:           python-pyqtchart
Version:        5.15.5
Release:        %autorelease
Summary:        Set of Python bindings for The Qt Charts library
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://www.riverbankcomputing.com/software/pyqtchart/
Source0:        %{pypi_source PyQtChart}

BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-qt5-devel
BuildRequires:  python3dist(sip) >= 5.3
BuildRequires:  python3dist(pyqt-builder) >= 1.6
BuildRequires:  qt5-qtcharts-devel
# as of 2020-04-18, depends on libQt5Charts.so.5(Qt_5.14.2_PRIVATE_API)(64bit)
BuildRequires:  qt5-qtbase-private-devel

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} >= 42 || 0%{?rhel} >= 11
ExcludeArch:    %{ix86}
%endif

%global distinfo %{python3_sitearch}/PyQtChart-%{version}.dist-info

%description
PyQtChart is a set of Python bindings for The Qt Company's Qt Charts library.
The bindings sit on top of PyQt5 and are implemented as a single module.


%package -n python3-pyqtchart
Summary:    %{summary}
Requires:   python3-qt5

%description -n python3-pyqtchart
PyQtChart is a set of Python 3 bindings for The Qt Company's Qt Charts library.
The bindings sit on top of PyQt5 and are implemented as a single module.


%package -n python3-pyqtchart-devel
Summary:    Development files for PyQtChart
Requires:   python3-pyqtchart%{_isa} == %{version}-%{release}
# For the directories:
Requires:   python3-qt5-devel
Requires:   python3-qscintilla-qt5

%description -n python3-pyqtchart-devel
Development files for PyQtChart, such as sip files.


%prep
%autosetup -p1 -n PyQtChart-%{version}


%build
%set_build_flags
sip-build \
  --no-make \
  --qmake="%{_qt5_qmake}" \
  --api-dir=%{_qt5_datadir}/qsci/api/python \
  --verbose
%make_build CXXFLAGS="%{optflags} -fPIC \$(DEFINES)" -C build


%install
%make_install INSTALL_ROOT=%{buildroot} -C build

# Make sure all modules are executable for RPM to get their dependencies, debuginfo, etc.
chmod a+rx %{buildroot}%{python3_sitearch}/PyQt5/*.so

%check
# Make sure we don't leak buildroot to dist-info
grep %{buildroot} %{buildroot}%{distinfo}/* && exit 1 || true


%files -n python3-pyqtchart
%license LICENSE
%doc ChangeLog NEWS README
%{python3_sitearch}/PyQt5/QtChart.*
%{distinfo}/

%files -n python3-pyqtchart-devel
%{_datadir}/qt5/qsci/api/python/PyQtChart.api
%{python3_sitearch}/PyQt5/bindings/QtChart/


%changelog
%autochangelog
