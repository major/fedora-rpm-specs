%global srcname pathable

Name:           python-%{srcname}
Version:        0.4.4
Release:        %autorelease
Summary:        Object-oriented paths

License:        Apache-2.0
URL:            https://pypi.python.org/pypi/%{srcname}
Source:         %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
A python library which provides traverse resources like paths and
access resources on demand with separate accessor layer.}

%description %_description


%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%pyproject_check_import


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
%autochangelog
