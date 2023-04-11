%global dracutdir %(pkg-config --variable=dracutdir dracut)

Name:           twincam
Version:        0.6
Release:        4%{?dist}
Summary:        A lightweight camera application

License:        GPLv2
URL:            https://github.com/ericcurtin/twincam
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(libevent_pthreads)
BuildRequires:  pkgconfig(libcamera)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  SDL2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  systemd

# twincam is not expected to be used in these architectures
ExcludeArch: s390x ppc64le %ix86

%description
A lightweight camera application, designed to start quickly in a bare
environment. It is named twincam as it is built with automotive in mind like a
twin-cam engine, it is simply the name of the application.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

mkdir -p %{buildroot}%{dracutdir}/modules.d/81twincam
mkdir -p %{buildroot}%{_unitdir}/sysinit.target.wants
mkdir -p %{buildroot}%{_unitdir}/multi-user.target.wants
install -m644 lib/dracut/modules.d/81twincam/module-setup.sh %{buildroot}%{dracutdir}/modules.d/81twincam/
install -m644 lib/systemd/system/twincam-quit.service %{buildroot}%{_unitdir}/
install -m644 lib/systemd/system/twincam.service %{buildroot}%{_unitdir}/
ln -sf ../twincam.service %{buildroot}%{_unitdir}/sysinit.target.wants/
ln -sf ../twincam-quit.service %{buildroot}%{_unitdir}/multi-user.target.wants/

%check
%meson_test

%post
dracut -f

%files
%license COPYING
%doc README.md
%{_bindir}/twincam
%{dracutdir}/modules.d/81twincam/module-setup.sh
%{_unitdir}/twincam.service
%{_unitdir}/twincam-quit.service
%{_unitdir}/sysinit.target.wants/twincam.service
%{_unitdir}/multi-user.target.wants/twincam-quit.service

%changelog
%autochangelog
