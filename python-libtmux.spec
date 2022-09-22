%global srcname libtmux

Name:           python-%{srcname}
Version:        0.11.0
Release:        %autorelease
Summary:        Scripting library for tmux

License:        BSD
URL:            https://github.com/tmux-python/libtmux
Source:         %{pypi_source}
BuildArch:      noarch

%global _description %{expand:
libtmux is the tool behind tmuxp, a tmux workspace manager in
python.  It builds upon tmux's target and formats to create an object
mapping to traverse, inspect and interact with live tmux sessions.}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
%{?python_provide:%python_provide python3-%{srcname}}
Requires:       tmux >= 1.8

%description -n python3-%{srcname} %{_description}

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
%doc README.md CHANGES
%{python3_sitelib}/%{srcname}-*.dist-info/
%{python3_sitelib}/%{srcname}/

%changelog
%autochangelog
