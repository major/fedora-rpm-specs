Name:           python-jupyter-lsp
Version:        2.3.0
Release:        %autorelease
Summary:        Multi-Language Server WebSocket proxy for Jupyter Notebook/Lab server
# SPDX
License:        BSD-3-Clause
URL:            https://pypi.org/project/jupyter-lsp/
Source:         %{pypi_source jupyter_lsp}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio

%global _description %{expand:
Multi-Language Server WebSocket proxy for your Jupyter notebook or lab server.
For Python 3.6+.}


%description %_description

%package -n     python3-jupyter-lsp
Summary:        %{summary}

Requires:       python-jupyter-filesystem

%description -n python3-jupyter-lsp %_description


%prep
%autosetup -p1 -n jupyter_lsp-%{version}

sed -i "/--cov /d" setup.cfg
sed -i "/--cov-report/d" setup.cfg
sed -i "/--flake8/d" setup.cfg


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files jupyter_lsp

install -m 0755 -p -d %{buildroot}%{_sysconfdir}/jupyter/jupyter_server_config.d
mv -v %{buildroot}{%{_prefix},}%{_sysconfdir}/jupyter/jupyter_server_config.d/jupyter-lsp-jupyter-server.json


%check
# test_r_package_detection fails if R language server is not installed
# test_listener and test_session were silently skipped until pytest 8.4+ made them fail
# we are skipping them for the time being
# upstream report: github.com/jupyter-lsp/jupyterlab-lsp/issues/1159
%pytest -k "not test_r_package_detection" \
        --ignore jupyter_lsp/tests/test_listener.py \
        --ignore jupyter_lsp/tests/test_session.py


%files -n python3-jupyter-lsp -f %{pyproject_files}
%doc README.md
%config(noreplace) %{_sysconfdir}/jupyter/jupyter_server_config.d/jupyter-lsp-jupyter-server.json


%changelog
%autochangelog
