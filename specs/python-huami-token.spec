# test requires real credentials and network access
%bcond_with check

Name:           python-huami-token
Version:        0.8.0
Release:        %autorelease
Summary:        Obtain watch or band Bluetooth token from Huami servers
License:        MIT
URL:            https://codeberg.org/argrento/huami-token
Source:         %{url}/archive/v%{version}.tar.gz#/huami_token-%{version}.tar.gz
# support pycryptodomex
Patch:          %{name}-deps.patch
BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with check}
BuildRequires:  python3dist(pytest)
%endif

%global _desc %{expand:
Script to obtain watch or band bluetooth access token from Huami
servers. It will also download AGPS data packs cep_alm_pak.zip and
cep_7days.zip.
}

%description %_desc

%package     -n python3-huami-token
Summary:        %{summary}

%description -n python3-huami-token %_desc

%prep
%autosetup -p1 -n huami-token
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L huami_token

%check
%pyproject_check_import
%if %{with check}
%pytest
%endif

%files -n python3-huami-token -f %{pyproject_files}
%doc README.md
%{_bindir}/huami-token

%changelog
%autochangelog
