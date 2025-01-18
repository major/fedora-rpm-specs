Name:           firmitas
Version:        0.1.4
Release:        2%{?dist}
Summary:        Simple notification service for X.509-standard TLS certificate statuses

License:        GPL-3.0-or-later
Url:            https://gitlab.com/t0xic0der/firmitas
Source0:        %{pypi_source firmitas}

BuildArch:      noarch

BuildRequires:  python3-devel

%description
Simple notification service for X.509-standard TLS certificate statuses

%prep
%autosetup -p 1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files firmitas

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/firmitas

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 27 2024 Akashdeep Dhar <t0xic0der@fedoraproject.org> - 0.1.4-1
- Attempt fixing the FTBFS RHBZ#2307964
- More information on https://github.com/fedora-infra/firmitas/releases/tag/v0.1.4

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 03 2024 Akashdeep Dhar <t0xic0der@fedoraproject.org> - 0.1.3-1
- Project moved from GitLab to GitHub (gridhead/firmitas to fedora-infra/firmitas)
- Add CI workflow for the project
- Automated dependency update - Bump requests from 2.31.0 to 2.32.2
- Automated dependency update - Bump urllib3 from 1.26.18 to 1.26.19
- Automated dependency update - Bump cryptography from 41.0.7 to 42.0.4

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.1.2-6
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.1.2-2
- Rebuilt for Python 3.12

* Thu Jun 08 2023 Akashdeep Dhar <t0xic0der@fedoraproject.org> - 0.1.2-1
- Made cosmetic changes to the RPM spec file
- Removed the version information from the changelog section of the RPM spec file
- Removed unnecessary macros from the RPM spec file
- Removed "pyproject-rpm-macros" from the build requirements section
- Switched license tag over to an SPDX identifier
- Raised the upper bound on "cryptography" runtime dependency
- Updated the dependency lockfile to the most recent versions

* Tue Jun 06 2023 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 0.1.1-2
- Cosmetic RPM specfile changes

* Thu Jun 01 2023 Akashdeep Dhar <t0xic0der@fedoraproject.org> - 0.1.1-1
- Stepped down dependency version requirements for EPEL9 compatibility
- Rework the RPM specfile to include support for EPEL9 release

* Thu Jun 01 2023 Akashdeep Dhar <t0xic0der@fedoraproject.org> - 0.1.0-1
- Added notification support for ticketing repositories on Pagure
- Added checking for the validity of X.509-standard TLS certificates
- Introduced configuration mapping for the notification service
- Introduced configuration mapping for the X.509-standard TLS certificates
