%global srcname pipdeptree

%global _description\
pipdeptree is a command line utility for displaying the installed python\
packages in form of a dependency tree. It works for packages installed\
globally on a machine as well as in a virtualenv.

Name:           python-%{srcname}
Version:        2.3.1
Release:        1%{?dist}
Summary:        Command line utility to show dependency tree of packages

License:        MIT
URL:            https://github.com/naiquevin/pipdeptree
Source0:        https://github.com/naiquevin/pipdeptree/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros >= 0-41

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%pyproject_extras_subpkg -n python3-%{srcname} graphviz

%prep
%autosetup -n %{srcname}-%{version}
# Remove unneeded testing deps
sed -i "/diff-cover/d;/covdefaults/d;/pytest-cov/d" pyproject.toml
# Remove version limits from virtualenv and graphviz
sed -i 's/"virtualenv.*",/"virtualenv",/' pyproject.toml
sed -i 's/"graphviz.*",/"graphviz",/' pyproject.toml

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"
%pyproject_buildrequires -w -x test,graphviz

%build
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pytest

%files -n python3-%{srcname} -f %pyproject_files
%license LICENSE
%doc README.md
%{_bindir}/pipdeptree

%changelog
* Wed Sep 07 2022 Lumír Balhar <lbalhar@redhat.com> - 2.3.1-1
- Update to 2.3.1
Resolves: rhbz#2124639

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.2.1-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 Lumír Balhar <lbalhar@redhat.com> - 2.2.1-1
- Update to 2.2.1
Resolves: rhbz#2038738

* Thu Oct 14 2021 Lumír Balhar <lbalhar@redhat.com> - 2.2.0-1
- Update to 2.2.0
Resolves: rhbz#2013547

* Mon Aug 02 2021 Lumír Balhar <lbalhar@redhat.com> - 2.1.0-1
- Update to 2.1.0
Resolves: rhbz#1988703

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 04 2021 Lumír Balhar <lbalhar@redhat.com> - 2.0.0-1
- Update to 2.0.0 (#1910899)

* Tue Sep 08 2020 Lumír Balhar <lbalhar@redhat.com> - 1.0.0-1
- Update to 1.0.0 (#1846897)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.13.2-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.13.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.13.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 21 2019 Dhanesh B. Sabane <dhanesh95@fedoraproject.org> - 0.13.2-1
- Fix Bug #1697089 - Bump version to 0.13.2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 13 2019 Dhanesh B. Sabane <dhanesh95@fedoraproject.org> - 0.13.1-2
- Bump version to 0.13.1 and ignore tests

* Sat Jun 30 2018 Dhanesh B. Sabane <dhanesh95@disroot.org> - 0.12.1-1
- Initial package.
