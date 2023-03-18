%bcond_without  check

%global srcname ebranch
%global _description %{expand:
A tool for branching Fedora packages for EPEL.

It allows:
- calculating the transitive closure of missing build dependencies
- calculating the chain-build ordering
- filing branch requests for the missing build dependencies}

Name:           python-%{srcname}
Version:        0.0.3
Release:        %autorelease
Summary:        Tool for branching Fedora packages for EPEL

License:        GPL-2.0-or-later
URL:            https://pagure.io/epel/ebranch
Source:         %pypi_source
Patch:          https://pagure.io/epel/ebranch/c/64f83714a66912e6d4ab303de9f9b56f95126f1a.patch#/%{srcname}-remove-shebangs.diff

BuildArch:      noarch

%description %{_description}


%package -n %{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
Requires:       python-bugzilla-cli
Requires:       rpmdistro-repoquery >= 0^20230201

%description -n %{srcname} %{_description}


%prep
%autosetup -p 1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires -r requirements-test.txt


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%if %{with check}
%check
%pytest
%endif


%files -n %{srcname} -f %{pyproject_files}
%license COPYING.md
%doc README.md
%{_bindir}/%{srcname}


%changelog
%autochangelog
