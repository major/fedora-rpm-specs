%global pypi_name guizero

Name:           python-%{pypi_name}
Version:        1.3.0
Release:        4%{?dist}
Summary:        Python module to allow learners to easily create GUIs
License:        BSD
URL:            https://github.com/lawsie/guizero
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-tkinter
BuildRequires:  python3dist(pytest)
BuildRequires:  /usr/bin/xvfb-run
BuildRequires:  font(dejavusans)
BuildRequires:  font(dejavuserif)
BuildRequires:  pyproject-rpm-macros

%description
Guizero is designed to allow new learners to quickly and easily create
GUIs for their programs.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(pillow) >= 4.3
Requires:       python3-tkinter

%description -n python3-%{pypi_name}
Guizero is designed to allow new learners to quickly and easily create
GUIs for their programs.


%generate_buildrequires
%pyproject_buildrequires -r


%prep
%autosetup -n %{pypi_name}-%{version}

# use free fonts in tests
sed -i 's/Times New Roman/DejaVu Serif/g' tests/*.py
sed -i 's/Arial/DejaVu Sans/g' tests/*.py


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files guizero


%check
# if called form builddir, tests open a window when collecting and hang until closed
pushd tests
export PYTHONPATH=%{buildroot}%{python3_sitelib}
xvfb-run %{__python3} -m pytest -v
popd


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license license.txt


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.3.0-2
- Rebuilt for Python 3.11

* Tue Mar 08 2022 Charalampos Stratakis <cstratak@redhat.com> - 1.3.0-1
- Update to 1.3.0
- Fixes: rhbz#2036490

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 25 2021 Tomas Hrnciar <thrnciar@redhat.com> - 1.2.0-1
- Update to 1.2.0

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 09:32:39 CET 2021 Tomas Hrnciar <thrnciar@redhat.com> - 1.1.0-4
- Update to 1.1.1
- Spec converted to use pyproject-rpm-macros

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-2
- Rebuilt for Python 3.9

* Tue Mar 17 2020 Tomas Hrnciar <thrnciar@redhat.com> - 1.1.0-1
- Update to 1.1.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.4-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Tue Aug 27 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.4-1
- Update to 0.6.4 (#1745741)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.3-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 14 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.3-1
- Initial package
