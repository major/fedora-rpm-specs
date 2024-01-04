%global srcname  re-assert
%global slugname re_assert
%global forgeurl https://github.com/asottile/re-assert

%global common_description %{expand:
Show where your regex match assertion failed!}

%bcond_without tests

Name:           python-%{srcname}
Version:        1.1.0
%forgemeta
Release:        %autorelease
Summary:        Show where your regex match assertion failed!
URL:            %{forgeurl}
Source:         %{forgesource}
Patch:          0001_adding_pytest_to_the_testing_dependencies.patch
# SPDX
License:        MIT
BuildArch:      noarch
BuildRequires:  python3-devel

%description %{common_description}

%package -n python3-%{srcname}
Summary: %{summary}
%description -n python3-%{srcname} %{common_description}

%prep
%forgeautosetup -p1

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x test}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{slugname}

%if %{with tests}
%check
%pytest
%endif

%files -n python3-%{srcname} -f %{pyproject_files}

%changelog
%autochangelog
