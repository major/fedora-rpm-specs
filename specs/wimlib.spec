Name:           wimlib
Version:        1.14.4
Release:        4%{?dist}
Summary:        Open source Windows Imaging (WIM) library

# wimlib is dual-licensed (GPL-3.0-or-later/LGPL-3.0-or-later) but is linked to
# libntfs-3g (GPL-3.0-or-later), utilities are GPL-3.0-or-later, some internal
# headers are MIT
License:        GPL-3.0-or-later AND MIT
URL:            https://wimlib.net/
Source0:        %{url}/downloads/%{name}-%{version}.tar.gz
# Disable tests requiring mount privileges
Patch0:         %{name}-1.14.3-tests.patch

%if 0%{?fedora} > 41
BuildRequires:  autoconf
BuildRequires:  libtool
%endif
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(libntfs-3g)

%description
wimlib is a C library for creating, modifying, extracting, and mounting files in
the Windows Imaging Format (WIM files). wimlib and its command-line frontend
'wimlib-imagex' provide a free and cross-platform alternative to Microsoft's
WIMGAPI, ImageX, and DISM.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.


%package utils
Summary:        Tools for creating, modifying, extracting, and mounting WIM files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description utils
This package provides tools for creating, modifying, extracting, and mounting
files in the Windows Imaging Format (WIM files).


%prep
%autosetup -p0


%build
# Ensure build files match the installed Automake version
%if 0%{?fedora} > 41
autoreconf -fiv
%endif
%configure \
    --disable-silent-rules \
    --disable-static
# Remove Rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build


%install
%make_install
find $RPM_BUILD_ROOT -name "*.la" -delete


%check
%make_build check


%files
%doc NEWS.md README.md
%license COPYING COPYING.GPLv3
%{_libdir}/*.so.15*


%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc


%files utils
%{_bindir}/*
%{_mandir}/man1/*.1.*


%changelog
* Sat Jan 25 2025 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.14.4-4
- Fix FTBFS (RHBZ #2341541)
- Drop useless BuildRequires

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Mar 02 2024 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.14.4-1
- Update to 1.14.4

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Sep 24 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.14.3-1
- Update to 1.14.3
- Switch license tag to SPDX

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 03 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.13.6-1
- Update to 1.13.6
- Update license tag (CC0 replaced by MIT)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 01 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.13.5-1
- Update to 1.13.5

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.13.4-4
- Rebuilt with OpenSSL 3.0.0

* Thu Sep 02 2021 Neal Gompa <ngompa@fedoraproject.org> - 1.13.4-3
- Rebuild for ntfs-3g soname bump

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.13.4-1
- Update to 1.13.4

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 27 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.13.3-1
- Update to 1.13.3

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.13.2-1
- Update to 1.13.2

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 26 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.13.1-1
- Initial RPM release
