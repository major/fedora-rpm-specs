Name:           kicad
Version:        8.0.8
Release:        2%{?dist}
Epoch:          1
Summary:        EDA software suite for creation of schematic diagrams and PCBs

License:        GPL-3.0-or-later
URL:            https://www.kicad.org

Source0:        https://gitlab.com/kicad/code/kicad/-/archive/%{version}/kicad-%{version}.tar.gz
Source1:        https://gitlab.com/kicad/services/kicad-doc/-/archive/%{version}/kicad-doc-%{version}.tar.gz
Source2:        https://gitlab.com/kicad/libraries/kicad-templates/-/archive/%{version}/kicad-templates-%{version}.tar.gz
Source3:        https://gitlab.com/kicad/libraries/kicad-symbols/-/archive/%{version}/kicad-symbols-%{version}.tar.gz
Source4:        https://gitlab.com/kicad/libraries/kicad-footprints/-/archive/%{version}/kicad-footprints-%{version}.tar.gz
Source5:        https://gitlab.com/kicad/libraries/kicad-packages3D/-/archive/%{version}/kicad-packages3D-%{version}.tar.gz

# https://gitlab.com/kicad/code/kicad/-/issues/237
ExclusiveArch:  x86_64 aarch64 ppc64le

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  glew-devel
BuildRequires:  glm-devel
BuildRequires:  gtk3-devel
BuildRequires:  libappstream-glib
BuildRequires:  libcurl-devel
BuildRequires:  libgit2-devel
BuildRequires:  libngspice-devel
BuildRequires:  libsecret-devel
BuildRequires:  make
BuildRequires:  opencascade-devel
BuildRequires:  python3-devel
BuildRequires:  python3-wxpython4
BuildRequires:  shared-mime-info
BuildRequires:  swig
BuildRequires:  unixODBC-devel
BuildRequires:  wxGTK-devel
BuildRequires:  zlib-devel

# Documentation
BuildRequires:  po4a
BuildRequires:  rubygem-asciidoctor

Provides:       bundled(fmt) = 9.0.0
Provides:       bundled(libdxflib) = 3.26.4
Provides:       bundled(polyclipping) = 6.4.2
Provides:       bundled(potrace) = 1.15

Requires:       electronics-menu
Requires:       libgit2
Requires:       libngspice
Requires:       libsecret
Requires:       ngspice-codemodel
Requires:       python3-wxpython4
Requires:       unixODBC

Suggests:       kicad

%description
KiCad is EDA software to design electronic schematic
diagrams and printed circuit board artwork of up to
32 layers.

%package        packages3d
Summary:        3D Models for KiCad
License:        CC-BY-SA
BuildArch:      noarch
Requires:       kicad >= 8.0.0

%description    packages3d
3D Models for KiCad.

%package        doc
Summary:        Documentation for KiCad
License:        GPLv3+ or CC-BY
BuildArch:      noarch

%description    doc
Documentation for KiCad.


%prep
%setup -q -a 1 -a 2 -a 3 -a 4 -a 5

%build

# KiCad application
%cmake \
    -DKICAD_SCRIPTING_WXPYTHON=ON \
    -DKICAD_USE_OCC=ON \
    -DKICAD_INSTALL_DEMOS=ON \
    -DKICAD_BUILD_QA_TESTS=OFF \
    -DKICAD_BUILD_I18N=ON \
    -DKICAD_I18N_UNIX_STRICT_PATH=ON \
    -DKICAD_USE_EGL=OFF \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DPYTHON_SITE_PACKAGE_PATH=%{python3_sitearch} \
    -DKICAD_VERSION_EXTRA=%{release}
%cmake_build

# Templates
pushd %{name}-templates-%{version}/
%cmake
%cmake_build
popd

# Symbol libraries
pushd %{name}-symbols-%{version}/
%cmake
%cmake_build
popd

# Footprint libraries
pushd %{name}-footprints-%{version}/
%cmake
%cmake_build
popd

# 3D models
pushd %{name}-packages3D-%{version}/
%cmake
%cmake_build
popd

# Documentation (HTML only)
pushd %{name}-doc-%{version}/
%cmake \
    -DPDF_GENERATOR=none \
    -DBUILD_FORMATS=html
%cmake_build
popd


%install

# KiCad application
%cmake_install

# Install desktop
for desktopfile in %{buildroot}%{_datadir}/applications/*.desktop ; do
  desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  --delete-original                          \
  ${desktopfile}
done

# Templates
pushd %{name}-templates-%{version}/
%cmake_install
cp -p LICENSE.md ../LICENSE-templates.md
popd

# Symbol libraries
pushd %{name}-symbols-%{version}/
%cmake_install
cp -p LICENSE.md ../LICENSE-symbols.md
popd

# Footprint libraries
pushd %{name}-footprints-%{version}/
%cmake_install
cp -p LICENSE.md ../LICENSE-footprints.md
popd

# 3D models
pushd %{name}-packages3D-%{version}/
%cmake_install
popd

# Documentation
pushd %{name}-doc-%{version}/
%cmake_install
popd

%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml


%files -f %{name}.lang
%doc AUTHORS.txt
%attr(0755, root, root) %{_bindir}/*
%{_libdir}/%{name}/
%{_libdir}/libkicad_3dsg.so*
%{_libdir}/libkigal.so*
%{_libdir}/libkicommon.so*
%{python3_sitearch}/_pcbnew.so
%pycached %{python3_sitearch}/pcbnew.py
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.*
%{_datadir}/icons/hicolor/*/mimetypes/application-x-*.*
%{_datadir}/mime/packages/*.xml
%{_metainfodir}/*.metainfo.xml
%license LICENSE*
%exclude %{_datadir}/%{name}/3dmodels/*

%files packages3d
%{_datadir}/%{name}/3dmodels/*.3dshapes
%license %{name}-packages3D-%{version}/LICENSE*

%files doc
%{_docdir}/%{name}/help/
%exclude %{_docdir}/%{name}/AUTHORS.txt
%license %{name}-doc-%{version}/LICENSE*


%changelog
* Tue Jan 14 2025 Pete Walter <pwalter@fedoraproject.org> - 1:8.0.8-2
- Rebuild for libgit2 1.9.x

* Sat Jan 11 2025 Steven A. Falco <stevenfalco@gmail.com> - 1:8.0.8-1
- Update to 8.0.8

* Mon Dec 02 2024 Steven A. Falco <stevenfalco@gmail.com> - 1:8.0.7-1
- Update to 8.0.7

* Thu Oct 17 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1:8.0.6-2
- Fix for SWIG 4.3.0

* Mon Oct 14 2024 Steven A. Falco <stevenfalco@gmail.com> - 1:8.0.6-1
- Update to 8.0.6

* Fri Sep 06 2024 Steven A. Falco <stevenfalco@gmail.com> - 1:8.0.5-1
- Update to 8.0.5

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:8.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 16 2024 Steven A. Falco <stevenfalco@gmail.com> - 1:8.0.4-1
- Update to 8.0.4

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 1:8.0.3-2
- Rebuilt for Python 3.13

* Mon Jun 03 2024 Steven A. Falco <stevenfalco@gmail.com> - 1:8.0.3-1
- Update to 8.0.3

* Sat Jun 01 2024 Richard Shaw <hobbes1069@gmail.com> - 1:8.0.2-3
- Rebuild for opencascade 7.8.1.

* Thu May 02 2024 Steven A. Falco <stevenfalco@gmail.com> - 1:8.0.2-2
- Allow Python version 3.13

* Sat Apr 27 2024 Steven A. Falco <stevenfalco@gmail.com> - 1:8.0.2-1
- Update to 8.0.2

* Thu Mar 14 2024 Steven A. Falco <stevenfalco@gmail.com> - 1:8.0.1-1
- Update to 8.0.1

* Wed Mar 06 2024 Steven A. Falco <stevenfalco@gmail.com> - 1:8.0.0-2
- Correct lib file versions

* Fri Feb 23 2024 Steven A. Falco <stevenfalco@gmail.com> - 1:8.0.0-1
- Update to 8.0.0

* Fri Feb 16 2024 Steven A. Falco <stevenfalco@gmail.com> - 1:8.0.0-0.5.rc3
- Update to 8.0.0-rc3

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:8.0.0-0.4.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Steven A. Falco <stevenfalco@gmail.com> - 1:8.0.0-0.3.rc2
- Update to 8.0.0-rc2

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:8.0.0-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 13 2024 Steven A. Falco <stevenfalco@gmail.com> - 1:8.0.0-0.1.rc1
- Update to 8.0.0-rc1

* Thu Dec 28 2023 Steven A. Falco <stevenfalco@gmail.com> - 1:7.0.10-1
- Update to 7.0.10

* Sun Nov 05 2023 Steven A. Falco <stevenfalco@gmail.com> - 1:7.0.9-1
- Update to 7.0.9

* Fri Sep 29 2023 Steven A. Falco <stevenfalco@gmail.com> - 1:7.0.8-1
- Update to 7.0.8

* Tue Sep 12 2023 Steven A. Falco <stevenfalco@gmail.com> - 1:7.0.7-3
- No longer need rpath fixups

* Mon Aug 14 2023 Steven A. Falco <stevenfalco@gmail.com> - 1:7.0.7-2
- Need lsb for F37 and below

* Mon Aug 14 2023 Steven A. Falco <stevenfalco@gmail.com> - 1:7.0.7-1
- Update to 7.0.7

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 05 2023 Steven A. Falco <stevenfalco@gmail.com> - 1:7.0.6-1
- Update to 7.0.6

* Mon Jun 19 2023 Python Maint <python-maint@redhat.com> - 1:7.0.5-2
- Rebuilt for Python 3.12

* Fri May 26 2023 Steven A. Falco <stevenfalco@gmail.com> - 1:7.0.5-1
- Update to 7.0.5

* Mon May 22 2023 Steven A. Falco <stevenfalco@gmail.com> - 1:7.0.4-1
- Update to 7.0.4

* Sat May 13 2023 Steven A. Falco <stevenfalco@gmail.com> - 1:7.0.3-1
- Update to 7.0.3

* Fri Apr 14 2023 Steven A. Falco <stevenfalco@gmail.com> - 1:7.0.2-1
- Update to 7.0.2

* Thu Mar 23 2023 Steven A. Falco <stevenfalco@gmail.com> - 1:7.0.1-2
- Put redhat-lsb-core back

* Fri Mar 10 2023 Steven A. Falco <stevenfalco@gmail.com> - 1:7.0.1-1
- Update to 7.0.1

* Thu Feb 16 2023 Lubomir Rintel <lkundrak@v3.sk> - 1:7.0.0-2
- Don't hard-depend on redhat-lsb-core

* Sat Feb 11 2023 Steven A. Falco <stevenfalco@gmail.com> - 1:7.0.0-1
- Update to 7.0.0

* Fri Feb 03 2023 Steven A. Falco <stevenfalco@gmail.com> - 1:7.0.0-0.5.rc2
- Recommend libngspice rather than ngspice

* Sat Jan 28 2023 Steven A. Falco <stevenfalco@gmail.com> - 1:7.0.0-0.4.rc2
- Add a requirement for redhat-lsb-core to aid with bug reports.

* Wed Jan 25 2023 Steven A. Falco <stevenfalco@gmail.com> - 1:7.0.0-0.3.rc2
- Update to 7.0.0-0.3.rc2

* Wed Jan 25 2023 Steven A. Falco <stevenfalco@gmail.com> - 1:6.0.11-1
- Update to 6.0.11

* Thu Jan 19 2023 Steven A. Falco <stevenfalco@gmail.com> - 1:6.0.10-4
- GCC13 fix

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jan 14 2023 Richard Shaw <hobbes1069@gmail.com> - 1:6.0.10-2
- Rebuild for opencascade.

* Sat Jan 07 2023 Steven A. Falco <stevenfalco@gmail.com> - 1:7.0.0-0.1.rc1
- Test build for 7.0.0-0.1.rc1

* Sun Dec 18 2022 Steven A. Falco <stevenfalco@gmail.com> - 1:6.0.10-1
- Update to 6.0.10

* Wed Nov 23 2022 Steven A. Falco <stevenfalco@gmail.com> - 1:6.0.9-3
- Remove EGL flag

* Wed Nov 23 2022 Steven A. Falco <stevenfalco@gmail.com> - 1:6.0.9-2
- Rebuild for wxWidgets wxGLCanvas

* Fri Oct 28 2022 Steven A. Falco <stevenfalco@gmail.com> - 1:6.0.9-1
- Update to 6.0.9

* Fri Oct 21 2022 Steven A. Falco <stevenfalco@gmail.com> - 1:6.0.8-5
- Remove wxWidgets work-around

* Thu Oct 20 2022 Steven A. Falco <stevenfalco@gmail.com> - 1:6.0.8-4
- Patch for SWIG 4.1.0

* Thu Oct 20 2022 Steven A. Falco <stevenfalco@gmail.com> - 1:6.0.8-3
- Move pcbnew.so a different way

* Sat Oct 15 2022 Steven A. Falco <stevenfalco@gmail.com> - 1:6.0.8-2
- Move pcbnew.so

* Tue Sep 27 2022 Steven A. Falco <stevenfalco@gmail.com> - 1:6.0.8-1
- Update to 6.0.8

* Thu Sep 08 2022 Steven A. Falco <stevenfalco@gmail.com> - 1:6.0.7-7
- Convert license to SPDX format

* Fri Sep 02 2022 Steven A. Falco <stevenfalco@gmail.com> - 1:6.0.7-6
- Add some missing bundled library 'Provides'

* Tue Aug 16 2022 Steven A. Falco <stevenfalco@gmail.com> - 1:6.0.7-5
- EGL requires a built-in libGLEW

* Tue Aug 16 2022 Steven A. Falco <stevenfalco@gmail.com> - 1:6.0.7-4
- Make wx version conditional

* Thu Aug 11 2022 Steven A. Falco <stevenfalco@gmail.com> - 1:6.0.7-3
- Work around wxPython issue

* Thu Aug 04 2022 Scott Talbert <swt@techie.net> - 1:6.0.7-2
- Rebuild with wxWidgets 3.2

* Tue Jul 26 2022 Steven A. Falco <stevenfalco@gmail.com> - 1:6.0.7-1
- Update to 6.0.7

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Steven A. Falco <stevenfalco@gmail.com> - 1:6.0.6-3
- Add ngspice requirement for its models

* Tue Jun 21 2022 Steven A. Falco <stevenfalco@gmail.com> - 1:6.0.6-2
- Patch for python 3.11

* Sat Jun 18 2022 Steven A. Falco <stevenfalco@gmail.com> - 1:6.0.6-1
- Update to 6.0.6

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 1:6.0.5-3
- Rebuilt for Python 3.11

* Fri May 06 2022 Steven A. Falco <stevenfalco@gmail.com> - 1:6.0.5-2
- Patch for static vector crash

* Tue May 03 2022 Steven A. Falco <stevenfalco@gmail.com> - 1:6.0.5-1
- Update to 6.0.5

* Sat Mar 19 2022 Steven A. Falco <stevenfalco@gmail.com> - 1:6.0.4-1
- Update to 6.0.4

* Tue Mar 15 2022 Steven A. Falco <stevenfalco@gmail.com> - 1:6.0.3-1
- Update to 6.0.3

* Fri Mar 04 2022 Steven A. Falco <stevenfalco@gmail.com> - 1:6.0.2-3
- Fix cmake issue for doc

* Fri Mar 04 2022 Steven A. Falco <stevenfalco@gmail.com> - 1:6.0.2-2
- Fix cmake issue

* Fri Feb 11 2022 Steven A. Falco <stevenfalco@gmail.com> - 1:6.0.2-1
- Update to 6.0.2

* Thu Feb 10 2022 Orion Poplawski <orion@nwra.com> - 1:6.0.1-5
- Rebuild for glew 2.2

* Mon Jan 31 2022 Steven A. Falco <stevenfalco@gmail.com> - 1:6.0.1-4
- Fix conflict in docs

* Tue Jan 25 2022 Steven A. Falco <stevenfalco@gmail.com> - 1:6.0.1-3
- Patch missing include file

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 12 2022 Steven A. Falco <stevenfalco@gmail.com> - 1:6.0.1-1
- Update to 6.0.1

* Sat Dec 25 2021 Steven A. Falco <stevenfalco@gmail.com> - 1:6.0.0-2
- Update cmake flags

* Thu Dec 23 2021 Steven A. Falco <stevenfalco@gmail.com> - 1:6.0.0-1
- Update to 6.0.0

* Tue Nov 16 2021 Steven A. Falco <stevenfalco@gmail.com> - 1:6.0.0-0.1.rc1
- Update to 6.0.0-rc1

* Thu Nov 04 2021 Steven A. Falco <stevenfalco@gmail.com> - 1:5.1.12-1
- Update to 5.1.12

* Thu Nov 04 2021 Steven A. Falco <stevenfalco@gmail.com> - 1:5.1.11-1
- Update to 5.1.11

* Tue Oct 19 2021 Steven A. Falco <stevenfalco@gmail.com> - 1:5.1.10-8
- URL no longer valid

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1:5.1.10-7
- Rebuilt with OpenSSL 3.0.0

* Mon Aug 23 2021 Steven A. Falco <stevenfalco@gmail.com> - 1:5.1.10-6
- Rebuilt for new ngspice library

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1:5.1.10-4
- Rebuilt for Python 3.10

* Wed Jun 02 2021 Steven A. Falco <stevenfalco@gmail.com> - 1:5.1.10-3
- Remove illegal rpath

* Fri May 28 2021 Steven A. Falco <stevenfalco@gmail.com> - 1:5.1.10-2
- Remove provides and obsoletes

* Tue Apr 27 2021 Steven A. Falco <stevenfalco@gmail.com> - 1:5.1.10-1
- Update to 5.1.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 22 2020 Steven A. Falco <stevenfalco@gmail.com> - 1:5.1.9-1
- Update to 5.1.9

* Wed Dec 02 2020 Steven A. Falco <stevenfalco@gmail.com> - 1:5.1.8-5
- AppStream metadata fixes

* Fri Nov 27 2020 Richard Shaw <hobbes1069@gmail.com> - 1:5.1.8-4
- Rebuild for OCC 7.5.0.

* Thu Nov 26 2020 Steven A. Falco <stevenfalco@gmail.com> - 1:5.1.8-4
- Add Python 3.10 compatibility - add one more cmake file.

* Thu Nov 26 2020 Steven A. Falco <stevenfalco@gmail.com> - 1:5.1.8-3
- Add Python 3.10 compatibility

* Thu Nov 26 2020 Richard Shaw <hobbes1069@gmail.com> - 1:5.1.8-2
- Rebuild for OCC 7.5.0.

* Wed Oct 28 2020 Steven A. Falco <stevenfalco@gmail.com> - 1:5.1.8-1
- Update to 5.1.8

* Sat Sep 26 2020 Steven A. Falco <stevenfalco@gmail.com> - 1:5.1.7-1
- Update to 5.1.7

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Steven A. Falco <stevenfalco@gmail.com> - 1:5.1.6-5
- Prepare for new cmake macros

* Thu May 28 2020 Charalampos Stratakis <cstratak@redhat.com> - 1:5.1.6-4
- Add Python 3.9 compatibility

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1:5.1.6-3
- Rebuilt for Python 3.9

* Fri May 15 2020 Steven A. Falco <stevenfalco@gmail.com> - 1:5.1.6-2
- Patch for boost 1.73 compile error.

* Tue May 12 2020 Steven A. Falco <stevenfalco@gmail.com> - 1:5.1.6-1
- Update to 5.1.6

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 18 2019 Steven A. Falco <stevenfalco@gmail.com> - 1:5.1.5-1
- Update to 5.1.5

* Sat Nov 16 2019 Steven A. Falco <stevenfalco@gmail.com> - 1:5.1.4-6
- Switch to opencascade for F32 and up

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1:5.1.4-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Wed Aug 21 2019 Miro Hrončok <mhroncok@redhat.com> - 1:5.1.4-4
- Rebuilt for Python 3.8

* Tue Aug 20 2019 Dan Horák <dan[at]danny.cz> - 1:5.1.4-3
- enable build on ppc64le

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1:5.1.4-2
- Rebuilt for Python 3.8

* Sun Aug 04 2019 Steven A. Falco <stevenfalco@gmail.com> - 1:5.1.4-1
- Update to 5.1.4

* Fri Aug 02 2019 Steven A. Falco <stevenfalco@gmail.com> - 1:5.1.3-3
- Revert the previous change pending further discussion

* Fri Aug 02 2019 Steven A. Falco <stevenfalco@gmail.com> - 1:5.1.3-2
- Correct crash caused by _GLIBCXX_ASSERTIONS

* Mon Jul 29 2019 Steven A. Falco <stevenfalco@gmail.com> - 1:5.1.3-1
- Update to 5.1.3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 10 2019 Steven A. Falco <stevenfalco@gmail.com> - 1:5.1.2-2
- SWIG patch for rawhide (fc31)

* Mon Apr 22 2019 Steven A. Falco <stevenfalco@gmail.com> - 1:5.1.2-1
- Update to 5.1.2

* Wed Apr 17 2019 Steven A. Falco <stevenfalco@gmail.com> - 1:5.1.1-1
- Update to 5.1.1

* Mon Mar 11 2019 Steven A. Falco <stevenfalco@gmail.com> - 1:5.1.0-1
- Update to 5.1.0

* Fri Mar 01 2019 Steven A. Falco <stevenfalco@gmail.com> - 1:5.1.0-0.1.rc2
- Update to 5.1.0-rc2

* Thu Jan 31 2019 Steven A. Falco <stevenfalco@gmail.com> - 1:5.0.2-5
- Remove workaround for ngspice library

* Mon Jan 14 2019 Steven A. Falco <stevenfalco@gmail.com> - 1:5.0.2-4
- Enable ngspice

* Sun Dec 16 2018 Steven A. Falco <stevenfalco@gmail.com> - 1:5.0.2-3
- Revert missing build dependency - upstream bug fixed

* Sun Dec 09 2018 Steven A. Falco <stevenfalco@gmail.com> - 1:5.0.2-2
- Add missing build dependency needed by F29

* Tue Dec 04 2018 Steven A. Falco <stevenfalco@gmail.com> - 1:5.0.2-1
- Update to 5.0.2

* Fri Oct 12 2018 Steven A. Falco <stevenfalco@gmail.com> - 1:5.0.1-1
- Update to 5.0.1

* Fri Aug 24 2018 Steven A. Falco <stevenfalco@gmail.com> - 1:5.0.0-4
- Force "release build" to work around a bug in the cmake scripts

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 1:5.0.0-3
- Rebuilt for glew 2.1.0

* Fri Aug 03 2018 Steven A. Falco <stevenfalco@gmail.com> - 1:5.0.0-2
- Separate 3D models from main package

* Fri Jul 20 2018 Steven A. Falco <stevenfalco@gmail.com> - 1:5.0.0-1
- Update to 5.0.0

* Sat Jul 14 2018 Steven A. Falco <stevenfalco@gmail.com> - 1:5.0.0-0.4.rc3
- Adding BuildRequires to fix "missing compiler" error with the latest rawhide

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.0-0.3.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 04 2018 Steven A. Falco <stevenfalco@gmail.com> - 1:5.0.0-0.2.rc3
- Update to 5.0.0-rc3

* Thu Jun 14 2018 Steven A. Falco <stevenfalco@gmail.com> - 1:5.0.0-0.1.rc2
- Update to 5.0.0-rc2

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 04 2017 Scott Talbert <swt@techie.net> - 1:4.0.7-2
- Update to build against merged compat-wxGTK3-gtk2-devel package

* Wed Sep 27 2017 Lubomir Rintel <lkundrak@v3.sk> - 1:4.0.7-1
- Update to 4.0.7

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> - 1:4.0.6-3
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sun Apr 02 2017 Lubomir Rintel <lkundrak@v3.sk> - 1:4.0.6-1
- Update to 4.0.6

* Wed Feb 22 2017 Lubomir Rintel <lkundrak@v3.sk> - 1:4.0.5-3
- Add missing footprint libraries

* Tue Feb 14 2017 Lubomir Rintel <lkundrak@v3.sk> - 1:4.0.5-2
- Fix build with newer boost

* Tue Feb 14 2017 Lubomir Rintel <lkundrak@v3.sk> - 1:4.0.5-1
- Update to 4.0.5

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 1:4.0.4-2
- Rebuild for glew 2.0.0

* Tue Oct 18 2016 Lubomir Rintel <lkundrak@v3.sk> - 1:4.0.4-1
- Update to 4.0.4

* Thu Aug 25 2016 Lubomir Rintel <lkundrak@v3.sk> - 1:4.0.3-1
- Update to 4.0.3

* Wed Apr 20 2016 Lubomir Rintel <lkundrak@v3.sk> - 1:4.0.2-2
- Add AppStream metadata

* Tue Mar 01 2016 Lubomir Rintel <lkundrak@v3.sk> - 1:4.0.2-1
- Update to 4.0.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 1:4.0.1-4
- Rebuilt for Boost 1.60

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 1:4.0.1-3
- Rebuild for glew 1.13

* Thu Dec 17 2015 Lubomir Rintel <lkundrak@v3.sk> - 1:4.0.1-2
- Hardcode the C++ ABI version to make wxGTK happy

* Tue Dec 15 2015 Lubomir Rintel <lkundrak@v3.sk> - 1:4.0.1-1
- Update to 4.0.1

* Thu Dec 03 2015 Lubomir Rintel <lkundrak@v3.sk> - 1:4.0.0-1
- Update to the release
- SPEC file cleanup:
- Use tarballs, drop the 3rd party libraries we bundled

* Sat Oct 24 2015 Lubomir Rintel <lkundrak@v3.sk> - 2015.10.24-1.rev6276
- Update to a later snapshot
- Updated library, new documentation, translations

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 2015.08.03-4.rev6041
- Rebuilt for Boost 1.59

* Wed Aug 05 2015 Jonathan Wakely <jwakely@redhat.com> 2015.08.03-3.rev6041
- Rebuilt for Boost 1.58

* Mon Aug 03 2015 Lubomir Rintel <lkundrak@v3.sk> - 2015.08.03-2.rev6041
- Set KICAD_BUILD_VERSION
- Ship the maintainer tools with the source package

* Mon Aug 03 2015 Lubomir Rintel <lkundrak@v3.sk> - 2015.08.03-1.rev6041
- Update to a later snapshot

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.03.21-5.rev5528
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 2015.03.21-4.rev5528
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.03.21-3.rev5528
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 2015.03.21-2.rev5528
- Handle all 64-bit architectures

* Sun Mar 22 2015 Lubomir Rintel <lkundrak@v3.sk> - 2015.03.21-1.rev5528
- Update to a later snapshot
- Fix the freerouter patch
- Enable parallel build

* Thu Mar 19 2015 Lubomir Rintel <lkundrak@v3.sk> - 2015.02.05-1.rev5404
- Update to a later snapshot

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 2014.03.13-11.rev4744
- Rebuild for boost 1.57.0
- Add upstream patch to support new Boost.Context API
  (kicad-2014.03.13-boost-context.patch)

* Fri Jan 02 2015 Lubomir Rintel <lkundrak@v3.sk> - 2014.03.13-10.rev4744
- Use local autorouter

* Sun Nov 30 2014 Lubomir Rintel <lkundrak@v3.sk> - 2014.03.13-9.rev4744
- Install library footprints

* Mon Aug 18 2014 Rex Dieter <rdieter@fedoraproject.org> 2014.03.13-8.rev4744
- update mime scriptlets

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2014.03.13-7.rev4744
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2014.03.13-6.rev4744
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 2014.03.13-5.rev4744
- Rebuild for boost 1.55.0

* Tue Mar 18 2014 Jaromir Capik <jcapik@redhat.com> - 2014.03.13-4.rev4744
- Removing ExcludeArch as boost-context has been built for arm

* Mon Mar 17 2014 Ville Skyttä <ville.skytta@iki.fi> - 2014.03.13-3.rev4744
- Don't strip binaries too early (#1076929)

* Mon Mar 17 2014 Jaromir Capik <jcapik@redhat.com> - 2014.03.13-2.rev4744
- Fixing the pcb_calculator desktop file (missing underscore)

* Thu Mar 13 2014 Jaromir Capik <jcapik@redhat.com> - 2014.03.13-1.rev4744
- Update to the latest available revisions
- Building with -j1 instead of _smp_mflags (probably causing build failures)
- Creating scripts for source downloading & postprocessing
- Fixing bogus dates in the changelog

* Mon Dec 23 2013 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2013.06.11-2.rev4021
- Removed kicad.pdf from kicad (Fix #1001243)
- Clean up spec file as suggested by Michael Schwendt
- ldconfig no more needed in this release
- Fix kicad-doc Group
- kicad-doc no more requires kicad
 
* Sat Jun 22 2013 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2013.06.11-1.rev4021
- New upstream release
- Added symbols and modules (with 3d view) from Walter Lain
 
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.01.19-3.rev3256
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.01.19-2.rev3256
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jan 29 2012 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2012.01.19-1.rev3256
- New upstream release
- Add doxygen as build requirement
- Add bulgarian language
- Add it and pl tutorials
- Update versioning patch
- Add patch to fix python syntax in bom-in-python (Gerd v. Egidy <gerd@egidy.de>)
- Add a new patch to fix a new link time error
- Fix a PS plotting scale bug
- Move junction button close to no connexion button
- Fix thermal relief gap calculation for circular pads in pcbnew
- Add undo/redo support for Pcbnew auto place, auto move, and auto route features.
- Make CvPcb correctly preview the selected component footprint if one has already been assigned.
- Fix a bug in pcb calculation
- Width tuning (width correction) for PS plotting of tracks, pads and vias

* Wed Jan 25 2012 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2011.07.12-4.rev3047
- Fix gcc-4.7 issue by Scott Tsai <scottt.tw@gmail.com> 

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2011.07.12-3.rev3047
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 15 2011 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2011.07.12-2.rev3047
- Fix patch command 

* Tue Jul 12 2011 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2011.07.12-1.rev3047
- New upstream version
- Update versioning patch
- Add Polish documentation
- Add Epcos MKT capacitors library
- Fix localisation installation path

* Mon Apr  4 2011 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2011.01.28-3.rev2765
- Fix 3D viewer crash (BZ #693008)

* Wed Mar 23 2011 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2011.01.28-2.rev2765
- Add missing library

* Tue Mar 22 2011 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2011.01.28-1.rev2765
- New upstream version
- Update versioning patch, all others patches no more needed
- Patch to fix a link time error (with help from Kevin Kofler and Nikola Pajkovsky)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2010.05.27-10.rev2363
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 30 2011 Dan Horák <dan@danny.cz> - 2010.05.27-9.rev2363
- Add s390x as 64-bit arch

* Sat Jan 29 2011 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.27-8.rev2363
- Fix 3D view crash with some graphics cards (BZ #664143).

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 2010.05.27-7.rev2363
- rebuilt against wxGTK-2.8.11-2

* Tue Jun 15 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.27-6
- Fix some module edition issues (https://bugs.launchpad.net/kicad/+bug/593546,
  https://bugs.launchpad.net/kicad/+bug/593547)

* Fri Jun 11 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.27-5
- Fix a crash in searching string (https://bugs.launchpad.net/kicad/+bug/592566)

* Tue Jun  8 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.27-4
- Fix a focus issue (https://bugs.launchpad.net/kicad/+bug/587970)
- Fix an unwanted mouse cursor move when using the t hotkey in pcbnew
- Fix an issue on arcs draw in 3D viewer (https://bugs.launchpad.net/kicad/+bug/588882)

* Mon May 31 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.27-3
- Fix an undo-redo issue (https://bugs.launchpad.net/kicad/+bug/586032)

* Sun May 30 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.27-2
- Don't forget icons

* Sat May 29 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.27-1
- New packager version
- Update kicad version number patch
- Patch to fix https://bugs.launchpad.net/kicad/+bug/587175
- Patch to fix https://bugs.launchpad.net/kicad/+bug/587176

* Fri May 21 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.09-3
- Fix the kicad version number
- Fix a problem when trying to modify a footprint value in eeschema
  https://bugs.launchpad.net/kicad/+bug/583939

* Tue May 18 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.09-2
- No backup of patched files to delete
- Add noreplace flag to config macro

* Mon May 17 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.09-1
- New upstream version
- All previous patches no more needed
- Backward to cmake 2.6 requirement

* Sun May  9 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.05-1
- New upstream version
- All previous patches no more needed
- Fix url: KiCad move from SourceForge.net to LaunchPad.net
- Remove vendor tag from desktop-file-install
- Add x-kicad-pcbnew mimetype
- Add new icons for mimetype

* Mon May  3 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.04.06-9.rev2515
- Fix a minor bug that occurs when changing module orientation or side

* Mon May  3 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.04.06-8.rev2515
- Auto update 3D viewer: fix https://bugs.launchpad.net/kicad/+bug/571089
- Create png from screen (libedit): fix https://bugs.launchpad.net/kicad/+bug/573833

* Sun May  2 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.04.06-7.rev2515
- Rename COTATION class (french word) in DIMENSION and fix
  https://bugs.launchpad.net/kicad/+bug/568356 and https://bugs.launchpad.net/kicad/+bug/568357
- Some code cleaning ans enhancements + fix a bug about last netlist file used (LP #567902)

* Sat May  1 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.04.06-6.rev2515
- Make cleanup feature undoable, fix https://bugs.launchpad.net/kicad/+bug/564619
- Fix issues in SVG export, fix https://bugs.launchpad.net/kicad/+bug/565388
- Minor pcbnew enhancements
- Fix minor gerber problems, fix https://bugs.launchpad.net/kicad/+bug/567881

* Sat May  1 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.04.06-5.rev2515
- DRC have to use the local parameters clearance if specified,
  and NETCLASS value only if no local value specified. 

* Sat May  1 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.04.06-4.rev2514
- Fix https://bugs.launchpad.net/bugs/568896 and https://bugs.launchpad.net/bugs/569312

* Thu Apr 29 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.04.06-3.rev2514
- Fix a crash that happens sometimes when opening the design rule dialog

* Mon Apr 26 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.04.06-2.rev2514
- Fix https://bugs.launchpad.net/bugs/570074

* Mon Apr 12 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.04.06-1.rev2514
- New upstream version
- Patches no more needed

* Mon Apr  5 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.03.14-5.rev2463
- Add patch to fix SF #2981759

* Sat Apr  3 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.03.14-4.rev2463
- Apply upstream patch to fix inch/mm ratio
- Provide a source download URL

* Wed Mar 17 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.03.14-3.rev2463
- Patch with svn revision 2463 which fix 2 bugs
- Harmonize identation in %%changelog

* Tue Mar 16 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2010.03.14-2.rev2462
- Link fixes. Really, these libraries should be linked properly so they don't need
  the executable linking calls to be explicitly correct, but cmake gives me a headache.
- Fix demo installation

* Mon Mar 15 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.03.14-1.rev2462
- New upstream version

* Mon Aug 24 2009 Jon Ciesla <limb@jcomserv.net> - 2009.07.07-4.rev1863
- Multilib path correction, BZ 518916.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2009.07.07-3.rev1863
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 08 2009 Jon Ciesla <limb@jcomserv.net> - 2009.07.07-2.rev1863
- Dropped eeschema desktop file.
- Moved English kicad.pdf to main rpm.
- Added ls.so.conf file and ldconfig to post, postun to fix libs issue.
- Dropped category Development from desktop file.

* Tue Jul 7 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 2009.07.07-1.rev1863
- svn rev 1863
- documentation splitted into multiple packages
- libraries are now taken directly from SVN rather than from older releases
- build changed to cmake based

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2007.07.09-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug 29 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 2007.07.09-4
- First patch is Patch0 - should fix build in Rawhide.
- Include %%_libdir/kicad directory.
- Drop explicit Requires wxGTK in favour of automatic SONAME dependencies.

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2007.07.09-3
- Autorebuild for GCC 4.3

* Mon Oct 15 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2007.07.09-2
- Update desktop file

* Thu Oct 04 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2007.07.09-1
- New upstream version
- Merge previous patches
- Remove X-Fedora, Electronics and Engineering categories
- Update desktop file

* Mon Aug 27 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2007.01.15-4
- License tag clarification

* Thu Aug 23 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2007.01.15-3
- Rebuild

* Wed Feb 14 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2007.01.15-2
- Fix desktop entry. Fix #228598

* Thu Feb  8 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2007.01.15-1
- New upstream version

* Thu Feb  8 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006.08.28-4
- Add patch to build with RPM_OPT_FLAGS and remove -s from LDFLAGS
  Contribution of Ville Skyttä <ville[DOT]skytta[AT]iki[DOT]fi>
  Fix #227757
- Fix typo in french summary

* Thu Dec 28 2006 Jason L Tibbitts III <tibbs@math.uh.edu> 2006.08.28-3
- Rebuild with wxGTK 2.8.

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 2006.08.28-2
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Fri Sep 22 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006.08.28-1
- New upstream version
- Use macro style instead of variable style
- Install missing modules. Fix #206602

* Fri Sep  1 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006.06.26-6
- FE6 rebuild

* Mon Jul 10 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006.06.26-5
- Removing backup files is no more needed.

* Mon Jul 10 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006.06.26-4
- Remove BR libGLU-devel that is no more needed (bug #197501 is closed)
- Fix files permissions.

* Mon Jul  3 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006.06.26-3
- s/mesa-libGLU-devel/libGLU-devel/

* Mon Jul  3 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006.06.26-2
- BR mesa-libGLU-devel

* Wed Jun 28 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006.06.26-1
- New upstream version

* Tue Jun 13 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006.04.24-5
- Change name
- Use %%{_docdir} instead of %%{_datadir}/doc
- Use %%find_lang
- Update desktop database
- Convert MSDOS EOL to Unix EOL
- Remove BR utrac

* Mon Jun 12 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006-04-24-0-4
- Patch to suppress extra qualification compile time error on FC5
- BR utrac to convert MSDOS files before applying patch
  This will be remove for the next upstream version.

* Tue May 23 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006-04-24-0-3
- Install help in /usr/share/doc/kicad/ as the path is hardcoded in gestfich.cpp
- Add desktop file

* Mon May 22 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006-04-24-0-2
- Add a second tarball that contains many things that are not included in
  the upstream source tarball such components and footprints librairies,
  help, localisation, etc.

* Sun May 21 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006-04-24-0-1
- Initial Fedora RPM
