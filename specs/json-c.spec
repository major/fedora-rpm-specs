%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}

# We don't want accidental SONAME bumps.
# When there is a SONAME bump in json-c, we need to request
# a side-tag for bootstrap purposes:
#
# 1. Build a bootstrap build of the systemd package, and wait
#    for it to be available inside the side-tag.
# 2. Re-build the following build-chain for bootstrap:
#    json-c : cryptsetup
# 3. Untag the systemd bootstrap build from the side-tag, and
#    disable bootstrapping in the systemd package.  Re-build
#    the systemd package into Rawhide.
# 4. Wait for the changes to populate and re-build the following
#    chain into the side-tag:
#    satyr : libdnf libreport
# 5. Merge the side-tag using Bodhi.
#
# After that procedure any other cosumers can be re-build
# in Rawhide as usual.
%global so_ver 5

# Releases are tagged with a date stamp.
%global reldate 20240915


Name:           json-c
Version:        0.18
Release:        2%{?dist}
Summary:        JSON implementation in C

License:        MIT
URL:            https://github.com/%{name}/%{name}
Source0:        %{url}/archive/%{name}-%{version}-%{reldate}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  ninja-build
%ifarch %{valgrind_arches}
BuildRequires:  valgrind
%endif

%description
JSON-C implements a reference counting object model that allows you
to easily construct JSON objects in C, output them as JSON formatted
strings and parse JSON formatted strings back into the C representation
of JSON objects.  It aims to conform to RFC 7159.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.


%package        doc
Summary:        Reference manual for json-c

#BuildArch:     noarch

BuildRequires:  doxygen
BuildRequires:  hardlink

%description    doc
This package contains the reference manual for %{name}.


%prep
%autosetup -n %{name}-%{name}-%{version}-%{reldate} -p 1

# Remove pre-built html documentation.
rm -fr doc/html

# Update Doxyfile.
doxygen -s -u doc/Doxyfile.in


%build
%cmake \
  -DBUILD_STATIC_LIBS:BOOL=OFF       \
  -DCMAKE_BUILD_TYPE:STRING=RELEASE  \
  -DCMAKE_C_FLAGS_RELEASE:STRING=""  \
  -DDISABLE_BSYMBOLIC:BOOL=OFF       \
  -DDISABLE_WERROR:BOOL=ON           \
  -DENABLE_RDRAND:BOOL=ON            \
  -DENABLE_THREADING:BOOL=ON         \
  -G Ninja
%cmake_build --target all doc


%install
%cmake_install

# Documentation
mkdir -p %{buildroot}%{_pkgdocdir}
cp -a %{__cmake_builddir}/doc/html ChangeLog README README.* \
  %{buildroot}%{_pkgdocdir}
hardlink -cfv %{buildroot}%{_pkgdocdir}


%check
export USE_VALGRIND=0
%ctest
%ifarch %{valgrind_arches}
export USE_VALGRIND=1
%ctest
%endif
unset USE_VALGRIND


%ldconfig_scriptlets


%files
%license AUTHORS
%license COPYING
%{_libdir}/lib%{name}.so.%{so_ver}*


%files devel
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/ChangeLog
%doc %{_pkgdocdir}/README*
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%files doc
%if 0%{?fedora} || 0%{?rhel} >= 7
%license %{_datadir}/licenses/%{name}*
%endif
%doc %{_pkgdocdir}


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 04 2024 Tomas Korbar <tkorbar@redhat.com> - 0.18-1
- Update to 0.18
- Fixes: rhbz#2312454

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Aug 13 2023 Björn Esser <besser82@fedoraproject.org> - 0.17-1
- Update to 0.17
- Fixes: rhbz#2231647

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 02 2022 Björn Esser <besser82@fedoraproject.org> - 0.16-3
- Rebuilt for arc4random in glibc 2.36 (or later)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 17 2022 Tomas Korbar <tkorbar@redhat.com> - 0.16-1
- Update to 0.16
- Resolves: rhbz#2075376

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 08 2021 Björn Esser <besser82@fedoraproject.org> - 0.15-1
- Update to 0.15
- Backport several fixes from upstream commits
- Change doc package to be arched

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Björn Esser <besser82@fedoraproject.org> - 0.14-7
- Use new cmake macros

* Tue May 26 2020 Björn Esser <besser82@fedoraproject.org> - 0.14-6
- Build using Ninja instead of Make
- Add a patch to move Doxyfile into doc subdir
- Remove pre-built html documentation
- Update Doxyfile during %%prep
- Add a patch to apply some optimizations to arraylist
- Hardlink the files in %%_pkgdocdir

* Mon May 25 2020 Björn Esser <besser82@fedoraproject.org> - 0.14-5
- Run the testssuite with valgrind on %%valgrind_arches

* Mon May 18 2020 Björn Esser <besser82@fedoraproject.org> - 0.14-4
- Add a patch to fix a test
- Add a patch to fix generation of user-documentation

* Mon May 11 2020 Björn Esser <besser82@fedoraproject.org> - 0.14-3
- Add upstream patch fixing usage of errno in json_parse_uint64()

* Sun May 10 2020 Björn Esser <besser82@fedoraproject.org> - 0.14-2
- Add a patch to backport fixes applied on upstream master branch
- Re-enable RDRAND as json-c can detect broken implementations in CPUs now
- Disable -Werror during build

* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 0.14-1
- Update to 0.14

* Mon Apr 20 2020 Björn Esser <besser82@fedoraproject.org> - 0.13.99-0.4.20200416gita911439
- Remove config.h file from installation
- Drop hardlinking of the documentation files

* Thu Apr 16 2020 Björn Esser <besser82@fedoraproject.org> - 0.13.99-0.3.20200416gita911439
- Update to recent git snapshot

* Tue Apr 14 2020 Björn Esser <besser82@fedoraproject.org> - 0.13.99-0.2.20200414git7fb8d56
- Update to recent git snapshot

* Tue Apr 14 2020 Björn Esser <besser82@fedoraproject.org> - 0.13.99-0.1.20200414gitab5425a
- Update to recent git snapshot using forge macros

* Sun Apr 12 2020 Björn Esser <besser82@fedoraproject.org> - 0.13.1-11
- Drop bootstrap logic, as the package is no dependency of @build anymore
- Add some explicit BuildRequires, which were implicit
- Small spec file cleanups

* Sat Apr 11 2020 Björn Esser <besser82@fedoraproject.org> - 0.13.1-10
- Add explicit configure switch to disable rdrand
- Add explicit configure switch to enable linking with Bsymbolic
- Do not use macros to invoke executables
- Drop obsolete %%pretrans scriptlet

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 2019 Petr Menšík <pemensik@redhat.com> - 0.13.1-8
- Remove empty doc dir from library package

* Wed Nov 06 2019 Miroslav Lichvar <mlichvar@redhat.com> 0.13.1-7
- Disable rdrand support (#1745333)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 26 2019 Björn Esser <besser82@fedoraproject.org> - 0.13.1-5
- Use hardlink without full path to the binary (#1721964)
- Use new style bootstrap logic

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 08 2018 Björn Esser <besser82@fedoraproject.org> - 0.13.1-2
- Add some cherry-picked fixes from upstream master

* Tue Mar 06 2018 Björn Esser <besser82@fedoraproject.org> - 0.13.1-1
- New upstream release (rhbz#1552053)

* Tue Mar 06 2018 Björn Esser <besser82@fedoraproject.org> - 0.13.1-0.1
- Bootstrapping for so-name bump

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.13-6
- Switch to %%ldconfig_scriptlets

* Thu Dec 14 2017 Björn Esser <besser82@fedoraproject.org> - 0.13-5
- Update patch fixing a segfault caused by possible invalid frees

* Wed Dec 13 2017 Björn Esser <besser82@fedoraproject.org> - 0.13-4
- Add upstream patch fixing invalid free in some cases

* Wed Dec 13 2017 Björn Esser <besser82@fedoraproject.org> - 0.13-3
- Add upstream patch for adding size_t json_c_object_sizeof()
- Enable partial multi-threaded support

* Mon Dec 11 2017 Björn Esser <besser82@fedoraproject.org> - 0.13-2
- Drop json_object_private.h

* Mon Dec 11 2017 Björn Esser <besser82@fedoraproject.org> - 0.13-1
- New upstream release (rhbz#1524155)

* Sun Dec 10 2017 Björn Esser <besser82@fedoraproject.org> - 0.13-0.1
- Bootstrapping for so-name bump
- Keep json_object_private.h

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Björn Esser <besser82@fedoraproject.org> - 0.12.1-2
- Add patch to replace obsolete autotools macro

* Thu Apr 27 2017 Björn Esser <besser82@fedoraproject.org> - 0.12.1-1
- Update to new upstream release
- Introduces SONAME bump, that should have been in 0.12 already
- Unify %%doc
- General spec-file cleanup

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 29 2014 Christopher Meng <rpm@cicku.me> - 0.12-4
- SONAME bump postponed.

* Mon Jul 28 2014 Christopher Meng <rpm@cicku.me> - 0.12-3
- SONAME bump, see bug 1123785

* Fri Jul 25 2014 Christopher Meng <rpm@cicku.me> - 0.12-2
- NVR bump

* Thu Jul 24 2014 Christopher Meng <rpm@cicku.me> - 0.12-1
- Update to 0.12

* Sat Jul 12 2014 Tom Callaway <spot@fedoraproject.org> - 0.11-8
- fix license handling

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 09 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.11-7
- Address CVE-2013-6371 and CVE-2013-6370 (BZ #1085676 and #1085677).
- Enabled rdrand support.

* Mon Feb 10 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.11-6
- Bump spec.

* Sat Dec 21 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.11-5
- Run test suite during build.
- Drop empty NEWS from docs.

* Tue Sep 10 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.11-4
- Remove default warning flags so that package builds on EPEL as well.

* Sat Aug 24 2013 Remi Collet <remi@fedoraproject.org> - 0.11-3
- increase parser strictness for php

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 29 2013 Remi Collet <remi@fedoraproject.org> - 0.11-1
- update to 0.11
- fix source0
- enable both json and json-c libraries

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 24 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.10-2
- Compile and install json_object_iterator using Remi Collet's fix (BZ #879771).

* Sat Nov 24 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.10-1
- Update to 0.10 (BZ #879771).

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 23 2012 Jiri Pirko <jpirko@redhat.com> - 0.9-4
- add json_tokener_parse_verbose, and return NULL on parser errors

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Apr 06 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.9-1
- First release.
