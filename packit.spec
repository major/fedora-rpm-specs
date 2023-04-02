%global pypi_name packitos
%global real_name packit

Name:           %{real_name}
Version:        0.72.0
Release:        1%{?dist}
Summary:        A tool for integrating upstream projects with Fedora operating system

License:        MIT
URL:            https://github.com/packit/packit
Source0:        %pypi_source
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-click-man
BuildRequires:  python3-GitPython
BuildRequires:  python3-gnupg
BuildRequires:  python3-ogr
BuildRequires:  python3-packaging
BuildRequires:  python3-pyyaml
BuildRequires:  python3-specfile
BuildRequires:  python3-tabulate
BuildRequires:  python3-cccolutils
BuildRequires:  python3-copr
BuildRequires:  python3-koji
BuildRequires:  python3-rpkg
BuildRequires:  python3-lazy-object-proxy
BuildRequires:  python3-marshmallow
BuildRequires:  python3-marshmallow-enum
BuildRequires:  python3-requests
BuildRequires:  python3-requests-kerberos
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(setuptools-scm-git-archive)
BuildRequires:  python3-bodhi-client >= 7.0.0
BuildRequires:  python3-cachetools
BuildRequires:  python3-fedora
%if 0%{?rhel}
# epel-8 requires typing-extensions due to old python version
BuildRequires:  python3-typing-extensions
%endif
Requires:       python3-%{real_name} = %{version}-%{release}

%description
This project provides tooling and automation to integrate upstream open source
projects into Fedora operating system.

%package -n     python3-%{real_name}
Summary:        %{summary}
# new-sources
Requires:       fedpkg
Requires:       git
# kinit
Requires:       krb5-workstation
# rpmbuild
Requires:       rpm-build
# bumpspec
Requires:       rpmdevtools
# Copying files between repositories
Requires:       rsync
%if 0%{?rhel}
# rhbz#1968618 still not fixed for epel-8
Requires:       python3-koji
%endif
%{?python_provide:%python_provide python3-%{real_name}}

%description -n python3-%{real_name}
Python library for Packit,
check out packit package for the executable.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%if 0%{?rhel}
# rhbz#1968618 still not fixed for epel-8
sed -i -e 's|koji|# koji|' setup.cfg
%endif

%build
%py3_build

%install
%py3_install
python3 setup.py --command-packages=click_man.commands man_pages --target %{buildroot}%{_mandir}/man1

install -d -m 755 %{buildroot}%{_datadir}/bash-completion/completions
cp files/bash-completion/packit %{buildroot}%{_datadir}/bash-completion/completions/packit

%files
%license LICENSE
%{_bindir}/packit
%{_mandir}/man1/packit*.1*
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{real_name}
%{_bindir}/_packitpatch

%files -n python3-%{real_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/*

%changelog
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
