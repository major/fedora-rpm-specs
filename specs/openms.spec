%bcond_with check
%bcond_with debug

ExclusiveArch: %{qt6_qtwebengine_arches}

# Python binding
%global with_pyOpenMS 1
#

# Filter private libraries
%global __provides_exclude ^(%%(find %{buildroot}%{_libdir}/OpenMS -name '*.so' | xargs -n1 basename | sort -u | paste -s -d '|' -))
%global __requires_exclude ^(%%(find %{buildroot}%{_libdir}/OpenMS -name '*.so' | xargs -n1 basename | sort -u | paste -s -d '|' -))

%global commit b886c44b4ca0625932f9874613918856774cfd8d
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20250722

Name:      openms
Summary:   LC/MS data management and analyses
Version:   3.4.1
Epoch:     2
Release:   %autorelease -s %{date}git%{shortcommit}
# BSD-3-Clause is the main license
# Apache-2.0, CC-BY-4.0 and CC0-1.0 are coming from TDL directory
License:   BSD-3-Clause AND Apache-2.0 AND CC-BY-4.0 AND CC0-1.0
URL:       http://www.openms.de/
#Source0:   https://github.com/OpenMS/OpenMS/archive/Release%%{version}/OpenMS-release-%%{version}.tar.gz
Source0:   https://github.com/OpenMS/OpenMS/archive/%{commit}/OpenMS-%{commit}.tar.gz

##TOPPView, TOPPAS, INIFileEditor .desktop and icon files
Source1:   https://raw.githubusercontent.com/OpenMS/OpenMS/develop/src/openms_gui/source/VISUAL/ICONS/TOPPView.png
Source2:   https://raw.githubusercontent.com/OpenMS/OpenMS/develop/src/openms_gui/source/VISUAL/ICONS/TOPPAS.png
Source3:   https://raw.githubusercontent.com/OpenMS/OpenMS/develop/src/openms_gui/source/VISUAL/ICONS/INIFileEditor.png
Source4:   inifileeditor.desktop

BuildRequires: make
BuildRequires: cmake
BuildRequires: patchelf
BuildRequires: coin-or-Cbc-devel
BuildRequires: coin-or-Cgl-devel
BuildRequires: coin-or-Clp-devel
BuildRequires: coin-or-CoinUtils-devel
BuildRequires: coin-or-Osi-devel
BuildRequires: hdf5-devel
BuildRequires: libsvm-devel
BuildRequires: gcc-c++
BuildRequires: gsl-devel
BuildRequires: glpk-devel
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtsvg-devel
BuildRequires: qt6-qtwebengine-devel
BuildRequires: xerces-c-devel
BuildRequires: boost-devel
BuildRequires: sqlite-devel
BuildRequires: wildmagic5-devel
BuildRequires: zlib-devel
BuildRequires: bzip2-devel
BuildRequires: tbb-devel
BuildRequires: eigen3-devel
BuildRequires: desktop-file-utils
BuildRequires: percolator
BuildRequires: libappstream-glib
BuildRequires: yaml-cpp-devel >= 0.8.0
Requires:      qt6-qtdeclarative-devel%{?_isa}

# Build documentation
# Doxygen useful only on SVN versions  
BuildRequires: doxygen, dos2unix, graphviz
BuildRequires: texlive, texlive-a4wide, texlive-xtab

# Xvfb is needed to run a virtual X server used by some tests
BuildRequires: xorg-x11-server-Xvfb, gnuplot, gawk

Requires: percolator%{?_isa}
Requires: %{name}-data%{?_isa} = 2:%{version}-%{release}
Requires: R-core%{?_isa}

# Remove -O0 flag for tests compiling
Patch0: %{name}-remove_testflag.patch

Patch1: %{name}-3.2.0-bz2254779.patch
Patch3: %{name}-bug7907.patch


%description
OpenMS is a C++ library for LC-MS data management and analyses.
It offers an infrastructure for the rapid development of mass spectrometry
related software. OpenMS is free software available under the three clause BSD
license and runs under Windows, MacOSX and Linux.

It comes with a vast variety of pre-built and ready-to-use tools for proteomics
and metabolomics data analysis (TOPPTools) and
powerful 2D and 3D visualization(TOPPView).

OpenMS offers analyses for various quantitation protocols,
including label-free quantitation, SILAC, iTRAQ, SRM, SWATH, etc.

It provides built-in algorithms for de-novo identification and database search,
as well as adapters to other state-of-the art tools like Mascot, OMSSA, etc.
It supports easy integration of OpenMS built tools into workflow engines like
Knime, Galaxy, WS-Pgrade, and TOPPAS via the TOPPtools concept and
a unified parameter handling via a 'common tool description' (CTD) scheme.

The OpenMS Proteomics Pipeline is a pipeline for 
the analysis of HPLC-MS data. 
It consists of several small applications that 
can be chained to create analysis pipelines tailored 
for a specific problem.

The TOPP tools are divided into several subgroups:
 
 - Graphical Tools
 - File Handling
 - Signal Processing and Preprocessing
 - Quantitation
 - Map Alignment
 - Protein/Peptide Identification
 - Protein/Peptide Processing
 - Targeted Experiments
 - Peptide Property Prediction
 - Misc

%package utilities
Summary: OpenMS utilities
Requires: %{name}-data%{?_isa} = 2:%{version}-%{release}
Obsoletes: %{name}-tools < 2:%{version}-%{release}
%description utilities
Besides TOPP, OpenMS offers a range of utilities. 
They are not included in TOPP as they are not part of 
typical analysis pipelines, but they still might be 
very helpful to you.

The Utilities are divided into several subgroups:
 
 - Maintenance
 - Signal Processing and Preprocessing
 - File handling
 - Algorithm evaluation
 - Peptide identification
 - Quantitation
 - Misc
 - Metabolite identification
 - Quality control

%if 0%{?with_pyOpenMS}
%package -n python3-openms
Summary: Python wrapper for OpenMS
%py_provides python3-%{name}

BuildRequires: python3-setuptools
BuildRequires: python3-devel
BuildRequires: python3-numpy
BuildRequires: python3-autowrap >= 0.23.0
BuildRequires: python3-pip
BuildRequires: python3-cython >= 3.1.0
BuildRequires: python3-wheel
BuildRequires: python3-biopython
BuildRequires: python3-virtualenv
BuildRequires: python3-pandas
BuildRequires: python3-pytest
Requires:      python3-biopython
Requires:      %{name}%{?_isa} = 2:%{version}-%{release}

%description -n python3-openms
This package contains Python3 bindings for a large part of the OpenMS library
for mass spectrometry based proteomics.  It thus provides providing facile 
access to a feature-rich, open-source algorithm library 
for mass-spectrometry based proteomics analysis. 
These Python bindings allow raw access to the data-structures and algorithms 
implemented in OpenMS, specifically those for file access 
(mzXML, mzML, TraML, mzIdentML among others), basic signal processing 
(smoothing, filtering, de-isotoping and peak-picking) and complex data analysis 
(including label-free, SILAC, iTRAQ and SWATH analysis tools).
%endif

%package devel
Summary: OpenMS header files
Requires: %{name}%{?_isa} = 2:%{version}-%{release}
%description devel
OpenMS development files.

%package data
Summary: The OpenMS data files
%description data
The OpenMS data files.

%package doc
Summary: OpenMS documentation
%description doc
HTML documentation of OpenMS.

%prep
%autosetup -N -n OpenMS-%{commit}

%patch -P 0 -p1 -b .backup
%patch -P 1 -p1 -b .backup
%ifarch %{power64}
%patch -P 3 -p1 -b .backup
%endif

# Remove invalid tags
sed -e 's| <project_group></project_group>||g' -i share/OpenMS/DESKTOP/*.appdata.xml


%build
# Likely running out of memory during build
%global _smp_ncpus_max 2

%if %{with debug}
cmake -Wno-dev -DCMAKE_CXX_COMPILER_VERSION:STRING=$(gcc -dumpversion) \
 -DENABLE_UPDATE_CHECK:BOOL=OFF -DGIT_TRACKING:BOOL=OFF \
 -DCMAKE_COLOR_MAKEFILE:BOOL=ON \
 -DENABLE_IPO:BOOL=ON \
 -DCMAKE_CXX_FLAGS_DEBUG:STRING="-DDEBUG -O0 -g %{__global_ldflags}" -DCMAKE_C_FLAGS_DEBUG:STRING="-DDEBUG -O0 -g %{__global_ldflags}" \
 -DCMAKE_BUILD_TYPE=Debug \
 -DBoost_IOSTREAMS_LIBRARY_DEBUG:FILEPATH=%{_libdir}/libboost_iostreams.so \
 -DBoost_MATH_C99_LIBRARY_DEBUG:FILEPATH=%{_libdir}/libboost_math_c99.so \
 -DBoost_REGEX_LIBRARY_DEBUG:FILEPATH=%{_libdir}/libboost_regex.so \
 -DXercesC_LIBRARY_DEBUG:FILEPATH=%{_libdir}/libxerces-c.so \
%else
%cmake -Wno-dev -DCMAKE_CXX_COMPILER_VERSION:STRING=$(gcc -dumpversion) \
 -DGIT_TRACKING:BOOL=OFF \
 -DENABLE_UPDATE_CHECK:BOOL=OFF \
 -DCMAKE_COLOR_MAKEFILE:BOOL=ON \
 -DCMAKE_CXX_FLAGS_RELEASE:STRING="-Wno-cpp %{build_cxxflags} -std=gnu++17" -DCMAKE_C_FLAGS_RELEASE:STRING="-Wno-cpp %{build_cflags} -std=gnu17" \
 -DCMAKE_BUILD_TYPE=Release \
 -DBoost_IOSTREAMS_LIBRARY_RELEASE:FILEPATH=%{_libdir}/libboost_iostreams.so \
 -DBoost_MATH_C99_LIBRARY_RELEASE:FILEPATH=%{_libdir}/libboost_math_c99.so \
 -DBoost_REGEX_LIBRARY_RELEASE:FILEPATH=%{_libdir}/libboost_regex.so \
 -DXercesC_LIBRARY_RELEASE:FILEPATH=%{_libdir}/libxerces-c.so \
%endif
 -DCMAKE_VERBOSE_MAKEFILE=TRUE -DCMAKE_PREFIX_PATH=%{_prefix} \
 -DENABLE_SVN=OFF -DBOOST_USE_STATIC=OFF \
 -DCMAKE_SKIP_RPATH:BOOL=NO -DCMAKE_SKIP_INSTALL_RPATH:BOOL=NO \
 -DMT_ENABLE_OPENMP=ON -DENABLE_GCC_WERROR:BOOL=OFF \
 -DPERCOLATOR_BINARY:FILEPATH=%{_bindir}/percolator \
 -DBOOST_USE_STATIC:BOOL=OFF -DBoost_INCLUDE_DIR:PATH=%{_includedir} \
 -DENABLE_TUTORIALS:BOOL=OFF -DENABLE_UNITYBUILD:BOOL=OFF \
 -DHAS_XSERVER:BOOL=OFF \
 -DCMAKE_INSTALL_PREFIX=%{_prefix} \
 -DINSTALL_BIN_DIR:PATH=bin -DINSTALL_CMAKE_DIR:PATH=%{_lib}/cmake/OpenMS \
 -DINSTALL_DOC_DIR:PATH=share/doc/openms-doc -DINSTALL_INCLUDE_DIR:PATH=include \
 -DINSTALL_LIB_DIR:PATH=%{_lib}/OpenMS -DINSTALL_SHARE_DIR:PATH=share/OpenMS \
 -DPACKAGE_TYPE:STRING=none -DWITH_GUI:BOOL=ON \
 -DXercesC_INCLUDE_DIRS:PATH=%{_includedir}/xercesc \
 -DOPENMS_DISABLE_UPDATE_CHECK:BOOL=OFF -DENABLE_UPDATE_CHECK:BOOL=OFF -DGIT_TRACKING:BOOL=OFF \
 -DFETCHCONTENT_UPDATES_DISCONNECTED:BOOL=ON -DYAML_CPP_FORMAT_SOURCE:BOOL=OFF -DYAML_CPP_INSTALL:BOOL=ON \
 -DFETCHCONTENT_UPDATES_DISCONNECTED_YAML-CPP_FETCH_CONTENT:BOOL=ON \
 -DFETCHCONTENT_FULLY_DISCONNECTED:BOOL=ON -Dyaml-cpp_DIR:PATH=%{_libdir}/cmake/yaml-cpp \
%if %{?__isa_bits:%{__isa_bits}}%{!?__isa_bits:32} == 64
 -DOPENMS_64BIT_ARCHITECTURE:BOOL=ON \
%else
 -DOPENMS_64BIT_ARCHITECTURE:BOOL=OFF \
%endif
%if %{with check}
 -DBUILD_TESTING:BOOL=ON \
 -DBUILD_EXAMPLES:BOOL=ON \
 -DENABLE_TOPP_TESTING:BOOL=ON \
 -DENABLE_CLASS_TESTING:BOOL=ON \
%else
 -DBUILD_TESTING:BOOL=OFF \
 -DBUILD_EXAMPLES:BOOL=OFF \
 -DENABLE_TOPP_TESTING:BOOL=OFF \
 -DENABLE_CLASS_TESTING:BOOL=OFF \
%endif
%if 0%{?with_pyOpenMS}
 -DPYOPENMS=ON -DPYTHON_EXECUTABLE:FILEPATH=%{__python3} \
 -DCYTHON_EXECUTABLE:FILEPATH=%{_bindir}/cython3 \
 -DPY_NUM_THREADS:STRING=2 -DPY_NUM_MODULES:STRING=4 \
%else
 -DPYOPENMS=OFF \
%endif
%if "%{?_lib}" == "lib64"
  %{?_cmake_lib_suffix64}
%endif

%if %{with check}
%cmake_build
%else
%cmake_build -- OpenMS TOPP GUI
%endif

%if 0%{?with_pyOpenMS}
export LD_LIBRARY_PATH=$PWD/lib:$LD_LIBRARY_PATH
%cmake_build -- -j1 pyopenms
%endif

%install
export LD_LIBRARY_PATH=$PWD/lib:$LD_LIBRARY_PATH
%{_bindir}/xvfb-run -a %cmake_install

# Install executable tests
%if %{with check}
install -pm 755 %_vpath_builddir/src/tests/class_tests/bin/*_test %{buildroot}%{_bindir}/
%endif

# Fix rpaths
patchelf --set-rpath %{_libdir}/OpenMS %{buildroot}%{_bindir}/*
patchelf --set-rpath %{_libdir}/OpenMS %{buildroot}%{_libdir}/OpenMS/*.so

%if 0%{?with_pyOpenMS}
pushd %_vpath_builddir/pyOpenMS
%py3_install

ln -s -f %{_libdir}/OpenMS/libOpenMS.so %{buildroot}%{python3_sitearch}/pyopenms/libOpenMS.so
ln -s -f %{_libdir}/OpenMS/libOpenSwathAlgo.so %{buildroot}%{python3_sitearch}/pyopenms/libOpenSwathAlgo.so
ln -s -f %{_libdir}/OpenMS/libSuperHirn.so %{buildroot}%{python3_sitearch}/pyopenms/libSuperHirn.so

## Fix R script
sed -i "1 s|^#!/usr/bin/env Rscript\b|#!/usr/bin/Rscript|" %{buildroot}%{python3_sitearch}/pyopenms/share/OpenMS/SCRIPTS/plot_trafo.R
chmod 0755 %{buildroot}%{python3_sitearch}/pyopenms/share/OpenMS/SCRIPTS/plot_trafo.R
sed -i -e '1i#!/usr/bin/Rscript' %{buildroot}%{python3_sitearch}/pyopenms/share/OpenMS/SCRIPTS/mzTab2tsv_PEP.R
sed -i -e '1i#!/usr/bin/Rscript' %{buildroot}%{python3_sitearch}/pyopenms/share/OpenMS/SCRIPTS/mzTab2tsv_PRT.R
sed -i -e '1i#!/usr/bin/Rscript' %{buildroot}%{python3_sitearch}/pyopenms/share/OpenMS/SCRIPTS/mzTab2tsv_PSM.R

# wrong-script-end-of-line-encoding
sed -i 's/\r$//' %{buildroot}%{python3_sitearch}/pyopenms/share/OpenMS/SCRIPTS/mzTab2tsv_PRT.R
sed -i 's/\r$//' %{buildroot}%{python3_sitearch}/pyopenms/share/OpenMS/TOOLS/EXTERNAL/Rscript_mzTab2tsv_PRT.ttd
sed -i 's/\r$//' %{buildroot}%{python3_sitearch}/pyopenms/share/OpenMS/TOOLS/EXTERNAL/Rscript_mzTab2tsv_PSM.ttd

# OBO should be a text file format used by OBO-Edit
chmod 0644 %{buildroot}%{python3_sitearch}/pyopenms/share/OpenMS/CV/*.obo
chmod 0644 %{buildroot}%{python3_sitearch}/pyopenms/share/OpenMS/TOOLS/EXTERNAL/*.ttd
chmod 0644 %{buildroot}%{python3_sitearch}/pyopenms/share/OpenMS/CHEMISTRY/Enzymes.xml
popd
%endif
# with_pyOpenMS

##Install TOPPAS/TOPPView .png icons
mkdir -p %{buildroot}%{_datadir}/icons/TOPP/pixmaps
install -pm 644 %{SOURCE1} %{buildroot}%{_datadir}/icons/TOPP
install -pm 644 %{SOURCE2} %{buildroot}%{_datadir}/icons/TOPP
install -pm 644 %{SOURCE3} %{buildroot}%{_datadir}/icons/TOPP

##Install TOPPAS/TOPPView/inifileeditor .desktop files
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
 --set-key=Exec --set-value="env OPENMS_DATA_PATH=%{_datadir}/OpenMS TOPPAS" \
 --set-icon=%{_datadir}/icons/TOPP/TOPPAS.png \
 --set-key=StartupNotify --set-value=true \
 --add-category=Utility \
 --dir=%{buildroot}%{_datadir}/applications share/OpenMS/DESKTOP/TOPPAS.desktop

desktop-file-install \
 --set-key=Exec --set-value="env OPENMS_DATA_PATH=%{_datadir}/OpenMS TOPPView %U" \
 --set-icon=%{_datadir}/icons/TOPP/TOPPView.png \
 --set-key=StartupNotify --set-value=true \
 --add-category=Utility \
 --dir=%{buildroot}%{_datadir}/applications share/OpenMS/DESKTOP/TOPPView.desktop

desktop-file-install \
 --add-category=Utility \
 --set-key=Exec --set-value="env OPENMS_DATA_PATH=%{_datadir}/OpenMS INIFileEditor" \
 --dir=%{buildroot}%{_datadir}/applications %{SOURCE4}

# Install appdata files
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 share/OpenMS/DESKTOP/*.appdata.xml %{buildroot}%{_metainfodir}/

# HTML files copied
# I want to pack them by using %%doc macro
cp -a %{buildroot}%{_datadir}/doc/openms-doc/html html
rm -rf %{buildroot}%{_datadir}/doc/openms-doc/html

# Tool Description Library (TDL)
mv src/openms/extern/tool_description_lib/README.md src/openms/extern/tool_description_lib/README-tdl.md
rm -rf %{buildroot}%{_datadir}/doc/tdl

# Fix R script
sed -i "1 s|^#!/usr/bin/env Rscript\b|#!/usr/bin/Rscript|" %{buildroot}%{_datadir}/OpenMS/SCRIPTS/plot_trafo.R

chmod 0755 %{buildroot}%{_datadir}/OpenMS/SCRIPTS/plot_trafo.R

# Remove unused files
rm -rf %{buildroot}%{_includedir}/thirdparty
rm -rf %{buildroot}%{_datadir}/doc/OpenMS_host

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%if %{with check}
## starting tests
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}/OpenMS
export PATH=%{buildroot}%{_bindir}
export OPENMS_DATA_PATH=%{buildroot}%{_datadir}/OpenMS
export PYTHONPATH=%{buildroot}%{python3_sitearch}
export EXAMPLE_PATH=%{buildroot}%{_datadir}/OpenMS
LD_PRELOAD=%{buildroot}%{_libdir}/OpenMS/libOpenMS_GUI.so
LD_PRELOAD=%{buildroot}%{_libdir}/OpenMS/libOpenMS.so
LD_PRELOAD=%{buildroot}%{_libdir}/OpenMS/libOpenSwathAlgo.so
LD_PRELOAD=%{buildroot}%{_libdir}/OpenMS/libSuperHirn.so
%{_bindir}/ctest -j 4 -V --force-new-ctest-process --output-on-failure --test-dir build -E 'MRMAssay_test|MzMLFile_test|File_test|TOPP_OpenSwathWorkflow|Doxygen_Warning_test'
%endif

%files
%{_bindir}/TOPPView
%{_bindir}/TOPPAS
%{_bindir}/INIFileEditor
%{_bindir}/DTAExtractor
%{_bindir}/DatabaseSuitability
%{_bindir}/StaticModification
%{_bindir}/SwathWizard
%{_bindir}/FileConverter
%{_bindir}/FileInfo
%{_bindir}/FileMerger
%{_bindir}/IDMerger
%{_bindir}/IDRipper
%{_bindir}/IDFileConverter
%{_bindir}/MapStatistics
%{_bindir}/SpectraMerger
%{_bindir}/TextExporter
%{_bindir}/MzTabExporter
%{_bindir}/BaselineFilter
%{_bindir}/InternalCalibration
%{_bindir}/MapNormalizer
%{_bindir}/MassTraceExtractor
%{_bindir}/NoiseFilterGaussian
%{_bindir}/NoiseFilterSGolay
%{_bindir}/PeakPickerHiRes
%{_bindir}/HighResPrecursorMassCorrector
%{_bindir}/Resampler
%{_bindir}/SpectraFilterNLargest
%{_bindir}/SpectraFilterNormalizer
%{_bindir}/SpectraFilterThresholdMower
%{_bindir}/SpectraFilterWindowMower
%{_bindir}/Decharger
%{_bindir}/EICExtractor
%{_bindir}/FeatureFinderCentroided
%{_bindir}/FeatureFinderMetabo
%{_bindir}/FeatureLinkerUnlabeledKD
%{_bindir}/IsobaricAnalyzer
%{_bindir}/ProteinQuantifier 
%{_bindir}/SeedListGenerator
%{_bindir}/ConsensusMapNormalizer
%{_bindir}/MapAlignerIdentification
%{_bindir}/MapAlignerPoseClustering
%{_bindir}/MapRTTransformer
%{_bindir}/FeatureLinkerLabeled
%{_bindir}/FeatureLinkerUnlabeled
%{_bindir}/FeatureLinkerUnlabeledQT
%{_bindir}/MascotAdapter
%{_bindir}/MascotAdapterOnline
%{_bindir}/IonMobilityBinning
%{_bindir}/AssayGeneratorMetaboSirius
%{_bindir}/SiriusExport
%{_bindir}/SpecLibSearcher
%{_bindir}/ConsensusID
%{_bindir}/FalseDiscoveryRate
%{_bindir}/IDConflictResolver
%{_bindir}/IDFilter
%{_bindir}/IDMapper
%{_bindir}/IDPosteriorErrorProbability
%{_bindir}/IDRTCalibration
%{_bindir}/PeptideIndexer
%{_bindir}/ProteinInference
%{_bindir}/MRMMapper
%{_bindir}/MetaProSIP
%{_bindir}/OpenSwathDecoyGenerator
%{_bindir}/OpenSwathChromatogramExtractor
%{_bindir}/OpenSwathAnalyzer
%{_bindir}/OpenSwathRTNormalizer
%{_bindir}/OpenSwathFeatureXMLToTSV
%{_bindir}/OpenSwathConfidenceScoring
%{_bindir}/OpenSwathAssayGenerator
%{_bindir}/GenericWrapper
%{_bindir}/ExecutePipeline
%{_bindir}/FeatureFinderIdentification
%{_bindir}/FeatureFinderMultiplex
%{_bindir}/MRMTransitionGroupPicker
%{_bindir}/MSGFPlusAdapter
%{_bindir}/MetaboliteSpectralMatcher
%{_bindir}/OpenSwathWorkflow
%{_bindir}/PeakPickerIterative
%{_bindir}/PercolatorAdapter
%{_bindir}/SimpleSearchEngine
%{_bindir}/IDScoreSwitcher
%{_bindir}/MzMLSplitter
%{_bindir}/LuciphorAdapter
%{_bindir}/SageAdapter
%{_bindir}/DatabaseFilter
%{_bindir}/XTandemAdapter
%{_metainfodir}/*.appdata.xml
%{_datadir}/applications/TOPPAS.desktop
%{_datadir}/applications/TOPPView.desktop
%{_datadir}/applications/inifileeditor.desktop
%{_datadir}/icons/TOPP/
%{_libdir}/OpenMS/

%files utilities
%{_bindir}/AssayGeneratorMetabo
%{_bindir}/ClusterMassTraces
%{_bindir}/ClusterMassTracesByPrecursor
%{_bindir}/Epifany
%{_bindir}/FeatureFinderMetaboIdent
%{_bindir}/GNPSExport
%{_bindir}/NucleicAcidSearchEngine
%{_bindir}/ProteomicsLFQ
%{_bindir}/QualityControl
%{_bindir}/RNAMassCalculator
%{_bindir}/MapAlignerTreeGuided
%{_bindir}/MSFraggerAdapter
%{_bindir}/MSstatsConverter
%{_bindir}/MaRaClusterAdapter
%{_bindir}/NovorAdapter
%{_bindir}/RNADigestor
%{_bindir}/CometAdapter
%{_bindir}/MetaboliteAdductDecharger
%{_bindir}/OpenPepXL
%{_bindir}/OpenPepXLLF
%{_bindir}/OpenMSDatabasesInfo
%{_bindir}/PSMFeatureExtractor
%{_bindir}/XFDR
%{_bindir}/SpectraSTSearchAdapter
%{_bindir}/DatabaseFilter
%{_bindir}/TargetedFileConverter
%{_bindir}/FileFilter
%{_bindir}/IDDecoyProbability
%{_bindir}/OpenMSInfo
%{_bindir}/ExternalCalibration
%{_bindir}/OpenSwathFileSplitter
%{_bindir}/MultiplexResolver
%{_bindir}/TICCalculator
%{_bindir}/PhosphoScoring
%{_bindir}/INIUpdater
%{_bindir}/RNPxlXICFilter
%{_bindir}/FuzzyDiff
%{_bindir}/XMLValidator
%{_bindir}/SemanticValidator
%{_bindir}/CVInspector
%{_bindir}/IDSplitter
%{_bindir}/OpenSwathMzMLFileCacher
%{_bindir}/Digestor
%{_bindir}/DigestorMotif
%{_bindir}/DecoyDatabase
%{_bindir}/SequenceCoverageCalculator
%{_bindir}/IDExtractor
%{_bindir}/IDMassAccuracy 
%{_bindir}/SpecLibCreator
%{_bindir}/MRMPairFinder
%{_bindir}/ImageCreator
%{_bindir}/MassCalculator
%{_bindir}/DeMeanderize
%{_bindir}/OpenSwathDIAPreScoring
%{_bindir}/OpenSwathRewriteToFeatureXML
%{_bindir}/AccurateMassSearch
%{_bindir}/QCCalculator
%{_bindir}/QCImporter
%{_bindir}/QCEmbedder
%{_bindir}/QCExporter
%{_bindir}/QCExtractor
%{_bindir}/QCMerger
%{_bindir}/QCShrinker
%{_bindir}/TriqlerConverter
%{_bindir}/FLASHDeconv
%{_bindir}/FLASHDeconvWizard
%{_bindir}/JSONExporter

%files data
%doc CHANGELOG AUTHORS README* CODE_OF_CONDUCT.md
%license LICENSE*
%{_datadir}/OpenMS/

%files doc
%doc CHANGELOG AUTHORS README* CODE_OF_CONDUCT.md
%license LICENSE*
%doc html

%files devel
%license LICENSE* src/openms/extern/tool_description_lib/LICENSES/*.txt
%doc CHANGELOG AUTHORS README* CODE_OF_CONDUCT.md
%doc src/openms/extern/tool_description_lib/README-tdl.md
%if %{with check}
%{_bindir}/*_test
%endif
%{_includedir}/OpenMS/
%{_includedir}/tdl/
%{_libdir}/cmake/OpenMS/
%{_libdir}/cmake/tdl/

%if 0%{?with_pyOpenMS}
%files -n python3-openms
%license License.txt
%doc src/pyOpenMS/README_WRAPPING_NEW_CLASSES
%{python3_sitearch}/pyopenms/
%{python3_sitearch}/pyopenms-*.egg-info/
%endif

%changelog
%autochangelog
