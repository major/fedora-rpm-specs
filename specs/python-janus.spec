Name:           python-janus
Version:        1.0.0
Release:        11%{?dist}
Summary:        Thread-safe asyncio-aware queue for Python

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/aio-libs/janus
Source:         %{url}/archive/v%{version}/janus-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
# Testing requirements to avoid extra checks
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)

%global _description %{expand:
Mixed sync-async queue, supposed to be used for communicating between classic
synchronous (threaded) code and asynchronous (in terms of asyncio) one.

Like Janus god the queue object from the library has two faces: synchronous and
asynchronous interface.

Synchronous is fully compatible with standard queue, asynchronous one follows
asyncio queue design.}

%description %_description

%package -n python3-janus
Summary:        %{summary}

%description -n python3-janus %_description


%prep
%autosetup -p1 -n janus-%{version}


%generate_buildrequires
%pyproject_buildrequires -r

# Upstream is broken, the PR: https://github.com/aio-libs/janus/pull/436
sed -i 's/LICENSE.txt/LICENSE/' setup.cfg


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files janus


%check
%pytest


%files -n python3-janus -f %{pyproject_files}
%doc CHANGES.rst README.rst


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.0-10
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.0.0-8
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.0.0-4
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Aug 12 2022 Roman Inflianskas <rominf@aiven.io> - 1.0.0-2
- Actually include LICENSE file

* Fri Aug 05 2022 Roman Inflianskas <rominf@aiven.io> - 1.0.0-1
- Initial package
