Name:           python-cmdkit
Version:        2.7.7
Release:        1%{?dist}
Summary:        A library for developing command-line applications in Python
License:        Apache-2.0
URL:            https://cmdkit.readthedocs.io/
Source:         https://github.com/glentner/CmdKit/archive/v%{version}/CmdKit-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

# for tests
BuildRequires:  python3-pytest
BuildRequires:  python3-hypothesis
BuildRequires:  python3-yaml
BuildRequires:  python3-tomli-w

%description
%summary

%package -n python3-cmdkit
Summary:        %{summary}

%description -n python3-cmdkit
%summary


%prep
%autosetup -p1 -n CmdKit-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files cmdkit


%check
%pytest


%files -n python3-cmdkit -f %{pyproject_files}
%doc README.*
%license LICENSE


%changelog
* Tue Dec 31 2024 Jonathan Wright <jonathan@almalinux.org> - 2.7.7-1
- update to 2.7.7

* Tue Dec 10 2024 Jonathan Wright <jonathan@almalinux.org> - 2.7.6-1
- initial package release rhbz#2327938
