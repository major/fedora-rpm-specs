Name:           fastbit
Version:        2.0.3
Release:        32%{?dist}
Summary:        An Efficient Compressed Bitmap Index Technology
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://sdm.lbl.gov/fastbit/
Source0:        https://code.lbl.gov/frs/download.php/file/426/%{name}-%{version}.tar.gz

# Code patch to fix format truncation issue, sent to upstream ML
Patch0:         fastbit_format_truncation.patch

# Code patch to fix FSF address in fbmerge.cpp, sent to upstream ML
Patch1:         fastbit_fsf_address.patch

# Code patch to remove indentation warnings, sent to upstream ML
Patch2:         fastbit_indentation.patch

# Code patch to remove unused variable warnings, sent to upstream ML
Patch3:         fastbit_unused_variable.patch

# Build system patch to ensure linkage to pthread
Patch10:        fastbit_pthread_linkage.patch

# Build system patch for tests to use compiled binaries, not libtool wrappers
Patch11:        fastbit_tests_use_binaries.patch

Patch30:        %{name}-gcc11.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl-interpreter

%description
FastBit is an open-source data processing library following the spirit of NoSQL
movement. It offers a set of searching functions supported by compressed bitmap
indexes. It treats user data in the column-oriented manner similar to
well-known database management systems such as Sybase IQ, MonetDB, and Vertica.
It is designed to accelerate user's data selection tasks without imposing undue
requirements.

%package devel
Summary: FastBit development
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Development package for FastBit.  Includes headers, libraries and man pages for
using FastBit API.

%prep
%autosetup -p1 -n %{name}-%{version}

echo fixing permissions ...
find . -type f -perm /0111 \
    \( -name \*.cpp -or -name \*.h -or -name \*.yy -or -name \*.ll -or \
       -name \*.html -or -name README \) -print -exec chmod 0644 {} \;

%build
aclocal -I tests/m4
autoconf
automake --copy --no-force
%configure \
    --disable-static \
    --enable-contrib \
    --with-quiet-nan
# patch libtool to remove rpaths
sed -i 's|^hardcode_into_libs=.*|hardcode_into_libs=no|g' libtool
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%check
# The test binaries need LD_LIBRARY_PATH to find the compiled fastbit library
# in the build tree.
%make_build LD_LIBRARY_PATH="%{buildroot}%{_libdir};%{_libdir}" check

%install
%make_install

# remove libtool archives
find %{buildroot} -name \*.la | xargs rm -f

%ldconfig_scriptlets
%ldconfig_scriptlets -n devel

%files
%doc NEWS README
%license COPYING
%{_docdir}/%{name}/*.html
%{_bindir}/ardea
%{_bindir}/fbmerge
%{_bindir}/ibis
%{_bindir}/rara
%{_bindir}/tcapi
%{_bindir}/thula
%{_bindir}/tiapi
%{_libdir}/libfastbit.so.*

%files devel
%dir %{_prefix}/include/%{name}
%{_prefix}/include/%{name}/*.{h,hh}
%{_bindir}/fastbit-config
%{_libdir}/libfastbit.so

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.3-31
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 2.0.3-24
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May 18 2021 Philip Kovacs <pkfed@fedoraproject.org> - 2.0.3-21
- Remove java bindings due to orphaned dependencies

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 09 2020 Jeff Law <law@redhat.com> - 2.0.3-19
- Fix ordered pointer comparisons against zero for gcc-11

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 2.0.3-17
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Feb 5 2020 Philip Kovacs <pkfed@fedoraproject.org> - 2.0.3-16
- Exclude arch s390x

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 11 2019 Philip Kovacs <pkfed@fedoraproject.org> - 2.0.3-14
- Rebuild for unretire
- License is BSD only

* Fri Sep 6 2019 Philip Kovacs <pkfed@fedoraproject.org> - 2.0.3-13
- Remove unnecessary build dependencies
- Improve packaging conformance

* Wed Jun 19 2019 Philip Kovacs <pkfed@fedoraproject.org> - 2.0.3-12
- Use make_build macro instead of make

* Wed Jun 19 2019 Philip Kovacs <pkfed@fedoraproject.org> - 2.0.3-11
- Replace __make macro with make

* Wed Jun 19 2019 Philip Kovacs <pkfed@fedoraproject.org> - 2.0.3-10
- Stop using autotools macros that were removed from rpm

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 25 2018 Philip Kovacs <pkfed@fedoraproject.org> - 2.0.3-7
- Add BuildRequires javapackages-tools for needed rpm macros

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 2.0.3-6
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Sat Feb 10 2018 Philip Kovacs <pkfed@fedoraproject.org> - 2.0.3-5
- Use new ldconfig_scriptlets macro.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Philip Kovacs <pkfed@fedoraproject.org> - 2.0.3-3
- Ensure linkage to pthread (for ld flag -z defs).

* Wed Dec 20 2017 Philip Kovacs <pkfed@fedoraproject.org> - 2.0.3-2
- Fix minor typos in spec.

* Tue Oct 10 2017 Philip Kovacs <pkfed@fedoraproject.org> - 2.0.3-1
- Packaging for Fedora.
