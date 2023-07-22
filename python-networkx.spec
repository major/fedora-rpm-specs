%global _with_bootstrap 1
# There is a bootstrap loop between libpysal and networkx when tests/docs are
# enabled
%bcond_with     bootstrap

# Whether to build documentation and run tests
%if %{without bootstrap} && 0%{?rhel} == 0
%bcond_without  doctest
%else
%bcond_with     doctest
%endif

Name:           python-networkx
Version:        3.1
Release:        3%{?dist}
Summary:        Creates and Manipulates Graphs and Networks
License:        BSD-3-Clause
URL:            https://networkx.org/
Source0:        https://github.com/networkx/networkx/archive/networkx-%{version}.tar.gz
# Some examples cannot be executed, so expect them to fail.
# Examples that require network access:
# - football
# - plot_delaunay (via contextily)
# - plot_points (via contextily)
# Examples that require packages not available from Fedora:
# - osmnx requires osmnx
# - plot_lines requires momepy
Patch0:         %{name}-doc.patch

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  python3-devel

%if %{with doctest}
# Tests
BuildRequires:  %{py3_dist pytest-mpl}

# Documentation
BuildRequires:  python-pygraphviz-doc
BuildRequires:  python3-docs
BuildRequires:  python3-numpy-doc
BuildRequires:  %{py3_dist geopandas}
BuildRequires:  %{py3_dist libpysal}
BuildRequires:  sympy-doc
BuildRequires:  tex(latex)
BuildRequires:  tex-preview
%endif

%description
NetworkX is a Python package for the creation, manipulation, and
study of the structure, dynamics, and functions of complex networks.

%package -n python3-networkx
Summary:        Creates and Manipulates Graphs and Networks
Recommends:     xdg-utils

%description -n python3-networkx
NetworkX is a Python 3 package for the creation, manipulation, and
study of the structure, dynamics, and functions of complex networks.

%if %{with doctest}
%package doc
# The content is BSD-3-Clause.  Other licenses are due to files copied in by
# Sphinx.
# _static/_sphinx_javascript_frameworks_compat.js: BSD-2-Clause
# _static/basic.css: BSD-2-Clause
# _static/binder_badge_logo.svg: BSD-3-Clause
# _static/broken_example.png: BSD-3-Clause
# _static/copybutton.js
# _static/custom.css: BSD-3-Clause
# _static/doctools.js: BSD-2-Clause
# _static/documentation_options.js: BSD-2-Clause
# _static/file.png: BSD-2-Clause
# _static/jquery*.js: MIT
# _static/language_data.js: BSD-2-Clause
# _static/minus.png: BSD-2-Clause
# _static/no_image.png: BSD-3-Clause
# _static/opensearch.xml: BSD-2-Clause
# _static/plus.png: BSD-2-Clause
# _static/scripts/pydata-sphinx-theme.js: BSD-3-Clause
# _static/searchtools.js: BSD-2-Clause
# _static/sg_gallery.css: BSD-3-Clause
# _static/sg_gallery-binder.css: BSD-3-Clause
# _static/sg_gallery-dataframe.css: BSD-3-Clause
# _static/sg_gallery-rendered-html.css: BSD-3-Clause
# _static/sphinx_highlight.js: BSD-2-Clause
# _static/styles/pydata-sphinx-theme.css: BSD-3-Clause
# _static/styles/theme.css: BSD-3-Clause
# _static/underscore*.js: MIT
# genindex.html: BSD-2-Clause
# search.html: BSD-2-Clause
# searchindex.js: BSD-2-Clause
License:        BSD-3-Clause AND BSD-2-Clause AND MIT
Summary:        Documentation for networkx
Requires:       fontawesome-fonts-all
Provides:       bundled(js-jquery)
Provides:       bundled(js-underscore)

%description doc
Documentation for networkx

%pyproject_extras_subpkg -n python3-networkx extra
%endif

%prep
%autosetup -p0 -n networkx-networkx-%{version}

%if %{with doctest}
# Use local objects.inv for intersphinx
sed -e 's|\("https://docs\.python\.org/3/", \)None|\1"%{_docdir}/python3-docs/html/objects.inv"|' \
    -e 's|\("https://numpy\.org/doc/stable/", \)None|\1"%{_docdir}/python3-numpy-doc/objects.inv"|' \
    -e 's|\("https://pygraphviz.github.io/documentation/stable/", \)None|\1"%{_docdir}/python-pygraphviz/html/objects.inv"|' \
    -e 's|\("https://docs.sympy.org/latest/", \)None|\1"%{_docdir}/sympy-doc/html/objects.inv"|' \
    -i doc/conf.py
%endif

# Permit older versions of doc packages where Fedora is behind
sed -e 's/\(sphinx>=\)6\.1/\15.3/' \
    -e 's/\(sphinx-gallery>=\)0\.12/\10.11/' \
    -e 's/\(numpydoc>=1.\)5/\14/' \
    -i requirements/doc.txt

# Permit older versions of example packages where Fedora is behind
sed -e 's/\(seaborn>=0\.1\)2/\11/' \
    -e 's/\(cairocffi>=1\.\)4/\13/' \
    -i requirements/example.txt

# Fedora does not have osmnx or momepy
sed -i '/osmnx/d;/momepy/d' requirements/example.txt

%generate_buildrequires
%if %{with doctest}
%pyproject_buildrequires -x doc,extra,test requirements/example.txt
%else
%pyproject_buildrequires
%endif

%build
%pyproject_wheel

%if %{with doctest}
# Build the documentation
PYTHONPATH=$PWD/build/lib make -C doc html
rst2html --no-datestamp README.rst README.html
%endif

%install
%pyproject_install
%pyproject_save_files networkx
mv %{buildroot}%{_docdir}/networkx-%{version} ./installed-docs
rm -f installed-docs/INSTALL.txt

%if %{with doctest}
# Repack uncompressed zip archives
for fil in $(find doc/build -name \*.zip); do
  mkdir zip
  cd zip
  unzip ../$fil
  zip -9r ../$fil .
  cd ..
  rm -fr zip
done
%endif

%check
%if %{with doctest}
%pytest
%else
%pyproject_check_import -e '*.tests.*' -e '*.conftest'
%endif

%files -n python3-networkx -f %{pyproject_files}
%if %{with doctest}
%doc README.html installed-docs/*
%endif

%if %{with doctest}
%files doc
%doc doc/build/html/*
%endif

%changelog
* Thu Jul 20 2023 Python Maint <python-maint@redhat.com> - 3.1-3
- Rebuilt for Python 3.12

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.1-2
- Bootstrap for Python 3.12

* Fri Apr  7 2023 Jerry James <loganjerry@gmail.com> - 3.1-1
- Version 3.1
- Drop obsolete test patch
- Dynamically generate python dependencies

* Thu Mar 30 2023 Jerry James <loganjerry@gmail.com> - 2.8.8-3
- Add "extra" extras subpackage
- Simplify conditionals

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 13 2022 Jerry James <loganjerry@gmail.com> - 2.8.8-1
- Version 2.8.8
- Clarify license of the doc subpackage

* Sat Oct  1 2022 Jerry James <loganjerry@gmail.com> - 2.8.7-1
- Version 2.8.7
- Drop upstreamed matplotlib patch

* Wed Aug 31 2022 Jerry James <loganjerry@gmail.com> - 2.8.6-2
- Add patch to adapt an example to matplotlib 3.6.0

* Mon Aug 22 2022 Jerry James <loganjerry@gmail.com> - 2.8.6-1
- Version 2.8.6
- Convert License tag to SPDX

* Tue Aug  2 2022 Jerry James <loganjerry@gmail.com> - 2.8.5-1
- Version 2.8.5
- Add -test patch to work around a test failure

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 23 2022 Python Maint <python-maint@redhat.com> - 2.8.3-3
- Rebuilt for Python 3.11

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 2.8.3-2
- Bootstrap for Python 3.11

* Wed Jun  8 2022 Jerry James <loganjerry@gmail.com> - 2.8.3-1
- Version 2.8.3

* Wed May 18 2022 Jerry James <loganjerry@gmail.com> - 2.8.1-1
- Version 2.8.1

* Wed Apr 20 2022 Jerry James <loganjerry@gmail.com> - 2.8-1
- Version 2.8
- Bring back the doc subpackage

* Tue Mar 29 2022 Jerry James <loganjerry@gmail.com> - 2.7.1-1
- Version 2.7.1
- Do not build documentation by default
- Reorganize BRs and Rs by type (extras, tests, docs, etc.)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Oct 29 2021 Jerry James <loganjerry@gmail.com> - 2.6.3-2
- Change igraph dependency to match change in Rawhide
- Update project URL

* Fri Sep 10 2021 Jerry James <loganjerry@gmail.com> - 2.6.3-1
- Version 2.6.3

* Wed Aug 25 2021 Jerry James <loganjerry@gmail.com> - 2.6.2-1
- Version 2.6.2
- Drop upstreamed -pyyaml patch

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.5.1-3
- Rebuilt for Python 3.10

* Tue May  4 2021 Jerry James <loganjerry@gmail.com> - 2.5.1-2
- Allow use of decorator >= 5.0.7

* Tue Apr  6 2021 Jerry James <loganjerry@gmail.com> - 2.5.1-1
- Verion 2.5.1

* Tue Jan 26 2021 Jerry James <loganjerry@gmail.com> - 2.5-3
- Add -pyyaml patch to fix FTBFS

* Fri Dec 11 2020 Petr Lautrbach <plautrba@redhat.com> - 2.5-2
- Limit BuildRequires to necessary minimum in Red Hat Enterprise Linux
- Skip pytest in Red Hat Enterprise Linux
- Do not build -doc subpackage for Red Hat Enterprise Linux

* Sat Aug 22 2020 Jerry James <loganjerry@gmail.com> - 2.5-1
- Version 2.5
- All patches except -doc have been upstreamed; drop them

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4-4
- Rebuilt for Python 3.9

* Mon Mar  9 2020 Jerry James <loganjerry@gmail.com> - 2.4-3
- Add -deprecated and -arg-order patches to fix FTBFS with python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov  4 2019 Jerry James <loganjerry@gmail.com> - 2.4-1
- New upstream version
- Drop upstreamed patches: -is, -source-target, -union-find, -cb-iterable,
  -iterable, and -dict-iteration
- Unbundle fonts from the documentation
- Reenable the tests
- Add -test patch

* Wed Sep 11 2019 Jerry James <loganjerry@gmail.com> - 2.3-5
- Add -doc patch to fix building the gallery of examples
- Add -is patch to reduce noise in sagemath
- Add upstream bug fix patches: -source-target, -union-find, -cb-iterable,
  -iterable, and -dict-iteration

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 16 2019 Jerry James <loganjerry@gmail.com> - 2.3-2
- Merge the -test subpackage back into the main package (bz 1708372)

* Sat Apr 27 2019 Jerry James <loganjerry@gmail.com> - 2.3-1
- New upstream version
- Drop upstreamed -abc patch
- Add a -test subpackage (bz 1668197)
- Convert most Requires to Recommends (bz 1668197)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 30 2018 Jerry James <loganjerry@gmail.com> - 2.2-2
- Add -abc patch to quiet warnings

* Sat Oct 13 2018 Jerry James <loganjerry@gmail.com> - 2.2-1
- New upstream version (bz 1600361)
- Drop all patches
- Drop the python2 subpackages (bz 1634570)
- Figure out the BuildRequires all over again (bz 1576805)
- Consolidate BuildRequires so I can tell what is actually on the list
- Drop conditionals for RHEL < 8; this version can never appear there anyway
- Consolidate back to a single package for the same reason
- Temporarily disable tests due to multigraph bug in graphviz > 2.38

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.11-12
- Rebuilt for Python 3.7

* Fri May 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.11-11
- Update graphviz dependency for python2
- Drop graphviz dependency for python3 (graphviz doesn't support python3)

* Fri Mar 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.11-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 07 2017 Merlin Mathesius <mmathesi@redhat.com> - 1.11-8
- Cleanup spec file conditionals

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 23 2016 Orion Poplawski <orion@cora.nwra.com> - 1.11-5
- Add patch to fix sphinx build

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.11-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Apr 14 2016 Jerry James <loganjerry@gmail.com> - 1.11-3
- Change pydot dependencies to pydotplus (bz 1326957)

* Sat Apr  2 2016 Jerry James <loganjerry@gmail.com> - 1.11-2
- Fix gdal and pydot dependencies

* Sat Mar  5 2016 Jerry James <loganjerry@gmail.com> - 1.11-1
- New upstream version
- Drop upstreamed -numpy patch

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb  1 2016 Jerry James <loganjerry@gmail.com> - 1.10-1
- Comply with latest python packaging guidelines (bz 1301767)

* Tue Dec  1 2015 Jerry James <loganjerry@gmail.com> - 1.10-1
- New upstream version
- Update URLs
- Add -numpy patch to fix test failure

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Jerry James <loganjerry@gmail.com> - 1.9.1-3
- Note bundled jquery

* Tue Oct  7 2014 Jerry James <loganjerry@gmail.com> - 1.9.1-2
- Fix python3-networkx-drawing subpackage (bz 1149980)
- Fix python(3)-geo subpackage

* Mon Sep 22 2014 Jerry James <loganjerry@gmail.com> - 1.9.1-1
- New upstream version
- Fix license handling

* Thu Jul 10 2014 Jerry James <loganjerry@gmail.com> - 1.9-2
- BR python-setuptools

* Tue Jul  8 2014 Jerry James <loganjerry@gmail.com> - 1.9-1
- New upstream version
- Drop upstreamed -test-rounding-fix patch
- Upstream no longer bundles python-decorator; drop the workaround

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.8.1-13
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Thu Mar 13 2014 Pádraig Brady <pbrady@redhat.com> - 1.8.1-12
- Split to subpackages and support EL6 and EL7

* Thu Oct  3 2013 Jerry James <loganjerry@gmail.com> - 1.8.1-2
- Update project and source URLs

* Fri Aug  9 2013 Jerry James <loganjerry@gmail.com> - 1.8.1-1
- New upstream version

* Mon Jul 29 2013 Jerry James <loganjerry@gmail.com> - 1.8-1
- New upstream version
- Add tex-preview BR for documentation

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug  6 2012 Jerry James <loganjerry@gmail.com> - 1.7-1
- New upstream version

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 10 2012 Jerry James <loganjerry@gmail.com> - 1.6-2
- Mass rebuild for Fedora 17

* Mon Nov 28 2011 Jerry James <loganjerry@gmail.com> - 1.6-1
- New upstream version
- Do not use bundled python-decorator
- Remove Requires: ipython, needed by one example only
- Clean junk files left in /tmp

* Wed Jun 22 2011 Jerry James <loganjerry@gmail.com> - 1.5-1
- New upstream version
- Drop defattr
- Build documentation

* Sat Apr 23 2011 Jerry James <loganjerry@gmail.com> - 1.4-1
- New upstream version
- Build for both python2 and python3
- Drop BuildRoot, clean script, and clean at start of install script

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jan 20 2010 Conrad Meyer <konrad@tylerc.org> - 1.0.1-1
- Bump version to 1.0.1.
- License changed LGPLv2+ -> BSD.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 24 2009 Conrad Meyer <konrad@tylerc.org> - 0.99-3
- Replace __python macros with direct python invocations.
- Disable checks for now.
- Replace a define with global.

* Thu Mar 12 2009 Conrad Meyer <konrad@tylerc.org> - 0.99-2
- License is really LGPLv2+.
- Include license as documentation.
- Add a check section to run tests.

* Sat Dec 13 2008 Conrad Meyer <konrad@tylerc.org> - 0.99-1
- Initial package.
