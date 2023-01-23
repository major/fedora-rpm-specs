Name:           tkgate
Version:        2.0
Release:        39.beta10%{?dist}
Summary:        An event driven digital circuit simulator

License:        GPLv2+
URL:            http://www.tkgate.org/

Patch0:         tkgate-2.0-doc.patch
Patch1:         tkgate-2.0-lm.patch
# From debian wheezy
Patch2:         tkgate-2.0-typos.patch
# From debian wheezy
Patch3:         tkgate-2.0-hardening.patch

Source0:        http://www.tkgate.org/downloads/%{name}-%{version}-b10.tgz

%{?el5:BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)}

# el5/el6 have been shipped with vendor prefixed desktop files
# We must continue to do so until EOL of these distros.
%{?el5:%global vendor_desktop 1}
%{?el6:%global vendor_desktop 1}

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  tk-devel tcl-devel libICE-devel libSM-devel
BuildRequires:  desktop-file-utils

Requires:       electronics-menu

%description
TkGate is a event driven digital circuit simulator
based on Verilog. TkGate
supports a wide range of primitive circuit elements as
well as user-defined modules for hierarchical design.

%package ca
Summary:           Locales and examples for tkgate, Digital Circuit Simulator
Requires:          %{name} = %{version}-%{release}
Supplements:       (%{name} = %{version}-%{release} and langpacks-ca)
%{?!el5:BuildArch:         noarch}

%description ca
This package contains the Catalan locales and examples for tkgate, 
Digital Circuit Simulator

%package cs
Summary:           Locales and examples for tkgate, Digital Circuit Simulator
Requires:          %{name} = %{version}-%{release}
Supplements:       (%{name} = %{version}-%{release} and langpacks-cs)
%{?!el5:BuildArch:         noarch}

%description cs
This package contains the Czech locales and examples for tkgate, 
Digital Circuit Simulator

%package cy
Summary:           Locales and examples for tkgate, Digital Circuit Simulator
Requires:          %{name} = %{version}-%{release}
Supplements:       (%{name} = %{version}-%{release} and langpacks-cy)
%{?!el5:BuildArch:         noarch}

%description cy
This package contains the Welsh locales and examples for tkgate, 
Digital Circuit Simulator

%package de
Summary:           Locales and examples for tkgate, Digital Circuit Simulator
Requires:          %{name} = %{version}-%{release}
Supplements:       (%{name} = %{version}-%{release} and langpacks-de)
%{?!el5:BuildArch:         noarch}

%description de
This package contains the German locales and examples for tkgate, 
Digital Circuit Simulator

%package es
Summary:           Locales and examples for tkgate, Digital Circuit Simulator
Requires:          %{name} = %{version}-%{release}
Supplements:       (%{name} = %{version}-%{release} and langpacks-es)
%{?!el5:BuildArch:         noarch}

%description es
This package contains the Spanish locales and examples for tkgate, 
Digital Circuit Simulator

%package fr
Summary:           Locales and examples for tkgate, Digital Circuit Simulator
Requires:          %{name} = %{version}-%{release}
Supplements:       (%{name} = %{version}-%{release} and langpacks-fr)
%{?!el5:BuildArch:         noarch}

%description fr
This package contains the French locales and examples for tkgate, 
Digital Circuit Simulator

%package it
Summary:           Locales and examples for tkgate, Digital Circuit Simulator
Requires:          %{name} = %{version}-%{release}
Supplements:       (%{name} = %{version}-%{release} and langpacks-it)
%{?!el5:BuildArch:         noarch}

%description it
This package contains the Italian locales and examples for tkgate, 
Digital Circuit Simulator


%package ja
Summary:           Locales and examples for tkgate, Digital Circuit Simulator
Requires:          %{name} = %{version}-%{release}
Supplements:       (%{name} = %{version}-%{release} and langpacks-ja)
%{?!el5:BuildArch:         noarch}

%description ja
This package contains the Japanese locales and examples for tkgate, 
Digital Circuit Simulator


%prep
%setup -q -n %{name}-%{version}-b10

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# propagate paths to sources
sed -i "s|\"\${tkg_gateHome}/libexec/verga\"|\"%{_bindir}/verga\"|" scripts/parms.tcl
sed -i "s|\"%s/libexec/tkgate\",TkGate\.homedir|\"%{_bindir}/tkgate\"|" src/tkgate/verilog_out.c

sed -i "s|license.txt||" scripts/license.tcl
sed -i "s|TKGATE_LIBDIRS=\"\(.*\)\"|TKGATE_LIBDIRS=\"\1 %{_libdir}\"|" configure
# E: backup-file-in-package
find . -type f -name "*~" -exec rm -f  {} ';'
find . -type f -name "\#*\#" -exec rm -f  {} ';'
find . -type f \( -name "*.bak" -o -name "*.orig" -o -name "*.old" -o -name "*.orig2" \) -delete
find . -type f -name orig-messages -delete

# spurious-executable-perm
chmod 0755 scripts/tree.tcl
chmod 0644 test/verga/maketests.sh
chmod 0644 test/verga/runtests.sh

# E: zero-length
%{__rm} -f locale/{en,ja}/tutorials/definition.txt
%{__rm} -f bindings/none
%{__rm} -f scripts/dip.tcl
%{__rm} -f test/verga/grammar.out


cat > %{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Digital circuit simulator
GenericName=Verilog circuit simulator
Comment=TkGate
Type=Application
Exec=tkgate
Icon=tkgate
Categories=Engineering;Electronics;
EOF


%build
CFLAGS="%{optflags} -DUSE_INTERP_RESULT -std=gnu89"
%configure
%{__make} %{?_smp_mflags} 


%install
%{?el5:%{__rm} -rf %{buildroot}}
%{__make} INSTALL="install -p" install DESTDIR=%{buildroot}

# Symlink points to BuildRoot:
%{__rm} -rf %{buildroot}%{_datadir}/%{name}/libexec/


# desktop file and its icon
desktop-file-install %{?vendor_desktop:--vendor fedora} \
    --dir %{buildroot}%{_datadir}/applications \
    %{name}.desktop

install -d %{buildroot}%{_datadir}/pixmaps/
install -pm 0644 images/run01.gif %{buildroot}%{_datadir}/pixmaps/%{name}.png
cp -p site-preferences %{buildroot}%{_datadir}/%{name}/site-preferences

%files ca
%{_datadir}/%{name}/locale/ca/*

%files cs
%{_datadir}/%{name}/locale/cs/*

%files cy
%{_datadir}/%{name}/locale/cy/*

%files de
%{_datadir}/%{name}/locale/de/*

%files es
%{_datadir}/%{name}/locale/es/*

%files fr
%{_datadir}/%{name}/locale/fr/*

%files it
%{_datadir}/%{name}/locale/it/*

%files ja
%{_datadir}/%{name}/locale/ja/*


%files
%doc README README.verga COPYING
%doc license.txt pkg-comment pkg-descr TODO
%doc doc/ test/
%{_bindir}/gmac
%{_bindir}/%{name}
%{_bindir}/verga
%{_datadir}/%{name}
%{_mandir}/man1/gmac.1.gz
%{_mandir}/man1/tkgate.1.gz
%{_mandir}/man1/verga.1.gz
%{_datadir}/applications/%{?vendor_desktop:fedora-}%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%exclude %{_datadir}/%{name}/locale/ca
%exclude %{_datadir}/%{name}/locale/cs
%exclude %{_datadir}/%{name}/locale/cy
%exclude %{_datadir}/%{name}/locale/de
%exclude %{_datadir}/%{name}/locale/es
%exclude %{_datadir}/%{name}/locale/fr
%exclude %{_datadir}/%{name}/locale/it
%exclude %{_datadir}/%{name}/locale/ja

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-39.beta10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 11 2023 Florian Weimer <fweimer@redhat.com> - 2.0-38.beta10
- Build in C89 mode (#2160043)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-37.beta10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-36.beta10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-35.beta10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-34.beta10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-33.beta10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-32.beta10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-31.beta10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-30.beta10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-29.beta10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-28.beta10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-27.beta10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-26.beta10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-25.beta10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Mar 12 2016 Parag Nemade <pnemade AT redhat DOT com> - 2.0-24.beta10
- Add Supplements: for https://fedoraproject.org/wiki/Packaging:Langpacks guidelines

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-23.beta10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-22.beta10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-21.beta10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jul 12 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.0-20.beta10
- Append -DUSE_INTERP_RESULT to CFLAGS to work-around Tcl/Tk-8.6
  incompatibilities (FTBFS RHBZ #1107452).
- Adopt tkgate-2.0-typos.patch, tkgate-2.0-hardening.patch from Debian
  (FTBFS RHBZ #1107452, RHBZ #1037359).
- Partially modernize spec.
- Don't ship *.orig2 editor backup files.
- Make locale packages noarch.
- Fix paths to tools.
- Rebase patches.
- Reflect Source0: having changed.

* Sat Jul 12 2014 Ville Skyttä <ville.skytta@iki.fi> - 2.0-19.beta10
- Don't ship editor backup files
- Fix bogus dates in %%changelog

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-18.beta10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 2.0-17.beta10
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-16.beta10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-15.beta10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Feb 14 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 2.0-14.beta10
- Remove vendor tag from desktop file

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-13.beta10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-12.beta10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-11.beta10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Mar 23 2010 Thibault North <tnorth [AT] fedoraproject DOT org> - 2.0-10.beta10
- Build fix (thanks Bruno Wolff)

* Wed Jan 20 2010 Thibault North <tnorth [AT] fedoraproject DOT org> - 2.0-9.beta10
- Fixes

* Wed Jan 20 2010 Thibault North <tnorth [AT] fedoraproject DOT org> - 2.0-8.beta10
- updated to beta 10

* Sat Aug 29 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 2.0-7.beta9
- updated to beta 9

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-6.beta7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 6 2009 Thibault North <tnorth [AT] fedoraproject DOT org> - 2.0-5.beta7
- Minor fixes required for the package

* Thu Mar 5 2009 Thibault North <tnorth [AT] fedoraproject DOT org> - 2.0-4.beta7
- Fixes in installed files

* Tue Feb 24 2009 Thibault North <tnorth [AT] fedoraproject DOT org> - 2.0-1.beta7
- Updated to beta7

* Thu Feb 19 2009 Thibault North <tnorth [AT] fedoraproject DOT org> - 2.0-3.beta6
- Updated to beta6
- Separated locales
- Compilation fixes for 64 bits arch

* Wed Jan 21 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 2.0-2.beta4
- updated to beta4

* Sat Dec 06 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 2.0-1.alpha11
- Initial package for fedora
