%bcond_without check
%bcond_with debug

ExclusiveArch: %{qt5_qtwebengine_arches}

# Python binding
%global with_pyOpenMS 1
Obsoletes: python3-openms < 0:2.7.0-2
Obsoletes: python2-openms < 0:2.4.0-1
#

# Filter private libraries
%global __provides_exclude ^(%%(find %{buildroot}%{_libdir}/OpenMS -name '*.so' | xargs -n1 basename | sort -u | paste -s -d '|' -))
%global __requires_exclude ^(%%(find %{buildroot}%{_libdir}/OpenMS -name '*.so' | xargs -n1 basename | sort -u | paste -s -d '|' -))

Name:      openms
Summary:   LC/MS data management and analyses
Version:   3.0.0
Release:   0.2%{?dist}
License:   BSD
URL:       http://www.openms.de/
Source0:   https://github.com/OpenMS/OpenMS/archive/Release%{version}/OpenMS-Release%{version}.tar.gz

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
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires: qt5-qtwebkit-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: qt5-qtwebengine-devel
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

## Build documentation
## Doxygen useful only on SVN versions  
BuildRequires: doxygen, dos2unix, graphviz
BuildRequires: texlive, texlive-a4wide, texlive-xtab

##Xvfb is needed to run a virtual X server used by some tests
BuildRequires: xorg-x11-server-Xvfb, gnuplot, gawk

Requires: percolator%{?_isa}
Requires: %{name}-data%{?_isa} = %{version}-%{release}
Requires: R-core%{?_isa}

# Remove -O0 flag for tests compiling
Patch0: %{name}-remove_testflag.patch

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
as well as adapters to other state-of-the art tools like XTandem, Mascot,
OMSSA, etc.
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

%package tools
Summary: OpenMS tools
Requires: %{name}-data%{?_isa} = %{version}-%{release}
%description tools
Besides TOPP, OpenMS offers a range of other tools. 
They are not included in TOPP as they are not part of 
typical analysis pipelines, but they still might be 
very helpful to you.

The UTILS tools are divided into several subgroups:
 
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
BuildRequires: python3-nose
BuildRequires: python3-autowrap >= 0.8.1
BuildRequires: python3-pip
BuildRequires: %{_bindir}/cython
BuildRequires: python3-wheel
BuildRequires: python3-biopython
BuildRequires: python3-virtualenv
BuildRequires: python3-pandas
BuildRequires: python3-pytest
Requires: python3-biopython%{?_isa}
Requires: %{name}%{?_isa} = %{version}-%{release}

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
Requires: %{name}%{?_isa} = %{version}-%{release}
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
%autosetup -N -n OpenMS-Release%{version}

dos2unix share/OpenMS/SIMULATION/FASTAProteinAbundanceSampling.py
%patch -P 0 -p1 -b .backup

# Remove invalid tags
sed -e 's| <project_group></project_group>||g' -i share/OpenMS/DESKTOP/*.appdata.xml


%build
%ifarch %{ix86}
# Likely running out of memory during build
%global _smp_ncpus_max 2
%else
%global _smp_ncpus_max 4
%endif
mkdir -p build
%if %{with debug}
cmake -Wno-dev -B build -S ./ -DCMAKE_CXX_COMPILER_VERSION:STRING=$(gcc -dumpversion) \
 -DENABLE_UPDATE_CHECK:BOOL=OFF \
 -DCMAKE_COLOR_MAKEFILE:BOOL=ON \
 -DCMAKE_CXX_FLAGS_DEBUG:STRING="-DDEBUG -O0 -g %{__global_ldflags}" -DCMAKE_C_FLAGS_DEBUG:STRING="-DDEBUG -O0 -g %{__global_ldflags}" \
 -DCMAKE_BUILD_TYPE=Debug \
 -DBoost_IOSTREAMS_LIBRARY_DEBUG:FILEPATH=%{_libdir}/libboost_iostreams.so \
 -DBoost_MATH_C99_LIBRARY_DEBUG:FILEPATH=%{_libdir}/libboost_math_c99.so \
 -DBoost_REGEX_LIBRARY_DEBUG:FILEPATH=%{_libdir}/libboost_regex.so \
 -DXercesC_LIBRARY_DEBUG:FILEPATH=%{_libdir}/libxerces-c.so \
%else
# LTO flags break Python binding on i686
%ifarch %{ix86}
%define _lto_cflags %{nil}
%endif
%cmake -Wno-dev -B build -S ./ -DCMAKE_CXX_COMPILER_VERSION:STRING=$(gcc -dumpversion) \
 -DGIT_TRACKING:BOOL=OFF \
 -DENABLE_UPDATE_CHECK:BOOL=OFF \
 -DCMAKE_COLOR_MAKEFILE:BOOL=ON \
 -DCMAKE_CXX_FLAGS_RELEASE:STRING="-Wno-cpp %{build_cxxflags}" -DCMAKE_C_FLAGS_RELEASE:STRING="-Wno-cpp %{build_cflags}" \
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
 -DPY_NUM_THREADS:STRING=2 -DPY_NUM_MODULES:STRING=4
%else
 -DPYOPENMS=OFF
%endif

%if %{with check}
%make_build all -C build
%else
%make_build OpenMS TOPP UTILS GUI -C build
%endif

%if 0%{?with_pyOpenMS}
export LD_LIBRARY_PATH=$PWD/lib:$LD_LIBRARY_PATH
make pyopenms -C build
%endif

%install
export LD_LIBRARY_PATH=$PWD/lib:$LD_LIBRARY_PATH
%{_bindir}/xvfb-run -a %make_install -C build

# Install executable tests
%if %{with check}
install -pm 755 build/src/tests/class_tests/bin/*_test %{buildroot}%{_bindir}/
%endif

# Fix rpaths
patchelf --set-rpath %{_libdir}/OpenMS %{buildroot}%{_bindir}/*
patchelf --set-rpath %{_libdir}/OpenMS %{buildroot}%{_libdir}/OpenMS/*.so

%if 0%{?with_pyOpenMS}
pushd build/pyOpenMS
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

##Install appdata files
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 share/OpenMS/DESKTOP/*.appdata.xml %{buildroot}%{_metainfodir}/

##HTML files copied
##I want to pack them by using %%doc macro
cp -a %{buildroot}%{_datadir}/doc/openms-doc/html html
rm -rf %{buildroot}%{_datadir}/doc/openms-doc/html

## Fix R script
sed -i "1 s|^#!/usr/bin/env Rscript\b|#!/usr/bin/Rscript|" %{buildroot}%{_datadir}/OpenMS/SCRIPTS/plot_trafo.R

chmod 0755 %{buildroot}%{_datadir}/OpenMS/SCRIPTS/plot_trafo.R

# Remove unused files
rm -rf %{buildroot}%{_includedir}/thirdparty

%if %{with check}
cp -a %{buildroot}%{_datadir}/OpenMS/examples/examples/* %{buildroot}%{_datadir}/OpenMS/examples/
rm -rf %{buildroot}%{_datadir}/OpenMS/examples/examples
%endif

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%if %{with check}
## starting tests
pushd build
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}/OpenMS
export PATH=%{buildroot}%{_bindir}:%{_bindir}
export OPENMS_DATA_PATH=%{buildroot}%{_datadir}/OpenMS
export PYTHONPATH=%{buildroot}%{python3_sitearch}:../src/OpenMS
LD_PRELOAD=%{buildroot}%{_libdir}/OpenMS/libOpenMS_GUI.so
LD_PRELOAD=%{buildroot}%{_libdir}/OpenMS/libOpenMS.so
LD_PRELOAD=%{buildroot}%{_libdir}/OpenMS/libOpenSwathAlgo.so
LD_PRELOAD=%{buildroot}%{_libdir}/OpenMS/libSuperHirn.so
ctest -j 1 -VV --force-new-ctest-process --output-on-failure -E 'MRMAssay_test|SVMWrapper_test|File_test' && exit 1
popd
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
%{_bindir}/PeakPickerWavelet
%{_bindir}/PrecursorMassCorrector
%{_bindir}/HighResPrecursorMassCorrector
%{_bindir}/Resampler
%{_bindir}/SpectraFilterBernNorm
%{_bindir}/SpectraFilterMarkerMower
%{_bindir}/SpectraFilterNLargest
%{_bindir}/SpectraFilterNormalizer
%{_bindir}/SpectraFilterParentPeakMower
%{_bindir}/SpectraFilterScaler
%{_bindir}/SpectraFilterSqrtMower
%{_bindir}/SpectraFilterThresholdMower
%{_bindir}/SpectraFilterWindowMower
%{_bindir}/TOFCalibration
%{_bindir}/Decharger
%{_bindir}/EICExtractor
%{_bindir}/FeatureFinderCentroided
%{_bindir}/FeatureFinderIsotopeWavelet
%{_bindir}/FeatureFinderMetabo
%{_bindir}/FeatureFinderMRM
%{_bindir}/FeatureLinkerUnlabeledKD
%{_bindir}/IsobaricAnalyzer
%{_bindir}/ProteinQuantifier 
%{_bindir}/ProteinResolver
%{_bindir}/SeedListGenerator
%{_bindir}/ConsensusMapNormalizer
%{_bindir}/MapAlignerIdentification
%{_bindir}/MapAlignerPoseClustering
%{_bindir}/MapAlignerSpectrum
%{_bindir}/MapRTTransformer
%{_bindir}/FeatureLinkerLabeled
%{_bindir}/FeatureLinkerUnlabeled
%{_bindir}/FeatureLinkerUnlabeledQT
%{_bindir}/CompNovo
%{_bindir}/CompNovoCID
%{_bindir}/MascotAdapter
%{_bindir}/MascotAdapterOnline
%{_bindir}/PepNovoAdapter
%{_bindir}/XTandemAdapter
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
%{_bindir}/InclusionExclusionListCreator
%{_bindir}/PrecursorIonSelector
%{_bindir}/MRMMapper
%{_bindir}/MetaProSIP
%{_bindir}/OpenSwathDecoyGenerator
%{_bindir}/OpenSwathChromatogramExtractor
%{_bindir}/OpenSwathAnalyzer
%{_bindir}/OpenSwathRTNormalizer
%{_bindir}/OpenSwathFeatureXMLToTSV
%{_bindir}/OpenSwathConfidenceScoring
%{_bindir}/OpenSwathAssayGenerator
%{_bindir}/PTModel
%{_bindir}/PTPredict
%{_bindir}/RTModel
%{_bindir}/RTPredict
%{_bindir}/GenericWrapper
%{_bindir}/ExecutePipeline
%{_bindir}/FeatureFinderIdentification
%{_bindir}/FeatureFinderMultiplex
%{_bindir}/FidoAdapter
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
%{_bindir}/DatabaseFilter
%{_bindir}/RNPxlSearch
%{_metainfodir}/*.appdata.xml
%{_datadir}/applications/TOPPAS.desktop
%{_datadir}/applications/TOPPView.desktop
%{_datadir}/applications/inifileeditor.desktop
%{_datadir}/icons/TOPP/
%{_libdir}/OpenMS/
%dir %{_libdir}/cmake/OpenMS
%{_libdir}/cmake/OpenMS/OpenMSConfig.cmake
%{_libdir}/cmake/OpenMS/OpenMSConfigVersion.cmake

%files tools
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
%{_bindir}/SiriusAdapter
%{_bindir}/XFDR
%{_bindir}/RNPxlSearch
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
%{_bindir}/FFEval
%{_bindir}/LabeledEval
%{_bindir}/RTEvaluation
%{_bindir}/TransformationEvaluation
%{_bindir}/Digestor
%{_bindir}/DigestorMotif
%{_bindir}/DecoyDatabase
%{_bindir}/SequenceCoverageCalculator
%{_bindir}/IDExtractor
%{_bindir}/IDMassAccuracy 
%{_bindir}/SpecLibCreator
%{_bindir}/ERPairFinder
%{_bindir}/MRMPairFinder
%{_bindir}/ImageCreator
%{_bindir}/MassCalculator
%{_bindir}/MSSimulator
%{_bindir}/SvmTheoreticalSpectrumGeneratorTrainer
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
%license LICENSE
%{_datadir}/OpenMS/

%files doc
%doc CHANGELOG AUTHORS README* CODE_OF_CONDUCT.md
%license LICENSE
%doc html

%files devel
%license LICENSE
%doc CHANGELOG AUTHORS README* CODE_OF_CONDUCT.md
%if %{with check}
%{_bindir}/*_test
%endif
%{_includedir}/OpenMS/

%if 0%{?with_pyOpenMS}
%files -n python3-openms
%license src/pyOpenMS/License.txt
%doc src/pyOpenMS/FOR_DEVELOPERS
%doc src/pyOpenMS/README_WRAPPING_NEW_CLASSES
%{python3_sitearch}/pyopenms/
%{python3_sitearch}/pyopenms-*.egg-info/
%endif

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Antonio Trande <sagitter@fedoraproject.org> - 3.0.0-0.1
- Pre-release 3.0.0

* Wed Feb 01 2023 Antonio Trande <sagitter@fedoraproject.org> - 2.8.0-0.5
- Fixed for GCC-13

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 18 2022 Jerry James <loganjerry@gmail.com> - 2.8.0-0.3
- Rebuild for libsvm 3.3

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Mar 05 2022 Antonio Trande <sagitter@fedoraproject.org> - 2.8.0-0.1
- Pre-release 2.8.0
- Patched for GCC-12
- ExclusiveArch qt5_qtwebengine_arches

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 28 2021 Antonio Trande <sagitter@fedoraproject.org> - 2.7.0-2
- Rebuild for hdf5 1.12.1
- Disable Python binding

* Sat Sep 18 2021 Antonio Trande <sagitter@fedoraproject.org> - 2.7.0-1
- Release 2.7.0
- Tests disabled
- Use bundled seqan (optimized for OpenMS)

* Tue Aug 10 2021 Orion Poplawski <orion@nwra.com> - 2.6.0-11
- Rebuild for hdf5 1.10.7

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 2.6.0-10
- Rebuilt for Boost 1.76

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 22 2021 Antonio Trande <sagitter@fedoraproject.org> - 2.6.0-8
- Patched for upstream bug #5381

* Sat Jun 19 2021 Antonio Trande <sagitter@fedoraproject.org> - 2.6.0-7
- Release build
- Enable Python binding (not in ARM and s390x)
- Enable check

* Wed Feb 17 2021 Antonio Trande <sagitter@fedoraproject.org> - 2.6.0-6
- Filter private libraries

* Tue Feb 16 2021 Antonio Trande <sagitter@fedoraproject.org> - 2.6.0-5
- Remove fido-pi dependencies

* Tue Feb 02 2021 Antonio Trande <sagitter@fedoraproject.org> - 2.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild
- Patch GLPK version

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 2.6.0-3
- Rebuilt for Boost 1.75

* Sun Oct 25 2020 Antonio Trande <sagitter@fedoraproject.org> - 2.6.0-2
- Avoid skipping rpaths

* Fri Oct 02 2020 Antonio Trande <sagitter@fedoraproject.org> - 2.6.0-1
- Release 2.6.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-7
- Second attempt - Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild
- Enable cmake_in_source_build

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Orion Poplawski <orion@cora.nwra.com> - 2.5.0-5
- Rebuild for hdf5 1.10.6

* Tue Jun 02 2020 Antonio Trande <sagitter@fedoraproject.org> - 2.5.0-4
- Rebuild for boost-1.73

* Fri May 01 2020 Antonio Trande <sagitter@fedoraproject.org> - 2.5.0-3
- Rebuild for coin-or-* updates

* Tue Feb 25 2020 Antonio Trande <sagitter@fedoraproject.org> - 2.5.0-2
- Add Desktop file's categories

* Tue Feb 25 2020 Antonio Trande <sagitter@fedoraproject.org> - 2.5.0-1
- Release 2.5.0
- Doc sub-package becomes arch-dependent

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 08 2019 Antonio Trande <sagitter@fedoraproject.org> - 2.4.0-7
- Rebuild for autowrap 0.19.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Jerry James <loganjerry@gmail.com> - 2.4.0-5
- Rebuild for coin-or package updates

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Jonathan Wakely <jwakely@redhat.com> - 2.4.0-3
- Rebuilt for Boost 1.69

* Tue Nov 06 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.4.0-2
- Add rpmlintrc file

* Tue Oct 30 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.4.0-1
- Release 2.4.0
- Disable Python3 binding
- Drop Python2 binding
- Use Qt5

* Wed Aug 22 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.3.0-14
- Patched for removing unrecognized command line options

* Wed Aug 22 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.3.0-13
- Deprecate Python2 binding of fedora 30+

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-11
- Rebuilt for Python 3.7

* Mon May 21 2018 Jerry James <loganjerry@gmail.com> - 2.3.0-10
- Rebuild for glpk 4.65

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 2.3.0-9
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Mon Feb 12 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.3.0-8
- Fix XML file's permissions

* Sun Feb 11 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.3.0-7
- Compile pyOpenMS
- Set Python2 required packages
- Fix R scripts shebang

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.3.0-5
- Rebuild for boost-1.66
- Remove obsolete scriptlets

* Wed Jan 10 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.3.0-4
- Set maximum required version of seqan

* Fri Jan 05 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.3.0-3
- Tests disabled

* Fri Jan 05 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.3.0-2
- Fix R script

* Wed Jan 03 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.3.0-1
- Update to OpenMS-2.3.0
- Drop obsolete GCC7 patches

* Thu Dec 21 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.2.0-7
- Appdata file moved into metainfo data directory

* Mon Nov 13 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.2.0-6
- Rebuild OpenMS-2.2.0
- Remove obsolete patch

* Fri Oct 13 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.2.0-5
- Rebuild for wildmagic5-5.17

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Björn Esser <besser82@fedoraproject.org> - 2.2.0-3
- Rebuilt for Boost 1.64

* Sun Jul 23 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.2.0-2
- Rebuild for boost-1.64

* Wed Jun 28 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0
- Include patch for GCC-7

* Sat Jun 10 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.1.0-9.20170131gitbde813
- Rebuild for wildmagic5-5.15

* Fri Apr 14 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.1.0-8.20170131gitbde813
- Rebuild for biopython-1.69

* Wed Apr 05 2017 Jerry James <loganjerry@gmail.com> - 2.1.0-7.20170131gitbde813
- Rebuild for glpk 4.61

* Tue Feb 07 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.1.0-6.20170131gitbde813
- Rebuild for boost-1.63

* Tue Jan 31 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.1.0-5.20170131gitbde813
- Rebuild for GCC-7.0.1
- Add CMAKE_CXX_COMPILER_VERSION option

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 2.1.0-4
- Rebuilt for Boost 1.63

* Fri Jan 06 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.1.0-3
- Fix desktop icons

* Wed Dec 28 2016 Rich Mattes <richmattes@gmail.com> - 2.1.0-2
- Rebuild for eigen3-3.3.1

* Tue Nov 22 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0 (stable release)
- Drop old patch

* Thu Nov 10 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.1.0-0.1
- Update to 2.1.0 (pre-release)
- Patched to fix PyOpenMS
- Python bindings disabled (upstream issue #2286)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-35.20160121git6f51b3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jun 24 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.0.0-34.20160121git6f51b3
- Rebuild for Biopython-1.67

* Tue May 17 2016 Jonathan Wakely <jwakely@redhat.com> - 2.0.0-33.20160121git6f51b3
- Rebuilt for linker errors in boost (#1331983)

* Sat Mar 12 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.0.0-32.20160121git6f51b3
- Rebuild for GLPK-4.59

* Fri Feb 19 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.0.0-31.20160121git6f51b3
- Rebuild for GLPK-4.58

* Mon Feb 15 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.0.0-30.20160121git6f51b3
- Macros removed from Obsolets tags

* Sun Feb 14 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.0.0-29.20160121git6f51b3
- PyOpenMS disabled on x86 arches
- Remove invalid tags from appdata files

* Sun Feb 14 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.0.0-28.20160121git6f51b3
- Specified the number of Make jobs
- Patched for GCC-6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-27.20160121git6f51b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.0.0-26.20160121git6f51b3
- Fixed package dependency

* Tue Jan 26 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.0.0-25.20160121git6f51b3
- Data sub-package arched

* Mon Jan 25 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.0.0-24.20160121git6f51b3
- Disabled HAS_XSERVER option

* Fri Jan 22 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.0.0-23.20160121git6f51b3
- Update to commit #6f51b3
- Excluded some tests
- Added python provides macros
- Rebuild for wildmagic5-5.14
- Fixed Python2 sub-package
- Removed tutorials

* Thu Dec 10 2015 Antonio Trande <sagitter@fedoraproject.org> - 2.0.0-22.20151210gitf19f8b
- Update to commit #f19f8b
- Python3 binding
- Added python-biopython as BR package

* Wed Nov 04 2015 Antonio Trande <sagitter@fedoraproject.org> - 2.0.0-21.20150529git88dc25
- Hardened builds on <F23

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 2.0.0-20.20150529git88dc25
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-19.20150529git88dc25
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Fri Jul 24 2015 Antonio Trande <sagitter@fedoraproject.org> 2.0.0-18.20150529git88dc25
- Rebuild again

* Sat Jul 18 2015 Antonio Trande <sagitter@fedoraproject.org> 2.0.0-17.20150529git88dc25
- Rebuild for Boost upgrade to 1.58.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-16.20150529git88dc25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Antonio Trande <sagitter@fedoraproject.org> 2.0.0-15.20150529git88dc25
- memleak test excluded again

* Tue Jun 09 2015 Antonio Trande <sagitter@fedoraproject.org> 2.0.0-14.20150529git88dc25
- Exclude TOPP_OpenSwathAssayGenerator_test_1_out1 test

* Tue Jun 09 2015 Antonio Trande <sagitter@fedoraproject.org> 2.0.0-13.20150529git88dc25
- Update to the post-release #88dc25
- Packaged MetaProSIP and OpenSwathAssayGenerator
- Obsolete wrong python2-openms 2.0.0
- Replaced XTandem with fido-pi

* Fri May 15 2015 Antonio Trande <sagitter@fedoraproject.org> 2.0.0-12
- Bug fix in upstream desktop files

* Fri May 15 2015 Antonio Trande <sagitter@fedoraproject.org> 2.0.0-11
- Fix PeakPickerWavelet test
- Set environment variables in desktop files

* Fri May 08 2015 Antonio Trande <sagitter@fedoraproject.org> 2.0.0-10
- Excluded TOPP_XTandemAdapter_ test

* Fri May 08 2015 Antonio Trande <sagitter@fedoraproject.org> 2.0.0-9
- Rebuild after XTandem update
- Try to execute XTandem test

* Sat May 02 2015 Antonio Trande <sagitter@fedoraproject.org> 2.0.0-8
- memleaks test excluded

* Sat May 02 2015 Antonio Trande <sagitter@fedoraproject.org> 2.0.0-7
- mzML unittests patched
- PyOpenMS compiled without parallel make
- PyOpenMS tests disabled

* Fri May 01 2015 Antonio Trande <sagitter@fedoraproject.org> 2.0.0-6
- Source archive re-compressed by upstream
- Sym-linked the library pyopenms/libSuperHirn.so

* Fri May 01 2015 Antonio Trande <sagitter@fedoraproject.org> 2.0.0-5
- SPEC cleanups

* Thu Apr 30 2015 Antonio Trande <sagitter@fedoraproject.org> 2.0.0-4
- Patched pyOpenMS version definition
- Removed 'pyopenms_bdist_egg' make target

* Thu Apr 30 2015 Antonio Trande <sagitter@fedoraproject.org> 2.0.0-3
- PyOpenMS is still compiled against Python2 on Linux

* Mon Apr 13 2015 Antonio Trande <sagitter@fedoraproject.org> 2.0.0-2
- Fix make test

* Sat Apr 11 2015 Antonio Trande <sagitter@fedoraproject.org> 2.0.0-1
- Update to the release 2.0

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 1.11.1-12
- Rebuild for boost 1.57.0

* Sat Dec 13 2014 Antonio Trande <sagitter@fedoraproject.org> 1.11.1-11
- Parallel make disabled

* Fri Dec 12 2014 Antonio Trande <sagitter@fedoraproject.org> 1.11.1-10
- Parallel make just on Fedora 20+

* Mon Dec 08 2014 Antonio Trande <sagitter@fedoraproject.org> 1.11.1-9
- Fixed unused-direct-shlib-dependency warnings
- Fixed residual spurious executable permissions
- Avoided python shared object stripping
- Added a patch (Patch5) to detect additional QT libraries

* Fri Dec 05 2014 Antonio Trande <sagitter@fedoraproject.org> 1.11.1-8
- Fixed INIFileEditor .desktop file
- Fixed some spurious executable permissions

* Fri Dec 05 2014 Antonio Trande <sagitter@fedoraproject.org> 1.11.1-7
- Fixed some cmake options
- Fixed %%post/%%postun/%%posttrans
- Added TOPP and Tutorial tests
- Fixed iCPP warnings of the PNG files
- Built a noarch data sub-package
- python-openms's data file directory linked to /usr/share/OpenMS  
- TOPP tests disabled (some of them fail)

* Tue Oct 07 2014 Antonio Trande <sagitter@fedoraproject.org> 1.11.1-6
- Added conditional arch macro

* Mon Oct 06 2014 Antonio Trande <sagitter@fedoraproject.org> 1.11.1-5
- Included XTandem BR

* Mon Sep 29 2014 Antonio Trande <sagitter@fedoraproject.org> 1.11.1-4
- Added cmake's options for TBB
- Added nested C++ templates patch (Patch4)

* Mon Jun 30 2014 Antonio Trande <sagitter@fedoraproject.org> 1.11.1-3
- Added setuptools patch
- Added library patch
- pyOpenMS building enabled
- Performed pyOpenMS tests
- Added .desktop files and related .xpm icons

* Sun Jun 01 2014 Antonio Trande <sagitter@fedoraproject.org> 1.11.1-2
- Check disabled
- pyOpenMS building disabled
- Added a macro for pyOpenMS

* Thu May 22 2014 Antonio Trande <sagitter@fedoraproject.org> 1.11.1-1
- First package
