Name:           FreeSOLID
Version:        2.1.1
Release:        51%{?dist}
Summary:        3D collision detection C++ library
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://sourceforge.net/projects/freesolid/
Source0:        http://sourceforge.net/projects/freesolid/files/FreeSOLID/FreeSOLID-2.1.1.zip/FreeSOLID-2.1.1.zip
# https://sourceforge.net/tracker/?func=detail&aid=3484912&group_id=65180&atid=510061
Patch0:         %{name}-%{version}-src.patch
# https://sourceforge.net/tracker/?func=detail&aid=3484910&group_id=65180&atid=510061
Patch1:         %{name}-%{version}-headers.patch
# https://sourceforge.net/tracker/?func=detail&aid=3484908&group_id=65180&atid=510061
Patch2:         %{name}-%{version}-endpoint.patch
# https://sourceforge.net/tracker/?func=detail&aid=3484907&group_id=65180&atid=510061
Patch3:         %{name}-%{version}-autotools.patch
# https://sourceforge.net/tracker/?func=detail&aid=3484909&group_id=65180&atid=510061
Patch4:         %{name}-%{version}-fsf-fix.patch
# https://sourceforge.net/tracker/?func=detail&aid=3484911&group_id=65180&atid=510061
Patch5:         %{name}-%{version}-pkgconfig.patch
# https://sourceforge.net/tracker/?func=detail&aid=3509457&group_id=65180&atid=510059
Patch6:         %{name}-%{version}-configure.patch
Patch7:         %{name}-%{version}-freesolid-config.patch
Patch8:         %{name}-%{version}-Makefile.am-update.patch

BuildRequires:  gcc-c++
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  SDL-devel
BuildRequires:  qhull-devel
BuildRequires:  make


%description
FreeSOLID is a library for collision detection of three-dimensional
objects undergoing rigid motion and deformation. FreeSOLID is designed
to be used in interactive 3D graphics applications.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       qhull-devel

%description    devel
Libraries and header files for developing applications that use %{name}.


%prep
%setup -q -n FreeSOLID-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
#%%patch6 -p1
%patch -P7 -p1
%patch -P8 -p1
mv configure.in configure.ac
autoupdate

%if 0%{?fedora} > 24
# check for libqhull/qhull_a.h instead of qhull/qhull_a.h
sed -i -e 's,qhull/qhull_a.h,libqhull/qhull_a.h,' configure*
%endif

mkdir m4
rm acinclude.m4 aclocal.m4
rm ltmain.sh missing depcomp install-sh config.*
chmod 755 configure


%build
autoreconf -fvi
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
rm $( find %{buildroot} -name '*.la' ) %{buildroot}%{_infodir}/dir
rm -rf sample/*.o sample/.libs $(find sample -type f -a -executable)


%files
%doc README TODO
%license COPYING COPYING.LIB
%{_libdir}/*.so.*

%files devel
%doc sample
%{_infodir}/*
%{_bindir}/freesolid-config
%{_libdir}/*.so
%{_libdir}/pkgconfig/FreeSOLID.pc
%{_includedir}/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.1-50
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 10 2023 Tom Callaway <spot@fedoraproject.org> - 2.1.1-45
- rebuild for new qhull

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Apr 14 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.1.1-39
- Fix FTBFS (BZ#1943075) with Autoconf 2.71

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 10 2020 Martin Gansser <martinkg@fedoraproject.org> - 2.1.1-36
- Remove Requires: qhull from FreeSOLID.pc.in
- Rebuilt

* Fri Feb 07 2020 Martin Gansser <martinkg@fedoraproject.org> - 2.1.1-35
- Rebuilt

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 03 2018 Martin Gansser <martinkg@fedoraproject.org> - 2.1.1-30
- Remove Requires: qhull from FreeSOLID.pc.in
- Add RR qhull-devel to devel package

* Mon Feb 19 2018 Martin Gansser <martinkg@fedoraproject.org> - 2.1.1-29
- rebuilt for rawhide

* Fri Feb 09 2018 Filipe Rosset <rosset.filipe@gmail.com> - 2.1.1-28
- rebuilt for rawhide

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Apr 29 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.1.1-23
- Rebuild for qhull-2015.2-1.
- Reflect qhull_a.h's location having changed.
- Add %%license.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.1.1-20
- Rebuilt for GCC 5 C++11 ABI change

* Fri Feb 13 2015 Martin Gansser <martinkg@fedoraproject.org> 2.1.1-19
- Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 22 2013 Ralf Corsépius - 2.1.1-15
- Remove m4/.gitkeep from FreeSOLID-2.1.1-autotools.patch 
  (Fix Fedora_19_Mass_Rebuild FTBFS).

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012  Martin Gansser <linux4martin@gmx.de> 2.1.1-13
- Rebuild
- enabled pkg-config to use qhull-devel package
* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Tue Jul 10 2012  Martin Gansser <linux4martin@gmx.de> 2.1.1-11
- update added correct freesolid.config.patch
- added Makefile.am patch
- reverted fsf-fix patch
* Mon Jul 9 2012  Martin Gansser <linux4martin@gmx.de> 2.1.1-10
- updated fsf-fix patch
* Mon Jul 9 2012  Martin Gansser <linux4martin@gmx.de> 2.1.1-9
- added multilib wrapper script free-solid-config to use pkg-config
- updated FreeSOLID pkgconfig patch
- updated spec file
* Fri Jun 22 2012  Martin Gansser <linux4martin@gmx.de> 2.1.1-8
- added configure patch
- rebuild for Fedora 17
* Wed Mar 21 2012  Martin Gansser <linux4martin@gmx.de> 2.1.1-7
- moved ldconfig to the base package
* Wed Mar 21 2012  Martin Gansser <linux4martin@gmx.de> 2.1.1-6
- changed free-sold.pc -> FreeSOLID.pc
- renamed post section to post devel for solid2.info file
- renamed prerun section to preun devel for solid2.info file
* Tue Mar 20 2012  Martin Gansser <linux4martin@gmx.de> 2.1.1-5
- changed the package name.
- Added configure patch solves incompatibilities with libtool-2.
* Tue Feb 7 2012  Martin Gansser <linux4martin@gmx.de> 2.1.1-4
- Cleaned up samples, port of devel package docs.
* Tue Feb 7 2012  Martin Gansser <linux4martin@gmx.de> 2.1.1-3
- Fixed License type.
* Mon Feb 6 2012  Martin Gansser <linux4martin@gmx.de> 2.1.1-2
- Fixed Source URL.
- Review fix: pkgconfig dep, devel package ?_isa dep, macros.
* Sun Feb 5 2012  Martin Gansser <linux4martin@gmx.de> 2.1.1-1
- Initial package
