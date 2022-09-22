Name:           python-pyupgrade
Version:        2.38.0
Release:        1%{?dist}
Summary:        A tool to upgrade syntax of Python code for newer versions of the language

License:        MIT
URL:            https://github.com/asottile/pyupgrade
Source:         %{url}/archive/v%{version}/pyupgrade-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
# Testing requirements
# covdefaults (from tox.ini -> requirements-dev.txt) is not packaged
# for Fedora, using pytest directly
BuildRequires:  python3dist(pytest)

%global _description %{expand:
A tool to upgrade syntax of Python code for newer versions of the language.}

%description %_description

%package -n python3-pyupgrade
Summary:        %{summary}

%description -n python3-pyupgrade %_description


%prep
%autosetup -p1 -n pyupgrade-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pyupgrade


%check
%pytest


%files -n python3-pyupgrade -f %{pyproject_files}
%doc README.md
%{_bindir}/pyupgrade


%changelog
* Mon Sep 19 2022 Roman Inflianskas <rominf@aiven.io> - 2.38.0-1
- Update to 2.38.0 (resolves rhbz#2127202)

* Thu Jul 28 2022 Roman Inflianskas <rominf@aiven.io> - 2.37.3-1
- Update to 2.37.3

* Mon Jul 25 2022 Roman Inflianskas <rominf@aiven.io> - 2.37.2-1
- Initial package

