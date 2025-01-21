# 2024-06-11
%global commit c84a596ce6ee653a326c35f98252fbe7d25c4305
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global plugin_dir %(%___build_pre; pkg-config --variable=plugin_dir audacious)

%global aud_plugin_api %(grep '[ ]*#define[ ]*_AUD_PLUGIN_VERSION[ ]\\+' %{_includedir}/libaudcore/plugin.h 2>/dev/null | sed 's!.*_AUD_PLUGIN_VERSION[ ]*\\([0-9]\\+\\).*!\\1!')
%if 0%{aud_plugin_api} > 0
%global aud_plugin_dep Requires: audacious(plugin-api)%{?_isa} = %{aud_plugin_api}
%endif


Name: xmp-plugin-audacious
Version: 4.0.0.3.8
Release: 0.2.20240611git%{shortcommit}%{?dist}
Summary: Multi-format module playback plugin for Audacious using libxmp
Source: https://github.com/mschwendt/xmp-plugin-audacious/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
License: GPL-2.0-or-later
URL: http://xmp.sourceforge.net/
BuildRequires: make
BuildRequires: libtool automake autoconf gcc-c++
BuildRequires: audacious-devel >= 3.8
BuildRequires: libxmp-devel

%description
.


%package -n audacious-plugins-xmp
Summary: Multi-format module playback plugin for Audacious using libxmp
%if 0%{?fedora}
%{?aud_plugin_dep}
%else
Requires: audacious
%endif
# added 2024-07-24
Provides: xmp-plugin-audacious = %{version}-%{release}
Obsoletes: xmp-plugin-audacious < 4.0.0.3.8

%description -n audacious-plugins-xmp
Audacious input plugin based on Extended Module Player (xmp) library.

Libxmp is a library that renders module files to PCM data. It supports
over 90 mainstream and obscure module formats including Protracker (MOD),
Scream Tracker 3 (S3M), Fast Tracker II (XM), and Impulse Tracker (IT).

Many compressed module formats are supported, including popular Unix, DOS,
and Amiga file packers including gzip, bzip2, SQSH, PowerPacker, etc.


%prep
%if 0%{?fedora}
# Enforce availability of the audacious(plugin-api) dependency.
%{!?aud_plugin_dep:echo 'No audacious(plugin-api) dependency!' && exit -1}
%endif

# just a guard
pkg-config --print-variables audacious | grep ^plugin_dir

%setup -qn %{name}-%{commit}
autoreconf -i

%build
%configure
make OPTFLAGS="%{optflags}" V=1 %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files -n audacious-plugins-xmp
%license COPYING
%{plugin_dir}/Input/*.so
#exclude %%{plugin_dir}/Input/*.la

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0.3.8-0.2.20240611gitc84a596
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Michael Schwendt <mschwendt@fedoraproject.org> - 4.0.0.3.8-0.1.20240611gitc84a596c
- Clean up snapshot stuff, and build audacious-plugins-xmp package.

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-0.35.20240611gitc84a596
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Michael Schwendt <mschwendt@fedoraproject.org> - 4.0.0-0.34.20240611gitc84a596c
- Fix settings on right side of dialog.

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-0.33.20160922git637d1e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-0.32.20160922git637d1e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-0.31.20160922git637d1e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-0.30.20160922git637d1e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-0.29.20160922git637d1e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jul 26 2021 Michael Schwendt <mschwendt@fedoraproject.org> - 4.0.0-0.28.20160922git
- Fix build for libxmp 4.5.0 EXPORT --> LIBXMP_EXPORT.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-0.27.20160922git637d1e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-0.26.20160922git637d1e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-0.25.20160922git637d1e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun  4 2020 Michael Schwendt <mschwendt@fedoraproject.org> - 4.0.0-0.24.20160922git637d1e0
- Escape macros in spec file comments.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-0.23.20160922git637d1e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-0.22.20160922git637d1e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-0.21.20160922git637d1e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Michael Schwendt <mschwendt@fedoraproject.org> - 4.0.0-0.20.20160922gitgit637d1e0
- add BuildRequires gcc-c++
- use %%license macro
- remove ancient Obsoletes

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-0.20.20160922git637d1e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-0.19.20160922git637d1e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Sep  3 2017 Michael Schwendt <mschwendt@fedoraproject.org> - 4.0.0-0.18.20160922gitgit637d1e0
- Rebuild for libaudcore SONAME bump.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-0.17.20160922git637d1e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-0.16.20160922git637d1e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-0.15.20160922git637d1e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 22 2016 Michael Schwendt <mschwendt@fedoraproject.org> - 4.0.0-0.14.20160922git637d1e0
- Patch for Audacious 3.8 plugin API.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-0.13.20141214git7a354bb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-0.12.20141214git7a354bb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.0.0-0.11.20141214git7a354bb
- Rebuilt for GCC 5 C++11 ABI change

* Tue Mar  3 2015 Michael Schwendt <mschwendt@fedoraproject.org> - 4.0.0-0.10.20141214git7a354bb
- Copy from Fedora Copr builds but keep old package versioning scheme
  for now.

* Sun Dec 14 2014 Michael Schwendt <mschwendt@fedoraproject.org>
- Fix 8-bit sample precision.

* Sun Dec 14 2014 Michael Schwendt <mschwendt@fedoraproject.org>
- Upgrade to preliminary fork for Audacious 3.6-alpha1.
- Plugin API version definition has moved to libaudcore header directory.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-0.9.20131127gitff91487
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-0.8.20131127gitff91487
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 27 2014 Michael Schwendt <mschwendt@fedoraproject.org>
- Add a guard for pkg-config based plugin_dir in %%prep

* Sun Apr 27 2014 Michael Schwendt <mschwendt@fedoraproject.org> - 4.0.0-0.7.20131127gitff01498
- pkgconfig input_plugin_dir is no longer, so use plugin_dir
  (this fixes #1091756 dir conflicts)

* Fri Feb 28 2014 Michael Schwendt <mschwendt@fedoraproject.org> - 4.0.0-0.6.20131127gitff01498
- Patch for Audacious 3.5-devel API.
- Update aud_plugin_api global to examine api.h header.

* Tue Feb 25 2014 Dominik Mierzejewski <rpm@greysector.net> - 4.0.0-0.5.20131127gitff91487
- updated to ff91487

* Sat Nov 16 2013 Dominik Mierzejewski <rpm@greysector.net> - 4.0.0-0.4.20131107gitfae5d38
- updated to fae5d38
- fixes spin button in preferences

* Wed Oct 30 2013 Dominik Mierzejewski <rpm@greysector.net> - 4.0.0-0.3.e0213c0
- updated to e0213c0
- dropped obsolete condition

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-0.2.8c492d7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Dominik Mierzejewski <rpm@greysector.net> - 4.0.0-0.1.8c492d7
- initial build based loosely on xmp.spec
