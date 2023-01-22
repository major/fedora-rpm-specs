Name:           python-async-lru
Version:        1.0.3
Release:        2%{?dist}
Summary:        Simple lru_cache for asyncio
License:        MIT
URL:            https://github.com/aio-libs/async_lru
Source:         https://github.com/aio-libs/async-lru/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio


%global _description %{expand:
This package is 100% port of Python built-in
function functools.lru_cache for asyncio.}


%description %_description

%package -n     python3-async-lru
Summary:        %{summary}

%description -n python3-async-lru %_description


%prep
%autosetup -p1 -n async-lru-%{version}
# Removing pytest CLI options. Most of them are related to coverage.
sed -i "/addopts/d" setup.cfg

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files async_lru


%check
# Ignore RuntimeWarnings about unawaited coroutines
# see https://github.com/aio-libs/async-lru/issues/341
%pytest -W ignore::RuntimeWarning


%files -n python3-async-lru -f %{pyproject_files}
%doc README.rst


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 05 2022 Lumír Balhar <lbalhar@redhat.com> - 1.0.3-1
- Initial package