Name:           python-pyclibrary
Version:        0.3.0
Release:        %autorelease
Summary:        C parser and ctypes automation for Python
BuildArch:      noarch

License:        MIT
URL:            https://pyclibrary.readthedocs.org/
Source:         %{pypi_source pyclibrary}

BuildRequires:  python3-devel
# For _ctypes_test
BuildRequires:  python3-test


%global _description %{expand:
C parser and bindings automation for Python.

Fork of https://launchpad.net/pyclibrary.
}

%description %_description

%package -n python3-pyclibrary
Summary:        %{summary}

%description -n python3-pyclibrary %_description


%prep
%autosetup -p1 -n pyclibrary-%{version}
%pyproject_patch_dependency pytest-cov:ignore


%generate_buildrequires
%pyproject_buildrequires -g test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pyclibrary


%check
%pytest


%files -n python3-pyclibrary -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
