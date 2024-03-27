%global _description %{expand:
BioSig is a software library for processing of biomedical signals (EEG, ECG,
etc.) with Matlab, Octave, C/C++ and Python. A standalone signal viewer
supporting more than 30 different data formats is also provided.}

%global pretty_name biosig

Name:       biosig4c++
Version:    2.6.0
Release:    %autorelease
Summary:    A software library for processing of biomedical signals

# SPDX
License:    GPL-3.0-or-later
URL:        https://sourceforge.net/projects/%{pretty_name}/
Source0:    https://downloads.sourceforge.net/project/%{pretty_name}/BioSig%20for%20C_C%2B%2B/src/%{pretty_name}-%{version}.src.tar.xz

# Drop i686
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  suitesparse-devel
BuildRequires:  tinyxml-devel
BuildRequires:  zlib-devel
BuildRequires:  gcc-c++
BuildRequires:  pkgconf-pkg-config
BuildRequires:  libb64-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make

%description
%{_description}

%package devel
Summary:    A software library for processing of biomedical signals
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
%{_description}


%prep
%autosetup -p1 -n %{pretty_name}-%{version}


%build
autoreconf -i -f
%configure
pushd %{name}
%make_build
%make_build save2gdf
%make_build biosig_fhir
popd

# make %{?_smp_mflags} mex4o
# make %{?_smp_mflags} biosig4python


%install
pushd %{name}
%make_install
popd

# Remove static libraries
rm -fv $RPM_BUILD_ROOT/%{_libdir}/libbiosig.a
rm -fv $RPM_BUILD_ROOT/%{_libdir}/libphysicalunits.a

chmod -x $RPM_BUILD_ROOT%{_mandir}/man1/*.1
# Remove man pages for tools that aren't included
rm -f $RPM_BUILD_ROOT/%{_mandir}/man1/{mexSLOAD,sigviewer}.1

%ldconfig_scriptlets

%files
%license COPYING
%doc %{name}/AUTHORS %{name}/README %{name}/NEWS %{name}/THANKS
%{_bindir}/bin2rec
%{_bindir}/biosig2gdf
%{_bindir}/rec2bin
%{_bindir}/heka2itx
%{_bindir}/physicalunits
%{_bindir}/save2aecg
%{_bindir}/save2gdf
%{_bindir}/save2scp
%{_bindir}/biosig_fhir
%{_libdir}/libbiosig.so.3
%{_mandir}/man1/*.1.gz



%files devel
%{_includedir}/%{pretty_name}-dev.h
%{_includedir}/%{pretty_name}.h
%{_includedir}/biosig2.h
%{_includedir}/gdftime.h
%{_includedir}/physicalunits.h
%{_libdir}/libbiosig.so
%{_libdir}/pkgconfig/libbiosig.pc


%changelog
%autochangelog
