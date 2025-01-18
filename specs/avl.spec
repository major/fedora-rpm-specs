Name:           avl
Version:        3.36
Release:        20%{?dist}
Summary:        Aerodynamic and flight-dynamic analysis of rigid aircrafts

# Plotlib is LGPLv2+, the rest is GPLv2+
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            http://web.mit.edu/drela/Public/web/avl/
Source0:        http://web.mit.edu/drela/Public/web/avl/avl%{version}.tgz
# The package does not ship a license file
Source1:        LICENSE.GPL
Source2:        LICENSE.LGPL
# Makefile variables and flags
Patch0:         avl3.36-makefile.patch

BuildRequires:  gcc-gfortran
BuildRequires:  libX11-devel
BuildRequires:  make
Requires:       xorg-x11-fonts-misc

%description
AVL is a program for the aerodynamic and flight-dynamic analysis of rigid aircraft
of arbitrary configuration. It employs an extended vortex lattice model for
the lifting surfaces, together with a slender-body model for fuselages and nacelles.
General nonlinear flight states can be specified. The flight dynamic analysis
combines a full linearization of the aerodynamic model about any flight state,
together with specified mass properties.


%prep
%autosetup -p1 -n Avl
cp %{SOURCE1} .
cp %{SOURCE2} .


%build
export FFLAGS="%{optflags}"
export CFLAGS="%{optflags}"

%make_build -C plotlib
%make_build -C eispack
%make_build -C bin


%install
%make_install -C bin BINDIR=%{_bindir}


%files
%doc version_notes.txt avl_doc.txt session1.txt session2.txt
%license LICENSE.GPL LICENSE.LGPL
%{_bindir}/avl


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.36-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 3.36-19
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.36-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.36-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.36-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.36-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.36-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.36-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.36-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.36-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.36-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.36-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.36-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.36-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.36-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 08 2017 Sandro Mani <manisandro@gmail.com> - 3.36-1
- Update to 3.36

* Wed Feb 01 2017 Sandro Mani <manisandro@gmail.com> - 3.35-6
- Rebuild (gfortran)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.35-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.35-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.35-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 12 2014 Sandro Mani <manisandro@gmail.com> - 3.35-1
- Update to version 3.35

* Sat Jan 25 2014 Sandro Mani <manisandro@gmail.com> - 3.32-5
- Rebuild without-fdefault-real-8

* Fri Sep 20 2013 Sandro Mani <manisandro@gmail.com> - 3.32-4
- Conflict with old avl

* Fri Sep 13 2013 Sandro Mani <manisandro@gmail.com> - 3.32-3
- Fix license

* Thu Sep 12 2013 Sandro Mani <manisandro@gmail.com> - 3.32-2
- Add license file

* Thu Sep 12 2013 Sandro Mani <manisandro@gmail.com> - 3.32-1
- Initial package for review
