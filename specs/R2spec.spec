Name:           R2spec
Version:        6.0.0
Release:        %autorelease
Summary:        Python script to generate R spec files and RPMs

License:        GPL-3.0-or-later
URL:            https://pagure.io/r2spec
Source0:        https://releases.pagure.org/r2spec/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
Requires:       mock
Provides:       R2rpm

%description
R2spec is a small python tool that generates spec files for R packages.
R2spec provides R2rpm which generates RPM binaries for R packages using
the R2spec API.

%prep
%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files r2spec
install -Dpm 644 docs/R2*.1 -t %{buildroot}/%{_mandir}/man1/

%check
%pytest

%files -f %{pyproject_files}
%doc README.md CHANGELOG
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/R2rpm
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/R2rpm.1*

%changelog
%autochangelog
