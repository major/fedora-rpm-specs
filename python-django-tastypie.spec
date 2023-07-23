%global pypi_name django-tastypie
%global sum A flexible and capable API layer for Django
Name:           python-%{pypi_name}
Version:        0.13.3
Release:        27%{?dist}
Summary:        %{sum}

License:        BSD
URL:            https://github.com/toastdriven/django-tastypie/

# Release version doesn't include tests
Source0:        https://github.com/%{pypi_name}/%{pypi_name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
# Let's keep Requires and BuildRequires sorted alphabetically
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx

%description
Tastypie is an webservice API framework for Django. It provides a convenient, 
yet powerful and highly customizable, abstraction for creating REST-style 
interfaces.

%package doc
Summary: Documentation for %{name}

Requires: python3-%{pypi_name} = %{version}-%{release}

%description doc
This package contains documentation for %{name}.

%package -n python3-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-dateutil
Requires:       python3-django
Requires:       python3-mimeparse

Obsoletes:      %{pypi_name} < 0.9.11-3
Obsoletes:      python-%{pypi_name} <= 0.13.3-8
Obsoletes:      python2-%{pypi_name} <= 0.13.3-8

%description -n python3-%{pypi_name}
Tastypie is an webservice API framework for Django. It provides a convenient, 
yet powerful and highly customizable, abstraction for creating REST-style 
interfaces.

%prep 
%setup -q -n %{pypi_name}-%{version}


%build
# (re)generate the documentation
#pushd docs
sphinx-build-3 docs docs/_build/html
#make html
#popd
rm -rf docs/_build/html/.??*

%py3_build


%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst AUTHORS LICENSE
%dir %{python3_sitelib}/tastypie
%{python3_sitelib}/django_tastypie*
%{python3_sitelib}/tastypie/*

%files doc
%doc docs/_build/html

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.13.3-26
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.13.3-23
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.13.3-20
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.13.3-17
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.13.3-15
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.13.3-14
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.13.3-10
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 05 2017 Miro Hrončok <mhroncok@redhat.com>
- Remove Python 2 subpackage (#1494761)
- Remove Groups
- Use Python 3 for documentation
- Move docs build into %%build
- Use modern Python build+install macros
- Remove RHEL conditionals

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.13.3-5
- Rebuild for Python 3.6

* Sun Jul 31 2016 Petr Viktorin <pviktori@redhat.com> - 0.13.3-4
- Fix Python sitelib directories

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.3-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat Feb 27 2016 Cédric OLIVIER <cedric.olivier@free.fr> - 0.13.3-2
- provide python3 subpackage (rhbz#1312325)

* Thu Feb 18 2016 Cédric OLIVIER <cedric.olivier@free.fr> - 0.13.3-1
- Update to 0.13.3 (rhbz#1308500)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Cédric OLIVIER <cedric.olivier@free.fr> - 0.13.1-1
- Update to 0.13.1 (rhbz#1244039)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Oct 27 2014 Cédric OLIVIER <cedric.olivier@free.fr> - 0.12.1-1
- Update to 0.12.1 (rhbz#1142992)

* Thu Aug 07 2014 Matthias Runge <mrunge@redhat.com> - 0.11.1-4
- Fix python-dateutil requires

* Wed Aug 06 2014 Jon Ciesla <limburgher@gmail.com> - 0.11.1-3
- Fix python-dateutil Requires.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Matthias Runge <mrunge@redhat.com> - 0.11.1-1
- update to 0.11.1 (rhbz#1100733)

* Mon May 19 2014 Matthias Runge <mrunge@redhat.com> - 0.11.0-1
- update to 0.11.0 (rhbz#959137)
- remove check section :-(, upstream does not provide tests in tarballs

* Tue Aug 27 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.9.14-4
- Fix unversioned docdir issue (rhbz#1001252).
- Fix bogus changelog entry.

* Sun Aug 11 2013 Cédric OLIVIER <cedric.olivier@free.fr> 0.9.14-3
- Change Docdir to Unversioned Docdir

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 26 2013 Miro Hrončok <mhroncok@redhat.com> - 0.9.14-1
- New version
- Using new GitHub rule to get archive with tests
- Run tests manually
- Added BR python-defusedxml
- Dropped dance around release and development versioning
- Added patch for Django 1.5

* Mon Mar 25 2013 Cédric OLIVIER <cedric.olivier@free.fr> 0.9.12-1
- Updated to upstream 0.9.12

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.12-0.2.alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 14 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.9.12-0.1.alpha
- Updated to upstream version 0.9.12-alpha.
- Adapted the specfile to prerelease versioning.
- Add some BuildRequires, so that more tests are run (these
are soft requirements, so they aren't in Requires)
- Fixed URL to point to upstream, not PyPI.
- Made the spec compatible with EPEL6.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar 18 2012 Cédric OLIVIER <cedric.olivier@free.fr> 0.9.11-4
- Bugfix in obsoletes

* Sun Mar 18 2012 Cédric OLIVIER <cedric.olivier@free.fr> 0.9.11-3
- Removing bundled .egg-info during prep

* Sat Mar 17 2012 Cédric OLIVIER <cedric.olivier@free.fr> 0.9.11-2
- Adding missing buildrequires
- Adding info about renaming django-tastypie
- Adding check section
- Adding documentation subpackage

* Fri Mar 02 2012 Cédric OLIVIER <cedric.olivier@free.fr> 0.9.11-1
- Initial version of the package
