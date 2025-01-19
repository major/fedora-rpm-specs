%global pkgname pagure-exporter
%global srcname pagure_exporter
%global desc Simple exporter tool that helps migrate repository files, data assets and issue tickets from projects on Pagure to GitLab

Name:           %{pkgname}
Version:        0.1.3
Release:        4%{?dist}
Summary:        %{desc}

License:        GPL-3.0-or-later
Url:            https://github.com/gridhead/%{pkgname}
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
%{desc}

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.1.3-2
- Rebuilt for Python 3.13

* Wed Mar 13 2024 Packit <hello@packit.dev> - 0.1.3-1
- Add some installability checks (Akashdeep Dhar)
- Update Packit configuration (Akashdeep Dhar)
- Step down the version requirement for python-gitlab (Akashdeep Dhar)
- Bump version from v0.1.2 to v0.1.3 (fedohide-origin)
- Automated dependency updates (renovate[bot])
- add fedora-rawhide & fedora-40 aliases to packit jobs config (Shubham Karande)
- Change the recordings after the GitLab Runners tokens were purged (Akashdeep Dhar)
- Remove stray GitLab Runners token when detected (Akashdeep Dhar)
- Remove stray IntelliJ files (Akashdeep Dhar)
- Rework the testcases to address cleaning of repositories (Akashdeep Dhar)
- Add refreshed recordings for the newly added functionalities (Akashdeep Dhar)
- Include view and work code for retaining issue ticket order (Akashdeep Dhar)
- Add options and variables to track the new feature (Akashdeep Dhar)
- Update dependency ruff to ^0.0.285 || ^0.1.0 || ^0.2.0 || ^0.3.0 (renovate[bot])
- Rework the recordings to address the changed tests (Akashdeep Dhar)
- Clean statutory rate limit addressing functions (Akashdeep Dhar)
- Automated dependency updates (renovate[bot])
- Automated dependency updates (renovate[bot])
- Update recordings to speed up the testing process (Akashdeep Dhar)
- Change the testcases to accommodate the shift (Akashdeep Dhar)
- Modify the condition config for the test environment (Akashdeep Dhar)
- Replace scoped client object in favor for contextualized client object (Akashdeep Dhar)
- Introduce two shared variables to contextualize GitLab client and project objects (Akashdeep Dhar)
- Move repository checking code from requests to python-gitlab (Akashdeep Dhar)
- update_doc_use_venv_instead_of_virtualenv (ooooo)
- Complete first run of refactoring (Akashdeep Dhar)
- Add python-gitlab in dependencies (Akashdeep Dhar)
- Automated dependency updates (renovate[bot])
- Update dependency ruff to ^0.0.285 || ^0.1.0 || ^0.2.0 (renovate[bot])
- Update dependency black to v24 (renovate[bot])
- Update dependency pytest to v8 (renovate[bot])
- Automated dependency updates (renovate[bot])
- Automated dependency updates (renovate[bot])
- Automated dependency updates (renovate[bot])
- Resolves rhbz#2269273

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild


* Mon Dec 11 2023 Akashdeep Dhar <t0xic0der@fedoraproject.org> - 0.1.2-1
- Expanded the documentation to explain branch protection
- Censor the sensitive information from STDOUT
- Add support for automatic dependency updates using Renovate
- Circumvent the rate limits on the GitLab API requests
- Added support for migrating issue ticket confidentiality
- Added advanced HTTP requests testing support using VCR.py
- Added configuration to avoid false security flagging

* Thu Oct 19 2023 Akashdeep Dhar <t0xic0der@fedoraproject.org> - 0.1.1-1
- Reworked the documentation sections with proper updates
- Initialized packaging workflow with RPM specfile for the project codebase
- Stepped down version of the runtime dependency requests from ^2.31.0 to ^2.28.0
- Stepped down version of the runtime dependency GitPython from ^3.1.37 to ^3.1.0
- Removed unnecessary runtime dependency tqdm from the list

* Tue Oct 17 2023 Akashdeep Dhar <t0xic0der@fedoraproject.org> - 0.1.0-1
- Created the initial release of the project
- Added support for transferring repositories files from projects on Pagure to GitLab
- Added support for transferring issue tickets from projects on Pagure to GitLab
- Added support for inbuilt logging library for better compatibility with journalling
- Added options for filtering by branch names when transferring repository files
- Added options for filtering by issue ticket status when transferring issue tickets
- Added options for filtering by issue ticket identity selection when transferring issue tickets
- Added options for filtering by issue ticket identity ranges when transferring issue tickets
- Added options for migrating current states when transferring issue tickets
- Added options for migrating tagged labels when transferring issue tickets
- Added options for migrating created comments when transferring issue tickets
- Ensured excellent quality of the codebase with 100% coverage of functional code
- Included support for continuous integration using GitHub Actions and Pre-Commit CI
