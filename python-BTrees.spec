# When bootstrapping a new architecture, there is no python3-ZODB-doc package
# yet, since it requires this package to build.  We only need it for building
# documentation, so use the following procedure:
# 1. Do a bootstrap build of this package.
# 2. Build python-ZODB.
# 3. Do a normal build of this package.
%bcond_with bootstrap

Name:           python-BTrees
Version:        5.0
Release:        2%{?dist}
Summary:        Scalable persistent object containers

License:        ZPL-2.1
URL:            https://www.zodb.org/
Source0:        %pypi_source BTrees

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  python-zope-interface-doc
BuildRequires:  python3-devel
BuildRequires:  python3-docs
BuildRequires:  python3-persistent-devel
BuildRequires:  python3-persistent-doc

%if %{without bootstrap}
BuildRequires:  python-ZODB-doc
%endif

%global common_desc %{expand:
This package contains a set of persistent object containers built around
a modified BTree data structure.  The trees are optimized for use inside
ZODB's "optimistic concurrency" paradigm, and include explicit
resolution of conflicts detected by that mechanism.}

%description %{common_desc}

%package -n python3-BTrees
Summary:        Scalable persistent object containers

%description -n python3-BTrees %{common_desc}

%package        doc
# The content is ZPL-2.1.  Other licenses are due to files copied in by Sphinx.
# _static/_sphinx_javascript_frameworks_compat.js: BSD-2-Clause
# _static/basic.css: BSD-2-Clause
# _static/css: MIT
# _static/custom.css: BSD-3-Clause
# _static/doctools.js: BSD-2-Clause
# _static/documentation_options.js: BSD-2-Clause
# _static/file.png: BSD-2-Clause
# _static/jquery*.js: MIT
# _static/js: MIT
# _static/language_data.js: BSD-2-Clause
# _static/minus.png: BSD-2-Clause
# _static/plus.png: BSD-2-Clause
# _static/searchtools.js: BSD-2-Clause
# _static/sphinx_highlight.js: BSD-2-Clause
# _static/underscore*.js: MIT
# genindex.html: BSD-2-Clause
# search.html: BSD-2-Clause
# searchindex.js: BSD-2-Clause
License:        ZPL-2.1 AND BSD-2-Clause AND BSD-3-Clause AND MIT
Summary:        Documentation for BTrees
BuildArch:      noarch
Requires:       font(fontawesome)
Requires:       font(lato)
Requires:       font(robotoslab)
Provides:       bundled(js-jquery)
Provides:       bundled(js-underscore)

%description    doc
Documentation for %{name}.

%prep
%autosetup -n BTrees-%{version}

# Use local objects.inv for intersphinx
sed -e "s|\('https://docs\.python\.org/3/': \)None|\1'%{_docdir}/python3-docs/html/objects.inv'|" \
    -e "s|\('https://persistent\.readthedocs\.io/en/latest/': \)None|\1'%{_docdir}/python3-persistent-doc/objects.inv'|" \
    -e 's|\("https://zopeinterface\.readthedocs\.io/en/latest/": \)None|\1"%{_docdir}/python-zope-interface/html/objects.inv"|' \
    -i docs/conf.py

%if %{without bootstrap}
sed -e 's|\("https://zodb\.org/en/latest/": \)None|\1"%{_docdir}/python-ZODB-doc/html/objects.inv"|' \
    -i docs/conf.py
%endif

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files BTrees

%{py3_test_envvars} make -C docs html
rst2html --no-datestamp CHANGES.rst CHANGES.html
rst2html --no-datestamp README.rst README.html

# Remove unwanted documentation and source files; fix permissions
rm -f docs/_build/html/{.buildinfo,_static/placeholder.txt}
rm -f %{buildroot}%{python3_sitearch}/BTrees/*{.c,.h,~}
chmod 0755 %{buildroot}%{python3_sitearch}/BTrees/*.so
sed -i '/\.c$/d;/\.h$/d' %{pyproject_files}

%check
%tox

%files -n python3-BTrees -f %{pyproject_files}
%doc CHANGES.html README.html
%exclude %{python3_sitearch}/BTrees/tests

%files doc
%doc docs/_build/html/*

%changelog
* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 5.0-2
- Rebuilt for Python 3.12

* Thu Feb 23 2023 Jerry James <loganjerry@gmail.com> - 5.0-1
- Dynamically generate BuildRequires

* Fri Feb 10 2023 Jerry James <loganjerry@gmail.com> - 5.0-1
- Version 5.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Jerry James <loganjerry@gmail.com> - 4.11.3-1
- Remove support for Fedora 35 and earlier

* Mon Nov 28 2022 Jerry James <loganjerry@gmail.com> - 4.11.3-1
- Version 4.11.3
- Clarify license of the doc subpackage

* Wed Nov  9 2022 Jerry James <loganjerry@gmail.com> - 4.11.1-1
- Version 4.11.1

* Sun Nov  6 2022 Jerry James <loganjerry@gmail.com> - 4.11.0-1
- Version 4.11.0

* Mon Sep 12 2022 Jerry James <loganjerry@gmail.com> - 4.10.1-1
- Version 4.10.1
- Convert License tag to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Python Maint <python-maint@redhat.com> - 4.10.0-3
- Rebuilt for Python 3.11

* Mon Jun 20 2022 Jerry James <loganjerry@gmail.com> - 4.10.0-2
- Rebuild for python 3.11

* Wed Mar  9 2022 Jerry James <loganjerry@gmail.com> - 4.10.0-1
- Version 4.10.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 14 2022 Jerry James <loganjerry@gmail.com> - 4.9.2-3
- Update python macros
- Fix documentation crosslinks
- Test with tox instead of nose on Fedora 36+

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun  9 2021 Jerry James <loganjerry@gmail.com> - 4.9.2-1
- Version 4.9.2

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.9.1-2
- Rebuilt for Python 3.10

* Thu May 27 2021 Jerry James <loganjerry@gmail.com> - 4.9.1-1
- Version 4.9.1

* Wed May 26 2021 Jerry James <loganjerry@gmail.com> - 4.9.0-1
- Version 4.9.0

* Wed Apr 14 2021 Jerry James <loganjerry@gmail.com> - 4.8.0-1
- Version 4.8.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan  7 2021 Jerry James <loganjerry@gmail.com> - 4.7.2-4
- Remove no longer needed sphinx_rtd_theme font unbundling (bz 1913819)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.7.2-2
- Rebuilt for Python 3.9

* Wed Apr  8 2020 Jerry James <loganjerry@gmail.com> - 4.7.2-1
- Version 4.7.2

* Sun Mar 22 2020 Jerry James <loganjerry@gmail.com> - 4.7.1-1
- Version 4.7.1
- Use fc-match for a more robust approach to symlinking fonts

* Wed Mar 18 2020 Jerry James <loganjerry@gmail.com> - 4.7.0-1
- Version 4.7.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Jerry James <loganjerry@gmail.com> - 4.6.1-1
- Version 4.6.1
- Add -doc subpackage
- Unbundle fonts from the documentation

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.6.0-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.6.0-2
- Rebuilt for Python 3.8

* Fri Aug  2 2019 Jerry James <loganjerry@gmail.com> - 4.6.0-1
- New upstream version

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 17 2018 Jerry James <loganjerry@gmail.com> - 4.5.1-2
- Drop python2 subpackage

* Thu Aug  9 2018 Jerry James <loganjerry@gmail.com> - 4.5.1-1
- New upstream version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.5.0-2
- Rebuilt for Python 3.7

* Fri Apr 27 2018 Jerry James <loganjerry@gmail.com> - 4.5.0-1
- New upstream version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.4.1-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 25 2017 Jerry James <loganjerry@gmail.com> - 4.4.1-1
- New upstream version

* Sat Jan 14 2017 Jerry James <loganjerry@gmail.com> - 4.4.0-1
- New upstream version

* Fri Jan  6 2017 Jerry James <loganjerry@gmail.com> - 4.3.2-1
- New upstream version

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.3.1-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue May 17 2016 Jerry James <loganjerry@gmail.com> - 4.3.1-1
- New upstream version

* Tue May 10 2016 Jerry James <loganjerry@gmail.com> - 4.3.0-1
- New upstream version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb  1 2016 Jerry James <loganjerry@gmail.com> - 4.2.0-1
- Update to current python packaging guidelines
- Actually package the documentation we built
- Run all the tests
- Don't ship the tests

* Fri Nov 13 2015 Jerry James <loganjerry@gmail.com> - 4.2.0-1
- New upstream version, fixes python 3.5 build

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun  8 2015 Jerry James <loganjerry@gmail.com> - 4.1.4-1
- New upstream version

* Sat May 23 2015 Jerry James <loganjerry@gmail.com> - 4.1.3-1
- New upstream version

* Tue Apr 14 2015 Jerry James <loganjerry@gmail.com> - 4.1.2-1
- New upstream version

* Mon Jan  5 2015 Jerry James <loganjerry@gmail.com> - 4.1.1-1
- New upstream version
- Drop upstreamed -overflow patch
- Use license macro

* Tue Aug 12 2014 Jerry James <loganjerry@gmail.com> - 4.0.8-2
- Add -overflow patch to fix test failures with 32-bit python 3.4

* Mon Jun  2 2014 Jerry James <loganjerry@gmail.com> - 4.0.8-1
- Initial RPM
