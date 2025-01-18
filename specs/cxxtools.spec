Name:           cxxtools
Version:        3.0
Release:        14%{?dist}
Summary:        A collection of general-purpose C++ classes
Epoch:          1

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+ 
URL:            http://www.tntnet.org/cxxtools.html
Source0:        https://github.com/maekitalo/cxxtools/archive/refs/tags/V%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         %{name}-%{version}-arm.patch
Patch1:         %{name}-%{version}-gcc11.patch
Patch2:         %{name}-%{version}-i686.patch
Patch3:         %{name}-%{version}-ppc64le.patch
# fix error: aggregate 'tm tim' has incomplete type and cannot be defined
Patch4:         %{name}-%{version}-timer.patch

BuildRequires:  make
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
Provides:       bundled(md5-polstra)

%description
%{summary}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description    devel
Development files for %{name}


%prep
%autosetup -p0 -n %{name}-%{version}

# fix spurious executable perm
find -name "*.cpp" -exec chmod -x {} \;
find -name "*.h" -exec chmod -x {} \;

%build
# configure tests try to compile code containing ASMs to a .o file
# In an LTO world, that always works as compilation does not happen until
# link time.  As a result we get the wrong results from configure.
# This can be fixed by using -ffat-lto-objects
# -ffat-lto-objects forces compilation even with LTO.  It is the default
# for F33, but not expected to be enabled by default for F34
%define _lto_cflags -flto=auto -ffat-lto-objects

#aclocal && automake
%configure --disable-static \
%ifarch s390 s390x aarch64
    --with-atomictype=pthread \
%endif
    %{nil}
%make_build

%install
%make_install

# Find and remove all la files
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

#%%check
#    test/alltests

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/libcxxtools*.so.*

%files devel
%{_bindir}/cxxtools-config
%{_bindir}/cxxtz
%{_bindir}/siconvert
%{_libdir}/libcxxtools*.so
%{_libdir}/pkgconfig/%{name}-*.pc
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/cxxtools/

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1:3.0-13
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 30 2024 Martin Gansser <martinkg@fedoraproject.org> - 1:3.0-11
- Rebuilt disable test suite

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 03 2022 Martin Gansser <martinkg@fedoraproject.org> - 1:3.0-6
- Add %%{name}-%%{version}-timer.patch to fix (BZ#2113165)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1:3.0-3
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 01 2021 Martin Gansser <martinkg@fedoraproject.org> - 1:3.0-1
- Update to 1:3.0-1
- Add BR openssl-devel
- Add %%{name}-%%{version}-gcc11.patch
- Add %%{name}-%%{version}-i686.patch
- Add %%{name}-%%{version}-ppc64le.patch

* Sun Jan 31 2021 Martin Gansser <martinkg@fedoraproject.org> - 1:2.2.1-26
- Add modified %%{name}-%%{version}-gcc11.patch now C++17 ready
 
* Fri Jan 29 2021 Martin Gansser <martinkg@fedoraproject.org> - 1:2.2.1-25
- Add %%{name}-%%{version}-gcc11.patch
- Add CXXFLAGS "-std=gnu++14 -fPIE" as this code is not C++17 ready

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 21 2020 Jeff Law <law@redhat.com> - 1:2.2.1-23
- Re-enable LTO

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Jeff Law <law@redhat.com> - 1:2.2.1-21
- Disable LTO

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 21 2018 Martin Gansser <martinkg@fedoraproject.org> - 1:2.2.1-17
- Fix FTBFS due missing BR gcc gcc-c++ (RHBZ#1603733)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Apr 29 2016 Than Ngo <than@redhat.com> - 2:2.2.1-11
- backport upstream patch to fix the rounding errors on ppc
- cleanup specfile

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 09 2015 Martin Gansser <martinkg@fedoraproject.org> - 2.2.1-9
- Rebuilt

* Thu Sep 24 2015 Martin Gansser <martinkg@fedoraproject.org> - 2.2.1-8
- Rebuilt
- added epoch to allow upgrade to older release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.2.1-6
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 baude <baude@us.ibm.com> - 2.2.1-3
- Moving removal of .las from check to install section 

* Mon Feb 17 2014 Martin Gansser <martinkg@fedoraproject.org> - 2.2.1-2
- fix build on aarch64 where atomicity detection fails

* Mon Jan 20 2014 Martin Gansser <martinkg@fedoraproject.org> - 2.2.1-1
- new release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 3 2013 Martin Gansser <martinkg@fedoraproject.org> - 2.2-1
- new release
- spec file cleanup

* Fri Sep 21 2012 Jon Ciesla <limburgher@gmail.com> - 2.1.1-5
- Fix FTBFS on ARM.

* Thu Jul 26 2012 Dan Horák <dan[at]danny.cz> - 2.1.1-4
- fix build on s390(x) where atomicity detection fails

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 28 2012 Martin Gansser <linux4martin@gmx.de> - 2.1.1-2
- added Provides: bundled(md5-polstra)

* Sat May 26 2012 Martin Gansser <linux4martin@gmx.de> - 2.1.1-1
- rebuild for new release
- fixed url
- removed empty files from doc
- fixed Requires for devel package
- added group tag for main package
- added unit test

* Sun Apr 29 2012 Martin Gansser <linux4martin@gmx.de> - 2.1-1
- new release
- removed license comment

* Mon Sep 19 2011 Sebastian Vahl <fedora@deadbabylon.de> - 2.0-2
- split into -devel subpkg

* Sun Sep 18 2011 Sebastian Vahl <fedora@deadbabylon.de> - 2.0-1
- initial release

