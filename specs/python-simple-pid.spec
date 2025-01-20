Name:		python-simple-pid
Version:	2.0.0
Release:	4%{?dist}
Summary:	A PID (proportional–integral–derivative) controller in Python

License:	MIT
URL:		https://github.com/m-lundberg/simple-pid
Source0:	%{pypi_source simple-pid}

BuildArch:	noarch
BuildRequires:	python3-devel
BuildRequires:	python3-pytest

%global _description %{expand:
A simple and easy to use PID controller in Python. If you want a PID
controller without external dependencies that just works, this is for you!
The PID was designed to be robust with help from Brett Beauregards guide.}

%description %_description

%package -n python3-simple-pid
Summary:	A PID (proportional–integral–derivative) controller in Python

%description -n python3-simple-pid %_description

%prep
%autosetup -p1 -n simple-pid-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest

%files -n python3-simple-pid
%license LICENSE.md
%doc README.md
%{python3_sitelib}/simple_pid/
%{python3_sitelib}/simple_pid-%{version}.dist-info/

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.0.0-2
- Rebuilt for Python 3.13

* Sat Dec 30 2023 Tomasz Torcz <ttorcz@fedoraproject.org> - 2.0.0-1
- initial package version
