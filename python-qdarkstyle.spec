# Created by pyp2rpm-3.3.2
%global pypi_name qdarkstyle
%global mod_name QDarkStyle

# PySide2 is broken with Python 3.12; do not support it on Fedora 39 and later.
#
# python-pyside2 fails to build with Python 3.12: error: use of undeclared
#     identifier 'PyUnicode_AS_UNICODE'
# https://bugzilla.redhat.com/show_bug.cgi?id=2155447
#
# python3-shiboken2-devel wants python < 3.11
# https://bugzilla.redhat.com/show_bug.cgi?id=2149820
#
# F39FailsToInstall: python3-pyside2, python3-shiboken2,
#     python3-shiboken2-devel
# https://bugzilla.redhat.com/show_bug.cgi?id=2220452
#
# Bug python-pyside2: FTBFS in Fedora rawhide/f39
# https://bugzilla.redhat.com/show_bug.cgi?id=2226300
%bcond pyside2 %{expr:0%{?fedora} < 39}

Name:           python-%{pypi_name}
Version:        3.0.2
Release:        %autorelease
Summary:        A dark stylesheet for Python and Qt applications

License:        MIT
URL:            https://github.com/ColinDuquesnoy/QDarkStyleSheet
Source0:        https://files.pythonhosted.org/packages/source/q/%{pypi_name}/QDarkStyle-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(helpdev) >= 0.6.2
BuildRequires:  python3dist(m2r)
BuildRequires:  python3dist(pyqt5)
%if %{with pyside2}
BuildRequires:  python3dist(pyside2)
%endif
BuildRequires:  python3dist(qtpy) >= 1.7
BuildRequires:  python3dist(qtsass)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3-watchdog

# required for tests
BuildRequires:  python3-PyQt4
BuildRequires:  python3dist(pyqtgraph)
BuildRequires:  python3dist(tox)

%description
A dark stylesheet for Qt applications (Qt4, Qt5, PySide, PySide2, PyQt4, 
PyQt5, QtPy, PyQtGraph).

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
%if %{with pyside2}
Requires:       (python3dist(pyqt5) or python3dist(pyside2))
%else
Requires:       (python3dist(pyqt5))
%endif
Requires:       python3dist(pyqt5)
Requires:       python3dist(qtpy) >= 1.7
Requires:       python3dist(qtsass)

Recommends:     python3dist(helpdev) >= 0.6.2

%description -n python3-%{pypi_name}
A dark stylesheet for Qt applications (Qt4, Qt5, PySide, PySide2, PyQt4, 
PyQt5, QtPy, PyQtGraph).


%prep
%autosetup -n QDarkStyle-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE.rst
%doc AUTHORS.rst CHANGES.rst CONTRIBUTING.rst
%{_bindir}/qdarkstyle
%{_bindir}/qdarkstyle.example
%{_bindir}/qdarkstyle.utils
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{mod_name}-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
