%global sname   skinelchihd
# version we want build against
%global vdr_version 2.6.1
%if 0%{?fedora} >= 38
%global vdr_version 2.6.3
%endif

Name:           vdr-skinelchihd
Version:        1.2.3
Release:        1%{?dist}
Summary:        A Elchi based skin with True Color support for the Video Disc Recorder

License:        GPLv2+
URL:            https://github.com/FireFlyVDR/vdr-plugin-skinelchihd
Source0:        %url/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Configuration files for plugin parameters. These are Fedora specific and not in upstream.
Source1:        %{name}.conf
BuildRequires:  make
BuildRequires:  gcc-c++
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
%autosetup -n vdr-plugin-%{sname}-%{version}

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
