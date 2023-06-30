%if 0%{?rhel} == 9
# RHEL 9 is missing python-flexmock
%bcond_with tests
%else
%bcond_without tests
%endif


%global desc %{expand:
Python library for parsing and manipulating RPM spec files.
Main focus is on modifying existing spec files, any change should result
in a minimal diff.}


Name:           python-specfile
Version:        0.19.0
Release:        2%{?dist}

Summary:        A library for parsing and manipulating RPM spec files
License:        MIT
URL:            https://github.com/packit/specfile

Source0:        %{pypi_source specfile}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
%if %{with tests}
# tests/unit/test_guess_packager.py
BuildRequires:  git-core
%endif


%description
%{desc}


%package -n python%{python3_pkgversion}-specfile
Summary:        %{summary}


%description -n python%{python3_pkgversion}-specfile
%{desc}


%prep
%autosetup -p1 -n specfile-%{version}


%generate_buildrequires
%pyproject_buildrequires %{?with_tests: -x testing}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files specfile


%if %{with tests}
%check
%pytest
%endif


%files -n python%{python3_pkgversion}-specfile -f %{pyproject_files}
%doc README.md


%changelog
* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 0.19.0-2
- Rebuilt for Python 3.12

* Thu Jun 22 2023 Packit <hello@packit.dev> - 0.19.0-1
- Parsing has been optimized so that even spec files with hundreds of thousands of lines can be processed in reasonable time. (#240)

* Fri May 26 2023 Packit <hello@packit.dev> - 0.18.0-1
- Specfile library now handles multiple `%%changelog` sections. (#230)

* Thu May 11 2023 Packit <hello@packit.dev> - 0.17.0-1
- Added a new `guess_packager()` function that uses similar heuristics as `rpmdev-packager`, meaning that the `Specfile.add_changelog_entry()` method no longer requires `rpmdev-packager` to guess the changelog entry author. (#220)
- The `Specfile.add_changelog_entry()` method now uses dates based on UTC instead of the local timezone. (#223)

* Thu Apr 20 2023 Packit <hello@packit.dev> - 0.16.0-1
- Added `Specfile.has_autorelease` property to detect if a spec file uses the `%%autorelease` macro. (#221)

* Fri Mar 10 2023 Packit <hello@packit.dev> - 0.15.0-1
- Parsing the spec file by RPM is now performed only if really necessary, greatly improving performance in certain scenarios. (#212)
- Checked that license is a valid SPDX license.

* Thu Feb 23 2023 Packit <hello@packit.dev> - 0.14.0-1
- Fixed a bug that broke parsing in case spec file contained conditionalized macro definitions or similar constructs. (#209)
- Specfile no longer depends on rpm-py-installer, it now depends directly on rpm. (#207)

* Mon Jan 30 2023 Packit <hello@packit.dev> - 0.13.2-1
- Fixed infinite loop that occured when section options were followed by whitespace. (#197)

* Mon Jan 23 2023 Packit <hello@packit.dev> - 0.13.1-1
- Fixed a bug in section parsing that caused sections to be ignored when there were macro definitions spread across the spec file and not cumulated at the top. (#191)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 20 2023 Packit <hello@packit.dev> - 0.13.0-1
- Added `Section.options` attribute for convenient manipulation of section options. (#183)
- specfile now supports single-line sections where section content is represented by a macro starting with a newline. (#182)
- Added `evr` argument to `Specfile.add_changelog_entry()`. This allows adding a changelog entry with an EVR value that's different from the current specfile's value. This makes it easier to reconstruct a specfile's `%changelog` based on another source using the higher level interface. (#181)

* Fri Jan 06 2023 Packit <hello@packit.dev> - 0.12.0-1
- All classes including `Specfile` itself can now be copied using the standard `copy()` and `deepcopy()` functions from `copy` module. (#176)
- `Section.name` attribute has been renamed to a more fitting `Section.id`. (#167)
- `setup.cfg` now uses `license_files` instead of deprecated `license_file`. (#162)

* Wed Dec 14 2022 Packit <hello@packit.dev> - 0.11.1-1
- Tags enclosed in conditional macro expansions are not ignored anymore. (#156)
- Fixed context managers being shared between Specfile instances. (#157)

* Fri Dec 09 2022 Packit <hello@packit.dev> - 0.11.0-1
- Context managers (`Specfile.sections()`, `Specfile.tags()` etc.) can now be nested and combined together (with one exception - `Specfile.macro_definitions()`), and it is also possible to use tag properties (e.g. `Specfile.version`, `Specfile.license`) inside them. It is also possible to access the data directly, avoiding the `with` statement, by using the `content` property (e.g. `Specfile.tags().content`), but be aware that no modifications done to such data will be preserved. You must use `with` to make changes. (#153)

* Wed Nov 30 2022 Packit <hello@packit.dev> - 0.10.0-1
- Fixed an issue that caused empty lines originally inside changelog entries to appear at the end. (#140)
- Renamed the `ignore_missing_includes` option to a more general `force_parse`. If specified, it allows to attempt to parse the spec file even if one or more sources required to be present at parsing time are not available. Such sources include sources referenced from shell expansions in tag values and sources included using the `%include` directive. (#137)

* Sat Nov 12 2022 Packit <hello@packit.dev> - 0.9.1-1
- `specfile` now supports localized tags (e.g. `Summary(fr)`) and tags with qualifiers (e.g. `Requires(post)`).
  It also follows more closely rpm parsing logic and doesn't fail on invalid section names. (#132)

* Tue Oct 25 2022 Packit <hello@packit.dev> - 0.9.0-1
- Added utility classes for working with (N)EVR. (#113)
- Fixed an issue with multiple instances of `Specfile` not expanding macros in the right context. (#117)

* Fri Oct 14 2022 Packit <hello@packit.dev> - 0.8.0-1
- Added `Specfile.update_tag()` method that allows updating tag values while trying to preserve macro expansions. You can watch a demo on [YouTube](https://youtu.be/yzMfBPdFXZY). (#101)

* Fri Oct 07 2022 Packit <hello@packit.dev> - 0.7.0-1
- It is now possible to filter changelog entries by specifying lower bound EVR, upper bound EVR or both. (#104)
- Added support for filenames specified in source URL fragments, for example: `https://example.com/foo/1.0/download.cgi#/%{name}-%{version}.tar.gz` (#100)

* Thu Aug 25 2022 Packit <hello@packit.dev> - 0.6.0-1
- Switched to our own implementation of working with `%changelog` timestamps and removed dependency on arrow (#88)
- Fixed requires of EPEL 8 rpm (#86)

* Wed Aug 10 2022 Packit <hello@packit.dev> - 0.5.1-1
- Added new `%conf` section (#74)
- Switched to rpm-py-installer (#75)
- Fixed detecting extended timestamp format in `%changelog` (#77, #81)

* Fri Jul 22 2022 Packit <hello@packit.dev> - 0.5.0-1
- Strict optional typing is now enforced (#68)
- Fixed deduplication of tag names (#69)
- Sources and patches can now be removed by number (#69)
- Number of digits in a source number is now expressed the same way as packit does it (#69)
- Empty lines are now compressed when deleting tags (#69)
- Added convenience property for getting texts of tag comments (#69)
- Added convenience method for adding a patch (#69)

* Tue Jun 21 2022 Packit <hello@packit.dev> - 0.4.0-1
- Added convenience properties for most used tags (#63)
- Hardened linting by ignoring only specific mypy errors (#64)
- Fixed list of valid tag names and ensured newly added tags are not part of a condition block (#66)
- Initial patch number and its default number of digits are now honored (#66)
- Fixed a bug in `%prep` macro stringification (#67)

* Mon Jun 20 2022 Python Maint <python-maint@redhat.com> - 0.3.0-2
- Rebuilt for Python 3.11

* Mon May 16 2022 Packit <hello@packit.dev> - 0.3.0-1
- Made `Sources` a `MutableSequence` (#36)
- Started using consistent terminology for source numbers and added the option to insert a source with a specific number (#47)
- Added support for implicit source numbering (#48)
- Documented sources and `%prep` macros in README (#49)
- Implemented high-level manipulation of version and release (#54)
- Added support for `* Mon May 16 2022 John Doe <packager@example.com> - 0.3.0-1.fc35
- local build` (#56)
- Added `remote` property to sources and enabled addition of `Sources` (#59)
- Implemented mid-level manipulation of `%prep` section, including modification of `%prep` macros (#37, #52)


* Thu Mar 31 2022 Packit <hello@packit.dev> - 0.2.0-1
- Enabled Zuul CI (#8)
- Switched from git:// to https:// for rebase hook (#22)
- Updated pre-commit configuration and adapted to type changes brought by new version of mypy (#24)
- Non-lowercase section names are now supported (#26)
- Added `Sections.get()` convenience method (#29)
- Added packit configuration and enabled packit (#25)
- Fixed infinite recursion when deep-copying instances of `Sections` and `Tags` (#30)
- Updated Fedora and EPEL spec files (#32)
- Fixed issues caused by older versions of dependencies on EPEL 8 (#33)
- Implemented high-level manipulation of sources and patches (#20, #36)
- It is now possible to parse spec files with missing local sources (#23)

* Mon Feb 21 2022 Nikola Forró <nforro@redhat.com> - 0.1.1-1
- New upstream release 0.1.1

* Tue Feb 08 2022 Nikola Forró <nforro@redhat.com> - 0.1.0-1
- Initial package
