Name:           python-nkdfu
Version:        0.2
Release:        %autorelease
Summary:        DFU tool for updating Nitrokeys firmware

License:        GPL-2.0-only
URL:            https://github.com/Nitrokey/nkdfu
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz

# Update project metadata to support flit-core version 4+
Patch:          https://github.com/Nitrokey/nkdfu/pull/2.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
%{summary}.}

%description %_description

%package -n     python3-nkdfu
Summary:        %{summary}

%description -n python3-nkdfu %_description


%prep
%autosetup -p1 -n nkdfu-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files nkdfu -l


%check
%pyproject_check_import


%files -n python3-nkdfu -f %{pyproject_files}
%{_bindir}/nkdfu
%doc README.md

%changelog
%autochangelog
