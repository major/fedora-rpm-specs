%global commit0 a3c2476de19e6635458273ceeaeceff124fabd63
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20190517

Name:           libva-v4l2-request
Version:        1.0.0
Release:        9.%{?date0}git%{?shortcommit0}%{?dist}
Summary:        VA-API Backend using v4l2-request API

License:        LGPLv2+ and MIT
URL:            https://github.com/bootlin/libva-v4l2-request
Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
# https://github.com/bootlin/libva-v4l2-request/pull/38
Patch3:         https://patch-diff.githubusercontent.com/raw/bootlin/libva-v4l2-request/pull/38.patch

BuildRequires:  gcc
BuildRequires:  meson

BuildRequires:  libva-devel
BuildRequires:  libdrm-devel


%description
This VA-API backend is designed to work with the Linux Video4Linux2
Request API that is used by a number of video codecs drivers, including
the Video Engine found in most Allwinner SoCs.


%prep
%autosetup -p1 -n %{name}-%{commit0}


%build
%meson
%meson_build


%install
%meson_install


%check
%meson_test


%files
%license COPYING COPYING.LGPL COPYING.MIT
%doc AUTHORS CREDITS README.md
%{_libdir}/dri/v4l2_request_drv_video.so


%changelog
* Tue Mar 21 2023 Nicolas Chauvet <kwizart@gmail.com> - 1.0.0-9.20190517gita3c2476
- rebuilt

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8.20190517gita3c2476
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7.20190517gita3c2476
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6.20190517gita3c2476
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 27 2021 Nicolas Chauvet <kwizart@gmail.com> - 1.0.0-5.20190517gita3c2476
- Fix FTBFS

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4.20190517gita3c2476
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3.20190517gita3c2476
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2.20190517gita3c2476
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul  3 2020 Nicolas Chauvet <kwizart@gmail.com> - 1.0.0-1.20190517gita3c2476
- Initial spec file
