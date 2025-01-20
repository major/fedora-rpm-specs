%global with_docs 1
%global with_check 1
%global with_django 1

%global srcname whitenoise
%global owner evansd

%if 0%{?rhel} == 9
%undefine with_check
%undefine with_django
%endif

Name:           python-%{srcname}
Version:        6.4.0
Release:        7%{?dist}
Summary:        Static file serving for Python web apps

License:        MIT
URL:            http://whitenoise.evans.io/
# pypi source does not contain tests
Source0:        https://github.com/evansd/whitenoise/archive/refs/tags/%{version}.tar.gz
Patch:          whitenoise-6.4.0-default-docs-theme.patch

BuildArch:      noarch

%description
Radically simplified static file serving for python web apps. with a couple of
lines of config whitenoise allows your web app to serve its own static files,
making it a self-contained unit that can be deployed anywhere without relying
on nginx, amazon s3 or any other external service. (Especially useful on
Heroku, OpenShift and other PaaS providers.)


%package -n python3-%{srcname}
Summary:        Static file serving for Python web apps
License:        MIT

BuildRequires:  python3-devel
BuildRequires:  python3-brotli
%if 0%{?with_django}
BuildRequires:  python3-django
%endif

#for tests
BuildRequires:  python3-pytest

%description -n python3-%{srcname}
Radically simplified static file serving for python web apps. with a couple of
lines of config whitenoise allows your web app to serve its own static files,
making it a self-contained unit that can be deployed anywhere without relying
on nginx, amazon s3 or any other external service. (especially useful on
heroku, openshift and other paas providers.)


%if 0%{?with_docs}
%package -n python3-%{srcname}-doc
Summary:        Documentation for the Python Whitenoise module
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

%description -n python3-%{srcname}-doc
Documentation for the Python Whitenoise module
%endif


%prep
%autosetup -n %{srcname}-%{version} -p1
# remove dangling doc symlink
rm docs/changelog.rst
# copy common doc files to top dir
cp -pr docs/ README.rst LICENSE ../

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

# Build documentation
%if 0%{?with_docs}
pushd docs
sphinx-build-3 -b html -d build/doctrees . html
# remove unneeded files which create rpmlint warnings
rm -f html/.buildinfo
popd
%endif


%install
%pyproject_install

%pyproject_save_files whitenoise


%if 0%{?with_check}
%check
export DJANGO_SETTINGS_MODULE=tests.django_settings
%pytest
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license LICENSE


%if 0%{?with_docs}
%files -n python3-%{srcname}-doc
%doc docs/html
%license LICENSE
%endif


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 6.4.0-5
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 13 2023 Jonathan Wright <jonathan@almalinux.org> - 6.4.0-1
- update to 6.4.0 rhbz#2093782
- modernize spec

* Thu Mar 02 2023 Jonathan Wright <jonathan@almalinux.org > - 6.1.0-5
- Skip tests on EL9 due to missing python3-django package
- Remove unnecessary python3-brotli exclusion for el8

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 6.1.0-2
- Rebuilt for Python 3.11

* Mon May 30 2022 Kevin Fenzi <kevin@scrye.com> - 6.1.0-1
- Update to 6.1.0. Fixes rhbz#2052810

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Aug 08 2021 Kevin Fenzi <kevin@scrye.com> - 5.3.0-1
- Update to 5.3.0. Fixes rhbz#1983269

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.2.0-2
- Rebuilt for Python 3.10

* Sat May 22 2021 Kevin Fenzi <kevin@scrye.com> - 5.2.0-1
- Update to 5.2.0. Fixes rhbz#1866031

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 11 2020 Neal Gompa <ngompa13@gmail.com> - 5.1.0-1
- Update to 5.1.0

* Wed Jun 10 2020 Neal Gompa <ngompa13@gmail.com> - 5.0.1-4
- Drop BR on python3-brotli for EL8 as it is not available

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.0.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Piotr Popieluch <piotr1212@gmail.com> - 5.0.1-1
- Update to 5.0.1

* Tue Sep 24 2019 David Moreau-Simard <dmsimard@redhat.com> - 4.1.4-1
- Update to latest upstream release

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.1-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.1-2
- Drop explicit locale setting
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Tue Oct 02 2018 Piotr Popieluch <piotr1212@gmail.com> - 4.1-1
- Update to 4.1
- Remove Python 2 subpackage

* Sun Jul 29 2018 Piotr Popieluch <piotr1212@gmail.com> - 3.3.1-4
- Update python_sitelib to python2_sitelib macro

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.3.1-2
- Rebuilt for Python 3.7

* Mon Mar 19 2018 Piotr Popieluch <piotr1212@gmail.com> - 3.3.1-2
- Update to 3.3.1
- Disable checks on python3 until we have support for Django2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Piotr Popieluch <piotr1212@gmail.com> - 3.1-4
- Upate requires to include Python version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.1-2
- Rebuild for Python 3.6

* Sun Sep 25 2016 Piotr Popieluch <piotr1212@gmail.com> - - 3.1-1
- Update to 3.1

* Sun Sep 25 2016 Piotr Popieluch <piotr1212@gmail.com> - 2.0.6-5
- Update to newer package guidelines
- EL6 support

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.6-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 29 2015 Piotr Popieluch <piotr1212@gmail.com> - 2.0.6-2
- Add license to all subpackages
- Create a python2 subpackage

* Fri Nov 27 2015 Piotr Popieluch <piotr1212@gmail.com> - 2.0.6-1
- Update to new version
- Add missing BR
- Change source from pypi to github
- Use py.test
- Add doc subpackage

* Tue Nov 10 2015 Piotr Popieluch <piotr1212@gmail.com> - 2.0.4-3
- Rewrite spec to support EL6 & EL7

* Thu Nov 05 2015 Piotr Popieluch <piotr1212@gmail.com> - 2.0.4-2
- Remove shebang from gzip.py script

* Thu Oct 22 2015 Piotr Popieluch <piotr1212@gmail.com> - 2.0.4-1
- Initial package
