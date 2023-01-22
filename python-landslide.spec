%global srcname landslide

Name:		python-%{srcname}
Version:	1.1.8
Release:	9%{?dist}
Summary:	Lightweight markup language-based html5 slideshow generator

License:	ASL 2.0
URL:		https://pypi.python.org/pypi/%{srcname}
Source0:	%{pypi_source}
Patch0:         %{srcname}-1.1.8-make_unversioned.diff

BuildArch:	noarch


%description
Takes your Markdown, ReST, or Textile file(s) and generates 
fancy HTML5 slideshows.

%package -n python3-%{srcname}
Summary:	%{summary}

BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-sphinx
# Test dependencies:
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(markdown)
BuildRequires:  python3dist(pytest)

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Takes your Markdown, ReST, or Textile file(s) and generates 
fancy HTML5 slideshows.


%prep
%autosetup -p1 -n %{srcname}-%{version}
# Change shebang to recognized the default interpreter installed 
# from system-wide
sed -i '1s=^#!/usr/bin/\(python\|env python\)[23]\?=#!%{__python3}=' \
  landslide/main.py
# Remove bundled egg-info
rm -rf landslide.egg-info


%build
%py3_build


%install
%py3_install
find %{buildroot} -name 'main.py' | xargs chmod 0755


%check
%pytest tests.py


%files -n python3-%{srcname}
%doc CHANGELOG.md README.md examples
%license LICENSE
%{_bindir}/landslide
%{python3_sitelib}/landslide
%{python3_sitelib}/landslide-*.egg-info


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1.8-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug  4 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.1.8-5
- Enable tests

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.8-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 25 2020 Michel Alexandre Salim <salimma@fedoraproject.org. - 1.1.8-1
- Update to 1.1.8

* Thu Aug  6 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.1.6-1
- Update to 1.1.6
- Patch in support for Markdown 3.x compatibility

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-16
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-14
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-13
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 27 2017 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.3-6
- Fix shebang to avoid depending on both Python 2 and Python 3
- Package python3- subpackage

* Wed Feb 22 2017 Jan Beran <jberan@redhat.com> - 1.1.3-5
- Provides Python 3 package

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 1 2015 Eduardo Echeverria  <echevemaster@gmail.com> - 1.1.3-1
- Initial packaging

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 07 2013 Eduardo Echeverria  <echevemaster@gmail.com> - 1.1.1-2
- Change shebang to recognize the installed default interpreter.
- Remove MANIFEST.in from documentation

* Sun Jul 07 2013 Eduardo Echeverria  <echevemaster@gmail.com> - 1.1.1-1
- Initial packaging

