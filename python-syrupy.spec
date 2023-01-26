Name:           python-syrupy
Version:        3.0.6
Release:        1%{?dist}
Summary:        Pytest snapshot plugin

License:        Apache-2.0
URL:            https://tophat.github.io/syrupy
Source:         https://github.com/tophat/syrupy/archive/v%{version}/syrupy-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Syrupy is a pytest snapshot plugin. It enables developers
to write tests which assert immutability of computed results.}

%description %_description

%package -n python3-syrupy
Summary:        %{summary}

%description -n python3-syrupy %_description


%prep
%autosetup -p1 -n syrupy-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files syrupy


%check
%pytest


%files -n python3-syrupy -f %{pyproject_files}
%doc README.* CHANGELOG.md


%changelog
* Thu Jan 12 2023 Jonathan Wright <jonathan@almalinux.org> - 3.0.6-1
- Initial package build
