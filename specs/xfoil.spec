Name:           xfoil
Version:        6.99
Release:        23%{?dist}
Summary:        Subsonic Airfoil Development System

# Plotlib is LGPLv2+, the rest is GPLv2+
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            http://web.mit.edu/drela/Public/web/xfoil/
Source0:        http://web.mit.edu/drela/Public/web/xfoil/%{name}%{version}.tgz
# The package does not ship a license file
Source1:        LICENSE.GPL
Source2:        LICENSE.LGPL
# Makefile variables and flags
Patch0:         xfoil-6.99-makefile.patch
# Code fixes (from debian package)
Patch1:         xfoil-6.99-xfoil-fixes.patch
Patch2:         xfoil-6.99-fix-write-after-end.patch
Patch3:         xfoil-6.99-pxplot-args.patch
# Set osmap file location
Patch4:         xfoil-6.99-default-osfile.patch

BuildRequires: make
BuildRequires:  gcc-gfortran libX11-devel
Requires:       xorg-x11-fonts-misc


%description
XFOIL is an interactive program for the design and analysis of subsonic
isolated airfoils.


%prep
%autosetup -p1 -n Xfoil
cp %{SOURCE1} .
cp %{SOURCE2} .


%build
export FFLAGS="-fallow-argument-mismatch %{optflags}"
export CFLAGS="%{optflags} -DDEFAULT_OSFILE=\\\"%{_datadir}/%{name}/osmap.dat\\\""

%make_build -C orrs/bin osgen
pushd orrs
./bin/osgen osmaps_ns.lst
popd
%make_build -C plotlib
%make_build -C bin


%install
%make_install -C bin BINDIR=%{_bindir}
install -Dpm 0644 orrs/osmap.dat %{buildroot}/%{_datadir}/%{name}/osmap.dat


%files
%license LICENSE.GPL LICENSE.LGPL
%doc sessions.txt version_notes.txt xfoil_doc.txt
%{_datadir}/%{name}/
%{_bindir}/xfoil
%{_bindir}/pplot
%{_bindir}/pxplot


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.99-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 6.99-22
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.99-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.99-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.99-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.99-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.99-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.99-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.99-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.99-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.99-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.99-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.99-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.99-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.99-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.99-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.99-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.99-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.99-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.99-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Sandro Mani <manisandro@gmail.com> - 6.99-3
- Rebuild (gfortran)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.99-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 05 2015 Sandro Mani <manisandro@gmail.com> - 6.99-1
- Update to 6.99

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.97-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.97-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.97-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Jan 25 2014 Sandro Mani <manisandro@gmail.com> - 6.97-4
- Build without -fdefault-real-8

* Thu Sep 12 2013 Sandro Mani <manisandro@gmail.com> - 6.97-3
- Fix license

* Thu Sep 12 2013 Sandro Mani <manisandro@gmail.com> - 6.97-2
- Add license file

* Thu Sep 12 2013 Sandro Mani <manisandro@gmail.com> - 6.97-1
- Initial package for review
