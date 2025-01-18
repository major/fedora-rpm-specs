# NVIDIA Cg toolkit is not free
%define with_Cg         0
%if %with_Cg
%define real_name       OpenEXR_Viewers-nonfree
%define V_suffix        -nonfree
%define priority        10
%else
%define real_name       OpenEXR_Viewers
%define V_suffix        -fedora
%define priority        5
%endif

%global project openexr

Name:           %{real_name}
Version:        2.3.0
Release:        18%{?dist}
Summary:        Viewers programs for OpenEXR

# Automatically converted from old format: AMPAS BSD - review is highly recommended.
License:        AMPAS
URL:            http://www.openexr.com
Source0: https://github.com/%{project}/%{project}/releases/download/v%{version}/OpenEXR_Viewers-%{version}.tar.gz

Patch1: openexr_viewers-2.0.1-dso.patch
Patch2: openexr_viewers-gcc-11-fixes.patch
Patch3: openexr_viewers-imfheader.patch

BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  gcc-c++

BuildRequires:  fltk-devel >= 1.1
BuildRequires:  pkgconfig(OpenEXR) >= 2.1
%if %with_Cg
BuildRequires:  Cg
BuildRequires:  freeglut-devel
Provides: OpenEXR_Viewers = %{version}
%else
BuildConflicts:  Cg
%endif

%if 0%{?openexr_ctl}
BuildRequires:  pkgconfig(OpenEXR_CTL)
BuildRequires:  OpenEXR_CTL
Requires:  OpenEXR_CTL%{?_isa}
%endif
Requires(post): /usr/sbin/alternatives
Requires(preun): /usr/sbin/alternatives


%description
exrdisplay is a simple still image viewer that optionally applies color
transforms to OpenEXR images, using ctl as explained in this document:
doc/OpenEXRViewers.pdf

%if %with_Cg
playexr is a program that plays back OpenEXR image sequences, optionally
with CTL support, applying rendering and display transforms in line with
the current discussions at the AMPAS Image Interchange Framework committee
(September 2006).

This is the nonfree version compiled with NVIDIA Cg support
See: https://developer.nvidia.com/cg-toolkit
%else

%package docs
Summary:        Documentation for %{name}

%description docs
This package contains documentation files for %{name}.
%endif

%prep
%setup -q -n openexr_viewers-%{version}

%patch -P1 -p1 -b .dso
%patch -P2 -p1 -b .gcc11
%patch -P3 -p1 -b .imfh

%if "%{_lib}" == "lib64"
sed -i -e 's|ACTUAL_PREFIX/lib/CTL|ACTUAL_PREFIX/lib64/CTL|' configure.ac
%endif
#Needed for patch1 and to update CTL compiler test
#autoconf
./bootstrap
sed -i -e 's|#include <vector>\n    using namespace Ctl|#include <vector>\n    #include <cstdlib>\nusing namespace Ctl|' configure


%build
export CXXFLAGS="$RPM_OPT_FLAGS -L%{_libdir}"
%configure  --disable-static \
  --disable-openexrtest \
  --disable-openexrctltest \
%if %with_Cg
  --with-cg-prefix=%{_prefix}
%endif

# Missing libs for playexr
sed -i -e 's|LIBS =|LIBS = -lglut|' playexr/Makefile

%make_build


%install
%make_install

# Remove the config.h - uneeded afaik
rm -rf $RPM_BUILD_ROOT%{_includedir}

# move the binary
mv $RPM_BUILD_ROOT%{_bindir}/exrdisplay $RPM_BUILD_ROOT%{_bindir}/exrdisplay%{V_suffix}

# Removing installed docs
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc

# Owernship of the alternative provides
touch $RPM_BUILD_ROOT%{_bindir}/exrdisplay

%post
alternatives --install %{_bindir}/exrdisplay exrdisplay %{_bindir}/exrdisplay%{V_suffix} %{priority} ||:


%preun
if [ $1 -eq 0 ]; then
  alternatives --remove exrdisplay %{_bindir}/exrdisplay%{V_suffix} || :
fi

%files
%doc ChangeLog README.md
%license LICENSE
%ghost %{_bindir}/exrdisplay
%{_bindir}/exrdisplay%{V_suffix}
%if %with_Cg
%{_bindir}/playexr
%else

%files docs
%doc doc/OpenEXRViewers.odt doc/OpenEXRViewers.pdf
%endif

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 2.3.0-17
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Apr 24 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.3.0-15
- Rebuilt for openexr 3.2.4

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 03 2022 Nicolas Chauvet <kwizart@gmail.com> - 2.3.0-8
- Fix FTBFS

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 02 2020 Björn Esser <besser82@fedoraproject.org> - 2.3.0-4
- Fix string quoting for rpm >= 4.16

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 02 2019 Richard Shaw <hobbes1069@gmail.com> - 2.3.0-1
- Update to 2.3.0.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 01 2018 Nicolas Chauvet <kwizart@gmail.com> - 2.2.1-1
- Update to 2.2.1

* Thu Jul 19 2018 Nicolas Chauvet <kwizart@gmail.com> - 2.2.0-11
- Spec clean-up
- Enable CTL with 1.5.2 update

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.2.0-3
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 2.2.0-2
- rebuild (fltk)

* Tue Nov 25 2014 Rex Dieter <rdieter@fedoraproject.org> 2.2.0-1
- 2.2.0

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 27 2013 Rex Dieter <rdieter@fedoraproject.org> 2.1.0-1
- 2.1.0

* Fri Oct 11 2013 Rex Dieter <rdieter@fedoraproject.org> 2.0.1-3
- OpenEXR_Viewers FTBFS: ImplicitDSO Linking issues (#1017880)

* Thu Oct 10 2013 Rex Dieter <rdieter@fedoraproject.org> 2.0.1-2
- make OpenEXR_CTL support optional (since it doesn't support openexr-2.x yet)

* Sat Oct 05 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.0.1-1
- Update to 2.0.1

* Sat Sep 14 2013 Bruno Wolff III <bruno@wolff.to> - 1.0.2-13
- Rebuild for ilmbase related soname bumps

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 11 2013 Rex Dieter <rdieter@fedoraproject.org> - 1.0.2-11
- rebuild (OpenEXR)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-8
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 24 2011 Rex Dieter <rdieter@fedoraproject.org> 1.0.2-6
- FTBFS OpenEXR_Viewers-1.0.2-3.fc15: ImplicitDSOLinking (#716011)

* Fri May 27 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.0.2-5
- Update gcc44 patch
- Rebuild for new fltk
- Drop old Obsoletes OpenEXR-utils < 1.6.0

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Sep 05 2010 Nicolas Chauvet <kwizart@gmail.com> - 1.0.2-2
- Fix CTL Module search path on lib64
- Fix OpenEXR_CTL detection at build time.

* Mon Aug 23 2010 Nicolas Chauvet <kwizart@gmail.com> - 1.0.2-1
- Update to 1.0.2

* Tue Oct 20 2009 kwizart < kwizart at gmail.com > - 1.0.1-7
- Rebuild for F-12

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 12 2009 kwizart < kwizart at gmail.com > - 1.0.1-4
- Rebuild for gcc44

* Fri Oct 17 2008 kwizart < kwizart at gmail.com > - 1.0.1-3
- Rebuild for F-10

* Sat May 10 2008 kwizart < kwizart at gmail.com > - 1.0.1-2
- Ghost the alternative provides
- Obsoletes OpenEXR-utils

* Wed Jan  9 2008 kwizart < kwizart at gmail.com > - 1.0.1-1
- Initial package for Fedora

