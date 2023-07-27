# tests are enabled by default
%bcond_without  tests

%global         srcname     msrest
%global         forgeurl    https://github.com/Azure/msrest-for-python
Version:        0.7.1
# MSFT isn't making tags any longer in this repo for some reason.
%global         commit      2d8fd04f68a124d0f3df7b81584accc3270b1afc
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        The runtime library "msrest" for AutoRest generated Python clients
License:        MIT
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(trio)
%endif

%global _description %{expand:
The runtime library "msrest" for AutoRest generated Python clients}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%pyproject_extras_subpkg -n python3-%{srcname} async


%prep
%forgeautosetup


%generate_buildrequires
%pyproject_buildrequires -x async


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%pyproject_check_import

%if %{with tests}
# Some tests require network connectivity, so they are skipped here.
%pytest \
    --ignore=tests/asynctests/test_pipeline.py \
    --ignore=tests/asynctests/test_universal_http.py \
    --ignore=tests/test_auth.py \
    --ignore=tests/test_runtime.py
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
