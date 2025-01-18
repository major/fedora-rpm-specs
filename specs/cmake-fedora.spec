Name:           cmake-fedora
Version:        2.9.3
Release:        22%{?dist}
Summary:        CMake helper modules for fedora developers
License:        BSD-2-Clause-FreeBSD
URL:            https://pagure.io/%{name}/
Source0:        https://releases.pagure.org/%{name}/%{name}-%{version}-Source.tar.gz

BuildRequires:  cmake >= 2.6.2
BuildRequires:  koji
Requires:       cmake >= 2.6.2
Requires:       git
Requires:       bodhi-client
Requires:       koji
Requires:       rpm-build
Requires:       fedpkg
Requires:       fedora-packager
Requires:       curl

BuildArch:      noarch

%description
cmake-fedora consist a set of cmake modules that provides
helper macros and targets for fedora developers.



%prep
%setup -q -n %{name}-%{version}-Source

%build
# $RPM_OPT_FLAGS should be loaded from cmake macro.
%cmake -DCMAKE_FEDORA_ENABLE_FEDORA_BUILD=1 .
%cmake_build

%install
%cmake_install

# We install document using doc
rm -fr %{buildroot}%{_docdir}/*

%check
ctest --output-on-failure


%files
%doc AUTHORS README.md ChangeLog COPYING
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}-fedpkg
%{_bindir}/%{name}-koji
%{_bindir}/%{name}-newprj
%{_bindir}/%{name}-pkgdb
%{_bindir}/%{name}-reset
%{_bindir}/%{name}-zanata
%{_bindir}/koji-build-scratch
%{_datadir}/cmake/Modules/CmakeFedoraScript.cmake
%{_datadir}/cmake/Modules/DateTimeFormat.cmake
%{_datadir}/cmake/Modules/ManageAPIDoc.cmake
%{_datadir}/cmake/Modules/ManageArchive.cmake
%{_datadir}/cmake/Modules/ManageChangeLogScript.cmake
%{_datadir}/cmake/Modules/ManageDependency.cmake
%{_datadir}/cmake/Modules/ManageEnvironment.cmake
%{_datadir}/cmake/Modules/ManageEnvironmentCommon.cmake
%{_datadir}/cmake/Modules/ManageFile.cmake
%{_datadir}/cmake/Modules/ManageGConf.cmake
%{_datadir}/cmake/Modules/ManageGettextScript.cmake
%{_datadir}/cmake/Modules/ManageGitScript.cmake
%{_datadir}/cmake/Modules/ManageMessage.cmake
%{_datadir}/cmake/Modules/ManageRPM.cmake
%{_datadir}/cmake/Modules/ManageRPMScript.cmake
%{_datadir}/cmake/Modules/ManageRelease.cmake
%{_datadir}/cmake/Modules/ManageReleaseFedora.cmake
%{_datadir}/cmake/Modules/ManageSourceVersionControl.cmake
%{_datadir}/cmake/Modules/ManageString.cmake
%{_datadir}/cmake/Modules/ManageTarget.cmake
%{_datadir}/cmake/Modules/ManageTranslation.cmake
%{_datadir}/cmake/Modules/ManageUninstall.cmake
%{_datadir}/cmake/Modules/ManageUpload.cmake
%{_datadir}/cmake/Modules/ManageVariable.cmake
%{_datadir}/cmake/Modules/ManageVersion.cmake
%{_datadir}/cmake/Modules/ManageZanata.cmake
%{_datadir}/cmake/Modules/ManageZanataDefinition.cmake
%{_datadir}/cmake/Modules/ManageZanataScript.cmake
%{_datadir}/cmake/Modules/ManageZanataSuggest.cmake
%{_datadir}/cmake/Modules/cmake_uninstall.cmake.in
%{_datadir}/cmake/Templates/fedora/CMakeLists.txt.template
%{_datadir}/cmake/Templates/fedora/RELEASE-NOTES.txt.template
%{_datadir}/cmake/Templates/fedora/bsd-3-clauses.txt
%{_datadir}/cmake/Templates/fedora/gpl-2.0.txt
%{_datadir}/cmake/Templates/fedora/gpl-3.0.txt
%{_datadir}/cmake/Templates/fedora/lgpl-2.1.txt
%{_datadir}/cmake/Templates/fedora/lgpl-3.0.txt
%{_datadir}/cmake/Templates/fedora/project.spec.in

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 16 2022 Takao Fujiwara <fujiwara@redhat.com> - 2.9.3-16
- Migrate license tag to SPDX

* Wed Aug 03 2022 Takao Fujiwara <fujiwara@redhat.com> - 2.9.3-15
- Resolves: #2113152 FTBFS with koji hardware failure

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 07 2020 Takao Fujiwara <fujiwara@redhat.com> - 2.9.3-10
- Resolves: #1863341 FTBFS replace make with cmake_build

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Takao Fujiwara <fujiwara@redhat.com> - 2.9.3-7
- Resolves: #1832434 - FTI: Delete Requires packagedb-cli

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 01 2017 Ding-Yi Chen <dchen at redhat.com> - 2.9.3-1
- Fixed cmake-fedora-fedpkg failed to push to bodhi.
- Target tag_pre now depends on target module-only.

* Fri Jul 28 2017 Ding-Yi Chen <dchen at redhat.com> - 2.9.2-1
Fixed RHBZ#1476070 - cmake-fedora-fedpkg failed to handle multiple builds

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Ding-Yi Chen <dchen at redhat.com> - 2.8.0-1
Migrate changes like fedorahosted to pagure.
And move from pkgdb to product definition center (PDC).
- Enhancement:
  + cmake-fedora-pkgdb new sub-commands:
    - git-branch package: List the git-branches of package
    - newest-nvr: Return NVR of master branch
    - newest-changelog: Return the latest ChangeLog in master branch.
- Changes:
  + koji-build-scratch is now back to use koji build --scratch
  + MANAGE_UPLOAD_FEDORAHOSTED is marked as depreciated
    But MANAGE_UPLOAD_PAGURE is not implemented yet, as pagure does not
    support scp upload yet
- Bugs:
  + Fixed RHBZ#1424757 - cmake-fedora: failed to handle f26-pending
  + Fixed RHBZ#1425263 - cmake-fedora: migrate from fedorahosted to pagure
  + Fixed fedpkg --dist depreciate warning

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Aug 19 2016 Ding-Yi Chen <dchen at redhat.com> - 2.7.1-1
- Bugs:
  + cmake-fedora-fedpkg: fix when git change is at staging, but not committed yet.

* Wed Aug 17 2016 Ding-Yi Chen <dchen at redhat.com> - 2.7.0-1
- Enhancement:
  + cmake-fedora-reset: The program that clean and reset the build environment
- Bugs:
  + Fixed Bug 1367656 - cmake-fedora-fedpkg: failed when commit is clean

* Thu Feb 25 2016 Ding-Yi Chen <dchen at redhat.com> - 2.6.0-1
- Enhancement:
  * ManageTranslation: MANAGE_POT_FILE: new options DOMAIN_NAME, MO_LOCALE_DIR
- Bug fix:
  * cmake-fedora-zanata: remove debug message
  * ManageTranslate: failed to generate pot targets when 
    MANAGE_TRANSLATION_GETTEXT_POT_FILES is not empty.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 29 2016 Ding-Yi Chen <dchen at redhat.com> - 2.5.1-1
- Fixed:
  * Out-of-the-source build for ibus-chewing

* Wed Jan 06 2016 Ding-Yi Chen <dchen at redhat.com> - 2.5.0-1
- Enhancement:
  * New Target: changelog_no_force: Does not update ChangeLog if RELEASE-NOTES.txt is newer than ChangeLog.
- Fixed:
  * MANAGE_ZANATA: Error message that missing right bracket.
    Thanks ChangZhu Chen for pointing it out.
  * Bug 1295278 - cmake-fedora: failed to update version when CMakeCache.txt is newer than RELEASE-NOTES.txt

* Wed Nov 18 2015 Ding-Yi Chen <dchen at redhat.com> - 2.4.4-1
- Fixed:
  * Bug 1283082 - CmakeFedoraScript.cmake is not found
  * Zanata target generation
  * Missing cmake-fedora-pkgdb

* Mon Nov 02 2015 Ding-Yi Chen <dchen at redhat.com> - 2.4.3-1
- Enhancement:
  * cmake-fedora-pkgdb: New script: pkgdb helper script.
  * cmake-fedora-zanata: New script: zanata helper script.
- Fixed:
  * Resolves: RHBZ 1194797: find -printf is not portable
- Changed:
  * Support zanata-server and zanata-client 3.7.
  * Add additional path to cmake-fedora.conf
  * cmake-fedora.conf: Remove bodhi branch, 
    use whatever cmake-fedora-pkgdb found. 
  * ManageFile: New function: MANAGE_FILE_COMMON_DIR
  * ManageString: Macro to function: STRING_UNQUOTE
  * koji-build-scratch: Use fedpkg backend instead
  * cmake-fedora-fedpkg: Fix

* Fri Oct 30 2015 Ding-Yi Chen <dchen at redhat.com> - 2.3.4-3
- Restore the RPM-ChangeLog

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Dec 10 2014 Ding-Yi Chen <dchen at redhat.com> - 2.3.4-1
- Fixed RHBZ 1144906 - cmake-fedora failed to build target pot_files if the .pot file not exists.
- ManageDependency: Now able to assign multiple PKG_CONFIG files.
- ManageGConf: Added "Variables to cache".
- cmake-fedora.conf: el7 and fc21 is now available in bodhi.
- ManageRPMScript: Fixed the mo file handling.
- ManageZanata: Use /usr/share/locale as SYSTEM_LOCALE source instead.

* Mon Sep 22 2014 Ding-Yi Chen <dchen at redhat.com> - 2.3.1-1
- Fixed RHBZ 1144906 - cmake-fedora failed to build target pot_files if the .pot file not exists.
- ManageDependency: var_CFLAGS and var_LIBS are also cached.
- ManageDependency: var_INCLUDEDIR also includes directories from var_CFLAGS.
- ManageGConf: Added "Variables to cache".
- cmake-fedora.conf: el7 and fc21 is now available in bodhi.

* Tue Aug 26 2014 Ding-Yi Chen <dchen at redhat.com> - 2.3.0-1
- cmake-fedora-fedpkg: fix try_command
- ManageChangeLogScript: New command "make"

* Mon Aug 25 2014 Ding-Yi Chen <dchen at redhat.com> - 2.2.1-1
- ManageEnvironmentCommon: Module of variable for both normal and script mode.
- ManageDependency: Make changes suitable for more generic *nix build.
    e.g. FEDORA_NAME -> PACKAGE_NAME
- ManageZanata: MANAGE_ZANATA: New option CLEAN_ZANATA_XML.
- Workaround for Bug 1115136, otherwise el7 won't work.

* Fri Aug 15 2014 Ding-Yi Chen <dchen at redhat.com> - 2.1.3-1
- Fixed cmake-fedora-fedpkg

* Thu Aug 14 2014 Ding-Yi Chen <dchen at redhat.com> - 2.1.0-3
- Fix long changelog

* Mon Aug 11 2014 Ding-Yi Chen <dchen at redhat.com> - 2.1.0-2
- Fixed rpmlint warning: macro-in-changelog

* Mon Aug 11 2014 Ding-Yi Chen <dchen at redhat.com> - 2.1.0-1
- Fixed Bug 1093336 - date(1): -u is much portable than --utc
- Fix EPEL 7 support.
- See ChangeLog for detailed ChangeLog

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 28 2014 Ding-Yi Chen <dchen at redhat.com> - 1.3.0-1
- Fixed Bug 1002279 - Project configuration bugs when using cmake-fedora-newprj
- Enhanced:
  + Support EPEL7
  + New targets: pack_src_no_force.
- Fixed:
  + cmake-fedora-newprj is fixed.

* Sat Feb 01 2014 Ding-Yi Chen <dchen at redhat.com> - 1.2.7-1
- Changed:
  + cmake-fedora.conf.in will also be searched if cmake-fedora.conf does not exist.
  + Target test is built before pack_src.

* Thu Jan 30 2014 Ding-Yi Chen <dchen at redhat.com> - 1.2.6-1
- Resolves Bug 1058631 - ManagePRM generate Broken defattr
- Enhancement:
  + ManageTarget: ADD_CUSTOM_TARGET_COMMAND: NO_FORCE: new option.
  + Projects that includes cmake-fedora as submodule are no longer requires cmake-fedora.conf
- Changed:
  + ManageTranslation: Fix po build
  + ManageRPM: Fix defattr
  + ManageReleaseFedora: helper scripts in CMAKE_SOURCE_DIR/cmake-fedora 
    can also be located

* Thu Jan 09 2014 Ding-Yi Chen <dchen at redhat.com> - 1.2.3-1
- Resolves Bug 1040333 - RFE: Suiport .gitignore file as 
  source of CPACK_SOURCE_IGNORE_FILES
- Resolves Bug 1046213 - RFE: RPM ChangeLog should be generated by 
  newest build from koji 
- Enhancement:
  + ChangeLog.prev is no longer required.
  + RPM-ChangeLog.prev is provide by koji now.
  + cmake-fedora-koji: 
    - new subcommand: newest-build and newest-changelog.
  + cmake-fedora-changelog: new script. 
  + New targets:
    - tag_push: Push to git.
  + ManageFile:
    - Add absolute file support
    - MANAGE_FILE_INSTALL: Add TARGETS support.
    - MANAGE_FILE_INSTALL: Add RENAME support.
    - GIT_GLOB_TO_CMAKE_REGEX: Convert git glob to cmake regex
  + ManageArchive:
    - PACK_SOURCE_CPACK: Pack with CPack
    - PACK_SOURCE_ARCHIVE: Now can specify OUTPUT_FILE.
    - SOURCE_ARCHIVE_CONTENTS_ADD: Add file to source archive.
    - SOURCE_ARCHIVE_CONTENTS_ADD_NO_CHECK: 
      Add file to source archive without checking.
    + ManageDependency: Manage dependencies.
  + ManageRPM: 
    - PACK_RPM: New options: SPEC_IN and SPEC.
    - RPM_SPEC_STRING_ADD: Add a string to SPEC string.
    - RPM_SPEC_STRING_ADD_DIRECTIVE: Add a directive to SPEC string.
    - RPM_SPEC_STRING_ADD_TAG: Add a string to SPEC string.
  + ManageString:
    - STRING_APPEND: Append a string to a variable.
    - STRING_PADDING: Padding the string to specified length
    - STRING_PREPEND: Prepend a string to a variable.
  + ManageTranslation:
    - MANAGE_GETTEXT: 
      + Can specify MSGFMT_OPTIONS and MSGMERGE_OPTIONS
      + Add gettext-devel to BUILD_REQUIRES.
  + ManageVariable:
    - VARIABLE_TO_ARGN: Merge the variable and options to 
      the form of ARGN.
  + Cached variables:
    - RPM_SPEC_CMAKE_FLAG: cmake flags in rpm build.
    - RPM_SPEC_MAKE_FLAG: make flags in rpm build.
    - Changed Modules:
  + ManageArchive:
    - PACK_SOURCE_ARCHIVE: Can now pass either 
      empty, outputDir, or source File. 
  + ManageGConf2: Fixed.
  + ManageString: STRING_SPLIT: New Option: ALLOW_EMPTY
  + ManageRPM
    - Add support of pre, post, and preun
  + ManageVariable:
    - VARIABLE_PARSE_ARGN can now handle multiple-appeared options.
- Changed:
  + CMake policy no longer enforced by default.
  + ManageString: STRING_SPLIT is changed from macro to function,
    so no need to put excessive backslashes.
- Removed:
  + Target after_release_commit and related are no longer required 
    and thus removed.

* Tue Nov 26 2013 Ding-Yi Chen <dchen at redhat.com> - 1.1.6-1
- Enhancement:
  + Fedora version will now automatically updated.
  + New macros:
    - VARIABLE_PARSE_ARGN: Parse the arguments.
  + New scripts: 
    cmake-fedora-koji: Koji utilities.
    cmake-fedora-fedpkg: Fedpkg utilities.
  + Changed scripts:
    koji-build-scratch: fedora_1, fedora_2, 
    epel_1, epel_2 can now be used as build scopes.
  + BODHI_UPDATE_TYPE is no longer required.
  + No need to manual edit project.spec.in
  + ADD_CUSTOM_TARGET_COMMAND now allow "ALL"
- Bug Fixes:
  Resolves: Bug 879141 - Excessive quotation mark for target tag_pre
  Resolves: Bug 992069 - cmake-fedora: FTBFS in rawhide
- Changed Modules
  + ManageUpload:
    - New macros:
      + MANAGE_UPLOAD_TARGET
    - Changed macros:
      + MANAGE_UPLOAD_SCP: parameter fileAlias replaced with targetName
      + MANAGE_UPLOAD_SFTP: parameter fileAlias replaced with targetName 
      + MANAGE_UPLOAD_FEDORAHOSTED: parameter fileAlias replaced with targetName
      + MANAGE_UPLOAD_SOURCEFORGE: parameter fileAlias replaced with targetName
    - Removed macros:
      + MANAGE_UPLOAD_MAKE_TARGET
      + MANAGE_UPLOAD_CMD
- Removed Directory: 
  + <PRJ_DOC_DIR>/examples: as the examples can be found in
    <CMAKE_ROOT>/Templates/fedora
- Removed Variables: 
  + FEDORA_AUTO_KARMA
- Removed Macros:
  + MANAGE_UPLOAD_MAKE_TARGET
  + MANAGE_UPLOAD_CMD
- Removed Targets:
  + bodhi_new: Submit the package to bodhi
  + fedpkg_<tag>_build: Build for tag
  + fedpkg_<tag>_commit: Import, commit and push

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 22 2012 Ding-Yi Chen <dchen at redhat.com> - 1.0.5-1
- Fedora 18 support.
- Source tarball filename is changed back to name-version-Source.tar.gz
  to avoid confusion between source generate by cmake-fedora
  (which contains ChangeLog and projectName.pot) and tarball generation service from hosting site
  (which does not contain generated files)
- koji-build-scratch: rawhide build target does not always have suffix -candidate.
- README updated.
- TODO updated.

* Fri Aug 17 2012 Ding-Yi Chen <dchen at redhat.com> - 1.0.4-1
- Source tarball filename is now name-version.tar.gz instead of name-version-Source.tar.gz
- after_release_commit depends rpm_changelog_prev_update if RPM supported enabled.
- Corrected the 'FORCE' of cmake CACHE
- Update the error messages when cmake-fedora is not installed.
- Fixed target: zanata_push_trans.
- Fixed zanata arguments.
- fedpkg clone is now triggered if the clone directory does not exist when doing the fedpkg_commit,
  it no longer the listed OUTPUT of an ADD_CUSTOM_COMMAND.
- Add target: translations as an universal easy target to generate/update translation files.

* Mon Jul 23 2012 Ding-Yi Chen <dchen at redhat.com> - 1.0.2-1
- Fixed after_release_commit

* Mon Jul 23 2012 Ding-Yi Chen <dchen at redhat.com> - 1.0.1-1
- Greatly simplified the modules design and usage.
- Release version are now defined in cmake-fedora.conf
  for easy maintenance.
- Fix the MANAGE_MESSAGE_LEVEL
- koji scratch builds are run only once before tagging.
- CVS support is removed.
- New command: koji-build-scratch for scratch build on all supported
  releases.
- New module: ManageTarget
- New function: SETTING_STRING_GET_VARIABLE
- New macro:
  + ADD_CUSTOM_TARGET_COMMAND
  + STRING_ESCAPE_SEMICOLON
- Macros changed behavior:
  MANAGE_ZANATA: Arguments are changed.
- Target changed: changelog_update are now separate as:
  + changelog_prev_update: Update ChangeLog.prev
  + rpm_changelog_prev_update: Update RPM-ChangeLog.prev
- Command renamed:
  + cmake-fedora-newprj.sh to cmake-fedora-newprj
- Module renamed:
  + ManageReleaseOnFedora to ManageReleaseFedora
  + ManageMaintainerTargets to ManageUpload
  + PackSource to ManageArchive
  + PackRPM to ManageRPM
  + UseGConf to ManageGConf
  + UseDoxygen to ManageAPIDoc
- Function renamed:
  + LOAD_RELEASE_FILE to RELEASE_NOTES_READ_FILE
- Macro renamed:
  + PACK_SOURCE to PACK_SOURCE_ARCHIVE
  + USE_MOCK to RPM_MOCK_BUILD
  + USE_DOXYGEN to MANAGE_APIDOC_DOXYGEN
  + USE_GETTEXT to MANAGE_GETTEXT
  + USE_ZANATA to MANAGE_ZANATA
- Variable renamed: PACK_SOURCE_IGNORE_FILES to SOURCE_ARCHIVE_IGNORE_FILES
- RELEASE_ON_FEDORA: support new tags: "fedora" for current fedora,
  and "epel" for current epel.
- ChangeLog generation rewritten, target version_check no longer need.
- Removed target: version_check
- Variable Removed:
  FEDORA_NEXT_RELEASE
  FEDORA_NEXT_RELEASE_TAGS
  FEDORA_LATEST_RELEASE
  FEDORA_PREVIOUS_RELEASE

* Tue Sep 20 2011 Ding-Yi Chen <dchen at redhat.com> - 0.8.1-1
- Fixed Bug 738958 - cmake-fedora: remove excessive quotation marks for Precompile definition
- Fixed Bug 733540 - cmake-fedora: "" should be read as empty string
- ManageEnvironment: Now defined cmake_policy won't get overridden.
- ManageString: STRING_UNQUOTE is now merely remove quote marks in the beginning and
    end of string. The string will not be changed otherwise.
- UseUninstall has renamed as ManageUninstall
- ManageMaintainerTargets: Reveal MAINTAINER_UPLOAD_COMMAND
- ManageTranslation: Adopt zanata python client 1.3, arguments are redesigned.
  + Change target: from "translations" to "gmo_files"
  + Add targets: zanata_push, zanata_push_trans, zanata_pull_trans
  + Add argument: ALL_FOR_PUSH, ALL_FOR_PUSH_TRANS and ALL_FOR_PULL
  + Add argument: OPTIONS for passing arguments.
- ManageReleaseOnFedora: Now default to build against candidate repos,
  unless _CANDIDATE_PREFERRED is set to "0".

* Thu Aug 18 2011 Ding-Yi Chen <dchen at redhat.com> - 0.7.994-1
- Fixed Bug 725615 - cmake-fedora: Use UTC for changelog
- Fixed Bug 725617 - cmake-fedora: target 'tag' should stop when tag file exists.
- Module CompileEnv.cmake is obsoleted by ManageEnvironment.cmake
  because it is what the variable actually store.
- Revised ManageTranslation, now zanata.xml.in can be put to either
  CMAKE_SOURCE_DIR or CMAKE_CURRENT_SOURCE_DIR.
- ManageReleaseOnFedora:
  + New Constants: FEDORA_NEXT_RELEASE_TAGS, FEDORA_SUPPORTED_RELEASE_TAGS.
  + Remove NORAWHIDE, as user can use TAGS to achieve the same.
  + Actually mkdir and clone project if the FedPkg directory is missing.
- ManageTranslation:
  + Fixed zanata.xml path problem
  + Fixed zanata related targets.
- New Variable: CMAKE_FEDORA_TMP_DIR for holding cmake-fedora files.
  + ChangeLog temporary files have moved to this directory.

* Fri Jul 08 2011 Ding-Yi Chen <dchen at redhat.com> - 0.7.1-1
- Target release now depends on upload.

* Fri Jul 08 2011 Ding-Yi Chen <dchen at redhat.com> - 0.7.0-1
- Fixed target: after_release_commit.
- Add "INCLUDE(ManageRelease)" in template
  so new project will not get CMake command "MANAGE_RELEASE"
- Corrected TODO.
- Corrected ChangeLog.prev and SPECS/RPM-ChangeLog.prev.
- By default, the CMAKE_INSTALL_PREFIX is set as '/usr'.

* Wed Jul 06 2011 Ding-Yi Chen <dchen at redhat.com> - 0.6.1-1
- Remove f13 from FEDORA_CURRENT_RELEASE_TAGS, as Fedora 13 is end of life.
- ManageMessage: New module.
  + M_MSG: Controllable verbose output
- ManageRelease: New module.
  + MANAGE_RELEASE: Make release by uploading files to hosting services
- Now ManageReleaseOnFedora includes ManageMaintainerTargets
- Modules are shown what they include and included by.
- Now tag depends on koji_scratch_build, while fedpkg_commit master
  (or other primary branch) depends directly on tag.
- MAINTAINER_SETTING_READ_FILE now can either use MAINTAINER_SETTING, or take
  one argument that define maintainer setting file.
- MANAGE_MAINTAINER_TARGETS_UPLOAD no longer require argument hostService,
  It now relies on HOSTING_SERVICES from maintainer setting file.
- Minimum cmake requirement is now raise to 2.6.
- Targets which perform after release now have the prefix "after_release".

* Wed Jul 06 2011 Ding-Yi Chen <dchen at redhat.com> - 0.6.1-1
- Remove f13 from FEDORA_CURRENT_RELEASE_TAGS, as Fedora 13 is end of life.
- ManageMessage: New module.
  + M_MSG: Controllable verbose output
- ManageRelease: New module.
  + MANAGE_RELEASE: Make release by uploading files to hosting services
- Now ManageReleaseOnFedora includes ManageMaintainerTargets
- Modules are shown what they include and included by.
- Now tag depends on koji_scratch_build, while fedpkg_commit master
  (or other primary branch) depends directly on tag.
- MAINTAINER_SETTING_READ_FILE now can either use MAINTAINER_SETTING, or take
  one argument that define maintainer setting file.
- MANAGE_MAINTAINER_TARGETS_UPLOAD no longer require argument hostService,
  It now relies on HOSTING_SERVICES from maintainer setting file.
- Minimum cmake requirement is now raise to 2.6

* Wed Jun 08 2011 Ding-Yi Chen <dchen at redhat.com> - 0.6.0-1
- Fixed Bug 684107 - [cmake-fedora] TAGS in USE_FEDPKG is ineffective.
- ManageTranslation:
  + Renamed from UseGettext
  + New Macro: USE_ZANATA() - Zanata support (experiential).
  + New Macro: USE_GETTEXT() - Gettext support.
    This macro merges GETTEXT_CREATE_POT and GETTEXT_CREATE_TRANSLATIONS,
    to simplified the usage and make the macro names more consistent.
- ManageReleaseOnFedora:
  + New Variable: FEDORA_EPEL_RELEASE_TAGS
- Clean up Modules: No unrelated files under Modules/
- Removed debug messages of:
  CMAKE_MAJOR_VERSION, CMAKE_MINOR_VERSION. CMAKE_PATCH_VERSION,
  _cmake_uninstall_in, _koji_tags, _tags.

* Sun Feb 27 2011 Ding-Yi Chen <dchen at redhat.com> - 0.5.0-1
- Macro: RELEASE_ON_FEDORA added.
- Target: release_on_fedora added.
- Now has more informative error message, when cmake-fedora is not installed.
- Fixed UseUninstall
- Fixed Bug 670079 - [cmake-fedora] target "release"
  will not stop when koji build failed
- Fixed Bug 671063 - [cmake-fedora] target "rpmlint"
  should not depend on "koji_scratch_build"
- Protocol for hosting server should now be specified as "[Hosting]_PROTOCOL".
- Refactoring ManageMaintainerTargets.
- fedpkg and koji build for every tags are revealed.
- Now set rawhide as f16, release dists are f15,f14,f13.
- rpm build process is now refined, no unnecessary build.
- Renamed target push_svc_tag to push_post_release.
- Renamed module UseFedpkg to ManageReleaseOnFedora

* Fri Jan 07 2011 Ding-Yi Chen <dchen at redhat.com> - 0.4.0-1
- New target: release
- New target: install_rpms
- ./Module should precedes /usr/share/cmake/Modules, so
  it always use latest modules.
- Fixed Reading a file that contains '\'.
- Added Macro PACK_RPM_GET_ARCH
- Added target install_rpms for bulk rpms installation.
- Target rpm now uses -bb instead of -ba.
- Target rpm now depends on srpm.
- Source version control logic is split out as ManageSourceVersionControl
- Module UseHostingService is renamed as ManageMaintainerTarget
- Macro USE_HOSTING_SERVICE_READ_SETTING_FILE is renamed as
  MAINTAINER_SETTING_READ_FILE

* Sun Dec 19 2010 Ding-Yi Chen <dchen at redhat.com> - 0.3.3-1
- Fixed: Support for out-of-source build.
- Fixed: Join the next line if ended with back slash '\'.
- ChangeLog: Now generate from "cmake ." directly.
- changelog: target removed. So it won't do unnecessary rebuild.

* Tue Nov 09 2010 Ding-Yi Chen <dchen at redhat.com> - 0.3.2-1
- Fixed: Macro invoked with incorrect arguments for macro named STRING_ESCAPE
  Caused by give and empty string from STRING_TRIM
- Removed: f12 from FEDORA_CURRENT_RELEASE_TAGS

* Mon Nov 08 2010 Ding-Yi Chen <dchen at redhat.com> - 0.3.1-1
- SETTING_FILE_GET_VARIABLES_PATTERN:
  Fixed: unable to use relative path problem.
  Fixed: UNQUOTE and NOESCAPE_SEMICOLON can now used together.

* Wed Nov 03 2010 Ding-Yi Chen <dchen at redhat.com> - 0.3.0-1
- New macro: SETTING_FILE_GET_VARIABLES_PATTERN
- New macro: PACK_SOURCE_FILES
- Fixed: Variable lost in SETTING_FILE_GET_ALL_VARIABLES and
  SETTING_FILE_GET_VARABLE.
- Fixed: Variable values won't apply in SETTING_FILE_GET_ALL_VARIABLES
- UseUninstall finds cmake_uninstall.in in additional paths:
  /usr/share/cmake/Modules and /usr/share/cmake/Modules
- Minor improvements in CMakeLists.txt and project.spec.in templates.

* Wed Oct 20 2010 Ding-Yi Chen <dchen at redhat.com> - 0.2.4-1
- cmake-fedora-newprj.sh: New option "-e" that extract value from specified
  spec or spec.in.
- Now usage is printed instead of junk output when project_name is not given.
- Source code (whatever is packed) and tarball dependency now checked.

* Sat Oct 16 2010 Ding-Yi Chen <dchen at redhat.com> - 0.2.3-1
- Inserted git pull for each fedpkg targets. Reduce the chance of conflict.
- Fixed target: bodhi_new. So it will actually run this command instead of
just showing it.

* Fri Oct 15 2010 Ding-Yi Chen <dchen at redhat.com> - 0.2.2-1
- Add new project building script.
- Build for EL-5, EL-6
- Add el5, el6 build.
- Fixed errors in UseFedpkg.
- Fixed target: tag
- Fixed target: bodhi_new

* Fri Oct 08 2010 Ding-Yi Chen <dchen at redhat.com> - 0.1.4-1
- Fixed error in UseFedpkg.

* Mon Oct 04 2010 Ding-Yi Chen <dchen at redhat.com> - 0.1.2-1
- Removed excess spaces.

* Mon Oct 04 2010 Ding-Yi Chen <dchen at redhat.com> - 0.1.1-1
- Added koji scratch build target.
- Fixed changelog_update.

* Mon Oct 04 2010 Ding-Yi Chen <dchen at redhat.com> - 0.1.0-1
- Initial package.

