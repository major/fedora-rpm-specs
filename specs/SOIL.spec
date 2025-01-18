Name:           SOIL
Version:        1.07
Release:        39.20080706%{?dist}
Summary:        Simple OpenGL Image Library

# src/image_helper.{c,h} are MIT-licensed
# Automatically converted from old format: Public Domain and MIT - review is highly recommended.
License:        LicenseRef-Callaway-Public-Domain AND LicenseRef-Callaway-MIT
URL:            http://www.lonesock.net/soil.html
Source0:        http://www.lonesock.net/files/soil.zip
Patch0:         %{name}-link-correctly.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  libGL-devel

%description
SOIL is a tiny C library used primarily for uploading textures into OpenGL. It
is based on stb_image version 1.16, the public domain code from Sean Barrett.
The author has extended it to load TGA and DDS files, and to perform common
functions needed in loading OpenGL textures. SOIL can also be used to save and
load images in a variety of formats (useful for loading height maps, non-OpenGL
applications, etc.)

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -qc
# workaround for RH bug #912831
mv Simple\ OpenGL\ Image\ Library/* .
rmdir Simple\ OpenGL\ Image\ Library
%patch -P0 -p1 -b .link-correctly


%build
pushd src
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -c -fPIC" \
    -f ../projects/makefile/alternate\ Makefile.txt
popd


%install
rm -rf $RPM_BUILD_ROOT
pushd src
make -f ../projects/makefile/alternate\ Makefile.txt install \
    DESTDIR=$RPM_BUILD_ROOT LIBDIR=%{_libdir} INCLUDEDIR=%{_includedir}/%{name} \
    INSTALL_FILE="install -pm 644" INSTALL_DIR="install -dp"
popd
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# kill the static library
rm -rf $RPM_BUILD_ROOT%{_libdir}/lib%{name}.a

# fix the library permissions
chmod 755 $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so.1.07-20071110

%ldconfig_scriptlets

%files
%doc soil.html
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-39.20080706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.07-38.20080706
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-37.20080706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-36.20080706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-35.20080706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-34.20080706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-33.20080706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-32.20080706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-31.20080706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-30.20080706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-29.20080706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-28.20080706
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-27.20080706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-26.20080706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-25.20080706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-24.20080706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 15 2018 Julian Sikorski <belegdol@fedoraproject.org> - 1.07-23.20080706
- Added gcc to BuildRequires as per https://fedoraproject.org/wiki/Packaging:C_and_C%2B%2B#BuildRequires_and_Requires

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-22.20080706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 04 2018 Julian Sikorski <belegdol@fedoraproject.org> - 1.07-21.20080706
- Removed ldconfig scriptlets as per
  https://fedoraproject.org/wiki/Changes/Removing_ldconfig_scriptlets

* Mon May 14 2018 Julian Sikorski <belegdol@fedoraproject.org> - 1.07-20.20080706
- Fixed typo in License field (RH #1577464)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-19.20080706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-18.20080706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-17.20080706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-16.20080706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-15.20080706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-14.20080706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-13.20080706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-12.20080706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-11.20080706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 19 2013 Julian Sikorski <belegdol@fedoraproject.org> - 1.07-10.20080706
- Reintroduced the move-one-folder-up workaround - spaces in path still cause
  problems (Red Hat bug #912831)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-9.20080706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 16 2013 Julian Sikorski <belegdol@fedoraproject.org> - 1.07-8.20080706
- Dropped the RPM workaround

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-7.20080706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-6.20080706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jan 12 2012 Julian Sikorski <belegdol@fedoraproject.org> - 1.07-5.20080706
- Fixed the License tag

* Wed Jan 11 2012 Julian Sikorski <belegdol@fedoraproject.org> - 1.07-4.20080706
- Use variables instead of sed to fix the makefile

* Fri Dec 23 2011 Julian Sikorski <belegdol@fedoraproject.org> - 1.07-3.20080706
- Ported a Debian patch ensuring the correct linking

* Thu Dec 22 2011 Julian Sikorski <belegdol@fedoraproject.org> - 1.07-2.20080706
- Renamed to SOIL

* Wed Nov 30 2011 Julian Sikorski <belegdol@fedoraproject.org> - 1.07-1.20080706
- Initial RPM release based on Debian package

