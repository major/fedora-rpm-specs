Name:       vapoursynth
Version:    70
Release:    1%{?dist}
Summary:    Video processing framework with simplicity in mind
License:    LGPL-2.1-only
URL:        http://www.vapoursynth.com

Source0:    https://github.com/%{name}/%{name}/archive/R%{version}/%{name}-R%{version}.tar.gz
Patch0:     %{name}-version-info.patch

BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  nasm
BuildRequires:  pkgconfig(tesseract)
BuildRequires:  pkgconfig(zimg)
BuildRequires:  python3-devel

%description
VapourSynth is an application for video manipulation. Or a plugin. Or a library.
It’s hard to tell because it has a core library written in C++ and a Python
module to allow video scripts to be created.

%package        libs
Summary:        VapourSynth's core library with a C++ API
Obsoletes:      lib%{name} < %{version}-%{release}
Provides:       lib%{name} == %{version}-%{release}
Obsoletes:      %{name}-plugins < %{version}-%{release}
Provides:       %{name}-plugins == %{version}-%{release}

%description    libs
VapourSynth's core library with a C++ API.

%package -n     python3-%{name}
Summary:        Python interface for VapourSynth

%description -n python3-%{name}
Python interface for VapourSynth/VSSCript.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.

%package        tools
Summary:        Extra tools for VapourSynth

%description    tools
This package contains the vspipe tool for interfacing with VapourSynth.

%prep
%autosetup -p1 -n %{name}-R%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
autoreconf -vif
%configure \
    --disable-static \
    --enable-x86-asm \
    --enable-core \
    --enable-vsscript \
    --enable-vspipe \
    --enable-python-module

%make_build

# Make libraries available for Python linking
ln -sf .libs build
%pyproject_wheel

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete

%pyproject_install
%pyproject_save_files %{name}

# Create plugin directory
mkdir -p %{buildroot}%{_libdir}/%{name}

# Let RPM pick up docs in the files section
rm -fr %{buildroot}%{_docdir}/%{name}

%check
#{python3} -m pytest -v
%tox

%files libs
%doc ChangeLog
%license COPYING.LESSER
%dir %{_libdir}/%{name}
%{_libdir}/lib%{name}.so.*
%{_libdir}/lib%{name}-script.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}-script.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}-script.pc

%files tools
%{_bindir}/vspipe

%files -n python3-%{name} -f %{pyproject_files}
%{python3_sitearch}/%{name}.so

%changelog
* Wed Jan 29 2025 Simone Caronni <negativo17@gmail.com> - 70-1
- Update to version 70.
- Trim changelog.
- Clean up SPEC file, switch to Python packaging guidelines for Python module.
- Fix License tag.
- Enable tests.

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 68-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 68-4
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 68-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 68-2
- Rebuilt for Python 3.13

* Wed May 22 2024 Simone Caronni <negativo17@gmail.com> - 68-1
- Update to R68.

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 65-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov 02 2023 Simone Caronni <negativo17@gmail.com> - 65-1
- Update to version R65.

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 63-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 01 2023 Python Maint <python-maint@redhat.com> - 63-2
- Rebuilt for Python 3.12

* Fri Jun 30 2023 Simone Caronni <negativo17@gmail.com> - 63-1
- Update to R63.

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 58-5
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 58-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild
