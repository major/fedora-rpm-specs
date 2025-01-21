Name:		vlfrx-tools
Version:	0.9m
Release:	9%{?dist}
Summary:	VLF Receiver Software Toolkit
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		http://www.abelian.org/vlfrx-tools/
Source0:	http://www.abelian.org/%{name}/%{name}-%{version}.tgz
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	alsa-lib-devel
BuildRequires:	libvorbis-devel
BuildRequires:	flac-devel
BuildRequires:	libX11-devel
BuildRequires:	libpng-devel
BuildRequires:	libXpm-devel
BuildRequires:	ncurses-devel
BuildRequires:	xforms-devel
BuildRequires:	libshout-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	fftw-devel
Requires:	sox
Requires:	gnuplot

%description
Designed for VLF radio signal processing, it also has applications for meteor
forward scatter, seismographic and natural radioactivity recording, ELF and
magnetometers, radio astronomy, bat detection, amateur radio, and other
projects which require precision timestamps preserved through signal capture,
storage, and post-processing.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install bindir=%{buildroot}%{_bindir}

%files
%{_bindir}/vt*
%doc README changelog

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9m-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep  4 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9m-8
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9m-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9m-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9m-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9m-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep 15 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9m-3
- Rebuild for new flac

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9m-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun  6 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.9m-1
- New version

* Thu May 26 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.9j-1
- Initial version
