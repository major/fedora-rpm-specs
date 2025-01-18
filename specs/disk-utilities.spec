# IPF support requires libcapsimage which is not distributable in Fedora
%bcond_with ipf

Name:           disk-utilities
Version:        2021.03.20
Release:        10%{?dist}
Summary:        Utilities for ripping, dumping, analysing, and modifying disk images

License:        Unlicense
URL:            https://github.com/keirf/Disk-Utilities
Source0:        %{url}/archive/%{version}/Disk-Utilities-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
%if %{with ipf}
BuildRequires:  libcapsimage-devel
%endif

%description
Disk Utilities is a collection of utilities for ripping, dumping, analysing,
and modifying disk images.

%package -n     libdisk
Summary:        A library for converting and manipulating disk images

%description -n libdisk
libdisk is a library for converting and manipulating disk images. It can
create disk images in a range of formats from Kryoflux STREAM and SPS/IPF
images (among others), and then allow these to be accessed and modified.

%package -n     libdisk-devel
Summary:        Development files for libdisk
Requires:       libdisk%{?_isa} = %{version}-%{release}

%description -n libdisk-devel
The libdisk-devel package contains libraries and header files for
developing applications that use libdisk.

%prep
%autosetup -n Disk-Utilities-%{version}

%build
%set_build_flags
%if %{with ipf}
export caps=y
%endif
%make_build

%install
export PREFIX="%{buildroot}%{_prefix}"
%if %{with ipf}
export caps=y
%endif
%make_install LIBDIR="%{buildroot}%{_libdir}"

%files
%license COPYING
%doc README.md
%{_bindir}/*
%{_datadir}/disk-analyse

%files -n libdisk
%license COPYING
%{_libdir}/libdisk.so.0*

%files -n libdisk-devel
%{_includedir}/libdisk
%{_libdir}/libdisk.so

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2021.03.20-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2021.03.20-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2021.03.20-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2021.03.20-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2021.03.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2021.03.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.03.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.03.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2021.03.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Apr  4 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 2021.03.20-1
- Update to 2021.03.20

* Sat Jan 23 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0-0.1.20210317git2ec77a4
- Initial package
