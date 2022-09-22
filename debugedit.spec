Name: debugedit
Version: 5.0
Release: 5%{?dist}
Summary: Tools for debuginfo creation
License: GPLv3+ and GPLv2+ and LGPLv2+
URL: https://sourceware.org/debugedit/
Source0: https://sourceware.org/pub/debugedit/%{version}/%{name}-%{version}.tar.xz
Source1: https://sourceware.org/pub/debugedit/%{version}/%{name}-%{version}.tar.xz.sig
Source2: gpgkey-5C1D1AA44BE649DE760A.gpg

BuildRequires: make gcc
BuildRequires: pkgconfig(libelf)
BuildRequires: pkgconfig(libdw)
BuildRequires: help2man
BuildRequires: gnupg2

# For the testsuite.
BuildRequires: autoconf
BuildRequires: automake

# The find-debuginfo.sh script has a couple of tools it needs at runtime.
# For strip_to_debug, eu-strip
Requires: elfutils
# For add_minidebug, readelf, awk, nm, sort, comm, objcopy, xz
Requires: binutils, gawk, coreutils, xz
# For find and xargs
Requires: findutils
# For do_file, gdb_add_index
# We only need gdb-add-index, so suggest gdb-minimal (full gdb is also ok)
Requires: /usr/bin/gdb-add-index
Suggests: gdb-minimal
# For run_job, sed
Requires: sed
# For dwz
Requires: dwz
# For append_uniq, grep
Requires: grep

%global _hardened_build 1

Patch1: 0001-tests-Handle-zero-directory-entry-in-.debug_line-DWA.patch

%description
The debugedit project provides programs and scripts for creating
debuginfo and source file distributions, collect build-ids and rewrite
source paths in DWARF data for debugging, tracing and profiling.

It is based on code originally from the rpm project plus libiberty and
binutils.  It depends on the elfutils libelf and libdw libraries to
read and write ELF files, DWARF data and build-ids.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
autoreconf -f -v -i
%configure
%make_build

%install
%make_install
# Temp symlink to make sure things don't break.
cd %{buildroot}%{_bindir}
ln -s find-debuginfo find-debuginfo.sh

%check
# The testsuite should be zero fail.
make check %{?_smp_mflags}

%files
%license COPYING COPYING3 COPYING.LIB
%doc README
%{_bindir}/debugedit
%{_bindir}/sepdebugcrcfix
%{_bindir}/find-debuginfo
%{_bindir}/find-debuginfo.sh
%{_mandir}/man1/debugedit.1*
%{_mandir}/man1/sepdebugcrcfix.1*
%{_mandir}/man1/find-debuginfo.1*

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 10 2022 Romanos Skiadas <rom.skiad@gmail.com> - 5.0-4
- Remove CFLAGS/LDFLAGS sed as they are already set to "" by debugedit

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 30 2021 Mark Wielaard <mjw@fedoraproject.org> - 5.0-2
- Add testsuite fix for GCC 11.2.1

* Mon Jul 26 2021 Mark Wielaard <mjw@fedoraproject.org> - 5.0-1
- Upgrade to upstream 5.0 release.

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Mark Wielaard <mjw@fedoraproject.org> - 0.3-1
- Update to upstream 0.3 pre-release. Removes find-debuginfo .sh suffix.
  - This release still has a find-debuginfo.sh -> find-debuginfo symlink.

* Wed May  5 2021 Mark Wielaard <mjw@fedoraproject.org> - 0.2-1
- Update to upstream 0.2 pre-release. Adds documentation.

* Wed Apr 28 2021 Mark Wielaard <mjw@fedoraproject.org> - 0.1-5
- Add dist to Release. Use file dependency for /usr/bin/gdb-add-index.

* Tue Apr 27 2021 Mark Wielaard <mjw@fedoraproject.org> - 0.1-4
- Use numbered Sources and https.

* Mon Apr 26 2021 Mark Wielaard <mjw@fedoraproject.org> - 0.1-3
- Fix some rpmlint issues, add comments, add license and doc,
  gpg verification, use pkgconfig BuildRequires, enable _hardened_build

* Mon Mar 29 2021 Panu Matilainen <pmatilai@redhat.com>
- Add pile of missing runtime utility dependencies

* Tue Mar 23 2021 Panu Matilainen <pmatilai@redhat.com>
- Initial packaging
