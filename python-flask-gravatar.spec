%global pkg_name flask-gravatar

Name:           python-%{pkg_name}
Version:        0.5.0
Release:        18%{?dist}
Summary:        Small extension for Flask to make usage of Gravatar service easy

License:        BSD
URL:            https://github.com/zzzsochi/Flask-Gravatar/
BuildArch:      noarch
Source0:        %{pypi_source Flask-Gravatar}
# Don't test pep8 as python-pytest-pep8 is obsolete
# Don't run linting tests
# Don't add flask_gravatar src folder to test path, buildroot path is already added by %%pytest
Patch0:         python-flask-gravatar_tests.patch

BuildRequires:  python3-devel


%description
Small extension for Flask to make usage of Gravatar service easy.

%package -n python3-%{pkg_name}
Summary: Small extension for Flask to make usage of Gravatar service easy


%description -n python3-%{pkg_name}
Small extension for Flask to make usage of Gravatar service easy.


%prep
%autosetup -p1 -n Flask-Gravatar-%{version}


%generate_buildrequires
%pyproject_buildrequires -r -x tests


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files flask_gravatar

%check
%pytest


%files -n python-%{pkg_name} -f %{pyproject_files}
%doc README.rst CHANGES.rst RELEASE-NOTES.rst AUTHORS
%license LICENSE


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.5.0-16
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 24 2021 Sandro Mani <manisandro@gmail.com> - 0.5.0-14
- Run %%pytest

* Wed Dec 08 2021 Sandro Mani <manisandro@gmail.com> - 0.5.0-13
- Revive package

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-4
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-2
- Rebuilt for Python 3.7

* Thu Mar 01 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.5.0-1
- new version 0.5.0

* Thu Mar 01 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.4.2-2
- improve spec file

* Tue Jan  3 2017 Jakub Dorňák <jakub.dornak@misli.cz> - 0.4.2-1
- Initial package
