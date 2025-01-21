%global sname   skinelchihd
%global commit0 56fc1731410f32d6f13507b8548c9d955af35759
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gitdate 20241008

# version we want to build against
%global vdr_version 2.6.3
# Set vdr_version based on Fedora version
%if 0%{?fedora} >= 42
%global vdr_version 2.7.2
%elif 0%{?fedora} >= 40
%global vdr_version 2.6.9
%endif

Name:           vdr-skinelchihd
Version:        1.2.5
# Release:        0.8.%%{gitdate}git%%{shortcommit0}%%{?dist}
Release:        2%{?dist}
Summary:        A Elchi based skin with True Color support for the Video Disc Recorder
License:        GPL-2.0-or-later
URL:            https://github.com/FireFlyVDR/vdr-plugin-skinelchihd
Source0:        %url/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Source0:        %%url/archive/%%{commit0}/%%{name}-%%{shortcommit0}.tar.gz
# Configuration files for plugin parameters. These are Fedora specific and not in upstream.
Source1:        %{name}.conf
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  gettext
%if 0%{?fedora} >= 38
#BuildRequires:  pkgconfig(ImageMagick)
BuildRequires:  ImageMagick-c++-devel
%else
BuildRequires:  pkgconfig(GraphicsMagick++)
%endif
BuildRequires:  vdr-devel >= %{vdr_version}
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description
This plugin for Klaus Schmidinger's Video Disc Recorder VDR adds the "Elchi HD"
skin. It is based on the Elchi skin with major re-factoring to make use of newer
VDR features like True Color support.

%prep
%autosetup -n vdr-plugin-%{sname}-%%{version}
#%%autosetup -n vdr-plugin-%%{sname}-%%{commit0}

%build
%{set_build_flags}
%if 0%{?fedora} >= 38
%make_build IMAGELIB=imagemagick
%else
%make_build IMAGELIB=graphicsmagick
%endif

%install
# make install would install the themes under /etc, let's not use that
make install-lib install-i18n DESTDIR=%{buildroot}
# install the themes to the custom location used in Fedora
install -dm 755 %{buildroot}%{vdr_vardir}/themes
install -pm 644 themes/*.theme %{buildroot}%{vdr_vardir}/themes/

# skinelchihd.conf
install -Dpm 644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/sysconfig/vdr-plugins.d/skinelchihd.conf

%find_lang %{name}

%files -f %{name}.lang
%doc HISTORY* README*
%license COPYING
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/skinelchihd.conf
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}
%{vdr_vardir}/themes/ElchiHD-*.theme

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Oct 09 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.2.5-1
- Rebuilt for new VDR API version 2.7.2
- Update to 1.2.5

* Wed Oct 09 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.2.4-0.8.20241008git56fc173
- Rebuilt for new VDR API version 2.7.2

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.4-0.7.20231222git53f8c87
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-0.6.20231222git53f8c87
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 15 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.2.4-0.5.20231222git53f8c87
- Rebuilt for new VDR API version 2.6.9

* Thu Jul 11 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.2.4-0.4.20231222git53f8c87
- Rebuilt for new VDR API version 2.6.8

* Fri Apr 12 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.2.4-0.3.20231222git53f8c87
- Rebuilt for new VDR API version

* Fri Jan 26 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.2.4-0.2.20231222git53f8c87
- Rebuilt for new VDR API version

* Fri Jan 05 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.2.4-0.1.20231222git53f8c87
- Rebuilt for new VDR API version
- Add BR gettext for rawhide

* Tue Sep 19 2023 Martin Gansser <martinkg@fedoraproject.org> - 1.2.3-1
- Update to 1.2.3

* Tue Sep 12 2023 Martin Gansser <martinkg@fedoraproject.org> - 1.2.2-1
- Update to 1.2.2

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Martin Gansser <martinkg@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Fri Jun 30 2023 Martin Gansser <martinkg@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0

* Thu Jun 08 2023 Martin Gansser <martinkg@fedoraproject.org> - 1.1.2-1
- Update to 1.1.2

* Fri Feb 10 2023 Martin Gansser <martinkg@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 14 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.1.0-2
- Rebuilt for new VDR API version

* Mon Dec 12 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Thu Dec 01 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-3
- Rebuilt for new VDR API version

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Feb 13 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0
- Switch to GraphicsMagick

* Sat Feb 05 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.5.0-10
- Rebuilt for new VDR API version

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 30 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.5.0-8
- Rebuilt for new VDR API version

* Sat Oct 16 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.5.0-7
- Rebuilt due FTI in rawhide

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Apr 28 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.5.0-5
- Rebuilt for new VDR API version

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 03 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.5.0-3
- Install the license file with %license not %doc

* Sun Aug 30 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.5.0-2
- Install the license file with %license not %doc

* Tue Aug 25 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.5.0-1
- Initial Build
