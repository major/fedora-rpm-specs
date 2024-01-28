%if %{?fedora}%{!?fedora:0} < 38
# python3-ipython-tests lacks auto-generated provides in Fedora < 38
%global __requires_exclude python.*dist\\(ipython\\[test\\]\\)
%endif

Name:		python-ipyparallel
Version:	8.6.1
Release:	6%{?dist}
Summary:	Interactive Parallel Computing with IPython

License:	BSD-3-Clause
URL:		https://github.com/ipython/ipyparallel
Source0:	%pypi_source ipyparallel
#		https://github.com/ipython/ipyparallel/pull/795
Patch0:		%{name}-doc-fixes.patch
#		https://github.com/ipython/ipyparallel/pull/796
Patch1:		%{name}-teardown.patch
Patch2:		https://github.com/ipython/ipyparallel/pull/818.patch#/%{name}-assert_called_once_with.patch

BuildArch:	noarch
BuildRequires:	make
BuildRequires:	python3-devel >= 3.7
BuildRequires:	python3-pip
BuildRequires:	python3dist(hatchling) >= 0.25
BuildRequires:	python3dist(entrypoints)
BuildRequires:	python3dist(decorator)
BuildRequires:	python3dist(pyzmq) >= 18
BuildRequires:	python3dist(traitlets) >= 4.3
BuildRequires:	python3dist(ipython) >= 4
BuildRequires:	python3dist(jupyter-client)
BuildRequires:	python3dist(ipykernel) >= 4.4
BuildRequires:	python3dist(tornado) >= 5.1
BuildRequires:	python3dist(psutil)
BuildRequires:	python3dist(python-dateutil) >= 2.1
BuildRequires:	python3dist(tqdm)
#		For testing:
BuildRequires:	python3dist(pytest)
BuildRequires:	python3dist(pytest-asyncio)
BuildRequires:	python3-zmq-tests
#		For documentation
BuildRequires:	python3dist(sphinx)
BuildRequires:	python3-ipython-sphinx
BuildRequires:	python3dist(matplotlib)
BuildRequires:	python3dist(myst-parser)
BuildRequires:	python3dist(nbsphinx)
BuildRequires:	python3dist(pydata-sphinx-theme)
BuildRequires:	pandoc

%description
IPython Parallel (ipyparallel) is a Python package and collection of
CLI scripts for controlling clusters of IPython processes, built on
the Jupyter protocol.

%package -n python3-ipyparallel
Summary:	Interactive Parallel Computing with IPython
%py_provides	python3-ipyparallel
Requires:	python-jupyter-filesystem >= 4.7.0-5

%description -n python3-ipyparallel
IPython Parallel (ipyparallel) is a Python package and collection of
CLI scripts for controlling clusters of IPython processes, built on
the Jupyter protocol.

%package -n python3-ipyparallel+test
Summary:	Tests for python3-ipyparallel
%py_provides	python3-ipyparallel+test
%py_provides	python3-ipyparallel-tests
Obsoletes:	python3-ipyparallel-tests < 8.4.1-3
Requires:	python3-ipyparallel = %{version}-%{release}
Requires:	python3-zmq-tests

%description -n python3-ipyparallel+test
This package contains the tests of python3-ipyparallel.

%package doc
Summary:	Documentation for python-ipyparallel

%description doc
This package contains the documentation of python-ipyparallel.

%prep
%setup -q -n ipyparallel-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

rm ipyparallel/labextension/schemas/ipyparallel-labextension/package.json.orig

sed /autodoc_traits/d -i docs/source/conf.py
sed s/autoconfigurable/autoclass/ -i docs/source/api/ipyparallel.rst

# Adjust test expectations for our build environment
sed -i 's/\[Errno -2\] Name or service not known/[Errno -3] Temporary failure in name resolution/' ipyparallel/tests/test_util.py

%build
%pyproject_wheel

pushd docs
PYTHONPATH=${PWD}/.. make html
rm -f build/html/.buildinfo
popd

%install
%pyproject_install

for f in apps/iploggerapp.py cluster/app.py controller/app.py \
	 controller/heartmonitor.py engine/app.py ; do
  sed '/\/usr\/bin\/env/d' -i %{buildroot}%{python3_sitelib}/ipyparallel/${f}
done

# Fix wrong install directory for configuraton files
mv %{buildroot}%{_prefix}%{_sysconfdir} %{buildroot}%{_sysconfdir}

%check
%pytest -Wdefault -v --color=no

%files -n python3-ipyparallel
%license COPYING.md
%doc README.md
%{python3_sitelib}/ipyparallel-*.*-info
%dir %{python3_sitelib}/ipyparallel
%{python3_sitelib}/ipyparallel/*.py
%{python3_sitelib}/ipyparallel/__pycache__
%{python3_sitelib}/ipyparallel/apps
%{python3_sitelib}/ipyparallel/client
%{python3_sitelib}/ipyparallel/cluster
%{python3_sitelib}/ipyparallel/controller
%{python3_sitelib}/ipyparallel/engine
%{python3_sitelib}/ipyparallel/labextension
%{python3_sitelib}/ipyparallel/nbextension
%{python3_sitelib}/ipyparallel/serialize
%{_bindir}/ipcluster
%{_bindir}/ipcontroller
%{_bindir}/ipengine
%{_datadir}/jupyter/labextensions/ipyparallel-labextension
%{_datadir}/jupyter/nbextensions/ipyparallel
%config(noreplace) %{_sysconfdir}/jupyter/jupyter_notebook_config.d/ipyparallel.json
%config(noreplace) %{_sysconfdir}/jupyter/jupyter_server_config.d/ipyparallel.json
%config(noreplace) %{_sysconfdir}/jupyter/nbconfig/tree.d/ipyparallel.json

%files -n python3-ipyparallel+test
%ghost %{python3_sitelib}/ipyparallel-*.*-info
%{python3_sitelib}/ipyparallel/tests

%files doc
%license COPYING.md
%doc docs/build/html

%changelog
* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 8.6.1-3
- Rebuilt for Python 3.12

* Sat Apr 15 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 8.6.1-2
- Fix AttributeError in tests

* Fri Apr 14 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 8.6.1-1
- Update to 8.6.1

* Thu Mar 30 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 8.5.1-1
- Update to 8.5.1
- Use source from PyPI

* Sat Mar 18 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 8.5.0-1
- Update to 8.5.0
- Drop patches (accepted upstream)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 03 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 8.4.1-3
- Rename tests subpackage to fix auto provides
- Ignore deprecation warnings from jupyter-core

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 26 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 8.4.1-1
- Update to 8.4.1
- Drop python 3.11 patch (accepted upstream)
- Use the pyproject rpm macros

* Thu Jun 23 2022 Miro Hrončok <mhroncok@redhat.com> - 8.2.1-3
- Build with pydata-sphinx-theme again

* Mon Jun 20 2022 Tomáš Hrnčiar <thrnciar@redhat.com> - 8.2.1-2
- Add patch for Python 3.11 compatibility

* Tue Apr 05 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 8.2.1-1
- Update to 8.2.1

* Mon Feb 07 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 8.2.0-1
- Update to 8.2.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 23 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 8.1.0-1
- Update to 8.1.0

* Mon Nov 15 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 8.0.0-1
- Update to 8.0.0

* Sun Oct 03 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 7.1.0-1
- Update to 7.1.0

* Tue Sep 14 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 7.0.1-1
- Update to 7.0.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 6.3.0-7
- Rebuilt for Python 3.10

* Thu May 06 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.3.0-6
- Ignore deprecation warnings

* Tue Apr 13 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.3.0-5
- Disable the test_px_blocking and test_px_nonblocking tests on Fedora 35+
- Remove obsolete scriptlet for removing old style config

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 6.3.0-2
- Rebuilt for Python 3.9

* Wed May 06 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.3.0-1
- Update to 6.3.0
- Drop patches (accepted upstream, or previously backported)

* Mon Apr 20 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.2.5-1
- Update to 6.2.5
- Remove Python 2 parts from the spec file (Fedora 29 is EOL)
- Drop patches (accepted upstream, or previously backported)
- Prevent KeyError when handling heart failures of already shut down engines
- Print more helpful errors from pytest.warns(None)
- Fix client test for python 3.8

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 01 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.2.4-4
- Compatibility with ipykernel 5.1.2 (backport from upstream)

* Mon Aug 12 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.2.4-3
- Compatibility fixes for Python 3.7, 3.8 (backport from upstream)
- Use unittest.mock if available
- Adapt to Python 3.8 with PEP 570
- Disable the test_abort test (occasional random failures)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 13 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.2.4-1
- Update to 6.2.4
- Avoid python3-mock dependency

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 13 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.2.3-2
- Don't build Python 2 packages for Fedora >= 30

* Mon Oct 22 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.2.3-1
- Update to 6.2.3

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.2.2-1
- Update to 6.2.2

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 6.2.1-2
- Rebuilt for Python 3.7

* Mon Jun 11 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.2.1-1
- Update to 6.2.1
- This version uses the possibility to split the configuration files into
  smaller files in .d directories introduced in Jupyter notebook 5.3.0
- Drop scriptlets for handling the old configuration
- Add scriptlet to remove old configuration when updating from earlier versions
- Enable the test_wait_for_send test again (the test suite now tries it three
  times before failing)

* Mon Jun 11 2018 Miro Hrončok <mhroncok@redhat.com> - 6.1.1-2
- Don't own /usr/share/jupyter/nbextensions,
  require python-jupyter-filesystem instead (#1589420)

* Wed Feb 07 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.1.1-1
- Update to 6.1.1

* Tue Feb 06 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.1.0-1
- Update to 6.1.0
- Drop patch python-ipyparallel-pr254.patch (previously backported)
- Only provide one documentation package
- Disable the test_wait_for_send test (occasional random failures)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 18 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.0.2-2
- Put tests in a separate subpackage

* Sun Apr 30 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.0.2-1
- Initial packaging
