%global commit0 c3d25b64b05aeb0c4eecc140aef617cfeced6b8e
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global commitdate0 20191205

Name:           libyami-utils
Version:        1.3.1
Release:        11.%{commitdate0}git%{shortcommit0}%{?dist}
Summary:        Libyami Utilities

License:        ASL 2.0
URL:            https://github.com/intel/libyami-utils
Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  libtool
BuildRequires:  gcc-c++

#Optional, used by some test scripts
#BuildRequires:  ffmpeg-devel
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libbsd)
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(libva-x11)
BuildRequires:  pkgconfig(libva-wayland)
BuildRequires:  pkgconfig(libyami)
BuildRequires: make


%description
Libyami Utilities.


%prep
%autosetup -p1 -n %{name}-%{commit0}
autoreconf -vif


%build
%configure \
  --enable-tests-gles \
  --enable-wayland

%make_build V=1


%install
%make_install


%files
%license LICENSE
%doc README.md
%{_bindir}/psnr
%{_bindir}/simpleplayer
%{_bindir}/yamidecode
%{_bindir}/yamiencode
%{_bindir}/yamiinfo
%{_bindir}/yamitranscode
%{_bindir}/yamivpp
%{_mandir}/man1/yami*


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-11.20191205gitc3d25b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-10.20191205gitc3d25b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-9.20191205gitc3d25b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-8.20191205gitc3d25b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7.20191205gitc3d25b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6.20191205gitc3d25b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5.20191205gitc3d25b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4.20191205gitc3d25b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 02 2019 Nicolas Chauvet <kwizart@gmail.com> - 1.3.1-3.20191205gitc3d25b6
- Update to 20191205

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2.20180921git7e801b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 05 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.3.1-1.20180921git7e801b5
- Update to 1.3.1

* Sun Aug 05 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.3.0-4.20180510git221523a
- Update to 20180510 git snapshot

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3.20180207git9b5a311
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 19 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.3.0-2.20180207git9b5a311
- Updated release field
- Simplified Source field
- Avoid deprecated libtool macro

* Thu Mar 08 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.3.0-1.git9b5a311
- Initial spec file
