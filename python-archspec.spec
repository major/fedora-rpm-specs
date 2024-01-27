%global srcname archspec

Name:           python-%{srcname}
Version:        0.2.2
Release:        3%{?dist}
Summary:        A library to query system architecture

License:        Apache-2.0 OR MIT
URL:            https://github.com/archspec/archspec
Source:         %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Archspec aims at providing a standard set of human-understandable labels for
various aspects of a system architecture like CPU, network fabrics, etc. and
APIs to detect, query and compare them.

This project grew out of Spack and is currently under active development. At
present it supports APIs to detect and model compatibility relationships among
different CPU microarchitectures.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}
rm -rf archspec/json/.git*


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


# No tests shipped yet: https://github.com/archspec/archspec/issues/136
%check
%tox


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.*
%{_bindir}/archspec


%changelog
* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Dec 02 2023 Orion Poplawski <orion@nwra.com> - 0.2.2-1
- Initial Fedora package
