Name:           python-nethsm
Version:        3.0.0
Release:        %autorelease
Summary:        Client-side Python SDK for NetHSM

License:        Apache-2.0
URL:            https://github.com/Nitrokey/nethsm-sdk-py
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
%{summary}.}

%description %_description

%package -n     python3-nethsm
Summary:        %{summary}

%description -n python3-nethsm %_description


%prep
%autosetup -p1 -n nethsm-sdk-py-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l nethsm -L


%check
# We can't really run upstream's test suite, almost all the tests depend
# on a container running a stubbed NetHSM.
%pyproject_check_import


%files -n python3-nethsm -f %{pyproject_files}
%license LICENSE
%doc README.md


%changelog
%autochangelog
