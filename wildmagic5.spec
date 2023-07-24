##Source code includes PDF documentation that is copyrighted
##You may download them for your personal use from upstream website

## The RPM macro for the linker flags does not exist on EPEL
%if 0%{?epel} < 7
%{!?__global_ldflags: %global __global_ldflags -Wl,-z,relro}
%endif

# Workaround for rhbz#2044028
%if 0%{?fedora} > 35
%undefine _package_note_file
%endif

%undefine _ld_as_needed

Name:  wildmagic5
Summary:  Wild Magic libraries
Version:  5.17
Release:  16%{?dist}
License:  Boost
URL: https://www.geometrictools.com
Source0:  https://www.geometrictools.com/Downloads/WildMagic5p17.zip

BuildRequires: make
BuildRequires: freeglut-devel, mesa-libGL-devel, mesa-libGLU-devel, libXext-devel
BuildRequires: libX11-devel, glibc-devel, libstdc++-devel, dos2unix
BuildRequires: gcc, gcc-c++

Patch0: %{name}-fix-SimplePendulum_output_files.patch
Patch1: %{name}-fix-DistancePointEllipseEllipsoid.patch
Patch2: %{name}-fix_ldflags.patch

%description
A library of source code for computing in the fields of graphics, 
mathematics, physics, and image analysis.
Web page documentation:
geometrictools.com/Documentation/Documentation.html

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package samples
Summary: Samples files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-data = %{version}-%{release}
%description samples
Graphics, Physics, Imagics and Mathematics 
directories containing sample files.
Execute the sample files in a dedicated directory because
they generate their own output files.
Web page documentation:
geometrictools.com/Documentation/Documentation.html

%package data
Summary: %{name} data files
BuildArch: noarch
%description data
This package provides the %{name} data files.
They are generally required when either using the library 
or developing with it or developing it.

%prep
%autosetup -n GeometricTools -N

dos2unix WildMagic5/SamplePhysics/SimplePendulum/SimplePendulum.cpp
dos2unix WildMagic5/SampleMathematics/DistancePointEllipseEllipsoid/DistancePointEllipseEllipsoid.cpp
dos2unix WildMagic5/SampleGraphics/makeapp.wm5
dos2unix WildMagic5/SamplePhysics/makeapp.wm5
dos2unix WildMagic5/SampleImagics/makeapp.wm5
dos2unix WildMagic5/SampleMathematics/makeapp.wm5
%patch0 -p0
%patch1 -p0
%patch2 -p0

sed -i 's|CFLAGS += -O2 -DNDEBUG|CFLAGS += %{optflags} -pthread -DNDEBUG|g' WildMagic5/LibGraphics/Renderers/GlxRenderer/makerend.wm5
sed -i 's|CFLAGS += -O2 -DNDEBUG|CFLAGS += %{optflags} -pthread -DNDEBUG|g' WildMagic5/SamplePhysics/makeapp.wm5
sed -i 's|@@LDFLAGS@@|%{__global_ldflags}|g' WildMagic5/SamplePhysics/makeapp.wm5
sed -i 's|CFLAGS += -O2 -DNDEBUG|CFLAGS += %{optflags} -pthread -DNDEBUG|g' WildMagic5/SampleGraphics/makeapp.wm5
sed -i 's|@@LDFLAGS@@|%{__global_ldflags}|g' WildMagic5/SampleGraphics/makeapp.wm5
sed -i 's|CFLAGS += -O2 -DNDEBUG|CFLAGS += %{optflags} -pthread -DNDEBUG|g' WildMagic5/SampleImagics/makeapp.wm5
sed -i 's|@@LDFLAGS@@|%{__global_ldflags}|g' WildMagic5/SampleImagics/makeapp.wm5
sed -i 's|CFLAGS += -O2 -DNDEBUG|CFLAGS += %{optflags} -pthread -DNDEBUG|g' WildMagic5/SampleMathematics/makeapp.wm5
sed -i 's|@@LDFLAGS@@|%{__global_ldflags}|g' WildMagic5/SampleMathematics/makeapp.wm5

##Fix soname bug
for i in `find . -type f \( -name "*makefile.wm5" \)`; do
sed -e 's|so.5.15|so.%{version}|g' -i $i
done
sed -e 's|15|17|g' -i WildMagic5/LibGraphics/Renderers/GlxRenderer/makerend.wm5
#

%build
##Build LibCore --> LibMathematics
export LDFLAGS="%{__global_ldflags} -lpthread -lm"
export CFLAGS="%{optflags} -pthread -DNDEBUG"
make CFG=ReleaseDynamic -f makefile.wm5 -C WildMagic5/LibCore -j1

export LDFLAGS="%{__global_ldflags} -lpthread -L../../SDK/Library/ReleaseDynamic -lWm5Core"
export CFLAGS="%{optflags} -pthread -DNDEBUG"
make CFG=ReleaseDynamic -f makefile.wm5 -C WildMagic5/LibMathematics -j1

##Build LibPhysics -> LibImagics -> LibGraphics
export LDFLAGS="%{__global_ldflags} -L../../SDK/Library/ReleaseDynamic -lWm5Mathematics -lpthread -L../../SDK/Library/ReleaseDynamic -lWm5Core"
export CFLAGS="%{optflags} -pthread -DNDEBUG"
make CFG=ReleaseDynamic -f makefile.wm5 -C WildMagic5/LibPhysics -j1

export LDFLAGS="%{__global_ldflags} -lpthread -L../../SDK/Library/ReleaseDynamic -lWm5Mathematics"
export CFLAGS="%{optflags} -pthread -DNDEBUG"
make CFG=ReleaseDynamic -f makefile.wm5 -C WildMagic5/LibImagics -j1

export LDFLAGS="%{__global_ldflags} -L../../SDK/Library/ReleaseDynamic -lWm5Mathematics -L%{_libdir} -lGL -lGLU -L../../SDK/Library/ReleaseDynamic -lWm5Core"
export CFLAGS="%{optflags} -pthread -DNDEBUG"
make CFG=ReleaseDynamic -f makefile.wm5 -C WildMagic5/LibGraphics -j1

##Build LibApplications
export LDFLAGS="%{__global_ldflags} \
 -L../../SDK/Library/ReleaseDynamic -lWm5Core -lWm5Mathematics -lWm5Graphics -lGL -lGLU \
 -L../../SDK/Library/ReleaseDynamic -lWm5Imagics -lWm5Physics"

%global WILD_OPT_FLAGS %(echo "-c -D__LINUX__ -DWM5_USE_OPENGL %{optflags} -fPIC -pthread -DNDEBUG")
make CFG=ReleaseDynamic -f makefile.wm5 -C WildMagic5/LibApplications CFLAGS="%{WILD_OPT_FLAGS}"

##Build sample applications
make CFG=ReleaseDynamic -f makefile.wm5 -C WildMagic5/SampleGraphics -j1
make CFG=ReleaseDynamic -f makefile.wm5 -C WildMagic5/SamplePhysics -j1
make CFG=ReleaseDynamic -f makefile.wm5 -C WildMagic5/SampleImagics -j1
make CFG=ReleaseDynamic -f makefile.wm5 -C WildMagic5/SampleMathematics -j1

%install
#make install DESTDIR=$RPM_BUILD_ROOT
##Manual installation

mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}/WildMagic
mkdir -p $RPM_BUILD_ROOT%{_datadir}/WildMagic/SampleImagics
mkdir -p $RPM_BUILD_ROOT%{_datadir}/WildMagic/SampleMathematics
mkdir -p $RPM_BUILD_ROOT%{_datadir}/WildMagic/SampleGraphics/BlendedAnimations
mkdir -p $RPM_BUILD_ROOT%{_datadir}/WildMagic/SamplePhysics/SimplePendulum/Data
cp -a WildMagic5/SDK/Library/ReleaseDynamic/*.so* $RPM_BUILD_ROOT%{_libdir}
cp -a WildMagic5/SDK/Include/* $RPM_BUILD_ROOT%{_includedir}/WildMagic
cp -a WildMagic5/Data $RPM_BUILD_ROOT%{_datadir}/WildMagic

mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/WildMagic/SampleGraphics
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/WildMagic/SamplePhysics
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/WildMagic/SampleImagics
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/WildMagic/SampleMathematics

######################Install additional data files################################
cp -a WildMagic5/SampleGraphics/BlendedAnimations/Data $RPM_BUILD_ROOT%{_datadir}/WildMagic/BlendedAnimations
cp -a WildMagic5/SampleGraphics/BlendedTerrain/Shaders $RPM_BUILD_ROOT%{_datadir}/WildMagic/BlendedTerrain
cp -a WildMagic5/SampleGraphics/BumpMaps/Shaders $RPM_BUILD_ROOT%{_datadir}/WildMagic/BumpMaps
cp -a WildMagic5/SampleGraphics/Castle/Shaders $RPM_BUILD_ROOT%{_datadir}/WildMagic/SampleGraphics/Castle
cp -a WildMagic5/SampleGraphics/Castle/Geometry $RPM_BUILD_ROOT%{_datadir}/WildMagic/SampleGraphics/Castle
cp -a WildMagic5/SampleGraphics/Castle/Textures $RPM_BUILD_ROOT%{_datadir}/WildMagic/SampleGraphics/Castle
cp -a WildMagic5/SampleGraphics/CubeMaps/Shaders $RPM_BUILD_ROOT%{_datadir}/WildMagic/SampleGraphics/CubeMaps
cp -a WildMagic5/SampleGraphics/CubeMaps/Data $RPM_BUILD_ROOT%{_datadir}/WildMagic/SampleGraphics/CubeMaps
cp -a WildMagic5/SampleGraphics/GlossMaps/Shaders $RPM_BUILD_ROOT%{_datadir}/WildMagic/SampleGraphics/GlossMaps
cp -a WildMagic5/SampleGraphics/MorphControllers/Data $RPM_BUILD_ROOT%{_datadir}/WildMagic/SampleGraphics/MorphControllers
cp -a WildMagic5/SampleGraphics/MorphFaces/Data $RPM_BUILD_ROOT%{_datadir}/WildMagic/SampleGraphics/MorphFaces
cp -a WildMagic5/SampleGraphics/MultipleRenderTargets/Shaders $RPM_BUILD_ROOT%{_datadir}/WildMagic/SampleGraphics/MultipleRenderTargets
cp -a WildMagic5/SampleGraphics/ProjectedTextures/Shaders $RPM_BUILD_ROOT%{_datadir}/WildMagic/SampleGraphics/ProjectedTextures
cp -a WildMagic5/SampleGraphics/ShadowMaps/Shaders $RPM_BUILD_ROOT%{_datadir}/WildMagic/SampleGraphics/ShadowMaps
cp -a WildMagic5/SampleGraphics/SkinnedBiped/Data $RPM_BUILD_ROOT%{_datadir}/WildMagic/SampleGraphics/SkinnedBiped
cp -a WildMagic5/SampleGraphics/Skinning/Shaders $RPM_BUILD_ROOT%{_datadir}/WildMagic/SampleGraphics/Skinning
cp -a WildMagic5/SampleGraphics/SphereMaps/Shaders $RPM_BUILD_ROOT%{_datadir}/WildMagic/SampleGraphics/SphereMaps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/WildMagic/SampleGraphics/Terrains/Data
cp -a WildMagic5/SampleGraphics/Terrains/Data/* $RPM_BUILD_ROOT%{_datadir}/WildMagic/SampleGraphics/Terrains/Data
cp -a WildMagic5/SampleGraphics/Terrains/Shaders $RPM_BUILD_ROOT%{_datadir}/WildMagic/SampleGraphics/Terrains
cp -a WildMagic5/SampleGraphics/VolumeFog/Shaders $RPM_BUILD_ROOT%{_datadir}/WildMagic/SampleGraphics/VolumeFog
cp -a WildMagic5/SampleGraphics/VolumeTextures/Shaders $RPM_BUILD_ROOT%{_datadir}/WildMagic/SampleGraphics/VolumeTextures

cp -a WildMagic5/SampleImagics/GpuGaussianBlur2/Data $RPM_BUILD_ROOT%{_datadir}/WildMagic/SampleImagics/GpuGaussianBlur2
cp -a WildMagic5/SampleImagics/GpuGaussianBlur2/Shaders $RPM_BUILD_ROOT%{_datadir}/WildMagic/SampleImagics/GpuGaussianBlur2
cp -a WildMagic5/SampleImagics/GpuGaussianBlur3/Data $RPM_BUILD_ROOT%{_datadir}/WildMagic/SampleImagics/GpuGaussianBlur3
cp -a WildMagic5/SampleImagics/GpuGaussianBlur3/Shaders $RPM_BUILD_ROOT%{_datadir}/WildMagic/SampleImagics/GpuGaussianBlur3

cp -a WildMagic5/SampleMathematics/BSplineFitContinuous/Data $RPM_BUILD_ROOT%{_datadir}/WildMagic/SampleMathematics/BSplineFitContinuous
mkdir -p $RPM_BUILD_ROOT%{_datadir}/WildMagic/SampleMathematics/DistancePointEllipseEllipsoid

mkdir -p $RPM_BUILD_ROOT%{_datadir}/WildMagic/SampleMathematics/NonlocalBlowup/Data
cp -a WildMagic5/SampleMathematics/NonlocalBlowup/Data/* $RPM_BUILD_ROOT%{_datadir}/WildMagic/SampleMathematics/NonlocalBlowup/Data

mkdir -p $RPM_BUILD_ROOT%{_datadir}/WildMagic/SampleMathematics/GeodesicHeightField/Data
cp -a WildMagic5/SampleMathematics/GeodesicHeightField/Data/* $RPM_BUILD_ROOT%{_datadir}/WildMagic/SampleMathematics/GeodesicHeightField/Data

cp -a WildMagic5/SampleGraphics/BlendedAnimations/Data $RPM_BUILD_ROOT%{_datadir}/WildMagic/SampleGraphics/BlendedAnimations
cp -p WildMagic5/SampleGraphics/BlendedTerrain/Shaders/BlendedTerrain.wmfx $RPM_BUILD_ROOT%{_datadir}/WildMagic/Data/Im
cp -p WildMagic5/SampleGraphics/BumpMaps/Shaders/SimpleBumpMap.wmfx $RPM_BUILD_ROOT%{_datadir}/WildMagic/Data/Im

pushd WildMagic5/SampleGraphics/BlendedAnimations/Data
	for i in `find . -type f \( -name "*.bmp" \)`; do
	cp -a $i $RPM_BUILD_ROOT%{_datadir}/WildMagic/Data/Bmp
	done
	for i in `find . -type f \( -name "*.txt" \)`; do
	cp -a $i $RPM_BUILD_ROOT%{_datadir}/WildMagic/Data/Wmfx
	done
	for i in `find . -type f \( -name "*.wmtf" \)`; do
	cp -a $i $RPM_BUILD_ROOT%{_datadir}/WildMagic/Data/Wmtf
	done
popd
pushd WildMagic5/SampleGraphics/BlendedTerrain/Shaders
	for i in `find . -type f \( -name "*.fx" \)`; do
	cp -a $i $RPM_BUILD_ROOT%{_datadir}/WildMagic/Data/CgShaders
	done
	for i in `find . -type f \( -name "*.wmtf" \)`; do
	cp -a $i $RPM_BUILD_ROOT%{_datadir}/WildMagic/Data/Wmtf
	done
popd
pushd WildMagic5/SampleGraphics/BumpMaps/Shaders
	for i in `find . -type f \( -name "*.fx" \)`; do
	cp -a $i $RPM_BUILD_ROOT%{_datadir}/WildMagic/Data/CgShaders
	done
	for i in `find . -type f \( -name "*.wmtf" \)`; do
	cp -a $i $RPM_BUILD_ROOT%{_datadir}/WildMagic/Data/Wmtf
	done
popd
#####################################################################################

###Make sample scripts of graphics, 
###mathematics, physics, and image analysis
##
##SamplePhysics
rm -f WildMagic5/SamplePhysics/*.wm5
for bin in `ls WildMagic5/SamplePhysics`; do
	mv WildMagic5/SamplePhysics/${bin}/${bin}.ReleaseDynamic $RPM_BUILD_ROOT%{_libexecdir}/WildMagic/SamplePhysics
	rm -fr $RPM_BUILD_ROOT%{_libexecdir}/WildMagic/SamplePhysics/${bin}
	cat > $RPM_BUILD_ROOT%{_libexecdir}/WildMagic/SamplePhysics/${bin} <<EOF
#!/bin/sh
export WM5_PATH=%{_datadir}/WildMagic
exec %{_libexecdir}/WildMagic/SamplePhysics/${bin}.ReleaseDynamic "\$@"
EOF
    chmod +x $RPM_BUILD_ROOT%{_libexecdir}/WildMagic/SamplePhysics/${bin}
done

##SampleGraphics
rm -f WildMagic5/SampleGraphics/*.wm5
mv WildMagic5/SampleGraphics/ReflectionsAndShadows WildMagic5/SampleGraphics/ReflectionsAndShadow
for bin in `ls WildMagic5/SampleGraphics`; do
	mv WildMagic5/SampleGraphics/${bin}/${bin}.ReleaseDynamic $RPM_BUILD_ROOT%{_libexecdir}/WildMagic/SampleGraphics/${bin}.ReleaseDynamic
	rm -fr $RPM_BUILD_ROOT%{_libexecdir}/WildMagic/SampleGraphics/${bin}
	cat > $RPM_BUILD_ROOT%{_libexecdir}/WildMagic/SampleGraphics/${bin} <<EOF
#!/bin/sh
export WM5_PATH=%{_datadir}/WildMagic
exec %{_libexecdir}/WildMagic/SampleGraphics/${bin}.ReleaseDynamic "\$@"
EOF
    chmod +x $RPM_BUILD_ROOT%{_libexecdir}/WildMagic/SampleGraphics/${bin}
done

##SampleImagics
rm -f WildMagic5/SampleImagics/*.wm5
for bin in `ls WildMagic5/SampleImagics`; do
	mv WildMagic5/SampleImagics/${bin}/${bin}.ReleaseDynamic $RPM_BUILD_ROOT%{_libexecdir}/WildMagic/SampleImagics/${bin}.ReleaseDynamic
	rm -fr $RPM_BUILD_ROOT%{_libexecdir}/WildMagic/SampleImagics/${bin}
	cat > $RPM_BUILD_ROOT%{_libexecdir}/WildMagic/SampleImagics/${bin} <<EOF
#!/bin/sh
export WM5_PATH=%{_datadir}/WildMagic
exec %{_libexecdir}/WildMagic/SampleImagics/${bin}.ReleaseDynamic "\$@"
EOF
    chmod +x $RPM_BUILD_ROOT%{_libexecdir}/WildMagic/SampleImagics/${bin}
done

##SampleMathematics
rm -f WildMagic5/SampleMathematics/*.wm5
for bin in `ls WildMagic5/SampleMathematics`; do
	mv WildMagic5/SampleMathematics/${bin}/${bin}.ReleaseDynamic $RPM_BUILD_ROOT%{_libexecdir}/WildMagic/SampleMathematics/${bin}.ReleaseDynamic
	rm -fr $RPM_BUILD_ROOT%{_libexecdir}/WildMagic/SampleMathematics/${bin}
	cat > $RPM_BUILD_ROOT%{_libexecdir}/WildMagic/SampleMathematics/${bin} <<EOF
#!/bin/sh
export WM5_PATH=%{_datadir}/WildMagic
exec %{_libexecdir}/WildMagic/SampleMathematics/${bin}.ReleaseDynamic "\$@"
EOF
    chmod +x $RPM_BUILD_ROOT%{_libexecdir}/WildMagic/SampleMathematics/${bin}
done
########################################################################################

%ldconfig_scriptlets

%files
%license WildMagic5/License/LICENSE_1_0.txt
%doc WildMagic5/Documentation/WildMagic5Overview.pdf
%{_libdir}/*.so.*

%files devel
%{_includedir}/WildMagic/
%{_libdir}/*.so

%files samples
%{_libexecdir}/WildMagic/

%files data
%doc WildMagic5/Documentation/*.txt
%doc WildMagic5/Documentation/Wm5InitTerm.pdf
%license WildMagic5/License/LICENSE_1_0.txt
%{_datadir}/WildMagic/

%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.17-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.17-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.17-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 28 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.17-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild
- Undefine _package_note_file

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.17-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.17-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.17-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.17-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.17-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 12 2019 Antonio Trande <sagitter@fedoraproject.org> - 5.17-7
- Re-define linker flags

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 22 2018 Antonio Trande <sagitter@fedoraproject.org> - 5.17-4
- Add gcc-c++ BR

* Sat Feb 17 2018 Antonio Trande <sagitter@fedoraproject.org> - 5.17-3
- Use %%ldconfig_scriptlets

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 13 2017 Antonio Trande <sagitter@fedoraproject.org> - 5.17-1
- Update to 5.17

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 09 2017 Antonio Trande <sagitter@fedoraproject.org> - 5.15-1
- Update to 5.15

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Antonio Trande <sagitter@fedoraproject.org> - 5.14-1
- Update to 5.14

* Thu Dec 10 2015 Antonio Trande <sagitter@fedoraproject.org> - 5.13-13
- Fix compilation flags of 'libWm5Applications.so' library

* Wed Nov 04 2015 Antonio Trande <sagitter@fedoraproject.org> - 5.13-12
- Rebuild with -fPIC

* Sat Oct 31 2015 Antonio Trande <sagitter@fedoraproject.org> - 5.13-11
- Hardened builds on <F23

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 29 2015 Antonio Trande <sagitter@fedoraproject.org> - 5.13-9
- Added global ldflags
- Defined global ldflags macro for EPEL6

* Tue Apr 28 2015 Antonio Trande <sagitter@fedoraproject.org> - 5.13-8
- Added DistancePointEllipseEllipsoid patch

* Sat Apr 25 2015 Antonio Trande <sagitter@fedoraproject.org> - 5.13-7
- Fixed script's arguments
- Installed additional data files for execution of the samples

* Sat Apr 18 2015 Antonio Trande <sagitter@fedoraproject.org> - 5.13-6
- Packaged some data files needed to graphic tests

* Sat Apr 18 2015 Antonio Trande <sagitter@fedoraproject.org> - 5.13-5
- Removed source code from Sample* directories
- Packaged PDF documentation in the data sub-package

* Thu Apr 16 2015 Antonio Trande <sagitter@fedoraproject.org> - 5.13-4
- %%build section re-arranged
- Set LDFLAGS/CFLAGS separately
- Built samples sub-package

* Tue Apr 14 2015 Antonio Trande <sagitter@fedoraproject.org> - 5.13-3
- Set LDFLAGS

* Sun Apr 12 2015 Antonio Trande <sagitter@fedoraproject.org> - 5.13-2
- Fixed BR packages
- Set C/C++ optimization flags

* Sun Apr 12 2015 Antonio Trande <sagitter@fedoraproject.org> - 5.13-1
- First package
