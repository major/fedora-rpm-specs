%global pypi_name ipywidgets

Name:           python-%{pypi_name}
Version:        8.0.4
Release:        1%{?dist}
Summary:        IPython HTML widgets for Jupyter

License:        BSD
URL:            http://ipython.org
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
Interactive HTML widgets for Jupyter notebooks and the IPython kernel.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Interactive HTML widgets for Jupyter notebooks and the IPython kernel.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# Jupyterlab_widgets is a new dependency in ipywidgets 7.6
# and it contains code which enables widgets in Jupyter lab
# not requiring any manual steps. But we don't have Jupyter lab
# in Fedora yet so we do not need this package at all.
sed -i "/jupyterlab_widgets/d" setup.cfg

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
* Thu Dec 22 2022 Lumír Balhar <lbalhar@redhat.com> - 8.0.4-1
- Update to 8.0.4 (rhbz#2155794)

* Wed Dec 07 2022 Lumír Balhar <lbalhar@redhat.com> - 8.0.3-1
- Update to 8.0.3 (rhbz#2151510)

* Sat Sep 03 2022 Lumír Balhar <lbalhar@redhat.com> - 8.0.2-1
- Update to 8.0.2
Resolves: rhbz#2123852

* Mon Aug 22 2022 Lumír Balhar <lbalhar@redhat.com> - 8.0.1-1
- Update to 8.0.1
Resolves: rhbz#2119307

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 7.7.0-3
- Rebuilt for Python 3.11

* Wed Jun 08 2022 Lumír Balhar <lbalhar@redhat.com> - 7.7.0-2
- Fix tests for Python 3.11
Resolves: rhbz#2086425

* Mon May 16 2022 Lumír Balhar <lbalhar@redhat.com> - 7.7.0-1
- Update to 7.7.0

* Thu Feb 03 2022 Lumír Balhar <lbalhar@redhat.com> - 7.6.5-1
- Update to 7.6.5
Resolves: rhbz#2023926

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 01 2021 Lumír Balhar <lbalhar@redhat.com> - 7.6.4-1
- Update to 7.6.4
Resolves: rhbz#1977142

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 7.6.3-2
- Rebuilt for Python 3.10

* Thu Feb 11 2021 Lumír Balhar <lbalhar@redhat.com> - 7.6.3-1
- Update to 7.6.3
Resolves: rhbz#1927539

* Mon Feb 08 2021 Lumír Balhar <lbalhar@redhat.com> - 7.5.1-4
- Fix tests for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Lumír Balhar <lbalhar@redhat.com> - 7.5.1-1
- Initial package.
