Name:           xfhell
Version:        3.5.1
Release:        13%{?dist}
Summary:        GTK based Ham Radio application for the Hellschreiber communications mode

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.5b4az.org/
Source0:        http://www.5b4az.org/pkg/%{name}/%{name}-%{version}.tar.bz2
#add .desktop file
Source1:        %{name}.desktop
#temporary Icon
Source2:        %{name}.png

Patch0:         xfhell-Makefile.patch
Patch1: xfhell-configure-c99.patch

BuildRequires: make
BuildRequires:  gcc gcc-c++
BuildRequires:  autoconf, automake, libtool
BuildRequires:  desktop-file-utils
BuildRequires:  alsa-lib-devel
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel


%description
xfhell is a GTK+ application for the "fuzzy" digital amateur radio 
communication mode known as Hellschreiber. 


%prep
%autosetup -p1


%build
./autogen.sh
export CFLAGS="%{optflags} `pkg-config --cflags gmodule-2.0`"
export LDFLAGS="%{optflags} -lm `pkg-config --libs gmodule-2.0`"
%configure
%make_build 


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# no upstream .desktop or icon yet
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/
cp -p %{SOURCE2} ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/%{name}.png

desktop-file-install \
        --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}

rm -f %{buildroot}%{_docdir}/%{name}/%{name}.1.gz
mkdir -p %{buildroot}%{_mandir}/man1
cp -a doc/%{name}.1.gz %{buildroot}%{_mandir}/man1/


%files
#Missing copy of the GPL, Notified upstream
%doc AUTHORS ChangeLog README
%doc doc/BDF_Spec.pdf doc/xfhell.html
%{_bindir}/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 3.5.1-12
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 Florian Weimer <fweimer@redhat.com> - 3.5.1-7
- C99 compatibility fixes (#2157935)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 19 2020 Richard Shaw <hobbes1069@gmail.com> - 3.5.1-1
- Update to 3.5.1.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 20 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 1.9-13
- Fix FTBFS with -Werror=format-security (#1037396, #1107276)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 10 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 1.9-10
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 7 2011 Randall J. Berry, N3LRX <dp67@fedoraproject.org> - 1.9-7
- linker error in build added libm.so

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.9-6
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 15 2010 Randall "Randy" Berry, N3LRX <dp67@fedoraproject.org> - 1.9-4
- Fix .desktop categories add Network;HamRadio;

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 11 2008 Sindre Pedersen Bjørdal <sindrepb@fedoraproject.org>- 1.9-1 
- New upstream release

* Sat Mar 01 2008 Robert 'Bob' Jensen <bob@bobjensen.com> - 1.4-4
- Fix Source0 Screwup again

* Sat Mar 01 2008 Robert 'Bob' Jensen <bob@bobjensen.com> - 1.4-3
- Fix Source0 Screwup

* Sat Mar 01 2008 Robert 'Bob' Jensen <bob@bobjensen.com> - 1.4-2
- Add .desktop and icon
- Submit for Review

* Sat Mar 01 2008 Robert 'Bob' Jensen <bob@bobjensen.com> - 1.4-1
- Upstream Version Bump

* Mon Dec 10 2007 Sindre Pedersen Bjørdal - 1.3-1
- Initial build
