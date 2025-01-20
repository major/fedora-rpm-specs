%global with_snapshot   0
#%%global shortcommit     1552170
#%%global checkout        g%%{shortcommit}
#%%global upversion       1.3-4
%global postrelease     .post4
%global debug_package   %{nil}

Summary:        AMD Radeon video cards monitoring utility
Name:           radeontop
Version:        1.4
Release:        11%{?dist}
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://github.com/clbr/%{name}

Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         %{name}-no-rebuild.patch

BuildRequires:  asciidoc
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(pciaccess)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  sed

%description
RadeonTop is a monitoring utility for AMD Radeon cards from R600 and up.

%prep
%autosetup -p1 -n %{name}-%{version}%{?shortcommit:-%{checkout}}
sed -i -e 's/unknown/%{version}/' getver.sh

%build
%set_build_flags
%make_build 

%install
%make_install LIBDIR=%{_lib}
%find_lang %{name}

# Add AppStream metadata
install -Dm 0644 -p %{name}.metainfo.xml \
        %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%check
# Validate Appstream metadata
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{name}.metainfo.xml

%files -f %{name}.lang
%doc README.md 
%license COPYING
%{_bindir}/%{name}
# Workaround failure to build on /usr/lib64
%{_libdir}/lib%{name}_xcb.so
%{_mandir}/man1/%{name}.1*
#AppStream metadata
%{_metainfodir}/%{name}.metainfo.xml

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4-10
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 26 2021 Dominik Mierzejewski <rpm@greysector.net> - 1.4-2
- stop rebuilding binaries at make install

* Thu Nov 25 2021 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1.4-1
- Update to 1.4 (#2026535)

* Wed Nov 03 2021 Dominik Mierzejewski <rpm@greysector.net> - 1.3.post4-4g1552170
- Ensure Fedora build flags are used

* Sun Aug 15 2021 Luya Tshimbalanga <luya@fedoraproject.org> - 1.3.post4-3g1552170
- Latest snapshot
- Fix versioning according to the packaging guideline

* Thu Dec 10 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1.3-1
- Update to 1.3 (#1906240)

* Fri Oct 09 2020 Luya Tshimbalanga <luya@fedoraproject.org> 1.2-7.20200415gitef27e8
- Latest upstream git snapshot for better amdgpu support
- Add git dependency to detect versioning

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6.20191218gitf2d55d6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5.20191218gitf2d55d6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 24 2019 Luya Tshimbalanga <luya@fedoraproject.org> 1.2-4.20191218gitdf2d55d
- Latest upstream git snapshot
- Better description of the application

* Sun Oct 13 2019 Luya Tshimbalanga <luya@fedoraproject.org> 1.2-3
- Latest upstream git snapshot fixing AMD APU detection

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 04 2019 Luya Tshimbalanga <luya@fedoraproject.org> 1.2-1
- Update to 1.2
- Clean up spec

* Sun Jun 02 2019 Luya Tshimbalanga <luya@fedoraproject.org> 1.2-0.3.20181226git33f74f
- Update to 20181226 git snapshot which support newer AMD GPUS (VEGAM,VEGA12,VEGA20)
- Modernise spec

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.2.20181031git7474f50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 30 2018 Luya Tshimbalanga <luya@fedoraproject.org> 1.2-0.1.20181031git7474f50
- Update to 20181031 which support newer AMD APU and GPU

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Luya Tshimbalanga <luya@fedoraproject.org> 1.1-1
- Update to 1.1

* Sun Mar 04 2018 Luya Tshimbalanga <luya@fedoraproject.org> 1.0-20180106git07ec13
- Latest upstream git snapshot

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 05 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 1.0-5
- Add metainfo file

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 1.0-1
- Update to upstream 1.0

* Fri Nov 18 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 0.9-5.20161118gitc0abadf
- Latest git snapshot

* Thu Aug 25 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 0.9-4.20160825git6fb1c5c
- Latest git snapshot
- Added libxcb dependency

* Wed Jul 20 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 0.9-3.20160704gitbb3ed18
- Latest git snapshot

* Fri May 27 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 0.9-2.20160527git2047d13
- Fix Changelog in prescribed format.
- Remove obsolete Group field from spec

* Fri May 27 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 0.9-1.20160527git2047d13
- Update to upstream 0.9

* Sun Feb 15 2015 Fabian Deutsch <fabiand@fedoraproject.org> - 0.8-1.20150215git281462c
- Update to upstream 0.8

* Thu Apr 24 2014 Fabian Deutsch <fabiand@fedoraproject.org> - 0.7-2.20140421giteadc100
- Fix commit position, BuildRequirements, build, and man page inclusion (thanks mschwendt)

* Mon Apr 21 2014 Fabian Deutsch <fabiand@fedoraproject.org> - 0.7-1.20140421giteadc100
- Initial package

