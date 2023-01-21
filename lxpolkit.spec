# Review at https://bugzilla.redhat.com/show_bug.cgi?id=579171

Name:           lxpolkit
Version:        0.1.0
Release:        26%{?dist}
Summary:        Simple PolicyKit authentication agent

License:        GPLv2+
URL:            http://lxde.org/
#VCS: git:git://lxde.git.sourceforge.net/gitroot/lxde/lxpolkit
Source0:        http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.gz
Patch0:         lxpolkit-0.1.0-format-security.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  gettext
BuildRequires:  polkit-devel
BuildRequires:  desktop-file-utils
Requires:       polkit >= 0.95
# required to replace polkit-gnome and polkit-kde
Provides:       PolicyKit-authentication-agent

%description
LXPolKit is a simple PolicyKit authentication agent developed for LXDE, the 
Lightweight X11 Desktop Environment.


%prep
%setup -q
%patch0 -p1
# Don't start in Xfce to avoid bugs like
# https://bugzilla.redhat.com/show_bug.cgi?id=616730
sed -i 's/^NotShowIn=GNOME;KDE;/NotShowIn=GNOME;KDE;XFCE;/g' data/lxpolkit.desktop.in.in


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
%find_lang %{name}
desktop-file-install \
    --remove-key="NotShowIn" \
    --add-only-show-in="LXDE;" \
    --delete-original \
    --dir=%{buildroot}%{_sysconfdir}/xdg/autostart \
    %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}.desktop


%files -f %{name}.lang
# FIXME add ChangeLog and NEWS if not empty
%doc AUTHORS COPYING README
%config %{_sysconfdir}/xdg/autostart/lxpolkit.desktop
%{_libexecdir}/%{name}
%{_datadir}/%{name}/


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 13 2015 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.0-10
- Only start lxpolkit in LXDE (#1114176, #1178272)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.1.0-8
- Fix FTBFS with -Werror=format-security (#1037186, #1106144)
- Cleanup spec

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.1.0-2
- Rebuild for new libpng

* Sun Aug 28 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.0-1
- Update to 0.1.0
- Do not start lxpolkit in Xfce (#616730)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-0.2.20100402git5087383
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Apr 02 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.0-0.1.20100402git5087383
- Update to git version 5087383
- Install binary to %%{_libexecdir}

* Mon Mar 29 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.0-0.1.20100329git93555fa
- Initial package

