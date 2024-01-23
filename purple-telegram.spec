Name:		purple-telegram
Version:	1.4.6
Release:	8%{?dist}
Summary:	Libpurple protocol plugin for Telegram support
License:	GPLv2+ and LGPLv2+
URL:		https://github.com/majn/telegram-purple
Source0:	https://github.com/majn/telegram-purple/releases/download/v%{version}/telegram-purple_%{version}.orig.tar.gz
ExcludeArch:	s390x
ExcludeArch:	ppc64
BuildRequires: make
BuildRequires:	gcc
BuildRequires:	gettext
BuildRequires:	libgcrypt-devel >= 1.6
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(purple)
BuildRequires:	pkgconfig(libwebp)
BuildRequires:	libappstream-glib
BuildRequires:	libpng-devel
Provides:	bundled(tgl) = 2.0.1
#Upstream is not interested in unbundling tgl 

%description
Adds support for Telegram IM to purple-based clients such as Pidgin.

%prep
%setup -n telegram-purple

%build
%global optflags %{optflags} -Wno-cast-function-type
%global debug_package %{nil}
%configure
make %{?_smp_mflags}

%install
%make_install
chmod 755 %{buildroot}/%{_libdir}/purple-2/telegram-purple.so
%find_lang telegram-purple

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/telegram-purple.metainfo.xml

%files -f telegram-purple.lang
%license COPYING
%doc README* CHANGELOG*
%{_libdir}/purple-2/telegram-purple.so

#Icons
%dir %{_datadir}/pixmaps/pidgin/
%{_datadir}/pixmaps/pidgin/protocols/*/telegram.png

#AppStream metadata
%{_metainfodir}/telegram-purple.metainfo.xml

%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 05 2021 Jiri Eischmann <eischmann@redhat.com> - 1.4.6-1
- Update to 1.4.6

* Fri Oct 02 2020 Jiri Eischmann <eischmann@redhat.com> - 1.4.4-1
- Update to 1.4.4
- Changing the metainfo file location

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 20 2020 Jiri Eischmann <eischmann@redhat.com> - 1.4.3-1
-Update to 1.4.3
-Adding macro for no debug info

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 03 2019 Jiri Eischmann <eischmann@redhat.com> - 1.4.2-1
- Update to 1.4.2

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 Jiri Eischmann <eischmann@redhat.com> - 1.4.1-1
- Update to 1.4.1
- libpng-devel added as dependency
- AArch64 added back to build architectures

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 01 2018 Jiri Eischmann <eischmann@redhat.com> - 1.3.1-3
- Turning off Werror, upstream rejected to fix the warnings

* Wed Jun 28 2017 Jiri Eischmann <eischmann@redhat.com> - 1.3.1-2
- Backporting a patch to build with Werror=format-overflow

* Mon Jun 26 2017 Jiri Eischmann <eischmann@redhat.com> - 1.3.1-1
- Update to 1.3.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Sandro Mani <manisandro@gmail.com> - 1.3.0-2
- Rebuild (libwebp)

* Tue Aug 9 2016 Jiri Eischmann <eischmann@redhat.com> - 1.3.0-1
- Update to 1.3.0
- Switching from git clone to upstream provided archive
- Removing appdata file installation because it's now installed by the build script
- Specifying bundled tgl

* Tue Mar 15 2016 Jiri Eischmann <eischmann@redhat.com> - 1.2.6-1
- Update to 1.2.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Jiri Eischmann <eischmann@redhat.com> - 1.2.5-1
- Update to 1.2.5
- Excluding ppc64 arch for now because it fails to build there

* Tue Jan 5 2016 Jiri Eischmann <eischmann@redhat.com> - 1.2.4-1
- Update to 1.2.4

* Tue Dec 29 2015 Kalev Lember <klember@redhat.com> - 1.2.2-5
- Rebuilt for libwebp soname bump

* Mon Dec 21 2015 Jiri Eischmann <eischmann@redhat.com> 1.2.2-4
- Specifying required version of libgcrypt-devel
- Changing summary

* Wed Dec 16 2015 Jiri Eischmann <eischmann@redhat.com> 1.2.2-3
- Another fix of ownership of protocol icon directories

* Tue Dec 15 2015 Jiri Eischmann <eischmann@redhat.com> 1.2.2-2
- Changed the way metainfo.xml file is installed, added validation for it
- Translation files now fully handled by macro
- BuildRequires now one per line
- Fixed ownership of directories of protocol icons

* Sat Dec 12 2015 Jiri Eischmann <eischmann@redhat.com> 1.2.2-1
- Update to 1.2.2
- Improved the spec (adding description, using pkgconfig for buildrequires, adding docs,...)
- Added translations
- Using libgcrypt instead of openssl

* Thu Sep 17 2015 Jiri Eischmann <eischmann@redhat.com> 1.2.1-1
- Initial build


