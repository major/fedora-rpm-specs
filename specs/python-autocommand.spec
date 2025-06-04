%global modname  autocommand
%global projname %{modname}

%bcond_without tests

Name:           python-%{projname}
Version:        2.2.2
Release:        %autorelease
Summary:        Generate argparse parsers from function signatures

License:        LGPL-3.0-or-later
URL:            https://github.com/Lucretiel/%{projname}
Source0:        %{pypi_source %{projname}}

# https://bugzilla.redhat.com/show_bug.cgi?id=2259644
Patch:          %{url}/pull/33.patch#/001-setuptools-fix.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=2327972
Patch:          %{url}/pull/40.patch#/002-python3.14-fix.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3-pytest
%endif

%global _description %{expand:
A library to automatically generate and run simple argparse parsers from
function signatures}

%description %_description

%package     -n python3-%{projname}
Summary:        %{summary}

%description -n python3-%{projname} %_description

%prep
%autosetup -p1 -n %{projname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%check
%if %{with tests}
%pytest
%else
%pyproject_check_import
%endif

%files -n python3-%{projname} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
