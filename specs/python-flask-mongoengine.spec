%global srcname flask-mongoengine

Name:           python-flask-mongoengine
Version:        1.0.0
Release:        9%{?dist}
Summary:        Flask extension that provides integration with MongoEngine

License:        BSD-3-Clause
URL:            https://flask-mongoengine.readthedocs.org/
Source0:        %{pypi_source}

# Flask >= 2.3 Support
# https://github.com/MongoEngine/flask-mongoengine/pull/507
# Parts are removed (tests aren't part of the tarball used here)
# And modified to apply cleanly
Patch01:        d283967f012463833c683746f86df1a2212a0eed.patch

BuildArch:      noarch


%description
A Flask extension that provides integration with MongoEngine. It handles
connection management for your app. You can also use WTForms as model forms
for your models.


%package -n python3-flask-mongoengine
Summary:        Flask extension that provides integration with MongoEngine
BuildRequires:  python3-devel

%description -n python3-flask-mongoengine
A Flask extension that provides integration with MongoEngine. It handles
connection management for your app. You can also use WTForms as model forms
for your models.

Python 3 version.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files flask_mongoengine


%check
# No real tests except coverage tests
%py3_check_import flask_mongoengine


%files -n python3-flask-mongoengine -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 1.0.0-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.0.0-4
- Backport Flask >= 2.3 fix

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 1.0.0-2
- Rebuilt for Python 3.12

* Wed Feb 08 2023 Sandro Mani <manisandro@gmail.com> - 1.0.0-1
- Update to 1.0.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Aug 27 2014 Matej Stuchlik <mstuchli@redhat.com> - 0.7.1-1
- Update to 0.7.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 13 2013 Matej Stuchlik <mstuchli@redhat.com> - 0.7-1
- Updated to 0.7

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 04 2013 Matej Stuchlik <mstuchli@redhat.com> - 0.6-2
- Added patch that removes unused dependencies and changed the URL field

* Wed Apr 3 2013 mstuchli <mstuchli@redhat.com> - 0.6-1
- Initial spec
