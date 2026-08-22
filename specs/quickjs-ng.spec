Name: quickjs-ng
Summary: Small and embeddable JavaScript engine

# QuickJS's original code is all MIT.
#
# libunicode-table.h contains generated code, based on data from the
# Unicode Character Database, subject to the Unicode License v3.
License: MIT AND Unicode-3.0

Version: 0.16.2
Release: 1%{?dist}

URL: https://github.com/quickjs-ng/quickjs
Source0: %{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

# License text not included upstream.
# See: https://github.com/quickjs-ng/quickjs/pull/1531
Source1: Unicode-3.0.txt

# Enable checking against test262, the Official ECMAScript Conformance Test Suite.
%global with_test262 1

%if 0%{?with_test262}
# test262 is licensed under BSD-3-Clause, with the exception of
# 'ECMA TR-104.pdf' being subject to LicenseRef-ECMA-spec.
# See: https://gitlab.com/fedora/legal/fedora-license-data/-/work_items/711
%global test262_commit 5ef1e5723be95296f36afb0386676fed0205869c
Source90: https://github.com/tc39/test262/archive/%{test262_commit}/test262-%{test262_commit}.tar.gz

# Fix an endianness-affected test that works only on little-endian
Patch90: qjsng-bigendian.patch
%endif

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: make

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:  %{ix86}

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
QuickJS is a small and embeddable JavaScript engine.
It aims to support the latest ECMAScript specification.

This project is a fork of the original QuickJS project by Fabrice Bellard
and Charlie Gordon, after it went dormant, with the intent of reigniting
its development.

# -- libs

%package libs
Summary: Library providing a small JavaScript engine

%description libs
This package provides QuickJS-NG as a shared library.

# -- devel

%package devel
Summary: Development files for %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package provides files required for developing programs
requiring %{name}.

# -- docs

%package doc
BuildArch: noarch
Summary: Documentation for %{name}

%description doc
This package provides example files showing how to develop programs
using %{name}.

# -- subpackages end


%prep
%autosetup -N -n quickjs-%{version}
sed -e '/^QJS=.*$/d' -e '/^QJSC=.*$/d' -e 's/^codegen:.*$/codegen:/' -i Makefile
ln %{SOURCE1} ./

%if 0%{?with_test262}
	rmdir test262
	tar xzf %{SOURCE90}
	mv test262-%{test262_commit} test262
%endif

%autopatch -p1


%build
# QuickJS comes with an interpreter and a bytecode compiler. The interpreter embeds some bytecode.
# Start by building the compiler...
%cmake
%cmake_build --target qjsc

# ...then use it to regenerate the bytecode. (Yes, we're mixing CMake with plain Make here.)
%make_build codegen QJSC="$(pwd)/%{_vpath_builddir}/qjsc"

# Having regenerated what's needed, build everything a second time.
%cmake --fresh
%cmake_build


%install
%cmake_install

mv %{buildroot}%{_docdir}/quickjs %{buildroot}%{_docdir}/%{name}
cp -a docs/docs -t %{buildroot}%{_docdir}/%{name}/


%check
# make test
./%{_vpath_builddir}/run-test262 -c tests.conf

# You might notice that the test program prints a non-zero number of errors,
# but the test suite as a whole still passes. This is because some tests
# are expected to fail due to missing features or other known bugs.
# Check test262.conf and test262_errors.txt for details.
%if 0%{?with_test262}
	# make test262
	./%{_vpath_builddir}/run-test262 -m -c test262.conf -a
	# make test262-fast
	./%{_vpath_builddir}/run-test262 -m -c test262.conf -c test262-fast.conf -a
%endif


%files
%{_bindir}/qjs
%{_bindir}/qjsc
%{_mandir}/man1/qjs*.1*

%files libs
%doc README.md SECURITY.md
%license LICENSE Unicode-3.0.txt
%{_libdir}/libqjs.so.%{version}
%{_libdir}/libqjs.so.0

%files devel
%{_libdir}/libqjs.so
%{_libdir}/cmake/qjs/
%{_includedir}/quickjs.h

%files doc
%doc %{_docdir}/%{name}/


%changelog
* Thu Aug 20 2026 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.16.2-1
- Update to v0.16.2

* Tue Aug 04 2026 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.16.1-1
- Update to v0.16.1

* Fri Jul 31 2026 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.16.0-1
- Update to v0.16.0

* Thu Jun 04 2026 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.15.1-1
- Update to v0.15.1

* Thu May 21 2026 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.15.0-1
- Update to v0.15.0

* Sat Apr 11 2026 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.14.0-1
- Update to v0.14.0

* Fri Dec 12 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.11.0-2
- Add patches to fix test failures in i686 and s390x

* Sun Nov 09 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.11.0-1
- Update to v0.11.0
- Fix license file not being installed
- Fix .so.0 file being put in -devel package
- Fix running the test suite in %%check
- Add help2man-generated man pages

* Thu May 15 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.10.1-1
- Update to v0.10.1

* Wed May 07 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.10.0-1
- Update to v0.10.0

* Tue Feb 04 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.8.0-1
- Initial packaging
