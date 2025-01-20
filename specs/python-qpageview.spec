# Created by pyp2rpm-3.3.8
%global pypi_name qpageview
%global pypi_version 0.6.2

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        10%{?dist}
Summary:        Widget to display page-based documents for Qt5/PyQt5

License:        GPL-3.0-or-later AND GPL-2.0-or-later
URL:            https://github.com/frescobaldi/qpageview
Source0:        %{pypi_source %pypi_name}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-qt5
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3-docs

%description
The qpageview module *qpageview* provides a page based document viewer widget
for Qt5/PyQt5.It has a flexible architecture potentionally supporting many
formats. Currently, it supports SVG documents, images, and, using the Poppler-
Qt5 binding, PDF documents.:: import qpageview from PyQt5.Qt import * a
QApplication([]) v qpageview.View() v.show() v.loadPdf("path/to/afile.pdf")
Homepage < •...

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
The qpageview module *qpageview* provides a page based document viewer widget
for Qt5/PyQt5.It has a flexible architecture potentionally supporting many
formats. Currently, it supports SVG documents, images, and, using the Poppler-
Qt5 binding, PDF documents.:: import qpageview from PyQt5.Qt import * a
QApplication([]) v qpageview.View() v.show() v.loadPdf("path/to/afile.pdf")
Homepage < •...

%package doc
Summary:        Documentation for qpageview
%description doc
Documentation for qpageview

%prep
%autosetup -n %{pypi_name}-%{pypi_version}

# Use local objects.inv for intersphinx
sed -e "s|\('https://docs\.python\.org/3', \)None|\1'%{_docdir}/python3-docs/html/objects.inv'|" \
  -i docs/source/conf.py

%build
%pyproject_wheel
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files qpageview

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE docs/source/license.rst
%doc README.rst

%files doc
%doc html
%license LICENSE docs/source/license.rst

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.6.2-8
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 0.6.2-4
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 23 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.6.2-2
- Review fixes.

* Thu May 05 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.6.2-1
- Initial package.
