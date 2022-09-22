%global _hardened_build 1

Name:           sng
Version:        1.1.0
Release:        15%{?dist}
Summary:        Lossless editing of PNGs via a textual representation

License:        zlib
URL:            http://sng.sourceforge.net/
Source0:        http://sourceforge.net/projects/sng/files/sng-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  grep
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
BuildRequires:  /usr/share/X11/rgb.txt

Requires:       /usr/share/X11/rgb.txt

%description
SNG (Scriptable Network Graphics) is a minilanguage designed
specifically to represent the entire contents of a PNG (Portable
Network Graphics) file in an editable form. Thus, SNGs representing
elaborate graphics images and ancillary chunk data can be readily
generated or modified using only text tools.

SNG is implemented by a compiler/decompiler called sng that losslessly
translates between SNG and PNG.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%check
# Upstream has a test suite, but the test files are not packaged.
# Let's just check on the files that are in the tarball.
./sng_regress *.png *.sng

%files
%license COPYING
%doc NEWS README TODO
%doc %_mandir/man1/sng.1*
%_bindir/sng

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.0-2
- Require rgb.txt also at runtime

* Wed Nov 16 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.0-1
- Initial packaging
