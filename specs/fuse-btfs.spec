%global _preprocessor_defines %{_preprocessor_defines} -DOPENSSL_NO_ENGINE

Summary:	FUSE filesystem Bittorrent
Name:		fuse-btfs
Version:	2.24
Release:	14%{?dist}

License:	GPL-3.0-only
URL:		https://github.com/johang/btfs
Source0:	https://github.com/johang/btfs/archive/v%{version}/btfs-%{version}.tar.gz

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	pkgconfig(fuse)
BuildRequires:	pkgconfig(libtorrent-rasterbar)
BuildRequires:	pkgconfig(libcurl)

%description
With BTFS, you can mount any .torrent file or magnet link and then use it as
any read-only directory in your file tree. The contents of the files will be
downloaded on-demand as they are read by applications. Tools like ls, cat and
cp works as expected. Applications like vlc and mplayer can also work without
changes.

%prep
%autosetup -n btfs-%{version}

%build
autoreconf -i
%configure
%make_build

%install
%{make_install}

%files
%{_bindir}/btfs
%{_bindir}/btfsstat
%{_bindir}/btplay
%{_mandir}/man1/btfs.1*

%doc README.md
%license LICENSE


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.24-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jul 30 2024 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 2.24-13
- OPENSSL_NO_ENGINE deprecation workaround rhbz#2300679

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.24-12
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.24-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.24-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.24-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.24-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.24-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.24-4
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May 25 2021 Leigh Scott <leigh123linux@gmail.com> - 2.24-2
- Rebuild for new libtorrent

* Sun Feb 14 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 2.24-1
- Update to 2.24

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 16 2020 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 2.23-1
- Update to 2.23

* Thu Sep 3 2020 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 2.22-2
- Spec changes based on review

* Sat Aug 15 2020 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 2.22-1
- Initial version of the package
