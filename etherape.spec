%define _hardened_build 1
Name:           etherape
Version:        0.9.20
Release:        3%{?dist}
Summary:        Graphical network monitor for Unix

License:        GPLv2+
URL:            http://etherape.sourceforge.net/
Source0:        http://downloads.sourceforge.net/sourceforge/etherape/%{name}-%{version}.tar.gz
Source1:        etherape.pam
Source2:        etherape.console

BuildRequires:  gcc
BuildRequires:  libpcap-devel, goocanvas2-devel, popt-devel
BuildRequires:  gettext, desktop-file-utils, itstool
BuildRequires:  gnome-doc-utils
BuildRequires:  scrollkeeper
BuildRequires: make
Requires(post): scrollkeeper
Requires(postun): scrollkeeper

%description
EtherApe is a graphical network monitor modeled after etherman. 

%prep
%setup -q


%build
%configure --bindir=%{_sbindir}
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/pam.d
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/%{_sysconfdir}/pam.d/etherape
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/security/console.apps
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT/%{_sysconfdir}/security/console.apps/etherape
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
ln -s consolehelper $RPM_BUILD_ROOT/%{_bindir}/etherape

%find_lang %{name}
desktop-file-install --dir ${RPM_BUILD_ROOT}%{_datadir}/applications \
    ${RPM_BUILD_ROOT}%{_datadir}/applications/etherape.desktop

%files -f %{name}.lang
%license COPYING
%doc ABOUT-NLS AUTHORS ChangeLog FAQ NEWS OVERVIEW README README.bugs TODO


%{_bindir}/etherape
%{_sbindir}/etherape
#%%dir %%{_sysconfdir}/%%{name}
#%%config(noreplace) %%{_sysconfdir}/%%{name}/services
%config(noreplace) %{_sysconfdir}/pam.d/etherape
%config(noreplace) %{_sysconfdir}/security/console.apps/etherape
%dir %{_datadir}/%{name}
%{_datadir}/help/C/%{name}/
%{_datadir}/%{name}/
%{_datadir}/applications/etherape.desktop
%{_datadir}/pixmaps/etherape.png
#%%dir %%{_datadir}/omf/etherape
#%%{_datadir}/omf/etherape/etherape-C.omf
%{_mandir}/man1/*

%post
scrollkeeper-update -q -o %{_datadir}/omf/%{name} || :

%postun
scrollkeeper-update -q || :


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 20 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.9.20-1
- 0.9.20

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 04 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.9.18-1
- 0.9.18.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 06 2017 Jon Ciesla <limburgher@gmail.com> - 0.9.15-1
- 0.9.15, BZ 1429169.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 06 2016 Jon Ciesla <limburgher@gmail.com> - 0.9.14-1
- 0.9.14, BZ 1305314.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 07 2013 Jon Ciesla <limburgher@gmail.com> - 0.9.13-1
- 0.9.13, BZ 960395.

* Mon Feb 11 2013 Jon Ciesla <limburgher@gmail.com> - 0.9.12-6
- Drop desktop vendor tag.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 13 2012 Jon Ciesla <limburgher@gmail.com> - 0.9.12-4
- Add hardened build.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.9.12-2
- Rebuild for new libpng

* Mon Jul 18 2011 Jan F. Chadima <jchadima@redhat.com> 0.9.12-1
- Upgrade to 0.9.12

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jul 17 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.9.7-9
- fix license tag

* Sat Apr 19 2008 Michael Rice <errr@errr-online.com> - 0.9.7-8
- fix ln -s 

* Sat Apr 19 2008 Michael Rice <errr[AT]errr-online.com> - 0.9.7-7
- Fix #442131 problems running as non root

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.7-6
- Autorebuild for GCC 4.3

* Wed Apr 11 2007 Michael Rice <errr[AT]errr-online.com> - 0.9.7-5
- Rebuild to get all matching version from FC-5 .. devel

* Mon Feb 12 2007 Michael Rice <errr[AT]errr-online.com> - 0.9.7-4
- Fix desktop file install

* Sat Feb 10 2007 Michael Rice <errr[AT]errr-online.com> - 0.9.7-3
- Add scrollkeeper post and postun script snips
- Fix dir ownership or pixmaps and omf
- Fix .desktop X category

* Wed Jan 31 2007 Michael Rice <errr[AT]errr-online.com> - 0.9.7-2
- Fix dup BR's 
- add missing BR for libgnomeui-devel scrollkeeper
- removed %%{buildroot}. in choice of other

* Wed Jan 24 2007 Michael Rice <errr[AT]errr-online.com> - 0.9.7-1
- Initial RPM release
