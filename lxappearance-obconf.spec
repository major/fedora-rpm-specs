# Review at https://bugzilla.redhat.com/show_bug.cgi?id=630184

%global git_snapshot 0
%global git_rev 5fad820707cdf6a565f909e483820b7a49bd4a36
%global git_date 20120304

%if 0%{?git_snapshot}
%global git_short %(echo %{git_rev} | cut -c-8)
%global git_version %{git_date}git%{git_short}
%endif

# Source0 was generated as follows:
# git clone git://lxde.git.sourceforge.net/gitroot/lxde/lxappearance-obconf
# cd lxappearance-obconf
# git archive --format=tar --prefix=lxappearance-obconf/ %{git_short} | bzip2 > lxappearance-obconf-%{?git_version}.tar.bz2

Name:           lxappearance-obconf
Version:        0.2.3
Release:        14%{?git_version:.%{?git_version}}%{?dist}
Summary:        Plugin to configure Openbox inside LXAppearance

License:        GPLv2+
URL:            http://lxde.org/
#VCS: git:git://lxde.git.sourceforge.net/gitroot/lxde/lxappearance-obconf
%if 0%{?git_snapshot}
Source0:        %{name}-%{?git_version}.tar.bz2
%else
Source0:        http://downloads.sourceforge.net/sourceforge/lxde/%{name}-%{version}.tar.xz
%endif

BuildRequires: make
BuildRequires:  gtk2-devel
BuildRequires:  pkgconfig(obrender-3.5)
BuildRequires:  openbox-devel >= 3.5.2
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(lxappearance)
BuildRequires:  libSM-devel
BuildRequires:  gettext
BuildRequires:  intltool
%{?git_snapshot:BuildRequires: libtool}
Requires:       lxappearance >= 0.5.0
Requires:       openbox >= 3.5.2

%description
This plugin adds an additional tab called "Window Border" to LXAppearance.
It is only visible when the plugin is installed and Openbox is in use.

%prep
%setup -q %{?git_version:-n %{name}}


%build
%{?git_version:sh autogen.sh}
%configure --disable-static
make %{?_smp_mflags} V=1


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%find_lang %{name}



%files -f %{name}.lang
# FIXME add NEWS and TODO if not empty
%doc AUTHORS CHANGELOG COPYING README
%{_libdir}/lxappearance/plugins/obconf.so
%{_datadir}/lxappearance/obconf/


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 28 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.3-1
- 0.2.3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jul 12 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.2-1
- 0.2.2

* Thu Jul 02 2015 Miroslav Lichvar <mlichvar@redhat.com> - 0.2.0-8
- Rebuild for new openbox

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 15 2013 Miroslav Lichvar <mlichvar@redhat.com> - 0.2.0-4
- Fix building with openbox-3.5.2 (#992155)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 04 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar 04 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.2-0.3.20120304git5fad8207
- Update to latest git to fix broken preview with Openbox 3.5

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-0.2.20110828git02aeaab2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Aug 28 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.2-0.1.20110828git02aeaab2
- Update to latest GIT snapshot to the package build with openbox >= 3.5.0

* Sun Aug 28 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.1-1
- Update to 0.1.1 (Note that upstream's 0.0.1 tarball is actually 0.1.1 in VCS)

* Wed Jul 14 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.0-0.1.20110714git3a0fd02d
- Update to latest GIT snapshot

* Fri Jan 28 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.0-0.1.20110128git710ba0e6
- Update to latest GIT snapshot

* Fri Sep 03 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.0-0.1.20100903git1769cdca
- Update to latest GIT snapshot

* Fri Aug 13 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.0-0.1.20100813git1bf017ee
- initial package
