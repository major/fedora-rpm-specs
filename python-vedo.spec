%global forgeurl https://github.com/marcomusy/vedo
Version:        2023.5.0
%forgemeta

Name:           python-vedo
Release:        %autorelease
Summary:        A python module for scientific analysis and visualization of 3D objects

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
A python module for scientific analysis of 3D objects and point clouds based on
VTK and numpy.}

%description %_description

%package -n     python3-vedo
Summary:        %{summary}

%description -n python3-vedo %_description

%prep
%autosetup -p1 -n vedo-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files vedo

%py3_shebang_fix %{buildroot}%{python3_sitelib}

%check
%{py3_test_envvars} %{python3} tests/common/test_*.py

%files -n python3-vedo -f %{pyproject_files}
%{_bindir}/vedo

%changelog
%autochangelog
