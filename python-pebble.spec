Name:           python-pebble
Version:        5.0.6
Release:        %autorelease
Summary:        Threading and multiprocessing eye-candy for Python
License:        LGPL-3.0-or-later
URL:            https://github.com/noxdafox/pebble
Source:         %{pypi_source Pebble}
BuildArch:      noarch

%global _description %{expand:
Pebble provides an API to manage threads and processes within an application.
It wraps Python’s standard library threading and multiprocessing objects.}

%description %_description

%package -n python3-pebble
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  python3-pytest

%description -n python3-pebble %_description

%prep
%autosetup -n Pebble-%{version}

%generate_buildrequires
# errors
# %%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pebble

%check
# test intermittently hangs
%{pytest} -v -k "not test_process_pool_multiple_futures"

%files -n python3-pebble -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
