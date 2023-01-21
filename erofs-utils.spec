%bcond_without fuse
%bcond_without lz4
%bcond_with lzma
%bcond_without selinux
%bcond_without uuid

Name:           erofs-utils
Version:        1.5
Release:        3%{?dist}

Summary:        Utilities for working with EROFS
License:        GPLv2+
URL:            https://git.kernel.org/pub/scm/linux/kernel/git/xiang/erofs-utils.git

Source0:        %{url}/snapshot/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
%if %{with fuse}
BuildRequires:  fuse-devel
%endif
%if %{with lz4}
BuildRequires:  lz4-devel
%endif
%if %{with lzma}
BuildRequires:  xz-devel >= 5.3.2
%endif
%if %{with selinux}
BuildRequires:  libselinux-devel
%endif
%if %{with uuid}
BuildRequires:  libuuid-devel
%endif

%description
EROFS stands for Enhanced Read-Only File System.  Different from other
read-only file systems, it is designed for flexibility, scalability, and
simplicity for high performance.

This package includes tools to create, check, and extract EROFS images.

%if %{with fuse}
%package -n erofs-fuse
Summary:        FUSE support for mounting EROFS images
Requires:       fuse

%description -n erofs-fuse
EROFS stands for Enhanced Read-Only File System.  Different from other
read-only file systems, it is designed for flexibility, scalability, and
simplicity for high performance.

This package includes erofsfuse to mount EROFS images.
%endif


%prep
%autosetup
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
%doc AUTHORS ChangeLog README
%license LICENSES/GPL-2.0

%if %{with fuse}
%files -n erofs-fuse
%{_bindir}/erofsfuse
%{_mandir}/man1/erofsfuse.1*
%doc AUTHORS ChangeLog README
%license LICENSES/GPL-2.0
%endif


%changelog
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
