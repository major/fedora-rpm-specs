Name:           lxrandr
Version:        0.3.2
Release:        11%{?dist}
Summary:        Simple monitor configuration tool

License:        GPLv3+
URL:            http://lxde.org/
#VCS: git:git://lxde.git.sourceforge.net/gitroot/lxde/lxrandr
Source0:        http://downloads.sourceforge.net/sourceforge/lxde/%{name}-%{version}.tar.xz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  %{_bindir}/xsltproc
BuildRequires:  docbook-utils
BuildRequires:  docbook-style-xsl
Requires:       xrandr

%description
LXRandR is a simple monitor configuration tool utilizing X RandR extension. 
It's a GUI frontend of the command line program xrandr and manages screen 
resolution and external monitors. When you run LXRandR with an external 
monitor or projector connected, its GUI will change and show you some options 
to quickly configure the external device.

LXRandR is the standard screen manager of LXDE, the Lightweight X11 Desktop 
Environment, but can be used in other desktop environments as well.


%prep
%setup -q
# quick fix for the icon
sed -i 's/^Icon=display/Icon=video-display/g' data/lxrandr.desktop.in


%build
%configure \
	--enable-man \
	--disable-silent-rules \
	%{nil}
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
desktop-file-install                                       \
  --delete-original                                        \
  --add-category="HardwareSettings;GTK;"                   \
  --dir=${RPM_BUILD_ROOT}%{_datadir}/applications          \
  ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop
%find_lang %{name}



%files -f %{name}.lang
%doc AUTHORS COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1.*


%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Adam Jackson <ajax@redhat.com> - 0.3.2-5
- Require xrandr not xorg-x11-server-utils

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar  1 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.2-1
- 0.3.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb  7 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.1-5
- Handle the case that monitor name contains dot (bug 1542596)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 28 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.1-1
- 0.3.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.0-1
- 0.3.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.1.2-2
- Rebuild for new libpng

* Sun Aug 28 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.2-1
- Update to 0.1.2
- BuildRequire intltool

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 23 2009 Christoph Wickert <fedora christoph-wickert de> - 0.1.1-3
- Workaround for infinite loop that causes FTBFS (#538905)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 07 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.1-1
- Update to 0.1.1
- Include new manpage

* Sun Nov 09 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.1-1
- Initial Fedora package
