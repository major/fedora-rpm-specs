%global commit0 edd1ad15e383d32c8d67bdc9198c834b6acebca5
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global commitdate0 20200125

Name:           libyami
Version:        1.3.2
Release:        7.%{commitdate0}git%{shortcommit0}%{?dist}
Summary:        Yet Another Media Infrastructure

License:        ASL 2.0 and BSD
URL:            https://github.com/intel/libyami
Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
Patch0:         libyami-libtool-macro.patch
Patch1:         libyami-init-bool.patch

BuildRequires:  libtool
BuildRequires:  gcc-c++

BuildRequires:  libva-devel
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(x11)
%{?_with_tests:
BuildRequires:  gtest-devel
BuildRequires: make
}


%description
It is YUMMY to your video experience on Linux like platform.
Yami is a core building block for media solutions. It parses video streams
and decodes them leveraging hardware acceleration.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n libyami-%{commit0}
autoreconf -vif


%build
%configure \
  --disable-static \
  --enable-dmabuf \
  --enable-wayland \
  --enable-mpeg2dec \
  --enable-vp9dec \
  --enable-vc1dec \
  --enable-fakedec \
  --enable-jpegenc \
  --enable-vp8svct \
  --enable-vp9enc \
  --enable-h265enc \
%{?_with_tests:--enable-tests}

%make_build V=1


%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%{?_with_tests:
%check
# Some tests require a va-api backend (and X11 server)
make check
}


%ldconfig_scriptlets


%files
%license LICENSE.md 
%license codecparsers/dboolhuff.LICENSE codecparsers/vp9quant.LICENSE
%doc NEWS README.md
%{_libdir}/*.so.1*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libyami.pc


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-7.20200125gitedd1ad1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6.20200125gitedd1ad1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5.20200125gitedd1ad1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-4.20200125gitedd1ad1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3.20200125gitedd1ad1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2.20200125gitedd1ad1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 06 2020 Nicolas Chauvet <kwizart@gmail.com> - 1.3.2-1.20200125gitedd1ad1
- Update to 1.3.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6.20190612gitb0ba3b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5.20190612gitb0ba3b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 02 2019 Nicolas Chauvet <kwizart@gmail.com> - 1.3.1-4.20190612gitb0ba3b1
- Update snapshot

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3.20180918gitfb48083
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 05 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.3.1-2.20180918gitfb48083
- Update commit0

* Fri Oct 05 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.3.1-1.20180510git0067a64
- Update to 1.3.1

* Sun Aug 05 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.3.0-6.20180510git0067a64
- Update to 20180510 git snapshot

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5.20180228git40fa32e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 16 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.3.0-4.20180228git40fa32e
- Switch to --with tests (opt-in)

* Fri Mar 09 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.3.0-3.20180228git40fa32e
- Improve dist tag with commitdate0
- Correct license
- Disable obsolete libtool macro

* Thu Mar 08 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.3.0-2.git40fa32e
- Switch to current git
- Improve descrition
- Enable more parsers
- Enable make check (unless gcc8 and 32bit)

* Wed Jan 24 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.3.0-1
- Initial spec file
