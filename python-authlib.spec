%global srcname authlib
%global pypi_name Authlib

Name:           python-%{srcname}
Version:        1.1.0
Release:        1%{?dist}
Summary:        Build OAuth and OpenID Connect servers in Python

License:        BSD
URL:            https://github.com/lepture/authlib
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Python library for building OAuth and OpenID Connect servers. JWS, JWK, JWA,
JWT are included.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -e %{toxenv},%{toxenv}-clients,%{toxenv}-flask,%{toxenv}-django,%{toxenv}-jose


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files authlib


%check
%tox


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md


%changelog
* Fri Nov 04 2022 Kai A. Hiller <V02460@gmail.com> - 1.1.0-1
- Update to v1.1.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.0.1-3
- Rebuilt for Python 3.11

* Thu Apr 21 2022 Kai A. Hiller <V02460@gmail.com> - 1.0.1-2
- Follow new Python packaging guidelines

* Tue Apr 12 2022 dkirwan <dkirwan@redhat.com> - 1.0.1-1
- Update to v1.0.1

* Thu Jan 27 2022 Kai A. Hiller <V02460@gmail.com> - 0.15.5-1
- Update to v1.15.5

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 29 2021 Kai A. Hiller <V02460@gmail.com> - 0.15.4-1
- Update to v1.15.4
- Make compatible with werkzeug 2

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 03 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.15.3-5
- Fix buidlroot↔buildroot typo

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.15.3-4
- Rebuilt for Python 3.10

* Mon Mar 29 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.15.3-3
- Enable “py3” tests since all of the dependencies are present

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 2021 Kai A. Hiller <V02460@gmail.com> - 0.15.3-1
- Update to v1.15.3

* Fri Dec 11 2020 Kai A. Hiller <V02460@gmail.com> - 0.15.2-1
- Update to v1.15.2

* Sun Oct 11 2020 Kai A. Hiller <V02460@gmail.com> - 0.15.0-1
- Update to v1.15.0

* Fri May 29 2020 Kai A. Hiller <V02460@gmail.com> - 0.14.3-1
- Initial package.
