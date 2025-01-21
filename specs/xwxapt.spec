Name:           xwxapt
Version:        3.4.1
Release:        16%{?dist}
Summary:        GTK+ graphical application for decoding and saving weather images

# Most files are GPLv2+ but some are GPLv3+ so combined work is GPLv3+
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later

URL:            http://www.5b4az.org/
Source0:        http://www.5b4az.org/pkg/apt/%{name}/%{name}-%{version}.tar.bz2
#add .desktop file
Source1:        %{name}.desktop
#temporary Icon
Source2:        %{name}.png
#Wrapper script for user config
Source3:        %{name}.sh.in

Patch1: xwxapt-3.4.1-fedora-c99.patch

BuildRequires: make
BuildRequires:  gcc gcc-c++
BuildRequires:  automake autoconf libtool gettext
BuildRequires:	alsa-lib-devel
BuildRequires:  gtk3-devel
BuildRequires:  rtl-sdr-devel
BuildRequires:  desktop-file-utils

Requires:	alsa-lib

%description
xwxapt is a GTK+ graphical version of wxapt. It uses the same decoding
engine as wxapt but it displays APT images at half-size as they are
received, storing the full-sized files when reception is completed. 

It also displays some status information (audio level, sync level,
sync status etc) and text messages as it runs.

%prep
%autosetup -p1


%build
./autogen.sh
%configure LDFLAGS="-lm"
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" PACKAGE_LIBS="$PACKAGE_LIBS -lm"


%install
# Install tries to install stuff to $HOME so do it manually...
install -pDm 0755 src/%{name} %{buildroot}%{_bindir}/%{name}.bin

#install default user configuration file
install -pDm 0644 %{name}/xwxaptrc %{buildroot}%{_datadir}/%{name}/xwxaptrc

#install wrapper script 
install -pDm 0755 %{SOURCE3} %{buildroot}%{_bindir}/xwxapt

# no upstream .desktop or icon yet so we'll use a temporary one
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp -p %{SOURCE2} ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/%{name}.png

desktop-file-install  \
        --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}


%files
%doc AUTHORS README NEWS
%doc doc/xwxapt.html
%license COPYING
%{_bindir}/%{name}*
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/*%{name}.desktop


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 3.4.1-15
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 09 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 3.4.1-13
- Rebuilt for new rtl-sdr

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Feb  9 2023 DJ Delorie <dj@redhat.com> - 3.4.1-10
- Fix C99 compatibility issue

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 06 2019 Richard Shaw <hobbes1069@gmail.com> - 3.4.1-1
- Update to 3.4.1.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-17.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-16.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-15.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-14.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-13.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-12.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-11.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-10.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-9.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-8.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-7.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-6.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-5.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-4.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.0-3.beta
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-2.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Apr 30 2010 Randall J. Berry 'Dp67' <dp67@fedoraproject.org> 2.0-1
- Upstream upgrade 2.0.Beta
- Fix .desktop file incude Network;
- BZ 525292 Audio setup error.
* Thu Apr 22 2010 Jon Ciesla <limb@jcomserv.net> - 1.2-4
- Fix for libm DSO Linking FTBFS, BZ 564864.
* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Wed Jan 14 2009 Randall J. Berry 'Dp67' <dp67@fedoraproject.org> 1.2-1
- Upstream upgrade to 1.2
- Mock build f9/f10/devel
- check rpmlint 3 packages and 1 specfiles checked; 0 errors, 0 warnings.
- submit for review
* Mon Jan 12 2009 Randall J. Berry 'Dp67' <dp67@fedoraproject.org> 1.1-2
- Mock build f9/f10/devel
- check rpmlint
* Sun Sep 21 2008 Randall J. Berry 'Dp67' <dp67@fedoraproject.org> 1.1-1
- Upstream upgrade to 1.1
- Build test for f9
* Sun Mar 02 2008 Sindre Pedersen Bjordal <sindrepb@fedoraproject.org> - 0.9-1
- Initial build
