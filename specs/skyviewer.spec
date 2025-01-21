Name:           skyviewer
Version:        1.1.0
Release:        5%{?dist}
Summary:        Program to display HEALPix-based skymaps in FITS files

License:        CFITSIO
URL:            http://lambda.gsfc.nasa.gov/toolbox/tb_skyviewer_ov.cfm
Source0:        http://lambda.gsfc.nasa.gov/toolbox/skyviewer/%{name}-%{version}.tar.gz
Source1:        skyviewer.desktop

BuildRequires:  make
BuildRequires:  cfitsio-devel
BuildRequires:  chealpix-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libQGLViewer-qt5-devel
BuildRequires:  cmake(qt5widgets)
BuildRequires:  cmake(qt5gui)
BuildRequires:  cmake(qt5xml)
BuildRequires:  cmake(qt5opengl)
BuildRequires:  mesa-libGLU-devel

%description
SkyViewer is an OpenGL based program to display HEALPix-based skymaps,
saved in FITS format files. The loaded skymaps can be viewed either on a 3D
sphere or as a Mollweide projection. In either case, realtime panning and
zooming are supported, along with rotations for the 3D sphere view,
assuming you have a strong enough graphics card.


%prep
%setup -q

%build
%{qmake_qt5} INCLUDE_DIR=%{_includedir} \
        LIB_DIR=%{_libdir} \
        INCPATH=%{_includedir}/cfitsio
make %{?_smp_mflags}


%install

# Binary
install -d %{buildroot}%{_bindir}
install -pm 0755 skyviewer %{buildroot}%{_bindir}

# Icon
install -d %{buildroot}%{_datadir}/pixmaps
install -pm 0644 images/spherical.png \
        %{buildroot}%{_datadir}/pixmaps/skyviewer.png

# Desktop entry
desktop-file-install --vendor='' %{SOURCE1} \
        --dir=%{buildroot}%{_datadir}/applications

%files
%license License.txt
%{_bindir}/skyviewer
%{_datadir}/pixmaps/skyviewer.png
%{_datadir}/applications/skyviewer.desktop
%doc test_iqu.fits README.txt general.txt notes-ngp.txt


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar  1 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0
- Use Qt5, libQGLViewer-qt5

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 29 2022 Maxwell G <gotmax@e.email> - 1.0.1-28
- Rebuild for cfitsio 4.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Feb 02 2021 Christian Dersch <lupinix@mailbox.org> - 1.0.1-24
- Rebuilt for libcfitsio.so.7

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 2019 Christian Dersch <lupinix@fedoraproject.org> - 1.0.1-19
- rebuilt

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 12 2018 Rich Mattes <richmattes@gmail.com> - 1.0.1-17
- Update library name for libQGLViewer
- Enable ARM architectures (rhbz#1548678)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 26 2018 Christian Dersch <lupinix@mailbox.org> - 1.0.1-15
- rebuilt for cfitsio 3.450

* Fri Feb 23 2018 Christian Dersch <lupinix@mailbox.org> - 1.0.1-14
- rebuilt for cfitsio 3.420 (so version bump)
- exclude ARM builds for now as builds are failing since last mass rebuild (#1548678)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Apr 07 2017 Christian Dersch <lupinix@mailbox.org> - 1.0.1-9
- removed ExcludeArch ppc64 as healpix is available there now

* Wed Apr 05 2017 Christian Dersch <lupinix@mailbox.org> - 1.0.1-8
- rebuilt for healpix 3.31
- modernized spec a bit
- ExcludeArch: ppc64 (healpix not available there)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jul 18 2016 Nikos Roussos <comzeradd@fedoraproject.org> - 1.0.1-6
- Rebuild for libQGLViewer

* Wed Feb 03 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.0.1-5
- use %%qmake_qt4 macro to ensure proper build flags

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.1-3
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 04 2014 Nikos Roussos <comzeradd@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 09 2014 Orion Poplawski <orion@cora.nwra.com> - 1.0.0-14
- Rebuild for cfitsio 3.360

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 25 2013 Tom Callaway <spot@fedoraproject.org> - 1.0.0-12
- rebuild for new cfitsio
- fix ftbfs, link to libGLU

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-9
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0.0-7
- Rebuild for libQGLViewer-2.3.9.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 09 2010 Lubomir Rintel (Fedora Astronomy) <lkundrak@v3.sk> - 1.0.0-5
- Rebuild

* Tue Apr 27 2010 Lubomir Rintel (Fedora Astronomy) <lkundrak@v3.sk> - 1.0.0-4
- Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 09 2009 Lubomir Rintel (Fedora Astronomy) <lkundrak@v3.sk> - 1.0.0-2
- Update license
- Fix RBs (Jussi Lehtola)
- Add documentation

* Wed Mar 25 2009 Lubomir Rintel (Fedora Astronomy) <lkundrak@v3.sk> - 1.0.0-1
- Initial packaging
