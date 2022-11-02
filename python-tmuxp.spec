%global srcname tmuxp

Name:           python-%{srcname}
Version:        1.18.1
Release:        %autorelease
Summary:        Tmux session manager

License:        MIT
URL:            https://tmuxp.git-pull.com/
Source:         %{pypi_source}

BuildArch:      noarch

%description
%{summary}.

%package -n python3-%{srcname}
Summary:	%{summary}
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

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

%files -n python3-%{srcname}
%license LICENSE
%doc README.md CHANGES examples
%{_bindir}/tmuxp
%{python3_sitelib}/%{srcname}-*.dist-info/
%{python3_sitelib}/%{srcname}/

%changelog
%autochangelog
