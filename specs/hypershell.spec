Name:           hypershell
Version:        2.7.0
Release:        1%{?dist}
Summary:        Utility for processing shell commands over a distributed, asynchronous queue

License:        Apache-2.0
URL:            https://hypershell.org
Source:         https://github.com/hypershell/hypershell/archive/%{version}/hypershell-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

# for tests
BuildRequires:  python3-pytest
BuildRequires:  python3-yaml
BuildRequires:  sqlite

%global _description %{expand:
Elegant, cross-platform, high-throughput computing utility
for processing shell commands over a distributed, asynchronous queue.
Highly scalable workflow automation tool for many-task scenarios.
}

%description %_description


%prep
%autosetup
# loosen sqlalchemy requirement a little for el10
sed -i 's/"sqlalchemy>=2.0.29"/"sqlalchemy>=2.0.26"/g' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x postgres
%pyproject_extras_subpkg -n python3-hypershell postgres


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files hypershell

install -pDm 0644 share/man/man1/hsx.1 %{buildroot}%{_mandir}/man1/hsx.1
install -pDm 0644 share/man/man1/hyper-shell.1 %{buildroot}%{_mandir}/man1/hyper-shell.1

%check
%pytest


%files -f %{pyproject_files}
%doc README.*
%license LICENSE
%exclude %{_bindir}/hs
%{_bindir}/hsx
%{_bindir}/hyper-shell
%{_mandir}/man1/hsx.1*
%{_mandir}/man1/hyper-shell.1*


%changelog
* Wed May 28 2025 Jonathan Wright <jonathan@almalinux.org> - 2.7.0-1
- initial package build rhbz#2332450
