%define _legacy_common_support 1

Name:		bspwm
Version:	0.9.9
Release:	16%{?dist}
Summary:	A tiling window manager based on binary space partitioning

# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		https://github.com/baskerville/bspwm
Source0:	%{url}/archive/%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	xcb-util-devel
BuildRequires:	xcb-util-wm-devel
BuildRequires:	xcb-util-keysyms-devel
BuildRequires:	desktop-file-utils
BuildRequires: make


%description
bspwm is a tiling window manager that represents windows as the leaves of a
full binary tree.

It only responds to X events, and the messages it receives on a dedicated
socket.

bspc is a program that writes messages on bspwm's socket.

bspwm doesn't handle any keyboard or pointer inputs: a third party program
(e.g. sxhkd) is needed in order to translate keyboard and pointer events to
bspc invocations.


%prep
%setup -q


%build
make VERBOSE=1 %{?_smp_mflags} CFLAGS="%{optflags}" \
	LDFLAGS="%{?__global_ldflags}"


%install
%make_install PREFIX="%{_prefix}"


%check
desktop-file-validate %{buildroot}/%{_datadir}/xsessions/%{name}.desktop


%files
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/bspc
%{_docdir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/man1/bspc.1.gz
%{_datadir}/bash-completion/completions/bspc
%{_datadir}/zsh/site-functions/_bspc
%{_datadir}/fish/vendor_completions.d/bspc.fish
%{_datadir}/xsessions/%{name}.desktop


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.9-15
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Jeff Law <law@redhat.com> - 0.9.9-4
- Enable legacy common support

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 5 2019 Oles Pidgornyy <pidgornyy@informatik.uni-frankfurt.de> - 0.9.9-1
- Update to 0.9.9

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 18 2017 Oles Pidgornyy <pidgornyy@informatik.uni-frankfurt.de> - 0.9.2-1
- Update to 0.9.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Mar 15 2016 Oles Pidgornyy <pidgornyy@informatik.uni-frankfurt.de> - 0.9.1-1
- Update to 0.9.1
- Fix compliance to freedesktop specifications

* Sat Mar 12 2016 Oles Pidgornyy <pidgornyy@informatik.uni-frankfurt.de> - 0.9-1
- Initial release
