%global srcname incremental

%global common_description %{expand:
Incremental is a small library that versions your Python projects.}

Name:           python-%{srcname}
Version:        22.10.0
Release:        %autorelease
Summary:        It versions your Python projects

License:        MIT
URL:            https://github.com/twisted/incremental
Source0:        %{url}/archive/%{srcname}-%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description %{common_description}

%package -n     python3-%{srcname}
Summary:        %{summary}
Provides:       %{srcname} = %{version}-%{release}

%description -n python3-%{srcname} %{common_description}

%prep
%autosetup -p1 -n %{srcname}-%{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
