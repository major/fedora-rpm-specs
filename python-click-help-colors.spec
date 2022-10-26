%global srcname  click-help-colors
%global pkgname  python-click-help-colors
%global slugname click_help_colors
%global forgeurl https://github.com/click-contrib/click-help-colors

%global common_description %{expand:
Colorization of help messages in Click}

%bcond_without tests

Name:           %{pkgname}
Version:        0.9.1
%forgemeta
Release:        %autorelease
Summary:        Colorization of help messages in Click
License:        MIT
URL:            %{forgeurl}
Source:         %{pypi_source}
Patch:          0001_updating_test_optional_packages_target_name.patch
BuildArch:      noarch

BuildRequires: python3-devel

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
%pyproject_save_files %{slugname}

%if %{with tests}
%check
%pytest -vv
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc examples README.rst

%changelog
%autochangelog
