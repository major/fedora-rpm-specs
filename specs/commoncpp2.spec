Name:          commoncpp2
Version:       1.8.1
Release:       34%{?dist}
Summary:       GNU Common C++ class framework

# Library is GPLv2+ with exceptions
# Automatically converted from old format: GPLv2+ with exceptions - review is highly recommended.
License:       LicenseRef-Callaway-GPLv2+-with-exceptions
URL:           http://www.gnu.org/software/commoncpp/
Source0:       https://ftp.gnu.org/gnu/commoncpp/%{name}-%{version}.tar.gz

# Fix mkfifo modes: S_IREAD | S_IWRITE -> S_IRUSR | S_IWUSR
Patch1:        commoncpp2-statfix.patch
# Fix build against GCC9+
Patch2:        commoncpp2-gcc9.patch
# Fix two occurences of incorrect sizeof usage
Patch3:        commoncpp2_sizeof.patch
# Replace obsolete macros
Patch4:        commoncpp2_obsoletem4.patch
# Call setgroups before setuid
Patch5:        commoncpp2_setgroups.patch
# Disable thread1 test which is badly written and hangs (or takes a very long time)
# Add return code to detect failure/success
Patch6:        commoncpp2_tests.patch

BuildRequires: automake autoconf libtool
BuildRequires: doxygen
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libxml2-devel
BuildRequires: zlib-devel
BuildRequires: make


%description
GNU Common C++ is a portable and highly optimized class framework for writing
C++ applications that need to use threads, sockets, XML parsing,
serialization, config files, etc. This framework offers a class foundation
that hides platform differences from your C++ application so that you need
not write platform specific code. GNU Common C++ has been ported to compile
natively on most platforms which support posix threads.


%package devel
Summary:       Header files and libraries for %{name} development
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      libxml2-devel%{?_isa}
Requires:      zlib-devel%{?_isa}

%description devel
The %{name}-devel package contains the header files and libraries needed
to develop programs that use the %{name} library.


%package doc
Summary:       Developer documentation for %{name}
# Automatically converted from old format: GPLv2+ with exceptions and GFDL - review is highly recommended.
License:       LicenseRef-Callaway-GPLv2+-with-exceptions AND LicenseRef-Callaway-GFDL
BuildArch:     noarch

%description doc
The %{name}-doc package contains the developer documentation for %{name}.


%prep
%autosetup -p1


%build
# Kill rpath
autoreconf -ifv
%configure \
    --disable-static \
    --disable-dependency-tracking

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

# Parallel build occasionally broken
make CXX="g++ -std=c++14"

# Build tests
pushd tests
%make_build CXX="g++ -std=c++14"
popd


%install
%make_install
find %{buildroot} -name '*.la' -delete

# Drop info index
rm -f %{buildroot}%{_infodir}/dir

%check
pushd tests
LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./test.sh
popd


%files
%doc README ChangeLog
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_bindir}/ccgnu2-config
%{_includedir}/cc++/
%{_libdir}/*.so
%{_libdir}/pkgconfig/libccext2.pc
%{_libdir}/pkgconfig/libccgnu2.pc
%{_datadir}/aclocal/ost_check2.m4

%files doc
%doc doc/html
%{_infodir}/commoncpp2.info*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.8.1-33
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Jeff Law <law@redhat.com> - 1.8.1-23
- Force C++14 as the code is not C++17 ready

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 Sandro Mani <manisandro@gmail.com> - 1.8.1-21
- Actually add files to %%doc
- Only list GFDL license for %%doc subpackage
- Drop badly written thread1 test, enable remaining tests

* Tue Feb 04 2020 Sandro Mani <manisandro@gmail.com> - 1.8.1-20
- Split off documentation
- Clarify license
- Drop ldconfig_scriptlets
- Add %%{?_isa} to Requires
- Patch another incorrect sizeof usage
- Build tests, add %%check (disabled with comment though)
- Patch setuid not preceded by setgroups call
- Fix unused direct dependencies
- Fix obsolete m4 macros

* Wed Jan 29 2020 Sandro Mani <manisandro@gmail.com> - 1.8.1-19
- Revived package

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.8.1-16
- Rebuild with fixed binutils

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.8.1-8
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-2
- Rebuilt for c++ ABI breakage

* Sun Jan 22 2012 Kevin Fenzi <kevin@scrye.com> - 1.8.1-1
- Update to 1.8.1

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 06 2009 Andreas Thienemann <andreas@bawue.net> - 1.7.3-1
- Updated to new upstream version 1.7.3

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 15 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.6.1-2
- fix license tag

* Wed Feb 06 2008 Andreas Thienemann <andreas@bawue.net> - 1.6.1-1
- Updated to new upstream version 1.6.1
- Reverted the ld-check patch as it's no longer needed

* Fri Nov 10 2006 Andreas Thienemann <andreas@bawue.net> - 1.5.0-1
- Updated package to 1.5.0

* Sun May 28 2006 Andreas Thienemann <andreas@bawue.net> - 1.4.2-1
- Updated to 1.4.2

* Sun May 28 2006 Andreas Thienemann <andreas@bawue.net> - 1.4.1-1
- Updated to 1.4.1

* Sun Feb 05 2006 Andreas Thienemann <andreas@bawue.net> - 1.3.23-1
- Incorporated suggestions for extras

* Fri Feb 03 2006 Andreas Thienemann <andreas@bawue.net> - 1.3.22-1
- Initial spec.
