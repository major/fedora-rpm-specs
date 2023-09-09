%bcond_without tests

%global pypi_name matplotlib-venn
%global forgeurl https://github.com/konstantint/%{pypi_name}

%global _description %{expand:
Venn diagram plotting routines for Python/Matplotlib. The package
provides four main functions: venn2, venn2_circles, venn3 and
venn3_circles.}


Name:           python-%{pypi_name}
Version:        0.11.9
Release:        %autorelease
Summary:        Routines for plotting area-weighted two- and three-circle venn diagrams
%global tag %{version}
%forgemeta
License:        MIT
URL:            %forgeurl
Source0:        %forgesource
Patch:          https://github.com/konstantint/matplotlib-venn/pull/70.patch

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  make
BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files matplotlib_venn

%check
%if %{with tests}
%pytest
%endif

%files -n python3-matplotlib-venn -f %{pyproject_files}
%doc README.rst DEVELOPER-README.rst CHANGELOG.txt

%changelog
%autochangelog
