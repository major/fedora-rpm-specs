%global srcname  click-default-group
%global libname click_default_group

%global common_description %{expand:
Provides DefaultGroup, a subclass of click.Group that invokes a default
subcommand instead of showing a help message when a subcommand is not passed.}

Name:           python-%{srcname}
Version:        1.2.2
Release:        %autorelease
Summary:        Extends click.Group to invoke a command without explicit subcommand name

License:        BSD
URL:            https://github.com/sublee/click-default-group/
Source0:        %url/archive/v%{version}/%{srcname}-%{version}.tar.gz
# Fix detection of error message in test, related to click 8
Patch0:         https://patch-diff.githubusercontent.com/raw/click-contrib/click-default-group/pull/18.patch#/0001-Fix-detection-of-error-message.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description %{common_description}

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{common_description}

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{libname}

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
