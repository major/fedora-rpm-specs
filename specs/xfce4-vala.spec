%if 0%{?rhel} == 7
%global vala_version_api 0.34
%else
%global vala_version_api 0.56
%endif

%global srcurl  http://archive.xfce.org/src/bindings/%{name}

Name:           xfce4-vala
Version:        4.10.3
Release:        42%{?dist}
Summary:        Vala bindings for the Xfce framework

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://wiki.xfce.org/vala-bindings
# caution! %%version may not be evaluable in %%global
Source0:        %{srcurl}/%(echo %{version} |sed s:\..$::)/%{name}-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires: make
BuildRequires: exo-devel
BuildRequires: garcon-devel
BuildRequires: libxfce4ui-devel
BuildRequires: libxfce4util-devel
BuildRequires: xfce4-panel-devel
BuildRequires: xfconf-devel

BuildRequires: vala-devel

# Needed for %%{_datadir}/vala*/vapi directory
Requires: vala(api) = %{vala_version_api}

%description
Xfce4 Vala provides bindings for the Xfce framework


%prep
%setup -q

%build
%configure --with-vala-api=%{vala_version_api}
%make_build

%install
%make_install


%files
%license COPYING
%doc AUTHORS NEWS README
%{_datadir}/pkgconfig/xfce4-vala.pc
%{_datadir}/vala-%{vala_version_api}/vapi/*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.3-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 4.10.3-41
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.3-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.3-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.3-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.3-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.3-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jan 30 2022 Kevin Fenzi <kevin@scrye.com> - 4.10.3-35
- Rebuild for vala 0.56. Fixes rhbz#2042332

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 23 2021 Kalev Lember <klember@redhat.com> - 4.10.3-33
- Rebuilt for vala 0.54

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Apr 13 2021 Kalev Lember <klember@redhat.com> - 4.10.3-31
- Rebuilt for vala 0.52

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 Kalev Lember <klember@redhat.com> - 4.10.3-27
- Rebuilt for vala 0.48

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Kalev Lember <klember@redhat.com> - 4.10.3-25
- Rebuilt for vala 0.46

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 07 2019 Kalev Lember <klember@redhat.com> - 4.10.3-23
- Rebuilt for vala 0.44

* Sun Aug 12 2018 Raphael Groner <projects.rg@smart.ms> - 4.10.3-22
- fix evaluation of version for source0

* Sun Aug 12 2018 Raphael Groner <projects.rg@smart.ms> - 4.10.3-21
- Rebuilt for vala 0.41

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 20 2017 Kalev Lember <klember@redhat.com> - 4.10.3-18
- Rebuilt for vala 0.40

* Mon Aug 21 2017 Kalev Lember <klember@redhat.com> - 4.10.3-17
- Rebuilt for vala 0.38

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 Kalev Lember <klember@redhat.com> - 4.10.3-15
- Rebuilt for vala 0.36

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 22 2016 Kalev Lember <klember@redhat.com> - 4.10.3-13
- Rebuilt for vala 0.34

* Thu Mar 10 2016 Raphael Groner <projects.rg@smart.ms> - 4.10.3-12
- improve check of vala API version

* Mon Mar 07 2016 Raphael Groner <projects.rg@smart.ms> - 4.10.3-11
- Bump vala to 0.32
- modernize
- use vala version to see ABI breakage in rebuilds (BuildRequires)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec  4 2015 Peter Robinson <pbrobinson@fedoraproject.org> 4.10.3-10
- RHEL 7.2 ships with vala 0.26

* Mon Jul 20 2015 Kevin Fenzi <kevin@scrye.com> 4.10.3-9
- Fix vala deps on epel7

* Mon Jun 22 2015 Kevin Fenzi <kevin@scrye.com> 4.10.3-8
- Add conditional for epel7 and build epel7 version.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 27 2015 Kalev Lember <kalevlember@gmail.com> - 4.10.3-6
- Bump vala to 0.30
- Use new vala(api) virtual provide to pull in the right vala version

* Mon May 25 2015 Raphael Groner <projects.rg@smart.ms> - 4.10.3-5
- bump to vala 0.28

* Fri Nov 14 2014 poma <poma@gmail.com> 4.10.3-4
- Bump vala to 0.26. Fixes bug #1164387

* Sun Jun 08 2014 Kevin Fenzi <kevin@scrye.com> 4.10.3-3
- Bump vala to 0.24

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 19 2013 Kevin Fenzi <kevin@scrye.com> 4.10.3-1
- Update to 4.10.3 final version.

* Thu Aug 15 2013 Kevin Fenzi <kevin@scrye.com> 4.10.3-0.1.git20130815
- Initial version for Fedora
