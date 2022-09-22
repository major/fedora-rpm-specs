Name:           ntfs2btrfs
Version:        20210923
Release:        3%{?dist}
Summary:        Conversion tool from NTFS to Btrfs

License:        GPLv2+
URL:            https://github.com/maharmstone/ntfs2btrfs
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake >= 3.14.3
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  cmake(fmt)
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(lzo2)
BuildRequires:  pkgconfig(libzstd)

# Adapted for specific use in this program, cannot be reasonably separated
Provides:       bundled(ntfs-3g-system-compression)

# Upstream doesn't have big endian support in the handwritten assembler
ExcludeArch:    ppc64 s390x

%description
ntfs2btrfs is a tool which does in-place conversion of Microsoft's NTFS
filesystem to the open-source filesystem Btrfs, much as btrfs-convert
does for ext2.

The original image is saved as a reflink copy at image/ntfs.img,
and if you want to keep the conversion you can delete this to
free up space.


%prep
%autosetup


%build
%cmake
%cmake_build

%install
%cmake_install


%files
%license LICENCE
%doc README.md
%{_sbindir}/ntfs2btrfs
%{_mandir}/man8/ntfs2btrfs.8*


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20210923-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Davide Cavalca <dcavalca@fedoraproject.org> - 20210923-2
- Rebuild for fmt soversion bump

* Sat Mar 12 2022 Neal Gompa <ngompa@fedoraproject.org> - 20210923-1
- Update to version 20210923

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20210523-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20210523-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 11 2021 Neal Gompa <ngompa13@gmail.com> - 20210523-1
- Update to version 20210523

* Fri Apr 02 2021 Neal Gompa <ngompa13@gmail.com> - 20210402-1
- Update to version 20210402 for improved altarch support

* Mon Mar 15 2021 Neal Gompa <ngompa13@gmail.com> - 20210105-1
- Initial packaging for Fedora (RH#1938464)
