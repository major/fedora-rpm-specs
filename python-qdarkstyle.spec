# Created by pyp2rpm-3.3.2
%global pypi_name qdarkstyle
%global mod_name QDarkStyle

Name:           python-%{pypi_name}
Version:        3.0.2
Release:        8%{?dist}
Summary:        A dark stylesheet for Python and Qt applications

License:        MIT
URL:            https://github.com/ColinDuquesnoy/QDarkStyleSheet
Source0:        https://files.pythonhosted.org/packages/source/q/%{pypi_name}/QDarkStyle-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(helpdev) >= 0.6.2
BuildRequires:  python3dist(m2r)
BuildRequires:  python3dist(pyqt5)
BuildRequires:  python3dist(pyside2)
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
 
Requires:       (python3dist(pyqt5) or python3dist(pyside2))
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
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 01 2022 Python Maint <python-maint@redhat.com> - 3.0.2-5
- Rebuilt for Python 3.11

* Thu May 12 2022 Miro Hrončok <mhroncok@redhat.com> - 3.0.2-4
- Drop build time requires from runtime
- Fixes: rhbz#2064905

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 05 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.0.2-1
- Update to 3.0.2

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.8.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 28 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.8.1-1
- Update to 2.8.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.8-2
- Rebuilt for Python 3.9

* Mon Mar 16 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.8-1
- Update to 2.8 
- uses pyside2

* Sat Dec 21 2019 Mukundan Ragavan <nonamedotc@gmail.com> - 2.7-1
- Initial package.
