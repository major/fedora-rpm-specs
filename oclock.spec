Name:       oclock
Version:    1.0.4
Release:    5%{?dist}
Summary:    A simple analog clock

License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.gz
Source1:    %{name}-%{version}.tar.gz.sig
# Keyring copied on 2023-02-26 from: xfontsel.gpg
Source2:        %{name}.gpg
BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  xorg-x11-util-macros
BuildRequires:  gnupg2

Obsoletes:  xorg-x11-apps < 7.7-31

%description
oclock is a simple analog clock using the SHAPE extension to make
a round (possibly transparent) window.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
autoreconf -v --install
%configure --disable-silent-rules
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/X11/app-defaults/Clock-color

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat May 06 2023 Ranjan Maitra <aarem@fedoraproject.org> - 1.0.4-4
- Rebuild for F38
- Submitted to repos, after unretiring.

* Sun Feb 26 2023 Ranjan Maitra <aarem@fedoraproject.org> - 1.0.4-3
- Rebuild for F37
- Copied and renamed oclock.gpg from xfontsel.gpg and provided verification

* Fri Nov 19 2021 Ranjan Maitra <aarem@fedoraproject.org> - 1.0.4-2
- Rebuild for F35. 

* Thu Apr 08 2021 Peter Hutterer <peter.hutterer@redhat.com> - 1.0.4-2
- Fix Obsoletes line to actually obsolete the -30 xorg-x11-apps (#1947245)

* Tue Mar 02 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.0.4-1
- Split oclock out from xorg-x11-apps into a separate package (#1933935)
