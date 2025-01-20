# vim: syntax=spec

%global libdir %{_prefix}/lib

Name: rpkg-macros
Version: 2.0
Release: 11%{?dist}
Summary: Set of preproc macros for rpkg utility
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: https://pagure.io/rpkg-util.git

%if 0%{?fedora} || 0%{?rhel} > 6
VCS: git+https://pagure.io/rpkg-util#280343176796be54686f84a677f5744027ce84e9:macros
%endif

# Source is created by:
# git clone https://pagure.io/rpkg-util.git
# cd rpkg-util/macros
# git checkout rpkg-macros-2.0-1
# ./rpkg spec --sources
Source0: rpkg-util-macros-28034317.tar.gz

BuildArch: noarch

BuildRequires: bash
BuildRequires: preproc
%if 0%{?fedora}
BuildRequires: git-core
%else
BuildRequires: git
%endif
BuildRequires: coreutils
BuildRequires: findutils
BuildRequires: rpm-git-tag-sort

Requires: bash
%if 0%{?fedora}
Requires: git-core
%else
Requires: git
%endif
Requires: coreutils
Requires: findutils
Requires: rpm-git-tag-sort

%description
Set of preproc macros to be used by rpkg utility. They
are designed to dynamically generate certain parts
of rpm spec files. You can use those macros also without
rpkg by:

   $ cat <file_with_the_macros> | preproc -s /usr/lib/rpkg.macros.d/all.bash -e INPUT_PATH=<file_with_the_macros>

INPUT_PATH env variable is passed to preproc to inform
macros about the input file location. The variable is used
to derive INPUT_DIR_PATH variable which rpkg macros use.

If neither INPUT_PATH nor INPUT_DIR_PATH are specified,
INPUT_PATH will stay empty and INPUT_DIR_PATH will default
to '.' (the current working directory).

Another option to experiment with the macros is to source
/usr/lib/rpkg.macros.d/all.bash into your bash environment
Then you can directly invoke the macros on your command-line
as bash functions. See content in /usr/lib/rpkg.macros.d to
discover available macros.

Please, see man rpkg-macros for more information.

%prep
%setup -T -b 0 -q -n rpkg-util-macros

%check
export GIT_CONFIG_GLOBAL=`pwd`/gitconfig
git config --global protocol.file.allow always
git config --global init.defaultBranch master
PATH=bin/:$PATH tests/run

%install
install -d %{buildroot}%{libdir}
install -d %{buildroot}%{libdir}/rpkg.macros.d
cp -ar macros.d/* %{buildroot}%{libdir}/rpkg.macros.d

install -d %{buildroot}%{_bindir}
install -p -m 755 bin/pack_sources %{buildroot}%{_bindir}/pack_sources

install -d %{buildroot}%{_mandir}/man1
install -p -m 644 man/rpkg-macros.1 %{buildroot}/%{_mandir}/man1/

%files
%{!?_licensedir:%global license %doc}
%license LICENSE
%{libdir}/rpkg.macros.d
%{_bindir}/pack_sources
%{_mandir}/man1/rpkg-macros.1*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0-10
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 18 2021 clime <clime@fedoraproject.org> 2.0-1
- derive GIT_ROOT and other git properties from the INPUT_DIR_PATH directory
- INPUT_DIR_PATH, if not specified, is derived from INPUT_PATH

* Mon Nov 30 2020 clime <clime@fedoraproject.org> 1.1-1
- add trick in pack_sources to allow creating the archive in CWD

* Mon Oct 05 2020 clime <clime@fedoraproject.org> 1.0-1
- fix version check in git_pack
- rpm-git-tag-sort is also required during build for tests
- add man pages for rpkg-macros, redirect there from MACRO REFERENCE
  in man rpkg
- fix parameter order for rpm-git-tag-sort in git_merged_tag_refs
- fix version parsing from the latest tag, package name may contain
  dashes!
- implement support for multiple Sources at once
- use rpm-git-tag-sort for tag sorting & filtering in git_merged_tag_refs
submodules
- fix git_head for detached head state
- in git_bumped_version, lead must be numeric and greater than zero to output
follow as zero + small code tweak in git_version_generic
- remove now unused git_bumped_release, set "" as default for lead in
git_bumped_version
- make lead="" the only special case, otherwise lead is lead
- unify code and params for git_release and git_version
- code cleanup

* Tue Mar 10 2020 clime <clime@fedoraproject.org> 0.4-1
- remove shebangs in library files according to Fedora review
- changes according to review - usage of %%{_prefix} in spec, g-w for
pack_sources
- use git-core on Fedoras

* Fri Mar 06 2020 clime <clime@fedoraproject.org> 0.3-1
- fix warning about unset git indetity in test_submodule_sources
- skip test for submodule_sources on epel6
- add missing sleep in tests, add TODO
- fix changelog renderring for legacy git as there is no points-at
  option
- resolve problem in git_pack and submodules for epel7

* Wed Mar 04 2020 clime <clime@fedoraproject.org> 0.2-1
- fix bug on centos7 bash in is_physical_subpath function

* Wed Mar 04 2020 clime <clime@fedoraproject.org> 0.1-1
- initial release
