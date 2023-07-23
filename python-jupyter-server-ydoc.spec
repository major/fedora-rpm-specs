Name:           python-jupyter-server-ydoc
Version:        0.7.0
Release:        2%{?dist}
Summary:        A Jupyter Server Extension Providing Y Documents
License:        BSD-3-Clause
URL:            https://jupyter.org
Source:         %{pypi_source jupyter_server_ydoc}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Jupyter Server YDoc is a Jupyter Server Extension providing support
for Y documents.}


%description %_description

%package -n     python3-jupyter-server-ydoc
Summary:        %{summary}
Requires:       python-jupyter-filesystem

%description -n python3-jupyter-server-ydoc %_description


%prep
%autosetup -p1 -n jupyter_server_ydoc-%{version}

# pytest-tornasync will never be available in Fedora
# and upstream will switch to pytest-jupyter soon
# https://github.com/jupyterlab/jupyterlab/issues/13794
sed -i "/pytest_tornasync/d" pyproject.toml

sed -i "/coverage/d" pyproject.toml


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files jupyter_server_ydoc

install -m 0755 -p -d %{buildroot}%{_sysconfdir}/jupyter/jupyter_notebook_config.d
install -m 0755 -p -d %{buildroot}%{_sysconfdir}/jupyter/jupyter_server_config.d
mv -v %{buildroot}{%{_prefix},}%{_sysconfdir}/jupyter/jupyter_notebook_config.d/jupyter_server_ydoc.json
mv -v %{buildroot}{%{_prefix},}%{_sysconfdir}/jupyter/jupyter_server_config.d/jupyter_server_ydoc.json


%check
%pytest


%files -n python3-jupyter-server-ydoc -f %{pyproject_files}
%doc README.md
%config(noreplace) %{_sysconfdir}/jupyter/jupyter_notebook_config.d/jupyter_server_ydoc.json
%config(noreplace) %{_sysconfdir}/jupyter/jupyter_server_config.d/jupyter_server_ydoc.json


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jan 16 2023 Lumír Balhar <lbalhar@redhat.com> - 0.7.0-1
- Initial package