%define debug_package %{nil}

Name:           gnome-rdp        
Version:        0.3.1.0
Release:        37%{?dist}
Summary:        Remote Desktop Protocol client for the GNOME desktop environment

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://sourceforge.net/projects/gnome-rdp
Source0:        http://downloads.sourceforge.net/%name/%{name}-%{version}.tar.gz
# Now the license is not include in the latest tarball
# I'll open the bug in the upstream
# wget -O COPYING-GNOME-RDP http://sourceforge.net/p/gnome-rdp/code/HEAD/tree/tags/gnome-rdp.0.2.3/COPYING?format=raw 
Source1:	COPYING-GNOME-RDP

# Mono only available on these:
ExclusiveArch: %{mono_arches}
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:   %{ix86}

BuildRequires:	gcc
BuildRequires:  glib2-devel >= 2.15.3
BuildRequires:  gtk2-devel >= 2.12.0  
BuildRequires:  mono-devel >= 1.9
BuildRequires:  mono-data-sqlite >= 1.9
BuildRequires:  gtk-sharp2-devel >= 1.9
BuildRequires:  gnome-sharp-devel >= 2.16.1
BuildRequires:  gnome-desktop-sharp >= 2.20.1
BuildRequires:  gnome-desktop-sharp-devel >= 2.20.1
BuildRequires:  gnome-keyring-sharp-devel
BuildRequires:  gettext
BuildRequires:  perl(XML::Parser)
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  desktop-file-utils
BuildRequires:  tigervnc
BuildRequires:  rdesktop
BuildRequires:  openssh-clients
BuildRequires:  gnome-terminal
BuildRequires:	libappindicator-sharp-devel
BuildRequires: make
Requires:       libappindicator
Requires:       rdesktop >= 1.6.0
Requires:	tigervnc
# for vncpasswd
Requires:	tigervnc-server

%description
gnome-rdp is a Remote Desktop Protocol client for the GNOME desktop
environment. It supports RDP, VNC and SSH. Configured sessions can be saved to
the built in list.

%prep
%setup -q
cp -a %{SOURCE1} .
sed -i 's/tight-vncviewer/vncviewer/' Sessions/SessionCollection.cs
sed -i 's/pkglib_SCRIPTS/programfiles_SCRIPTS/' Makefile.include
sed -i "s#gmcs#mcs#g" Makefile.*
sed -i "s#gmcs#mcs#g" gnome-rdp.make
sed -i "s#gmcs#mcs#g" configure*

%build
%configure 
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

install -d %{buildroot}%{_datadir}/applications
desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications \
	Menu/gnome-rdp.desktop 
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
install -pm 0644 Menu/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/



%files
%doc COPYING-GNOME-RDP
%{_bindir}/gnome-rdp
%{_libdir}/gnome-rdp
%{_datadir}/applications/gnome-rdp.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.1.0-36
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.0-26
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 06 2018 Luis Bazan <lbazan@fedoraproject.org> - 0.3.1.0-21
- Fix FTBS BZ #1604156

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.1.0-18
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1.0-14
- mono rebuild for aarch64 support

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.3.1.0-11
- Rebuild (mono4)

* Sun Jan  4 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.3.1.0-10
- Update ExclusiveArch, modernise spec

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Sep 13 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 0.3.1.0-7
- Fix #982788 by adding libappindicator to requires

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 7 2013 Eduardo Echeverria <echevemaster@gmail.com> - 0.3.1.0-5
- Fix errors with assembly of the executable

* Fri Jun 7 2013 Eduardo Echeverria <echevemaster@gmail.com> - 0.3.1.0-4
- Fix FTBFS

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jul 13 2012 Luis Bazan <bazanluis20@gmail.com> - 0.3.1.0-1
- New Upstream Version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu May 26 2011 Dan Horák <dan[at]danny.cz> - 0.2.3-9
- updated the supported arch list

* Mon May 16 2011 Tom Callaway <spot@fedoraproject.org> - 0.2.3-8
- use Mono.Data.Sqlite
- fix program to actually run

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 26 2009 Dennis Gilmore <dennis@ausil.us> - 0.2.3-6
- exclude sparc64

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 02 2009 John Anderson <john.e.anderson@gmail.com> - 0.2.3-4
- Fix vnc for bug #508302

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Sep 11 2008 John Anderson <john.e.anderson@gmail.com> - 0.2.3-2
- Changed licensing in package to GPL3 to match upstream
- Removed DESTDIR from build command

* Tue Aug 26 2008 John Anderson <john.e.anderson@gmail.com> - 0.2.3-1
- New upstream release
- Now using nant build
- Better description
- Added ssh, vnc requirements
- Listed reasons for excludes

* Thu Aug 07 2008 John Anderson <john.e.anderson@gmail.com> - 0.2.2.3-5
- Fixed startup script to work on i386 and x86_64, builds in koji, runs on fc10 alpha

* Tue Jul 22 2008 John Anderson <john.e.anderson@gmail.com> - 0.2.2.3-4
- Fixed sqlite dependency for x86_64, added excludes for ppc

* Mon Jul 21 2008 John Anderson <john.e.anderson@gmail.com> - 0.2.2.3-3	
- Fixed VTE sharp dependencies

* Wed Jul 16 2008 John Anderson <john.e.anderson@gmail.com> - 0.2.2.3-2
- Fixed comments from Christoph Wickert and Guido Ledermann per review (#448717)

* Tue May 27 2008 John Anderson <john.e.anderson@gmail.com> - 0.2.2.3-1
- Initial build.
