Name:           python-ZODB
Version:        5.8.0
Release:        2%{?dist}
Summary:        Zope Object Database and persistence

License:        ZPL-2.1
URL:            https://www.zodb.org/
Source0:        %pypi_source ZODB
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  python-BTrees-doc
BuildRequires:  python3-devel
BuildRequires:  python3-docs
BuildRequires:  python3-persistent-devel
BuildRequires:  python3-persistent-doc

%global common_desc                                                \
The ZODB package provides a set of tools for using the Zope Object \
Database (ZODB).

%description
%{common_desc}

%package -n python3-ZODB
Summary:        Zope Object Database and persistence

%description -n python3-ZODB
%{common_desc}

%package doc
# The content is ZPL-2.1.  Other licenses are due to files copied in by Sphinx.
# _static/_sphinx_javascript_frameworks_compat.js: BSD-2-Clause
# _static/basic.css: BSD-2-Clause
# _static/css: MIT
# _static/doctools.js: BSD-2-Clause
# _static/documentation_options.js: BSD-2-Clause
# _static/file.png: BSD-2-Clause
# _static/jquery*.js: MIT
# _static/js: MIT
# _static/language_data.js: BSD-2-Clause
# _static/minus.png: BSD-2-Clause
# _static/plus.png: BSD-2-Clause
# _static/searchtools.js: BSD-2-Clause
# _static/underscore*.js: MIT
# genindex.html: BSD-2-Clause
# search.html: BSD-2-Clause
# searchindex.js: BSD-2-Clause
License:        ZPL-2.1 AND BSD-2-Clause AND MIT
Summary:        Documentation for ZODB

%description doc
Documentation for ZODB.

%prep
%autosetup -n ZODB-%{version}

# Use local objects.inv for intersphinx
sed -e "s|\('https://docs\.python\.org/3/', \)None|\1'%{_docdir}/python3-docs/html/objects.inv'|" \
    -e "s|\('https://persistent\.readthedocs\.io/en/latest/', \)None|\1'%{_docdir}/python3-persistent-doc/objects.inv'|" \
    -e "s|\(\"https://btrees\.readthedocs\.io/en/latest/\", \)None|\1'%{_docdir}/python-BTrees-doc/objects.inv'|" \
    -i docs/conf.py

# Fix shebangs
%py3_shebang_fix src/ZODB/scripts

%generate_buildrequires
%pyproject_buildrequires -t -x test,docs

%build
%pyproject_wheel

# Build the documentation
cp -p docs/.static/zodb.ico doc
make -C docs html SPHINXBUILD=%{_bindir}/sphinx-build PYTHONPATH=$PWD/src
rm docs/build/html/.buildinfo
rst2html --no-datestamp CHANGES.rst CHANGES.html

%install
%pyproject_install
%pyproject_save_files ZODB

%check
export PYTHONPATH=$PWD/src
%tox

%files -n python3-ZODB -f %{pyproject_files}
%doc CHANGES.html
%{_bindir}/fsdump
%{_bindir}/fsoids
%{_bindir}/fsrefs
%{_bindir}/fstail
%{_bindir}/repozo

%files doc
%doc docs/build/html

%changelog
* Thu Feb 23 2023 Jerry James <loganjerry@gmail.com> - 5.8.0-2
- Dynamically generate BuildRequires

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 13 2022 Jerry James <loganjerry@gmail.com> - 5.8.0-1
- Add License tag to the doc subpackage

* Wed Nov  9 2022 Jerry James <loganjerry@gmail.com> - 5.8.0-1
- Version 5.8.0
- Convert License tag to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Jerry James <loganjerry@gmail.com> - 5.7.0-2
- Rebuild for python 3.11

* Sat Mar 19 2022 Jerry James <loganjerry@gmail.com> - 5.7.0-1
- Version 5.7.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.6.0-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 16 2020 Jerry James <loganjerry@gmail.com> - 5.6.0-1
- Version 5.6.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.5.1-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 5.5.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 5.5.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 17 2018 Jerry James <loganjerry@gmail.com> - 5.5.1-1
- New upstream release
- Drop the python2 subpackage

* Thu Sep 13 2018 Jerry James <loganjerry@gmail.com> - 5.4.0-4
- Build documentation again, in the -doc subpackage

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 5.4.0-2
- Rebuilt for Python 3.7

* Mon Mar 26 2018 Jerry James <loganjerry@gmail.com> - 5.4.0-1
- New upstream release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct  7 2017 Jerry James <loganjerry@gmail.com> - 5.3.0-1
- New upstream release
- Skip doc building until new dependencies can be added to Fedora

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 5.1.1-2
- Rebuild for Python 3.6

* Sat Dec 10 2016 Jerry James <loganjerry@gmail.com> - 5.1.1-1
- New upstream release

* Tue Sep  6 2016 Jerry James <loganjerry@gmail.com> - 5.0.0-1
- New upstream release

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jun 10 2016 Jerry James <loganjerry@gmail.com> - 4.3.1-1
- New upstream release

* Wed Jun  1 2016 Jerry James <loganjerry@gmail.com> - 4.3.0-1
- New upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb  1 2016 Jerry James <loganjerry@gmail.com> - 4.2.0-3
- Comply with latest python packaging guidelines

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun  9 2015 Jerry James <loganjerry@gmail.com> - 4.2.0-1
- New upstream release

* Mon Jan 12 2015 Jerry James <loganjerry@gmail.com> - 4.1.0-1
- New upstream release

* Wed Aug  6 2014 Jerry James <loganjerry@gmail.com> - 4.0.1-1
- New upstream release

* Wed Jun 11 2014 Jerry James <loganjerry@gmail.com> - 4.0.0-1
- Initial RPM
