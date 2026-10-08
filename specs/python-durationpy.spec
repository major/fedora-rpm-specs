Name:           python-durationpy
Version:        0.11
Release:        %autorelease
Summary:        Module for converting between datetime.timedelta and Go's Duration strings

License:        MIT
URL:            https://github.com/icholy/durationpy
Source:         %{url}/archive/refs/tags/%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
Module for converting between datetime.timedelta and Go's Duration strings}

%description %_description

%package -n python3-durationpy
Summary:        %{summary}

%description -n python3-durationpy %_description

%prep
%autosetup -p1 -n durationpy-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l durationpy

%check
%pytest test.py

%files -n python3-durationpy -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
