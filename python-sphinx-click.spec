%global pypi_name sphinx-click

Name:           python-%{pypi_name}
Version:        4.3.0
Release:        2%{?dist}
Summary:        Sphinx extension that automatically documents Click applications

License:        MIT
URL:            https://github.com/click-contrib/sphinx-click
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
# pytest is not an upstream dependency, we use it here out of convenience
BuildRequires:  python3dist(pytest)
BuildRequires:  pyproject-rpm-macros

%global package_desc \
sphinx-click is a Sphinx plugin that allows you to automatically extract\
documentation from a click-based application and include it in your docs.

%description
%{package_desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

# The doc subpackage was removed, obsolete it to have clean upgrade path
# This was added in Fedora 35 and can be removed in Fedora 37
Obsoletes:      python-%{pypi_name}-doc < 2.7.1-1

%description -n python3-%{pypi_name}
%{package_desc}

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sphinx_click

%check
%pytest -v tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst ChangeLog

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 27 2022 Charalampos Stratakis <cstratak@redhat.com> - 4.3.0-1
- Update to 4.3.0
Resolves: rhbz#2074604

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.0.0-2
- Rebuilt for Python 3.11

* Wed Apr 06 2022 Charalampos Stratakis <cstratak@redhat.com> - 4.0.0-1
- Update to 4.0.0
Resolves: rhbz#2049614

* Mon Jan 31 2022 Karolina Surma <ksurma@redhat.com> - 3.0.3-1
- Update to 3.0.3
Resolves rhbz#2020252

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.0.0-2
- Rebuilt for Python 3.10

* Wed Jun 02 2021 Karolina Surma <ksurma@redhat.com> - 3.0.0-1
- Update to 3.0.0
Resolves rhbz#1960706

* Wed Apr 14 2021 Karolina Surma <ksurma@redhat.com> - 2.7.1-1
- Update to 2.7.1
Resolves rhbz#1940703
- Remove -doc subpackage

* Wed Feb 24 2021 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-3
- Explicitly add used requires, don't require pbr on runtime
- Fixes: rhbz#1931673

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Tomas Hrnciar <thrnciar@redhat.com> - 2.5.0-1
- Update to 2.5.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.3.2-2
- Rebuilt for Python 3.9

* Wed Apr 15 2020 Charalampos Stratakis <cstratak@redhat.com> - 2.3.2-1
- Update to 2.3.2 (#1822901)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 10 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.1-1
- Update to 2.3.1 (#1754192)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 24 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-1
- Update to 2.2.0 for Sphinx 2.1 official support (#1704910)

* Wed Mar 13 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-2
- sphinx-click 2.0.1 works with sphinx 2.0.0b1

* Sun Feb 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-1
- Update to 2.0.1 to make it build with Click 7

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-2
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Michal Cyprian <mcyprian@redhat.com> - 1.0.4-1
- Initial package.
