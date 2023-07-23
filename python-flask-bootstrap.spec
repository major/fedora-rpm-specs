%global pypi_name Flask-Bootstrap
%global _description\
FlaskBootstrap packages Bootstrap into an extension that\
mostly consists of a blueprint named 'bootstrap'. It can also create links to\
serve Bootstrap from a CDN and works with no boilerplate code in your\
application

Name:           python-flask-bootstrap
Version:        3.3.7.1
Release:        22%{?dist}
Summary:        Include Bootstrap in your project without boilerplate code

License:        BSD
URL:            https://github.com/mbr/flask-bootstrap
Source0:        https://files.pythonhosted.org/packages/source/F/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# https://github.com/mbr/flask-bootstrap/issues/169
Source1:        https://raw.githubusercontent.com/mbr/flask-bootstrap/master/LICENSE

BuildArch:      noarch

BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

Provides:       bundled(bootstrap)
Provides:       bundled(jquery)

%description    %_description

%package -n     python3-flask-bootstrap
Summary:        %{summary}
%{?python_provide:%python_provide python3-flask-bootstrap}

Requires:       python3-flask >= 0.8
Requires:       python3-dominate
Requires:       python3-visitor
%description -n python3-flask-bootstrap %_description

%prep
%autosetup -n %{pypi_name}-%{version}
cp %{SOURCE1} .

%build
%py3_build

%install
%py3_install

%files -n python3-flask-bootstrap
%doc README.rst
%license LICENSE
%{python3_sitelib}/flask_bootstrap
%{python3_sitelib}/Flask_Bootstrap-%{version}-py*egg-info

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.3.7.1-21
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.3.7.1-18
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.3.7.1-15
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.3.7.1-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.7.1-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.7.1-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.3.7.1-6
- Subpackage python2-flask-bootstrap has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.3.7.1-4
- Rebuilt for Python 3.7

* Thu Apr 26 2018 David Hannequin david.hannequin@gmail.com - 3.3.7.1-3
- Add license.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 08 2017 David Hannequin david.hannequin@gmail.com - 3.3.7.1-1
- Initial package.
