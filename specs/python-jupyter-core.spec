# Unset -s on python shebang - ensure that extensions installed with pip
# to user locations are seen and properly loaded
%undefine _py3_shebang_s

Name:           python-jupyter-core
Version:        5.8.1
Release:        %autorelease
Summary:        The base package for Jupyter projects

License:        BSD-3-Clause
URL:            http://jupyter.org
Source:         %{pypi_source jupyter_core}
BuildArch:      noarch

BuildRequires:  python3-devel

%bcond tests    1
%if %{with tests}
BuildRequires:  python3-pytest
%endif

%description
Core common functionality of Jupyter projects.

This package contains base application classes and configuration inherited by
other projects.

%package -n     python3-jupyter-core
Summary:        The base package for Jupyter projects
Obsoletes:      python-jupyter-core-doc < 5.7.2-4

%description -n python3-jupyter-core
Core common functionality of Jupyter projects.

This package contains base application classes and configuration inherited by
other projects.

%package -n python-jupyter-filesystem
Summary:        Jupyter filesystem layout

%description -n python-jupyter-filesystem
This package provides directories required by other packages that add
extensions to Jupyter.


%prep
%autosetup -p1 -n jupyter_core-%{version}
%py3_shebang_fix jupyter_core/troubleshoot.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l jupyter jupyter_core

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


%check
%pyproject_check_import
%if %{with tests}
# deselected tests unset PATH env variables and can only run when installed
# test_jupyter_path_(no)_user_site are deselected because we change
# user install location path in Fedora, for reference see:
# https://src.fedoraproject.org/rpms/python3.10/blob/rawhide/f/00251-change-user-install-location.patch
%pytest -Wdefault -v \
    --deselect "tests/test_command.py::test_not_on_path" \
    --deselect "tests/test_command.py::test_path_priority" \
    --deselect "tests/test_command.py::test_argv0" \
    --deselect "tests/test_paths.py::test_jupyter_path_prefer_env" \
    --deselect "tests/test_paths.py::test_jupyter_path_user_site" \
    --deselect "tests/test_paths.py::test_jupyter_path_no_user_site" \
;
%endif


%files -n python3-jupyter-core -f %{pyproject_files}
%doc README.md
%{_bindir}/jupyter
%{_bindir}/jupyter-migrate
%{_bindir}/jupyter-troubleshoot

%files -n python-jupyter-filesystem
%{_datadir}/jupyter
%{_sysconfdir}/jupyter


%changelog
%autochangelog
