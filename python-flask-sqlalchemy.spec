%global srcname Flask-SQLAlchemy

Name:           python-flask-sqlalchemy
Version:        2.5.1
Release:        8%{?dist}
Summary:        Adds SQLAlchemy support to Flask application

License:        BSD
URL:            https://github.com/pallets/flask-sqlalchemy
Source0:        %{pypi_source}

BuildArch:      noarch

%description
Flask-SQLAlchemy is an extension for Flask that adds support for
SQLAlchemy to your application. It aims to simplify using SQLAlchemy with
Flask by providing useful defaults and extra helpers that make it easier
to accomplish common tasks.

%package -n python3-flask-sqlalchemy
Summary:        Adds SQLAlchemy support to Flask application

%py_provides python3-%{srcname}
%py_provides python3-flask-sqlalchemy

BuildRequires:  python3-devel
BuildRequires:  python3-mock
BuildRequires:  python3-setuptools
BuildRequires:  python3-flask
BuildRequires:  python3-pytest
BuildRequires:  python3-sqlalchemy

%description -n python3-flask-sqlalchemy
Flask-SQLAlchemy is an extension for Flask that adds support for
SQLAlchemy to your application. It aims to simplify using SQLAlchemy with
Flask by providing useful defaults and extra helpers that make it easier
to accomplish common tasks.

Python 3 version.

%prep
%setup -q -n %{srcname}-%{version}
rm -f docs/_static/.DS_Store
rm -f docs/.DS_Store
rm -f docs/_themes/.gitignore

%build
%py3_build

%install
%py3_install

%check
# We expect 2 warnings in one test due to Flask >= 2.2.0
# Upstream report: https://github.com/pallets-eco/flask-sqlalchemy/issues/1068
%pytest --deselect tests/test_basic_app.py::test_persist_selectable

%files -n python3-flask-sqlalchemy
%license LICENSE.rst
%doc docs/ README.rst CHANGES.rst PKG-INFO
%{python3_sitelib}/Flask_SQLAlchemy-*.egg-info/
%{python3_sitelib}/flask_sqlalchemy/

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 03 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 2.5.1-7
- Add workaround for Flask 2.2 support

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 2.5.1-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.5.1-2
- Rebuilt for Python 3.10

* Mon May 24 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 2.5.1-1
- Update to flask-sqlalchemy 2.5.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 2.4.4-1
- Update to flask-sqlalchemy 2.4.4

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 18 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-4
- Subpackage python2-flask-sqlalchemy has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 2019 Pavel Raiskup <praiskup@redhat.com> - 2.4.0-1
- latest upstream release

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.3.2-2
- Rebuilt for Python 3.7

* Mon Mar 05 2018 Ralph Bean <rbean@redhat.com> - 2.3.2-1
- Latest upstream.

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.1-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.1-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 29 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.1-1
- Update to 2.1
- Follow new packaging guidelines
- Run tests

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Dec 10 2014 Tim Flink <tflink@fedoraproject.org> - 2.0-1
- enable python3 builds only for fedora - there's no python3 in el*

* Wed Dec 10 2014 Tim Flink <tflink@fedoraproject.org> - 2.0-1
- Upgraded to upstream 2.0
- Enhanced internal signal control, made more customizable and less global to play nice with non-flask-sqlalchemy sessions

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Jan 21 2014 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 1.0-2
- Fixed #1055251

* Wed Aug 07 2013 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 1.0-1
- Upgraded to upstream 1.0 and added python3 support

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 09 2012 Tim Flink <tflink@fedoraproject.ort> - 0.16-1
- Upgraded to upstream 0.16

* Tue Aug 21 2012 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.14-4
- Added python-sqlalchemy as requires

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.14-1
- Initial RPM release
