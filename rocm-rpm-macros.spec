Name:           rocm-rpm-macros
Version:        1.0
Release:        10%{?dist}
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

%global gpu_list gfx8 gfx9 gfx10 gfx11


Requires:       environment-modules
ExclusiveArch:  x86_64
%description
This package contains ROCm RPM macros for building ROCm packages.

%package modules
Summary: ROCm enviroment modules
Requires: environment(modules)

%description modules
This package contains ROCm environment modules for switching
between different GPU families.

%prep
%setup -cT
install -pm 644 %{SOURCE0} .
install -pm 644 %{SOURCE1} .
mkdir modules
install -pm 644 %{SOURCE2} modules
install -pm 644 %{SOURCE3} modules
install -pm 644 %{SOURCE4} modules
install -pm 644 %{SOURCE5} modules
install -pm 644 %{SOURCE6} modules
install -pm 644 %{SOURCE7} modules
install -pm 644 %{SOURCE8} modules
install -pm 644 %{SOURCE9} modules


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
%dir %{_libdir}/rocm
%dir %{_libdir}/rocm/gfx*
%dir %{_libdir}/rocm/gfx*/bin
%dir %{_libdir}/rocm/gfx*/lib
%dir %{_libdir}/rocm/gfx*/lib/cmake
%{_datadir}/modulefiles/rocm/

%changelog
* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 12 2024 Tom Rix <trix@redhat.com> 1.0-9
- Use semicolon seperators

* Tue Dec 12 2023 Tom Rix <trix@redhat.com> 1.0-8
- Add gfx906, gfx908 and gfx90a modules

* Fri Nov 17 2023 Jeremy Newton <alexjnewt at hotmail dot com> 1.0-7
- Add more directory ownership

* Thu Nov 02 2023 Jeremy Newton <alexjnewt at hotmail dot com> 1.0-6
- change package to arched x86_64 to capture the correct libdir

* Sun Oct 22 2023 Tom Rix <trix@redhat.com> 1.0-5
- make directories rocblas will use

* Sat Oct 14 2023 Tom Rix <trix@redhat.com> 1.0-4
- Use fedora repo over personal repo

* Fri Oct 13 2023 Tom Rix <trix@redhat.com> 1.0-3
- Fix license
- Fix dist use in version

* Thu Oct 12 2023 Tom Rix <trix@redhat.com> 1.0-2
- Remove version for macros
- Combine modules as a subpackage

* Sun Oct 8 2023 Tom Rix <trix@redhat.com> 5.7.0-1
- Initial package
