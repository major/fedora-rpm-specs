%global pypi_name django-robots
%global obs_ver 0.8.0-3

Name:           python-%{pypi_name}
Version:        3.1.0
Release:        19%{?dist}
Summary:        Robots exclusion application for Django, complementing Sitemaps

License:        BSD
URL:            https://github.com/jazzband/django-robots
Source0:        https://github.com/jazzband/%{pypi_name}/archive/%{version}.tar.gz#/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  gettext

%description
Django application to manage robots.txt files following the robots exclusion 
protocol, complementing the Django Sitemap contrib app.

%package -n python3-%{pypi_name}
Summary:        Robots exclusion application for Django - Python 3 version

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-django

%{?python_provide:%python_provide python3-%{pypi_name}}
Obsoletes:      python-%{pypi_name} < 2.0-5
Obsoletes:      python2-%{pypi_name} < 2.0-5

%description -n python3-%{pypi_name}
Django application to manage robots.txt files following the robots exclusion
protocol, complementing the Django Sitemap contrib app.
This package provides Python 3 build of %{pypi_name}.

%prep
%autosetup -n %{pypi_name}-%{version}


%build
%py3_build

%install
%py3_install
rm -rf %{buildroot}%{python3_sitelib}/tests


# Language files; not under /usr/share, need to be handled manually
(cd %{buildroot} && find .%{python3_sitelib} -name 'django.?o') | sed -e 's|^.||' | sed -e \
  's:\(.*/locale/\)\([^/_]\+\)\(.*\.mo$\):%lang(\2) \1\2\3:' \
  >> python3-%{pypi_name}.lang

%files -f python3-%{pypi_name}.lang -n python3-%{pypi_name}
%doc README.rst docs/
%license LICENSE.txt
# list some files explicitly to avoid listing locale files twice
%dir %{python3_sitelib}/robots
%{python3_sitelib}/robots/*.py
%{python3_sitelib}/robots/__pycache__
%{python3_sitelib}/robots/migrations
%{python3_sitelib}/robots/south_migrations
%dir %{python3_sitelib}/robots/templates/
%dir %{python3_sitelib}/robots/templates/robots
%{python3_sitelib}/robots/templates/robots/rule_list.html
%{python3_sitelib}/django_robots*.egg-info

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.1.0-18
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.1.0-15
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.1.0-12
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-2
- Rebuilt for Python 3.7

* Thu Feb 15 2018 Matthias Runge <mrunge@redhat.com> - 3.1.0-1
- rebase to 3.1.0
- drop python2 subpackage for https://fedoraproject.org/wiki/Changes/Django20
* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0-2
- Rebuild for Python 3.6

* Thu Jul 21 2016 Matthias Runge <mrunge@redhat.com> - 2.0-1
- porting the specfile to Python 3, thanks to Jan Beran <jberan@redhat.com>
- major spec file cleanup

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-9
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 23 2012 Matthias Runge <mrunge@matthias-runge.de> - 0.8.1-2
- renamed to python-django-robots
- SPEC cleanup

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Apr 14 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 0.8.0-1
- initial spec
