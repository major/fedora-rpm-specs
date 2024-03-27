%global forgeurl https://github.com/noxdafox/pebble

# Tests take rather long compared to build. Allow skipping.
%bcond tests 1

Name:           python-pebble
Version:        5.0.7
Release:        %autorelease
Summary:        Threading and multiprocessing eye-candy for Python

%global tag %{version}
%forgemeta

License:        LGPL-3.0-or-later
URL:            %{forgeurl}
Source:         %{forgesource}
Patch:          %{forgeurl}/pull/130.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
Pebble provides an API to manage threads and processes within an application.
It wraps Python’s standard library threading and multiprocessing objects.}

%description %_description

%package -n python3-pebble
Summary:        %{summary}

%description -n python3-pebble %_description

%prep
%forgeautosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pebble

%check
%if %{with tests}
  # test intermittently hangs
  %{pytest} -v -k "not test_process_pool_multiple_futures"
%else
  %pyproject_check_import
%endif

%files -n python3-pebble -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
