Name:		pidgin-window-merge
Version:	0.3
Release:	26%{?dist}
Summary:	Pidgin plugin for single window mode

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		https://github.com/dm0-/window_merge
Source0:	https://github.com/downloads/dm0-/window_merge/window_merge-0.3.tar.gz	

BuildRequires: make
BuildRequires:  gcc
BuildRequires:	pidgin-devel
BuildRequires:	libappstream-glib
Requires:	pidgin

%global	pname	window_merge

%description
Enabling this plugin will allow conversations to be attached to the Buddy List
window.  Preferences are available to customize the plugin's panel layout.

%prep
%setup -qn %{pname}-%{version}

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} plugindir=%{_libdir}/pidgin
rm -f %{buildroot}%{_libdir}/pidgin/%{pname}.la

mkdir -p %{buildroot}%{_datadir}/appdata
cat > %{buildroot}%{_datadir}/appdata/%{name}.metainfo.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2015 Jiri Eischmann <eischmann@redhat.com> 
-->
<component type="addon"><id>pidgin-window-merge</id><extends>pidgin.desktop</extends><name>Window Merge</name><summary>A plugin that merges the contact list and chat windows into a single window</summary><url type="homepage">https://github.com/dm0-/window_merge</url><metadata_license>GFDL-1.3</metadata_license><project_license>GPL-3.0</project_license><updatecontact>eischmann_at_redhat.com</updatecontact></component>
EOF

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/pidgin-window-merge.metainfo.xml

%files
%{_libdir}/pidgin/%{pname}.so
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%license COPYING

#AppData
%{_datadir}/appdata/pidgin-window-merge.metainfo.xml


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3-25
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-17
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jiri Eischmann <eischmann@redhat.com> - 0.3-5
- Including the metadata file directly in the spec file and adding libappstream-glib as a dependency

* Sun Dec 27 2015 Jiri Eischmann <eischmann@redhat.com> - 0.3-4
- Fixing appdata file installation and adding validation check

* Sun Dec 13 2015 Jiri Eischmann <eischmann@redhat.com> - 0.3-3
- Changing name of the package
- Separating the appdata file to another source

* Sun Apr 19 2015 Jiri Eischmann <eischmann@redhat.com> - 0.3-2
- Adding AppData, adding Fedora 23 as build platform

* Sun Apr 19 2015 Jiri Eischmann <eischmann@redhat.com> - 0.3-1
- Initial package
