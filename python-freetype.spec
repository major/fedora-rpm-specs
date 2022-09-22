%global module_name                  freetype
%global srcname                      freetype-py
%global pythonicname                 freetype_py
%global sum                          Freetype python bindings
%global __pypi_default_extension     zip

Name:          python-%{module_name}
Version:       2.2.0
Release:       11%{?dist}
Summary:       Freetype python bindings

License:       BSD
# Move to a different URL planned:
# https://github.com/rougier/freetype-py/issues/111
URL:           https://github.com/rougier/freetype-py
Source0:       %pypi_source

BuildArch:     noarch
BuildRequires: freetype

%description
%{sum}.

%package -n python3-%{module_name}
Summary:        %{sum}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
# tests use tox
BuildRequires:  python3dist(tox-current-env)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(wheel)
BuildRequires:  pyproject-rpm-macros
%py_provides python3-%{module_name}

%description -n python3-%{module_name}
%{sum}.

%prep
%autosetup -n %{srcname}-%{version}

# remove sheebangs from regular Python files
sed -i '1{\@^#!/usr/bin/env python@d}' freetype/*.py
sed -i '1{\@^#!/usr/bin/env python@d}' examples/*.py

# remove egg files from source
rm -r %{pythonicname}.egg-info

%build
%py3_build

%install
%py3_install

%check
%tox

%files -n python3-%{module_name}
%doc examples README.rst
%license LICENSE.txt
%{python3_sitelib}/%{module_name}/
%{python3_sitelib}/%{pythonicname}-%{version}-py3.*.egg-info/


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.2.0-10
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.2.0-7
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 25 2020 Andy Mender <andymenderunix@fedoraproject.org> - 2.2.0-5
- Remove patch (fixed upstream and not needed in Fedora 33+)

* Tue Nov 24 2020 Andy Mender <andymenderunix@fedoraproject.org> - 2.2.0-4
- Remove explicit call to python dependency generator (on by default)
- Switch Source0 to PyPi
- Add patch for setuptools_scm with toml
- Use %%py_provides macro
- Correctly enable tests via tox
- Clean up SPEC file

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Parag Nemade <pnemade AT redhat DOT com> - 2.2.0-1
- Update to 2.2.0 version (#1855370)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 17 2018 Parag Nemade <pnemade AT redhat DOT com> - 2.0-2
- dropped python2 subpackage

* Tue Jul 03 2018 Parag Nemade <pnemade AT redhat DOT com> - 2.0-1
- Update to 2.0 version (#1595976)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-3
- Rebuilt for Python 3.7

* Mon Mar 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.1-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Tue Feb 27 2018 Parag Nemade <pnemade AT redhat DOT com> - 1.2.1-1
- Update to 1.2.1 version (#1545641)
- Upstream keeps mistaking for generating egg-info, I have to adjust here

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 01 2017 Parag Nemade <pnemade AT redhat DOT com> - 1.1-1
- Update to 1.1 version

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-2
- Rebuild for Python 3.6

* Sat Sep 03 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.0.2-1
- Update to 1.0.2

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Feb 12 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.0.1-1
- update to 1.0.1

* Wed Nov 05 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.5.1-1
- update to 0.5.1
- Don't use Pypi as source URL as it contains wrong 1.0 tarball
- remove the removal of line 15 from setup.py as no data_files now

* Sun Nov 02 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.4.2-3
- enable python3 subpackage

* Fri Oct 24 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.4.2-2
- License is BSD not MIT

* Mon Sep 22 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.4.2-1
- Initial packaging

