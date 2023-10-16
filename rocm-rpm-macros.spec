Name:           rocm-rpm-macros
Version:        1.0
Release:        4%{?dist}
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


Requires:       environment-modules
BuildArch:      noarch
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


%install
mkdir -p %{buildroot}%{_rpmmacrodir}/
install -Dpm 644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}/
mkdir -p %{buildroot}%{_datadir}/modulefiles/rocm/
cp -p modules/* %{buildroot}%{_datadir}/modulefiles/rocm/

%files
%license GPL
%{_rpmmacrodir}/macros.rocm

%files modules
%license GPL
%{_datadir}/modulefiles/rocm/

%changelog
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
