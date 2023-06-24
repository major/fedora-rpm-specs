Name:           python-jupyter-server-terminals
Version:        0.4.2
Release:        3%{?dist}
Summary:        A Jupyter Server Extension Providing Terminals
License:        BSD-3-Clause
URL:            https://jupyter.org
Source:         %{pypi_source jupyter_server_terminals}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
Jupyter Server Terminals is a Jupyter Server Extension
providing support for terminals.}


%description %_description

%package -n     python3-jupyter-server-terminals
Summary:        %{summary}

Requires:  python-jupyter-filesystem

%description -n python3-jupyter-server-terminals %_description


%prep
%autosetup -p1 -n jupyter_server_terminals-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files jupyter_server_terminals

install -m 0755 -p -d %{buildroot}%{_sysconfdir}/jupyter/jupyter_server_config.d
mv -v %{buildroot}{%{_prefix},}%{_sysconfdir}/jupyter/jupyter_server_config.d/jupyter_server_terminals.json

%check
# The dependency on jupyter-server creates a dependency loop
# we cannot break yet.
# %%pytest


%files -n python3-jupyter-server-terminals -f %{pyproject_files}
%doc README.md
%config(noreplace) %{_sysconfdir}/jupyter/jupyter_server_config.d/jupyter_server_terminals.json


%changelog
* Thu Jun 22 2023 Python Maint <python-maint@redhat.com> - 0.4.2-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 21 2022 Lumír Balhar <lbalhar@redhat.com> - 0.4.2-1
- Initial package