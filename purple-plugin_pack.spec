%global intname purple-plugin-pack

Name:           purple-plugin_pack
Version:        2.8.0
Release:        7%{?dist}

License:        GPL-2.0-or-later
Summary:        A set of plugins for libpurple, pidgin, and finch
URL:            https://keep.imfreedom.org/pidgin/%{intname}
Source0:        https://dl.bintray.com/pidgin/releases/%{intname}-%{version}.tar.xz
Source1:        %{intname}.metainfo.xml

BuildRequires:  pkgconfig(enchant-2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtkspell-2.0)
BuildRequires:  pkgconfig(pidgin)
BuildRequires:  pkgconfig(purple)

BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  ninja-build

Provides:       %{intname}

%description
This package contains a number of plugins for use with the purple IM/IRC
library.

%package pidgin
Summary:        A set of plugins for pidgin
Provides:       %{intname}-pidgin
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       pidgin%{?_isa}

Provides:       %{name}-pidgin-xmms = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-pidgin-xmms < %{?epoch:%{epoch}:}%{version}-%{release}

%description pidgin
This package contains a number of plugins for use with the pidgin client.

%prep
%autosetup -n %{intname}-%{version}

%build
%meson \
    -Dwerror=false \
    -Dpurple-version=2 \
    -Dtypes=default \
    -Dnls=true
%meson_build

%install
%meson_install
%find_lang plugin_pack
install -Dm 644 %{SOURCE1} %{buildroot}%{_metainfodir}/%{intname}.metainfo.xml

%files -f plugin_pack.lang
%doc AUTHORS ChangeLog
%license COPYING
%{_metainfodir}/%{intname}.metainfo.xml
%{_libdir}/purple-2/*.so

%files pidgin
%doc AUTHORS ChangeLog
%license COPYING
%{_libdir}/pidgin/*.so

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 31 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2.8.0-1
- Updated to version 2.8.0.
- Performed major SPEC cleanup.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 16 2019 Pavel Raiskup <praiskup@redhat.com> - 2.7.0-11
- fix FTBFS (rhbz#1675694)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Jan Synáček <jsynacek@redhat.com> - 2.7.0-2
- Ship AppStream metainfo file (#1300463)

* Thu Jan 28 2016 Jan Synáček <jsynacek@redhat.com> - 2.7.0-1
- Update to 2.7.0 (#890738)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.6.3-3
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 04 2011 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 2.6.3-1
- Upstream update

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Nov 20 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 2.4.0-2
- Update Source0 URL

* Tue Oct  7 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 2.4.0-1
- Upstream update
- Extract inner function in switchspell (#462822)

* Sun Apr  6 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 2.3.0-1
- Upstream update

* Thu Feb 14 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 2.2.0-5
- Rebuild for GCC 4.3

* Tue Jan  8 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 2.2.0-4
- Switch from aspell to enchant (#427949)

* Mon Jan  7 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 2.2.0-3
- Switch from gtkspell to aspell

* Thu Nov 15 2007 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 2.2.0-2
- Added provides to other subpackages

* Wed Nov 14 2007 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 2.2.0-1
- Update to 2.2.0
- Add provides of purple-plugin-pack

* Thu Oct  4 2007 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 2.1.1-1
- Initial RPM release
