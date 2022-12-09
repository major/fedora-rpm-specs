# Tests depend on pytest-jupyter and that depends back
# on jupyter-server[test] so we might need to break this loop.
%bcond_with tests

Name:           python-jupyter-server
Version:        2.0.0~rc8
Release:        1%{?dist}
Summary:        The backend for Jupyter web applications
License:        BSD-3-Clause
URL:            https://jupyter-server.readthedocs.io
Source:         %{pypi_source jupyter_server}
# Removing useless steps from build process
# See: https://github.com/jupyter-server/jupyter_server/issues/1107
Patch:          build.patch

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
The Jupyter Server provides the backend (i.e. the core services,
APIs, and REST endpoints) for Jupyter web applications like
Jupyter notebook, JupyterLab, and Voila.}


%description %_description

%package -n     python3-jupyter-server
Summary:        %{summary}

%description -n python3-jupyter-server %_description


%prep
%autosetup -n jupyter_server-2.0.0rc8
sed -i '/"pre-commit"/d' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x test}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files jupyter_server


%check
%if %{with tests}
%pytest
%endif


%files -n python3-jupyter-server -f %{pyproject_files}
%doc README.md
%{_bindir}/jupyter-server

%pyproject_extras_subpkg -n python3-jupyter-server test


%changelog
* Mon Nov 28 2022 Lumír Balhar <lbalhar@redhat.com> - 2.0.0~rc8-1
- Initial package