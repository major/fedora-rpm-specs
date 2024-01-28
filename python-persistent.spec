Name:           python-persistent
Version:        5.1
Release:        3%{?dist}
Summary:        Translucent persistent python objects

License:        ZPL-2.1
URL:            http://www.zodb.org/
Source0:        https://github.com/zopefoundation/persistent/archive/%{version}/persistent-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-docs

%global common_desc %{expand:
This package contains a generic persistence implementation for Python.  It
forms the core protocol for making objects interact transparently with a
database such as python-ZODB3.}

%description %{common_desc}

%package -n python3-persistent
Summary:        Translucent persistent python objects

%description -n python3-persistent %{common_desc}

%package -n python3-persistent-devel
Summary:        Development files for python3-persistent
Requires:       python3-persistent = %{version}-%{release}
BuildArch:      noarch

%description -n python3-persistent-devel
Header files for building applications that use python3-persistent.

%package -n python3-persistent-doc
# The content is ZPL-2.1.  Sphinx copies files into the output with these
# licenses:
# - searchindex.js: BSD-2-Clause
# - _static/basic.css: BSD-2-Clause
# - _static/classic.css: BSD-2-Clause
# - _static/doctools.js: BSD-2-Clause
# - _static/documentation_options.js: BSD-2-Clause
# - _static/file.png: BSD-2-Clause
# - _static/jquery*.js: MIT
# - _static/language_data.js: BSD-2-Clause
# - _static/minus.png: BSD-2-Clause
# - _static/plus.png: BSD-2-Clause
# - _static/pygments.css: ZPL-2.1
# - _static/searchtools.js: BSD-2-Clause
# - _static/sidebar.js: BSD-2-Clause
# - _static/_sphinx_javascript_frameworks_compat.js: BSD-2-Clause
# - _static/underscore*.js: MIT
License:        ZPL-2.1 AND BSD-2-Clause AND MIT
Summary:        Documentation for python3-persistent
Requires:       python3-persistent = %{version}-%{release}
BuildArch:      noarch

Provides:       bundled(js-jquery)
Provides:       bundled(js-underscore)

%description -n python3-persistent-doc
Documentation for python3-persistent.

%prep
%autosetup -N -n persistent-%{version}
%if 0%{?python3_version_nodots} > 311
%autopatch -p1
%endif

# Use local objects.inv for intersphinx
sed -i "s|\('https://docs\.python\.org/3/': \)None|\1'%{_docdir}/python3-docs/html/objects.inv'|" docs/conf.py

%generate_buildrequires
%pyproject_buildrequires -x test,docs rtd.txt

%build
%pyproject_wheel

# Build the documentation
export PYTHONPATH=$PWD/build/lib.%{python3_platform}-cpython-%{python3_version_nodots}
make -C docs html
rst2html --no-datestamp CHANGES.rst CHANGES.html
rst2html --no-datestamp README.rst README.html

%install
%pyproject_install
%pyproject_save_files persistent

# Remove unwanted documentation and source files; fix permissions (Python 3)
rm -f docs/_build/html/.buildinfo
rm -f %{buildroot}%{python3_sitearch}/persistent/*.{c,h}
chmod 0755 %{buildroot}%{python3_sitearch}/persistent/*.so
sed -i '/\.c$/d;/\.h$/d' %{pyproject_files}

# Install _compat.h, needed by BTrees
cp -p src/persistent/_compat.h %{buildroot}%{_includedir}/python3.*/persistent

%check
# The tests depend on uninstalled files, so we cannot use %%tox to test.  We
# also can't point PYTHONPATH to build, because what it wants isn't there
# either.  So we do this song and dance to get the tests to run.
export PYTHONPATH=$PWD/src
cp -p build/lib.*/persistent/*.so src/persistent
zope-testrunner --test-path=src -vc

%files -n python3-persistent -f %{pyproject_files}
%doc CHANGES.html README.html

%files -n python3-persistent-devel
%{_includedir}/python3.*/persistent/

%files -n python3-persistent-doc
%doc docs/_build/html/*

%changelog
* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct  5 2023 Jerry James <loganjerry@gmail.com> - 5.1-1
- Version 5.1
- Drop upstreamed python 3.12 patch

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Jerry James <loganjerry@gmail.com> - 5.0-3
- Add upstream patch for python 3.12 compatibility

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 5.0-3
- Rebuilt for Python 3.12

* Thu Feb 23 2023 Jerry James <loganjerry@gmail.com> - 5.0-2
- Dynamically generate BuildRequires

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan  9 2023 Jerry James <loganjerry@gmail.com> - 5.0-1
- Version 5.0
- Run tests with zope-testrunner

* Mon Nov 28 2022 Jerry James <loganjerry@gmail.com> - 4.9.3-1
- Version 4.9.3

* Sun Nov  6 2022 Jerry James <loganjerry@gmail.com> - 4.9.2-1
- Version 4.9.2

* Fri Sep 16 2022 Jerry James <loganjerry@gmail.com> - 4.9.1-1
- Version 4.9.1
- Convert License tag to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Jerry James <loganjerry@gmail.com> - 4.9.0-2
- Rebuild for python 3.11

* Thu Mar 10 2022 Jerry James <loganjerry@gmail.com> - 4.9.0-1
- Version 4.9.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.7.0-3
- Rebuilt for Python 3.10

* Wed Apr 14 2021 Jerry James <loganjerry@gmail.com> - 4.7.0-2
- Install _compat.h, needed by BTrees

* Tue Apr 13 2021 Jerry James <loganjerry@gmail.com> - 4.7.0-1
- Version 4.7.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.6.4-2
- Rebuilt for Python 3.9

* Fri Mar 27 2020 Jerry James <loganjerry@gmail.com> - 4.6.4-1
- Version 4.6.4
- Drop upstreamed -refs patch

* Thu Mar 19 2020 Jerry James <loganjerry@gmail.com> - 4.6.3-1
- Version 4.6.3
- Drop upstreamed -32bit patch

* Wed Mar 18 2020 Jerry James <loganjerry@gmail.com> - 4.6.2-1
- Version 4.6.2
- Add -refs and -32bit patches
- Build with -fwrapv to fix test failures on 32-bit systems
- Stop shipping _compat.h; BTrees has its own copy

* Thu Mar  5 2020 Jerry James <loganjerry@gmail.com> - 4.6.0-1
- Version 4.6.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov  6 2019 Jerry James <loganjerry@gmail.com> - 4.5.1-1
- Version 4.5.1

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.5.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.5.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 11 2019 Jerry James <loganjerry@gmail.com> - 4.5.0-1
- New upstream version
- Drop upstreamed -format patch

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 17 2018 Jerry James <loganjerry@gmail.com> - 4.4.3-1
- New upstream version
- Drop the python2 subpackage

* Mon Sep 24 2018 Jerry James <loganjerry@gmail.com> - 4.4.2-1
- New upstream version

* Tue Jul 31 2018 Jerry James <loganjerry@gmail.com> - 4.3.0-1
- New upstream version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.2.4.2-4
- Rebuilt for Python 3.7

* Tue Feb 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.2.4.2-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 20 2017 Jerry James <loganjerry@gmail.com> - 4.2.4.2-1
- New upstream version

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 21 2017 Jerry James <loganjerry@gmail.com> - 4.2.4-1
- New upstream version

* Thu Mar  9 2017 Jerry James <loganjerry@gmail.com> - 4.2.3-1
- New upstream version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 21 2016 Jerry James <loganjerry@gmail.com> - 4.2.2-3
- Install a header file that upstream overlooked

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.2.2-2
- Rebuild for Python 3.6

* Fri Dec  2 2016 Jerry James <loganjerry@gmail.com> - 4.2.2-1
- New upstream version

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri May 27 2016 Jerry James <loganjerry@gmail.com> - 4.2.1-1
- New upstream version

* Sat May  7 2016 Jerry James <loganjerry@gmail.com> - 4.2.0-1
- New upstream version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb  1 2016 Jerry James <loganjerry@gmail.com> - 4.1.1-3
- Comply with latest python packaging guidelines

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun  5 2015 Jerry James <loganjerry@gmail.com> - 4.1.1-1
- New upstream version

* Sat May 23 2015 Jerry James <loganjerry@gmail.com> - 4.1.0-1
- New upstream version
- Drop upstreamed -timestamp patch

* Tue Apr 14 2015 Jerry James <loganjerry@gmail.com> - 4.0.9-1
- New upstream version

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun  3 2014 Jerry James <loganjerry@gmail.com> - 4.0.8-2
- Conditionalize python 3 build
- Remove %%clean script

* Thu May 29 2014 Jerry James <loganjerry@gmail.com> - 4.0.8-1
- Initial RPM (bz 1102950)
