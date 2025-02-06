Name:           python-findpython
Version:        0.6.2
Release:        %autorelease

Summary:        A utility to find python versions on your system

License:        MIT
URL:            https://github.com/frostming/findpython
Source:         %{pypi_source findpython}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest


%global _description %{expand:
Findpython searches for python executables available on the system.}

%description %_description

%package -n     python3-findpython
Summary:        %{summary}

%description -n python3-findpython %_description


%prep
%autosetup -p1 -n findpython-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -L findpython


%check
%pytest


%files -n python3-findpython -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/findpython

%changelog
%autochangelog
