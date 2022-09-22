Name:         bicon
License:      LGPLv2+ and Python
Version:      0.5
Release:      16%{?dist}
Summary:      Bidirectional Console
Source:       https://github.com/behdad/bicon/releases/download/%{version}/%{name}-%{version}.tar.gz
URL:          https://www.arabeyes.org/Bicon

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: fribidi-devel
BuildRequires: kbd
BuildRequires: libtool
BuildRequires: make
Requires:      kbd
Requires:      setxkbmap
Requires:      xkbcomp

%description
BiCon is the bidirectional console as presented by Arabeyes.

%package devel
Summary:        Development Libraries for BiCon
Requires:       %{name} = %{version}-%{release}

%description devel
The bicon-devel package contains the libraries and header files
that are needed for writing applications with BiCon.

%package fonts
Summary:        Font Files for BiCon
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description fonts
The bicon-fonts package contains the font files for BiCon.

%package keymaps
Summary:        Keymap Files for BiCon
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description keymaps
The bicon-keymaps package contains the keymap files for BiCon.

%prep
%setup -q

%build
libtoolize
autoreconf --verbose --force --install
%configure \
  --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p" install

rm -f $RPM_BUILD_ROOT%{_libdir}/bicon/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/bicon/*.a

%files
%doc AUTHORS COPYING README
%{_bindir}/*
%{_libdir}/bicon/*.so.*
%dir %{_datadir}/%{name}
%{_datadir}/man/man1/*.gz

%files devel
%{_includedir}/*
%{_libdir}/bicon/*.so
%{_libdir}/pkgconfig/*.pc

%files fonts
%{_datadir}/%{name}/font

%files keymaps
%{_datadir}/%{name}/keymap

%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Adam Jackson <ajax@redhat.com> - 0.5-12
- Require setxkbmap and xkbcomp not xorg-x11-xkb-utils

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Aug 26 2015 Takao Fujiwara <tfujiwar@redhat.com> - 0.5-1
- Bumped to 0.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 29 2014 Takao Fujiwara <tfujiwar@redhat.com> - 0.4-1
- Bumped to 0.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 04 2013 Takao Fujiwara <tfujiwar@redhat.com> - 0.2.0-6
- Added autoreconf to use autoconf 2.69 or later. BZ#925094

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 20 2011 Takao Fujiwara <tfujiwar@redhat.com> - 0.2.0-1
- Initial release. Bug 670090.
