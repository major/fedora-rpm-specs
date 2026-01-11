Name:           python-zombie-imp
Version:        0.0.4
Release:        %autorelease
Summary:        A copy of the `imp` module that was removed in Python 3.12

License:        Python-2.0.1
URL:            https://github.com/encukou/zombie-imp
Source:         %{pypi_source zombie_imp}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-test

%global _description %{expand:
A copy of the imp module that was removed in Python 3.12.
This is a compat package to ease transition to Python 3.12.
It shouldn't be used and packages using `imp` module
should use `importlib.metadata` instead.}

%description %_description

%package -n python3-zombie-imp
Summary:        %{summary}

# This package is deprecated, no new packages in Fedora can depend on it
Provides:       deprecated()

%description -n python3-zombie-imp %_description


%prep
%autosetup -p1 -n zombie_imp-%{version}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files zombie_imp imp


%check
%tox


%files -n python3-zombie-imp -f %{pyproject_files}
%doc README.*


%changelog
%autochangelog
