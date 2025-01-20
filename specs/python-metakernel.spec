%global __requires_exclude python.*dist\\((jupyter-kernel-test|pytest-cov|pytest-timeout)\\)

Name:		python-metakernel
#		The python and echo subpackages have their own version
#		and release numbers - update below in each package section
#		Running rpmdev-bumpspec on this specfile will update all the
#		release tags automatically
Version:	0.30.2
Release:	5%{?dist}
%global pkgversion %{version}
%global pkgrelease %{release}
Summary:	Metakernel for Jupyter

License:	BSD-3-Clause
URL:		https://github.com/Calysto/metakernel
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
#		Address failing tests with Python 3.13
#		https://github.com/Calysto/metakernel/issues/279
#		https://github.com/Calysto/metakernel/pull/280
Patch0:		0001-Test-compatibility-with-Python-3.13.patch

BuildArch:	noarch
BuildRequires:	make
BuildRequires:	python3-devel >= 3.8
BuildRequires:	python3-pip
BuildRequires:	python3dist(hatchling) >= 1.5
BuildRequires:	python3dist(ipykernel) >= 5.5.6
BuildRequires:	python3dist(jedi) >= 0.18
BuildRequires:	python3dist(jupyter-core) >= 4.9.2
BuildRequires:	python3dist(pexpect) >= 4.8
#		For testing:
BuildRequires:	python3dist(pytest)
BuildRequires:	python3dist(pytest-timeout)
BuildRequires:	python3dist(requests)
BuildRequires:	python3dist(ipyparallel)
BuildRequires:	python3dist(pydot)
BuildRequires:	man
#		For documentation
BuildRequires:	python3dist(sphinx)
BuildRequires:	python3dist(sphinx-bootstrap-theme)
BuildRequires:	python3dist(myst-parser)
BuildRequires:	python3dist(numpydoc)
BuildRequires:	python3dist(recommonmark)

%description
A Jupyter/IPython kernel template which includes core magic functions
(including help, command and file path completion, parallel and
distributed processing, downloads, and much more).

%package -n python3-metakernel
Summary:	Metakernel for Jupyter
%py_provides	python3-metakernel
Obsoletes:	python3-metakernel-bash < 0.19.1-24

%description -n python3-metakernel
A Jupyter/IPython kernel template which includes core magic functions
(including help, command and file path completion, parallel and
distributed processing, downloads, and much more).

%package -n python3-metakernel+test
Summary:	Tests for python3-metakernel
%py_provides	python3-metakernel+test
%py_provides	python3-metakernel-tests
Obsoletes:	python3-metakernel-tests < 0.29.3-2
Requires:	python3-metakernel = %{version}-%{release}
Requires:	man

%description -n python3-metakernel+test
This package contains the tests of python3-metakernel.

%package doc
Summary:	Documentation for python-metakernel

%description doc
This package contains the documentation of python-metakernel.

%package -n python3-metakernel-python
Version:	0.19.1
Release:	71%{?dist}
Summary:	A Python kernel for Jupyter/IPython
%py_provides	python3-metakernel-python
Requires:	python3-metakernel = %{pkgversion}-%{pkgrelease}
Requires:	python-jupyter-filesystem

%description -n python3-metakernel-python
A Python kernel for Jupyter/IPython, based on MetaKernel.

%package -n python3-metakernel-echo
Version:	0.19.1
Release:	71%{?dist}
Summary:	A simple echo kernel for Jupyter/IPython
%py_provides	python3-metakernel-echo
Requires:	python3-metakernel = %{pkgversion}-%{pkgrelease}
Requires:	python-jupyter-filesystem

%description -n python3-metakernel-echo
A simple echo kernel for Jupyter/IPython, based on MetaKernel.

%prep
%setup -q -n metakernel-%{pkgversion}
%patch -P0 -p1

%build
%pyproject_wheel

pushd metakernel_python
%pyproject_wheel
popd

pushd metakernel_echo
%pyproject_wheel
popd

pushd docs
PYTHONPATH=.. make html
rm -f _build/html/.buildinfo
popd

%install
%pyproject_install
rm %{buildroot}%{python3_sitelib}/metakernel/magics/README.md

for f in tests/test_expect.py; do
  sed '/\/usr\/bin\/env/d' -i %{buildroot}%{python3_sitelib}/metakernel/${f}
done

PYTHONPATH=metakernel_python \
  python3 -m metakernel_python install --name python3-metakernel-python \
  --prefix %{buildroot}%{_prefix}
PYTHONPATH=metakernel_echo \
  python3 -m metakernel_echo install --name python3-metakernel-echo \
  --prefix %{buildroot}%{_prefix}

%check
# The completion magic test checks for the existence of ~/.bashrc
touch ~/.bashrc
PYTHONPATH=metakernel_python ipcluster start -n=3 &
pid=$!
# The version of jupyter-client in Fedora 39/40 calls datetime.utcnow()
# Ignore DeprecationWarning from Python 3.12 due to this
# The version of jupyter-client in Fedora 41 calls datetime.strptime()
# with a deprecated set of arguments
# Ignore DeprecationWarning from Python 3.13 due to this
pytest -v --color=no \
    -W "ignore:datetime.datetime.utcnow() is deprecated:DeprecationWarning" \
    -W "ignore:Parsing dates involving a day of month without a year specified is ambiguious:DeprecationWarning"
ipcluster stop
wait $pid

%files -n python3-metakernel
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/metakernel-*.*-info
%dir %{python3_sitelib}/metakernel
%{python3_sitelib}/metakernel/*.py
%{python3_sitelib}/metakernel/__pycache__
%{python3_sitelib}/metakernel/images
%dir %{python3_sitelib}/metakernel/magics
%{python3_sitelib}/metakernel/magics/*.py
%{python3_sitelib}/metakernel/magics/__pycache__
%{python3_sitelib}/metakernel/utils

%files -n python3-metakernel+test
%ghost %{python3_sitelib}/metakernel-*.*-info
%{python3_sitelib}/metakernel/tests
%{python3_sitelib}/metakernel/magics/tests

%files doc
%license LICENSE.txt
%doc docs/_build/html

%files -n python3-metakernel-python
%{python3_sitelib}/metakernel_python-*.*-info
%{python3_sitelib}/metakernel_python.py
%{python3_sitelib}/__pycache__/metakernel_python.*
%{_datadir}/jupyter/kernels/python3-metakernel-python

%files -n python3-metakernel-echo
%{python3_sitelib}/metakernel_echo-*.*-info
%{python3_sitelib}/metakernel_echo.py
%{python3_sitelib}/__pycache__/metakernel_echo.*
%{_datadir}/jupyter/kernels/python3-metakernel-echo

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 15 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.30.2-3
- Address failing tests with Python 3.13

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 0.30.2-2
- Rebuilt for Python 3.13

* Thu Mar 28 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.30.2-1
- Update to version 0.30.2

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Sep 12 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.30.1-1
- Update to version 0.30.1
- Drop patch accepted upstream

* Fri Sep 08 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.30.0-2
- Adapt to Python 3.12.0rc2

* Tue Sep 05 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.30.0-1
- Update to version 0.30.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.29.5-1
- Update to version 0.29.5
- Drop patch accepted upstream

* Fri Jul 07 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.29.4-4
- Ignore DeprecationWarnings for datetime.utcnow()

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 0.29.4-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 12 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.29.4-1
- Update to version 0.29.4

* Sat Dec 03 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.29.3-2
- Rename tests subpackage to fix auto provides

* Thu Dec 01 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.29.3-1
- Update to version 0.29.3

* Tue Aug 09 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.29.2-1
- Update to version 0.29.2

* Thu Aug 04 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.29.1-1
- Update to version 0.29.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.29.0-3
- Relax dependencies for Fedora 36

* Tue Jun 28 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.29.0-2
- Relax dependencies for Fedora 35

* Sun Jun 26 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.29.0-1
- Update to version 0.29.0

* Mon Jun 20 2022 Python Maint <python-maint@redhat.com> - 0.28.2-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 03 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.28.2-1
- Update to version 0.28.2

* Fri Nov 26 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.28.1-1
- Update to version 0.28.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.27.5-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.27.5-2
- Disable test failing due to new readline library version

* Tue Nov 10 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.27.5-1
- Update to version 0.27.5
- Drop patches accepted upstream

* Sat Nov 07 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.27.4-1
- Update to version 0.27.4
- Fix compatibility with older jedi versions broken in 0.27.3
- Add missing dollar signs to %latex examples and tests
- Escape backslashes in strings in test code

* Fri Nov 06 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.27.3-1
- Update to version 0.27.3

* Wed Nov 04 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.27.1-1
- Update to version 0.27.1

* Thu Sep 03 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.27.0-1
- Update to version 0.27.0

* Wed Aug 26 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.26.1-1
- Update to version 0.26.1

* Sat Aug 22 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.26.0-1
- Update to version 0.26.0

* Wed Aug 19 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.25.1-1
- Update to version 0.25.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.24.4-2
- Rebuilt for Python 3.9

* Thu Apr 16 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.24.4-1
- Update to version 0.24.4
- Remove Python 2 parts from the spec file (Fedora 29 is EOL)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 20 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.24.3-1
- Update to version 0.24.3

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.24.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.24.2-1
- Update to version 0.24.2
- Drop patch python-metakernel-Fix-TypeError.patch (accepted upstream)

* Wed Jun 05 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.24.1-1
- Update to version 0.24.1
- Drop metakernel-bash packages (upstream removed sources)
- Tests are now using pytest instead of nose
- Fix a TypeError

* Mon May 13 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.23.0-1
- Update to version 0.23.0

* Sun May 05 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.22.1-1
- Update to version 0.22.1

* Wed May 01 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.21.2-1
- Update to version 0.21.2

* Mon Apr 29 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.21.0-1
- Update to version 0.21.0
- Drop patch python-metakernel-adjustment-for-newer-jedi.patch (backported)
- Drop patch python-metakernel-python-exec.patch (accepted upstream)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 16 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.20.14-9
- Adapt to Python 3 only ipcluster in Fedora >= 30

* Tue Nov 13 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.20.14-8
- Don't build Python 2 packages for Fedora >= 30

* Mon Jul 16 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.20.14-7
- Don't rely on 'python' in path during testing

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.20.14-5
- Rebuilt for Python 3.7

* Mon Jun 25 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.20.14-4
- Adjustment for newer jedi (Backport from upstream git)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.20.14-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.20.14-1
- Update to 0.20.14
- Drop patches python-metakernel-install.patch and
  python-metakernel-bash-eval.patch (accepted upstream)
- Only provide one documentation package

* Sun Nov 26 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.20.12-2
- Use full path to python interpreter in kernel description
- Fix missing printout in bash kernel

* Fri Nov 17 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.20.12-1
- Update to 0.20.12

* Mon Oct 23 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.20.10-1
- Update to 0.20.10

* Fri Oct 20 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.20.8-1
- Update to 0.20.8

* Fri Sep 22 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.20.7-1
- Update to 0.20.7

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 14 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.20.4-1
- Update to 0.20.4

* Thu May 18 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.20.2-2
- Put tests in a separate subpackage

* Sat May 13 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.20.2-1
- Update to 0.20.2

* Sat Apr 29 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.20.1-1
- Initial packaging
