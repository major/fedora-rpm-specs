Name:           xwayland-run
Version:        0.0.2
Release:        2%{?dist}
Summary:        Set of utilities to run headless X/Wayland clients

License:        GPL-2.0-or-later
URL:            https://gitlab.freedesktop.org/ofourdan/xwayland-run
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz

# From: https://gitlab.freedesktop.org/ofourdan/xwayland-run/-/merge_requests/4
Patch0001:      0001-wlheadless-Add-support-for-kwin.patch

BuildArch:      noarch

BuildRequires:  meson >= 0.60.0
BuildRequires:  git-core
BuildRequires:  python3-devel
Requires:       (weston or kwin-wayland or mutter or cage or gnome-kiosk)
Requires:       xorg-x11-server-Xwayland

# Provide names of the other utilities included
Provides:       wlheadless-run = %{version}-%{release}
Provides:       xwfb-run = %{version}-%{release}

%description
xwayland-run contains a set of small utilities revolving around running
Xwayland and various Wayland compositor headless.


%prep
%autosetup -S git_am


%build
%meson
%meson_build


%install
%meson_install


%files
%license COPYING
%doc README.md
%{_bindir}/wlheadless-run
%{_bindir}/xwayland-run
%{_bindir}/xwfb-run
%{_datadir}/wlheadless/
%{_mandir}/man1/wlheadless-run.1*
%{_mandir}/man1/xwayland-run.1*
%{_mandir}/man1/xwfb-run.1*
%{python3_sitelib}/wlheadless/


%changelog
* Sun Dec 10 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.0.2-2
- Refresh kwin support patch
- Add provides for other included utilities

* Sun Dec 10 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.0.2-1
- Initial package
