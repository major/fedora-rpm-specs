Name:           CTL
Version:        1.5.3
Release:        %autorelease
Summary:        The Color Transformation Language

# Automatically converted from old format: AMPAS BSD - review is highly recommended.
License:        AMPAS
URL:            http://github.com/ampas/CTL
Source0:        %{url}/archive/ctl-%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-ctlrender-Add-missing-Half-Iex-libraries-at-link-tim.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake

# http://bugzilla.redhat.com/357461
# The CTL license is ok, Free but GPL Incompatible.
BuildRequires:  aces_container-devel
# As of OpenEXR 3 upstream has significantly reorganized the libraries
# including splitting out imath as a standalone library (which this project may
# or may not need). Please see
# https://github.com/AcademySoftwareFoundation/Imath/blob/master/docs/PortingGuide2-3.md
# for porting details and encourage upstream to support it. For now a 2.x
# compat package is provided.
%if 0%{?fedora} || 0%{?rhel} > 8
BuildRequires:  cmake(OpenEXR) < 3
%else
BuildRequires:  OpenEXR-devel
BuildRequires:  ilmbase-devel
%endif
BuildRequires:  libtiff-devel

# Provide this package as case-insensitive
Provides: ctl = %{version}-%{release}
# Obsoletes old libraries - rhbz#1644764
Provides:       OpenEXR_CTL-libs = %{version}-%{release}
Obsoletes:      OpenEXR_CTL-libs < 1.5.2-1


%description
The Color Transformation Language, or CTL, is a programming language
for digital color management.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ilmbase-devel%{?_isa}
Requires:       OpenEXR-devel%{?_isa}
Provides:       OpenEXR_CTL-devel = %{version}-%{release}
Obsoletes:      OpenEXR_CTL-devel < 1.5.2-1

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package docs
Summary:        Documentation for %{name}

%description docs
This package contains documentation files for %{name}.

%package -n     OpenEXR_CTL
Summary:        A simplified OpenEXR interface to CTL
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n  OpenEXR_CTL
exrdpx is an initial version of a CTL-driven file converter
that translates DPX files into OpenEXR files and vice versa.
The conversion between the DPX and OpenEXR color spaces is
handled by CTL transforms.

exr_ctl_exr is an initial version of a program that can bake
the effect of a series of CTL transforms into the pixels of
an OpenEXR file.


%prep
%autosetup -p1 -n CTL-ctl-%{version}
# remove executable bit
chmod -x lib/IlmCtl/Ctl*.cpp


%build
%cmake \
  -DCTL_BUILD_TESTS=OFF

%cmake_build


%install
%cmake_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# Remove installed docs
rm -rf %{buildroot}%{_docdir}
rm -rf %{buildroot}%{_prefix}/doc


%files
%doc AUTHORS CHANGELOG README.md
%license LICENSE
%{_libdir}/*.so.*
%{_datadir}/CTL

%files devel
%{_includedir}/CTL/
%{_includedir}/OpenEXR/ImfCtlApplyTransforms.h
%{_libdir}/*.so

%files docs
%doc doc/CtlManual.pdf doc/CtlManual.doc

%files -n OpenEXR_CTL
%{_bindir}/ctlrender
%{_bindir}/exr_ctl_exr
%{_bindir}/exrdpx


%changelog
%autochangelog
