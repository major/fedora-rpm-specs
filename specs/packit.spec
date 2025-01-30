# Testing dependencies: deepdiff, flexmock are missing on EPEL 9. Cannot use testing environment
%if 0%{?el9}
%bcond_with tests
%else
%bcond_without tests
%endif

Name:           packit
Version:        1.0.1
Release:        1%{?dist}
Summary:        A tool for integrating upstream projects with Fedora operating system

License:        MIT
URL:            https://github.com/packit/packit
Source0:        %{pypi_source packitos}
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(click-man)
Requires:       python3-packit = %{version}-%{release}

%description
This project provides tooling and automation to integrate upstream open source
projects into Fedora operating system.

%package -n     python3-packit
Summary:        %{summary}
# new-sources
Requires:       fedpkg
Requires:       git-core
# kinit
Requires:       krb5-workstation
# rpmbuild
Requires:       rpm-build
# bumpspec
Requires:       rpmdevtools
# Copying files between repositories
Requires:       rsync

Recommends:       osh-cli

%description -n python3-packit
Python library for Packit,
check out packit package for the executable.


%prep
%autosetup -n packitos-%{version}


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x testing}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files packit
PYTHONPATH="%{buildroot}%{python3_sitelib}" click-man packit --target %{buildroot}%{_mandir}/man1

install -d -m 755 %{buildroot}%{bash_completions_dir}
cp files/bash-completion/packit %{buildroot}%{bash_completions_dir}/packit


%files
%license LICENSE
%{_bindir}/packit
%{_mandir}/man1/packit*.1*
%{bash_completions_dir}/packit

%files -n python3-packit -f %{pyproject_files}
# Epel9 does not tag the license file in pyproject_files as a license. Manually install it in this case
%if 0%{?el9}
%license LICENSE
%endif
%doc README.md

%changelog
* Sun Jan 26 2025 Packit <hello@packit.dev> - 1.0.1-1
- `version_update_mask` now applies to EPEL dist-git branches in the same way it does to stable Fedora branches. (#2507)
- Resolves: rhbz#2342176

* Mon Jan 20 2025 Packit <hello@packit.dev> - 1.0.0-1
- Job type `build` removed after deprecation, is now `copr_build`.
- Job type `production_build` removed after deprecation, is now `upstream_koji_build`.
- Key `upstream_project_name` removed after deprecation, is now `upstream_package_name`.
- Key `synced_files` removed after deprecation, is now `files_to_sync`.
- Resolves: rhbz#2338988

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.106.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 16 2024 Packit <hello@packit.dev> - 0.106.0-1
- We have added a `--resultdir` option for building in mock via our CLI (`packit build in-mock`). (#2475)
- Resolves: rhbz#2332425

* Fri Dec 06 2024 Packit <hello@packit.dev> - 0.105.0-1
- There is a new action/hook, `post-modifications`, that is executed after all modifications to the spec file are done and in case of syncing release after all remote sources are downloaded and before uploading to lookaside cache. You can use it for example to construct an additional source that depends on the primary source (that may not yet be available in other actions). (#2474)
- Resolves: rhbz#2330760

* Mon Nov 25 2024 Packit <hello@packit.dev> - 0.104.1-1
- Packit now uses the fedora-distro-aliases library to expand Fedora aliases. This is Packit's original code being improved and properly maintained by the Copr team. For further suggestions about aliases, use github.com/rpm-software-management/fedora-distro-aliases.
- Resolves: rhbz#2328698

* Fri Nov 15 2024 Packit <hello@packit.dev> - 0.104.0-1
- Packit configuration file can now have a placeholder top-level key `_` that is ignored when read.
  This is useful for storing yaml anchors in complex config files, e.g.:
```yaml
_:
  base-test: &base-test
    job: tests
    fmf_path: .distro
jobs:
  - <<: *base-test
    trigger: pull_request
    manual_trigger: true
  - <<: *internal-test
    trigger: commit
    use_internal_tf: true
```
(#2378)
- You can now define `with_opts` and `without_opts` in target-specific configuration of `copr_build` job to build with `--with` and `--without` rpmbuild options. (#2463)
- Resolves: rhbz#2325040

* Sun Nov 10 2024 Packit <hello@packit.dev> - 0.103.0-1
- Packit now supports and defaults to `fast_forward_merge_into` syntax via `--dist-git-branches-mapping` in `dist-git init`. (#2456)

* Tue Oct 22 2024 Packit <hello@packit.dev> - 0.102.2-1
- Fixed passing list of resolved bugs when running `packit propose-downstream` or `packit pull-from-upstream`. (#2447)
- Resolves: rhbz#2321004

* Fri Oct 11 2024 Packit <hello@packit.dev> - 0.102.1-1
- We have fixed an issue that was introduced during the unification of the interface for passing resolved Bugzillas / Jira tickets to the `sync-release` or `bodhi_update` jobs. (#2442)
- `packit validate-config` now checks for the existence of downstream package. (#2436)
- Packit now allows building VM images via CLI without any Copr repository specified. (#2434)
- Resolves: rhbz#2318003

* Fri Oct 04 2024 Packit <hello@packit.dev> - 0.102.0-1
- Check for `upstream_project_url` presence in the configuration when `pull_from_upstream` job is configured was removed from `validate-config`, as this is no longer required. (#2423)
- `packit init` now adds working directories that are used in `packit prepare-sources` into the `.gitignore` file in the same directory where Packit config resides. (#2431)
- Previously, `create-update` command took `--resolve-bugzillas` option and `propose-downstream` command took `--resolve-bug` option. The options have been unified into `--resolve-bug` for better user experience. If you used `create-update` with `--resolve-bugzillas` you have to use `--resolve-bug` (or shorthand `-b`) now instead. (#2428)
- Resolves: rhbz#2316445

* Wed Sep 18 2024 Packit <hello@packit.dev> - 0.101.1-1
- In the user configuration file, it's possible to set `default_parse_time_macros`, e.g. might be helpful in situations like [packit/packit-service#2514](https://github.com/packit/packit-service/issues/2514). (#2408)
- Packit now allows to configure mock bootstrap feature setup of Copr projects with a new `bootstrap` configuration option. (#2411)
- Resolves: rhbz#2313250

* Fri Sep 06 2024 Packit <hello@packit.dev> - 0.101.0-1
- Packit now supports passing custom arguments to various static analyzers through `--csmock-args` CLI option and `csmock_args` configuration. (#2402)
- When synching a new release Packit is now able to fast forward a specified merge to a configured list of branches.
  Use the `dist_git_branches` new syntax as in this example:
  `{"rawhide": {"fast_forward_merge_into": ["f40"]}, "fedora-stable": {}}` (#2363)
- Resolves: rhbz#2310376

* Sat Aug 24 2024 Packit <hello@packit.dev> - 0.100.3-1
- `dist-git init` command now allows `upstream-git-url` not to be specified. (#2387)
- Resolves: rhbz#2306481

* Thu Aug 15 2024 Packit <hello@packit.dev> - 0.100.2-1
- Update to version 0.100.2
- Resolves: rhbz#2300464

* Thu Aug 01 2024 Packit <hello@packit.dev> - 0.100.1-1
- Dummy release to test the "build in side tags" new feature!
- Resolves: rhbz#2300464

* Mon Jul 29 2024 Packit <hello@packit.dev> - 0.100.0-1
- `packit pull-from-upstream` now allows omitting `upstream_project_url` in the configuration in which case the interaction with the upstream repository is skipped during release syncing. (#2354)
- We have implemented a CLI support for Koji builds against CBS Koji instance. (#2267)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jul 12 2024 Packit <hello@packit.dev> - 0.99.0-1
- Update to version 0.99.0

* Thu Jul 04 2024 Packit <hello@packit.dev> - 0.98.0-1
- Packit now updates its own, not yet merged, pull requests instead of creating new ones for new releases. (#2204)
- Resolves: rhbz#2295821

* Fri Jun 21 2024 Packit <hello@packit.dev> - 0.97.3-1
- We have fixed a bug that caused inconsistency between the promised environment variables (from the docs) and the environment that has been actually provided. Now you should have access to `PACKIT_UPSTREAM_REPO` and `PACKIT_DOWNSTREAM_REPO`, if they have been cloned already, in the `post-upstream-clone` action. (#2327)
- Resolves: rhbz#2293661

* Mon Jun 17 2024 Nikola Forró <nforro@redhat.com> - 0.97.2-2
- Rebuilt for Python 3.13
- Resolves: rhbz#2291573

* Thu Jun 06 2024 Packit <hello@packit.dev> - 0.97.2-1
- We have fixed the syncing of ACLs for `propose-downtream` for CentOS Stream. (#2318)
- Resolves: rhbz#2290733

* Fri May 17 2024 Packit <hello@packit.dev> - 0.97.1-1
- We have fixed the behaviour for `dist-git init` command when `upstream-git-url` argument is specified.
- Resolves: rhbz#2278839

* Wed May 15 2024 Packit <hello@packit.dev> - 0.97.0-1
- Add a `scan-in-osh` subcommand in the CLI to perform a scan through OpenScanHub. By default, it performs a full scan of the packages and a differential scan can be performed through `--base-srpm` option. (#2301)
- When running `dist-git init` command from CLI, you can pass a command to specify a git URL of the project. (#2308)

* Mon Apr 22 2024 Packit <hello@packit.dev> - 0.95.0-1
- `packit dist-git init` now allows specifying `--version-update-mask` option and also any arbitrary top-level configuration options. (#2288)
- We have fixed Packit auto-referencing Upstream Release Monitoring bug for release syncing to CentOS Stream. (#2284)
- Resolves: rhbz#2276194

* Mon Apr 08 2024 Packit <hello@packit.dev> - 0.94.2-1
- Packit previously put the "[packit]" string as a prefix in the subject of pull-from-upstream commits. Now the prefix is no longer there - this is made unnecessary noise in autochangelog. This affects the default. Custom action can still override this behavior. (#2263)
- We have fixed a race condition that could occur when multiple `copr_build` jobs sharing a Copr project but having different targets were running at the same time. (#2274)
- Resolves: rhbz#2273977

* Thu Mar 28 2024 Packit <hello@packit.dev> - 0.94.1-1
- `packit validate-config` now checks whether `upstream_project_url` is set if `pull_from_upstream` job is configured. (#2254)
- `Resolves` is changed to `Resolves:` for the dist-git commit since that's the correct format for CentOS Stream 9. (#2260)
- Resolves: rhbz#2272077

* Sun Mar 17 2024 Packit <hello@packit.dev> - 0.94.0-1
- Added new configuration options `status_name_template` and `allowed_builders`.
- Resolves rhbz#2266037

* Mon Feb 26 2024 Packit <hello@packit.dev> - 0.93.0-1
- Packit now checks the version to propose against the version in specfile and doesn't create downgrade PRs. (#2239)

* Mon Feb 19 2024 Packit <hello@packit.dev> - 0.92.0-1
- Packit now supports `trigger: ignore` which can be used for templating by using the YAML. (#2234)
- Packit now searches for bugzilla about new release created by Upstream Release Monitoring to reference each time it syncs the release downstream. (#2229)
- Resolves rhbz#2264878

* Wed Feb 07 2024 Packit <hello@packit.dev> - 0.91.0-1
- We have introduced new CLI command `packit dist-git init` that initializes Packit configuration for release automation in dist-git repository. (#2225)
- `packit validate-config` now checks whether the Upstream Release Monitoring for the package is correctly configured if `pull_from_upstream` job is present in the configuration. (#2226)
- There is a new global configuration option `parse_time_macros` that allows to configure macros to be explicitly defined or undefined at spec file parse time. (#2222)
- Resolves rhbz#2259201

* Sun Jan 28 2024 Packit <hello@packit.dev> - 0.90.0-1
- `pull-from-upstream` and `propose-downstream` commands now have the `--sync-acls` option that enables syncing the ACLs between dits-git repo and fork. The default behaviour was, however, changed to not sync the ACLs. (#2214)
- Packit now properly handles exceptions when syncing ACLs during release syncing. (#2213)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.89.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Packit <hello@packit.dev> - 0.89.0-1
- We have fixed a bug in handling chroot-specific configuration once the chroots themselves are updated. (#2194)

* Sun Jan 07 2024 Packit <hello@packit.dev> - 0.88.0-1
- We have fixed a bug preventing the release from being synced downstream if the changelog to be set is empty. (#2183)
- Resolves rhbz#2257183

* Thu Nov 30 2023 Packit <hello@packit.dev> - 0.87.1-1
- Packit now links the information related to upstream in PRs opened when syncing a release. (#2173)
- Resolves rhbz#2252328

* Fri Nov 24 2023 Packit <hello@packit.dev> - 0.87.0-1
- Packit now correctly sets the specfile content (e.g. changelog entry) even if it syncs the specfile from upstream the first time. (#2170)
- Packit now supports pre-release version in `propose_downstream` and `pull_from_upstream`. A spec file update might be required, see the documentation for more details. (#2149)
- Resolves rhbz#2251367

* Mon Nov 20 2023 Packit <hello@packit.dev> - 0.86.2-1
- Packit _0.86.1_ was not released on PyPI due to an internal bug, it should be fixed in this release.

* Mon Oct 30 2023 Packit <hello@packit.dev> - 0.85.0-1
- Packit no longer downloads sources excluded using spec file conditions. (#2132)

* Mon Oct 16 2023 Packit <hello@packit.dev> - 0.84.0-1
- We have adjusted how we include the resolved bugzillas in the commit messages created when syncing the release downstream so that the resolved bugzillas are included in changelog when using %%autochangelog. (#2126)
- Packit now properly cleans up the branch after syncing the release which should prevent unwanted files (e.g.tarballs) being committed in dist-git. (#2125)
- Packit no longer accepts `packit.json` or `.packit.json` as a configuration file name. (#2123)
- Packit now updates ACL of a dist-git fork when creating dist-git PRs to allow users and groups with commit rights to the original dist-git repo to push directly to a source branch. (#2112)
- We have fixed an issue that prevented you from running the jobs on the GitLab.com due to failing resolution of the upstream/downstream relationship for the cloned project. (#2120)
- We have fixed an issue that you could encounter when running the Packit from the CLI that caused misinterpretation of the repository to be an upstream repo instead of a downstream. (#2117)
- Resolves rhbz#2244381

* Fri Oct 06 2023 Packit <hello@packit.dev> - 0.83.0-1
- We have fixed an issue that prevented automated allowlisting in the Packit Service. (#2113)
- Packit now also detects resolved bugs in the default update notes (created from changelog diff) and assigns these when submitting the Bodhi updates. (#2111)
- Packit now exports `PACKIT_UPSTREAM_PACKAGE_NAME`, `PACKIT_DOWNSTREAM_PACKAGE_NAME` and `PACKIT_CONFIG_PACKAGE_NAME` also in the `changelog_entry` action. (#2103)

* Fri Sep 29 2023 Packit <hello@packit.dev> - 0.82.0-1
- You can now specify bugs resolved by an update by `-b` or `--resolve-bug` option for `propose-downstream` and `pull-from-upstream` commands. The values will be added by default to the changelog and commit message and provided in `commit-message` and `changelog-entry` actions as `PACKIT_RESOLVED_BUGS` env variable. (#2094)
- Resolves rhbz#2240355

* Sat Sep 23 2023 Packit <hello@packit.dev> - 0.81.0-1
- Packit now supports the `pkg_tool` option in the config (at the top-level or with specific packages when using the monorepo syntax). This option can be used for switching between `fedpkg` or `centpkg`. (#2085)
- When updating the `Version` tag during `propose_downstream` or `pull_from_upstream`, Packit now tries to update referenced macros (if any) rather than overwriting the references. (#2087)
- If you have concerns about Packit uploading new archives to lookaside cache before creating a pull request, you can newly set `upload_sources` to False to disable this. (#2086)
- We have fixed a bug that could cause duplicit PRs to be created when using the `commit-message` action. (#2080)
- Packit now supports `commit-message` action that can be used to override the default commit message produced by Packit during `propose-downstream` or `pull-from-upstream`. Please pay attention to our [documentation](https://packit.dev/docs/configuration/actions#commit-message) with regards to the usage of this action. (#2070)

* Fri Sep 08 2023 Packit <hello@packit.dev> - 0.80.0-1
- Packit CLI now provides a new command `pull-from-upstream`, offering the same functionality as `propose-downstream` but suited for usage from the dist-git repository with Packit configuration placed there. This was primarily added to help reproduce the behaviour of the service's [pull_from_upstream job](https://packit.dev/docs/configuration/downstream/pull_from_upstream). (#2063)
- Packit now exposes `PACKIT_PACKAGE_NAME`, `PACKIT_UPSTREAM_PACKAGE_NAME` and `PACKIT_DOWNSTREAM_PACKAGE_NAME` environment variables to all actions. (#2061)
- We have fixed a bug in `packit source-git init` caused by changed behaviour in a newer version of rpmbuild. (#2048)

* Mon Aug 07 2023 Packit <hello@packit.dev> - 0.78.2-1
- Packit's license in RPM specfile is now confirmed to be SPDX compatible. (#2026)
- `source-git init --ignore-missing-autosetup` help was improved to be less confusing. (#2016) (#2017)

* Tue Aug 1 2023 Packit <hello@packit.dev> - 0.78.1-1
- Temporarily disabled test dependencies on Fedora Rawhide because of missing `python3-deepdiff`. (#2008)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.77.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jun 17 2023 Packit <hello@packit.dev> - 0.77.0-1
- Packit now includes dist-git branch in the title of the PRs for `propose-downstream` and `pull-from-upstream`. (#1996)
- We have fixed an issue with `files_to_sync` filters not being applied properly. (#1977)

* Fri May 26 2023 Packit <hello@packit.dev> - 0.76.0-1
- Unsuccessful Image Builder requests now provide error details so you can fix the Image configuration. (#1981)
- Copr projects created by Packit will not follow the Fedora branching from now on.
  This decision has been made to lower the load on Copr from the temporary Copr projects created, mainly, for the PR builds.
  If you are releasing your packages to Copr, please use the new setting `follow_fedora_branching`.
  Already existing projects are not affected by this change and it is also not enforced with the custom Copr repositories. (#1970)

* Fri Apr 28 2023 Packit <hello@packit.dev> - 0.75.0-1
- Detection of `%%autorelease` usage in dist-git spec file during `propose-downstream` and `pull-from-upstream` has been improved and Packit will always preserve it. (#1949)
- Changed build tool to hatchling and moved metadata to `pyproject.toml`. (PEP621) (#1913)
- Respect `upstream_ref` for tags that start with "a", "b", "c", "e", "n", "r", "s". This was caused by an issue with a `branches` prefix being treated as a set of letters to remove. (#1943)
- Reset `Release` field in dist-git spec file to `1` when the version in upstream spec file is not up-to-date with the release that triggered `propose_downstream`. (#1940)
- Correctly catch the logs, if any of the user actions fail during the propose-downstream. (#1939)
- `packit source-git` related commands can skip dist-git repos, where the git trailer is not found, when looking for the right dist-git dir where to work. (#1938)
- More monorepo related fixes. (#1946, #1947, #1948)

* Sun Apr 16 2023 Packit <hello@packit.dev> - 0.74.0-1
- Allow configuring tmt tests with fmf root outside of git root. (#1936)
- Removed adding the "Signed-off-by" tag to commits created by Packit. (#1934)
- Packit's source_git functionality installs/loads the `_packitpatch` script in a more reliable manner that doesn't rely on deprecated setuptools functionality. (#1926)

* Thu Apr 06 2023 Packit <hello@packit.dev> - 0.73.0-1
- Packit now supports monorepo configuration in CLI (#1864)

* Fri Mar 31 2023 Packit <hello@packit.dev> - 0.72.0-1
- Packit now preserves `autorelease` macro during `propose_downstream` and `pull_from_upstream`. (#1904)

* Sat Mar 25 2023 Packit <hello@packit.dev> - 0.71.0-1
- `upstream_tag_template` is now also used when looking for the latest version tag in Git. This allows upstream repositories to mix different tag-patterns in the same repository, but consider only one to tell the latest version. (#1891)

* Mon Mar 20 2023 Packit <hello@packit.dev> - 0.70.0-1
- Now packit uses the `get_current_version` action defined by the user to retrieve version before updating the specfile %%setup macro (if any). (#1886)

* Sun Mar 05 2023 Packit <hello@packit.dev> - 0.69.0-1
- `packit validate-config` now correctly checks glob-patterns in `files_to_sync`. (#1865)
- Aliases logic was updated to account for the upcoming Fedora release (Bodhi now marks such release as `frozen`). (#1863)
- Command `packit validate-config` now provides details about errors when it cannot parse the config file. (#1861)
- Packit does fewer API calls when searching for the package configuration file in remote repositories. (#1846)
- `--update-release`/`--no-update-release` now affects only `Release`, not `Version`. (#1857)
- Packit now provides `PACKIT_PROJECT_VERSION` environment variable when running `changelog-entry` action. (#1853)

* Mon Feb 20 2023 Packit <hello@packit.dev> - 0.68.0-1
- Packit now requires bodhi in version 7.0.0 at minimum. (#1844)
- You can now use `--srpm` option with the `packit build locally` CLI command. (#1810)

* Fri Feb 03 2023 Packit <hello@packit.dev> - 0.67.0-1
- Packit now sanitizes changelog messages in order not to break spec file parsing. (#1841)

* Fri Jan 20 2023 Packit <hello@packit.dev> - 0.66.0-1
- When configuring Copr chroot (target in Packit terminology) specific configuration, make sure to specify `additional_modules` as a string containing module names separated with a comma, example: "httpd:2.4,python:4". (#1826)
- Target-specific configuration for Copr builds can now be defined and Packit will set it for the appropriate Copr chroots. (#1822)
- You can now specify `update_release: false` in the configuration to tell Packit not to change the `Version` and `Release` in the spec file. It works the same as `--no-update-release` (renamed from now deprecated `--no-bump`) in the CLI. (#1827)
- Packit now supports setting `module_hotfixes` for Copr projects. (#1829)
- All Copr projects created by Packit now default to `enable_net=False`. Our documentation stated this but it wasn't the case. This is now corrected. (#1825)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.65.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Packit <hello@packit.dev> - 0.65.2-1
- No changes. This is a fixup release for sake of Packit deployment.

* Thu Dec 22 2022 Packit <hello@packit.dev> - 0.65.1-1
- Packit now puts the correct release number into the changelog when the `Release` tag is reset during `propose-downstream`. (#1816)

* Fri Dec 09 2022 Packit <hello@packit.dev> - 0.65.0-1
- Packit now correctly handles a race condition when it tries to create bodhi updates for builds that are not yet tagged properly. CLI exprience was also improved for this case. (#1803)
- Packit now resets the `Release` tag during `propose-downstream` if the version is updated and the `Release` tag has not explicitly been overridden in the upstream specfile. (#1801)

* Fri Dec 02 2022 Packit <hello@packit.dev> - 0.64.0-1
- `packit propose-downstream` now uploads all remote sources (those specified as URLs) and the source specified by `spec_source_id` (whether remote or not) to lookaside. Previously, only Source0 was uploaded.
Source0 is no longer treated specially, but as `spec_source_id` is `Source0` by default, Source0 is still being uploaded by default unless `spec_source_id` is overriden. (#1778)

* Sat Nov 12 2022 Packit <hello@packit.dev> - 0.63.1-1
- Packit now correctly finds SRPM when rpmbuild reports warnings when it parses the spec file. (#1772)
- When packit.yaml is present in the repo but is empty, Packit now produces a better error message instead of an internal Python exception. (#1769)

* Fri Nov 04 2022 Packit <hello@packit.dev> - 0.63.0-1
- Fixed an issue due to which the repository was never searched for a specfile if 'specfile_path' was not specified, and 'specfile_path' was always set to '<repo_name>.spec'. (#1758)
- Packit is now able to generate automatic Bodhi update notes including a changelog diff since the latest stable build of a package. (#1747)

* Thu Oct 27 2022 Packit <hello@packit.dev> - 0.62.0-1
- Fixed an issue with version and release being updated even if `--no-bump` flag was specified. Also fixed an issue when `None` appeared in release instead of a number. (#1753)

* Fri Oct 21 2022 Packit <hello@packit.dev> - 0.61.0-1
- Packit can now correctly authenticate with Bodhi 6 and therefore create Bodhi updates. 🚀 (#1746)
- Packit now requires Python 3.9 or later. (#1745)

* Fri Oct 07 2022 Packit <hello@packit.dev> - 0.60.0-1
- Propose downstream job now pushes changes even when it's not creating a new pull request. This allows updating already existing pull requests. (#1725)

* Fri Sep 16 2022 Packit <hello@packit.dev> - 0.59.1-1
- `packit propose-downstream` is now more informative when sources cannot be downloaded. (#1698)

* Thu Aug 25 2022 Packit <hello@packit.dev> - 0.59.0-1
- Packit CLI can now submit VM images in Red Hat Image Builder.
  All build-related commands have now consistent `--wait`/`--no-wait` options. (#1666)
- No more annoying issues will be created after a successfull propose downstream. (#1693)

* Fri Aug 05 2022 Packit <hello@packit.dev> - 0.57.0-1
- BREAKING CHANGE: fixed an issue where the repo was searched for the specfile before checking if 'downstream_package_name' is set, and '<downstream_package_name>.spec' can be used as the 'specfile_path'. (#1663)

* Thu Jul 28 2022 Packit <hello@packit.dev> - 0.56.0-1
- Packit can now build RPMs in mock. For more information see https://packit.dev/docs/cli/build/mock (#1662)
- Packit now provides a more helpful error message when it hits a known issue while creating a Bodhi update: fedora-infra/bodhi#4660 (#1660)
- Packit now correctly supports `tmt_plan` and `tf_post_install_script` in the configuration. (#1659)
- RPM build commands of Packit CLI have been merged into one build subcommand, for more information see the updated documentation at https://packit.dev/docs/cli/build/. We have also introduced a new `--srpm` option to the new build subcommand that can be used to trigger local, Copr or Koji build from an already built SRPM rather than the one implicitly created by Packit. (#1611)


* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.55.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Packit <hello@packit.dev> - 0.55.0-1
- Packit can now correctly create bodhi updates using the new Bodhi 6 client. (#1651)


* Wed Jun 29 2022 Packit <hello@packit.dev> - 0.54.0-1
- Packit Bash completion file is no longer needlessly executable. (#1634)
- Transition to Bodhi's new authentication mechanism is now fully complete. (#1635)


* Wed Jun 22 2022 Packit <hello@packit.dev> - 0.53.0-1
- Packit now works with Bodhi 5 and Bodhi 6 authentication mechanism. (#1629)
- Git ref name that Packit works with during `propose-downstream` is now made more obvious in logs. (#1626)
- Packit now correctly handles creation of custom archives in root while a specfile is in a subdirectory. (#1622)
- Creation of a Bodhi update will not timeout anymore as Packit is now using a more efficient way of obtaining the latest build in a release. (#1612)

* Tue Jun 21 2022 Python Maint <python-maint@redhat.com> - 0.52.1-2
- Rebuilt for Python 3.11

* Wed Jun 08 2022 Packit <hello@packit.dev> - 0.52.1-1
- Fixed a regression where string values for the `targets` and `dist_git_branches` configuration keys were not accepted. (#1608)

* Thu May 26 2022 Packit <hello@packit.dev> - 0.52.0-1
- Packit will not raise exceptions anymore when creating an SRPM with dangling symlinks. (#1592)
- `packit validate-config` now checks the paths in the package config (path of the specfile,
  paths of the files to be synced) relative to the project path (#1596)
- The name of the temporary branch in `_packitpatch` was normalized which fixed applying the patches during `packit source-git init` (#1593)

* Fri May 13 2022 Packit <hello@packit.dev> - 0.51.0-1
- We have decided to deprecate `metadata` section for job configurations. All
  metadata-specific configuration values can be placed on the same level as the job
  definition. For now we are in a backward-compatible period, please move your settings
  from the `metadata` section. (#1569)
- Packit now correctly removes patches during `packit source-git init` when the
  preamble does not contain blank lines. (#1582)
- `packit source-git` commands learnt to replace Git-trailers in commit
  messages if they already exist. (#1577)
- Packit now supports `--release-suffix` parameter in all of the related CLI
  commands. Also we have added a support for the `release_suffix` option from
  configuration to the CLI. With regards to that we have introduced a new CLI
  switch `--default-release-suffix` that allows you to override the configuration
  option to Packit-generated default option that ensures correct NVR ordering
  of the RPMs. (#1586)


* Thu May 05 2022 Packit <hello@packit.dev> - 0.50.0-1
- When initializing source-git repos, the author of downstream commits created from patch files which are not in a git-am format is set to the original author of the patch-file in dist-git, instead of using the locally configured Git author. (#1575)
- Packit now supports `release_suffix` configuration option that allows you to override the long release string provided by Packit that is used to ensure correct ordering and uniqueness of RPMs built in Copr. (#1568)
- From the security perspective, we have to decided to disable the `create_pr` option for our service, from now on Packit will unconditionally create PRs when running `propose-downstream`.
  We have also updated the `propose-downstream` CLI such that it is possible to use `create_pr` from configuration or override it via `--pr`/`--no-pr` options. (#1563)
- The `source-git update-*` commands now check whether the target repository is pristine and in case not raise an error. (#1562)


* Wed Apr 13 2022 Packit <hello@packit.dev> - 0.49.0-1
- A new configuration option `downstream_branch_name` has been added, which is meant to be used in source-git projects and allow users to customize the name of the branch in dist-git which corresponds to the current source-git branch. (#1555)
- Introduced two new build and test target aliases: `fedora-latest-stable` resolves to the latest stable Fedora Linux release,
  while `fedora-branched` resolves to all branched releases (all Fedora Linux release, except `rawhide`). (#1546)
- When using `post_upstream_clone` to generate your spec-file, Packit now correctly checkouts the release before the action is run. (#1542)

* Wed Mar 30 2022 Packit <hello@packit.dev> - 0.48.0-1
- `packit source-git update-dist-git` and `packit source-git update-source-git` now check the synchronization of source-git and dist-git repositories prior to doing the update. If the update can't be done, for example, because the histories have diverged, the command provides instructions on how to synchronize the repositories. A `--force` option is available to try to update the destination repository anyway.
- Downstream synchronization of the Packit configuration file (aka `packit.yaml`) should be fixed. (#1532)
- Packit will no longer error out when trying to create a new Copr repository when it is already present (caused by a race condition). (#1527)
- Interactions with Bodhi should be now more reliable when creating Bodhi updates. (#1528)

* Thu Mar 17 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 0.47.1-1
- When using Packit CLI for creating Bodhi updates, you can now set `fas_username` and `fas_password`
  in your Packit user config to not be asked about that when the command is executed. (#1517)

* Tue Mar 08 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 0.47.0-1
- When specfile is being generated, and both `specfile_path` and
  `downstream_package_name` are not set, Packit now correctly resolves this
  situation and sets `specfile_path` to the name of the upstream repo suffixed
  with ".spec". (#1499)
- We are now building SRPMs for Packit's own PRs in Copr. For more info see #1490 and
  https://packit.dev/docs/configuration/#srpm_build_deps (#1490)
- All source-git-commands were updated to append a `From-source-git-commit` or `From-dist-git-commit`
  Git-trailer to the commit messages they create in dist-git or source-git, in order to
  save the hash of the commits from which these commits were created. This information
  is going to be used to tell whether a source-git repository is in sync with the
  corresponding dist-git repository. (#1488)
- Spec file and configuration file are no more automatically added to the list of files
  to sync when the `new files_to_sync` option is used. The old `synced_files` option is
  deprecated. (#1483)
- We have added a new configuration option for Copr builds `enable_net` that allows you to
  disable network access during Copr builds. It is also complemented by
  `--enable-net/--disable-net` CLI options if you use Packit locally. (#1504)

* Wed Feb 16 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 0.46.0-1
- Synchronization of default files can now be disabled using a new config
  `files_to_sync`. Key `sync_files` is now deprecated. (#1483)
- Packit now correctly handles colons in git trailer values in source-git commits. (#1478)
- Fedora 36 was added to the static list of `fedora-` aliases. (#1480)


* Fri Feb 04 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 0.45.0-1
- A new `packit source-git update-source-git` command has been introduced for
  taking new changes from dist-git (specified by a revision range) to source-git.
  These may include any changes except source code, patches and `Version` tag
  changes in the spec file. ([packit#1456](https://github.com/packit/packit/pull/1456))
- There's a new configuration option `create_sync_note` that allows you to
  disable creating of README by packit in downstream. ([packit#1465](https://github.com/packit/packit/pull/1465))
- A new option `--no-require-autosetup` for `source-git init` command has been
  introduced. Please note that source-git repositories not using `
%setup       -q
` may
  not be properly initialized. ([packit#1470](https://github.com/packit/packit/pull/1470))




* Thu Jan 20 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 0.44.0-1
- Packit now correctly finds the release, even if you don't use the version as
  the title of the release on GitHub. ([packit#1437](https://github.com/packit/packit/pull/1437))
- Local branches are now named as `pr/{pr_id}` when checking out a PR, even
  when it's not being merged with the target branch. This results in the NVR
  of the build containing `pr{pr_id}` instead of `pr.changes{pr_id}`. ([packit#1445](https://github.com/packit/packit/pull/1445))
- A bug which caused ignoring the `--no-bump` and `--release-suffix` options
  when creating an SRPMs from source-git repositories has been fixed. Packit
  also doesn't touch the `Release` field in the specfile unless it needs to be
  changed (the macros are not expanded that way when not necessary). ([packit#1452](https://github.com/packit/packit/pull/1452))
- When checking if directories hold a Git-tree, Packit now also allows `.git`
  to be a file with a `gitdir` reference, not only a directory. ([packit#1458](https://github.com/packit/packit/pull/1458))

* Wed Dec 08 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.43.0-1
- A new `packit prepare-sources` command has been implemented for preparing                                                                                                                                                                 
  sources for an SRPM build using the content of an upstream repository.                                                                                                                                                                    
  ([packit#1424](https://github.com/packit/packit/pull/1424))                                                         
- Packit now visibly informs about an ongoing cloning process to remove                                                                                                                                                                     
  potential confusion.                                                                                                                                                                                                                      
  ([packit#1431](https://github.com/packit/packit/pull/1431))                                                                                                                                                                               
- The `upstream_package_name` config option is now checked for illegal                                                                                                                                                                      
  characters and an error is thrown if it contains them.                                                                                                                                                                                    
  ([packit#1434](https://github.com/packit/packit/pull/1434))    


* Thu Nov 25 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.42.0-1
- Running `post-upstream-clone` action in `propose-downstream` command was fixed.
  This solves the issue for projects that generate the specfile during this action.
- New config option `env` has been added for specifying environment variables
  used for running tests in the Testing Farm.

* Thu Nov 11 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.41.0-1
- Packit now supports `changelog-entry` action that is used when creating
  SRPM. The action is supposed to generate whole changelog entry (including
  the `-` at the start of the lines) and has a priority over any other way we
  modify the changelog with. (#1367)
- Fixed an issue, which raised an `UnicodeEncodingError`, when working with
  dist-git patch files with an encoding other than UTF-8. (#1406)
- Backup alias definitions now reflect the official release of Fedora Linux 35. (#1405)
- We have introduced a new configuration option `merge_pr_in_ci` that allows
  you to disable merging of PR into the base branch before creating SRPM in
  service. (#1395)
- Fixed an issue, where spec-files located in a sub-directory of upstream
  projects, were not placed in the root of the dist-git repo when proposing
  changes downstream. (#1402)

* Wed Oct 27 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.40.0-1
- Packit will deduce the version for SRPM from the spec file, if there are no git tags or action for acquiring current version defined. (#1388)
- We have introduced new options for generating SRPM packages: (#1396)
  - `--no-bump` that prevents changing of the release in the SRPM, which can be used for creating SRPMs on checked out tags/releases.
  - `--release-suffix` that allows you to customize the suffix after the release number, e.g. reference bugzilla or specific branch of the build.

* Thu Oct 14 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.39.0-1
- Bug in Packit causing issues with local build when the branch was named with prefix rpm has been fixed. (#1380)
- We have added a new option to Packit CLI when creating Bodhi updates, you can use `-b` or `--resolve-bugzillas` and specify IDs (separated by comma, e.g. `-b 1` or `-b 1,2,3`) of bugzillas that are being closed by the update. (#1383)

* Thu Sep 30 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.38.0-1
- `packit validate-config` was updated to check if files to be synced
  downstream are present in the upstream repo and emit a warning in case they
  are missing. (#1366)
- Patch files are read as byte streams now, in order to support having
  non-UTF-8 characters. (#1372)


* Fri Sep 17 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.37.0-1
- `packit source-git` init was updated to try to apply patches with `git am` first, and use `patch` only when this fails, in order to keep the commit message of Git-formatted (mbox) patch files in the source-git history. (#1358)
- Packit now provides `PACKIT_RPMSPEC_RELEASE` environment variable in actions. (#1363)

* Wed Sep 01 2021 Jiri Popelka <jpopelka@redhat.com> - 0.36.0-1
- `status` command has been refactored and now provides much cleaner output. (#1329)
- A log warning is raised if the specfile specified by the user in the config doesn't exist. (#1342)
- Packit by default locally merges checked out pull requests into target branch. Logging for checking out pull requests was improved to contain hashes and summaries of last commit on both source and target branches. (#1344)
- `source-git update-dist-git` now supports using Git trailers to define patch metadata, which will control how patches are generated and added to the spec-file. `source-git init` uses this format to capture patch metadata when setting up a source-git repo, instead of the YAML one. To maintain backwards compatibility, the YAML format is still parsed, but only if none of the patches defines metadata using Git trailers. (#1336)
- Fixed a bug that caused purging or syncing upstream changelog (when not configured) from specfile when running `propose-downstream`. New behavior preserves downstream changelog and in case there are either no entries or no %changelog section present, it is created with a new entry. (#1349)

* Mon Aug 09 2021 Tomas Tomecek <ttomecek@redhat.com> - 0.35.0-1
- Propose-downstream: log when a PR already exists downstream (#1322).
- `packit init` to set spec file path in the config if it's not defined (#1313).
- Make it possible to clone packages from staging dist-git (#1306).
- Source-git: squash patches by patch name - no need to have a dedicated attribute, `squash_commits`, for that (#1309).
- Source-git: look for the config file in .distro/source-git.yaml as well (#1302).
- Source-git: change logging from error to warning when %prep is not using setup (#1317).

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 08 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.34.0-1
- Source-git: `source-git init` was refactored, which also changed and simplified the CLI.

* Thu Jun 24 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.33.1-1
- Release 0.33.1

* Thu Jun 10 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.32.0-1
- Command `packit generate` was removed. It has been deprecated for a while
  in favour of `packit init`. (#1269)
- Packit now explicitly requires git and rpm-build. (#1276)
- Source-git: Patch handling is more consistent. (#1263)
- Source-git: Passing changelog from source-git repo to dist-git was fixed. (#1265)
- Source-git: There is a new `source-git` subcommand, that groups source-git related
  commands `init` and `update-dist-git`. (#1273)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.31.0-2
- Rebuilt for Python 3.10

* Mon May 31 2021 Frantisek Lachman <flachman@redhat.com> - 0.31.0-1
- Downstream package name is set when dist-git path is provided. (#1246)
- A bug with older Python present on Fedora Linux 32 and EPEL 8 is fixed. (#1240)
- There is a new `update-dist-git` subcommand that is
  an improved offline version of `propose-downstream`. (#1228)
- Source-git: Commit metadata newly includes `patch_id`. (#1252)

* Fri May 14 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.30.1-1
 - Fixed a bug caused by new click release. (#1238)

* Fri May 14 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.30.0-1
- Patching: removed location_in_specfile from commit metadata. (#1229)
- Refactored and extended the synced_files mechanism. (#1211)
- Fixed a bug regarding the fedora-latest alias. (#1222)

* Fri Apr 30 2021 Jiri Popelka <jpopelka@redhat.com> - 0.29.0-1
- Source-git: add info about sources to packit.yaml when initiating a new source-git repo
  and don't commit dist-git sources from the lookaside cache. (#1208, #1216)
- Source-git: fix SRPM creation failing with duplicate Patch IDs. (#1206)
- Support git repository cache. (#1214)
- Reflect removed COPR chroots in a COPR project. (#1197)
- Deprecate current_version_command and create_tarball_command. (#1212)
- Fix crashing push-updates command. (#1170)
- Improve fmf/tmt tests configuration. (#1192)

* Wed Mar 31 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.28.0-1
- Remove the no-op `--dry-run` option.
- Handle `centos-stream` targets as `centos-stream-8`, in order to help with the name change in Copr.
- `fmf_url` and `fmf_ref` can be used in a job's `metadata` to specify an external repository and reference to be used to test the package.
- Introduce a `fedora-latest` alias for the latest _branched_ version of Fedora Linux.
- Add a top-level option `-c, --config` to specify a custom path for the package configuration (aka `packit.yaml`).
- Source-git: enable using CentOS Stream 9 dist-git as a source.
- Source-git: rename the subdirectory to store downstream packaging files from `fedora` to the more general `.distro`.
- Source-git: fix creating source-git repositories when Git is configured to call the default branch something other then `master`.

* Thu Mar 18 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.27.0-1
- (Source-git) Several improvements of history linearization.
- (Source-git) Detect identical patches in propose-downstream.
- (Source-git) Patches in a spec file are added after the first empty line below the last Patch/Source.
- Fetch all sources defined in packit.yaml.
- New option to sync only specfile from downstream.

* Thu Mar 04 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.26.0-1
- Fix construction of the Koji tag for epel branches when running `packit create-update`. ([#1122](https://github.com/packit/packit/pull/1122))
- `create-update` now also shows a message about Bodhi requiring the password. ([#1127](https://github.com/packit/packit/pull/1127))
- `packit init` correctly picks up sources from CentOS and fetches specfile from CentOS dist-git. ([#1106](https://github.com/packit/packit/pull/1106))
- Fix translating of the target aliases by treating the highest pending version in Bodhi as `rawhide`. ([#1114](https://github.com/packit/packit/pull/1114))
- The format of Packit logs is unified for all log levels. ([#1119](https://github.com/packit/packit/pull/1119))
- There is a new configuration option `sources` which enables to define sources to override their URLs in specfile.
  You can read more about this in [our documentation](https://packit.dev/docs/configuration/#sources). ([#1131](https://github.com/packit/packit/pull/1131))

* Fri Feb 12 2021 Matej Mužila <mmuzila@redhat.com> - 0.25.0-1
- `propose-update` command now respects requested dist-git branches. ([#1094](https://github.com/packit/packit/pull/1094))
- Improve the way how patches are added to spec file. ([#1100](https://github.com/packit/packit/pull/1100))
- `--koji-target` option of the `build` command now accepts aliases. ([#1052](https://github.com/packit/packit/pull/1052))
- `propose-downstream` on source-git repositories now always uses `--local-content`. ([#1093](https://github.com/packit/packit/pull/1093))
- Don't behave as if `ref` would be always a branch. ([#1089](https://github.com/packit/packit/pull/1089))
- Detect a name of the default branch of a repository instead of assuming it to be called `master`. ([#1074](https://github.com/packit/packit/pull/1074))

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.24.0-1
- No user-facing changes done in this release.

* Thu Jan 07 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.23.0-1
- The `propose-update` has been renamed to `propose-downstream`; `propose-update` is now deprecated
  to unify the naming between CLI and service. ([@jpopelka](https://github.com/jpopelka), [#1065](https://github.com/packit-service/packit/pull/1065))
- Our README has been cleaned and simplified. ([@ChainYo](https://github.com/ChainYo), [#1058](https://github.com/packit-service/packit/pull/1058))
- The :champagne: comment with the installation instructions has been disabled by default. ([@mfocko](https://github.com/mfocko), [#1057](https://github.com/packit-service/packit/pull/1057))
- More information can be found in [our documentation](https://packit.dev/docs/configuration/#notifications).
- Packit is being prepared to be released in EPEL 8 so it can be consumed in RHEL and CentOS Stream. ([@nforro](https://github.com/nforro), [#1055](https://github.com/packit-service/packit/pull/1055))

* Thu Dec 10 2020 Packit Service <user-cont-team+packit-service@redhat.com> - 0.22.0-1
- `packit init` introduces the `--upstream-url` option. When specified,
  `init` also sets up a source-git repository next to creating a configuration file.
- Don't rewrite macros when setting release and version in spec file.
- Fix generation of Copr settings URL for groups.
- Improve processing of the version when proposing a Fedora update.

* Wed Nov 25 2020 Packit Service <user-cont-team+packit-service@redhat.com> - 0.21.0-1
- pre-commit autoupdate (Jiri Popelka)
- 0.21.0 release (Release bot)
- parsing git remote URL: inform what's happening... (Tomas Tomecek)
- Revert "Allow recursive search for specfile in repository" (Matej Focko)
- Regenerate test_data for recursive (Matej Focko)
- Allow recursive search for specfile in repository (Matej Focko)
- cli.copr-build: replace / with - (Tomas Tomecek)
- copr, log CoprException.result when creating repo fails (Tomas Tomecek)
- Delete recipe-tests.yaml (Jiri Popelka)
- Add build to default jobs (lbarcziova)
- Add test case for Upstream._fix_spec_source() (Nikola Forró)
- Fix SpecFile.get_source() (Nikola Forró)

* Fri Nov 13 2020 Packit Service <user-cont-team+packit-service@redhat.com> - 0.20.0-1
- new upstream release: 0.20.0

* Thu Oct 29 2020 Packit Service <user-cont-team+packit-service@redhat.com> - 0.19.0-1
- new upstream release: 0.19.0

* Thu Oct 15 2020 Packit Service <user-cont-team+packit-service@redhat.com> - 0.18.0-1
- new upstream release: 0.18.0

* Thu Oct 01 2020 Packit Service <user-cont-team+packit-service@redhat.com> - 0.17.0-1
- new upstream release: 0.17.0

* Thu Sep 03 2020 rebase-helper <rebase-helper@localhost.local> - 0.16.0-1
- new upstream release: 0.16.0

* Thu Aug 20 2020 Packit Service <user-cont-team+packit-service@redhat.com> - 0.15.0-1
- new upstream release: 0.15.0

* Tue Jul 28 2020 Jiri Popelka <jpopelka@redhat.com> - 0.14.0-1
- new upstream release: 0.14.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Hunor Csomortáni <csomh@redhat.com> - 0.13.1-1
- new upstream release: 0.13.1

* Thu Jul 09 2020 Packit Service <user-cont-team+packit-service@redhat.com> - 0.13.0-1
- new upstream release: 0.13.0

* Wed Jun 24 2020 lbarcziova <lbarczio@redhat.com> - 0.12.0-1
- new upstream release: 0.12.0

* Thu Jun 11 2020 Jan Sakalos <sakalosj@gmail.com> - 0.11.1-1
- new upstream release: 0.11.1

* Thu May 28 2020 Miro Hrončok <mhroncok@redhat.com> - 0.11.0-2
- Rebuilt for Python 3.9

* Thu May 28 2020 Tomas Tomecek <ttomecek@redhat.com> - 0.11.0-1
- new upstream release: 0.11.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.10.1-2
- Rebuilt for Python 3.9

* Thu Apr 16 2020 Jiri Popelka <jpopelka@redhat.com> - 0.10.1-1
- new upstream release: 0.10.1

* Tue Apr 14 2020 Jiri Popelka <jpopelka@redhat.com> - 0.10.0-1
- new upstream release: 0.10.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 21 2019 Frantisek Lachman <flachman@redhat.com> - 0.7.1-1
- new upstream release: 0.7.1

* Fri Oct 04 2019 Frantisek Lachman <flachman@redhat.com> - 0.7.0-1
- new upstream release: 0.7.0

* Thu Sep 12 2019 Jiri Popelka <jpopelka@redhat.com> - 0.6.1-1
- new upstream release: 0.6.1

* Tue Sep 10 2019 Tomas Tomecek <ttomecek@redhat.com> - 0.6.0-1
- new upstream release: 0.6.0

* Mon Aug 26 2019 Tomas Tomecek <ttomecek@redhat.com> - 0.5.1-1
- new upstream release: 0.5.1

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-2
- Rebuilt for Python 3.8

* Fri Aug 02 2019 Packit Service - 0.5.0-1
- new upstream release: 0.5.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 28 2019 Jiri Popelka <jpopelka@redhat.com> - 0.4.2-1
- New upstream release

* Sat May 18 2019 Jiri Popelka <jpopelka@redhat.com> - 0.4.1-1
- Patch release

* Wed May 15 2019 Jiri Popelka <jpopelka@redhat.com> - 0.4.0-1
- New upstream release: 0.4.0
- Build man pages since F30

* Thu Apr 11 2019 Jiri Popelka <jpopelka@redhat.com> - 0.3.0-2
- click-man needs more BuildRequires

* Wed Apr 10 2019 Tomas Tomecek <ttomecek@redhat.com> - 0.3.0-1
- New upstream release: 0.3.0

* Fri Mar 29 2019 Jiri Popelka <jpopelka@redhat.com> - 0.2.0-2
- man pages

* Tue Mar 19 2019 Tomas Tomecek <ttomecek@redhat.com> - 0.2.0-1
- New upstream release 0.2.0

* Thu Mar 14 2019 Frantisek Lachman <flachman@redhat.com> - 0.1.0-1
- New upstream release 0.1.0

* Mon Mar 04 2019 Frantisek Lachman <flachman@redhat.com> - 0.0.1-1
- Initial package.
