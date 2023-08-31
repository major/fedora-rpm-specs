%bcond fuse     1
%bcond lz4      %[ 0%{?fedora} >= 34 || 0%{?rhel} >=  9 ]
%bcond lzma     %[ 0%{?fedora} >= 36 || 0%{?rhel} >= 10 ]
%bcond selinux  1
%bcond uuid     1

Name:           erofs-utils
Version:        1.6
Release:        3%{?dist}

Summary:        Utilities for working with EROFS
License:        GPL-2.0-only AND GPL-2.0-or-later AND (GPL-2.0-only OR Apache-2.0) AND (GPL-2.0-or-later OR Apache-2.0) AND Unlicense
URL:            https://git.kernel.org/pub/scm/linux/kernel/git/xiang/erofs-utils.git

Source:         %{url}/snapshot/%{name}-%{version}.tar.gz
Patch:          %{url}/patch/?id=27aeef179bf17d5f1d98f827e93d24839a6d4176#/%{name}-1.6-CVE-2023-33551.patch
Patch:          %{url}/patch/?id=2145dff03dd3f3f74bcda3b52160fbad37f7fcfe#/%{name}-1.6-CVE-2023-33552.patch

BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
%if %{with fuse}
BuildRequires:  pkgconfig(fuse) >= 2.6
%endif
%if %{with lz4}
BuildRequires:  lz4-devel >= 1.9.3
%endif
%if %{with lzma}
BuildRequires:  xz-devel >= 5.4
%endif
%if %{with selinux}
BuildRequires:  pkgconfig(libselinux)
%endif
%if %{with uuid}
BuildRequires:  pkgconfig(uuid)
%endif

%description
EROFS stands for Enhanced Read-Only File System.  It aims to be a general
read-only file system solution for various use cases instead of just focusing
on saving storage space without considering runtime performance.

This package includes tools to create, check, and extract EROFS images.

%if %{with fuse}
%package -n erofs-fuse
Summary:        FUSE support for mounting EROFS images
Requires:       fuse

%description -n erofs-fuse
EROFS stands for Enhanced Read-Only File System.  It aims to be a general
read-only file system solution for various use cases instead of just focusing
on saving storage space without considering runtime performance.

This package includes erofsfuse to mount EROFS images.
%endif


%prep
%autosetup -p1
autoreconf -fi

%build
%configure \
    %{?with_fuse:--enable-fuse} %{!?with_fuse:--disable-fuse} \
    %{?with_lz4:--enable-lz4} %{!?with_lz4:--disable-lz4} \
    %{?with_lzma:--enable-lzma} %{!?with_lzma:--disable-lzma} \
    %{?with_selinux:--with-selinux} %{!?with_selinux:--without-selinux} \
    %{?with_uuid:--with-uuid} %{!?with_uuid:--without-uuid}
%make_build

%install
%make_install


%files
%{_bindir}/dump.erofs
%{_bindir}/fsck.erofs
%{_bindir}/mkfs.erofs
%{_mandir}/man1/dump.erofs.1*
%{_mandir}/man1/fsck.erofs.1*
%{_mandir}/man1/mkfs.erofs.1*
%doc AUTHORS ChangeLog README docs/PERFORMANCE.md docs/compress-hints.example
%license LICENSES/Apache-2.0 LICENSES/GPL-2.0

%if %{with fuse}
%files -n erofs-fuse
%{_bindir}/erofsfuse
%{_mandir}/man1/erofsfuse.1*
%doc AUTHORS ChangeLog README
%license LICENSES/Apache-2.0 LICENSES/GPL-2.0
%endif


%changelog
* Tue Aug 29 2023 David Michael <fedora.dm0@gmail.com> - 1.6-3
- Backport patches for CVE-2023-33551 and CVE-2023-33552.
- Change conditional build feature defaults for supporting EPEL 9.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Mar 11 2023 David Michael <fedora.dm0@gmail.com> - 1.6-1
- Update to the 1.6 release.

* Wed Jan 25 2023 David Michael <fedora.dm0@gmail.com> - 1.5-4
- Enable MicroLZMA support.
- Switch the License tag to SPDX, and ship matching noneffective license files.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 David Michael <fedora.dm0@gmail.com> - 1.5-1
- Update to the 1.5 release.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 25 2021 David Michael <fedora.dm0@gmail.com> - 1.4-2
- Backport the patch to install a man page for fsck.
- Backport the patch to fix dump output.

* Sun Nov 21 2021 David Michael <fedora.dm0@gmail.com> - 1.4-1
- Update to the 1.4 release.

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 31 2021 David Michael <fedora.dm0@gmail.com> - 1.3-1
- Update to the 1.3 release.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 09 2021 David Michael <fedora.dm0@gmail.com> - 1.2.1-1
- Update to the 1.2.1 release.

* Thu Dec 10 2020 David Michael <fedora.dm0@gmail.com> - 1.2-1
- Update to the 1.2 release.
- Split FUSE support into an independent subpackage.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 13 2020 David Michael <fedora.dm0@gmail.com> - 1.1-1
- Update to the 1.1 release.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 David Michael <fedora.dm0@gmail.com> - 1.0-1
- Initial package.
