# vim: set expandtab:
# ----------------------------------------------------------------------------
# Preamble
# ----------------------------------------------------------------------------
# fedpkg lint: W: no-documentation
# The %%doc directive below installs COPYING and uw_copy_040507.html
# as part of the main package, so this warning should not be generated; see
# https://fedoraproject.org/wiki/Common_Rpmlint_issues#no-documentation
# 'This would be rare as most packages should have some license text,
# a changelog or other information that is better placed in the main package
# instead of a -doc subpackage.'
#
# fedpkg lint: W: files-duplicate: 
# the files user_guide.html index.html in directory /usr/share/doc/cppad 
# are the same. This is because a redirect from index.hml to user_guide.html 
# will not reload when user_guide.html changes.
#
# fedora uses its own soversion number for cppad_lib
# 5.0 corresponds to version 20240000 
%define soversion 5.0

# This is really an out of soruce build because the source is in the
# CppAD-%%{version} sub-directory. The fedora macros are confused and need 
# this defined true.
%define __cmake_in_source_build 1
# ----------------------------------------------------------------------------

# Fedora Release starts with 1; see
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Versioning/
Name:    cppad
Version: 20250000.0
Release: 2%{?dist}
Summary: C++ Algorithmic Differentiation (AD), %{name}-devel and %{name}-doc
#
License: EPL-2.0 OR GPL-2.0-or-later
URL:     https://github.com/coin-or/CppAD
Source:  %{url}/archive/%{version}/CppAD-%{version}.tar.gz
#
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake >= 3.0
BuildRequires: make
BuildRequires: python-xrst >= 2025.0
BuildRequires: python-sphinx_rtd_theme
BuildRequires: python-toml
BuildRequires: python-sphinx-copybutton
BuildRequires: python-pyspellchecker
BuildRequires: python-furo


%description
C++ Algorithmic Differentiation (AD) library file libcppad_lib.so; 
see %{name}-devel and %{name}-doc.

# ---------------------------------------------------------------------------
%package devel
Summary: The %{name} C++ include files for Algorithmic Differentiation (AD)
Provides: %{name} = %{version}-%{release}
# Requested by bug report
#     https://bugzilla.redhat.com/show_bug.cgi?id=1197488
Provides: coin-or-cppad = %{version}-%{release}
Provides: coin-or-cppad-devel = %{version}-%{release}

%description devel
We refer to the step by step conversion from an algorithm that computes 
function values to an algorithm that computes derivative values as 
Algorithmic Differentiation (often referred to as Automatic Differentiation.) 
Given a C++ algorithm that computes function values, {name} generates an 
algorithm that computes its derivative values. A brief introduction to 
Algorithmic Differentiation (AD) can be found at 
     http://en.wikipedia.org/wiki/Automatic_differentiation
See the package %{name}-doc for documentation of this version of %{name}. 
The documentation, for the most recent version of %{name}, can be found at
     https://cppad.readthedocs.io

# ----------------------------------------------------------------------------
%package doc
Summary: Documentation for %{name}-devel
BuildArch: noarch

%description doc
The %{name}-doc package installs the HTML documentation for this version
of %{name}-devel in
     %{_docdir}/%{name}
The documentation, for the most recent version of %{name}, can be found at
     https://cppad.readthedocs.io/latest

# -----------------------------------------------------------------------------
# prep
# -----------------------------------------------------------------------------
%prep
#
# Create an empty directory named cppad-%%{version}, 
# changed into that directory and unpack Source.
%setup -q -c
#
# atomic_op.hpp
# Fix warning. This should not be necessary when version > 20250000.0
sed -i CppAD-%{version}/include/cppad/local/var_op/atomic_op.hpp \
   -e 's|arg_tmp\[1\];|*arg_tmp = { 0 };|'
#
# xrst.toml
# This is not a git repository so suppress the warning that could not double
# check that all the files with xrst commands were included.
echo ''                   >> CppAD-%{version}/xrst.toml
echo '[input_files]'      >> CppAD-%{version}/xrst.toml
echo 'data = [ ]'         >> CppAD-%{version}/xrst.toml
#
# CppAD-%%{version}/build/html
# run xrst to create the documentation files in the directory above
mkdir CppAD-%{version}/build
xrst --version
number_jobs=$(echo %{?_smp_mflags} | sed -e 's|[^0-9]*\([0-9]*\)[^0-9]*|\1|')
if [ "$number_jobs" == '' ]
then
   number_jobs='1'
fi
xrst \
   --config_file CppAD-%{version}/xrst.toml \
   --local_toc \
   --target html \
   --html_theme sphinx_rtd_theme \
   --index_page_name user_guide \
   --group_list default app \
   --number_jobs $number_jobs \
   --suppress_spell_warnings
#
# CppAD-%%{version}/build/html
# remove hidden files not needed for viewing documentation
rm CppAD-%{version}/build/html/.buildinfo
rm -r CppAD-%{version}/build/html/.doctrees
mv CppAD-%{version}/build/html html

#
# COPYING, uw_copy_040507.html
mv CppAD-%{version}/COPYING  COPYING
mv CppAD-%{version}/uw_copy_040507.html uw_copy_040507.html
#
# fix bug
# should not be needed once version > 20250000.0
cat << EOF > temp.sed
/setup_random(size_t& not_used)/! b end
: loop
N
/\\n *}/! b loop
s|^|# if ! CPPAD_IS_SAME_UNSIGNED_INT_SIZE_T\\n|
s|$|\\n# endif|
#
: end
EOF
sed -i.bak CppAD-%{version}/include/cppad/local/play/player.hpp -f temp.sed
#
# fix bug
# should not be needed once version > 20250000.0
cat << EOF > temp.sed
/CHECK_CXX_SOURCE_COMPILES/! b end
s|^|   SET(CMAKE_REQUIRED_DEFINITIONS "" )\\
   SET(CMAKE_REQUIRED_INCLUDES    "" )\\
   SET(CMAKE_REQUIRED_LIBRARIES   "" )\\
   IF( cppad_cxx_flags )\\
      SET(CMAKE_REQUIRED_FLAGS   "\${cppad_cxx_flags} \${CMAKE_CXX_FLAGS}" )\\
   ELSE( cppad_cxx_flags )\\
      SET(CMAKE_REQUIRED_FLAGS   "" )\\
   ENDIF( cppad_cxx_flags )\\
|
#
: end
EOF
sed -i.bak CppAD-%{version}/cmake/compile_source_test.cmake -f temp.sed
#
# ----------------------------------------------------------------------------
# cppad_lib: replace soversion number and ensure build type is release 
sed -i.bak CppAD-%{version}/cppad_lib/CMakeLists.txt \
    -e "s|print_variable(soversion)|SET(soversion %{soversion} )\n&|" \
    -e "s|\${cppad_debug_which}|debug_none|"
#
# ----------------------------------------------------------------------------
# Print machine epsilon before any other testing
cat << EOF > temp.cpp
# include <iostream>
# include <limits>
template <class Float> void print_epsilon(const char* type_name)
{   Float epsilon = std::numeric_limits<Float>::epsilon();
    std::cout << type_name << " epsilon = " << epsilon << "\n";
}
int main(void)
{   print_epsilon<float>("float");
    print_epsilon<double>("double");
    print_epsilon<long double>("long double");
    return 0;
}
EOF
g++ -std=c++11 temp.cpp -o temp
./temp > temp.out
cat temp.out
# ----------------------------------------------------------------------------
# Comment out test of to_string long double on ppc64le arch. Understanding why
# it is failing will have to wait until there is a fedora 36 ppc64le test machine.
### if [ "%{_arch}" == 'ppc64le' ]
### then
###     sed -i.bak CppAD-%{version}/example/utility/to_string.cpp \
###         -e 's|ok *&= *floating<long double>();|// &|'  
### fi
# ----------------------------------------------------------------------------
# build
# -----------------------------------------------------------------------------
%build
#
# 1. Cannot use %%{_includedir}, %%{_libdir}, %%{_datadir}, %%{_docdir} 
# because they are absolute paths. Relative values would be more flexible 
# because they can be combined with %%{_prefix} to get absolute values.
#
# 2. The debug_all is overridden for cppad_lib by the edit of
# cppad_lib/CMakeLists.txt above
#
# 3. The gnu c++ compiler seems to be generating an incorrect warning about
# array bounds in thread_alloc.hpp. Use -Wno-array-bounds to suppress it.
#
# cppad_cxx_flags
# extra C++ compiler flags
cppad_cxx_flags=\
'-Wall -pedantic-errors -std=c++11 -Wshadow -Wconversion  -Wno-array-bounds'
#
# CMake Warning:
# Manually-specified variables were not used by the project:
#    CMAKE_C_FLAGS_RELEASE
#    CMAKE_Fortran_FLAGS_RELEASE
#    CMAKE_INSTALL_DO_STRIP
#    INCLUDE_INSTALL_DIR
#    LIB_INSTALL_DIR
#    LIB_SUFFIX
#    SHARE_INSTALL_PREFIX
#    SYSCONF_INSTALL_DIR
#
%cmake --version
%cmake \
    -S CppAD-%{version} \
    -B . \
    \
    -D CMAKE_VERBOSE_MAKEFILE=0 \
    -G 'Unix Makefiles' \
    \
    -D cppad_prefix=%{_prefix} \
    -D cppad_postfix='' \
    \
    -D cmake_install_includedirs=include \
    -D cmake_install_libdirs=%{_lib} \
    \
    -D cmake_install_datadir=share \
    -D cmake_install_docdir=share/doc \
    \
    -D cmake_defined_ok=false \
    -D include_doc=false \
    -D cppad_static_lib=false \
    -D cppad_debug_and_release=true \
    \
    -D include_adolc=false \
    -D include_ipopt=false \
    -D include_cppadcg=false \
    \
    -D colpack_prefix='NOTFOUND' \
    -D fadbad_prefix='NOTFOUND' \
    -D sacado_prefix='NOTFOUND' \
    \
    -D cppad_cxx_flags="$cppad_cxx_flags" \
    -D cppad_profile_flag='' \
    -D cppad_testvector=cppad \
    -D cppad_max_num_threads=64 \
    -D cppad_tape_id_type=size_t \
    -D cppad_tape_addr_type='unsigned int' \
    -D cppad_debug_which='debug_all'
#
# see https://docs.fedoraproject.org/en-US/packaging-guidelines/
#   parallel_make
%make_build

# -----------------------------------------------------------------------------
# Install
# -----------------------------------------------------------------------------
%install
# https://docs.fedoraproject.org/en-US/packaging-guidelines/
#   why_the_makeinstall_macro_should_not_be_used
%make_install

%files
%{_libdir}/libcppad_lib.so.%{soversion}

# These documentation files come from the source code tarball
%doc COPYING uw_copy_040507.html


%files devel
%{_includedir}/%{name}
%{_datadir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/libcppad_lib.so

%files doc

# These documentation files are build by the xrst command above
%doc html

# -----------------------------------------------------------------------------
# Check
# -----------------------------------------------------------------------------
# use the installed include files to compile and run the tests
%check
make %{?_smp_mflags} check
# ----------------------------------------------------------------------------
# %%clean
# Use %%clean with no arguments to surpress the cleanup of BUILDROOT 
# This enables one to check that the necessary files are installed.
# ----------------------------------------------------------------------------
%changelog
* Sat Jan 18 2025 Brad Bell <bradbell at seanet dot com> - 20250000.0-1
- This fixes two bugs and will not be necessary
- once the upstream source advances to 20250000.1.

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20250000.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 14 2025 Brad Bell <bradbell at seanet dot com> - 20250000.0-1
- New upstream source cppad-20250000.0.

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20240000.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Mar 01 2024 Brad Bell <bradbell at seanet dot com> - 20240000.3-2
- This fixes a bug in fun2val.hpp. This change will not be necessary
- once the upstream source advances to 20240000.4.

* Sat Feb 17 2024 Brad Bell <bradbell at seanet dot com> - 20240000.3-1
- This fixes a long standing bug; see the heading 02-14 on
- https://cppad.readthedocs.io/latest/whats_new_24.html

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20240000.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20240000.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Brad Bell <bradbell at seanet dot com> - 20240000.2-1
- Upstream moved i386 special cases into cmake script.
- Checking that other upstream changes do not affect Fedora install.

* Tue Jan 09 2024 Brad Bell <bradbell at seanet dot com> - 20240000.1-1
- thread_alloc.hpp: i386 i686: fix allignment for doubles
- op_hash_table: i386 i686: avoid second specialization of is_pod for same type.
- xrst.toml: add comment about why we are adding to this file.
- xrst command: speed up parallel build by settting number_jobs.


* Mon Jan 08 2024 Brad Bell <bradbell at seanet dot com> - 20240000.1-1
- Upstream fix of bug found by build on buildvm-x86-16.iad2.fedoraproject.org

* Sat Jan 06 2024 Brad Bell <bradbell at seanet dot com> - 20240000.0-1
- New upstream source cppad-20240000.0.
- require python-xrst >= 2024.0
- xrst.toml: no need to change to pyenchant because pyspellchecker avaialble
- upstream source changed CPPAD_DEBUG_AND_RELEASE to a cmake argument

* Mon Dec 25 2023 Brad Bell <bradbell at seanet dot com> - 20230000.0-3
- migrated to SPDX license
- move %%doc directive before subpackages (becasue it is in main package)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20230000.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jan 29 2023 Brad Bell <bradbell at seanet dot com> - 20230000.0-1
- Move libcppad_lib.so to main package (fixes a fedpkg lint error).
- Fix comment about where doc files come from.
- Move %%define __cmake_in_source_build to top of spec file.
- Add discussion of fedpkg lint files-duplicate warning.

* Sat Jan 28 2023 Brad Bell <bradbell at seanet dot com> - 20230000.0-1
- Advance upstream source to 2023.
- Add python-xrst to BuildRequires so can buile documentation.
- Remove Source1, change Source0 -> Source, and make definition so tarball 
  has the same name as the directory it creates.
- Change URL from documentation to git repo so can use in Source definition.
- Change some cmake definitions from empty string to NOTFOUND.
- Explicity specify the source directory (-S) and binary (-B) in camke comamnd.
- Add comments about __cmake_in_source_build confusion
- Update comments about cmake settings and warnings

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20220000.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20220000.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat May 21 2022  Brad Bell <bradbell at seanet dot com> - 20220000.4-1
- Advance to upstream 20220000.4. Main motivation for this is to make 
  cppad_eigen.hpp work with Eigen 3.4.0.

* Mon Feb 14 2022  Brad Bell <bradbell at seanet dot com> - 20220000.1-1
- Not necessary to advance to 20220000.2 because Fedora build is getting
  correct result for cppad.pc.

* Wed Feb 02 2022  Brad Bell <bradbell at seanet dot com> - 20220000.1-1
- Try commenting out to_string test of long double on ppc56le arch.
  This problem does not reproduce on ppc64le-test.fedorainfracloud.org.

* Tue Feb 01 2022  Brad Bell <bradbell at seanet dot com> - 20220000.1-1
- Modify to_string.cpp patch to print out more information on failure.
- Add simple program to print machine epsilon before any other testing.

* Mon Jan 31 2022  Brad Bell <bradbell at seanet dot com> - 20220000.1-1
- Fix following long standing typos in cmake command:
- 1. cppad_test_vector -> cppad_testvector
- 2. cppad_max_num_theads -> cppad_max_num_threads
- Temporary change to debug ppc64le build failure: replace to_string.cpp
- Replace temporary change by a patch to example/utility/to_string.cpp

* Mon Jan 24 2022 Brad Bell <bradbell at seanet dot com> - 20220000.1-1
- Advance to upstream source 20220000.1
- Add -Wno-array-bounds to compiler flags (see remarks about this flag)

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20210000.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 02 2021 Brad Bell <bradbell at seanet dot com> - 20210000.7-1
- Advance to upstream source 20210000.7

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20210000.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Mar 07 2021 Brad Bell <bradbell at seanet dot com> - 20210000.5-2
- Remove %%debug_package (not necessary to create debug info).
- Use %%setup to unpack tarballs (sets premissions properly).
- Add comments about using %%clean to check BUILDROOT.

* Sun Feb 28 2021 Brad Bell <bradbell at seanet dot com> - 20210000.5-1
- Advance to upstream source 20210000.5
- Remove patches that are no longer necessary.
- Change: Source1, Source2 -> Source0, Source1.
- Change: make %%{?_smp_mflags} -> %%make_build
- Change: make install DESTDIR=%%{buildroot} -> %%make_install.

* Thu Feb 18 2021 Brad Bell <bradbell at seanet dot com> - 20210000.3-3
- Patch corresponding to bug fix in upstream source 20210000.5

* Tue Feb 02 2021 Brad Bell <bradbell at seanet dot com> - 20210000.3-2
- Patch corresponding to bug fix in upstream source 20210000.4

* Tue Jan 26 2021 Brad Bell <bradbell at seanet dot com> - 20210000.3-1
- Advance to upstream source 20210000.3
- Remove patches that are no longer necessary.
- Update cmake command line to new version of upstream source.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20200000.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 27 2020 Brad Bell <bradbell at seanet dot com> - 20200000.0-7
- Add _smp_mflags to the make check command (parallel make)
- Build Debuginfo version of the cppad_lib library.

* Sat Aug 01 2020 Brad Bell <bradbell at seanet dot com> - 20200000.0-6
- define __cmake_in_source_build see:
  https://docs.fedoraproject.org/en-US/packaging-guidelines/CMake/
- Change soversion edit so modified soversion displayed during cmake command

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20200000.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20200000.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20200000.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Brad Bell <bradbell at seanet dot com> - 20200000.0-2
- Remove comment about object library becasue install libcppadlib.so
- Patch to not install empty include (in 20200000.1 upstream)
- Patch to not use GreaterThanZero during reverse mode (in 2020000.2)
- Remove PowTestSeven which tested the GreaterThanZeor in reverse mode

* Thu Jan 02 2020 Brad Bell <bradbell at seanet dot com> - 20200000.0-1
- Advance to version 2020 of cppad
- This is a major change because it we need to install the binary cppad_lib.
- No longer have lint error because must build library before installing.
- Remove patch for upstream source < 20190200.5.
- No debug_package, so need to ensure CPPAD_DEBUG_AND_RELEASE always defined. 
- cppad_deprecatred is no longer in cmake command line.
- cppad_debug_which is set to debug_all and overridden for cppad_lib directory.

* Wed Sep 18 2019 Brad Bell <bradbell at seanet dot com> - 20190200.4-2
- fedpkg lint now reconizes EPL-2.0 license so remove comment about its error
- Use sed edit of 20190200.4 to obtain bug fix that is in 20190200.5

* Tue Aug 06 2019 Brad Bell <bradbell at seanet dot com> - 20190200.4-1
- Bug fix by advancing to upstream source 20190200.4

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20190200.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 29 2019 Brad Bell <bradbell at seanet dot com> - 20190200.0-3
- Bug fix corresponding to upstream source 20190200.3.
- Fix license field and add comment at top about fedpkg lint license mistake.

* Fri Feb 01 2019 Brad Bell <bradbell at seanet dot com> - 20190200.0-2
- Test with corrected version of source2; i.e., 20190200.doc.tar.gz

* Fri Feb 01 2019 Brad Bell <bradbell at seanet dot com> - 20190200.0-1
- Advance to version 2019 of cppad (actually 2019-02).
- Home page and sources have moved to github.
- Documentation is now a separate source tarball.
- Copyright changed from GPL3 -> EPL2 with GPL2 or later option.
- Change tabs to spaces and add 'vim: setexpandtab' command at top.
- Install pkgconfig files in both data and lib directories.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180000.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20180000.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20180000.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 02 2018 Brad Bell <bradbell at seanet dot com> - 20180000.0-1
- fedpkg lint no longer generates spelling error for use of 'devel'.
- Comment out %%clean because only the normal build area is used.
- Change minumum cmake version to 2.8 (needed for epel7 branch).
- Use comments to better group to sections of the spec file.

* Mon Jan 01 2018 Brad Bell <bradbell at seanet dot com> - 20180000.0-1
- Advance to version 2018 of cppad.

* Fri Nov 24 2017 Brad Bell <bradbell at seanet dot com> - 20170000.4-3
- Use sed to add bug fix corresponding to cppad-20170000.8.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170000.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170000.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr 03 2017 Brad Bell <bradbell at seanet dot com> - 20170000.4-1
- Advance to 20170000.4 to take advantage of some upstrean bug fixes.

* Tue Mar 07 2017 Brad Bell <bradbell at seanet dot com> - 20170000.3-1
- Advance to 20170000.3 to take advantage of some upstrean bug fixes.
- The results of cmake comman depend on the architecture, so remove 'noarch'
- see https://bugzilla.redhat.com/show_bug.cgi?id=1427391

* Thu Feb 16 2017 Brad Bell <bradbell at seanet dot com> - 20170000.1-3
- patch source to fix bug in ForSparseHes.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170000.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 Brad Bell <bradbell at seanet dot com> - 20170000.1-1
- Advance to version 2017 of cppad.
- New link for discussion of fedpkg lint warning rpm-builroot-usage
- (old link seems to have disappeared).
- Change CMakeLists.txtbak -> CMakeLists.txt.bak.
- Use find to create list of CMakeLists.txt files and check that edit
- of these files goes as expected.
- Include explicit setting of all possible cmake command options
- (empty prefix setting correspond to packages not included).
- cppad_sparse_list=YES removed (YES is now always chosen by upstream source)
- Change some comparisons to properly scale to machine epsilon.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20160000.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 1 2016 Brad Bell <bradbell at seanet do com> - 20160000.0-1
- Advance to version 2016 of cppad.
- Remove patch for static testing library (fixed upstream).
- Remove patch to avoid install of cppad_colpack.cpp (fixed upstream).
- Change cmake_install_prefix -> cppad_prefix (changed upstream).
- Change c++98 to c++11 so installed version can support both (new capability).
- Remove setting cppad_implicit_ctor_from_any type (no longer in upstream).
- Add setting cppad_deprecated (new upstream flag).
- Change original copy of files from *.stamp to *.bak
- Patch CMakeLists.txt files to remove building and use of cppad_lib object.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20150000.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 11 2015 Brad Bell <bradbell at seanet dot com> - 20150000.9-2
- Move Provides coin-or-cppad below %%package-devel;
- see https://bugzilla.redhat.com/show_bug.cgi?id=1197488

* Mon Mar 02 2015 Brad Bell <bradbell at seanet dot com> - 20150000.9-1
- 1: Advance to newer version of upstream source to fix some bugs.
- 2: Remove patch of test_more/optimize.cpp which is no longer necessary.
- 3: Add Provides coin-or-cppad.

* Mon Feb 09 2015 Brad Bell <bradbell at seanet dot com> - 20150000.4-3
- 1: Change std=c++11 to std=c++98 so works with rel6 (also so works
- in f20 and f21 when std=c++11 is not specified).
- 2: Change speed/src/libspeed_src to be a static library because it is only
- used for testing (shared library was not being found on epl6).
- 3: Cleanup %%{buildroot} at start so it can be used for debugging on failure.
- 4: Fix an exact equal check that should have been a near equal check.

* Sun Feb 01 2015 Brad Bell <bradbell at seanet dot com> - 20150000.4-2
- Fix rmplint warning about macro-in-comment.
- Edit comments at top of about warnings that won't be fixed.

* Sat Jan 31 2015 Brad Bell <bradbell at seanet dot com> - 20150000.4-1
- Advance to version 2015 of cppad.
- Ensure cmake >= 2.8; see https://bugzilla.redhat.com/show_bug.cgi?id=896116
- Remove patch for location of docdir (fixed upstream).
- Patch CMakeLists.txt to remove install of cppad_colpack.cpp (it is not used).
- List all cmake options (including defaults) that are used by this install.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140000.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140000.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild


* Tue Jan 21 2014 Brad Bell <bradbell at seanet dot com> - 20140000.2-1
- Advance to version 2014 of cppad.
- Add link to web discussion about rpm-buildroot-usage warning.
- Fix rpmlint warning about mixing tabs and spaces in spec file.

* Mon Oct 07 2013 Brad Bell <bradbell at seanet doc com> - 20130000.3-1
- 1. Use new upstream source to fix warnings generated by g++ 4.8.1.
- 2. As per https://fedoraproject.org/wiki/Changes/UnversionedDocdirs 
- move xml documentation from /usr/share/doc/%%{name}-%%{version} to
- /usr/share/doc/%%{name}

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130000.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 28 2013 Brad Bell <bradbell at seanet doc com> - 20130000.2-1
- Fix bug https://bugzilla.redhat.com/show_bug.cgi?id=913929
- in the upstream soruce and use the corresponding upstream release.
- Note, the previous commit, 20130000.1-3,  could have been avoided using
- https://fedoraproject.org/wiki/Using_the_Koji_build_system#Scratch_Builds

* Wed Feb 13 2013 Brad Bell <bradbell at seanet doc com> - 20130000.1-3
- Attempt to reproduce failure reported in bug id=913929
- (The build logs were deleted because I did not get to this soon enough)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130000.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 08 2013 Brad Bell <bradbell at seanet dot com> - 20130000.1-1
- Use a new upstream source.
- Remove the patches that were fixed in the upstream source. 
- Convert tabs to spaces (avoid rpmlint warning).
- Fix rpmlint warning for cppad-doc group warning.
- Add comment for rpmlint warning about using buildroot.

* Sat Jan 05 2013 Brad Bell <bradbell at seanet dot com> - 20130000.0-3
- The patch.sed script in this file is for a final test of a solution on the 
- remote machine. Expect to modify upstream source so it is not necessary.

* Fri Jan 04 2013 Brad Bell <bradbell at seanet dot com> - 20130000.0-2
- Debugging build to try to understand failure of test_more/epsilon.cpp
- on a remote machine that I do not have access to.

* Fri Jan 04 2013 Brad Bell <bradbell at seanet dot com> - 20130000.0-1
- Advance to version 2013 of cppad.
- Remove old patches that are no longer necessary.
- Convert from auto-tools to cmake build system.
- Add new patches (using sed in setup section) that are now necessary.
- Fix some bogus dates in change log by changing day of the week.
- Getting folloing incorrect warning from g++ during rpmbuild:
- .../cppad/thread_alloc.hpp:203:44: ... subsrcipt is above array bounds ... 

* Sun Oct 21 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 20120101.1-3
- Switch to arch'ed BuildArch.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120101.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan 18 2012 Brad Bell <bradbell at seanet dot com> - 20120101.1-1 
- Advance to version 2012 of cppad.
- Remove old patches that are no longer necessary.
- Add new patches (using sed in setup section) that are now necessary.
- Change comments about rpmlint output (using more recent version).

* Mon Oct 17 2011 Brad Bell <bradbell at seanet dot com> - 20110101.5-1
- Advance to next 2011 release to fix warnings generated by g++ 4.6.1.
- Fix comment as to when certain sed patching will no longer be necessary.
- Make sed patching of permissions in doc destination directory more specific.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110101.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 19 2011 Brad Bell <bradbell at seanet dot com> - 20110101.2-3
- Remove duplicate test results from build.log
- Improve comments before patching top level makefile.in.
- Fix rpmlint warnings about %%{_docdir}, %%{name}, and %%{version} in comments.
- Fix rpmlint warning by changing tabs to spaces.
- Fix rpmlint wrning by removing dot at end of Summary.
- Change RPM_BUILD_ROOT to _builddir.
- Improve comments (at top) about know rpmlint warnings.

* Tue Jan 18 2011 Brad Bell <bradbell at seanet dot com> - 20110101.2-2
- Fix rpmlint error, libdir-macro-in-noarch-package by moving the pkg-config 
- file cppad.pc from %%_libdir to %%_datadir.
- Improve the %%Summary and %%description entries.
- Fix some rpmlint spelling warnings including xml -> XML, html -> HTML. 
- Document (at top of spec file) reason for other warnings that are not fixed.

* Mon Jan 17 2011 Brad Bell <bradbell at seanet dot com> - 20110101.2-1 
- The fedora source 20110101.0 has the worng check sum, get new upstream source.
- Remove sed patches for problems that were fixed in upstream source.
- Change makefile.in so tests include from install (not distribute) directory
- (see comments above `find . -name 'makefile.in` above).

* Sun Jan 09 2011 Brad Bell <bradbell at seanet dot com> - 20110101.0-2
- Remove include/cppad_ipopt_nlp.hpp from distribution.
- Remove lib/libspeed.a from distribution.
- Add lib/pkgconfig/cppad.pc to files section (because it is installed).
- Use a single sed script file with comments to do all the makefile.in edits.
- Remove edits of makefile.am (not used so not reason to patch it).

* Sat Jan 08 2011 Brad Bell <bradbell at seanet dot com> - 20110101.0-1
- Use new major version for 2011.
- abs_top_builddir is missing from definitions in makefile.in 
- (should be fixed in future versions of cppad).
- The single command "make test" now builds and runs all the tests.

* Thu Jul 08 2010 Brad Bell <bradbell at seanet dot com> - 20100101.4-1
- Use new upstream source which has bug fix at revision
- https://projects.coin-or.org/CppAD/changeset/1698

* Wed Mar 31 2010 Brad Bell <bradbell at seanet dot com> - 20100101.2-1
- Use new upstream source with bug fixes at revision
- https://projects.coin-or.org/CppAD/changeset/1664
- and remove patch from Wed Feb 10 2010. 

* Wed Feb 10 2010 Brad Bell <bradbell at seanet dot com> - 20100101.0-2
- Patch sources for bug fix between 20100101.0 and 20100101.1.
- This should no longer be necessary once a new upstream source is loaded.

* Fri Jan 01 2010 Brad Bell <bradbell at seanet dot com> - 20100101.0-1
- Use new upstream source.
- Remove out of date comment about where this spec file is maintained.
- Remove patches that are no longer necessary in prep section.
- Change calling sequence for correctness of speed tests (we do not run speed
- tests, that requires a computer with no other processes running).

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090303.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 20 2009 Brad Bell <bradbell at seanet dot com> 20090303-4
- Patch cppad/local/fun_construct.hpp to give a more useful error message
- (so we can figure out why the Fedora 11 build is failing).

* Sat Jun 06 2009 Brad Bell <bradbell at seanet dot com> 20090303-3
- Patch file test_more/jacobian.cpp (required for versions below 20090606).
- Patch file cppad/local/default.hpp (required for versions below 20090606).
- Fix version (change 20080303 to 20090303) in previous two log entries.

* Mon Mar 30 2009 Brad Bell <bradbell at seanet dot com> 20090303-2
- Change tabs to spaces in spec file to avoid an rpmlint warning.
- The base package in previous release had no files, hence did not exist.
- Use Provides: in cppad-devel to indicate that it provides cppad.

* Sun Mar 29 2009 Brad Bell <bradbell at seanet dot com> 20090303-1
- Change to newer version of cppad.
- Create a base package that requres both devel and doc sub-packages

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080826.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Oct 08 2008 Brad Bell <bradbell at seanet dot com> 20080826-1
- Change to newer version of cppad.
- Change download directory to standard coin-or location.
- Remove editing of speed/main.cpp (no longer necessary).
- Add retape argument to check programs in speed directory.

* Fri Apr 04 2008 Brad Bell <bradbell at seanet dot com> 20080403-3
- Patch speed/main.cpp work with newer version of gcc
- (speed/main.cpp had not been tested with new version of gcc.)

* Thu Apr 03 2008 Brad Bell <bradbell at seanet dot com> 20080403-2
- Upload new source with the command
- make new-sources FILES="cppad-20080403.gpl.tgz"

* Thu Apr 03 2008 Brad Bell <bradbell at seanet dot com> 20080403-1
- New upstream version

* Sat Jan 12 2008  Brad Bell <bradbell at seanet dot com> 20071229-6
- Remove speed estimation correctness test because we are not in control of 
- which other jobs are on the machine that is doing the rpmbuild.

* Fri Jan 11 2008  Brad Bell <bradbell at seanet dot com> 20071229-5
- Remove introduction/exp_apx/exp_apx from the set of tests 
- (which should have been done in 20071229-4). 
- From now on test building rpm locally before making tags.

* Thu Jan 10 2008  Brad Bell <bradbell at seanet dot com> 20071229-4
- Add code to print out DBL_EPSILON at the beginning of the example tests.
- Remove --with-Introduction (it only checks by hand calculations that are in 
- AD Introduction section of the documentation). 
- Remove extra --with-Documentation

* Wed Jan 09 2008  Brad Bell <bradbell at seanet dot com> 20071229-3
- I mistakenly tried to make tag 20071229-2 in devel before committing local 
- changes. It appears tag was partially created, but not sure it is correct.
- So I am bumping the version number. 

* Wed Jan 09 2008  Brad Bell <bradbell at seanet dot com> 20071229-2
- Cygwin's version of md5sum puts a <space><star> between the check sum
- and the file name. Fedora build tools expect two spaces, so the star has
- was changed to a space in the devel, F-7, and F-8 sources file.

* Sat Dec 29 2007  Brad Bell <bradbell at seanet dot com> 20071229-1
- Fix gpl_license.sh in upstream source (missed some special cases).

* Thu Dec 27 2007 Brad Bell <bradbell at seanet dot com> 20071225-2
- Fix spelling errors in this file and day of the week errors in %%changelog.
- Add ChangeLog, AUTHORS, uw_copy_040507.html to devel %%doc files.
 
* Tue Dec 25 2007 Brad Bell <bradbell at seanet dot com> 20071225-1
- %%Source points to newly created directory for archived versions cppad
- modify makefile.in so does not set permissions for documentation files

* Fri Dec 21 2007 Brad Bell <bradbell at seanet dot com> 20071221-1
- Added introduction/exp_apx/exp_apx to the list of correctness tests.
- Use %% to avoid macro expansion in %%changelog.
- Remove tabs from this spec file.
- Remove period from end of base package summary.
- Change upstream makefile.am so that it copies directories instead of files.

* Thu Dec 20 2007 Brad Bell <bradbell at seanet dot com> 20071208-2
- Increment release number each time a new spec file is uploaded.
- Use the commands %%configure, %%check.
- Remove the %%doc command.
- Use more macros, including %%{?_smp_mflags}, %%{_includedir}, %%{_docdir}.

* Thu Dec 20 2007 Brad Bell <bradbell at seanet dot com> 20071208-1
- Remove comments, except for those that are useful to a fedora reviewer. 
- Use different Summary and description for each sub-package.
- Use %%{?dist} in Release entry.
- Use %%(%%{__id_u} -n) in BuildRoot entry. 
- Use noarch in BuildArch entry.
- Move -rf RPM_BUILD_ROOT from prep entry to install entry.
- Use macros where possible.

* Sat Dec 08 2007 Brad Bell <bradbell at seanet dot com> 20071208-1
- Fix all but one rpmlint warning (see Notes at beginning of this file).

* Mon Dec 03 2007 Brad Bell <bradbell at seanet dot com> 20071203-1
- first version of cppad that included RPM spec file.
