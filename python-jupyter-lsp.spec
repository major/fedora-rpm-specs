Name:           python-jupyter-lsp
Version:        1.5.1
Release:        2%{?dist}
Summary:        Multi-Language Server WebSocket proxy for Jupyter Notebook/Lab server
License:        BSD-3-Clause
URL:            https://pypi.org/project/jupyter-lsp/
Source:         %{pypi_source jupyter-lsp}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
Multi-Language Server WebSocket proxy for your Jupyter notebook or lab server.
For Python 3.6+.}


%description %_description

%package -n     python3-jupyter-lsp
Summary:        %{summary}

Requires:       python-jupyter-filesystem

%description -n python3-jupyter-lsp %_description


%prep
%autosetup -p1 -n jupyter-lsp-%{version}

sed -i "/--cov /d" setup.cfg
sed -i "/--cov-report/d" setup.cfg
sed -i "/--flake8/d" setup.cfg

# Remove empty file
# https://github.com/jupyter-lsp/jupyterlab-lsp/pull/884
rm jupyter_lsp/specs/base.py

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files jupyter_lsp

install -m 0755 -p -d %{buildroot}%{_sysconfdir}/jupyter/jupyter_notebook_config.d
install -m 0755 -p -d %{buildroot}%{_sysconfdir}/jupyter/jupyter_server_config.d
mv -v %{buildroot}{%{_prefix},}%{_sysconfdir}/jupyter/jupyter_notebook_config.d/jupyter-lsp-notebook.json
mv -v %{buildroot}{%{_prefix},}%{_sysconfdir}/jupyter/jupyter_server_config.d/jupyter-lsp-jupyter-server.json


%check
# test_r_package_detection fails if R language server is not installed
%pytest -k "not test_r_package_detection"


%files -n python3-jupyter-lsp -f %{pyproject_files}
%doc README.md
%config(noreplace) %{_sysconfdir}/jupyter/jupyter_notebook_config.d/jupyter-lsp-notebook.json
%config(noreplace) %{_sysconfdir}/jupyter/jupyter_server_config.d/jupyter-lsp-jupyter-server.json


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Dec 04 2022 Lumír Balhar <lbalhar@redhat.com> - 1.5.1-1
- Initial package