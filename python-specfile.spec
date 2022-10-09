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
Version:        0.7.0
Release:        1%{?dist}

Summary:        A library for parsing and manipulating RPM spec files
License:        MIT
URL:            https://github.com/packit/specfile

Source0:        %{pypi_source specfile}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


%description
%{desc}


%package -n python%{python3_pkgversion}-specfile
Summary:        %{summary}


%description -n python%{python3_pkgversion}-specfile
%{desc}


%prep
%autosetup -p1 -n specfile-%{version}
# Use packaged RPM python bindings downstream
sed -i 's/rpm-py-installer/rpm/' setup.cfg


%generate_buildrequires
%pyproject_buildrequires %{?with_tests: -x testing}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files specfile


%if 0%{?with_tests}
%check
%pytest
%endif


%files -n python%{python3_pkgversion}-specfile -f %{pyproject_files}
%doc README.md


%changelog
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
