Summary: FUSE filesystem to transcode FLAC to MP3 on the fly
Name: mp3fs
Version: 1.1.1
Release: 13%{dist}
# Automatically converted from old format: GPLv3+ and GFDL - review is highly recommended.
License: GPL-3.0-or-later AND LicenseRef-Callaway-GFDL
Source0: https://github.com/khenriks/mp3fs/releases/download/v%{version}/mp3fs-%{version}.tar.gz
URL: https://khenriks.github.io/mp3fs/
# While mp3fs does encode to MP3, it is a consumer, not a provider
#Provides: mp3encoder
# While mp3fs does not strictly require the fuse cli (which does not provide
# the fuse libraries), mp3fs is fairly useless without it.
Requires: fuse
BuildRequires: make
BuildRequires: fuse-devel lame-devel flac-devel libid3tag-devel gcc-c++
BuildRequires: libvorbis-devel
BuildRequires: zlib-devel

%description
MP3FS is A read-only FUSE file-system which trans-codes audio formats (currently
FLAC/OGG) to MP3 on the fly when opened and read. This was written to enable me
to use my FLAC collection with software and/or hardware which only understands
MP3. e.g. "GMediaServer" to a Netgear MP101 mp3 player.

It is also a novel alternative to traditional mp3 encoder applications. Just
use your favorite file browser to select the files you want encoded and copy
them somewhere!

%prep
%setup -q 

%build
%configure
%{make_build} LDFLAGS="$RPM_LD_FLAGS -lm" V=1

%install
%make_install

%files
%{!?_licensedir:%global license %%doc}
%license COPYING COPYING.DOC
%doc README.md INSTALL.md NEWS.md
%{_bindir}/%{name}
%{_mandir}/man1/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.1-12
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Sep 18 2022 Todd Zullinger <tmz@pobox.com> - 1.1.1-6%{dist}
- fix project URL

* Wed Sep 14 2022 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.1.1-5
- Rebuilt for flac 1.4.0
- Explicitly BR zlib-devel

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 17 2021 Stuart Gathman <stuart@gathman.org> 1.1.1-1
- New upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 30 2020 Stuart Gathman <stuart@gathman.org> 1.0-1
- New upstream release

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.91-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.91-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.91-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.91-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.91-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild
>>>>>>> f6527555a6483a34143acdaac711586a721ab060

* Mon Jun  4 2018 Stuart Gathman <stuart@gathman.org> 0.91-7
- Rebuilt to move from rpmfusion to Fedora, since dependencies have moved

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.91-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.91-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.91-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 26 2016 Stuart Gathman <stuart@gathman.org> 0.91-3
- Remove space from Summary:
- Include $RPM_LD_FLAGS in LDFLAGS
- Removed mp3encoder provides, not useful apparently

* Tue Oct 18 2016 Stuart Gathman <stuart@gathman.org> 0.91-2
- Clean up to resubmit to rpmfusion.

* Sat Jan 24 2015 Stuart Gathman <stuart@gathman.org> 0.91-1
- Update to 0.91 on Fedora 19

* Wed Oct 10 2012 Stuart Gathman <stuart@gathman.org> 0.32-1
- Update to 0.32 on Fedora 16

* Tue Jun 29 2010 Stuart Gathman <stuart@gathman.org> 0.20-1
- Update to 0.20 on Fedora 12

* Fri Oct 19 2007 Stuart Gathman <stuart@gathman.org> 0.13-1
- Update to 0.13 on Centos5

* Fri Oct 19 2007 Stuart Gathman <stuart@gathman.org> 0.11-1
- Update to 0.11 on Centos5

* Wed Nov 22 2006 Stuart Gathman <stuart@gathman.org> 0.03-2
- Rebuild with fuse-2.6

* Wed Nov  1 2006 Stuart Gathman <stuart@gathman.org> 0.03-1
- RPM 
