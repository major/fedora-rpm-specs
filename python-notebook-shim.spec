Name:           python-notebook-shim
Version:        0.2.2
Release:        2%{?dist}
Summary:        A shim layer for notebook traits and config
License:        BSD-3-Clause
URL:            https://pypi.org/project/notebook-shim/
Source:         %{pypi_source notebook_shim}

BuildArch:      noarch
BuildRequires:  python3-devel
# https://github.com/jupyter/notebook_shim/issues/28
BuildRequires:  python3-pytest-jupyter

%global _description %{expand:
This project provides a way for JupyterLab and other frontends
to switch to Jupyter Server for their Python Web application backend.}


%description %_description

%package -n     python3-notebook-shim
Summary:        %{summary}

Requires:  python-jupyter-filesystem

%description -n python3-notebook-shim %_description


%prep
%autosetup -p1 -n notebook_shim-%{version}

# pytest-tornasync will never be available in Fedora
# and upstream will switch to pytest-jupyter soon
sed -i "/pytest-tornasync/d" pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files notebook_shim

install -m 0755 -p -d %{buildroot}%{_sysconfdir}/jupyter/jupyter_server_config.d
mv -v %{buildroot}{%{_prefix},}%{_sysconfdir}/jupyter/jupyter_server_config.d/notebook_shim.json


%check
%pytest


%files -n python3-notebook-shim -f %{pyproject_files}
%doc README.md
%config(noreplace) %{_sysconfdir}/jupyter/jupyter_server_config.d/notebook_shim.json


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 01 2022 Lumír Balhar <lbalhar@redhat.com> - 0.2.2-1
- Initial package