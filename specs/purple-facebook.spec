# Filter provides from plugins.
%if 0%{?fedora} || 0%{?rhel} >= 7
%global __provides_exclude_from ^%{_libdir}/.*$
%else
%filter_provides_in %{_libdir}/.*\.so$
%filter_setup
%endif


Name:           purple-facebook
Version:        0.9.6
Release:        21%{?dist}
Summary:        Facebook protocol plugin for purple2

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/dequis/%{name}
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz

# Backported from upstream.
# https://github.com/dequis/purple-facebook/tree/wip-work-chat
Patch0000:      %{name}-0.9.6-fb-work-chat.patch
# https://github.com/dequis/purple-facebook/commit/b689527f7a48
Patch0001:      %{name}-0.9.6-include_case_6_for_optional_thrift_fields.patch
# https://github.com/dequis/purple-facebook/commit/868f4e3025d6
Patch0002:      %{name}-0.9.6-fix_taNewMessage.patch
# https://github.com/dequis/purple-facebook/commit/3f4e9500bed9
Patch0003:      %{name}-0.9.6-bump_FB_ORCA_AGENT_version.patch

# Backported from upstream pull-requests.
# https://github.com/dequis/purple-facebook/pull/414
Patch1000:      %{name}-0.9.6-option-show-inactive-as-away.patch

# Downstream
# GLib deprecation warnings.
Patch2000:      %{name}-0.9.6-g_type_class_add_private.patch
Patch2001:      %{name}-0.9.6-g_memdup.patch
Patch2002:      %{name}-0.9.6-G_TYPE_INSTANCE_GET_PRIVATE.patch
# GCC-15 / C23
Patch2003:	%{name}-0.9.6-Wincompatible-pointer-types.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  glib2-devel      >= 2.28
BuildRequires:  json-glib-devel  >= 0.14
BuildRequires:  libpurple-devel   < 3.00
BuildRequires:  zlib-devel

%description
Purple Facebook implements the Facebook Messenger protocol for pidgin,
finch, and libpurple.  While the primary implementation is for purple3,
this plugin is back-ported for purple2.

This project is not affiliated with Facebook, Inc.


%prep
%autosetup -p 1


%build
touch aclocal.m4 configure Makefile.am Makefile.in
%configure               \
  --disable-silent-rules \
  --enable-warnings
%make_build


%install
%make_install
find %{buildroot}%{_libdir} -name '*.*a' -print -delete


%check
%make_build check


%files
%license AUTHORS COPYING debian/copyright
%doc ChangeLog README
%{_libdir}/purple-2/libfacebook.so


%changelog
* Thu Jan 23 2025 Björn Esser <besser82@fedoraproject.org> - 0.9.6-21
- Add several patches to avoid deprecation warnings
- Add patch to fix build with GCC-15 / C23
  Fixes rhbz#2341118

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.6-19
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jan 8 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 0.9.6-14
- Fix flatpak build

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct 13 2021 Björn Esser <besser82@fedoraproject.org> - 0.9.6-10
- Update Patch2 to fix Failed to read thrift / assertion 'id == 2' failed
  See: https://github.com/dequis/purple-facebook/commit/1a6711f83d62

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Björn Esser <besser82@fedoraproject.org> - 0.9.6-7
- Add patch fixing taNewMessage bug
- Add patch bumping FB_ORCA_AGENT version

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Apr 05 2020 Björn Esser <besser82@fedoraproject.org> - 0.9.6-5
- Add patch fixing login issues

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 13 2019 Björn Esser <besser82@fedoraproject.org> - 0.9.6-1
- New upstream release
- Remove patches being applied upstream
- Refactor left patches for alignment

* Mon Jan 07 2019 Björn Esser <besser82@fedoraproject.org> - 0.9.5-13.9ff9acf9fa14
- Add patch to check and link zlib

* Mon Jan 07 2019 Björn Esser <besser82@fedoraproject.org> - 0.9.5-12.9ff9acf9fa14
- Add patch from upstream fixing 'Failed to get sync_sequence_id' (#1663599)

* Sat Oct 13 2018 Björn Esser <besser82@fedoraproject.org> - 0.9.5-11.9ff9acf9fa14
- Backported upstream patch for Facebook Work Chat

* Sat Oct 13 2018 Björn Esser <besser82@fedoraproject.org> - 0.9.5-10.9ff9acf9fa14
- Optimize sortability of patches
- Refactor patches for smooth alignment
- Remove empty line from spec file

* Fri Oct 05 2018 Björn Esser <besser82@fedoraproject.org> - 0.9.5-9.9ff9acf9fa14
- Update Patch101 to match upstream PR

* Thu Oct 04 2018 Björn Esser <besser82@fedoraproject.org> - 0.9.5-8.9ff9acf9fa14
- Backported pull-request fixing compiler warnings

* Thu Oct 04 2018 Björn Esser <besser82@fedoraproject.org> - 0.9.5-7.9ff9acf9fa14
- Add disclaimer to %%description

* Thu Oct 04 2018 Björn Esser <besser82@fedoraproject.org> - 0.9.5-6.9ff9acf9fa14
- Backported pull-request adding an option to show inactive friends as away

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-5.9ff9acf9fa14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 23 2018 Björn Esser <besser82@fedoraproject.org> - 0.9.5-4.9ff9acf9fa14
- Add patch from upstream fixing connection problem with TLS 1.3
- Add patch from upstream fixing another segfault with newer glib

* Wed Mar 21 2018 Björn Esser <besser82@fedoraproject.org> - 0.9.5-3.9ff9acf9fa14
- Add two patches from upstream fixing segfault with newer glib

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-2.9ff9acf9fa14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 Björn Esser <besser82@fedoraproject.org> - 0.9.5-1.9ff9acf9fa14
- New upstream release (rhbz#1487200)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-6.c9b74a765767
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-5.c9b74a765767
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.9.4-4.c9b74a765767
- Rebuild due to bug in RPM (RHBZ #1468476)

* Thu Jun 15 2017 Björn Esser <besser82@fedoraproject.org> - 0.9.4-3.c9b74a765767
- Properly run %%filter_setup

* Thu Jun 15 2017 Björn Esser <besser82@fedoraproject.org> - 0.9.4-2.c9b74a765767
- Filter provides from plugins on el6, too

* Mon Jun 12 2017 Björn Esser <besser82@fedoraproject.org> - 0.9.4-1.c9b74a765767
- New upstream release (rhbz#1460505)
- Filter provides from plugins

* Thu Mar 30 2017 Björn Esser <besser82@fedoraproject.org> - 0.9.3-1.c9b74a765767
- New upstream release (rhbz#1437164)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0.20160409-0.5.git66ee773
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct 16 2016 Björn Esser <fedora@besser82.io> - 0.0.0.20160409-0.4.git66ee773
- Initial import (rhbz 1385180)

* Sun Oct 16 2016 Björn Esser <fedora@besser82.io> - 0.0.0.20160409-0.3.git66ee773
- Minor change for building on el6 's!%%{_bindir}/echo!/bin/echo!'

* Sun Oct 16 2016 Björn Esser <me@besser82.io> - 0.0.0.20160409-0.2.git66ee773
- Move commit-sha to to Release-tag (rhbz 1385180)
- Update %%description 's!into pidgin!for pidgin!' (rhbz 1385180)

* Fri Oct 14 2016 Björn Esser <fedora@besser82.io> - 0.0.0.20160409.66ee77378d82-0.1
- Initial package (rhbz 1385180)
