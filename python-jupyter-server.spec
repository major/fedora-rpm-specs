# Tests depend on pytest-jupyter and that depends back
# on jupyter-server[test] so we might need to break this loop.
%bcond_without tests

Name:           python-jupyter-server
Version:        2.0.5
Release:        1%{?dist}
Summary:        The backend for Jupyter web applications
License:        BSD-3-Clause
URL:            https://jupyter-server.readthedocs.io
Source:         %{pypi_source jupyter_server}

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
%autosetup -n jupyter_server-%{version}
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
* Fri Dec 23 2022 Lumír Balhar <lbalhar@redhat.com> - 2.0.5-1
- Update to 2.0.5 (rhbz#2155966)

* Thu Dec 22 2022 Lumír Balhar <lbalhar@redhat.com> - 2.0.3-1
- Update to 2.0.3 (rhbz#2155584)

* Wed Dec 21 2022 Lumír Balhar <lbalhar@redhat.com> - 2.0.2-1
- Update to 2.0.2 (rhbz#2155288)

* Mon Nov 28 2022 Lumír Balhar <lbalhar@redhat.com> - 2.0.0~rc8-1
- Initial package