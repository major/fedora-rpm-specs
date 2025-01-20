%global _description \
rdopkg is a tool for automating RPM packaging tasks such as managing patches,\
updating to a new version and much more.\
\
Although it contains several RDO-specific actions, most of rdopkg\
functionality can be used for any RPM package following conventions\
described in the rdopkg manual.


Name:             rdopkg
Version:          1.7.0
Release:          7%{?dist}
Summary:          RPM packaging automation tool CLI

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:          Apache-2.0
URL:              https://github.com/softwarefactory-project/rdopkg
Source0:          %pypi_source

BuildArch:        noarch

BuildRequires:    git-core
# for documentation
BuildRequires:    asciidoc
BuildRequires:    make

Requires:         python3-rdopkg == %{version}-%{release}

%description %{_description}
This package contains rdopkg executable, man pages and docs.


%package -n python3-rdopkg
Summary:          RPM packaging automation tool

BuildRequires:    python3-devel
BuildRequires:    pyproject-rpm-macros
BuildRequires:    python3-pbr
BuildRequires:    python3-PyYAML

Requires:         python3-koji
Requires:         git-core
Requires:         git-review
Recommends:       python3-blessings
Recommends:       rpmlint

%description -n python3-rdopkg %{_description}

%prep
%autosetup -n %{name}-%{version} -S git

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files rdopkg

# Fedora 30 seriously dropped /usr/bin/python :D
sed -i -e 's/python /python3 /' Makefile doc/Makefile
make doc

# man pages
install -d -m 755 %{buildroot}%{_mandir}/man{1,7}
install -p -m 644 doc/man/*.1 %{buildroot}%{_mandir}/man1/
install -p -m 644 doc/man/*.7 %{buildroot}%{_mandir}/man7/


%files -n rdopkg
%doc README.md
%doc doc/*.adoc doc/html
%{_bindir}/rdopkg
%{_mandir}/man1/rdopkg*
%{_mandir}/man7/rdopkg*

%files -n python3-rdopkg -f %{pyproject_files}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.7.0-6
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1.7.0-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Oct 04 2023 Joel Capitao <jcapitao@redhat.com> - 1.7.0-1
- Update to 1.7.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 1.5.1-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 24 2022 Joel Capitao <jcapitao@redhat.com> - 1.5.1-1
- Update to 1.5.1

* Tue Oct 18 2022 Joel Capitao <jcapitao@redhat.com> - 1.5.0-1
- Update to 1.5.0

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 04 2022 Joel Capitao <jcapitao@redhat.com> - 1.4.0-6
- Use pyproject macros

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.4.0-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.4.0-2
- Rebuilt for Python 3.10

* Wed Mar 03 2021 Javier Peña <jpena@redhat.com> - 1.4.0-1
- Update to 1.4.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 12 2020 Joel Capitao <jcapitao@redhat.com> - 1.3.0-2
- Use git-core as BR instead of git

* Fri Aug 21 2020 Javier Peña <jpena@redhat.com> - 1.3.0-1
- Update to 1.3.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 14 2019 Javier Peña <jpena@redhat.com> - 1.1.1-1
- Update to 1.1.1

* Tue Oct 01 2019 Javier Peña <jpena@redhat.com> - 1.1.0-1
- Update to 1.1.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-2
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Jakub Ružička <jruzicka@redhat.com> 1.0.0-1
- Update to 1.0.0

* Wed Jun 26 2019 Jakub Ružička <jruzicka@redhat.com> 0.52.0-1
- Update to 0.52.0

* Mon Apr 08 2019 Jakub Ružička <jruzicka@redhat.com> 0.51.1-1
- Update to 0.51.1
- Change requirement: bunch -> munch

* Mon Apr 08 2019 Jakub Ružička <jruzicka@redhat.com> 0.50.0-1
- Update to 0.50.0

* Fri Mar 01 2019 Jakub Ružička <jruzicka@redhat.com> 0.49.0-3
- Fix /usr/bin/rdopkg being included in python3 subpackage

* Fri Mar 01 2019 Jakub Ružička <jruzicka@redhat.com> 0.49.0-2
- Recommend rpmlint

* Thu Feb 28 2019 Jakub Ružička <jruzicka@redhat.com> 0.49.0-1
- Update to 0.49.0
- Remove python2-rdopkg subpackage
- Clean up
- Require python-distroinfo >= 0.3.0

* Tue Feb 05 2019 Jakub Ružička <jruzicka@redhat.com> 0.48.0-1
- Update to 0.48.0
- Require python-distroinfo >= 0.2.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.47.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 05 2018 Jakub Ružička <jruzicka@redhat.com> 0.47.3-1
- Update to 0.47.3 bugfix release

* Tue Aug 21 2018 Jakub Ružička <jruzicka@redhat.com> 0.47.2-1
- info: fix `rdopkg info -l LOCAL` and add tests

* Tue Aug 21 2018 Jakub Ružička <jruzicka@redhat.com> 0.47.1-1
- Update to 0.47.1

* Wed Aug 15 2018 Jakub Ružička <jruzicka@redhat.com> 0.47.0-2
- add Requires: python for doc/gherkin-parser.py

* Wed Aug 15 2018 Jakub Ružička <jruzicka@redhat.com> 0.47.0-1
- core: use distroinfo module to access rdoinfo
- core: improve Python 3 compatibility
- distgit: fix version to tag translations for vX.Y.Z tag style
- distgit: allow '|' in patches_ignore regex
- distgit: prevent unneeded patch file changes
- doc: try using reno module to maintain release notes
- doctor: reworked with rainbows

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.46.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.46.3-3
- Rebuilt for Python 3.7

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.46.3-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 15 2018 Jakub Ružička <jruzicka@redhat.com> 0.46.3-1
- deps: Remove requirement on pyOpenSSL (previously a workaround)
- distgit: Add -R/--release-bump-index argument
- distgit: Support DLRN 0.date.hash and 0.1.date.hash Release formats
- distgit: Preserve Change-Id when amending a commit
- distgit: normalize commit messages
- new-version: ensure -H and -B work together
- new-version: don't display redundant message on -b
- new-version: enable `fedpkg new-sources` for Fedora by default
- new-version: fix `fedpkg new-sources` getting wrong tarball
- patch: return 0 on no new patches
- pkgenv: show patches base and base git ref information
- rdoinfo: Fix error on info-tags-diff for packages without buildsys-tags
- rdoinfo: Use "project" as package primary key to compare tags
- reqcheck: normalize python2/python3 package names
- spec: better detection of multiple changelog entries
- spec: don't get confused by changelog mentions in the changelog
- spec: don't duplicate %%{?dist}
- core: action alias support
- core: fix new action check for old state
- refactor: Remove legacy coprbuild action
- refactor: nice error messages on invalid Version/patches_base
- refactor: split utils.cmd, create separate utils.git module
- refactor: unify patch and update-patches
- tests: Add Zuul v3 jobs
- tests: Add newversion.feature scenario using --bug
- tests: Add topy to tox as a linting check
- tests: Extend newversion.feature for coverage of -H
- tests: add topy to whitelist_externals
- tests: expand fix.feature scenarios
- tests: improved reporting and test names
- tests: make spec file Then assert more descriptive
- doc: Trailing whitespace cleanup in doc files
- doc: Typo fixes from topy
- doc: include feature scenarios in the documentation
- doc: make file naming consistent
- doc: remove obsolete building doc
- doc: update README.md with Fedora/EPEL install instructions
- doc: update README.md with current information
- doc: update bug tracker information in the manual

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.45.0-5
- Escape macros in %%changelog

* Wed Sep 06 2017 Jakub Ružička <jruzicka@redhat.com> 0.45.0-4
- First Fedora release

* Mon Sep 04 2017 Jakub Ružička <jruzicka@redhat.com> 0.45.0-3
- Split CLI into separate package for easy py2 -> py3 transition
- Reccomend blessings instead of Require on supported platforms

* Wed Aug 30 2017 Jakub Ružička <jruzicka@redhat.com> 0.45.0-2
- Correct Source URL

* Wed Aug 30 2017 Jakub Ružička <jruzicka@redhat.com> 0.45.0-1
- fix: Fix rdo_projects.py example to work with latest rdoinfo
- fix: Remove obsolete run_tests.sh
- fix: Use absolute path for base_path when not using local_repo_path
- fix: cbsbuild: fix compatibility with Koji 1.13
- fix: core: only load state file on --continue
- fix: patch: format-patches with a standard abbrev setting
- fix: restore proper --continue functionality
- fix: show nice message on no distgit changes and unbreak gate
- spec: add Python 3 package
- spec: add docstrings to some methods
- spec: improve unicode support
- spec: properly expand macros defined in .spec file
- tests: Add a rdopkg fix scenario - no changelog update
- tests: Additional test for --abort clears rdopkg state file
- tests: add rdopkg fix revert everything scenario
- tests: enable python 3 testing
- tests: fix whitespace to make pycodestyle happy
- tests: speed up findpkg integration test
- tests: use tox to setup and run tests
- doc: Update MANIFEST.in
- doc: update HACKING.md for new test setup

* Thu Aug 24 2017 Jakub Ruzicka <jruzicka@redhat.com> 0.44.2-2
- Add Python 3 support with python3-rdopkg

* Wed Jul 26 2017 Jakub Ruzicka <jruzicka@redhat.com> 0.44.2-1
- Use absolute path for repo_path

* Tue Jul 25 2017 Jakub Ruzicka <jruzicka@redhat.com> 0.44.1-1
- setup.py: removed versioned requires breaking epel7
- Add pbr to requirements.txt

* Wed Jul 19 2017 Jakub Ruzicka <jruzicka@redhat.com> 0.44.0-1
- Update to 0.44.0
- Add BDD feature tests using python-behave
- Add options to specify user and mail in changelog entry
- Add support for buildsys-tags in info-tags-diff
- Adopt pbr for version and setup.py management
- Avoid prompt on non interactive console
- Avoid test failure due to git hooks
- Fix linting
- Fix output of info-tags-diff for new packages
- Improve changelog handling
- Improve patches_ignore detection
- Migrate to softwarefactory-project.io
- Python 3 compatibility fixes
- allow patches remote and branch to be set in git config
- core: refactor unreasonable default atomic=False
- distgit: Use NVR for commit title for multiple changelog lines
- distgit: new -H/--commit-header-file option
- document new-version's --bug argument
- guess: return RH osdist for eng- dist-git branches
- make git.config_get behave more like dict.get
- new-version: handle RHCEPH and RHSCON products
- patch: new -B/--no-bump option to only sync patches
- pkgenv: display color coded hashes for branches
- refactor: merge legacy rdopkg.utils.exception
- specfile: fix improper naming: get_nvr, get_vr
- tests: enable nice py.test diffs for common test code

* Thu Mar 30 2017 Jakub Ruzicka <jruzicka@redhat.com> 0.43-1
- Update to 0.43
- new-version: allow fully unattended runs
- new-version: re-enable reqdiff
- new-version: don't write patches_base for prefixed tags
- patch: improve new/old patches detection
- patch: new --changelog option
- patch: only create one commit
- update-patches: deprecate in favor of `rdopkg patch`
- pkgenv: don't query rdoinfo for obsolete information
- shell: allow passing action description
- specfile: raise when missing rpm lib in expand_macro()
- tests: increase unit test coverage
- tests: add findpkg integration tests to run_tests.sh
- tests: skip rpm test when rpm module isn't available
- tests: remove old test assets
- tests: run_tests.sh: actually fail on test failure
- cbsbuild: fix cbsbuild command failure
- dist: add pytest to test-requirements.txt
- distgit: better handling for patches_base and ignore
- distgit: correctly use -f/--force option
- doc: add virtualenv howto to HACKING and README
- doc: add documentation on how patches_base is calculated
- doc: improve docs for new-sources
- man: give example for patches_ignore
- guess: handle "VX.Y.Z" Git tags
- pep8 cleanup

* Tue Nov 22 2016 Jakub Ruzicka <jruzicka@redhat.com> 0.42-1
- Update to 0.42
- Counter past %%{?milestone} bug
- findpkg: new command to easily find single package
- specfile: extend BuildArch sanity check to %%autosetup
- specfile: add a sanity check for double # patches_base
- tag-patches: ignore RPM Epoch
- get-source: unbreak after defaults change
- reqcheck: add --spec/-s output for pasting
- pkgenv: show patches apply method

* Tue Nov 08 2016 Jakub Ruzicka <jruzicka@redhat.com> 0.41.4-1
- Update to 0.41.4
- Fixed -c argument parsing
- Evade pyton 2.7.5 regex bug on CentOS 7.2

* Fri Oct 21 2016 Jakub Ruzicka <jruzicka@redhat.com> 0.41.3-1
- Update to 0.41.3
- info: reintroduce lost info and info-diff-tags actions
- tag-patches: fix recommended "push" action
- Make --version work again

* Thu Oct 20 2016 Jakub Ruzicka <jruzicka@redhat.com> 0.41.2-1
- Update to 0.41.2
- Bugfix release that attempts to fix setup.py yet again

* Thu Oct 20 2016 Jakub Ruzicka <jruzicka@redhat.com> 0.41.1-1
- Update to 0.41.1
- Bugfix release that adds rdopkg.actions to setup.py

* Wed Oct 19 2016 Jakub Ruzicka <jruzicka@redhat.com> 0.41-1
- Update to 0.41
- patch: fix milestone handling and cover with unit tests
- Fix macro expansion when redefining macros
- Nuke python-parsley requirement
- actions: add "tag-patches" command
- refactor: split actions.py into action modules
- doc: rename asciidoc files from ".txt" to ".adoc"
- doc: update HACKING.md

* Thu Sep 15 2016 Jakub Ruzicka <jruzicka@redhat.com> 0.40-1
- Update to 0.40
- info-tags-diff: new utility action to show rdoinfo tag changes
- patch: fix traceback with no new patches
- pkgenv: fix traceback on unknown gerrit chain
- Fix new-version release tag management
- cbsbuild: make rpm module optional

* Wed Aug 24 2016 Jakub Ruzicka <jruzicka@redhat.com> 0.39-1
- Update to 0.39
- new-version: support X.Y.Z.0MILESTONE releases
- pkgenv: show NVR detected from .spec
- cbsbuild: make koji module optional

* Wed Jul 20 2016 Jakub Ruzicka <jruzicka@redhat.com> 0.38-1
- Update to 0.38

* Thu Jun 02 2016 Haikel Guemar <hguemar@fedoraproject.org> 0.37-2
- Drop deprecated rdoupdate code

* Mon May 23 2016 Jakub Ruzicka <jruzicka@redhat.com> 0.37-1
- Release 0.37
- patchlog: print rhbz numbers
- patch: add rhbz numbers from commits
- patch: Improve parsing of .spec Source attribute
- actions: Do not reset branch if local_patches is set
- Reintroduce new-sources autodetection for RHOSP
- check_new_patches: Do not count commits using the patches_ignore keyword
- README: update links and more
- HACKING.md: correct tests command

* Wed Apr 20 2016 Jakub Ruzicka <jruzicka@redhat.com> 0.36-1
- Release 0.36
- Support new review based workflow with rpmfactory
- patch, new-version: support review workflow
- review-patch, review-spec: new actions

* Fri Mar 04 2016 Jakub Ruzicka <jruzicka@redhat.com> 0.35.1-1
- Update to 0.35.1
- repoman: fix regression on local rdoinfo repo

* Fri Mar 04 2016 Jakub Ruzicka <jruzicka@redhat.com> 0.35-1
- Update to 0.35
- experimental support for patches in gerrit reviews

* Tue Jan 26 2016 Jakub Ruzicka <jruzicka@redhat.com> 0.34-1
- Update to 0.34
- info: support rdoinfo tags/overrides

* Mon Jan 11 2016 Jakub Ruzicka <jruzicka@redhat.com> 0.33-1
- Update to 0.33
- update-patches: support #patches_ignore regex filter

* Fri Oct 16 2015 Jakub Ruzicka <jruzicka@redhat.com> 0.32.1-1
- Update to 0.32.1
- new-version: fix patches branch detection

* Wed Oct 14 2015 Jakub Ruzicka <jruzicka@redhat.com> 0.32-1
- Update to 0.32
- clone: new action to setup RDO package git remotes
- update-patches: smarter .spec patch management

* Fri Oct 02 2015 Jakub Ruzicka <jruzicka@redhat.com> 0.31-1
- Update to 0.31
- new-version: auto --bump-only on missing patches branch
- new-version: only run `fedpkg new-sources` with non-empty sources file
- update-patches: update the "%%commit" macro
- patchlog: new action to show patches branch log
- remove unused 'rebase' action

* Tue Aug 11 2015 Jakub Ruzicka <jruzicka@redhat.com> 0.30-1
- Update to 0.30
- spec: require standalone pymod2pkg >= 0.2.1
- log: improve stdout vs stderr logging
- helpers.edit: Clear message about unset $EDITOR
- update-patches: ignore git submodule changes

* Tue Aug 04 2015 Jakub Ruzicka <jruzicka@redhat.com> 0.29.1-1
- Update to 0.29.1
- Handle version_tag_style in check_new_patches()

* Thu Jul 23 2015 Jakub Ruzicka <jruzicka@redhat.com> 0.29-2
- Update package description

* Thu Jul 23 2015 Jakub Ruzicka <jruzicka@redhat.com> 0.29-1
- Update to 0.29
- new-version: support vX.Y.Z version tags
- core: improve state file handling

* Fri Jun 26 2015 Jakub Ruzicka <jruzicka@redhat.com> 0.28.1-1
- Update to 0.28.1
- doc: such documentation, much clarity, wow

* Wed Jun 03 2015 Jakub Ruzicka <jruzicka@redhat.com> 0.28-1
- Update to 0.28
- reqquery: manage dem requirements like a boss

* Mon May 04 2015 Jakub Ruzicka <jruzicka@redhat.com> 0.27.1-1
- Update to 0.27.1
- update-patches: create commit even with only removed patches

* Mon Apr 27 2015 Jakub Ruzicka <jruzicka@redhat.com> 0.27-1
- Update to 0.27
- reqcheck: new action to check for correct Requires

* Mon Mar 30 2015 Jakub Ruzicka <jruzicka@redhat.com> 0.26-1
- Update to 0.26
- query: new action to query RDO package versions
- update: use SSH for update repo
- reqdiff: fix stupid regexp
- new-version: ignore missing requirements.txt diff

* Wed Feb 18 2015 Jakub Ruzicka <jruzicka@redhat.com> 0.25-1
- Update to 0.25
- update: parsable update summary in gerrit topic
- Provide set_colors function to control color output

* Wed Feb 04 2015 Jakub Ruzicka <jruzicka@redhat.com> 0.24-1
- Update to upstream 0.24
- update-patches: support %%autosetup patch apply method
- Require rdoupdate with cbs support

* Thu Jan 22 2015 Jakub Ruzicka <jruzicka@redhat.com> 0.23.1-1
- Update to 0.23.1
- Packaging fixes

* Tue Jan 20 2015 Jakub Ruzicka <jruzicka@redhat.com> 0.23-1
- Update to 0.23
- kojibuild: offer push when needed
- reqdiff: new action & integrated into new-version
- core: fix state file handling and atomic actions

* Tue Dec 09 2014 Jakub Ruzicka <jruzicka@redhat.com> 0.22-1
- Open source rdopkg
