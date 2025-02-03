Name: libfilezilla
Version: 0.49.0
Release: 3%{?dist}
URL: https://lib.filezilla-project.org/
Summary: C++ Library for FileZilla
License: GPL-2.0-or-later

Source0: https://download.filezilla-project.org/%{name}/%{name}-%{version}.tar.xz
Patch0: gcc13.patch

%if 0%{?rhel} == 8
# libuv-devel not present on s390x on EL-8
ExcludeArch: s390x
%endif

BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: gnutls-devel
BuildRequires: libxcrypt-devel
BuildRequires: nettle-devel
BuildRequires: make

%description
libfilezilla is a small and modern C++ library, offering some basic
functionality to build high-performing, platform-independent programs.

%package devel
Summary: Development files for C++ Library for FileZilla
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
libfilezilla is a small and modern C++ library, offering some basic
functionality to build high-performing, platform-independent programs.

This package contains files needed to compile code using libfilezilla.

%prep
%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install

%ldconfig_scriptlets

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/libfilezilla.so.46*

%files devel
%doc doc/*
%{_includedir}/*
%{_libdir}/libfilezilla.so
%{_libdir}/pkgconfig/libfilezilla.pc

%changelog
* Sat Feb 01 2025 Björn Esser <besser82@fedoraproject.org> - 0.49.0-3
- Add explicit BR: libxcrypt-devel

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.49.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 15 2024 Gwyn Ciesla <gwync@protonmail.com> - 0.49.0-1
- 0.49.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.48.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 10 2024 Gwyn Ciesla <gwync@protonmail.com> - 0.48.1-1
- 0.48.1

* Wed Jun 26 2024 Gwyn Ciesla <gwync@protonmail.com> - 0.48.0-1
- 0.48.0

* Mon Apr 15 2024 Gwyn Ciesla <gwync@protonmail.com> - 0.47.0-1
- 0.47.0

* Tue Feb 06 2024 Gwyn Ciesla <gwync@protonmail.com> - 0.46.0-1
- 0.46.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.45.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.45.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 26 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.45.0-1
- 0.45.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.41.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 27 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.41.1-1
- 0.41.1

* Fri Mar 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.40.0-4
- migrated to SPDX license

* Fri Jan 20 2023 Scott Talbert <swt@techie.net> - 0.40.0-3
- Fix FTBFS with GCC 13

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.40.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.40.0-1
- 0.40.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.38.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.38.1-1
- 0.38.1

* Fri Jul 08 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.38.0-1
- 0.38.0

* Mon May 02 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.37.2-1
- 0.37.2

* Fri Apr 08 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.37.1-1
- 0.37.1

* Thu Feb 03 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.36.0-1
- 0.36.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.35.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 09 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.35.0-1
- 0.35.0

* Tue Oct 26 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.34.2-1
- 0.34.2

* Tue Oct 19 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.34.1-1
- 0.34.1

* Tue Oct 12 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.34.0-1
- 0.34.0

* Tue Sep 14 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.32.0-1
- 0.32.0

* Mon Aug 09 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.31.1-1
- 0.31.1

* Wed Jul 28 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.31.0-1
- 0.31.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 09 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.30.0-1
- 0.30.0

* Fri Jul 02 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.29.0-1
- 0.29.0

* Tue May 04 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.28.0-1
- 0.28.0

* Mon Mar 15 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.27.1-1
- 0.27.1

* Thu Mar 04 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.27.0-1
- 0.27.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 17 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.26.0-1
- 0.26.0

* Mon Oct 19 2020 Jeff Law <law@redhat.com> - 0.25.0-2
- Fix missing #include for gcc-11

* Tue Oct 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.25.0-1
- 0.25.0

* Thu Aug 27 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.24.1-1
- 0.24.1

* Fri Aug 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.24.0-1
- 0.24.0

* Wed Aug 12 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.23.0-3
- Exclude s390x on EL-8 due to missing libuv-devel

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.23.0-1
- 0.23.0

* Tue May 12 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.22.0-1
- 0.22.0

* Mon Apr 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.21.0-1
- 0.21.0

* Tue Mar 10 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.20.2-1
- 0.20.2

* Mon Feb 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.20.1-1
- 0.20.1

* Fri Feb 14 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.20.0-1
- 0.20.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.19.3-1
- 0.19.3

* Thu Dec 19 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.19.2-1
- 0.19.2

* Fri Nov 15 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.19.1-1
- 0.19.1

* Thu Nov 07 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.19.0-1
- 0.19.0

* Mon Sep 23 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.18.2-2
- GCC 10 patch, https://trac.filezilla-project.org/ticket/12000

* Mon Sep 16 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.18.2-1
- 0.18.2

* Thu Aug 15 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.18.1-1
- 0.18.1

* Fri Aug 02 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.18.0-1
- 0.18.0

* Wed Jul 31 2019 Phil Wyett <philwyett@kathenas.org> - 0.17.1-3
- Use HTTPS and fix Source0 URL.
- Remove old unused patch.
- Modernize and cleanup spec file.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.17.1-1
- 0.17.1

* Tue Apr 30 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.16.0-1
- 0.16.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 26 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.15.1-1
- 0.15.1

* Fri Oct 19 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.15.0-1
- 0.15.0

* Fri Oct 05 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.14.0-1
- 0.14.0

* Fri Sep 21 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.13.2-1
- 0.13.2.

* Tue Sep 11 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.13.1-1
- Latest upstream.

* Tue Jul 17 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.13.0-1
- Latest upstream.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 11 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.12.3-1
- Latest upstream.

* Mon May 07 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.12.2-1
- Latest upstream.

* Fri Feb 23 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.12.1-1
- Latest upstream.

* Tue Feb 20 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.12.0-1
- Latest upstream.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.11.2-1
- Latest upstream.

* Wed Nov 01 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.11.1-1
- Latest upstream.

* Fri Sep 29 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.11.0-1
- Latest upstream.

* Mon Aug 14 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.10.1-1
- Latest upstream.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.10.0-1
- Latest upstream.

* Fri Jun 02 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.9.2-2
- Patch for filezilla build issue, from upstream.

* Thu May 25 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.9.2-1
- Latest upstream.

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Thu Feb 23 2017 Jon Ciesla <limburgher@gmail.com> - 0.9.1-1
- Latest upstream.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 29 2016 Jon Ciesla <limburgher@gmail.com> - 0.9.0-1
- Latest upstream.

* Wed Oct 26 2016 Jon Ciesla <limburgher@gmail.com> - 0.8.0-1
- Latest upstream.

* Mon Oct 03 2016 Jon Ciesla <limburgher@gmail.com> - 0.7.1-1
- Latest upstream.

* Mon Sep 26 2016 Jon Ciesla <limburgher@gmail.com> - 0.7.0-1
- Latest upstream.

* Thu Jul 28 2016 Jon Ciesla <limburgher@gmail.com> - 0.6.1-1
- Latest upstream.

* Thu Jul 21 2016 Jon Ciesla <limburgher@gmail.com> - 0.6.0-1
- Latest upstream.

* Tue Jun 21 2016 Jon Ciesla <limburgher@gmail.com> - 0.5.3-1
- Latest upstream.

* Sun May 22 2016 Jon Ciesla <limburgher@gmail.com> - 0.5.2-1
- Latest upstream.

* Mon Apr 25 2016 Jon Ciesla <limburgher@gmail.com> - 0.5.0-1
- Latest upstream.

* Mon Apr 04 2016 Jon Ciesla <limburgher@gmail.com> - 0.4.0.1-2
- Dropped buildroot, Group, buildroot scrup, and added --disable-static and
- isa-specific Requires.

* Tue Mar 15 2016 Jon Ciesla <limburgher@gmail.com> - 0.4.0.1-1
- Initial package creation.
