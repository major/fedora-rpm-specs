%global debug_package %{nil}
%global mod_name alternative-toolbar

Name:		rhythmbox-alternative-toolbar
Version:	0.18.4
Release:	8%{?dist}
Summary:	Client-side decorated compact toolbar for Rhythmbox
License:	GPLv3

URL:		https://github.com/fossfreedom/alternative-toolbar/
Source0:	https://github.com/fossfreedom/%{mod_name}/archive/v%{version}/%{mod_name}-%{version}.tar.gz
BuildRequires: make
BuildRequires:  gcc
BuildRequires:	intltool
BuildRequires:	glib2-devel
BuildRequires:	python3-gobject
BuildRequires:	gtk3
BuildRequires:	gobject-introspection
BuildRequires:	rhythmbox-devel
Requires:	rhythmbox

ExclusiveArch: %{ix86} %{arm} x86_64 ppc64 ppc64le

%description
Alternative Toolbar replaces the Rhythmbox large toolbar with a Client-Side
Decorated or Compact toolbar which can be hidden.

%prep
%autosetup -n %{mod_name}-%{version}

%build
./autogen.sh --prefix=%{_prefix}
%configure
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/rhythmbox/plugins/alternative-toolbar/LICENSE
%find_lang %{mod_name}

%files -f %{mod_name}.lang
%{_libdir}/rhythmbox/plugins/alternative-toolbar/
%{_datadir}/rhythmbox/plugins/alternative-toolbar
%{_datadir}/glib-2.0/schemas/org.gnome.rhythmbox.plugins.alternative_toolbar.gschema.xml
%{_datadir}/metainfo/org.gnome.rhythmbox.alternative-toolbar.addon.appdata.xml
%license LICENSE
%doc readme.html

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 09 2020 Petr Viktorin <pviktori@redhat.com> - 0.18.4-4
- Remove BuildRequires on pygobject2

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Tonet Jallo <tonet666p@fedoraproject.org> 0.18.4-1
- Upstream 0.18.4

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 26 2017 Tonet Jallo <tonet666p@fedoraproject.org> 0.17.3-6
- Improved the package summary.

* Mon Apr 17 2017 Tonet Jallo <tonet666p@fedoraproject.org> 0.17.3-5
- Removed the noarch label to resolv bug 1434240

* Wed Mar 8 2017 Athos Ribeiro <athoscr@fedoraproject.org> 0.17.3-4
- Make the package arched

* Tue Mar 7 2017 Tonet Jallo <tonet666p@fedoraproject.org> 0.17.3-3
- Using the LICENSE file located on buildroot instead libdir
- Using macro at autogen.sh
- Removed duplicated directories on files section
- Added version macro to Source0
- Removed dots on changelog
- Added BuildArch to noarch and ExclusiveArch both instead ExcludedArch only

* Thu Mar 2 2017 Tonet Jallo <tonet666p@fedoraproject.org> 0.17.3-2
- Excluded the same architectures from rhythmbox spec
- Changed the source link
- Added directories on files section
- Added versions on changelog
- Removed duplicated license file

* Sun Feb 26 2017 Tonet Jallo <tonet666p@fedoraproject.org> 0.17.3-1
- Initial packaging

