# The documentation doesn't build at the moment, use the prebuilt one instead
%bcond_with doc

%if 0%{?fedora} && 0%{?fedora} >= 42
# kernel 6.13.6 from Fedora 41 is too old for v4.1.2
%bcond_without system_amd_hsmp
%else
%bcond_with system_amd_hsmp
%endif

Name:           esmi_ib_library
Version:        4.1.2

%global major_version %(echo %{version} | cut -d. -f1)
%global minor_version %(echo %{version} | cut -d. -f2)
%global soversion %{version}.0
%global srcversion esmi_pkg_ver-%{version}

Release:        %autorelease
Summary:        E-SMI: EPYC System management Interface In-band Library

License:        NCSA
URL:            https://github.com/amd/esmi_ib_library
Source:         %{url}/archive/%{srcversion}/%{name}-%{srcversion}.tar.gz
# for OS releases where amd_hsmp.h from kernel-headers is too old
Source:         https://github.com/amd/amd_hsmp/raw/0773094d8a59c641150c8b04f16bc782eaee2bd9/amd_hsmp.h
# https://github.com/amd/esmi_ib_library/pull/18
Patch:          esmi-fix-finding-amd_hsmp-include.patch
# Patch to use the bundled amd_hsmp.h we download rather than the system one
Patch100:       esmi-use-bundled-amd_hsmp-include.patch

# This is a hardware enablement package for AMD x86_64 platforms
ExclusiveArch:  x86_64

BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gcc-c++
%if %{with system_amd_hsmp}
BuildRequires:  kernel-headers
%endif
BuildRequires:  sed
%if %{with doc}
BuildRequires:  doxygen
BuildRequires:  make
BuildRequires:  texlive-latex
%endif

Suggests:       %{name}-doc = %{version}-%{release}

%description
The EPYC System Management Interface In-band Library, or E-SMI library, is
part of the EPYC System Management Inband software stack. It is a C library
for Linux that provides a user space interface to monitor and control the CPU's
power, energy, performance and other system management features.

%package        devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development headers and libraries for %{name}.

%package        doc
Summary:        Additional documentation for %{name}
BuildArch:      noarch

%description    doc
This package contains additional documentation for %{name}.

%package -n     e_smi_tool
Summary:        E-SMI: EPYC™ System management Interface tool

%description -n e_smi_tool
This package contains E-SMI tool, a program based on the E-SMI In-band library
that provides options to Monitor and Control System Management functionality.

%prep
%autosetup -N -n %{name}-%{srcversion}
%autopatch -p1 -M 99
# The amd_hsmp.h provided by kernel-headers is out of date
%if %{without system_amd_hsmp}
cp -p %{SOURCE1} include/e_smi/amd_hsmp.h
%autopatch -p1 -m 100 -M 199
%endif

# Use FHS install paths and patch version detection
sed -i CMakeLists.txt \
    -e 's:${E_SMI}/bin:%{_bindir}:g' \
    -e 's:e_smi/include:%{_includedir}:g' \
    -e 's:${E_SMI}/lib/static:%{_libdir}:g' \
    -e 's:${E_SMI}/lib:%{_libdir}:g' \
    -e 's:${E_SMI}/doc:%{_pkgdocdir}:g' \
    -e 's:get_package_version_number("1.0.0.0":get_version_from_tag("%{soversion}":'

%if %{with doc}
# Remove prebuilt docs
rm ESMI_IB_Release_Notes.pdf ESMI_Manual.pdf
%endif

%build
%cmake
%cmake_build
%if %{with doc}
make -C %{_vpath_builddir} doc
%endif

%install
%cmake_install

# Strip rpath
chrpath -d %{buildroot}/%{_bindir}/e_smi_tool

%check
%ctest

%files
%license License.txt
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README.md
%doc %{_pkgdocdir}/RELEASENOTES.md
%{_libdir}/libe_smi64.so.%{major_version}
%{_libdir}/libe_smi64.so.%{version}

%files devel
%{_includedir}/e_smi/
%{_libdir}/libe_smi64.so

%files doc
%license License.txt
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/ESMI_IB_Release_Notes.pdf
%doc %{_pkgdocdir}/ESMI_Manual.pdf

%files -n e_smi_tool
%{_bindir}/e_smi_tool

%changelog
%autochangelog
