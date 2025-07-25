Name:      percolator
Summary:   Software for postprocessing of shotgun proteomics data
Version:   3.08
Release:   %autorelease

## Code under src/ (except RAMP) is licensed under a ASL 2.0 license.
## Code under src/converters/MSToolkit/RAMP is licensed under a LGPLv2+ license.
License:   Apache-2.0 AND LGPL-2.0-or-later
URL:       https://github.com/percolator/percolator
Source0:   https://github.com/percolator/percolator/archive/rel-3-08/percolator-rel-3-08.tar.gz

BuildRequires: make
BuildRequires: gcc, gcc-c++
BuildRequires: cmake

# Needed for testing
BuildRequires: gtest-devel
BuildRequires: eigen3-devel
BuildRequires: python3-devel
BuildRequires: boost-static, boost-devel
BuildRequires: pkgconfig(tokyocabinet)
BuildRequires: pkgconfig(xerces-c)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(libtirpc)
BuildRequires: xsd, zlib-devel, bzip2-devel

Patch0: percolator-unbundle_eigen_gtest.patch

Requires: %{name}-data = %{version}-%{release}
Obsoletes: fido-pi = 0:0

%description
The first step in analyzing an mass spectrometry assay is to match
the harvested spectra against a target database 
using database search engines such as Sequest and Mascot,
a process that renders list of peptide-spectrum matches.
However, it is not trivial to assess the accuracy
of these identifications.

Percolator uses a semi-supervised machine learning to 
discriminate correct from incorrect peptide-spectrum matches,
and calculates accurate statistics such as q-value (FDR)
and posterior error probabilities.

%package data
Summary: percolator data files
BuildArch: noarch
Requires: xml-common

%description data
This package contains XSD data files of %{name} and
models of elude tool.

%package static
Summary: percolator static libraries

%description static
This package contains static libraries of %{name}.

%prep
%autosetup -n percolator-rel-3-08 -N

%patch -P 0 -p1 -b .backup

## Remove spurious executable permissions
find . -type f -name "*.cpp" -exec chmod 0644 '{}' \;
find . -type f -name "*.h" -exec chmod 0644 '{}' \;
find . -type f -name "*.xx" -exec chmod 0644 '{}' \;
find . -type f -name "*.txt" -exec chmod 0644 '{}' \;

# Remove bundled files
rm -rf percolator/_deps/*

## Rename additional readme files
chmod a-x src/converters/MSToolkit/RAMP/README
mv src/converters/MSToolkit/RAMP/README src/converters/MSToolkit/RAMP/RAMP-README
mv src/converters/MSToolkit/RAMP/Readme.Mike.txt src/converters/MSToolkit/RAMP/RAMP-Readme.Mike.txt

## Set 'qvality' destination directory
sed -e 's|./bin|bin|g' -i src/qvality/CMakeLists.txt

%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
mkdir -p percolator
%cmake -Wno-dev -B percolator -S ./ \
 -DCMAKE_COLOR_MAKEFILE:BOOL=ON \
 -DCMAKE_VERBOSE_MAKEFILE=TRUE -DXML_SUPPORT:BOOL=ON \
 -DCMAKE_CXX_FLAGS_RELEASE:STRING="%{optflags} -Isrc -I%{_includedir}/xsd/cxx/tree -I%{_includedir}/tirpc -I%{_includedir}/eigen3" \
 -DCMAKE_EXE_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} -ltirpc" \
 -DCMAKE_BUILD_TYPE:STRING=Release -DBUILD_TESTING:BOOL=ON \
 -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES -DCMAKE_SKIP_RPATH:BOOL=YES \
 -DTARGET_ARCH=%{_arch}

### XSD files ran maually
### In Fedora 'xsd' executable is 'xsdcxx'
xsdcxx cxx-tree --generate-insertion XDR --generate-extraction XDR --root-element-all \
 --namespace-map http://per-colator.com/percolator_in/13=percolatorInNs src/xml/percolator_in.xsd

xsdcxx cxx-tree --generate-serialization --generate-insertion XDR --generate-extraction XDR --root-element-all \
 --namespace-map http://per-colator.com/percolator_out/15=percolatorOutNs src/xml/percolator_out.xsd
###

%define _vpath_builddir percolator
%cmake_build

mkdir -p src/fido
%cmake -Wno-dev -B src/fido \
 -DCMAKE_COLOR_MAKEFILE:BOOL=ON \
 -DCMAKE_VERBOSE_MAKEFILE=TRUE \
 -DCMAKE_BUILD_TYPE:STRING=Release \
 -DTokyoCabinet_INCLUDE_DIR=%{_includedir} \
 -DTokyoCabinet_LIBRARY=%{_libdir}/libtokyocabinet.so \
 -DCMAKE_CXX_FLAGS_RELEASE:STRING="%{optflags} -Isrc -I%{_includedir}/xsd/cxx/tree -I%{_includedir}/tirpc -I%{_includedir}/eigen3" \
 -DCMAKE_EXE_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} -ltirpc" \
 -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES -DCMAKE_SKIP_RPATH:BOOL=YES \
 -DTARGET_ARCH=%{_arch} -DBUILD_TESTING:BOOL=ON
 
%define _vpath_builddir src/fido
%cmake_build

mkdir -p src/converters
%cmake -Wno-dev -B src/converters \
 -DCMAKE_COLOR_MAKEFILE:BOOL=ON \
 -DCMAKE_VERBOSE_MAKEFILE=TRUE \
 -DCMAKE_CXX_FLAGS_RELEASE:STRING="%{optflags} -Isrc -I%{_includedir}/xsd/cxx/tree -I%{_includedir}/tirpc -I%{_includedir}/eigen3" \
 -DCMAKE_EXE_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} -ltirpc" \
 -DCMAKE_BUILD_TYPE:STRING=Release \
 -DPERCOLATOR-CONVERTERS_BINARY_DIR:STATIC=converters \
 -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES -DCMAKE_SKIP_RPATH:BOOL=YES \
 -DTokyoCabinet_INCLUDE_DIR=%{_includedir} \
 -DTokyoCabinet_LIBRARY=%{_libdir}/libtokyocabinet.so \
 -DSERIALIZE="TokyoCabinet" \
 -DTARGET_ARCH=%{_arch} -DBUILD_TESTING:BOOL=ON

### XSD files ran maually
### In Fedora 'xsd' executable is 'xsdcxx'
xsdcxx cxx-tree --generate-serialization --generate-insertion XDR --generate-extraction XDR --root-element-all \
 --namespace-map http://per-colator.com/percolator_in/13=percolatorInNs src/xml/percolator_in.xsd

xsdcxx cxx-tree --generate-serialization --generate-insertion XDR --generate-extraction XDR --root-element-all \
 --namespace-map http://per-colator.com/percolator_out/15=percolatorOutNs src/xml/percolator_out.xsd
##
xsdcxx cxx-tree --generate-serialization --generate-insertion XDR --generate-extraction XDR --root-element-all \
 --namespace-map http://psidev.info/psi/pi/mzIdentML/1.1=mzIdentML_ns src/xml/mzIdentML1.1.0.xsd

xsdcxx cxx-tree --generate-serialization --generate-insertion XDR --generate-extraction XDR --root-element-all \
 --namespace-map http://www.bioml.com/gaml/=gaml_tandem_ns src/xml/gaml_tandem1.0.xsd

xsdcxx cxx-tree --generate-serialization --generate-insertion XDR --generate-extraction XDR --root-element-all \
 --namespace-map http://www.thegpm.org/TANDEM/2011.12.01.1=tandem_ns --namespace-map =tandem_ns \
 --namespace-map http://www.bioml.com/gaml/=gaml_tandem_ns src/xml/tandem2011.12.01.1.xsd
###

%define _vpath_builddir src/converters
%cmake_build

%install
%define _vpath_builddir percolator
%cmake_install

%define _vpath_builddir src/converters
%cmake_install

## Install static libraries
mkdir -p %{buildroot}%{_libdir}/percolator
for i in `find . -type f \( -name "*.a" \)`; do
 install -pm 755 $i %{buildroot}%{_libdir}/percolator
done

rm -f %{buildroot}%{_bindir}/gtest_unit

%check
%define _vpath_builddir percolator
# https://github.com/percolator/percolator/issues/354
%ifarch %{ix86}
# nothing
%else
%ctest -VV
%endif

%files
%{_bindir}/percolator
%{_bindir}/qvality

%files data
%doc ReadMe.txt
%doc src/converters/MSToolkit/RAMP/RAMP-*
%license license.txt
%{_datadir}/xml/percolator/

%files static
%doc ReadMe.txt
%doc src/converters/MSToolkit/RAMP/RAMP-*
%license license.txt
%{_libdir}/percolator/

%changelog
%autochangelog
