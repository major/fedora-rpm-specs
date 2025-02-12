%global desc %{expand:
REQUest REcordingRequre [rekure] - Is Library for storing output of various
function and methods to persistent storage and be able to replay the stored
output to functions.}


Name:           python-requre
Version:        0.8.6
Release:        1%{?dist}
Summary:        Python library that allows re/store output of various objects for testing

License:        MIT
URL:            https://github.com/packit/requre
Source0:        %{pypi_source requre}
BuildArch:      noarch

BuildRequires:  python3-devel


%description
%{desc}


%package -n     python3-requre
Summary:        %{summary}


%description -n python3-requre
%{desc}


%prep
%autosetup -n requre-%{version}


%generate_buildrequires
# The -w flag is required for EPEL 9's older hatchling
%pyproject_buildrequires %{?el9:-w}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files requre


%files -n python3-requre -f %{pyproject_files}
# Epel9 does not tag the license file in pyproject_files as a license. Manually install it in this case
%if 0%{?el9}
%license LICENSE
%endif
%doc README.md
%{_bindir}/requre-patch


%changelog
* Mon Feb 10 2025 Packit <hello@packit.dev> - 0.8.6-1
- Trigger a new release to fix the PyPI upload action.

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.8.4-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 07 2024 Packit <hello@packit.dev> - 0.8.4-1
- Provide `__version__` of the package so it can be easily checked when installed on the system.

* Mon Oct 30 2023 Packit <hello@packit.dev> - 0.8.3-1
- Fix an issue of clashing with the _coverage_.
- Packaging has been modernized.

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.8.2-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.8.2-2
- Rebuilt for Python 3.11

* Mon Apr 25 2022 Packit <hello@packit.dev> - 0.8.2-1
- No user-facing changes.

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 18 2021 Frantisek Lachman <flachman@redhat.com> - 0.8.1-2
- Fix the changelog formatting.

* Fri Jun 18 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.8.1-1
- Fix the problem with kwarg decorators that causes the function body not to be executed.

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8.0-2
- Rebuilt for Python 3.10

* Fri May 07 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.8.0-1
- New decorators for handling temporary files (MkTemp) and directories (MkDTemp) in a more transparent way.
- The old implementation based on static paths and counter has been deprecated.

* Fri Apr 30 2021 Hunor Csomortáni <csomh@redhat.com> - 0.7.1-1
- Fix a performance issue when detecting cassettes following the old naming format.

* Fri Mar 12 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.7.0-1
- New version of requre 0.7.0 (Jan Ščotka)
- Workflow for uploading release to PyPI (Jiri Popelka)
- fix the name of storage file for unittest, use just class.method.yaml (Jan Ščotka)
- [pre-commit.ci] pre-commit autoupdate (pre-commit-ci[bot])

* Mon Mar 01 2021 Jan Ščotka <jscotka@redhat.com> - 0.6.1-1
- version increased (Jan Ščotka)
- test Tuple type (Jan Ščotka)
- add tuple as base simple type (Jan Ščotka)
- [pre-commit.ci] pre-commit autoupdate (pre-commit-ci[bot])

* Tue Feb 16 2021 Jan Ščotka <jscotka@redhat.com> - 0.6.0-1
- release new version 0.6.0 (Jan Ščotka)
- Cleanup import system (#152) (jscotka)
- improve failing test (Jan Ščotka)
- prepare code before next cleanup (Jan Ščotka)
- remove unused type of decoration and it was outtaded (Jan Ščotka)
- [pre-commit.ci] pre-commit autoupdate (pre-commit-ci[bot])
- Don't recommend to use 'pip' with 'sudo' (Hunor Csomortáni)
- Change 'master' to 'main' (Hunor Csomortáni)
- [pre-commit.ci] pre-commit autoupdate (pre-commit-ci[bot])
- small issue with setting up storage mode debug (Jan Ščotka)
- Bump Version in fedora/python-requre.spec (Jiri Popelka)
- [pre-commit.ci] pre-commit autoupdate (pre-commit-ci[bot])
- [pre-commit.ci] pre-commit autoupdate (pre-commit-ci[bot])
- [pre-commit.ci] pre-commit autoupdate (pre-commit-ci[bot])
- add backward compatibility to files (Jan Ščotka)
- improve file operations with guess if not given (Jan Ščotka)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 08 2020 Packit Service <user-cont-team+packit-service@redhat.com> - 0.5.0-1
- apply PR suggestion (Jan Ščotka)
- add default decorator and test (Jan Ščotka)
- guess proper return object type based on  return value (Jan Ščotka)
- Link our common contribution guidelines (Matej Focko)
- Fix mypy remark (Matej Focko)
- Move rebase check from pre-commit to pre-push hook (Matej Focko)
- Update docs/filter_format.rst (jscotka)
- Update docs/filter_format.rst (jscotka)
- Update docs/filter_format.rst (jscotka)
- Update docs/filter_format.rst (jscotka)
- Update docs/filter_format.rst (jscotka)
- Update docs/filter_format.rst (jscotka)
- update documentation (Jan Ščotka)
- fix examples (Jan Ščotka)
- fix ip addr and DNS issue inside tests (Jan Ščotka)
- Do not skip bug and security issues by stalebot (Frantisek Lachman)
- Do not run tests for zuul gating (Frantisek Lachman)
- Add more specific type for __replace_module_match_with_multiple_decorators (Frantisek Lachman)
- fix mistake (Jan Ščotka)
- Update requre/modules_decorate_all_methods.py (jscotka)
- apply PR suggestions (Jan Ščotka)
- Allow to use list as parameter for decoratos and add common aliases for decorators. (Jan Ščotka)
- Update pre-commit configuration for prettier (Hunor Csomortáni)
- Copy modules when listing to avoid changes during execution (Frantisek Lachman)
- adapt PR review issues (Jan Ščotka)
- optimise files handling, avoid duplication of stored files in test_data files (Jan Ščotka)
- Document installation instructions in README (Frantisek Lachman)
- Enable all fedora targets for master/release copr builds (Frantisek Lachman)
- Use default packit COPR projects (Frantisek Lachman)

* Tue Sep 22 2020 Packit Service <user-cont-team+packit-service@redhat.com> - 0.4.0-1
- new upstream release: 0.4.0

* Mon Sep 21 2020 Jan Ščotka <jscotka@redhat.com> - 0.3.0-1
- new upstream release: 0.3.0

* Wed Jan 15 2020 Jan Ščotka <jscotka@redhat.com> - 0.2.0-1
- Initial package.
