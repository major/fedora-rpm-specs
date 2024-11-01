Name:           rocm-rpm-macros
Version:        6.2.2
Release:        %autorelease
Summary:        ROCm RPM macros
License:        GPL-2.0-or-later

URL:            https://github.com/trixirt/rocm-rpm-macros
Source0:        macros.rocm
Source1:        GPL
# Modules
Source2:        default
Source3:        gfx8
Source4:        gfx9
Source5:        gfx10
Source6:        gfx11
Source7:        gfx906
Source8:        gfx908
Source9:        gfx90a
Source10:       gfx942
Source11:       gfx1031
Source12:       gfx1036
Source13:       gfx1100
Source14:       gfx1101
Source15:       gfx1102
Source16:       gfx1103
Source17:       default.rhel

%global gpu_list gfx8 gfx9 gfx10 gfx11 gfx90a gfx942 gfx1100 gfx1103

# Just some files
%global debug_package %{nil}

Requires:       environment-modules
ExclusiveArch:  x86_64
%description
This package contains ROCm RPM macros for building ROCm packages.

%package modules
Summary: ROCm enviroment modules
Requires: environment(modules)
Requires: cmake-filesystem

%description modules
This package contains ROCm environment modules for switching
between different GPU families.

%prep
%setup -cT
install -pm 644 %{SOURCE0} .
install -pm 644 %{SOURCE1} .
mkdir modules
%if 0%{?rhel}
install -pm 644 %{SOURCE17} modules/default
%else
install -pm 644 %{SOURCE2} modules
%endif
install -pm 644 %{SOURCE3} modules
install -pm 644 %{SOURCE4} modules
install -pm 644 %{SOURCE5} modules
install -pm 644 %{SOURCE6} modules
install -pm 644 %{SOURCE7} modules
install -pm 644 %{SOURCE8} modules
install -pm 644 %{SOURCE9} modules
install -pm 644 %{SOURCE10} modules
install -pm 644 %{SOURCE11} modules
install -pm 644 %{SOURCE12} modules
install -pm 644 %{SOURCE13} modules
install -pm 644 %{SOURCE14} modules
install -pm 644 %{SOURCE15} modules
install -pm 644 %{SOURCE16} modules

%install
mkdir -p %{buildroot}%{_rpmmacrodir}/
install -Dpm 644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}/
mkdir -p %{buildroot}%{_datadir}/modulefiles/rocm/
cp -p modules/* %{buildroot}%{_datadir}/modulefiles/rocm/
# Make directories users of modules will install to
for gpu in %{gpu_list}
do
    mkdir -p %{buildroot}%{_libdir}/rocm/$gpu/lib/cmake
    mkdir -p %{buildroot}%{_libdir}/rocm/$gpu/bin
done

%files
%license GPL
%{_rpmmacrodir}/macros.rocm

%files modules
%license GPL
%{_libdir}/rocm
%{_datadir}/modulefiles/rocm/

%changelog
%autochangelog
