%define _lto_cflags %{nil}
# Upstream does not maintain a soversion so we define one here.
# abi-compliance-checker or fedabipkgdiff can be used to determine if an abi
# breakage occurs in which case the  soversion shall be incremented.
%global sover 0.4
%global upname OpenCOLLADA

Name:           openCOLLADA
Version:        1.6.70
Release:        2%{?dist}
License:        MIT
Summary:        Collada 3D import and export libraries
URL:            https://github.com/RemiArnaud/OpenCOLLADA/

Source0:        https://github.com/RemiArnaud/OpenCOLLADA/archive/v%{version}-maya/%{upname}-%{version}.tar.gz

# Force a soversion.
Patch0:         OpenCOLLADA-cmake.patch
Patch1:         OpenCOLLADA-pcre.patch
Patch2:         openCOLLADA-daevalidator.patch

BuildRequires:  cmake gcc-c++
BuildRequires:  dos2unix
BuildRequires:  fftw-devel
BuildRequires:  pcre-devel
BuildRequires:  zlib-devel
BuildRequires:  libxml2-devel

%description 
COLLADA is a royalty-free XML schema that enables digital asset
exchange within the interactive 3D industry.
OpenCOLLADA is a Google summer of code opensource project providing
libraries for 3D file interchange between applications like blender.
COLLADABaseUtils          Utils used by many of the other projects
COLLADAFramework          Datamodel used to load COLLADA files
COLLADAStreamWriter       Sources (Library to write COLLADA files)
COLLADASaxFrameworkLoader Library that loads COLLADA files in a sax
                          like manner into the framework data model
COLLADAValidator          XML validator for COLLADA files, based on
                          the COLLADASaxFrameworkLoader
GeneratedSaxParser        Library used to load xml files in the way
                          used by COLLADASaxFrameworkLoader

%package        doc
Summary:        Developer documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description doc
This package provides documentation for %{name}.

%package        devel
Summary:        Include files for openCOLLADA development
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the include files necessary to build and
develop with the %{name} export and import libraries.

%package        utils
Summary:        XML validator for COLLADA files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description utils
XML validator for COLLADA files, based on the COLLADASaxFrameworkLoader.


%prep
%autosetup -p1 -n %{upname}-%{version}-maya

# Remove unused bundled libraries
rm -rf Externals/{Cg,expat,lib3ds,LibXML,MayaDataModel,pcre,zlib,zziplib}

# Add some docs, need to fix eol encoding with dos2unix in some files.
find ./ -name .project -delete
cp -pf COLLADAStreamWriter/README README.COLLADAStreamWriter
cp -pf COLLADAStreamWriter/LICENSE ./

iconv -f ISO_8859-1 -t utf-8 COLLADAStreamWriter/AUTHORS > \
  COLLADAStreamWriter/AUTHORS.tmp
touch -r COLLADAStreamWriter/AUTHORS COLLADAStreamWriter/AUTHORS.tmp
mv COLLADAStreamWriter/AUTHORS.tmp COLLADAStreamWriter/AUTHORS

dos2unix -f -k README.COLLADAStreamWriter
dos2unix -f -k LICENSE
dos2unix -f -k README
find htdocs/ -name *.php -exec dos2unix -f {} \;
find htdocs/ -name *.css -exec dos2unix -f {} \;


%build
%cmake -DUSE_STATIC=OFF \
       -DUSE_SHARED=ON \
       -Dsoversion=%{sover} \
       -DCMAKE_SKIP_RPATH=ON \
       -DCMAKE_BUILD_TYPE="RelWithDebInfo"

%cmake_build


%install
%cmake_install

# Manually install validator binaries
mkdir -p %{buildroot}%{_bindir}/
install -pm 0755 %{_vpath_builddir}/bin/*Validator %{buildroot}%{_bindir}/

# Install MathMLSolver headers
mkdir -p %{buildroot}%{_includedir}/MathMLSolver
cp -a Externals/MathMLSolver/include/* %{buildroot}%{_includedir}/MathMLSolver/


%{?ldconfig_scriptlets}


%files
%doc README README.COLLADAStreamWriter COLLADAStreamWriter/AUTHORS
%license LICENSE
%{_libdir}/lib*.so.%{sover}

%files doc
%doc htdocs/

%files devel
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_includedir}/*

%files utils
%{_bindir}/*


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.70-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jan 30 2022 Richard Shaw <hobbes1069@gmail.com> - 1.6.70-1
- Update to 1.6.70.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.68-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.68-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.68-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 11 2020 Richard Shaw <hobbes1069@gmail.com> - 1.6.68-1
- Update to 1.6.68.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.63-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.63-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.63-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.63-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.63-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Petr Pisar <ppisar@redhat.com> - 1.6.63-2
- Rebuild against patched libpcreposix library (bug #1667614)

* Sun Jul 22 2018 Richard Shaw <hobbes1069@gmail.com> - 1.6.63-1
- Update to 1.6.63.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.62-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 07 2018 Richard Shaw <hobbes1069@gmail.com> - 1.6.62-2
- Fix utils package dependency on libDAEValidatorLibrary.

* Tue Mar 27 2018 Richard Shaw <hobbes1069@gmail.com> - 1.6.62-1
- Update to 1.6.62.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-30.gitcaad49c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-29.gitcaad49c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-28.gitcaad49c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-27.gitcaad49c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 12 2016 Richard Shaw <hobbes1069@gmail.com> - 0-26.gitcaad49c
- Update to latest git checkout.
- Add patch for ARM narrowing error for GCC 6 on rawhide.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-25.git3335ac1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jul 25 2015 Richard Shaw <hobbes1069@gmail.com> - 0-24.git3335ac1
- Update to git checkout which works with blender 2.75.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-23.git69b844d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 13 2015 David Tardon <dtardon@redhat.com> - 0-22.git69b844d
- rebuild for yet another C++ ABI break

* Fri Feb 27 2015 David Tardon <dtardon@redhat.com> - 0-21.git69b844d
- rebuild for gcc5 C++ ABI change

* Thu Oct 09 2014 Sandro Mani <manisandro@gmail.com> - 0-20.git69b844d
- Add patch for missing includes which causes blender FTBFS

* Fri Sep  5 2014 Richard Shaw <hobbes1069@gmail.com> - 0-19.git69b844d
- Update to lastest git checkout.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-18.git9665d16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-17.git9665d16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-16.git9665d16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 09 2013 Richard Shaw <hobbes1069@gmail.com> - 0-15
- Update to latest upstream checkout. Required for blender 2.67.
- Add support for EPEL 6 build.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-14.svn871
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-13.svn871
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 18 2012 Richard Shaw <hobbes1069@gmail.com> - 0-12.svn871
- Update to latest svn.
- Add MathMLSolver includes.

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 0-11.svn864
- Rebuild against PCRE 8.30

* Thu Jan 05 2012 Richard Shaw <hobbes1069@gmail.com> - 0-10
- Rebuild for GCC 4.7.0.
- Change how library soversion is set and test for abi breakages.
- Fix overriding of required build flags.

* Wed Oct 26 2011 Richard Shaw <hobbes1069@gmail.com> - 0-9
- Update to svn revision 864.

* Wed Oct 26 2011 Richard Shaw <hobbes1069@gmail.com> - 0-8
- Update to svn revision 863.
- Fix typo in spec file.

* Thu Oct 06 2011 Richard Shaw <hobbes1069@gmail.com> - 0-6
- Update to svn revision 847.

* Wed Apr 27 2011 Richard Shaw <hobbes1069@gmail.com> - 0-5
- Created -utils and -doc sub-packages.
- Corrected installation location of -devel header files.

* Wed Apr 27 2011 Richard Shaw <hobbes1069@gmail.com> - 0-4
- Move from scons to cmake for building.
- Various other fixes.

* Thu Apr 21 2011 Richard Shaw <hobbes1069@gmail.com> - 0-3
- Switched from expat to libxml2 for xml support.
- Updated to svn838

* Fri Apr 15 2011 Richard Shaw <hobbes1069@gmail.com> - 0-2
- Updated spec file for better packaging compliance
- Fixed some rpmlint warnings

* Tue Apr 12 2011 Richard Shaw <hobbes1069@gmail.com> - 0-1
- Updated spec file for Fedora packaging compliance

* Thu Mar 31 2011 davejplater@gmail.com
- Update to svn836
- Upstream changes :
  * fix validation preprocessor flag
  * inti member variables
  * fix uri copy ctor, add missing includes
  * replace asserts
  * fix import
  * fix crash in utf conversion with recent gcc
  * replace asserts by custom assert

* Fri Feb 11 2011 davejplater@gmail.com
- Update to svn827
- Upstream changes:
  * fix Issue 125: cgfx shader source file is not honoring the
  search path on export.
  * fix Issue 89: CONTINUITY semantic is not defined. Define all
  semantics in COLLADASWInputList.h
  * partially fix Issue 71: wrong opacity for effects without set
  transparency
  * fix Issue 65: COLLADASaxFWL::Loader::loadDocument() don't check
  if the file correctly loads
  * fix Issue 62: build fixes for linux (gcc 4.4.3)
  * ignore bin and lib folder in pcre
  * Issue 35: IWriter start, cancel, and finish methods not called
  * remove precompiled pcre pattern from source
  * fix Issue 122: Root::loadDocument("../a/b/c.dae") attempts to
  open "../a/a/b/c.dae"
  * Issue 145: std::terminate() while loading lightwave dae through
  OpenCOLLADAValidator
  * fix Issue 146: OpenCOLLADAValidator crash
  COLLADASaxFWL::LibraryEffectsLoader::handleTexture
  * fix Issue 151: CMakeLists.txt overwrites custom CMAKE_CXX_FLAGS
  * Issue 153: crash in <articulated_system> improvements in
  kinematics loader related to mathml

* Fri Jan  7 2011 davejplater@gmail.com
- Spec file change to fix SLE_11_SP1 build made by repabuild.

* Mon Dec 27 2010 davejplater@gmail.com
- Update to svn788
- Upstream changes
  * fix Issue 148: Glitch in ftoa and dtoa (rename variables)

* Mon Nov 22 2010 davejplater@gmail.com
- Update to svn785
- Prevent build of dae2ogre with openCOLLADA-nodae2ogre.patch
- Upstream changes :
  * apply path from Issue 4: CMake or Scons
  * fix performance issue with many materials
  * fix: do not write empty <extra> element in <profile_COMMON>
  * apply patch (only first change) provided in Issue 136: Fix for
  color sets not exporting in colladaMaya
  * fix Issue 137: SetParam does not properly export float<n> with
  0's in it

* Sat Nov  6 2010 davejplater@gmail.com
- Update to svn 779 Removed openCOLLADA-assign_value.patch which is
  already incorporated in this revision.
- Upstream changes :
  * fix Issue 126: cgfx shader source file is not honoring the search
  path on export.
  * apply patch provided in Issue 4: CMake or Scons (add cmake files)
  * fix Issue 132: Small fix from compiling blender - collada with
  - Wall -Werror
  * fix Issue 131: Gcc will be initialized after warning fixes

* Tue Oct 26 2010 pth@suse.de
- Actually assign the passed value in setter function.
- Manually strip libraries

* Sun Oct 24 2010 davejplater@gmail.com
- Added patch COLLADA-linuxbuild.patch to fix shared lib build includes.
- Added patch openCOLLADA-buildflags.patch for optflags.
- Added patch openCOLLADA-soname.patch to add sonames to libs.

* Mon Oct 18 2010 davejplater@gmail.com
- Created new package openCOLLADA needed by blender-2.5x
- OpenCOLLADA is a stream based reader and writer library for
  COLLADA files. support@opencollada.org
