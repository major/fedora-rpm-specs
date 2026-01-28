%undefine __cmake_in_source_build
%global gmthome %{_datadir}/gmt
%global gmtconf %{_sysconfdir}/gmt
%global gmtdoc %{_docdir}/gmt

%if 0%{?fedora} >= 33
%bcond_without flexiblas
%else
%bcond_with flexiblas
%endif

%bcond_with octave
%if %with octave
%{!?octave_api: %global octave_api %(octave-config -p API_VERSION 2>/dev/null || echo 0)}
%global octave_mdir %(octave-config -p LOCALAPIFCNFILEDIR || echo)
%global octave_octdir %(octave-config -p LOCALAPIOCTFILEDIR || echo)
%endif

%global completion_dir %(pkg-config --variable=completionsdir bash-completion)
%if "%{completion_dir}" == ""
%global completion_dir "/etc/bash_completion.d"
%endif

Name:           GMT
Version:        6.6.0
Release:        %autorelease
Summary:        Generic Mapping Tools

License:        LGPL-3.0-or-later
URL:            https://www.generic-mapping-tools.org/
Source0:        https://github.com/GenericMappingTools/gmt/releases/download/%{version}/gmt-%{version}-src.tar.xz
# Add missing byteswap include
#Patch0:         https://patch-diff.githubusercontent.com/raw/GenericMappingTools/gmt/pull/6044.patch
#Patch1: GMT-c99.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc
%if 0%{?fedora} >= 41
BuildRequires:  bash-completion-devel
%else
BuildRequires:  bash-completion
%endif
%if %{with flexiblas}
BuildRequires:  flexiblas-devel
%else
BuildRequires:  openblas-devel
%endif
BuildRequires:  fftw-devel
BuildRequires:  gdal
BuildRequires:  gdal-devel
BuildRequires:  geos-devel
BuildRequires:  glib2-devel
BuildRequires:  GraphicsMagick
BuildRequires:  libXt-devel libXaw-devel libXmu-devel libXext-devel
BuildRequires:  netcdf-devel
BuildRequires:  pcre2-devel
BuildRequires:  dcw-gmt
BuildRequires:  gshhg-gmt-nc4
%if %with octave
BuildRequires:  octave-devel
%endif
# less is detected by configure, and substituted in GMT.in
BuildRequires:  less
BuildRequires:  xdg-utils
# For docs
BuildRequires:  /usr/bin/sphinx-build
BuildRequires:  ghostscript
Requires:       gdal
Requires:       GraphicsMagick
Requires:       less
Requires:       %{name}-common = %{version}-%{release}
Requires:       dcw-gmt
Requires:       gshhg-gmt-nc4
Provides:       gmt = %{version}-%{release}
Requires:       xdg-utils
%if %without octave
Obsoletes:      GMT-octave <= 4.5.11
%endif

# Do not generate provides for plugins
%global __provides_exclude_from ^%{_libdir}/gmt/.*\\.so$

%description
GMT is an open source collection of ~60 tools for manipulating geographic and
Cartesian data sets (including filtering, trend fitting, gridding, projecting,
etc.) and producing Encapsulated PostScript File (EPS) illustrations ranging
from simple x-y plots via contour maps to artificially illuminated surfaces
and 3-D perspective views.  GMT supports ~30 map projections and transforma-
tions and comes with support data such as coastlines, rivers, and political
boundaries.

GMT is developed and maintained by Paul Wessel and Walter H. F.  Smith with
help from a global set of volunteers, and is supported by the National
Science Foundation.

NOTE: Specific executables that conflict with other Fedora packages have been
removed.  These functions can still be accessed via the GMT wrapper script
with: GMT <function> [args]


%package        common
Summary:        Common files for %{name}
Provides:       gmt-common = %{version}-%{release}
BuildArch:      noarch

%description    common
The %{name}-common package contains common files for GMT (Generic
Mapping Tools) package.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Provides:       gmt-devel = %{version}-%{release}
Obsoletes:      GMT-static <= 4.5.11

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
Provides:       gmt-doc = %{version}-%{release}
Provides:       %{name}-examples = %{version}-%{release}
Obsoletes:      %{name}-examples < %{version}-%{release}
BuildArch:      noarch

%description    doc
The %{name}-doc package provides the documentation for the GMT (Generic
Mapping Tools) package.


%if %with octave
%package        octave
Summary:        Octave libraries for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       octave(api) = %{octave_api}
Provides:       gmt-octave = %{version}-%{release}

%description    octave
The %{name}-octave package contains and Octave interface for developing
applications that use %{name}.
%endif


%prep
%autosetup -p1 -n gmt-%{version}


%build
%cmake \
  -DCMAKE_INSTALL_LIBDIR=%{_lib} \
  -DGSHHG_ROOT=%{_datadir}/gshhg-gmt-nc4 \
  -DGMT_INSTALL_MODULE_LINKS=off \
  -DGMT_INSTALL_TRADITIONAL_FOLDERNAMES=off \
  -DLICENSE_RESTRICTED=LGPL \
%if %with octave
  -DGMT_OCTAVE=BOOL:ON \
%endif
  -DGMT_ENABLE_OPENMP=BOOL:ON \
  -DGMT_USE_THREADS=BOOL:ON \
%if %{with flexiblas}
  -DGMT_EXCLUDE_BLAS=BOOL:ON \
  -DGMT_EXCLUDE_LAPACK=BOOL:ON \
  -DBLAS_LIBRARY=-lflexiblas \
  -DLAPACK_LIBRARY=-lflexiblas \
%endif
  -DBASH_COMPLETION_DIR=%{completion_dir}
%cmake_build


%install
%cmake_install
#Setup configuration files 
mkdir -p $RPM_BUILD_ROOT%{gmtconf}/{mgg,dbase,mgd77}
pushd $RPM_BUILD_ROOT%{gmthome}/
# put conf files in %{gmtconf} and do links in %{gmthome}
for file in mgg/gmtfile_paths mgd77/mgd77_paths.txt; do
  mv $file $RPM_BUILD_ROOT%{gmtconf}/$file
  ln -s ../../../../../%{gmtconf}/$file $RPM_BUILD_ROOT%{gmthome}/$file
done
popd

# Configure coastline data location
mkdir -p $RPM_BUILD_ROOT%{gmthome}/coast
echo %{_datadir}/gshhg-gmt-nc4 > $RPM_BUILD_ROOT%{gmthome}/coast/coastline.conf

# Don't ship .bat files
find $RPM_BUILD_ROOT -name \*.bat -delete


%ldconfig_scriptlets


%files
%license COPYING.LESSERv3 COPYINGv3 LICENSE.TXT
%doc CITATION.cff CONTRIBUTING.md README.md
%{_bindir}/*
%{_libdir}/*.so.6*
%{_libdir}/gmt/

%files common
%license COPYING.LESSERv3 COPYINGv3 LICENSE.TXT
%doc CITATION.cff CONTRIBUTING.md README.md
%dir %{gmtconf}
%dir %{gmtconf}/mgg
%dir %{gmtconf}/dbase
%dir %{gmtconf}/mgd77
%config(noreplace) %{gmtconf}/mgg/gmtfile_paths
%config(noreplace) %{gmtconf}/mgd77/mgd77_paths.txt
%{gmthome}/
%{completion_dir}/

%files devel
%{_includedir}/*
%{_libdir}/*.so

%files doc
%{gmtdoc}/

%if %with octave
%files octave
%{octave_mdir}/*.m
%{octave_octdir}/*.mex
%endif


%changelog
%autochangelog
