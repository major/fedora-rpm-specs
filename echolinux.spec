%define _legacy_common_support 1
Name:		echolinux
Version:	0.17a
Release:	35%{?dist}
Summary:	Linux echoLink client

License:	GPL+
URL:		http://cqinet.sourceforge.net/
Source0:	echolinux-0.17a-nogsm.tar.gz
# We do not know the license for gsm.h (and libgsm.a)
# We use this script to remove gsm.h and libgsm.a before shipping it.
# Download the upstream tarball and invoke this script while in the
# tarball's directory:
# ./generate-echolinux-tarball.sh 1.0
Source1: generate-echolinux-tarball.sh
#xform changed include paths - https://sourceforge.net/tracker/index.php?func=detail&aid=2198156&group_id=56357&atid=480282
Patch0:		echolinux-0.17a-includes.patch
#allow env install paths - https://sourceforge.net/tracker/index.php?func=detail&aid=2198185&group_id=56357&atid=480282
Patch1:		echolinux-0.17a-installdir.patch
#do not link against static library (packaged .la file) - https://sourceforge.net/tracker/index.php?func=detail&aid=2198200&group_id=56357&atid=480282
Patch2:		echolinux-0.17a-nostatic.patch
#prefer -O2 instead of -O3
Patch3:		echolinux-0.17a-gcc.patch
Patch4:		echolinux-0.17a-optflags.patch
Patch5:		echolinux-c99.patch

BuildRequires:  gcc
BuildRequires:	xforms-devel, libXpm-devel, gsm-devel, desktop-file-utils
BuildRequires: make
#Requires:	

%description
EchoLinux is a "command line" driven engine that performs all of the actions
necessary to initiate sessions, accept connections and maintain connections
with other echoLink users. It also handles the compression/decompression of
the audio stream.

%prep
%setup -q
%patch0 -p1 -b .includes
%patch1 -p1 -b .installdir
%patch2 -p1 -b .nostatic
%patch3 -p1 -b .gcc
%patch4 -p1 -b .optflags
%patch5 -p1 -b .c99
%{__sed} -i 's/\r//' Using_EchoLinux.txt
%{__sed} -i 's/Encoding=UTF-8//g' %{name}.desktop
%{__sed} -i 's/.png//g' %{name}.desktop
%{__sed} -i 's/Application;Network;/Network;HamRadio;/g' %{name}.desktop


%build
make %{?_smp_mflags} -e CFLAGS="%{optflags}"


%install
rm -rf %{buildroot}
#fix perms on packages file
chmod -x README
mkdir -p %{buildroot}%{_bindir}
make install DESTDIR=%{buildroot}%{_bindir} INSTALL="install -p"
mkdir -p %{buildroot}%{_datadir}/pixmaps/
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
cp echolinux/*.txt echolinux/*.wav %{buildroot}%{_sysconfdir}/%{name}
cp pixmaps/echolinux_48x48.png %{buildroot}%{_datadir}/pixmaps/
desktop-file-install \
	--dir=%{buildroot}%{_datadir}/applications %{name}.desktop



%files
%doc gpl.txt README Using_EchoLinux.txt
%{_bindir}/echoaudio
%{_bindir}/echogui
%{_bindir}/echolinux
%config(noreplace) %{_sysconfdir}/echolinux
%{_datadir}/pixmaps/echolinux_48x48.png
%{_datadir}/applications/%{name}.desktop


%changelog
* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17a-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17a-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.17a-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.17a-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 10 2022 Florian Weimer <fweimer@redhat.com> - 0.17a-31
- Port to C99

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17a-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17a-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17a-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17a-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17a-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Apr 05 2020 Lucian Langa <lucilanga@gnome.eu.org> - 0.17a-25
- add temporary gcc10 fix

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17a-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17a-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17a-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17a-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17a-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17a-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17a-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17a-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.17a-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17a-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17a-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17a-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17a-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17a-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17a-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17a-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17a-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue May 18 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.17a-7
- rebuild (xforms)

* Fri Nov 27 2009 Lucian Langa <cooly@gnome.eu.org> - 0.17a-6
- improve desktop file (#530828)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17a-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 13 2009 Lucian Langa <cooly@gnome.eu.org> - 0.17a-4
- license tag fix
- fix compiler flags

* Thu Mar 12 2009 Lucian Langa <cooly@gnome.eu.org> - 0.17a-3
- include correct file for tarball generation

* Thu Dec 11 2008 Lucian Langa <cooly@gnome.eu.org> - 0.17a-2
- remove gsm.h and libgsm.a (license issue)

* Sun Sep 14 2008 Lucian Langa <cooly@gnome.eu.org> - 0.17a-1
- initial specfile


