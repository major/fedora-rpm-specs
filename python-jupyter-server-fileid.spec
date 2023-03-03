Name:           python-jupyter-server-fileid
Version:        0.8.0
Release:        1%{?dist}
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

%changelog
* Wed Mar 01 2023 Lumír Balhar <lbalhar@redhat.com> - 0.8.0-1
- Update to 0.8.0 (rhbz#2173025)

* Fri Feb 17 2023 Lumír Balhar <lbalhar@redhat.com> - 0.7.0-1
- Update to 0.7.0 (rhbz#2170695)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 05 2022 Lumír Balhar <lbalhar@redhat.com> - 0.6.0-1
- Initial package