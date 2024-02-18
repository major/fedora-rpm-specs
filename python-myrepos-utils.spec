%bcond_without check

%global srcname myrepos-utils

Name:           python-%{srcname}
Version:        0.0.4.2
Release:        %autorelease
Summary:        Additional utilities for myrepos

License:        GPL-2.0-or-later
URL:            https://git.sr.ht/~michel-slm/myrepos-utils
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Additional utilities for myrepos.}

%description %_description


%package -n %{srcname}
Summary:        %{summary}
Requires:       myrepos

%description -n %{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires %{?with_check:-r requirements-test.txt}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files myrepos_utils


%check
%pyproject_check_import myrepos_utils
%if %{with check}
%pytest -v
%endif


%files -n %{srcname} -f %{pyproject_files}
%doc README.md
%license COPYING.md
%{_bindir}/mr-utils


%changelog
%autochangelog
