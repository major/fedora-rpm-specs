Name:           python-jupyter-server-fileid
Version:        0.9.1
Release:        %autorelease
Summary:        A Jupyter Server extension for the File ID service
License:        BSD-3-Clause
URL:            https://pypi.org/project/jupyter-server-fileid/
Source:         %{pypi_source jupyter_server_fileid}

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
A Jupyter Server extension providing an implementation of the File ID service.}


%description %_description

%package -n     python3-jupyter-server-fileid
Summary:        %{summary}

Requires:       python-jupyter-filesystem
# Upstream has this dependency in jupyter-server-fileid[cli]
# but the executable script is in the main package.
# See https://github.com/jupyter-server/jupyter_server_fileid/issues/54
Requires:       python3-click

%description -n python3-jupyter-server-fileid %_description


%prep
%autosetup -p1 -n jupyter_server_fileid-%{version}

sed -i "/pytest-cov/d" pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files jupyter_server_fileid

install -m 0755 -p -d %{buildroot}%{_sysconfdir}/jupyter/jupyter_server_config.d
mv -v %{buildroot}{%{_prefix},}%{_sysconfdir}/jupyter/jupyter_server_config.d/jupyter_server_fileid.json


%check
%pytest


%files -n python3-jupyter-server-fileid -f %{pyproject_files}
%doc README.md
%{_bindir}/jupyter-fileid
%config(noreplace) %{_sysconfdir}/jupyter/jupyter_server_config.d/jupyter_server_fileid.json

%pyproject_extras_subpkg -n python3-jupyter-server-fileid test

%changelog
%autochangelog
