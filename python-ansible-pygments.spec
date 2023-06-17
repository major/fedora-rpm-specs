%global srcname ansible-pygments
%global pypiname ansible_pygments
%global pkgname python-%{srcname}

Name:    %{pkgname}
Version: 0.1.1
Release: 5%{?dist}
Summary: Provides Pygments highlighter for Ansible output for use in Sphinx
URL:       https://github.com/ansible-community/%{srcname}
Source:    %{url}/archive/%{version}/%{pypiname}-%{version}.tar.gz
License:   BSD
BuildArch: noarch

BuildRequires: python3-devel

%global _description %{expand:
This project provides a Pygments lexer that is able to handle Ansible output.
It may be used anywhere Pygments is integrated. The lexer is registered
globally under the name ansible-output.

It also provides a Pygments style for tools needing to highlight code snippets.
}

%description %{_description}

%package -n python3-%{srcname}
Summary: %summary

%py_provides python3-%{srcname}

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%{pyproject_wheel}

%install
%{pyproject_install}

%pyproject_save_files %{pypiname}

%check
%{tox}


%files -n python3-%{srcname} -f %{pyproject_files}
%doc     README.md
%license LICENSE.md


%changelog
* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.1.1-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.1.1-2
- Rebuilt for Python 3.11

* Mon Feb 07 2022 Karolina Surma <ksurma@redhat.com> - 0.1.1-1
- Update to 0.1.1
Resolves: rhbz#2042303

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Oct 03 2021 Chedi Toueiti <chedi.toueiti@gmail.com> - 0.1.0-1
- Initial commit version 0.1.0