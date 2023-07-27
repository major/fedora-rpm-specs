Name:           python-django
%global         pkgname Django
%global         ver 4.2.3
#global         pre ...
%global         real_version %{ver}%{?pre:%{pre}}
Version:        %{ver}%{?pre:~%{pre}}
Release:        1%{?dist}
Summary:        A high-level Python Web framework

License:        BSD-3-Clause
URL:            https://www.djangoproject.com/
Source0:        %{pypi_source %{pkgname} %{real_version}}

# FAIL: test_complex_override_warning (settings_tests.tests.TestComplexSettingOverride.test_complex_override_warning)
# Regression test for #19031
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/builddir/build/BUILD/Django-4.2.1/tests/settings_tests/tests.py", line 400, in test_complex_override_warning
#     self.assertEqual(cm.filename, __file__)
# AssertionError: '/usr/lib64/python3.12/unittest/case.py' != '/builddir/build/BUILD/Django-4.2.1/tests/settings_tests/tests.py'
# - /usr/lib64/python3.12/unittest/case.py
# + /builddir/build/BUILD/Django-4.2.1/tests/settings_tests/tests.py
Patch:          dirty-hack-remove-assert.patch

BuildArch:      noarch

%global _description %{expand:
Django is a high-level Python Web framework that encourages rapid
development and a clean, pragmatic design. It focuses on automating as
much as possible and adhering to the DRY (Don't Repeat Yourself)
principle.}

%description %_description


%package bash-completion
Summary:        Bash completion files for Django
BuildRequires:  bash-completion
Requires:       bash-completion

%description bash-completion
This package contains the Bash completion files form Django high-level
Python Web framework.


%package -n python3-django-doc
Summary:        Documentation for Django
Suggests:       python3-django = %{version}-%{release}
BuildRequires:  make

%description -n python3-django-doc
This package contains the documentation for the Django high-level
Python Web framework.


%package -n python3-django
Summary:        A high-level Python Web framework

Recommends:     (%{name}-bash-completion = %{version}-%{release} if bash)

BuildRequires:  python3-devel
BuildRequires:  python3-asgiref

Provides: bundled(jquery) = 2.2.3
Provides: bundled(xregexp) = 2.0.0

%description -n python3-django %_description

%prep
%autosetup -p1 -n %{pkgname}-%{real_version}

# hard-code python3 in django-admin
pushd django
for file in conf/project_template/manage.py-tpl ; do
    sed -i "s/\/env python/\/python3/" $file ;
done
popd

# Use non optimised psycopg for tests
# Not available in Fedora
sed -i 's/psycopg\[binary\]>=3\.1\.8/psycopg>=3.1.8/' tests/requirements/postgres.txt

# Remove unnecessary test BRs
sed -i '/^pywatchman\b/d' tests/requirements/py3.txt
sed -i '/^tzdata$/d' tests/requirements/py3.txt

# Remove deps on code checkers/linters
sed -i '/^black\b/d' tests/requirements/py3.txt
sed -i '/^blacken-docs\b/d' docs/requirements.txt

%generate_buildrequires
%pyproject_buildrequires -r tests/requirements/{py3,postgres,mysql,oracle}.txt docs/requirements.txt

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files django


# build documentation
(cd docs && mkdir djangohtml && mkdir -p _build/{doctrees,html} && make html)
cp -ar docs ..

# install man pages (for the main executable only)
mkdir -p %{buildroot}%{_mandir}/man1/
cp -p docs/man/* %{buildroot}%{_mandir}/man1/

# install bash completion script
bashcompdir=$(pkg-config --variable=completionsdir bash-completion)
mkdir -p %{buildroot}$bashcompdir
install -m 0644 -p extras/django_bash_completion \
  %{buildroot}$bashcompdir/django-admin.py

for file in django-admin django-admin-3 django-admin-%{python3_version} python3-django-admin manage.py ; do
   ln -s django-admin.py %{buildroot}$bashcompdir/$file
done

# Add backward compatible links to %%{_bindir}
ln -s ./django-admin %{buildroot}%{_bindir}/django-admin-3
ln -s ./django-admin %{buildroot}%{_bindir}/django-admin-%{python3_version}
ln -s ./django-admin %{buildroot}%{_bindir}/python3-django-admin

# remove .po files
find %{buildroot} -name "*.po" | xargs rm -f
sed -i '/.po$/d' %{pyproject_files}

%check
cd %{_builddir}/%{pkgname}-%{real_version}
export PYTHONPATH=$(pwd)
cd tests

# disable two tests due to regression in 3.12b4:
# https://github.com/python/cpython/issues/106669
%{python3} runtests.py --settings=test_sqlite --verbosity=2 --parallel 1 \
%if v"%{python3_version}" >= v"3.12"
  -k "not test_safe_mime_multipart and not test_unicode_address_header"
%endif

%files bash-completion
%{_datadir}/bash-completion

%files -n python3-django-doc
%doc docs/_build/html/*

%files -n python3-django -f %{pyproject_files}
%doc AUTHORS README.rst
%license LICENSE
%{_bindir}/django-admin
%{_bindir}/django-admin-3
%{_bindir}/django-admin-%{python3_version}
%{_bindir}/python3-django-admin
%{_mandir}/man1/django-admin.1*


%changelog
* Wed Jul 19 2023 Michel Alexandre Salim <salimma@fedoraproject.org> - 4.2.3-1
- Update to 4.2.3 (rhbz#2212391)
- Use SPDX license identifier
- Drop unused patches

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 4.2.1-3
- Rebuilt for Python 3.12

* Fri May 5 2023 Steve Traylen <steve.traylen@cern.ch> - 4.2.1-1
- Use non binary version of psycopg in tests
- Remove build dependency on black code checker
- update to 4.2.1 (rhbz#2059544)

* Mon Feb 13 2023 Matthias Runge <mrunge@redhat.com> - 4.1.7-1
- update to 4.1.7 (rhbz#2169312)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Karolina Surma <ksurma@redhat.com> - 4.0.2-5
- Fix docs build with Sphinx 5+

* Tue Jun 14 2022 Miro Hrončok <mhroncok@redhat.com> - 4.0.2-4
- Use dynamic BuildRequires for test and docs dependencies

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 4.0.2-3
- Rebuilt for Python 3.11

* Tue Apr 19 2022 Miro Hrončok <mhroncok@redhat.com> - 4.0.2-2
- Fix inspectdb.tests.InspectDBTestCase.test_custom_fields() on SQLite 3.37+
- Fixes: rhbz#2070100

* Wed Feb 02 2022 Matthias Runge <mrunge@redhat.com> - 4.0.2-1
- rebase to 4.0.2, fix for CVE-2022-22818 (rhbz#2049332)
- fix for CVE-2022-23833 (rhbz#2049325)
- this also fixes rhbz#1961135, rhbz#1967410, rhbz#1967428, rhbz#2037174, rhbz#2048940

* Mon Jan 24 2022 Matthias Runge <mrunge@redhat.com> - 4.0.1-1
- rebase to 4.0.x, https://fedoraproject.org/wiki/Changes/Django4.0, also rhbz#2006537

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 17 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 3.2.9-4
- Drop obsolete python_provide lines

* Wed Dec 15 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 3.2.9-3
- Use build-dependency generator
- Use pyproject macros

* Wed Dec 15 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 3.2.9-2
- Drop old BR on python3-mock

* Wed Nov 24 2021 Karolina Surma <ksurma@redhat.com> - 3.2.9-1
- update to 3.2.9
- unskip fixed tests
- backport fix for building docs with python-sphinx 4.3.0

* Wed Sep 08 2021 Matthias Runge <mrunge@redhat.com> - 3.2.7-1
- update to 3.2.7 (rhbz#1999958)

* Mon Aug 09 2021 Matthias Runge <mrunge@redhat.com> - 3.2.6-1
- update to 3.2.6 (rhbz#1957630)
- skip failing test AssertionError: "Error: invalid choice: 'test'
  (choose from 'foo')"(rhbz#1898084)

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.2.1-2
- Rebuilt for Python 3.10

* Tue May 04 2021 Matthias Runge <mrunge@redhat.com> - 3.2.1-1
- rebase to 3.2.1, fixes CVE-2021-31542
- rebase to 3.1.8 fixes CVE-2021-28658 (rbhz#1946580)
- rebase to 3.2.1 (rhbz#1917820)

* Fri Mar 05 2021 Matthias Runge <mrunge@redhat.com> - 3.1.7-1
- update to 3.1.7, fix CVE-2021-23336 (rhbz#1931542)

* Thu Feb 04 2021 Matthias Runge <mrunge@redhat.com> - 3.1.6-1
- update to 3.1.6, fix CVE-2021-3281 (rhbz#1923734)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 04 2021 Matthias Runge <mrunge@redhat.com> - 3.1.5-1
- update to 3.1.5

* Thu Dec 03 2020 Matthias Runge <mrunge@redhat.com> - 3.1.4-1
- update to 3.1.4 (rhbz#1893635)

* Thu Oct 01 2020 Matthias Runge <mrunge@redhat.com> - 3.1.2-1
- update to 3.1.2 (rhbz#1874420)

* Thu Sep 03 2020 Matthias Runge <mrunge@redhat.com> - 3.1.1-1
- update to 3.1.1 (rhbz#1874420)

* Sun Aug 30 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 3.1-1
- Update to 3.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 3.0.7-2
- Add BR on setuptools

* Sun Jun 07 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.7-1
- Update to 3.0.7
- Security fix for CVE-2020-7471 (rhbz#1798516)
- Security fix for CVE-2020-9402 (rhbz#1810093)
- Security fix for CVE-2020-13254 (rhbz#1843617)
- Security fix for CVE-2020-13596 (rhbz#1843627)

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.2-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 02 2020 Matthias Runge <mrunge@redhat.com> - 3.0.2-1
- bugfix release

* Tue Dec 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0-1
- Update to 3.0 final

* Tue Oct 15 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0~b1-1
- Update to 3.0b1 (rhbz#1761417)

* Fri Oct 04 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0~a1-1
- Update to 3.0a1 (rhbz#1750709)
- https://fedoraproject.org/wiki/Changes/Django3

* Thu Sep 05 2019 Matthias Runge <mrunge@redhat.com> - 2.2.5-1
- bugfix release 2.2.5 (rhbz#1747876)

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.4-2
- Rebuilt for Python 3.8

* Tue Aug 06 2019 Matthias Runge <mrunge@redhat.com> - 2.2.4-1
- fix CVE-2019-14235 (rhbz#1735784)
- fix CVE-2019-14234 (rhbz#1735780)
- fix CVE-2019-14233 (rhbz#1735775)
- fix CVE-2019-14232 (rhbz#1735771)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 04 2019 Matthias Runge <mrunge@redhat.com> - 2.2.3-1
- fix CVE-2019-12781 Incorrect HTTP detection with reverse-proxy connecting
  via HTTPS (rhbz#1726014)

* Tue Jun 04 2019 Matthias Runge <mrunge@redhat.com> - 2.2.2-1
- fix CVE-2019-12308 AdminURLFieldWidget XSS
  (rhbz#1716763)

* Wed Apr 10 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2-1
- Update to 2.2 (rhbz#1674439)

* Wed Feb 20 2019 Matthias Runge <mrunge@redhat.com> - 2.1.7-1
- Fix CVE-2019-6975: Memory exhaustion in django.utils.numberformat.format()
  rhbz#1678264

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.5-2
- Enable python dependency generator

* Mon Jan 07 2019 Matthias Runge <mrunge@redhat.com> - 2.1.5-1
- fix CVE-2019-3498 python-django: Content spoofing via URL path in
  default 404 page (rhbz#1663723)

* Mon Oct 22 2018 Matthias Runge <mrunge@redhat.com> - 2.1.2-1
- fix CVE-2018-16984 Password hash disclosure to “view only” admin users
  (rhbz#1639399)

* Fri Aug 17 2018 Matthias Runge <mrunge@redhat.com> - 2.1-1
- update to 2.1 (rhbz#1611025)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 06 2018 Matthias Runge <mrunge@redhat.com> - 2.0.7-1
- bugfix update to 2.0.7 (rhbz#1597265)

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.6-2
- Rebuilt for Python 3.7

* Mon Jun 04 2018 Matthias Runge <mrunge@redhat.com> - 2.0.6-1
- bugfix update to 2.0.6 (rhbz#1585347)

* Thu May 03 2018 Matthias Runge <mrunge@redhat.com> - 2.0.5-1
- update to 2.0.5 (rhbz#1574123)

* Tue Apr 03 2018 Matthias Runge <mrunge@redhat.com> - 2.0.4-1
- update to 2.0.4 (rhbz#1541188)

* Fri Mar 16 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-4
- Obsolete pythonX-django-ckeditor, pythonX-django-extensions,
  pythonX-django-helpdesk, pythonX-django-openid-auth, pythonX-django-pylibmc,
  pythonX-django-select2, pythonX-django-setuptest,
  pythonX-django-federated-login

* Sun Mar 11 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-3
- Obsolete pythonX-django-pgjson

* Wed Mar 07 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-2
- Obsolete pythonX-django-sekizai and pythonX-django-south

* Tue Mar 06 2018 Matthias Runge <mrunge@redhat.com> - 2.0.3-1
- update to 2.0.3, fix CVE-2018-7536 (rhbz#1552178)

* Fri Mar 02 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-4
- Obsolete packages retired from https://pagure.io/fesco/issue/1857

* Fri Mar 02 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-3
- Obsolete pythonX-django-model-utils and pythonX-django-netjsongraph

* Wed Feb 07 2018 Matthias Runge <mrunge@redhat.com> - 2.0.2-2
- requires python2 while being python3 (rhbz#15424)

* Fri Feb 02 2018 Matthias Runge <mrunge@redhat.com> - 2.0.2-1
- fix CVE-2018-6188

* Tue Jan 16 2018 Matthias Runge <mrunge@redhat.com> - 2.0.1-1
- update to 2.0.1
- remove python2 bits
- enable python3 tests

* Tue Jan 16 2018 Troy Dawson <tdawson@redhat.com> - 1.11.9-2
- Update conditionals

* Thu Jan 04 2018 Miro Hrončok <mhroncok@redhat.com> - 1.11.9-1
- update to 1.11.9

* Thu Jan 04 2018 Miro Hrončok <mhroncok@redhat.com> - 1.11.8-2
- Obsolete python(2)-django-devserver

* Fri Dec 15 2017 Matthias Runge <mrunge@redhat.com> - 1.11.8-1
- update to 1.11.8

* Wed Sep 06 2017 Matthias Runge <mrunge@redhat.com> - 1.11.5-1
- update to 1.11.5 (rhbz#1488683)

* Wed Aug 02 2017 Matthias Runge <mrunge@redhat.com> - 1.11.4-1
- update to 1.11.4 (rhbz#1477382)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Matthias Runge <mrunge@redhat.com> - 1.11.3-1
- Update to 1.11.3 (rhbz#1467029)

* Thu Jun 15 2017 Matthias Runge <mrunge@redhat.com> - 1.11.2-1
- update to 1.11.2 (rhbz#1448664
- add dependency to pytz (rhbz#1458493)

* Thu Apr 06 2017 Matthias Runge <mrunge@redhat.com> - 1.11-1
- update to 1.11 (rhbz#1410268)

* Tue Feb 28 2017 Matthias Runge <mrunge@redhat.com> - 1.10.5-1
- rebase to 1.10.5, fix FTBFS (rhbz#1424135)
- declare bundled libs (rhbz#1401243)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 12 2016 Stratakis Charalampos <cstratak@redhat.com> - 1.10.4-2
- Rebuild for Python 3.6
- Disable python3 tests for now

* Fri Dec 02 2016 Matthias Runge <mrunge@redhat.com> - 1.10.4-1
- update to stable 1.10.4 (rhbz#1400730)

* Wed Nov 02 2016 Matthias Runge <mrunge@redhat.com> - 1.10.3-1
- update to 1.10.3 (rhbz#1390782)
- fix CVE-2016-9013, CVE-2016-9014

* Mon Oct 03 2016 Matthias Runge <mrunge@redhat.com> - 1.10.2-1
- update to 1.10.2 (rhbz#1381019)

* Thu Sep 22 2016 Matthias Runge <mrunge@redhat.com> - 1.10.1-1
- rebase to 1.10.1 (rhbz#1338391)

* Thu Jul 21 2016 Matthias Runge <mrunge@redhat.com> - 1-9.8-1
- fix CVE-2016-6186 (rhbz#1357701)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.7-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jun 06 2016 Matthias Runge <mrunge@redhat.com> - 1.9.7-1
- bugfix release

* Tue May 31 2016 Nils Philippsen <nils@redhat.com>
- fix source URL

* Sun May  8 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.9.6-2
- Put the provives/obsoletes in the right spot for new python naming

* Tue May 03 2016 Matthias Runge <mrunge@redhat.com> - 1.9.6-1
- update to 1.9.6 (rhbz#1323374)

* Tue Mar 08 2016 Matthias Runge <mrunge@redhat.com> - 1.9.4-1
- update to 1.9.4 fixing a regression introduced in last
  upstream fix for CVE-2016-2512

* Wed Mar 02 2016 Matthias Runge <mrunge@redhat.com> - 1.9.3-1
- update to 1.9.3, fixing CVE-2016-2512, CVE-2016-2513
  (rhbz#1313500)

* Thu Feb 11 2016 Matthias Runge <mrunge@redhat.com> - 1.9.2-1
- update to 1.9.2 (rhbz#1266062)
- modernize spec file, provide py2, obsolete python-django

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

