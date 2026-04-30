%bcond_without tests

%global         srcname     asyncstdlib
%global         forgeurl    https://github.com/maxfischer2781/%{srcname}
Version:        3.14.0
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Async standard library for Python

License:        MIT
URL:            https://github.com/maxfischer2781/asyncstdlib
Source0:        %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(typing-extensions)
%endif

%global _description %{expand:
asyncstdlib provides async versions of the standard library helpers such as
zip, map, enumerate, functools.reduce, itertools.accumulate and many others.
It works with asyncio, trio, and any other async event loop.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%forgesetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pyproject_check_import

%if %{with tests}
%pytest unittests
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
