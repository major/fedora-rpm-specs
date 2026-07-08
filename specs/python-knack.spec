# tests are enabled by default
%bcond_without  tests

%global         srcname     knack
%global         forgeurl    https://github.com/microsoft/knack
Version:        0.14.0
Epoch:          1
%global         tag         v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        A Command-Line Interface framework

License:        MIT
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%global _description %{expand:
A Command-Line Interface framework}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%forgeautosetup -p1


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l knack


%if %{with tests}
%check
%pytest -k "not test_nargs_parameter" 
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc *.rst


%changelog
%autochangelog
