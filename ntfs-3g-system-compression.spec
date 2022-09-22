Name:     ntfs-3g-system-compression
Summary:  NTFS-3G plugin for reading "system compressed" files
Version:  1.0
Release:  10%{?dist}
License:  GPLv2+
URL:      https://github.com/ebiggers/ntfs-3g-system-compression
Source0:  https://github.com/ebiggers/ntfs-3g-system-compression/archive/v%{version}/ntfs-3g-system-compression-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(libntfs-3g) >= 2017.3.23
BuildRequires:  fuse-devel

%description
System compression, also known as "Compact OS", is a Windows feature that
allows rarely modified files to be compressed using the XPRESS or LZX
compression formats. It is not built directly into NTFS but rather is
implemented using reparse points. This feature appeared in Windows 10 and it
appears that many Windows 10 systems have been using it by default.

This RPM contains a plugin which enables the NTFS-3G FUSE driver to
transparently read from system-compressed files. Currently, only reading is
supported. Compressing an existing file may be done by using the "compact"
utility on Windows.

%prep
%autosetup

%build
autoreconf -i
%configure
%make_build

%install
%make_install
rm -rf %{buildroot}%{_libdir}/ntfs-3g/*.la

%files
%doc README.md
%license COPYING
%dir %{_libdir}/ntfs-3g/
%{_libdir}/ntfs-3g/ntfs-plugin-80000017.so

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 08 2022 Richard W.M. Jones <rjones@redhat.com> - 1.0-9
- Rebuild for ntfs-3g CVE

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 31 2021 Richard W.M. Jones <rjones@redhat.com> - 1.0-7
- Rebuild for updated ntfs-3g CVE (RHBZ#1999788)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 26 2019 Kamil Páral <kparal@redhat.com> - 1.0-1
- initial package
