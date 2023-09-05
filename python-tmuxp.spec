%global srcname tmuxp

Name:           python-%{srcname}
Version:        1.29.1
Release:        %autorelease
Summary:        Tmux session manager

# This is the proper SPDX license
License:        MIT
URL:            https://tmuxp.git-pull.com/
Source:         %{pypi_source}

BuildArch:      noarch

%description
%{summary}.

%package -n python3-%{srcname}
Summary:	%{summary}
BuildRequires:  python3-devel

%description -n python3-%{srcname}
%{summary}.

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files tmuxp

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGES examples
%{_bindir}/tmuxp

%changelog
%autochangelog
