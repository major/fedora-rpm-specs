%global htmldocdir %{_docdir}/dwgrep/html

Name:           dwgrep
Version:        0.4
Release:        22%{?dist}
Summary:        A tool for querying Dwarf (debuginfo) graphs

# Automatically converted from old format: GPLv3+ and (GPLv2+ or LGPLv3+) - review is highly recommended.
License:        GPL-3.0-or-later AND ( GPL-2.0-or-later OR LGPL-3.0-or-later )
URL:            http://pmachata.github.io/dwgrep/index.html
Source0:        https://github.com/pmachata/dwgrep/archive/%{version}/dwgrep-%{version}.tar.gz

Patch0:         include.patch
# Upstream commit a6443a883650 ("cmake/modules/FindDWARF: Do not depend on libebl")
# https://bugzilla.redhat.com/show_bug.cgi?id=1799294
Patch1:         0001-cmake-modules-FindDWARF-Do-not-depend-on-libebl.patch
# Upstream commit 2157fb8e1d36 ("CMakeLists: Declare CMP0075 as NEW")
Patch2:         0002-CMakeLists-Declare-CMP0075-as-NEW.patch
# Upstream commit bed210af1278 ("libzwerg/dwgrep-gendoc: Do not return std::move")
Patch3:         0003-libzwerg-dwgrep-gendoc-Do-not-return-std-move.patch
# Upstream commit 1475b6f2fcc0 ("libzwerg/parser.yy: Use new %%define-based declarations for Bison")
Patch4:         0004-libzwerg-parser.yy-Use-new-define-based-declarations.patch
# Upstream commit fa7830f5f27f ("libzwerg/pred_result, libzwerg/value: Add ostream operators"
Patch5:         0005-libzwerg-pred_result-libzwerg-value-Add-ostream-oper.patch
# Upstream commit b2c296979046 ("libzwerg/selector: Rewrite assertion on value_type::code() return type"
Patch6:         0006-libzwerg-selector-Rewrite-assertion-on-value_type-co.patch
# Upstream commit 81597f312b22 ("CMakeLists: Bump minimum C++ version")
# https://bugzilla.redhat.com/show_bug.cgi?id=2225763
Patch7:         0007-CMakeLists-Bump-minimum-C-version.patch
# Upstream commit 11721b78b67e ("libzwerg: Drop std-memory.hh, std-utility.hh")
# One hunk dropped because it's not applicable to 0.4.
Patch8:         0008-libzwerg-Drop-std-memory.hh-std-utility.hh.patch

Requires: libzwerg%{?_isa} = %{version}-%{release}

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  elfutils-devel
BuildRequires:  flex
BuildRequires:  gtest-devel
BuildRequires:  python3-sphinx
BuildRequires:  make

# Sphinx-generated documentation apparently bundles jquery.  An
# exception is granted for bundling jquery in particular.
# https://fedorahosted.org/fpc/ticket/408
Provides:       bundled(jquery)

%description

Dwgrep is a tool, an associated language (called Zwerg) and a library
(libzwerg) for querying Dwarf (debuginfo) graphs.

You can think of dwgrep expressions as instructions describing a path
through a graph, with assertions about the type of nodes along the
way: that a node is of given type, that it has a given attribute,
etc. There are also means of expressing sub-conditions,
i.e. assertions that a given node is acceptable if a separate
expression matches (or does not match) a different path through the
graph.


%package -n libzwerg
Summary:        Library for querying Dwarf (debuginfo) graphs

%description -n libzwerg

Libzwerg contains implementation of the Zwerg query engine as well as
individual words of both Core and Dwarf vocabularies.

%ldconfig_scriptlets -n libzwerg


%package -n libzwerg-devel
Summary:        Headers and shared development libraries for libzwerg
Requires:       libzwerg%{?_isa} = %{version}-%{release}
Requires:       elfutils-devel%{?_isa}

%description -n libzwerg-devel
Headers and shared object symbolic links for the Boost C++ libraries.


%package doc
Summary:        HTML documentation for dwgrep and libzwerg
BuildArch:      noarch

%description doc

This package contains dwgrep-related documentation in the HTML
format. The documentation provides the same content as that on the
Boost web page (http://pmachata.github.io/dwgrep/).


%prep
%setup -q -n dwgrep-%{version}
%patch 0 -p1
%patch 1 -p1
%patch 2 -p1
%patch 3 -p1
%patch 4 -p1
%patch 5 -p1
%patch 6 -p1
%patch 7 -p1
%patch 8 -p1


%build
mkdir build
pushd build
%cmake -B . -S ..
make %{?_smp_mflags}
make doc
popd


%install
pushd build

make install DESTDIR=$RPM_BUILD_ROOT

# We carry HTML documentation in a separate -doc subpackage.  However,
# we would still like the documentation to be installed to
# /usr/share/dwgrep as opposed to /usr/shared/dwgrep-doc.  So install
# it here by hand, and below in %%files, have HTML be owned by the doc
# subpackage and exclude it from the main package.
mkdir -p $RPM_BUILD_ROOT%{htmldocdir}
cp -Rp doc/html/* $RPM_BUILD_ROOT%{htmldocdir}

popd


%check
pushd build
make test
popd


%files
%doc NEWS README
%exclude %{htmldocdir}
%license COPYING COPYING-LGPLV3
%{_bindir}/dwgrep
%{_mandir}/man1/dwgrep.1*

%files doc
# Both -doc subpackage and main package should own the documentation
# package, because both put files in there.
%dir %{_docdir}/dwgrep
%{htmldocdir}

%files -n libzwerg
%license COPYING COPYING-LGPLV3
%{_libdir}/libzwerg.so.0.1

%files -n libzwerg-devel
# N.B.: COPYING* brought in by the libzwerg dependency.
%dir %{_includedir}/libzwerg
%{_includedir}/libzwerg/libzwerg.h
%{_includedir}/libzwerg/libzwerg-dw.h
%{_libdir}/libzwerg.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug  7 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4-21
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon May 13 2024 Petr Machata <pmachata@gmail.com> - 0.4-19
- Add 0007-CMakeLists-Bump-minimum-C-version.patch
  - Fixes: BZ#2225763
- Add 0008-libzwerg-Drop-std-memory.hh-std-utility.hh.patch
  - This removes code that was always meant as a stop-gap and now that
    C++14 is assumed, there's no place for it anymore. It's now actually
    more likely to harm the build than anything else.
- Change %patchX to %patch X, as per rpmbuild complaints.

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun May  8 2022 Petr Machata <me@pmachata.org> - 0.4-13
- Add 0005-libzwerg-pred_result-libzwerg-value-Add-ostream-oper.patch
- Add 0006-libzwerg-selector-Rewrite-assertion-on-value_type-co.patch
- The cmake macro now passes -S . by default, which breaks the build.
  Fix by overriding with -S .. explicitly.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Oct 25 2020 Petr Machata <me@pmachata.org> - 0.4-9
- The cmake macro now passes -B <arch> by default, which breaks the build.
  Fix by overriding with -B . explicitly.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 18 2020 Petr Machata <me@pmachata.org> - 0.4-6
- Add 0001-cmake-modules-FindDWARF-Do-not-depend-on-libebl.patch
  - Fixes: BZ#1799294
- Add 0002-CMakeLists-Declare-CMP0075-as-NEW.patch
- Add 0003-libzwerg-dwgrep-gendoc-Do-not-return-std-move.patch
- Add 0004-libzwerg-parser.yy-Use-new-define-based-declarations.patch

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 2019 Jeff Law <law@redhat.com> - 0.4-4
- Add missing #includes exposed by gcc-10 testing.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 28 2018 Petr Machata <pmachata@gmail.com> - 0.4-1
- Rebase to 0.4

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan  2 2018 Petr Machata <pmachata@gmail.com> - 0.3-4
- Add dwgrep-0.3-subop-reset.patch

* Tue Dec 26 2017 Petr Machata <pmachata@gmail.com> - 0.3-3
- Add a full V-R dependency of dwgrep on libzwerg so that they update together.

* Sun Dec 24 2017 Petr Machata <pmachata@gmail.com> - 0.3-2
- Depend on python3-sphinx, not python-sphinx.
  This resolves a taskotron citation.

* Thu Dec 21 2017 Petr Machata <pmachata@gmail.com> - 0.3-1
- Rebase to 0.3
- Drop dwgrep-0.2-functional-header.patch
- Add dwgrep-0.3-macro_gnu.patch

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2-5
- Fix build (#1423345)

* Fri Feb 17 2017 Jonathan Wakely <jwakely@redhat.com> - 0.2-5
- Add patch to fix build with GCC 7

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.2-2
- Rebuilt for GCC 5 C++11 ABI change

* Sat Feb 28 2015 Petr Machata <pmachata@redhat.com> - 0.2-1
- Rebase to 0.2
- Drop dwgrep-0.1-mpz_class-ctor.patch

* Wed Jan  7 2015 Petr Machata <pmachata@redhat.com> - 0.1-6
- Fix compilation on s390 (31-bit)

* Fri Jan  2 2015 Petr Machata <pmachata@redhat.com> - 0.1-5
- Per the review (BZ 1172800):
  - Move HTML documentation to main package's docdir instead of doc
    subpackage's docdir, but still have doc subpackage own it.

* Fri Dec 19 2014 Petr Machata <pmachata@redhat.com> - 0.1-4
- Per the review (BZ 1172800):
  - Just use %%{version} instead of %%{hash}
  - Use %%license to install license files
  - Fix overly specific dependency of elfutils-devel
  - Provide bundled(jquery)

* Thu Dec 11 2014 Petr Machata <pmachata@redhat.com> - 0.1-3
- Per the review (BZ 1172800):
  - Drop %%defattr which rpmbuild handles automatically
  - Likewise with rm -rf $BUILDROOT in %%install
  - Split BR's to individual lines
  - Own the directory /usr/include/libzwerg

* Wed Dec 10 2014 Petr Machata <pmachata@redhat.com> - 0.1-2
- Add BR cmake, flex, bison.

* Mon Dec  8 2014 Petr Machata <pmachata@redhat.com> - 0.1-1
- Initial package.
