# https://bugzilla.redhat.com/show_bug.cgi?id=1676717
%undefine _ld_as_needed

%define major 3
%global svn_rev 1909

Name:           freeimage
Version:        3.19.0
Release:        0.27%{?svn_rev:.svn%svn_rev}%{?dist}
Summary:        Multi-format image decoder library

# freeimage is tripple-licensed, see
# http://freeimage.sourceforge.net/license.html
# https://lists.fedoraproject.org/pipermail/legal/2013-October/002271.html
# Automatically converted from old format: GPLv2 or GPLv3 or MPLv1.0 - review is highly recommended.
License:        GPL-2.0-only OR GPL-3.0-only OR LicenseRef-Callaway-MPLv1.0
URL:            http://freeimage.sourceforge.net/
%if 0%{?svn_rev:1}
# Visit https://sourceforge.net/p/freeimage/svn/%{svn_rev}/tarball?path=/FreeImage/trunk
Source:        freeimage-svn-r%{svn_rev}-FreeImage-trunk.zip
%else
Source:        http://downloads.sourceforge.net/%{name}/FreeImage%(echo %{version} | sed 's|\.||g').zip
%endif
# Unbundle bundled libraries
Patch0:         FreeImage_unbundle.patch
# Fix incorrect path in doxyfile
Patch1:         FreeImage_doxygen.patch
# Patch for openexr 3
Patch2:         freeimage-openexr3.patch
# Proposed fix for CVE-2021-33367
Patch4:         CVE-2021-33367.patch
# Downstream fix for CVE-2021-40266
Patch5:         CVE-2021-40266.patch
# Downstream fix for CVE-2020-24292
Patch6:         CVE-2020-24292.patch
# Downstream fix for CVE-2020-24293
Patch7:         CVE-2020-24293.patch
# Downstream fix for CVE-2020-24295
Patch8:         CVE-2020-24295.patch
# Downstream fix for CVE-2021-40263
Patch9:         CVE-2021-40263.patch
# Downstream fix for CVE-2023-47997
Patch10:        CVE-2023-47997.patch
# Downstream fix for CVE-2023-47995
Patch11:        CVE-2023-47995.patch


BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  jxrlib-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmng-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libwebp-devel
BuildRequires:  LibRaw-devel
%if 0%{?fedora} > 34
BuildRequires:  openexr-devel
BuildRequires:  imath-devel
%else
BuildRequires:  OpenEXR-devel
%endif
BuildRequires:  openjpeg2-devel

%description
FreeImage is a library for developers who would like to support popular
graphics image formats like PNG, BMP, JPEG, TIFF and others as needed by
today's multimedia applications.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        plus
Summary:        C++ wrapper for FreeImage

%description    plus
The %{name}-plus package contains the C++ wrapper library for %{name}.


%package        plus-devel
Summary:        Development files for %{name}-devel
Requires:       %{name}-plus%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    plus-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}-plus.


%prep
%if 0%{?svn_rev:1}
%setup -n freeimage-svn-r%{svn_rev}-FreeImage-trunk
%else
%setup -n FreeImage
%endif
# sanitize encodings / line endings
for file in `find . -type f -name '*.c' -or -name '*.cpp' -or -name '*.h' -or -name '*.txt' -or -name Makefile`; do
  iconv --from=ISO-8859-15 --to=UTF-8 $file > $file.new && \
  sed -i 's|\r||g' $file.new && \
  touch -r $file $file.new && mv $file.new $file
done

%autopatch -p1

# remove all included libs to make sure these don't get used during compile
rm -r Source/Lib* Source/ZLib Source/OpenEXR

# clear files which cannot be built due to dependencies on private headers
# (see also unbundle patch)
> Source/FreeImage/PluginG3.cpp
> Source/FreeImageToolkit/JPEGTransform.cpp


%build
sh ./gensrclist.sh
sh ./genfipsrclist.sh
%ifarch %{power64} %{mips32} aarch64
%make_build -f Makefile.gnu CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC" LDFLAGS="%{__global_ldflags}"
%make_build -f Makefile.fip CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC" LDFLAGS="%{__global_ldflags}"
%else
%make_build -f Makefile.gnu CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" LDFLAGS="%{__global_ldflags}"
%make_build -f Makefile.fip CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" LDFLAGS="%{__global_ldflags}"
%endif

pushd Wrapper/FreeImagePlus/doc
doxygen FreeImagePlus.dox
popd


%install
install -Dpm 755 Dist/lib%{name}-%{version}.so %{buildroot}%{_libdir}/lib%{name}-%{version}.so
ln -s lib%{name}-%{version}.so %{buildroot}%{_libdir}/lib%{name}.so

install -Dpm 755 Dist/lib%{name}plus-%{version}.so %{buildroot}%{_libdir}/lib%{name}plus-%{version}.so
ln -s lib%{name}plus-%{version}.so %{buildroot}%{_libdir}/lib%{name}plus.so

install -Dpm 644 Source/FreeImage.h %{buildroot}%{_includedir}/FreeImage.h
install -Dpm 644 Wrapper/FreeImagePlus/FreeImagePlus.h %{buildroot}%{_includedir}/FreeImagePlus.h

# install missing symlink (was giving no-ldconfig-symlink rpmlint errors)
ldconfig -n %{buildroot}%{_libdir}


%files
%license license-*.txt
%doc Whatsnew.txt
%{_libdir}/lib%{name}-%{version}.so
%{_libdir}/lib%{name}.so.%major

%files devel
%doc Examples
%{_includedir}/FreeImage.h
%{_libdir}/lib%{name}.so

%files plus
%doc Wrapper/FreeImagePlus/WhatsNew_FIP.txt
%{_libdir}/lib%{name}plus-%{version}.so
%{_libdir}/lib%{name}plus.so.%major

%files plus-devel
%doc Wrapper/FreeImagePlus/html
%{_includedir}/FreeImagePlus.h
%{_libdir}/lib%{name}plus.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.0-0.27.svn1909
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 3.19.0-0.26.svn1909
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.0-0.25.svn1909
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Apr 24 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 3.19.0-0.24.svn1909
- Rebuilt for openexr 3.2.4

* Sun Mar 10 2024 Sandro Mani <manisandro@gmail.com> - 3.19.0-0.23.svn1909
- Add downstream patches for CVE-2023-47997, CVE-2023-47995

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.0-0.22.svn1909
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.0-0.21.svn1909
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Sep 28 2023 Sandro Mani <manisandro@gmail.com> - 3.19.0-0.20.svn1909
- Downstream fixes for CVE-2021-40266 CVE-2020-24292 CVE-2020-24293 CVE-2020-24295 CVE-2021-40263

* Mon Aug 28 2023 Sandro Mani <manisandro@gmail.com> - 3.19.0-0.19.svn1909
- Update to svn rev 1909

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.0-0.18.svn1889
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 26 2023 Sandro Mani <manisandro@gmail.com> - 3.19.0-0.17.svn1889
- Bump for Release parity with f37

* Thu Apr 13 2023 Sandro Mani <manisandro@gmail.com> - 3.19.0-0.16.svn1889
- Fix empty CVE-2021-33367.patch

* Thu Apr 13 2023 Sandro Mani <manisandro@gmail.com> - 3.19.0-0.15.svn1889
- Add proposed fix for CVE-2021-33367

* Thu Apr 06 2023 Sandro Mani <manisandro@gmail.com> - 3.19.0-0.14.svn1889
- Syncronize FreeImage_unbundle.patch with mingw-freeimage

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.0-0.13.svn1889
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 20 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.19.0-0.12.svn1889
- LibRaw rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.0-0.11.svn1889
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 23 2022 Sandro Mani <manisandro@gmail.com> - 3.19.0-0.10.svn1889
- Add patch for libtiff-4.4.0 comptability

* Fri May 20 2022 Sandro Mani <manisandro@gmail.com> - 3.19.0-0.9.svn1889
- Rebuild for gdal-3.5.0 and/or openjpeg-2.5.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.0-0.8.svn1889
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 21 2021 Richard Shaw <hobbes1069@gmail.com> - 3.19.0-0.7.svn1889
- Rebuild for OpenEXR/Imath 3.1.

* Thu Aug 19 2021 Sandro Mani <manisandro@gmail.com> - 3.19.0-0.6.svn1889
- Update to svn rev 1889

* Mon Aug 02 2021 Richard Shaw <hobbes1069@gmail.com> - 3.19.0-0.5.svn1859
- Update for OpenEXR/Imath 3.

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.0-0.4.svn1859
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.0-0.3.svn1859
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 01 2021 Richard Shaw <hobbes1069@gmail.com> - 3.19.0-0.2.svn1859
- Rebuild for OpenEXR 2.5.3.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.18.0-8
- Rebuild for new LibRaw

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 17 2019 Sandro Mani <manisandro@gmail.com> - 3.18.0-6
- Backport fixes for CVE-2019-12211 and 2019-12213

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 10 2019 Richard Shaw <hobbes1069@gmail.com> - 3.18.0-4
- Rebuild for OpenEXR 2.3.0.

* Wed Feb 13 2019 Sandro Mani <manisandro@gmail.com> - 3.18.0-3
- Disable --Wl,--as-needed (#1676717)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Sandro Mani <manisandro@gmail.com> - 3.18.0-1
- Update to 3.18.0

* Thu Jul 19 2018 Adam Williamson <awilliam@redhat.com> - 3.17.0-16
- Rebuild for new libraw
- fPIC for aarch64 also

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Sandro Mani <manisandro@gmail.coM> - 3.17.0-14
- Add missing BR: gcc-c++, make

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Sandro Mani <manisandro@gmail.com> - 3.17.0-9
- Rebuild (libwebp)

* Tue Dec 27 2016 Jon Ciesla <limburgher@gmail.com> - 3.17.0-8
- Rebuild for new LibRaw.

* Tue Oct 04 2016 Sandro Mani <manisandro@gmail.com> - 3.17.0-7
- Fix CVE-2016-5684 (rhbz#1381517)

* Fri Aug 12 2016 Michal Toman <mtoman@fedoraproject.org> - 3.17.0-6
- -fPIC on 32-bit MIPS

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 28 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 3.17.0-4
- Rebuilt for libwebp soname bump

* Thu Oct 15 2015 Karsten Hopp <karsten@redhat.com> 3.17.0-3
- ppc64 and ppc64le need -fPIC (rhbz#1272048)

* Wed Sep 30 2015 Sandro Mani <manisandro@gmail.com> - 3.17.0-2
- Fix under-linked library

* Thu Sep 17 2015 Sandro Mani <manisandro@gmail.com> - 3.17.0-1
- Update to 3.17.0
- Add fix for CVE-2015-0852 (#1257859)
- Put freeimage-plus in separate package

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.10.0-24
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 3.10.0-23
- rebuild (gcc5)

* Wed Nov 26 2014 Rex Dieter <rdieter@fedoraproject.org> 3.10.0-22
- rebuild (openexr), tighten subpkg deps via %%{?_isa}

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 27 2013 Rex Dieter <rdieter@fedoraproject.org> - 3.10.0-19
- rebuild (openexr)

* Mon Sep 09 2013 Bruno Wolff III <bruno@wolff.to> 3.10.0-18
- Rebuild for ilmbase related soname bumps

* Mon Aug 26 2013 Jon Ciesla <limburgher@gmail.com> - 3.10.0-17
- libmng rebuild.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 10 2013 Rex Dieter <rdieter@fedoraproject.org> - 3.10.0-15
- rebuild (OpenEXR)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 3.10.0-13
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 3.10.0-12
- rebuild against new libjpeg

* Fri Aug  3 2012 Tom Lane <tgl@redhat.com> 3.10.0-11
- Add patch for libtiff 4.0 API changes
Resolves: #845407

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 13 2012 Bruno Wolff III <bruno@wolff.to> 3.10.0-9
- Update for libpng 1.5 API

* Thu Feb 09 2012 Rex Dieter <rdieter@fedoraproject.org> 3.10.0-8
- rebuild (openjpeg)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 3.10.0-6
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 12 2011 Rex Dieter <rdieter@fedoraproject.org> - 3.10.0-4
- rebuild (openjpeg)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Mar 18 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 3.10.0-1
- Initial Fedora package
