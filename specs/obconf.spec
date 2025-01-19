%global git_rev_full 63ec47c5e295ad4f09d1df6d92afb7e10c3fec39
%global git_rev %(c=%{git_rev_full}; echo ${c:0:6})
%global git_date 20150213

Name:		obconf
Version:	2.0.4
Release:	28.%{git_date}git%{git_rev}%{?dist}
Summary:	A graphical configuration editor for the Openbox window manager

License:	GPL-2.0-or-later
URL:		http://icculus.org/openbox/index.php/ObConf:About
#Source0:	http://icculus.org/openbox/obconf/%{name}-%{version}.tar.gz
Source0:	https://github.com/danakj/obconf/archive/%{git_rev}/obconf-%{git_rev}.tar.gz
Patch0: obconf-c99.patch

BuildRequires: make
BuildRequires:	openbox-devel >= 3.5.2
BuildRequires:	gtk3-devel
BuildRequires:	startup-notification-devel
BuildRequires:	pkgconfig
BuildRequires:	desktop-file-utils
BuildRequires:	libSM-devel
BuildRequires:	gettext-devel
BuildRequires:	libtool

%description
ObConf is a graphical configuration editor for the Openbox window manager. 


%prep
%autosetup -p1 -n %{name}-%{git_rev_full}


%build
./bootstrap
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
%find_lang %{name}
desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications	\
	--add-category	X-Fedora	\
	--delete-original	\
	%{buildroot}%{_datadir}/applications/%{name}.desktop


%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_bindir}/%{name}
%{_datadir}/%{name}/  
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/mimelnk/
%{_datadir}/pixmaps/%{name}.png


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-28.20150213git63ec47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-27.20150213git63ec47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-26.20150213git63ec47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-25.20150213git63ec47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-24.20150213git63ec47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 27 2023 Florian Weimer <fweimer@redhat.com> - 2.0.4-23.20150213git63ec47
- Port to C99

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-22.20150213git63ec47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-21.20150213git63ec47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-20.20150213git63ec47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-19.20150213git63ec47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-18.20150213git63ec47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-17.20150213git63ec47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-16.20150213git63ec47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-15.20150213git63ec47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-14.20150213git63ec47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-13.20150213git63ec47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-12.20150213git63ec47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-11.20150213git63ec47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-10.20150213git63ec47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-9.20150213git63ec47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-8.20150213git63ec47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 02 2015 Miroslav Lichvar <mlichvar@redhat.com> - 2.0.4-7.20150213git63ec47
- rebuild for new openbox

* Fri Jun 26 2015 Miroslav Lichvar <mlichvar@redhat.com> - 2.0.4-6.20150213git63ec47
- update to 20150213git63ec47

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 2.0.4-4
- update mime scriptlets

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 15 2013 Miroslav Lichvar <mlichvar@redhat.com> - 2.0.4-1
- update to 2.0.4

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-14.20121006gitcfde28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 28 2013 Miroslav Lichvar <mlichvar@redhat.com> - 2.0.3-13.20121006gitcfde28
- update to 20121006gitcfde28
- buildrequire libtool
- remove obsolete macros

* Mon Apr 29 2013 Jon Ciesla <limburgher@gmail.com> - 2.0.3-12.20100212gitb04658
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-11.20100212gitb04658
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-10.20100212gitb04658
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-9.20100212gitb04658
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 30 2011 Miroslav Lichvar <mlichvar@redhat.com> - 2.0.3-8.20100212gitb04658
- fix config file loading (#739973)

* Fri Aug 05 2011 Miroslav Lichvar <mlichvar@redhat.com> - 2.0.3-7.20100212gitb04658
- update to 20100212gitb04658 for openbox-3.5

* Mon May 02 2011 Miroslav Lichvar <mlichvar@redhat.com> - 2.0.3-6.20091221gitc8ac23
- update to 20091221gitc8ac23 (#700937)
- include Hungarian and Romanian translations (#665584)
- don't set the theme preview if a null is returned (#692549)
- don't use a non-zero page size for some spinners (#694044)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Apr 17 2008 Miroslav Lichvar <mlichvar@redhat.com> - 2.0.3-2
- Rebuild for new openbox

* Sun Feb 03 2008 Miroslav Lichvar <mlichvar@redhat.com> - 2.0.3-1
- Update to 2.0.3

* Wed Aug 22 2007 Miroslav Lichvar <mlichvar@redhat.com> - 2.0.2-2
- Update license tag

* Mon Jul 23 2007 Miroslav Lichvar <mlichvar@redhat.com> - 2.0.2-1
- Update to 2.0.2

* Thu Jun 14 2007 Miroslav Lichvar <mlichvar@redhat.com> - 2.0.1-1
- Update to 2.0.1

* Sun Aug 27 2006 Peter Gordon <peter@thecodergeek.com> - 1.6-3
- Mass FC6 rebuild

* Thu Jul 13 2006 Peter Gordon <peter@thecodergeek.com> - 1.6-2
- Add BR: libSM-devel to fix build issue.

* Fri Jun 09 2006 Peter Gordon <peter@thecodergeek.com> - 1.6-1
- Initial packaging. 
