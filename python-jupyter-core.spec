# Unset -s on python shebang - ensure that extensions installed with pip
# to user locations are seen and properly loaded
%global py3_shebang_flags %(echo %py3_shebang_flags | sed s/s//)

Name:           python-jupyter-core
Version:        5.1.0
Release:        6%{?dist}
Summary:        The base package for Jupyter projects

License:        BSD
URL:            http://jupyter.org
Source0:        %{pypi_source jupyter_core}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-docs
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinxcontrib-github-alt
BuildRequires:  python3-myst-parser
BuildRequires:  pyproject-rpm-macros

%bcond_without tests
%if %{with tests}
BuildRequires:  python3-pytest
%endif

%description
Core common functionality of Jupyter projects.

This package contains base application classes and configuration inherited by
other projects.

%package -n     python3-jupyter-core
Summary:        The base package for Jupyter projects

%description -n python3-jupyter-core
Core common functionality of Jupyter projects.

This package contains base application classes and configuration inherited by
other projects.

%package -n python-jupyter-core-doc
Summary:        Documentation of the base package for Jupyter projects
%description -n python-jupyter-core-doc
Core common functionality of Jupyter projects.

This package contains documentation for the base application classes and
configuration inherited by other jupyter projects.

%package -n python-jupyter-filesystem
Summary:        Jupyter filesystem layout
%description -n python-jupyter-filesystem
This package provides directories required by other packages that add
extensions to Jupyter.

%prep
%autosetup -p1 -n jupyter_core-%{version}

# Use local objects.inv for intersphinx:
sed -i "s|{'https://docs.python.org/3/': None}|{'https://docs.python.org/3/': '/usr/share/doc/python3-docs/html/objects.inv'}|" docs/conf.py

%py3_shebang_fix jupyter_core/troubleshoot.py


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel

# generate html docs
PYTHONPATH=. sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%pyproject_install
%pyproject_save_files jupyter jupyter_core

# Create directories for python-jupyter-filesystem package
mkdir -p %{buildroot}%{_datadir}/jupyter
mkdir %{buildroot}%{_datadir}/jupyter/kernels
mkdir -p %{buildroot}%{_datadir}/jupyter/labextensions/@jupyter
mkdir %{buildroot}%{_datadir}/jupyter/nbextensions
mkdir -p %{buildroot}%{_sysconfdir}/jupyter
mkdir %{buildroot}%{_sysconfdir}/jupyter/jupyter_notebook_config.d
mkdir %{buildroot}%{_sysconfdir}/jupyter/jupyter_server_config.d
mkdir %{buildroot}%{_sysconfdir}/jupyter/nbconfig
mkdir %{buildroot}%{_sysconfdir}/jupyter/nbconfig/common.d
mkdir %{buildroot}%{_sysconfdir}/jupyter/nbconfig/edit.d
mkdir %{buildroot}%{_sysconfdir}/jupyter/nbconfig/notebook.d
mkdir %{buildroot}%{_sysconfdir}/jupyter/nbconfig/terminal.d
mkdir %{buildroot}%{_sysconfdir}/jupyter/nbconfig/tree.d


%if %{with tests}
%check
# deselected tests unset PATH env variables and can only run when installed
# test_jupyter_path_(no)_user_site are deselected because we change
# user install location path in Fedora, for reference see:
# https://src.fedoraproject.org/rpms/python3.10/blob/rawhide/f/00251-change-user-install-location.patch
%pytest -Wdefault -v \
    --deselect "jupyter_core/tests/test_command.py::test_not_on_path" \
    --deselect "jupyter_core/tests/test_command.py::test_path_priority" \
    --deselect "jupyter_core/tests/test_command.py::test_argv0" \
    --deselect "jupyter_core/tests/test_paths.py::test_jupyter_path_prefer_env" \
    --deselect "jupyter_core/tests/test_paths.py::test_jupyter_path_user_site" \
    --deselect "jupyter_core/tests/test_paths.py::test_jupyter_path_no_user_site" \
;
%endif


%global _docdir_fmt %{name}

%files -n python3-jupyter-core -f %{pyproject_files}
%license COPYING.md
%doc README.md
%{_bindir}/jupyter
%{_bindir}/jupyter-migrate
%{_bindir}/jupyter-troubleshoot

%files -n python-jupyter-core-doc
%doc html

%files -n python-jupyter-filesystem
%{_datadir}/jupyter
%{_sysconfdir}/jupyter


%changelog
* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 5.1.0-4
- Rebuilt for Python 3.12

* Thu Jun 22 2023 Lumír Balhar <lbalhar@redhat.com> - 5.1.0-3
- Add jupyter/labextensions/@jupyter to filesystem subpackage
Related: rhbz#2213169

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 30 2022 Lumír Balhar <lbalhar@redhat.com> - 5.1.0-1
- Update to 5.1.0 (rhbz#2130602)

* Wed Sep 14 2022 Charalampos Stratakis <cstratak@redhat.com> - 4.11.1-1
- Update to 4.11.1
Resolves: rhbz#2104974

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.10.0-2
- Rebuilt for Python 3.11

* Tue Apr 26 2022 Lumír Balhar <lbalhar@redhat.com> - 4.10.0-1
- Update to 4.10.0
Resolves: rhbz#2076222

* Wed Mar 09 2022 Charalampos Stratakis <cstratak@redhat.com> - 4.9.2-1
- Update to 4.9.2
Resolves: rhbz#2054899

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 25 2021 Karolina Surma <ksurma@redhat.com> - 4.9.1-1
- Update to 4.9.1
Resolves: rhbz#2017607
- Remove -s from Python shebang in `jupyter`, `jupyter-migrate`,
  `jupyter-troubleshoot` to let Jupyter see pip installed extensions

* Tue Oct 26 2021 Lumír Balhar <lbalhar@redhat.com> - 4.8.1-1
- Update to 4.8.1
Resolves: rhbz#1995388

* Tue Sep 14 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 4.7.0-5
- Add directories for jupyterlab extensions to python-jupyter-filesystem

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.7.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 Miro Hrončok <mhroncok@redhat.com> - 4.7.0-1
- Update to 4.7.0
- Fixes: rhbz#1893891

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Lumír Balhar <lbalhar@redhat.com> - 4.6.3-1
- Update to 4.6.3 (#1801546)

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 4.6.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Miro Hrončok <mhroncok@redhat.com> - 4.6.1-1
- Update to 4.6.1 (#1759630)
- Run tests

* Thu Sep 26 2019 Jerry James <loganjerry@gmail.com> - 4.5.0-1
- Update to 4.5.0 (bz 1722169)
- Drop obsoletes and conflicts needed for EOL versions of Fedora
- Drop explicit Provides that are now autogenerated
- Troubleshoot is now a supported entry point
- Drop old workaround for dual python2/python3 builds

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 4.4.0-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Miro Hrončok <mhroncok@redhat.com> - 4.4.0-7
- Subpackage python2-jupyter-core has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.4.0-4
- Rebuilt for Python 3.7

* Sun Jun 10 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 4.4.0-3
- Add python-jupyter-filesystem package

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Miro Hrončok <mhroncok@redhat.com> - 4.4.0-1
- Update to 4.4.0 (#1508192)
- Build docs with Python 3, BR python3-sphinxcontrib-github-alt
- Use local objects.inv for intersphinx, BR python3-docs

* Fri Sep 01 2017 Miro Hrončok <mhroncok@redhat.com> - 4.3.0-2
- Move executables from py2 to py3 (#1410332)

* Tue Aug 29 2017 Orion Poplawski <orion@cora.nwra.com> - 4.3.0-1
- Update to 4.3.0

* Tue Aug 29 2017 Orion Poplawski <orion@cora.nwra.com> - 4.1.0-10
- Use more python2- names

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.1.0-7
- Rebuild for Python 3.6

* Wed Nov 16 2016 Orion Poplwski <orion@cora.nwra.com> - 4.1.0-6
- Do not own __pycache__ dir
- Enable EPEL builds

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat Apr 23 2016 Thomas Spura <tomspur@fedoraproject.org> - 4.1.0-4
- Add obsoletes/provides for jupyter_core
- Fix python2 files installed with python3

* Mon Apr 18 2016 Thomas Spura <tomspur@fedoraproject.org> - 4.1.0-3
- Remove references to jupyter-troubleshoot
- Improve summary
- Remove shebang from troubleshoot.py

* Mon Apr 18 2016 Thomas Spura <tomspur@fedoraproject.org> - 4.1.0-2
- Add PYTHONPATH to sphinx-build (Zbigniew, #1327994)
- Install script differently (Zbigniew, #1327994)
- Rename packages to avoid underscore

* Mon Apr 18 2016 Thomas Spura <tomspur@fedoraproject.org> - 4.1.0-1
- Initial package.
