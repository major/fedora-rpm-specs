%global fosrev fos93d0303aad
%global isdev 1

Name:           tkabber
Version:        1.1.2
Release:        21%{?fosrev:.%{fosrev}}%{?dist}
Summary:        Client for the Jabber instant messaging system

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://tkabber.jabber.ru/
Source:         %{name}-%{version}%{?isdev:-dev}.tar.gz
# for relase version:
#Source0:        http://files.jabber.ru/tkabber/%{name}-%{version}.tar.gz
# script to get tkabber from svn
Source1:        tkabber-snapshot.sh
Source2:        tkabber.png
Source3:        tkabber.desktop
Source4:        tkabber
Source5:        tkabber-remote
Patch0:         tkabber-1.1.2-install.patch

BuildArch:      noarch

BuildRequires: make
BuildRequires:  desktop-file-utils
Requires:       tcllib
Requires:       bwidget
Requires:       tcltls
Requires:       tkimg
Requires:       tdom
Requires:       tktray
Requires:       tcl-tclxml
Requires:       tcl-tkpng
Requires:       tcl-zlib


%description
Tkabber is a Free and Open Source client for the Jabber
instant messaging system. It's written in Tcl/Tk, and
works on many platforms. The choice of Tcl/Tk for a Jabber
client is three-fold:
* it is portable: once you install a Tcl/Tk interpreter on
  your system, the Tkabber script "just runs" — without having
  to compile anything;
* it is customizable: Tkabber reads a configuration file when
  it starts that tells it the settings of various parameters; and,
* it is extensible: the configuration file is actually a Tcl
  script, so you can replace or augment entire portions of Tkabber
  (if you're so inclined).

%prep
%setup -qn %{name}-%{version}%{?isdev:-dev}
%patch -P0 -p1 -b .install

%if "0%{isdev} > 0"
%{__rm} {,tclxmpp/}.fslckout
%endif

%build

# empty here

%install

make install-bin DESTDIR=%{buildroot}

desktop-file-install --dir=%{buildroot}/%{_datadir}/applications %{SOURCE3}

mkdir -p %{buildroot}%{_datadir}/pixmaps/
mkdir -p %{buildroot}%{_bindir}
cp %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/
cp %{SOURCE4} %{SOURCE5} %{buildroot}%{_bindir}

chmod 755 %{buildroot}%{_bindir}/tkabber
chmod 755 %{buildroot}%{_bindir}/tkabber-remote


%files
%doc AUTHORS COPYING ChangeLog README doc/tkabber.html
%{_bindir}/tkabber
%{_bindir}/tkabber-remote
%{_datadir}/tkabber
%{_datadir}/applications/tkabber.desktop
%{_datadir}/pixmaps/tkabber.png

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-21.fos93d0303aad
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.2-20.fos93d0303aad
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-19.fos93d0303aad
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-18.fos93d0303aad
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-17.fos93d0303aad
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-16.fos93d0303aad
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-15.fos93d0303aad
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-14.fos93d0303aad
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-13.fos93d0303aad
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-12.fos93d0303aad
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-11.fos93d0303aad
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-10.fos93d0303aad
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-9.fos93d0303aad
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-8.fos93d0303aad
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-7.fos93d0303aad
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-6.fos93d0303aad
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-5.fos93d0303aad
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 30 2017 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 1.1.2-4.fos93d0303aad
- Update to latest dev version.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 01 2015 Dmitrij S. Kryzhevich <krege@land.ru> - 1.1.2-1
- Update to 1.1.2.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3.svn2173
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 01 2015 Dmitrij S. Kryzhevich <krege@land.ru> - 1.1.1-2.svn2173
- Fix patch.

* Wed Apr 01 2015 Dmitrij S. Kryzhevich <krege@land.ru> - 1.1.1-1.svn2173
- Update to new 1.1.1+ svn, revisino 2173.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2.svn2150
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 02 2014 Dmitrij S. Kryzhevich <krege@land.ru> 1.1-1.svn2150
- Update to 1.1+ svn, revision 2150.
- Clean spec.

* Tue Jan 28 2014 Dmitrij S. Kryzhevich <krege@land.ru> - 1.0-1.svn2114
- Update to 1.0+ svn, revision 2114.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-7.svn1948
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-6.svn1948
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-5.svn1948
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-4.svn1948
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-3.svn1948
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 05 2010 Dmitrij S. Kryzhevich <krege@land.ru> - 0.11.1-2.svn1948
- Fix License.
* Fri Nov 05 2010 Dmitrij S. Kryzhevich <krege@land.ru> - 0.11.1-1.svn1948
- First build.