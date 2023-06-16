%global _python_bytecompile_errors_terminate_build 0

%global pypi_name readability-lxml

Name:           python-%{pypi_name}
Version:        0.8.1
Release:        10%{?dist}
Summary:        Fast html to text parser (article readability tool)

License:        Apache-2.0 
URL:            https://github.com/buriy/python-readability
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(chardet)
BuildRequires:  python3dist(cssselect)
BuildRequires:  python3dist(lxml)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(timeout-decorator)

%description
Given a html document, it pulls out the main body text and cleans it up.

This is a python port of a ruby port of arc90's readability project.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%?python_enable_dependency_generator

%description -n python3-%{pypi_name}
Given a html document, it pulls out the main body text and cleans it up.

This is a python port of a ruby port of arc90's readability project.


%prep
%autosetup -n python-readability-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Remove shebang from Python libraries
for lib in readability/*.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done


%build
%py3_build


%install
%py3_install


%check
%{python3} -m pytest -v


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/readability_lxml-*-py%{python3_version}.egg-info
%{python3_sitelib}/readability/


%changelog
* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.8.1-10
- Rebuilt for Python 3.12

* Wed Mar 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.8.1-9
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.8.1-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 27 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.8.1-1
- Update to 0.8.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-4.20200326gitede4d01
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-3.20200326gitede4d01
- Rebuilt for Python 3.9

* Thu Mar 26 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.1-2.20200326gitede4d01
- Bump to latest snapshot with LICENSE file
- Remove shebang from Python libraries

* Fri Mar 20 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.1-1.20200320git5800210
- Update to latest git snapshot (0.8beta)

* Fri Mar 20 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.1-1
- Initial package
