Name:		mp3gain
Version:	1.6.2

%global tarball_version %(echo %version|sed 's/\\./_/g')

Release:	15%{?dist}
Summary:	Lossless MP3 volume adjustment tool

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2+
URL:		http://mp3gain.sourceforge.net/
Source0:	https://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{tarball_version}-src.zip
# copied from Debian
Source1:	%{name}.1
Source2:	README.method
Patch2:		%{name}-cflags-1.5.2.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: mpg123-devel


%description
MP3Gain analyzes and adjusts mp3 files so that they have the same
volume. It does not just do peak normalization, as many normalizers
do. Instead, it does some statistical analysis to determine how loud
the file actually sounds to the human ear. Also, the changes MP3Gain
makes are completely lossless. There is no quality lost in the change
because the program adjusts the mp3 file directly, without decoding
and re-encoding.


%prep
%setup -q -c %{name}-%{tarball_version}
%patch -P2 -p0 -b .cflags
install -p -m 644 %{SOURCE2} .
sed -i 's/\r//' lgpl.txt


%build
%make_build


%install
install -Dp -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dp -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1


%files
%doc README.method
%license lgpl.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6.2-14
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 16 2019  Karel Volný <kvolny@redhat.com> - 1.6.2-2
- Import to Fedora (rhbz#1664399)
- Fixed License tag
- Dropped Group tag
- Improved tarball_version definition
- Unzipped manpage

* Wed Jan 02 2019 Sérgio Basto <sergio@serjux.com> - 1.6.2-1
- Update to 1.6.2
- Add BuildRequires: gcc

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 30 2018 Sérgio Basto <sergio@serjux.com> - 1.6.1-1
- Update to 1.6.1
- Drop upstreamed patch
- Update spec

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.5.2-4
- Mass rebuilt for Fedora 19 Features

* Wed Jan 25 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 28 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.5.2-2
- Fix for glibc bug rhbz#747377

* Tue Oct 04 2011 Karel Volný <kvolny@redhat.com> - 1.5.2-1
- Version bump.
- Updated the tempfile and cflags patches.
- Removed the exit patch (applied upstream).

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.4.6-6
- rebuild for new F11 features

* Mon Aug 04 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 1.4.6-5
- rebuild

* Tue Nov 28 2006 Brian Pepple <bpepple@fedoraproject.org> - 1.4.6-4
- Bump.

* Sun Nov 26 2006 Brian Pepple <bpepple@fedoraproject.org> - 1.4.6-3
- D'Oh! Add HAVE_MEMCPY back to cflag patch.

* Sun Nov 26 2006 Brian Pepple <bpepple@fedoraproject.org> - 1.4.6-2
- Update cflags patch to use RPM_OPT_FLAGS.

* Mon Nov 20 2006 Brian Pepple <bpepple@fedoraproject.org> - 1.4.6-1
- Initial Livna spec.
