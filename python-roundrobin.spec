Name:           python-roundrobin
Version:        0.0.4
Release:        1%{?dist}
Summary:        Rather small collection of round robin utilites

License:        MIT
URL:            https://github.com/linnik/roundrobin
Source:         %{url}/archive/%{version}/roundrobin-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
# required for tests
BuildRequires:  python3-pytest

%global _description %{expand:
This is rather small collection of round robin utilites}

%description %_description

%package -n python3-roundrobin
Summary:        %{summary}

%description -n python3-roundrobin %_description


%prep
%autosetup -p1 -n roundrobin-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files roundrobin


%check
%pytest test.py


%files -n python3-roundrobin -f %{pyproject_files}
%doc README.*
%license LICENSE


%changelog
* Sun Aug 07 2022 Jonathan Wright <jonathan@almalinux.org> - 0.0.4-1
- Initial package build
- rhbz#2116219
