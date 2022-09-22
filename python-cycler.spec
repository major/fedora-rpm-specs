%global srcname cycler
%global sum Cycle through lists in various ways (used by matplotlib)
%global desc General purpose library used by matplotlib to cycle through lists for colors,\
marker styles, etc

Name:           python-%{srcname}
Version:        0.11.0
Release:        %autorelease
Summary:        %{sum}

License:        BSD
Source0:        %pypi_source
URL:            https://github.com/matplotlib/cycler.git

BuildArch:      noarch

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{sum}
BuildRequires:  python3-devel

%description -n python3-%{srcname}
%{desc}

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
