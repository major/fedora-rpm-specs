Name:           python-sphinxcontrib-zopeext
Version:        0.3.3
Release:        1%{?dist}
Summary:        Sphinx extension for documenting Zope interfaces

License:        BSD-2-Clause
URL:            https://pypi.org/project/sphinxcontrib-zopeext/
BuildArch:      noarch
Source0:        %pypi_source sphinxcontrib-zopeext

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist docutils}
BuildRequires:  %{py3_dist importlib-metadata}
BuildRequires:  %{py3_dist pip}
BuildRequires:  %{py3_dist poetry}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist wheel}
BuildRequires:  %{py3_dist zope.interface}

%description
This sphinx extension provides an autointerface directive for Zope
interfaces.

%package     -n python3-sphinxcontrib-zopeext
Summary:        Sphinx extension for documenting Zope interfaces

# This can be removed when Fedora 36 reaches EOL
Obsoletes:      python3-j1m.sphinxautointerface < 0.3.0-15

%description -n python3-sphinxcontrib-zopeext
This sphinx extension provides an autointerface directive for Zope
interfaces.

%prep
%autosetup -n sphinxcontrib-zopeext-%{version}

# Work around what appears to be a python-packaging bug.  Try removing this
# on the next release.
sed -i 's/!=3.5\.\*,!=4\.0\.\*,!=4\.1\.\*,//' PKG-INFO pyproject.toml setup.py

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files 'sphinxcontrib*'

%files -n python3-sphinxcontrib-zopeext -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
* Mon Sep  5 2022 Jerry James <loganjerry@gmail.com> - 0.3.3-1
- Version 0.3.3
- Drop upstreamed Sphinx 5 patch
- Convert License tag to SPDX

* Tue Jul 26 2022 Jerry James <loganjerry@gmail.com> - 0.3.2-6
- Adapt to Sphinx 5

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Jerry James <loganjerry@gmail.com> - 0.3.2-4
- Permit use of Sphinx 5 (rhbz#2108366)
- Minor spec file cleanups

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 0.3.2-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan  6 2022 Jerry James <loganjerry@gmail.com> - 0.3.2-1
- Version 0.3.2

* Wed Jan  5 2022 Jerry James <loganjerry@gmail.com> - 0.3.1-1
- Version 0.3.1
- Do not install sphinxcontrib/__init__.py (bz 2036438)

* Thu Dec 23 2021 Jerry James <loganjerry@gmail.com> - 0.3.0-1
- Version 0.3.0
- Remove %%check for now; nox is required but unavailable

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.4-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 15 2020 Jerry James <loganjerry@gmail.com> - 0.2.4-2
- Be more specific about owned directories
- Drop the deprecated pytest-runner BR and remove the dep from setup.py

* Mon Jun 15 2020 Jerry James <loganjerry@gmail.com> - 0.2.4-1
- Initial RPM
