Name:           python-pyls-spyder
Version:        0.4.0
Release:        %autorelease
Summary:        Spyder extensions for the python-language-server (pyls)

# SPDX
License:        MIT
URL:            https://github.com/spyder-ide/pyls-spyder
Source:         %{pypi_source pyls-spyder}
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
%{summary}.}

%description %{_description}

%package -n     python3-pyls-spyder
Summary:        %{summary}

%description -n python3-pyls-spyder %{_description}

%prep
%autosetup -n pyls-spyder-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pyls_spyder

%check
# Upstream provides no tests
%pyproject_check_import

%files -n python3-pyls-spyder -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md

%changelog
%autochangelog
