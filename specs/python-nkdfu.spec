Name:           python-nkdfu
Version:        0.2
Release:        %autorelease
Summary:        DFU tool for updating Nitrokeys firmware

License:        GPL-2.0-or-later
URL:            https://github.com/Nitrokey/nkdfu
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz

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
%pyproject_save_files nkdfu -L


%check
%pyproject_check_import


%files -n python3-nkdfu -f %{pyproject_files}
%{_bindir}/nkdfu
%license LICENSE
%doc README.md

%changelog
%autochangelog
