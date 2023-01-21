%if 0%{?epel}
# disable build of docs and tests for epel because of missing dependencies:
# - python3-ipykernel
# - python3-jupyter-client
# - python3-nbformat
# - python3-testpath
# tests and docs subpackages are also disabled
%bcond_with check
%bcond_with doc
%else
%bcond_without check
%bcond_without doc
%endif

Name:           ipython
Version:        8.8.0
Release:        2%{?dist}
Summary:        An enhanced interactive Python shell

# See bug #603178 for a quick overview for the choice of licenses
# most files are under BSD and just a few under Python or MIT
# There are some extensions released under GPLv2+
License:        (BSD and MIT and Python) and GPLv2+
URL:            http://ipython.org/
Source0:        %pypi_source
Patch1:         relax-pytest-version-requirement.patch

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-stack-data

%if %{with doc}
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-ipykernel
BuildRequires:  python3-matplotlib
BuildRequires:  python3-numpy
BuildRequires:  python3-typing-extensions
%endif

%if %{with check}
BuildRequires:  python3-Cython
BuildRequires:  python3-matplotlib
BuildRequires:  python3-matplotlib-inline
BuildRequires:  python3-pymongo
BuildRequires:  python3-tornado >= 4.0
BuildRequires:  python3-zmq
BuildRequires:  python3-zmq-tests
BuildRequires:  python3-nbformat
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-ipykernel
BuildRequires:  python3-jupyter-client
BuildRequires:  python3-testpath
# for frontend
BuildRequires:  python3-pygments
# for latex
BuildRequires: /usr/bin/dvipng
BuildRequires: tex(amsmath.sty)
BuildRequires: tex(amssymb.sty)
BuildRequires: tex(amsthm.sty)
BuildRequires: tex(bm.sty)
%endif

%global ipython_desc_base \
IPython provides a replacement for the interactive Python interpreter with\
extra functionality.\
\
Main features:\
 * Comprehensive object introspection.\
 * Input history, persistent across sessions.\
 * Caching of output results during a session with automatically generated\
   references.\
 * Readline based name completion.\
 * Extensible system of 'magic' commands for controlling the environment and\
   performing many tasks related either to IPython or the operating system.\
 * Configuration system with easy switching between different setups (simpler\
   than changing $PYTHONSTARTUP environment variables every time).\
 * Session logging and reloading.\
 * Extensible syntax processing for special purpose situations.\
 * Access to the system shell with user-extensible alias system.\
 * Easily embeddable in other Python programs.\
 * Integrated access to the pdb debugger and the Python profiler.

%description
%{ipython_desc_base}

%package -n python3-ipython
Summary:        An enhanced interactive Python shell
%{?python_provide:%python_provide python3-ipython}
%{?python_provide:%python_provide python3-ipython-console}
Provides:       ipython3 = %{version}-%{release}
Provides:       ipython = %{version}-%{release}
Provides:       python3-ipython-console = %{version}-%{release}
Obsoletes:      python3-ipython-console < 5.3.0-1
Conflicts:      python2-ipython < 7

BuildRequires:  python3-backcall
BuildRequires:  python3-decorator
BuildRequires:  python3-jedi >= 0.10
BuildRequires:  python3-pexpect
BuildRequires:  python3-pickleshare
BuildRequires:  python3-prompt-toolkit >= 2
BuildRequires:  python3-traitlets >= 4.2
Requires:       (tex(amsmath.sty) if /usr/bin/dvipng)
Requires:       (tex(amssymb.sty) if /usr/bin/dvipng)
Requires:       (tex(amsthm.sty)  if /usr/bin/dvipng)
Requires:       (tex(bm.sty)      if /usr/bin/dvipng)

%description -n python3-ipython
%{ipython_desc_base}

This package provides IPython for in a terminal.

%{?python_extras_subpkg:%python_extras_subpkg -n python3-ipython -i %{python3_sitelib}/*.egg-info notebook}

%package -n python3-ipython-sphinx
Summary:        Sphinx directive to support embedded IPython code
%{?python_provide:%python_provide python3-ipython-sphinx}
Requires:       python3-ipython = %{version}-%{release}
BuildRequires:  python3-sphinx
Requires:       python3-sphinx

%description -n python3-ipython-sphinx
%{ipython_desc_base}

This package contains the ipython sphinx extension.

%if %{with check}
%package -n python3-ipython+test
Summary:        Tests for %{name}
Provides:       python3-ipython-tests = %{version}-%{release}
Obsoletes:      python3-ipython-tests < 8.7.0-2
%{?python_provide:%python_provide python3-ipython-tests}
%{?python_provide:%python_provide python3-ipython+test}
Requires:       python3-ipykernel
Requires:       python3-ipython = %{version}-%{release}
Requires:       python3-jupyter-client
Requires:       python3-nbformat
Requires:       python3-zmq-tests
# For latex
Requires:       /usr/bin/dvipng
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(bm.sty)

%description -n python3-ipython+test
This package contains the tests of %{name}.
You can check this way, if ipython works on your platform.
%endif

%if %{with doc}
%package -n python3-ipython-doc
Summary:        Documentation for %{name}
%{?python_provide:%python_provide python3-ipython-doc}
%description -n python3-ipython-doc
This package contains the documentation of %{name}.
%endif


%prep
%autosetup -p1

# delete bundling libs
pushd IPython/external
ls -l
ls -l *

popd

# Remove shebangs
sed -i '1d' $(grep -lr '^#!/usr/' IPython)

find . -name '*.py' -print0 | xargs -0 sed -i '1s|^#!python|#!%{__python3}|'

%build
%py3_build


%if %{with doc}
pushd docs
PYTHONPATH=.. make html SPHINXBUILD='sphinx-build-3 -D intersphinx_timeout=1'
mkdir -p build/html/
rm -rf build/html/.buildinfo
popd
%endif


%install
%py3_install

# link the manpage to ipython3
mv %{buildroot}%{_mandir}/man1/ipython{,3}.1
ln -s ./ipython3.1 %{buildroot}%{_mandir}/man1/ipython.1


%if %{with check}
%check
# Ensure that the user's .pythonrc.py is not invoked during any tests.
export PYTHONSTARTUP=""
# Koji builders can be slow, especially on arms, we scale timeouts 4 times
export IPYTHON_TESTING_TIMEOUT_SCALE=4
# To prevent _pytest.pathlib.ImportPathMismatchError, we are
# testing directly in buildroot
pushd %{buildroot}%{python3_sitelib}/IPython
%pytest
rm -rf .pytest_cache
popd
%else
rm -r %{buildroot}%{python3_sitelib}/IPython/*/tests
%endif

%files -n python3-ipython
%{_bindir}/ipython3
%{_bindir}/ipython
%{_mandir}/man1/ipython.*
%{_mandir}/man1/ipython3.*

%dir %{python3_sitelib}/IPython
%{python3_sitelib}/IPython/external
%{python3_sitelib}/IPython/__pycache__/
%{python3_sitelib}/IPython/*.py*
%{python3_sitelib}/IPython/py.typed
%dir %{python3_sitelib}/IPython/testing
%{python3_sitelib}/IPython/testing/__pycache__/
%{python3_sitelib}/IPython/testing/*.py*
%{python3_sitelib}/IPython/testing/plugin
%{python3_sitelib}/ipython-%{version}-py%{python3_version}.egg-info/

%{python3_sitelib}/IPython/core/
%{python3_sitelib}/IPython/extensions/
%{python3_sitelib}/IPython/lib/
%{python3_sitelib}/IPython/terminal/
%{python3_sitelib}/IPython/utils/

# tests go into subpackage
%exclude %{python3_sitelib}/IPython/*/tests/


%files -n python3-ipython-sphinx
%{python3_sitelib}/IPython/sphinxext/

%if %{with check}
%files -n python3-ipython+test
%ghost %{python3_sitelib}/ipython-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/IPython/*/tests
%endif

%if %{with doc}
%files -n python3-ipython-doc
%doc docs/build/html
%endif


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 05 2023 Lumír Balhar <lbalhar@redhat.com> - 8.8.0-1
- Update to 8.8.0 (rhbz#2158352)

* Wed Dec  7 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 8.7.0-2
- Rename tests subpackage to fix auto provides

* Tue Nov 29 2022 Lumír Balhar <lbalhar@redhat.com> - 8.7.0-1
- Update to 8.7.0 (rhbz#2149289)

* Wed Nov 23 2022 Lumír Balhar <lbalhar@redhat.com> - 8.6.0-1
- Update to 8.6.0 (rhbz#2138766)

* Thu Sep 08 2022 Lumír Balhar <lbalhar@redhat.com> - 8.5.0-1
- Update to 8.5.0
Resolves: rhbz#2124923

* Fri Jul 29 2022 Lumír Balhar <lbalhar@redhat.com> - 8.4.0-5
- Fix FTBFS with Python 3.11b4

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 8.4.0-3
- Rebuilt for Python 3.11

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 8.4.0-2
- Bootstrap for Python 3.11

* Tue May 31 2022 Lumír Balhar <lbalhar@redhat.com> - 8.4.0-1
- Update to 8.4.0
Resolves: rhbz#2091308

* Fri Apr 29 2022 Lumír Balhar <lbalhar@redhat.com> - 8.3.0-1
- Update to 8.3.0
Resolves: rhbz#2080476

* Mon Mar 28 2022 Lumír Balhar <lbalhar@redhat.com> - 8.2.0-1
- Update to 8.2.0
Resolves: rhbz#2068891

* Tue Mar 08 2022 Lumír Balhar <lbalhar@redhat.com> - 8.1.1-1
- Update to 8.1.1
Resolves: rhbz#2060917

* Sat Feb 26 2022 Lumír Balhar <lbalhar@redhat.com> - 8.1.0-1
- Update to 8.1.0
Resolves: rhbz#2058882

* Mon Jan 24 2022 Lumír Balhar <lbalhar@redhat.com> - 8.0.1-1
- Update to 8.0.1
Resolves: rhbz#2042793

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.30.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 03 2021 Lumír Balhar <lbalhar@redhat.com> - 7.30.1-1
- Update to 7.30.1
Resolves: rhbz#2027069

* Mon Nov 01 2021 Lumír Balhar <lbalhar@redhat.com> - 7.29.0-1
- Update to 7.29.0
Resolves: rhbz#2018636

* Tue Oct 05 2021 Lumír Balhar <lbalhar@redhat.com> - 7.28.0-1
- Update to 7.28.0
Resolves: rhbz#2007824

* Mon Aug 30 2021 Lumír Balhar <lbalhar@redhat.com> - 7.27.0-1
- Update to 7.27.0
Resolves: rhbz#1998766

* Wed Aug 04 2021 Lumír Balhar <lbalhar@redhat.com> - 7.26.0-2
- Fix compatibility with Python 3.10rc1

* Mon Aug 02 2021 Lumír Balhar <lbalhar@redhat.com> - 7.26.0-1
- Update to 7.26.0
Resolves: rhbz#1988914

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.25.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 28 2021 Lumír Balhar <lbalhar@redhat.com> - 7.25.0-1
- Update to 7.25.0
Resolves: rhbz#1976438

* Fri Jun 11 2021 Lumír Balhar <lbalhar@redhat.com> - 7.24.1-1
- Update to 7.24.1
Resolves: rhbz#1967545

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 7.24.0-3
- Rebuilt for Python 3.10

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 7.24.0-2
- Bootstrap for Python 3.10

* Mon May 31 2021 Lumír Balhar <lbalhar@redhat.com> - 7.24.0-1
- Update to 7.24.0
Resolves: rhbz#1965746

* Tue May 04 2021 Lumír Balhar <lbalhar@redhat.com> - 7.23.1-1
- Update to 7.23.1
Resolves: rhbz#1955903

* Mon Mar 29 2021 Karolina Surma <ksurma@redhat.com> - 7.22.0-1
- Update to 7.22.0
Resolves: rhbz#1943788

* Sun Feb 28 2021 Lumír Balhar <lbalhar@redhat.com> - 7.21.0-1
- Update to 7.21.0
Resolves: rhbz#1933409

* Wed Feb 10 2021 Lumír Balhar <lbalhar@redhat.com> - 7.20.0-2
- Fix tests with Python 3.10.0a5

* Tue Feb 02 2021 Lumír Balhar <lbalhar@redhat.com> - 7.20.0-1
- Fix tests with Python 3.10.0a4
Resolves: rhbz#1901141
- Update to 7.20.0
Resolves: rhbz#1923782

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 13 2020 Lumír Balhar <lbalhar@redhat.com> - 7.19.0-1
- Update to 7.19.0 (#1893413)

* Tue Sep 08 2020 Lumír Balhar <lbalhar@redhat.com> - 7.18.1-1
- Update to 7.18.1 (#1873693)

* Mon Aug 31 2020 Lumír Balhar <lbalhar@redhat.com> - 7.18.0-1
- Update to 7.18.0 (#1873693)

* Tue Aug 04 2020 Lumír Balhar <lbalhar@redhat.com> - 7.17.0-1
- Update to 7.17.0 (#1862672)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.16.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Miro Hrončok <mhroncok@redhat.com> - 7.16.1-2
- Add ipython[notebook] subpackage

* Tue Jul 07 2020 Lumír Balhar <lbalhar@redhat.com> - 7.16.1-1
- Update to 7.16.1 (#1851577)

* Wed Jun 03 2020 Miro Hrončok <mhroncok@redhat.com> - 7.15.0-2
- Switch to runtime requires generated from upstream metadata
- Drop unused (Build)Requires

* Mon Jun 01 2020 Lumír Balhar <lbalhar@redhat.com> - 7.15.0-1
- Update to 7.15.0 (#1841983)

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 7.14.0-6
- Rebuilt for Python 3.9

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 7.14.0-5
- Bootstrap for Python 3.9

* Thu May 21 2020 Lumír Balhar <lbalhar@redhat.com> - 7.14.0-4
- Explicit tex dependencies for latextools (#1838474)

* Wed May 20 2020 Lumír Balhar <lbalhar@redhat.com> - 7.14.0-3
- Remove tests not compatible with Python 3.9.0b1 (#1837372)

* Tue May 05 2020 Lumír Balhar <lbalhar@redhat.com> - 7.14.0-2
- Remove tests not compatible with Python 3.9.0a6 (#1831182)

* Mon May 04 2020 Lumír Balhar <lbalhar@redhat.com> - 7.14.0-1
- Update to 7.14.0 (#1830483)

* Tue Apr 14 2020 Lumír Balhar <lbalhar@redhat.com> - 7.13.0-2
- Fix compatibility with Sphinx 3.0.0

* Wed Mar 04 2020 Lumír Balhar <lbalhar@redhat.com> - 7.13.0-1
- Update to 7.13.0 (#1808624)

* Mon Feb 10 2020 Lumír Balhar <lbalhar@redhat.com> - 7.12.0-1
- Update to 7.12.0 (#1797183)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Lumír Balhar <lbalhar@redhat.com> - 7.11.1-1
- Update to 7.11.1 (#1786893)

* Mon Dec 16 2019 Lumír Balhar <lbalhar@redhat.com> - 7.10.2-1
- Update to 7.10.2 (#1777612)

* Tue Nov 19 2019 Lumír Balhar <lbalhar@redhat.com> - 7.9.0-1
- Update to 7.9.0 (#1765760)

* Mon Sep 02 2019 Lumír Balhar <lbalhar@redhat.com> - 7.8.0-1
- Update to 7.8.0 (#1742354)

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 7.6.1-4
- Rebuilt for Python 3.8

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 7.6.1-3
- Bootstrap for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 2019 Miro Hrončok <mhroncok@redhat.com> - 7.6.1-1
- Update to 7.6.1 (#1725333)

* Tue May 21 2019 Miro Hrončok <mhroncok@redhat.com> - 7.5.0-1
- Update to 7.5.0 (#1678562)

* Tue Apr 09 2019 Miro Hrončok <mhroncok@redhat.com> - 7.4.0-1
- Update to 7.4.0 (#1678562)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 02 2019 David Cantrell <dcantrell@redhat.com> - 7.2.0-1
- Upgrade to 7.2.0 (#1662990)

* Wed Oct 03 2018 Miro Hrončok <mhroncok@redhat.com> - 7.0.1-1
- Update to 7.0.1 (#1610063)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 Miro Hrončok <mhroncok@redhat.com> - 6.4.0-3
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 6.4.0-2
- Bootstrap for Python 3.7

* Fri May 11 2018 Miro Hrončok <mhroncok@redhat.com> - 6.4.0-1
- Update to 6.4.0 (#1577182)
- Stop running the tests in xvfb (not needed since 5.x)

* Tue Apr 10 2018 Miro Hrončok <mhroncok@redhat.com> - 6.3.1-1
- Update to 6.3.1 (#1563215)

* Wed Apr 04 2018 Miro Hrončok <mhroncok@redhat.com> - 6.3.0-1
- Update to 6.3.0 (#1563215)
- Require numpy at least from the tests package (#1440518)
- Sort dependencies, remove unused

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 01 2017 Miro Hrončok <mhroncok@redhat.com> - 6.2.1-1
- Update to 6.2.1 (#1497372)

* Sat Sep 16 2017 Miro Hrončok <mhroncok@redhat.com> - 6.2.0-1
- Update to 6.2.0 (#1492256)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 01 2017 Miro Hrončok <mhroncok@redhat.com> - 6.1.0-1
- Update to 6.1.0 (#1457581)

* Fri Apr 21 2017 Miro Hrončok <mhroncok@redhat.com> - 6.0.0-1
- Update to 6.0.0 final

* Tue Apr 11 2017 Miro Hrončok <mhroncok@redhat.com> - 6.0.0-0.1.rc1
- Update to 6.0.0rc1
- Drop Python 2 (unsupported)

* Fri Mar 17 2017 Miro Hrončok <mhroncok@redhat.com> - 5.3.0-4
- Provide ipython2/3

* Fri Mar 17 2017 Miro Hrončok <mhroncok@redhat.com> - 5.3.0-3
- Remove bogus shebangs

* Wed Mar 15 2017 Miro Hrončok <mhroncok@redhat.com> - 5.3.0-2
- Also require traitlets

* Wed Mar 08 2017 Tomas Orsava <torsava@redhat.com> - 5.3.0-1
- Updated to 5.3.0
- Removed the gui and notebook subpackages as they are now distributed
  separately (packages python-qtconsole and python-notebook respectively)
- Binaries ipcluster, ipcontroller and ipengine no longer exist
- Removed all patches (0-2)
- Modified check section to fail the build upon test failures
- Fixed building of documentation
- Removed the pythonX-ipython-console subpackages, the functionality is now
  provided by the pythonX-ipython packages themselves

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 02 2017 Thomas Spura <tomspur@fedoraproject.org> - 3.2.1-11
- rename python-* packages to python2-* (#1409249)
- remove group tag

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.2.1-10
- Rebuild for Python 3.6

* Mon Sep 26 2016 Dominik Mierzejewski <rpm@greysector.net> - 3.2.1-9
- rebuilt for matplotlib-2.0.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Oct 9 2015 Orion Poplawski <orion@cora.nwra.com> - 3.2.1-5
- Require python-pexpect in Fedora

* Fri Sep 25 2015 Orion Poplawski <orion@cora.nwra.com> - 3.2.1-4
- Own IPython/html directory

* Thu Sep 17 2015 Orion Poplawski <orion@cora.nwra.com> - 3.2.1-3
- Add upstream patch to fix file execution vulnerability (bug #1264068)

* Wed Sep 2 2015 Orion Poplawski <orion@cora.nwra.com> - 3.2.1-2
- Add upstream patch to fix XSS vulnerability (bug #1259405)

* Mon Jul 13 2015 Orion Poplawski <orion@cora.nwra.com> - 3.2.1-1
- Update to 3.2.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 8 2015 Orion Poplawski <orion@cora.nwra.com> - 3.1.0-3
- Use python2 macros
- Fix python3 shebang fix

* Thu May 7 2015 Orion Poplawski <orion@cora.nwra.com> - 3.1.0-2
- Do not ship notebook on EL, missing python-tornado >= 4.0
- Move IPython/html/static/custom into -console.

* Sat Apr 25 2015 Orion Poplawski <orion@cora.nwra.com> - 3.1.0-1
- Update to 3.1.0
- Add BR/R on mistune
- Drop BR/R on jsonpointer
- Drop fabric

* Thu Feb 26 2015 Orion Poplawski <orion@cora.nwra.com> - 2.4.1-1
- update to 2.4.1

* Wed Feb 25 2015 Orion Poplawski <orion@cora.nwra.com> - 2.4.0-1
- update to 2.4.0

* Fri Nov 14 2014 Orion Poplawski <orion@cora.nwra.com> - 2.3.0-1
- update to 2.3.0

* Thu Aug  7 2014 Thomas Spura <tomspur@fedoraproject.org> - 2.2.0-1
- update to 2.2.0

* Sun Jul 27 2014 Thomas Spura <tomspur@fedoraproject.org> - 2.1.0-7
- Replace python3 shebang with python2 one (#1123618)

* Sun Jul  6 2014 Thomas Spura <tomspur@fedoraproject.org> - 2.1.0-6
- port ipython to fontawesome-4 and regenerate css in build (#1006575)

* Mon Jun 23 2014 Thomas Spura <tomspur@fedoraproject.org> - 2.1.0-5
- use mathjax from _jsdir instead of cdn
- enable python3 tests

* Wed Jun 18 2014 Thomas Spura <tomspur@fedoraproject.org> - 2.1.0-4
- BR/R same fonts for python{,3}-ipython-notebook (#1006575)
- require tornado >= 3.1.0 (#1006575)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jun  1 2014 Thomas Spura <tomspur@fedoraproject.org> - 2.1.0-2
- package part of notebook in main package (#1103423)
- add BR python-sphinx

* Fri May 30 2014 Thomas Spura <tomspur@fedoraproject.org> - 2.1.0-1
- update to 2.1.0
- Unbundle js-marked
- Add provides for bundled exception fpc#416
- Add BR Cython
- disable python3 tests for now (possible blocking in koji)
- Add BR python-pexpect

* Fri May 30 2014 Thomas Spura <tomspur@fedoraproject.org> - 2.0.0-2
- add BR/R python-path
- fix python -> python3 sed replacement
- fix running testsuite
- fix %%files
- Unbundle js-highlight

* Fri May 30 2014 Thomas Spura <tomspur@fedoraproject.org> - 2.0.0-1
- update to 2.0.0
- bundled argparse has been dropped
- unbundle fontawesome-fonts{,-web}
- unbundle nodejs-requirejs
- unbundle nodejs-underscore
- unbundle nodejs-highlight-js

* Fri May 30 2014 Thomas Spura <tomspur@fedoraproject.org> - 1.1.0-1
- update to 1.1.0
- drop both patches (upstream)
- add python-ipython-sphinx packages
- remove %%defattr
- rename run_testsuite to check
- building docs (currently fails with an ascii error)
- unbundle jsonschema
- unbundle decorator

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 0.13.2-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Oct  7 2013 Thomas Spura <tomspur@fedoraproject.org> - 0.13.2-3
- install into unversioned docdir (#993848)
- R on setuptools for starting with pkg_resources (#994673)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 10 2013 Thomas Spura <tomspur@fedoraproject.org> - 0.13.2-2
- Improve package descriptions (#950530)

* Sat Apr  6 2013 Thomas Spura <tomspur@fedoraproject.org> - 0.13.2-1
- update to 0.13.2 fixes #927169, #947633
- run tests in xvfb
- reword description of ipython-tests a bit

* Thu Feb 21 2013 Thomas Spura <tomspur@fedoraproject.org> - 0.13.1-4
- More changes to build for Python 3 (mostly by Andrew McNabb, #784947)
- Update package structure of python3-ipython subpackage to match python2-ipython one's
- enable python3 build of ipython
- exclude pylab tests for now, as it is broken on python3

* Thu Feb 21 2013 Thomas Spura <tomspur@fedoraproject.org> - 0.13.1-3
- obsolete old python packages (José Matos, #882724)
- notebook and gui subpackage require matplotlib not the console anymore (#872176)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 24 2012 Thomas Spura <tomspur@fedoraproject.org> - 0.13.1-1
- update to 0.13.1 (#838031)
- run tests with en_US.UTF-8

* Thu Aug 30 2012 Thomas Spura <tomspur@fedoraproject.org> - 0.13-5
- add empty python-ipython files section
- obsolete ipython

* Wed Aug  8 2012 Thomas Spura <tomspur@fedoraproject.org> - 0.13-4
- use versioned requires/provides on ipython

* Sat Aug  4 2012 Thomas Spura <tomspur@fedoraproject.org> - 0.13-3
- use python-foo for python2-foo and provide ipython-foo

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 30 2012 Thomas Spura <tomspur@fedoraproject.org> - 0.13-1
- update to new version
- R on mglob/pyparsing is obsolete
- remove patch, as it's upstream

* Fri Jan 27 2012 Thomas Spura <tomspur@fedoraproject.org> - 0.12-3
- skip no X tests
- continue with python3 support

* Sun Jan  8 2012 Thomas Spura <tomspur@fedoraproject.org> - 0.12-2
- add missing R tornado
- add _bindir to PATH to more tests pass in koji

* Mon Dec 19 2011 Thomas Spura <tomspur@fedoraproject.org> - 0.12-1
- update to new version
- bcond_without run_testsuite

* Sun Oct 23 2011 Thomas Spura <tomspur@fedoraproject.org> - 0.11-3
- add more missing R (matplotlib and pygments) (#748141)

* Tue Sep 20 2011 Michel Salim <salimma@fedoraproject.org> - 0.11-2
- make -gui subpackage depend on PyQt4, not PyQt

* Mon Jul  4 2011 Thomas Spura <tomspur@fedoraproject.org> - 0.11-1
- update to 0.11
- patches included upstream
- ipython changed bundled pretty, so redistributes it in lib now
- run testsuite
- new upstream url

* Sat Apr  9 2011 Thomas Spura <tomspur@fedoraproject.org> - 0.10.2-1
- update to new version
- patch3 is included upstream
- fixes #663823, #649281

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 15 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.10.1-3
- add fix for #646079 and use upstream fix for #628742

* Mon Oct 18 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.10.1-2
- argparse is in python 2.7 and 3.2

* Wed Oct 13 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.10.1-1
- unbundle a bit differently
- update to new version

* Tue Aug 31 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.10-8
- pycolor: wrong filename -> no crash (#628742)

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Jul 19 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.10-6
- add missing dependencies: pexpect and python-argparse

* Tue Jun 22 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.10-5
- two more unbundled libraries in fedora

* Mon Jun 21 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.10-4
- Update patch for import in argparse

* Fri Jun 11 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.10-3
- fix license tag (#603178)
- add requires on wxpython to gui subpackage (#515570)
- start unbundling the libraries - more to come (#603937)

* Tue Apr 13 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.10-2
- move docs into a subpackage
- subpackage wxPython
- subpackage tests
- use proper %%{python_site*} definitions
- make %%{files} more explicit
- add some missing R (fixes #529185, #515570)

* Tue Sep 22 2009 James Bowes <jbowes@redhat.com> - 0.10-1
- Update to 0.10

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 04 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.9.1-2
- Rebuild for Python 2.6

* Tue Dec 02 2008 James Bowes <jbowes@redhat.com> - 0.9.1-1
- Update to 0.9.1, specfile changes courtesy Greg Swift

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.8.4-2
- Rebuild for Python 2.6

* Wed Jun 11 2008 James Bowes <jbowes@redhat.com> - 0.8.4-1
- Update to 0.8.4

* Fri May 30 2008 James Bowes <jbowes@redhat.com> - 0.8.3-1
- Update to 0.8.3

* Wed Dec 12 2007 James Bowes <jbowes@redhat.com> - 0.8.2-1
- Update to 0.8.2

* Sun Aug 05 2007 James Bowes <jbowes@redhat.com> - 0.8.1-2
- Remove explicit requires on python-abi.

* Sun Aug 05 2007 James Bowes <jbowes@redhat.com> - 0.8.1-1
- Update to 0.8.1

* Thu Dec 14 2006 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.7.2-4
- Rebuild for new Python

* Sat Sep 16 2006 Shahms E. King <shahms@shahms.com> - 0.7.2-3
- Rebuild for FC6

* Fri Aug 11 2006 Shahms E. King <shahms@shahms.com> - 0.7.2-2
- Include, don't ghost .pyo files per new guidelines

* Mon Jun 12 2006 Shahms E. King <shahms@shahms.com> - 0.7.2-1
- Update to new upstream version

* Mon Feb 13 2006 Shahms E. King <shahms@shahms.com> - 0.7.1.fix1-2
- Rebuild for FC-5

* Mon Jan 30 2006 Shahms E. King <shahms@shahms.com> - 0.7.1.fix1-1
- New upstream 0.7.1.fix1 which fixes KeyboardInterrupt handling

* Tue Jan 24 2006 Shahms E. King <shahms@shahms.com> - 0.7.1-1
- Update to new upstream 0.7.1

* Thu Jan 12 2006 Shahms E. King <shahms@shahms.com> - 0.7-1
- Update to new upstream 0.7.0

* Mon Jun 13 2005 Shahms E. King <shahms@shahms.com> - 0.6.15-1
- Add dist tag
- Update to new upstream (0.6.15)

* Wed Apr 20 2005 Shahms E. King <shahms@shahms.com> - 0.6.13-2
- Fix devel release number

* Mon Apr 18 2005 Shahms E. King <shahms@shahms.com> - 0.6.13-1
- Update to new upstream version

* Fri Apr  1 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.6.12-2
- Include IPython Extensions and UserConfig directories.

* Fri Mar 25 2005 Shahms E. King <shahms@shahms.com> - 0.6.12-1
- Update to 0.6.12
- Removed unused python_sitearch define

* Tue Mar 01 2005 Shahms E. King <shahms@shahms.com> - 0.6.11-2
- Fix up %%doc file specifications
- Use offical .tar.gz, not upstream .src.rpm .tar.gz

* Tue Mar 01 2005 Shahms E. King <shahms@shahms.com> - 0.6.11-1
- Initial release to meet Fedora packaging guidelines
