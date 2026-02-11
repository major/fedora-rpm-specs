%global _binaries_in_noarch_packages_terminate_build %{nil}

%global llvm_test_suite_version 21.1.8
#global rc_ver 3
%global test_suite_srcdir test-suite-%{llvm_test_suite_version}%{?rc_ver:-rc%{rc_ver}}.src.fedora

%bcond_with snapshot_build

%if %{with snapshot_build}
%include %{_sourcedir}/version.spec.inc
%global llvm_test_suite_version_suffix pre%{llvm_test_suite_date}.g%{llvm_test_suite_git_revision_short}
%global test_suite_srcdir llvm-test-suite-%{llvm_test_suite_git_revision}.fedora
%endif

Name:		llvm-test-suite
Version:	%{llvm_test_suite_version}%{?rc_ver:~rc%{rc_ver}}%{?llvm_test_suite_version_suffix:~%{llvm_test_suite_version_suffix}}
Release:	%autorelease
Summary:	C/C++ Compiler Test Suite

License:	NCSA AND BSD-3-Clause-LBNL AND BSD-4.3TAHOE AND dtoa AND GPL-1.0-only AND GPL-2.0-or-later AND GPL-2.0-only AND MIT AND PSF-2.0 AND LicenseRef-Fedora-Public-Domain AND LicenseRef-Fedora-UltraPermissive AND AML AND Rdisc AND Apache-2.0 AND LGPL-3.0-only
URL:		http://llvm.org
# The LLVM Test Suite contains programs with "BAD" or unknown licenses which should
# be removed.  Some of the unknown licenses may be OK, but until they are reviewed,
# we will remove them.
# Use the pkg_test_suite.sh script to generate the test-suite tarball:
# ./pkg_test_suite.sh

# this condition is set by ./pkg_test_suite.sh to retrieve original sources
%if 0%{?original_sources:1}
%if %{with snapshot_build}
Source0:	https://github.com/llvm/llvm-test-suite/archive/%{llvm_test_suite_git_revision}.tar.gz
%else
Source0:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{llvm_test_suite_version}%{?rc_ver:-rc%{rc_ver}}/test-suite-%{llvm_test_suite_version}%{?rc_ver:-rc%{rc_ver}}.src.tar.xz
%endif
%else
Source0:	%{test_suite_srcdir}.tar.xz
%endif
Source1:	license-files.txt
Source2:	pkg_test_suite.sh
Source3:	changelog
%if %{with snapshot_build}
Source1000: version.spec.inc
%endif
BuildArch:	noarch

# We need python3-devel for pathfix.py.
BuildRequires: python3-devel

Requires: cmake
Requires: libstdc++-static
Requires: python3-lit >= 0.8.0
Requires: llvm
Requires: tcl
Requires: which

%description
C/C++ Compiler Test Suite that is maintained as an LLVM sub-project.  This test
suite can be run with any compiler, not just clang.


%prep
%autosetup -n %{test_suite_srcdir} -p1

%py3_shebang_fix \
	ParseMultipleResults \
	utils/*.py \
	CollectDebugInfoUsingLLDB.py \
	CompareDebugInfo.py \
	FindMissingLineNo.py \
	MicroBenchmarks/libs/benchmark/googletest/googlemock/test/*.py \
	MicroBenchmarks/libs/benchmark/googletest/googletest/test/*.py \
	MicroBenchmarks/libs/benchmark/tools/*.py

# get-report-time was removed in llvm-test-suite 23.
if [ -f tools/get-report-time ]; then
%py3_shebang_fix tools/get-report-time
fi

chmod -R -x+X ABI-Testsuite

# Merge Licenses into a single file
cat %{SOURCE1} | while read FILE; do
	echo $FILE >> LICENSE.TXT
	cat ./$FILE >> LICENSE.TXT
done

%build

#nothing to do

%install
mkdir -p %{buildroot}%{_datadir}/llvm-test-suite/
cp -R %{_builddir}/%{test_suite_srcdir}/* %{buildroot}%{_datadir}/llvm-test-suite


%files
%license LICENSE.TXT
%{_datadir}/llvm-test-suite/


%changelog
%{?autochangelog:%autochangelog}
%{!?autochangelog:%include %{_sourcedir}/changelog}
