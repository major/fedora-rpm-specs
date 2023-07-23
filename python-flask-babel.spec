%global pkg_name	flask-babel
%global mod_name	Flask-Babel
%bcond_without docs

%if 0%{?rhel}
%undefine with_docs
%endif

Name:		python-%{pkg_name}
Version:	2.0.0
Release:	8%{?dist}
Summary:	Adds i18n/l10n support to Flask applications
License:	BSD
URL:		http://github.com/mitsuhiko/%{pkg_name}/
Source0:	https://pypi.python.org/packages/source/F/%{mod_name}/%{mod_name}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	python%{python3_pkgversion}-babel
BuildRequires:	python%{python3_pkgversion}-devel
BuildRequires:	python%{python3_pkgversion}-flask
BuildRequires:	python%{python3_pkgversion}-jinja2
BuildRequires:	python%{python3_pkgversion}-setuptools
BuildRequires:	python%{python3_pkgversion}-pytz

# For tests
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock

# For documentation
%if %{with docs}
BuildRequires:  make
BuildRequires:  python3-docs
BuildRequires:  python3-sphinx
BuildRequires:  python3-Pallets-Sphinx-Themes
%endif

%global _description\
Adds i18n/l10n support to Flask applications with the help of the Babel library.

%description %_description

%package -n python%{python3_pkgversion}-%{pkg_name}
Summary:	Adds i18n/l10n support to Flask applications
# A modified version of speaklater is bundled
Provides:       bundled(python3-speaklater)

%description -n python%{python3_pkgversion}-%{pkg_name} %_description

%prep
%setup -q -n %{mod_name}-%{version}

# Use local objects.inv for intersphinx
# FIXME: the main flask package does not provide objects.inv (bz 1837646)
sed -e "s|\('http://docs\.python\.org/': \)None|\1'%{_docdir}/python3-docs/html/objects.inv'|" \
    -i docs/conf.py

# Update a call to a deprecated babel function
sed -i 's/\(numbers\.format_\)number/\1decimal/' flask_babel/__init__.py

%build
%py3_build

%if %{with docs}
# Build the documentation
make -C docs html

# We do not want the sphinx marker
rm -f docs/_build/html/.buildinfo
%endif

%install
%py3_install

%check
PYTHONPATH=$RPM_BUILD_ROOT/%{python3_sitelib}:%{python3_sitelib} pytest -v

%files -n python%{python3_pkgversion}-%{pkg_name}
%if %{with docs}
%doc docs/_build/html README.md
%else
%doc README.md
%endif
%license LICENSE
%{python3_sitelib}/*.egg-info/
%{python3_sitelib}/flask_babel

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 2.0.0-7
- Rebuilt for Python 3.12

* Thu Mar 02 2023 Jonathan Wright <jonathan@almalinux.org> - 2.0.0-6
- don't build docs on RHEL

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 2.0.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Aug 08 2021 Kevin Fenzi <kevin@scrye.com> - 2.0.0-1
- Update to 2.0.0. FIxes rhbz#1872942

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.0-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-2
- Rebuilt for Python 3.9

* Tue May 19 2020 Jerry James <loganjerry@gmail.com> - 1.0.0-1
- Version 1.0.0 (fixes bz 1830980)
- Add BRs on jinja2 and sphinx
- Drop BR and R on speaklater; a modified version is bundled
- Drop redundant Requires and Provides
- Ship documentation built with sphinx instead of sphinx source files
- Use the license macro

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11.2-7
- Subpackage python2-flask-babel has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11.2-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.11.2-2
- Rebuilt for Python 3.7

* Thu Mar 01 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.11.2-1
- new version 0.11.2

* Fri Feb 16 2018 Lumír Balhar <lbalhar@redhat.com> - 0.9-14
- Fixed source URL
- Fixed directory ownership

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.9-12
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.9-11
- Python 2 binary package renamed to python2-flask-babel
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9-8
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 29 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.9-6
- Rebuild to properly provide python-flask-babel

* Tue Jun 28 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.9-5
- Add python3 subpackage

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Dec 17 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.9-2
- Revert patch to pass check with older Babel (#1175391).

* Fri Jul 18 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.9-1
- Update to latest upstream release (#1106770).

* Thu Jul 17 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.8-6
- Add patch to work with latest Babel (#1106770).

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Sep 13 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.8-4
- Add missing python-setuptools build requires (#839071)
- Remove wrongly installed .gitignore

* Fri Aug 17 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.8-3
- Add missing build requires for proper chroot build
- Correct spec file to make %%check work without having package installed

* Sun Aug 5 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.8-2
- No need to set CFLAGS for noarch (#839071)
- Add %%check section (#839071)

* Tue Jul 10 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.8-1
- Initial python-flask-babel spec.
