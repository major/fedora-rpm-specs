%global module_name pycodestyle

%if 0%{?fedora} >= 32 || 0%{?rhel} >= 9
%bcond_with python2
%else
%bcond_without python2
%endif

Name:           python-%{module_name}
# WARNING: When updating pycodestyle, check not to break flake8!
Version:        2.10.0
Release:        3%{?dist}
Summary:        Python style guide checker
License:        MIT
URL:            https://pypi.python.org/pypi/%{module_name}
Source0:        %{pypi_source %{module_name}}
# Various fixes for Python 3.12
# https://github.com/PyCQA/pycodestyle/pull/1148
# https://github.com/PyCQA/pycodestyle/commit/84937582b81d570b95354e33a746947f84462c55
Patch0:         0001-add-fix-for-muting-FSTRING_MIDDLE-in-3.12.patch
# https://github.com/PyCQA/pycodestyle/pull/1129
# https://github.com/PyCQA/pycodestyle/commit/7023956c8975d34317aa146b8e3d73ebd43d204c
# Necessary precursor to make Patch2 apply cleanly
# Rediffed - dropped the changes to unpackaged files
Patch1:         0001-drop-python3.6.patch
# https://github.com/PyCQA/pycodestyle/pull/1152
# https://github.com/PyCQA/pycodestyle/commit/e8d84098da10d013ee686027e174814dbe4dd908
# Rediffed - dropped the changes to unpackaged github file
Patch2:         0001-get-testsuite-passing-on-3.12.patch
# https://github.com/PyCQA/pycodestyle/pull/1153
# https://github.com/PyCQA/pycodestyle/commit/0d786b43a09243d7655831d0b6c4a94a8d7c7581
Patch3:         0001-add-test-file-for-new-3.12-syntax.patch
# https://github.com/PyCQA/pycodestyle/pull/1154
# https://github.com/PyCQA/pycodestyle/commit/6fddf7399d70627c46d1cc82bb3c02da2d708ec4
Patch4:         0001-3.12-format-specs-are-not-an-error.patch

BuildArch:      noarch

%description
pycodestyle is a tool to check your Python code against some of the style
conventions in PEP 8. It has a plugin architecture, making new checks easy, and
its output is parseable, making it easy to jump to an error location in your
editor.

%if %{with python2}
%package -n python2-%{module_name}
Summary:        Python style guide checker
%{?python_provide:%python_provide python2-%{module_name}}

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
Requires:       python2-setuptools


%description -n python2-%{module_name}
pycodestyle is a tool to check your Python code against some of the style
conventions in PEP 8. It has a plugin architecture, making new checks easy, and
its output is parseable, making it easy to jump to an error location in your
editor.
%endif


%package -n python%{python3_pkgversion}-pycodestyle
Summary:    Python style guide checker
%{?python_provide:%python_provide python%{python3_pkgversion}-%{module_name}}
Conflicts:      python-pycodestyle < %{version}-%{release}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-sphinx_rtd_theme
BuildRequires:  make

%description -n python%{python3_pkgversion}-pycodestyle
pycodestyle is a tool to check your Python code against some of the style
conventions in PEP 8. It has a plugin architecture, making new checks easy, and
its output is parseable, making it easy to jump to an error location in your
editor.

This is a version for Python %{python3_pkgversion}.


%prep
%autosetup -n %{module_name}-%{version} -p1

# Remove #! from pycodestyle.py
sed --in-place "s:#!\s*/usr.*::" pycodestyle.py


%build
%if %{with python2}
%py2_build
%endif
%py3_build

make -C docs man SPHINXBUILD=sphinx-build-%{python3_version}


%install
%if %{with python2}
%py2_install
mv %{buildroot}%{_bindir}/pycodestyle %{buildroot}%{_bindir}/pycodestyle-%{python2_version}
ln -s ./pycodestyle-%{python2_version} %{buildroot}%{_bindir}/pycodestyle-2
%endif

%py3_install
mv %{buildroot}%{_bindir}/pycodestyle %{buildroot}%{_bindir}/pycodestyle-%{python3_version}
ln -s ./pycodestyle-%{python3_version} %{buildroot}%{_bindir}/pycodestyle-3
ln -s ./pycodestyle-3 %{buildroot}%{_bindir}/pycodestyle


install -D docs/_build/man/%{module_name}.1 %{buildroot}%{_mandir}/man1/%{module_name}.1


%check
%if %{with python2}
%{__python2} pycodestyle.py --max-doc-length=72 --testsuite testsuite
%{__python2} pycodestyle.py --max-doc-length=72 --doctest
%endif
%{__python3} pycodestyle.py --max-doc-length=72 --testsuite testsuite
%{__python3} pycodestyle.py --max-doc-length=72 --doctest


%if %{with python2}
%files -n python2-%{module_name}
%doc CHANGES.txt README.rst
%license LICENSE
%{_bindir}/pycodestyle-2
%{_bindir}/pycodestyle-2.7
%{python2_sitelib}/%{module_name}.py*
%{python2_sitelib}/%{module_name}-%{version}-*.egg-info
%endif

%files -n python%{python3_pkgversion}-pycodestyle
%doc README.rst CHANGES.txt
%license LICENSE
%{_mandir}/man1/%{module_name}.1.gz
%{_bindir}/pycodestyle
%{_bindir}/pycodestyle-3
%{_bindir}/pycodestyle-%{python3_version}
%pycached %{python3_sitelib}/%{module_name}.py
%{python3_sitelib}/%{module_name}-%{version}-*.egg-info/

%changelog
* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 13 2023 Adam Williamson <awilliam@redhat.com> - 2.10.0-1
- Update to 2.10.0
- Backport Python 3.12 fixes from upstream

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 2.9.1-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 04 2022 Orion Poplawski <orion@nwra.com> - 2.9.1-1
- Update to 2.9.1

* Tue Aug 02 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 2.9.0-1
- Update to 2.9.0 (RHBZ #2112577)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.8.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 12 2021 Orion Poplawski <orion@nwra.com> - 2.8.0-1
- Update to 2.8.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 05 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.7.0-1
- Update to 2.7.0

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.6.0-5
- Rebuilt for Python 3.10

* Thu Feb 18 2021 Miro Hrončok <mhroncok@redhat.com> - 2.6.0-4
- Properly BuildRequire make

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 31 2020 Miro Hrončok <mhroncok@redhat.com> - 2.6.0-1
- Update to 2.6.0 (#1827430)

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 Orion Poplawski <orion@nwra.com> - 2.5.0-6
- Drop python2 for Fedora 32+

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-2
- Make /usr/bin/pycodestyle Python 3

* Wed Feb 20 2019 Matthias Runge <mrunge@redhat.com> - 2.5.0-1
- update to 2.5.0 and fix FTBFS

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-2
- Rebuilt for Python 3.7

* Sat Jun 02 2018 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-1
- Update to 2.4.0 (#1565613)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 24 2017 Lumír Balhar <lbalhar@redhat.com> 2.3.1-1
- New upstream version 2.3.1
- Use 'python2' instead of just 'python' in the names of dependencies

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 10 2017 Orion Poplawski <orion@cora.nwra.com> - 2.0.0-5
- Fix python3 builds for EPEL
- Cleanup spec

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.0.0-3
- Rebuild for Python 3.6

* Thu Aug  4 2016 Luke Macken <lmacken@redhat.com> - 2.0.0-2
- Use the new python setup/build/install macros
- Remove Obsoletes/Provides for pep8, since it is currently not a drop-in replacement.
  https://bugzilla.redhat.com/show_bug.cgi?id=1342839#c10

* Sun Jun 05 2016 Luke Macken <lmacken@redhat.com> - 2.0.0-1
- The pep8 project has been renamed to pycodestyle
- Create python2 subpackage
- Update the source url to use pypi.io
- Build a man page instead of html docs

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 12 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Nov 11 2015 Robert Kuska <rkuska@redhat.com> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Nov 11 2015 Matthias Runge <mrunge@redhat.com> - 1.6.2-1
- update to 1.6.2

* Fri Nov 06 2015 Robert Kuska <rkuska@redhat.com> - 1.5.7-3
- Rebuilt for Python3.5 rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Oct 20 2014 Matthias Runge <mrunge@redhat.com> - 1.5.7-1
- update to 1.5.7

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 15 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed May 14 2014 Matthias Runge <mrunge@redhat.com> - 1.5.6-1
- update to 1.5.6 (rhbz#1087351)

* Tue Apr 08 2014 Matthias Runge <mrunge@redhat.com> - 1.5.4-1
- require python3-setuptools (rhbz#1084756)
- update to 1.5.4 (rhbz#1081516)

* Wed Feb 26 2014 Matthias Runge <mrunge@redhat.com> -1.4.6-2
- rename py3 version of pep8 to python3-pep8 (rhbz#1060408)

* Tue Aug 13 2013 Ian Weller <iweller@redhat.com> - 1.4.6-1
- update to 1.4.6

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 14 2013 Matthias Runge <mrunge@redhat.com> - 1.4.5-1
- update to 1.4.5 (rhbz#918924)
- introduce py3 package (rhbz#971941)

* Tue Feb 26 2013 Ian Weller <iweller@redhat.com> - 1.4.4-1
- Update to 1.4.4

* Mon Feb 11 2013 Ian Weller <iweller@redhat.com> - 1.4.2-1
- Update to 1.4.2

* Tue Jan 29 2013 Ian Weller <iweller@redhat.com> - 1.4.1-1
- Update to 1.4.1
- Add Sphinx docs

* Fri Sep 07 2012 Ian Weller <iweller@redhat.com> - 1.3.3-3
- Run test suite using the pep8.py that has been installed

* Fri Sep 07 2012 Ian Weller <iweller@redhat.com> - 1.3.3-2
- Add test suite

* Thu Sep 06 2012 Ian Weller <iweller@redhat.com> - 1.3.3-1
- Update to 1.3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 16 2012 Ian Weller <iweller@redhat.com> - 1.3-1
- Update to 1.3

* Sat Apr 07 2012 Ian Weller <iweller@redhat.com> - 1.0.1-1
- Update to 1.0.1

* Fri Jan 27 2012 Ian Weller <iweller@redhat.com> - 0.6.1-1
- Update to 0.6.1

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 21 2011 Ian Weller <iweller@redhat.com> - 0.6.0-2
- RHBZ 633102: Requires: python-setuptools

* Tue Nov 16 2010 Ian Weller <iweller@redhat.com> - 0.6.0-1
- Changed upstream (same code, new maintainer, new URL)
- New release

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Nov  9 2009 Ian Weller <ian@ianweller.org> - 0.4.2-2
- Add BR: python-setuptools
- Change URL to the correct upstream

* Sun Nov  8 2009 Ian Weller <ian@ianweller.org> - 0.4.2-1
- Initial package build
