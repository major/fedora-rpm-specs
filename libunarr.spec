Name:           libunarr
Version:        1.1.0
Release:        0.2.beta1%{?dist}
Summary:        Decompression library for rar, tar and zip archives

License:        LGPLv3+
URL:            https://github.com/selmf/unarr
Source0:        %{url}/releases/download/v%{version}.beta1/unarr-%{version}.beta1.tar.xz

BuildRequires:  cmake
BuildRequires:  gcc

BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(zlib)

%description
(lib)unarr is a decompression library for RAR, TAR, ZIP and 7z* archives.

It was forked from unarr, which originated as a port of the RAR extraction
features from The Unarchiver project required for extracting images from comic
book archives. Zeniko wrote unarr as an alternative to libarchive which didn't
have support for parsing filters or solid compression at the time.

While (lib)unarr was started with the intent of providing unarr with a proper
cmake based build system suitable for packaging and cross-platform development,
it's focus has now been extended to provide code maintenance and to continue the
development of unarr, which no longer is maintained.

%package        devel
Summary:        Development files for %{name}

Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
%autosetup -n unarr-%{version}.beta1 -p1

# wrong-file-end-of-line-encoding fix
sed -i 's/\r$//' README.md


%build
%cmake
%cmake_build


%install
%cmake_install


%files
%license COPYING
%doc CHANGELOG.md README.md AUTHORS
%{_libdir}/%{name}.so.1*

%files devel
%{_includedir}/unarr.h
%{_libdir}/%{name}.so
%{_libdir}/cmake/unarr/unarr-*.cmake
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.2.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun May 01 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 1.1.0-1
- chore(update): 1.1.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.1-10
- Rebuild with out-of-source builds new CMake macros

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 16 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.1-7
- Update

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 29 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.1-3
- Initial package.
