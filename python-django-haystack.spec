%global pypi_name django-haystack

%global betaver b2
%global dotbetaver %{?betaver:.%{betaver}}

Name:           python-%{pypi_name}
Version:        3.0
Release:        %{?betaver:0.}1%{dotbetaver}%{?dist}.8
Summary:        Pluggable search for Django

License:        BSD
URL:            http://haystacksearch.org/
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}%{?betaver}.tar.gz

BuildArch:      noarch

%description
Haystack provides modular search for Django. It features a unified, familiar
API that allows you to plug in different search backends (such as Solr,
Elasticsearch, Whoosh, Xapian, etc.) without having to modify your code.

Haystack is BSD licensed, plays nicely with third-party app without needing to
modify the source and supports advanced features like faceting, More Like This,
highlighting, spatial search and spelling suggestions.

You can find more information at http://haystacksearch.org/.

%package -n python3-%{pypi_name}
Summary:        Haystack provides modular search for Django - Python 3 version

BuildRequires: make
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-django

Requires:       python3-django

%{?python_provide:%python_provide python3-%{pypi_name}}

Obsoletes: python-%{pypi_name} < 2.5.0-5
Obsoletes: python2-%{pypi_name} < 2.5.0-5

%description -n python3-%{pypi_name}
Haystack provides modular search for Django. It features a unified, familiar
API that allows you to plug in different search backends (such as Solr,
Elasticsearch, Whoosh, Xapian, etc.) without having to modify your code.

Haystack is BSD licensed, plays nicely with third-party app without needing to
modify the source and supports advanced features like faceting, More Like This,
highlighting, spatial search and spelling suggestions.

You can find more information at http://haystacksearch.org/.

This package provides Python 3 build of %{pypi_name}.


%package docs
Summary: Documentation for Django Haystack pluggable search
# Not requiring the main package, as users may wish to install
# the documentation separately.

%description docs
Documentation for Django Haystack pluggable search

Haystack provides modular search for Django. It features a unified, familiar
API that allows you to plug in different search backends (such as Solr,
Elasticsearch, Whoosh, Xapian, etc.) without having to modify your code.

Haystack is BSD licensed, plays nicely with third-party app without needing to
modify the source and supports advanced features like faceting, More Like This,
highlighting, spatial search and spelling suggestions.

You can find more information at http://haystacksearch.org/.


%prep
%autosetup -n %{pypi_name}-%{version}%{?betaver}

%build
%py3_build

# Re-generate documentation
# Docs cannot be built in parallel
# We cannot build 'linkcheck' because it requires network access

pushd docs
make clean html htmlhelp latex json pickle changes
popd

%install
%py3_install
# Remove several useless files from the sources
find . -name ".gitignore" -exec rm -f {} \;
find . -name ".buildinfo" -exec rm -f {} \;
find . -name ".DS_Store" -exec rm -f {} \;
find . -name "last_build" -exec rm -f {} \;

%files -n python3-%{pypi_name}
%doc PKG-INFO README.rst AUTHORS
%license LICENSE
# For noarch packages: sitelib
%{python3_sitelib}/haystack
%{python3_sitelib}/django_haystack-%{version}*.egg-info/

%files docs
%doc docs/

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.1.b2.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 3.0-0.1.b2.7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.1.b2.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.1.b2.5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.0-0.1.b2.4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.1.b2.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.1.b2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0-0.1.b2.1
- Rebuilt for Python 3.9

* Mon May 04 2020 Nils Philippsen <nils@redhat.com> - 3.0-0.1.b2
- Update to version 3.0b2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-6
- Rebuilt for Python 3.7

* Tue Feb 13 2018 Matthias Runge <mrunge@redhat.com> - 2.5.0-5
- fix FTBFS
- drop python2 package for https://fedoraproject.org/wiki/Changes/Django20

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-2
- Rebuild for Python 3.6

* Wed Aug 3 2016 Jan Beran <jberan@redhat.com> - 2.5.0-1
- update to version 2.5.0
- source update
- modernized specfile with Python 3 packaging

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Stephen Gallagher <sgallagh@redhat.com> 2.3.1-1
- Update to 2.3.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 27 2014 Stephen Gallagher <sgallagh@redhat.com> 2.1.0-4
- Build -docs subpackage
- Remove hidden files and cruft from other OSes
- Force rebuild of documentation

* Fri Jan 24 2014 Stephen Gallagher <sgallagh@redhat.com> 2.1.0-3
- Remove extra BuildRequires: python-django

* Thu Jan 23 2014 Stephen Gallagher <sgallagh@redhat.com> - 2.1.0-2
- Correct %%description

* Thu Jan 23 2014 Stephen Gallagher <sgallagh@redhat.com> - 2.1.0-1
- Initial release

